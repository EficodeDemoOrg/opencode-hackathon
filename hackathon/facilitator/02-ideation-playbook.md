Phase 2 Playbook: Ideation and Teams (45 minutes)
===
Goal: collect real use cases from the participants' day-to-day work into **one master document**, then form teams of 3–5 around the ideas people want to build.

# Setup
- One shared document (from [`master-ideas.md`](master-ideas.md)) that everyone can edit. A table, one row per idea, plus an "Idea cards" section where each person adds their own.
- Each participant uses [`participant/01-idea-card.md`](../participant/01-idea-card.md) as the template (paste into the shared doc).
- A timer on screen.

# Run (35 min)
| Min | Step | How |
|---:|---|---|
| 0–3 | Frame | "An agent task is a good candidate when it is **frequent, rule-bound, checkable, and tolerant of a human review**. Today we want ideas from your *real work*, not demo ideas." Show the filters below. |
| 3–13 | **Silent writing** | Everyone writes **1–3 idea cards** in the doc. No talking. If someone is stuck, give them the prompts below. |
| 13–28 | **Share-out** | Round-robin, 45 seconds each: the pain, in one sentence. You type the row into the master table as they speak (or the helper does). Ask **one** clarifying question at most: *"What is the input, and what does a good output look like?"* |
| 28–33 | **Cluster and mark** | Merge duplicates and near-duplicates. Everyone marks up to **3 ideas they would join** (a `+Name` next to the row). |
| 33–35 | Announce | Read out the top ideas by interest. |

# Team formation (10 min, phase 2b)
1. Take ideas in order of interest. Say: "Team of 3–5. If you marked this one, join it." Fill teams from the top. Ideas with fewer than 3 people merge into a near neighbour or are parked.
2. Aim for **4–5 teams** for 20 people, **3 teams** for 10–12. If more teams appear, the presentation phase gets too long: merge.
3. Mix experience and **stack** where you can: someone who knows the Jira workflow, someone who knows the build tooling.
4. Each team names a **scribe** and a **proposal owner** (the person who will be accountable for it at the CAB, and who becomes the named human owner in the proposal).
5. Open breakout rooms, drop each team's idea row into their channel.
6. Park the unchosen ideas in the master doc under "Not taken this time". Those go into the follow-up report.

# Filters to put on screen
A good candidate is:
- **Frequent**: weekly or more. A one-off is not worth building.
- **Rule-bound**: you can write down how you do it, including the exceptions.
- **Checkable**: a test, a diff, a checklist, or a second person can tell whether the output is right.
- **Reversible**: a mistake is caught before it matters (draft, branch, PR, ticket comment). Not a production change.
- **Reachable**: the inputs are in Jira, Bitbucket, or the repo, so we can build it today.

A bad candidate for today: needs production access, needs data we may not touch, or the "check" is "ask the customer".

# Prompts for people who are stuck
- What do you do on a Monday that you do not enjoy and could explain in 10 steps?
- What do you ask a new team member to do on their first week?
- What does your PR review checklist have that nobody enjoys applying?
- What breaks at release time every time?
- What information do you copy from one tool to another?
- What took longer than it should last sprint, and why?
- What would you do with 10 more hours a week on test coverage, docs, or tech debt?

# Seed ideas (use only if the room is quiet)
Have these ready; do not lead with them.
| Idea | Input | Output | Natural guardrail |
|---|---|---|---|
| **PR review assistant** | Bitbucket PR diff + team checklist | Structured review comment (draft, not posted) | Read-only; a person posts the comment |
| **Ticket refinement** | Jira ticket | Acceptance criteria and open questions | Never invents criteria; lists gaps |
| **Jira to spec to change** | Jira ticket | Spec, then tested change on a branch | No commit; human reads the spec first |
| **Test gap finder** | Repo + coverage report | List of untested behaviours; draft tests in `src/test` only | Edit lane limited to tests |
| **Release notes / changelog** | Git history + Jira keys | Notes in house format | Cites every ticket; flags orphans |
| **Dependency bump triage** | Bump PR + changelog | Risk assessment + test results | Read-only plus `mvn test` |
| **Incident summary** | Timeline + tickets | Draft post-mortem | Facts separated from interpretation |
| **Legacy explainer** | Cloned repo | Architecture note + glossary | Reference clone is read-only |
| **Flaky test investigator** | CI log + test | Hypothesis + evidence | Can't edit production code |
| **Runbook updater** | Incident tickets + runbook | Proposed runbook diff | Draft only |
| **Duplicate/vague ticket triage** | New Jira tickets | Labels, duplicate links (proposed) | Never writes to Jira |
| **Migration helper** | Old API usage in repo | Mechanical changes in batches | Small batches; tests must pass |

# Tips
- If one person dominates the share-out, cap everyone at 45 seconds and say so up front.
- If an idea is too big ("rewrite our platform"), ask: "what is the smallest slice with a checkable output?"
- If an idea needs systems we cannot reach, ask whether Jira + Bitbucket + the repo can stand in for a *slice* of it.
- Protect quiet people: after the share-out, say "any card I missed?" and wait.
