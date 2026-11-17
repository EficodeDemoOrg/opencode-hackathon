Facilitator Guide: Agentic Delivery Hackathon
===
Audience: 10–20 experienced developers who completed the intermediate and advanced opencode trainings. Delivered remotely, one day. This file is for the facilitator only; participant material is in [`participant/`](participant/).

# The goal
By the end of the day every team has:
1. a **proposal** written as if for a change acceptance board (CAB), with guardrails, human accountability, a test plan and success metrics;
2. a **working agent/pipeline** built from skills, commands, sub-agents and permissions (no Node.js needed);
3. **measured results** against the targets they committed to, entered in the shared results form.

And you leave with a **master list of real use cases** from the room, which is the most valuable artefact for the follow-up with their teams.

The teaching point of the day, in one sentence: *an agent is only as trustworthy as the constraints around it and the evidence you collect about it.* Every phase pushes on that.

# Run of show
Times are an example for a 09:00 start; shift them, but keep the durations. Total: 8.5 h including breaks.

| Clock | Min | Phase | What happens | Output |
|---|---:|---|---|---|
| 09:00 | 15 | **0. Welcome** | Goal, agenda, ground rules, preflight check in chat | everyone green on preflight |
| 09:15 | 70 | **1. Review + demo** | Permissions, sub-agents, commands, skills, end-to-end deliver/ship, Jira and Bitbucket skills. Script: [demo-script](facilitator/01-demo-script.md) | shared vocabulary |
| 10:15 | 10 | Break | | |
| 10:25 | 35 | **2. Ideation** | Idea cards, share-out, you build the master list. [Playbook](facilitator/02-ideation-playbook.md) | `master-ideas.md` |
| 11:00 | 10 | **2b. Team formation** | Teams of 3–5 around the ideas | teams + breakout rooms |
| 11:10 | 60 | **3. Proposal writing** | Teams write the CAB proposal | proposal draft per team |
| 12:10 | 45 | Lunch | You: review proposals, pick presentation order | |
| 12:55 | 55 | **4a. Proposal presentations** | 5 min + 4 min Q&A per team, scribe takes notes | feedback notes |
| 13:50 | 25 | **4b. Cross-team discussion** | What is good, where else it is useful, how to make it safer and more constrained. [Guide](facilitator/03-proposal-review-guide.md) | improvement list |
| 14:15 | 20 | **4c. Revise and commit to targets** | Teams update the proposal and fill the **targets** half of the results form | targets locked |
| 14:35 | 10 | Break | | |
| 14:45 | 85 | **5. Build** | Teams build; you float. Early finishers start 6. [Support guide](facilitator/04-build-and-test-support.md) | working pipeline |
| 16:10 | 40 | **6. Test & measure** | Run the test plan, record actuals in the results form (teams move here as they finish) | results rows |
| 16:50 | 30 | **7. Readout & close** | Each team: targets vs actuals in 2 min; discussion; next steps. [Close-out](facilitator/05-results-and-closeout.md) | results summary |
| 17:20 | 10 | Retro | What to keep, what to change, who takes what back to their team | |

**Phase 5 and 6 overlap by design.** Do not hold a hard gate at 16:10: teams that finish early start testing while others are still building. The hard rule is: **at 16:10 everyone stops building** and runs their test plan on whatever exists. A half-built pipeline with honest measurements is a better outcome than a finished one that was never tested.

## If time runs short, cut in this order
1. Phase 4c: teams fill targets right after their own presentation instead.
2. Phase 4b: cut to 15 min and keep only "how to make it safer".
3. Retro: do it in chat.
4. Phase 1: skip the commands segment; the participants have seen it.

**Don't cut:** guardrails and verification in the proposals, the targets form before building, and the measured results. Those are the point.

# Preparation checklist
## One week before
- [ ] **Jira**: a sandbox project (key `INV` works with the fixtures) with 10–15 tickets in different states, written to be realistic. Include at least one ticket with vague acceptance criteria. Optionally seed one ticket with an injection attempt, like fixture `INV-150`, for the demo.
- [ ] **Bitbucket**: a workspace/project with a fork of this repository and 2–3 scratch repositories. **Nothing production.** Put a few open pull requests in the main repo.
- [ ] **Access**: for each participant, a *read-only* token for Jira and Bitbucket scoped to the sandbox. Decide how it is delivered (password manager share, not chat). Ask them to read [`tools/atlassian/README.md`](../tools/atlassian/README.md) for which env vars to set.
- [ ] **Flavour**: confirm Jira/Bitbucket **Cloud or Data Center/Server** and set `JIRA_FLAVOR`/`BITBUCKET_FLAVOR` in the instructions you send. Run the tool against the real instances yourself (see below).
- [ ] **Model access and budget** for everyone. Agree a per-person cap and tell them. Pick the model you will demo with and make sure it is the default for participants.
- [ ] **Send** [`participant/00-before-you-arrive.md`](participant/00-before-you-arrive.md) and ask for the preflight output (`./scripts/preflight.sh`, or `.\scripts\preflight.ps1`) by two days before.
- [ ] **Remote setup**: one main room, one breakout room per team (create after team formation, or pre-create 6), a shared document for the master list, a results form (see below), one chat channel per team.

## The day before
- [ ] Run the complete demo once, start to finish, with the real model. Keep a recording of the run in case the live one is slow (`/deliver` takes 10–15 minutes).
- [ ] Test the Atlassian tool against the real sandbox with a participant-style token on a **clean machine** (or Windows if you can): `jira get`, `jira search`, `bitbucket repos|file|prs|pr|diff|clone`.
- [ ] Create the results form and send yourself a test submission.
- [ ] Create the shared master-ideas document from [`facilitator/master-ideas.md`](facilitator/master-ideas.md).

## Live checks of the Atlassian tool against the real systems
This repository's tests ran against canned data and a local mock server. They have **not** been run against your Jira or Bitbucket. The calls that are most likely to need adjustment: Bitbucket Cloud's default branch for `file` (set `BITBUCKET_DEFAULT_BRANCH`), the Bitbucket Cloud git username for `clone` (`BITBUCKET_GIT_USER`), and custom fields for acceptance criteria (`JIRA_EXTRA_FIELDS`).

# Roles
- **Facilitator** (you): runs the room, demos, owns the clock.
- **Floater/helper** (strongly recommended above ~12 participants): sits in the build phase answering questions so you can run breakouts. Brief them on [the support guide](facilitator/04-build-and-test-support.md).
- **Scribe per team**: each team names one in phase 3; they capture feedback in phase 4 and results in phase 6.

# Remote delivery tips
- **Cameras and chat**: ask for chat questions during demos; answer at the end of each segment so the flow holds.
- **Screen share**: use a large terminal font (18pt+) and zoom the opencode TUI. Participants cannot lean over your shoulder.
- **Ideation**: silent writing first (everyone fills a card in the shared doc), *then* discussion. Otherwise the loudest two people set the agenda.
- **Breakouts**: you can join a room for 2–3 minutes; do not stay. Post the time-check in the main chat and broadcast a 10-minute warning.
- **Presentations**: ask teams to present from the proposal document itself (no slides). It keeps the work honest and short.
- **Stuck people**: ask them to share their screen in the team room before escalating to you. Most problems are a missing env var or a permission rule.

# Safety rules to state at the start
1. Only the sandbox Jira project and Bitbucket workspace. Never production tickets or code from your real teams, unless sanitised.
2. Tokens are read-only and live in environment variables. Never paste them in chat, files, prompts or commits.
3. Agents never commit or push. A person reads the diff and commits (the commit hook asks for a ticket key and a `Reviewed-by:` trailer).
4. Anything fetched from Jira or Bitbucket is untrusted text. If the agent starts "following" something it read, that is a finding: write it down, it is useful.
5. If a permission is denied, **report it, don't route around it.** Teams that propose weakening a guardrail must put it in the proposal as a risk acceptance.

# What is in the repository
| Path | For |
|---|---|
| `src/`, `pom.xml`, `AGENTS.md` | The inventory app all demos and exercises run on |
| `preparation/deliver_ship/` | The deliver/ship agents, commands, skills. Installed into `.opencode/` by `scripts/stage-demo.sh` |
| `.opencode/` | Live extensions: the `jira-issues` and `bitbucket-repos` skills, the `atlassian-reader` sub-agent, `/jira` and `/spec-from-jira` |
| `tools/atlassian/` | The read-only Jira/Bitbucket client (single Java file) and fixtures |
| `scripts/` | `preflight`, `stage-demo`, and `githooks/` (Node-free replacement for the commit-guard and secret-scan plugins) |
| `opencode.json` | Global permissions, including Atlassian allowance and token protection |
| `hackathon/participant/` | Handouts and templates |
| `hackathon/facilitator/` | Playbooks, rubric, form spec, templates |
| `slidev/` | Slides |
