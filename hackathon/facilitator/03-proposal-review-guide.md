Phase 4 Guide: Presentations, Discussion and Targets (100 minutes)
===
Goal: every team hears constructive, specific feedback on its proposal; the room learns from the other proposals; and each team leaves with **locked targets** and a safer, tighter design.

# 4a. Presentations (55 min for up to 6 teams)
- **5 minutes per team + 4 minutes Q&A.** Teams present **from the proposal document**, no slides.
- Ask the team to cover, in this order: the decision requested; what it does and does not do; the **guardrails and who enforces them**; the **named human and review step**; how it will be tested; the success numbers.
- **Scribes**: each team's scribe writes feedback into that team's proposal under "Feedback received". The helper records cross-cutting themes in a shared list.
- Hold the time. Say "one more question" at 3 minutes of Q&A.

## Q&A prompts (use the best two per team)
- What is the worst it can do if the model is wrong? If a ticket contains hostile text?
- Which guardrail is a rule and which is a sentence in a prompt?
- Is there a second route around that denial?
- Who reads the output at 4:30 on a Friday, and what do they check?
- What is your baseline, and how did you measure it?
- What would make you **stop** the pilot?
- What would you need to see to trust it on a production repository?

# 4b. Cross-team discussion (25 min)
Three rounds, about 8 minutes each. Put the question on screen, use the shared list.

1. **What is good about each proposal?** One specific thing per proposal. Start positive, and name the practice, not the person ("the audit trail that records the config version").
2. **Where else would it be useful?** For each proposal: which other team or repository could use it, and what would they change? Capture the reusable pieces (a skill, a sub-agent, a hook) in the master document as "reusable".
3. **How do we make it safer and more constrained?** For each proposal, one concrete tightening: a narrower permission, an allow-list, a smaller batch size, an extra check, a stop condition. Push for **enforced** changes, not extra prompt text.

## Facilitation moves
- "Which of these controls would still hold if the model ignored the prompt?"
- "Say the worst case in one sentence."
- "Could you make that read-only?"
- "What is the smallest version you could try first?"
- If two teams solved the same sub-problem differently, compare them side by side.

# 4c. Revise and lock targets (20 min)
1. Teams update the proposal with the accepted feedback (10 min).
2. Teams fill **Part A: Targets** of the [results form](../participant/06-results-form.md) (10 min). Check each team's targets before they go to build:
   - every metric has a baseline plan, a target and a failure threshold;
   - the three mandatory metrics are there;
   - at least one adversarial test case is planned;
   - the success rule is written as if/then.
3. After the targets are submitted they are **locked**: results are compared to them in the readout. If a team wants to change one, they change it in the results form *with a reason*, not silently.

# Proposal rubric
Use it to give each team 1–4 scores privately (or to guide your notes). 1 = missing, 2 = weak, 3 = solid, 4 = board-ready.

| Dimension | What a 4 looks like |
|---|---|
| **Problem and value** | Quantified baseline; clear non-goals |
| **Guardrails** | Each control names what enforces it; mostly hard controls; second routes considered; blast radius stated |
| **Human accountability** | Named owner; a named human reads *every* change; recorded in the commit; audit trail |
| **Verification** | Automatic checks before the human sees it; says what it cannot catch |
| **Test plan** | Normal, edge, negative and adversarial cases; baseline; sample size |
| **Metrics** | Baseline, target and failure threshold for each; if/then success rule |
| **Reusability** | Pieces another team could pick up |
| **Constraint** | Smallest scope that delivers value; stop conditions; kill switch |

Common weak spots to probe: guardrails that are prompts; "the developer reviews it" with no record; metrics without baselines; no adversarial case; scope that is "the whole pipeline".
