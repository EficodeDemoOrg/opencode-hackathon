import { Plugin } from "@opencode/plugin"
import { exec } from "node:child_process"
import { appendFileSync } from "node:fs"

// Runs a command in a folder and resolves with what it printed; never throws.
function run(command: string, cwd: string): Promise<string> {
  return new Promise((resolve) =>
    exec(command, { cwd, maxBuffer: 16 * 1024 * 1024 }, (_error, stdout) => resolve(stdout.trim())),
  )
}

// After every successful `git commit` by the agent, records how much it changed.
export default Plugin.define({
  id: "commit-stats",
  async setup(ctx) {
    const directory = ctx.location.directory

    await ctx.tool.hook("execute.after", async (event) => {
      if (event.tool !== "shell" || event.status !== "completed") return
      const command = String((event.input as { command?: string }).command ?? "")
      if (!/\bgit\s+commit\b/.test(command)) return
      const printed = String((event.result.output as { output?: string } | undefined)?.output ?? "")
      if (!/\d+ files? changed/.test(printed)) return // the commit did not happen

      const summary = await run('git log -1 "--format=%h %s"', directory)
      const stat = await run("git diff --shortstat HEAD~1 HEAD", directory)
      const entry = `${new Date().toISOString()}  ${summary}  |  ${stat}`

      appendFileSync(`${directory}/.opencode/commit-stats.log`, entry + "\n")

      // `content` is what the model reads: a string, or a list of content parts.
      const content = event.result.content
      event.result = {
        ...event.result,
        content: [
          ...(typeof content === "string" ? [{ type: "text" as const, text: content }] : (content ?? [])),
          { type: "text" as const, text: `[commit-stats] ${stat}` },
        ],
      }
    })
  },
})
