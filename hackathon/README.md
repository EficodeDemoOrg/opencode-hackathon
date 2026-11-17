Agentic Delivery Hackathon
===
A one-day, remote hackathon for 10–20 experienced developers who completed the intermediate and advanced opencode trainings. Participants propose real use cases, write a change-board proposal with guardrails, human accountability, a test plan and success metrics, then build and measure it. **No Node.js required.**

Facilitator: start with [`FACILITATOR-GUIDE.md`](FACILITATOR-GUIDE.md). Slides: [`slidev/hackathon.md`](../slidev/hackathon.md), run with `cd slidev && npm install && npm run hackathon` (slides are only for the presenter, so Node is needed on your machine only).

# The day
| Phase | Min | Participants do | Material |
|---|---:|---|---|
| 0. Welcome | 15 | Preflight, ground rules | [before you arrive](participant/00-before-you-arrive.md) |
| 1. Review & demo | 60 | Watch: permissions, sub-agents, commands, skills, deliver/ship, Jira and Bitbucket | [demo script](facilitator/01-demo-script.md) |
| 2. Ideation + teams | 45 | Idea cards, share-out, form teams of 3–5 | [idea card](participant/01-idea-card.md), [playbook](facilitator/02-ideation-playbook.md), [master list](facilitator/master-ideas.md) |
| 3. Proposal | 60 | Write the CAB proposal | [template](participant/02-proposal-template.md), [guardrails](participant/03-guardrails-menu.md), [metrics](participant/04-metrics-catalogue.md) |
| 4. Present + discuss | 100 | Present, give feedback, tighten, lock targets | [review guide](facilitator/03-proposal-review-guide.md), [results form](participant/06-results-form.md) |
| 5. Build | 85 | Build the agents/pipeline | [build playbook](participant/05-build-playbook.md), [support guide](facilitator/04-build-and-test-support.md) |
| 6. Test & measure | 40 | Run the test plan, record actuals | [results form](participant/06-results-form.md) |
| 7. Readout & close | 40 | Targets vs actuals, retro | [close-out](facilitator/05-results-and-closeout.md) |

# What the participants get
- The **inventory app** and the deliver/ship agents from the training (`preparation/deliver_ship`, installed with `scripts/stage-demo.sh`).
- **Read-only Jira and Bitbucket access** via [`tools/atlassian`](../tools/atlassian/README.md): a single Java file, with skills, a sub-agent and commands in `.opencode/`, plus fixtures to try it with no credentials.
- **Node-free guardrails**: permissions in `opencode.json` and agent files, and git hooks in `scripts/githooks` (tests, secret scan, ticket key, `Reviewed-by:` trailer).

# Layout
```text
hackathon/
  FACILITATOR-GUIDE.md      run of show, prep checklist, roles, remote tips
  participant/              handouts and templates (give these to participants)
  facilitator/              demo script, playbooks, rubric, form spec, master-ideas template
  results/                  where teams commit their proposal and results (no secrets, no real data)
tools/atlassian/            read-only Jira and Bitbucket client, fixtures
scripts/                    preflight, stage-demo, githooks
.opencode/                  jira-issues and bitbucket-repos skills, atlassian-reader agent, /jira, /spec-from-jira
```

# Status
Ready to rehearse, **not yet rehearsed end to end with a model.** Verified: the Atlassian tool against fixtures and a local mock server, the git hooks, `scripts/preflight.sh` and `scripts/stage-demo.sh`, and that `mvn test` passes. Not verified: any run against a real Jira/Bitbucket, the opencode agents and commands with a live model, and the PowerShell scripts (`.ps1`) on Windows. See the "day before" checklist in the facilitator guide.
