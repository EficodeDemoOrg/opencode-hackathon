import { Plugin } from "@opencode/plugin"
import { exec } from "node:child_process"
import { readFileSync } from "node:fs"

const RULES = [
  { name: "AWS access key", pattern: /AKIA[0-9A-Z]{16}/ },
  { name: "private key", pattern: /-----BEGIN [A-Z ]*PRIVATE KEY-----/ },
  { name: "hard-coded password", pattern: /password\s*[=:]\s*\S+/i },
]

// Runs a command in a folder and resolves with what it printed; never throws.
function run(command: string, cwd: string): Promise<string> {
  return new Promise((resolve) =>
    exec(command, { cwd, maxBuffer: 16 * 1024 * 1024 }, (_error, stdout) => resolve(stdout)),
  )
}

// Blocks any `git commit` the agent tries if the changes contain something that looks like a secret.
export default Plugin.define({
  id: "secret-scan",
  async setup(ctx) {
    const directory = ctx.location.directory

    await ctx.tool.hook("execute.before", async (event) => {
      if (event.tool !== "shell") return
      const command = String((event.input as { command?: string }).command ?? "")
      if (!/\bgit\s+commit\b/.test(command)) return

      // Scan everything that could end up in the commit, not only what is staged:
      // `git add -A && git commit ...` is one command, so nothing is staged yet when this runs.
      const lines: { file: string; text: string }[] = []

      let file = ""
      const diff = await run("git diff HEAD", directory)
      for (const line of diff.split("\n")) {
        if (line.startsWith("+++ b/")) file = line.slice(6)
        else if (line.startsWith("+") && !line.startsWith("+++")) lines.push({ file, text: line })
      }

      const untracked = await run("git ls-files --others --exclude-standard", directory)
      for (const path of untracked.split("\n").filter(Boolean)) {
        const content = readFileSync(`${directory}/${path}`, "utf8")
        for (const text of content.split("\n")) lines.push({ file: path, text })
      }

      const findings = new Set<string>()
      for (const rule of RULES) {
        for (const line of lines) {
          if (rule.pattern.test(line.text)) findings.add(`${rule.name} in ${line.file}`)
        }
      }

      if (findings.size > 0) {
        throw new Error(
          "secret-scan: this commit was blocked because it looks like it contains secrets:\n" +
            [...findings].map((finding) => `  - ${finding}`).join("\n") +
            "\nRemove the secret (or add the file to .gitignore) and commit again. Do not try to bypass this check.",
        )
      }
    })
  },
})
