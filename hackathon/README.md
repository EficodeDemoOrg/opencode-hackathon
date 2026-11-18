Agentic Delivery Hackathon
===
A one-day, remote-delivery hackathon for ~20 experienced developers who completed the advanced opencode training workshop. 

Participants propose real use cases, write a change-board proposal with guardrails, human accountability, a test plan and success metrics, then build and measure it. 

**No Node.js required.**

Facilitator: starts with [`FACILITATOR-GUIDE.md`](FACILITATOR-GUIDE.md). 
Slides: [`slidev/hackathon.md`](../slidev/hackathon.md), run with `cd slidev && npm install && npm run hackathon` (slides are only for the presenter, so Node is needed on your machine only).

# Planned schedule
Let's try and stick as close as possible to this: 

| Clock | Min | Phase                      | What happens                                                                                             | Output                      |
|-------|-----|----------------------------|----------------------------------------------------------------------------------------------------------|-----------------------------|
| 09:00 |  15 | **Welcome**                | Goal, agenda, ground rules, preflight check in: [before you arrive](participant/00-before-you-arrive.md) | everyone green on preflight |
| 09:15 |  80 | **Review + demo**          | Permissions, sub-agents, commands, skills, end-to-end deliver/ship, Jira and Bitbucket skills.           |           shared vocabulary |
| 10:30 |  20 | **Ideation**               | Use case brain storm [idea card](participant/01-idea-card.md)                                            |        master list of ideas |
| 10:55 |  15 | **Team formation**         | Four teams of 3-5 members around the ideas                                                               |      teams + breakout rooms |
| 11:10 |  50 | **Proposal writing**       | Teams write the proposals for the CAB following the [template](participant/02-proposal-template.md)      |     proposal draft per team |
| 12:00 |  60 | **Lunch**                  |                                                                                                          |                             |
| 13:00 |  25 | **Proposal presentations** | 3-5 min per team + Q&A, scribe takes notes [results form](participant/06-results-form.md)                |              feedback notes |
| 13:25 |  05 | **Commit to targets**      | Teams update the proposal and fill the **targets** half of the results form                              |              targets locked |
| 13:30 |  85 | **Build**                  | Teams [build](participant/05-build-playbook.md). Oskar helps where needed.                               |            working pipeline |
| 14:30 |  40 | **Test & measure**         | Run the test plan, record actuals in the results [results form](participant/06-results-form.md).         |              results logged |
| 15:30 |  30 | **Presentation prep**      | From code prototype to presentable project story                                                         |                             |
| 16:00 |  45 | **Team presentations**     | What we did, what went well, what needs improvement, [Close-out](facilitator/05-results-and-closeout.md) |             results summary |
| 16:45 |  15 | **Retro & close**          | Discussion. What was learned? What happens next? What will you bring to your team? Feedback to Oskar?    |                    feedback |
---


# What the participants get
- The **inventory app** and the deliver/ship agents from the training (`preparation/deliver_ship`, installed with `scripts/stage-demo.sh`).
- **Read-only Jira and Bitbucket access** via [`tools/atlassian`](../tools/atlassian/README.md): a single Java file, with skills, a sub-agent and commands in `.opencode/`, plus fixtures to try it with no credentials.
- **Node-free guardrails**: permissions in `opencode.json` and agent files, and git hooks in `scripts/githooks` (tests, secret scan, ticket key, `Reviewed-by:` trailer).

# Layout
```text
hackathon/
  FACILITATOR-GUIDE.md      run of show, prep checklist, roles, remote tips
  participant/              handouts and templates (for the participants)
  facilitator/              demo script, playbooks, rubric, form spec, master-ideas template
  results/                  where teams commit their proposal and results (no secrets, no real data)
tools/
  atlassian/                read-only Jira and Bitbucket client, fixtures
scripts/                    preflight, stage-demo, githooks
.opencode/                  
  agents/                   atlassian-reader
  skills/                   jira-issues, bitbucket-repos, ...
  commands/                 /jira, /spec-from-jira, ...
```

# Status
Verified: the Atlassian tool against fixtures and a local mock server, the git hooks, `scripts/preflight.sh` and `scripts/stage-demo.sh`, and that `mvn test` passes. Not verified: any run against a real Jira/Bitbucket, the opencode agents and commands with a live model, and the PowerShell scripts (`.ps1`) on Windows. See the "day before" checklist in the facilitator guide.
