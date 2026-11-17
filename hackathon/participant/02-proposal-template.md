Change Proposal: <Name of the agent / pipeline>
===
Write this **as if for the change acceptance board (CAB)**. The board decides whether this agent may be used on real work. They are sceptical, busy and not agent experts. Keep it to **2–3 pages**; use tables and short sentences. Fill in every section; write "none" rather than leaving one empty.

Copy this file to `hackathon/results/<team>-proposal.md` (or your team's shared doc).

| | |
|---|---|
| Team | |
| Proposal owner (**accountable human**) | |
| Date / version | |
| Idea # from the master list | |

# 1. Summary and decision requested
Three sentences: what the agent does, for whom, and the **decision you want from the board** (for example: "approve a 4-week pilot on repository X with team Y, with the limits below").

# 2. Problem and benefit
- Today: what happens, how often, how long it takes, who is affected. Give numbers, even rough.
- With the agent: what changes. What stays the same.
- **What the agent does not do** (non-goals).

# 3. Scope
| Item | In scope | Out of scope |
|---|---|---|
| Systems and repositories | | |
| Environments (never production by default) | | |
| Data touched and its classification | | |
| Kinds of change the agent may propose | | |

# 4. Design
In one diagram or a short list:
- the **flow**, from trigger to the human decision;
- each **primary agent, sub-agent, command and skill**, and what it is for;
- the **inputs**, and which of them are **untrusted** (tickets, PR text, logs, code from other repos);
- the **outputs**, and where they land (draft, branch, comment).

| Component | Type (agent/sub-agent/command/skill/tool) | Purpose | Reads | Writes | Shell commands allowed |
|---|---|---|---|---|---|
| | | | | | |

# 5. Guardrails
Use the [guardrails menu](03-guardrails-menu.md). Show **how each is enforced**, not just that it exists.

## 5.1 Permission matrix
| Capability | Allowed? | Enforced by (rule / hook / tool code / CI) | How we test that it holds |
|---|---|---|---|
| Edit files (which paths?) | | | |
| Run shell commands (which?) | | | |
| Network / web fetch | | | |
| Read Jira / Bitbucket (which projects/repos?) | | | |
| Write to Jira / Bitbucket | no | | |
| Commit / push | no | | |
| Call other agents | | | |
| Read secrets / environment | no | | |

## 5.2 Blast radius
The worst thing that can happen if the agent is **wrong**, and if it is **manipulated by hostile input**. State the limit of the damage and what contains it.

## 5.3 Stop conditions
Iteration limits, what makes the pipeline stop and report instead of retrying, and the kill switch (how a person turns it off in one step).

# 6. Human accountability
- **Named owner** of the agent and its configuration.
- **For every code change**: who reads the diff, what they check, and where it is recorded (e.g. "the author commits with a `Reviewed-by:` trailer; the PR needs one other approval").
- Which steps are **human-only** (commit, merge, release, posting to a ticket).
- The **audit trail**: what is logged (what the agent read, what it changed, which model, which config version) and where.
- Who is accountable when it goes wrong.

# 7. Verification (before a human sees it)
The checks that run **automatically** before human review, and what each catches.
| Check | Catches | Deterministic? | Blocks hand-over if it fails? |
|---|---|---|---|
| e.g. `mvn test` | regressions | yes | yes |
| e.g. reviewer sub-agent | spec mismatch | no | reports |
| | | | |

Say what **cannot** be verified automatically, and how the human covers it.

# 8. Test and validation plan
Specific enough that someone else could run it.
| # | Scenario | Type (normal / edge / **negative** / **adversarial**) | Input | Expected result | Pass if |
|--:|---|---|---|---|---|
| 1 | | normal | | | |
| 2 | | edge | | | |
| 3 | | negative: asked for something out of scope | | refused/stopped | |
| 4 | | adversarial: hostile text in a ticket or PR | | ignored and reported | |
| 5 | | repeat of #1, three runs | | similar result | |

- **Baseline**: how you will measure how long the task takes today (a timed manual run on the same inputs).
- **Sample size**: how many real or realistic cases you will run.

# 9. Metrics and success criteria
Choose from the [metrics catalogue](04-metrics-catalogue.md). **Commit to the numbers before you build.** These go into the results form.
| Metric | How measured | Baseline | **Target (success)** | **Failure threshold** |
|---|---|---|---|---|
| | | | | |
| | | | | |
| **Guardrail breaches** | audit log + review | n/a | **0** | any |

State what you will do with each outcome: success, partial, fail.

# 10. Risks and mitigations
| Risk | Likelihood | Impact | Mitigation | Residual risk |
|---|---|---|---|---|
| Plausible but wrong output accepted by a tired reviewer | | | | |
| Prompt injection via an input | | | | |
| Over-reliance / skills atrophy | | | | |
| Sensitive data in prompts or logs | | | | |
| | | | | |

# 11. Rollout, rollback and dependencies
- Pilot: where, who, how long, entry and exit criteria.
- Rollback: how to remove the agent and any change it influenced.
- Dependencies: tokens and their scopes, models, tools, people's time.
- Cost: expected model/token cost per run.

# 12. Approvals
| Role | Name | Decision | Date |
|---|---|---|---|
| Proposal owner | | | |
| Security / risk reviewer | | | |
| Engineering lead | | | |

---
## Self-check before presenting
- [ ] A reader who knows nothing about opencode can follow sections 1–3.
- [ ] Every guardrail in 5 names *what enforces it*; none relies only on a prompt.
- [ ] Every code change has a **named human** who reads it.
- [ ] The test plan includes a negative and an adversarial case.
- [ ] Every metric has a baseline, a target and a failure threshold.
- [ ] I can say what the agent will **not** do.
