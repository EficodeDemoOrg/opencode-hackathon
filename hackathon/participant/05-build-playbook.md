Build Playbook
===
You have about 85 minutes to build, then 40 to test and measure. Build the **smallest thing that lets you run your test plan**. Your proposal is the spec: the guardrails you promised are part of the deliverable, not decoration.

# Work in this order
| Step | Time | Do | Done when |
|---|---:|---|---|
| 1. Skeleton | 15 min | Create the agent/command/skill files from the nearest existing example (table below). Get one end-to-end run on **fixture data**. | A run produces output |
| 2. Guardrails | 15 min | Write the permissions from your proposal's matrix. **Try to break them**: ask the agent to do each forbidden thing. | Every "no" in your matrix is denied, and you saw it |
| 3. Verification | 15 min | Add the automatic checks (tests, reviewer sub-agent, report format with open questions and suspicious content). | A wrong output is caught before a human sees it |
| 4. Real inputs | 20 min | Switch from fixtures to the sandbox Jira/Bitbucket. Run on your test-plan inputs. | 3+ real cases run |
| 5. Harden | 20 min | Fix what failed. Add the adversarial case (planted instruction in a ticket). | Adversarial case ignored and reported |

**At 16:10 stop building** and move to the test phase with whatever works.

# Start from the closest example
| You are building | Start from |
|---|---|
| a read-only role that fetches and summarises | `.opencode/agents/atlassian-reader.md` |
| a role limited to certain files | `test-writer` (in `preparation/deliver_ship/agents`) |
| a read-only reviewer | `code-reviewer` |
| an orchestrator with a loop and limits | `deliver` |
| a procedure with a fixed output shape | `.opencode/skills/jira-issues/SKILL.md` |
| a command that triggers a sub-agent | `.opencode/commands/jira.md` |
| a command that composes a sub-agent and a skill | `.opencode/commands/spec-from-jira.md` |

Run `./scripts/stage-demo.sh` first if you do not see `deliver`, `test-writer` and friends in `.opencode/`.

# Atlassian access
```bash
export ATLASSIAN_FIXTURES=tools/atlassian/fixtures      # canned data, no credentials
# or the sandbox: see tools/atlassian/README.md
java tools/atlassian/Atlassian.java jira get INV-143
```
Set variables in the shell you launch `opencode` from. Never paste a token anywhere.

# Rules of the road
- **One role, one lane.** If you give an agent more rights to get past a problem, write it into the proposal as a risk acceptance and tell the instructor.
- **Denied means report.** Do not look for another route.
- **The last matching rule wins.** Put `*` denials before exceptions. Repeat critical denials in agents.
- **Check for a second route.** If `read` of a file is denied, is there a shell command that reads it?
- **Agents never commit.** You do, after reading the diff. The hook wants `INV-123: subject` and a `Reviewed-by:` trailer.
- **Keep a log** of anything surprising (the agent obeyed something it read, a rule did not hold, a wrong answer that looked right). It is a result.

# When stuck, in this order
1. Read the error or the denial out loud. What exactly was refused?
2. Open the rules and find the **last** one that matches.
3. Share your screen with your team, then ask the floater.
4. If a model is slow, work on the test plan and the results form while it runs.

# Definition of done
- [ ] Runs end to end on at least three realistic inputs.
- [ ] Every "no" in the proposal's permission matrix was tried and denied.
- [ ] A human-review step exists and is recorded.
- [ ] A negative test and an adversarial test have been run.
- [ ] You know how to turn it off.
- [ ] Results recorded in the [results form](06-results-form.md).
