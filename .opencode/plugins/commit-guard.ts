import { Plugin } from "@opencode/plugin"
import { exec } from "node:child_process"

// Runs a command in a folder. Resolves with whether it succeeded and what it printed; never throws.
function run(command: string, cwd: string): Promise<{ ok: boolean; output: string }> {
  return new Promise((resolve) =>
    exec(command, { cwd, maxBuffer: 16 * 1024 * 1024 }, (error, stdout, stderr) =>
      resolve({ ok: !error, output: stdout + stderr }),
    ),
  )
}

// Runs the test suite before every `git commit` the agent tries, and blocks the commit if it fails.
export default Plugin.define({
  id: "commit-guard",
  async setup(ctx) {
    const directory = ctx.location.directory

    await ctx.tool.hook("execute.before", async (event) => {
      if (event.tool !== "shell") return
      const command = String((event.input as { command?: string }).command ?? "")
      if (!/\bgit\s+commit\b/.test(command)) return

      const result = await run("mvn -q test", directory)
      if (!result.ok) {
        const tail = result.output.split("\n").slice(-40).join("\n")
        throw new Error(
          "commit-guard: the test suite failed, so this commit was blocked.\n" +
            "Fix the failing tests, then commit again.\n\n" +
            tail,
        )
      }
    })
  },
})
