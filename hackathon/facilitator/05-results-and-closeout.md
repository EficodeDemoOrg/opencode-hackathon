Phase 7 Guide: Results Readout and Close-out (40 minutes)
===

# Readout (30 min)
**2 minutes per team, 1 minute of questions**, reading from the filled results form on screen: targets next to actuals.

Each team covers:
1. What was built (one sentence).
2. Targets vs actuals: which were met and which were not.
3. The most important finding, good or bad.
4. Their own verdict: pilot, change, or stop.

Then 8–10 minutes of discussion across teams:
- What did every team run into? (Those are the platform-level lessons.)
- Which **guardrails held**, and which did not?
- Which pieces are reusable by other teams, and what would they need first?
- What would the board decide now?

# Collect the results
- Export the online form responses to a spreadsheet. Column layout is in [`results-form-spec.md`](results-form-spec.md); a ready CSV header is in [`results-collector.csv`](results-collector.csv).
- Ask each team to commit or share their agent files, skills, proposal and filled form into `hackathon/results/<team>/`. Remind them: **no tokens, no real data**; a person commits.
- Keep the audit logs if teams are willing to share them.

# Retro (10 min)
Three questions, answered in chat in one minute, then read out:
1. What will you take back to your team on Monday?
2. What would you change about today?
3. What is the one control you will insist on before anyone runs an agent on production code?

# Follow-up report (within a week)
Send participants and sponsors a short report:
| Section | Content |
|---|---|
| Summary | What the day produced, in five lines |
| Master list | Every idea from `master-ideas.md`, with which were built |
| Results table | Per team: targets, actuals, verdict |
| Guardrail findings | Second routes found, hostile-input incidents, guardrail changes made |
| Reusable pieces | Skills, agents, commands, hooks worth adopting; who owns them |
| Recommendations | Pilots to start, with the conditions; changes to the standard configuration |
| Parked ideas | The ones not built |

## Reminders to include
- Rotate or revoke every token issued for the day.
- Delete `repos/` clones and logs on machines that held sandbox data.
- Reset the sandbox Jira/Bitbucket if you will reuse it.
