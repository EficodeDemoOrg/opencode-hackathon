Build, Test and Measure
===
Your job here is to **unblock, not to build**. Keep teams honest about their targets and make sure the measurements get recorded.

# Checkpoints
Post these in the main chat at the clock times (adjust to your start).
| Clock | Checkpoint        | Ask each team                                                    |
|-------|-------------------|------------------------------------------------------------------|
| 13:00 | Skeleton )        | "Do you have one end-to-end run, even on fixtures?"              |
| 13:15 | **Guardrails**    | "Have you *tried* every 'no' in your matrix and seen it denied?" |
| 14:00 | **Real inputs**   | "Have you run on sandbox data yet? Is the baseline timed?"       |
| 14:15 | **Adversarial**   | "Have you planted a hostile instruction and run it?"             |
| 15:00 | **Stop building** | "All should be testing, now. Run the plan on what you have."     |
| 15:30 | Results           | "Part B of the form needs filling. Need to prep story for CAB."  |
| 16:00 | Hard stop         | "Submit the form. Time to face the CAB"                          |

# Early finishers
Move them on, do not let them idle: run the test plan, add a second adversarial case, try to **break a colleague's guardrail** (pair with another finished team), or write the "reusable pieces" notes for the master document.

# Triage
| Symptom | Likely cause | Fix |
|---|---|---|
| Agent "can't find" the Atlassian tool, or asks for permission every time | Rule text does not match the command, or a later rule overrides it | Open `opencode.json`; find the **last** rule that matches the exact command. The allow is `java tools/atlassian/Atlassian.java *` |
| `Environment variable ... is not set` | Variable set in a different shell than the one that started opencode, or opencode started from a GUI | Export in the launching shell and restart opencode |
| `No fixture for this request` | `ATLASSIAN_FIXTURES` not set, or a ticket/repo that has no fixture file | Add a fixture file at the printed path, or switch to the sandbox |
| `HTTP 401/403` | Wrong auth type for Cloud vs Data Center, expired or wrongly scoped token | Cloud: `JIRA_EMAIL` + API token. Data Center: `JIRA_FLAVOR=server` + PAT. Check token scopes |
| `HTTP 404` on a Bitbucket file | Wrong branch | `--ref` or `BITBUCKET_DEFAULT_BRANCH` |
| `Refusing redirect to another host` | A deliberate tool guardrail tripped (the API redirected off-host) | Check the base URL; do not remove the check |
| Sub-agent returns "denied" for something it should do | Its `*` deny is placed after its allows | Put `*` denials first |
| Sub-agent ignores the skill | Skill not allowed for that agent, or the description is vague | Allow the skill in its permissions; rewrite the description to say what and when |
| Agent performs a forbidden action via another command | A second route (`cat`, `sed -i`, redirection) is allowed | Deny it, or remove the broad allow. This is a **finding**: record it |
| Commit is rejected by the hook | Missing ticket key or trailer; tests failing; secret pattern | Read the hook message. Never use `--no-verify`; say so if a team proposes it |
| Windows: quoting or paths | PowerShell vs bash | Use forward slashes in the tool paths; run via PowerShell scripts where provided |
| Model slow or rate limited | Shared quota | Stagger runs; use the wait time to write test cases |

# Questions to ask when you visit a team
- "Show me the denial." (Not "do you have a denial.")
- "What happens if the ticket says to ignore your instructions?"
- "How are you timing the baseline?"
- "Who is the named human, and what do they do with the diff?"
- "What will you do if the result is a fail?"
- "What would you cut to finish a testable version?"

# Hold the line
- **Do not lock down or loosen guardrails for them.** Ask the question; let them decide and record it.
- If a team widens a permission to get unstuck, it goes in **Changes you made to guardrails** in the results form.
- Praise honest negative results out loud. "We found the agent obeyed the ticket" is the most useful sentence of the day.

# Test phase (from 16:10)
- Teams run the cases in their plan and record **every** run, including failures, in the case log.
- Make sure the scribe records agent time and human review time separately.
- Check Part B against Part A: if a target is missing an actual, ask why.
- Remind them to export or note the audit log (`logs/atlassian-audit.log`) as evidence of what the agent read.

# Facilitator watch-list
Note these for the close-out; they feed the follow-up report.
- Guardrail changes made during the day.
- Second routes found around denials.
- Times a model followed hostile text.
- Teams that built something another team could reuse.
