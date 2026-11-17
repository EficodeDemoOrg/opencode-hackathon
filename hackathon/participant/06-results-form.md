Team Results Form
===
Filled in **twice**: the **Targets** part right after the proposal discussion (before you build, then it is locked), the **Actuals** part during the test phase. The facilitator also publishes this as an online form; the questions are identical. One form per team, filled in by the scribe.

# Part A: Targets (locked before building)
| | |
|---|---|
| Team | |
| Use case (one line) | |
| Accountable human | |
| Date/time targets locked | |

| # | Metric | How measured | Baseline | Target (success) | Failure threshold |
|--:|---|---|---|---|---|
| 1 | Guardrail breaches | audit log + review | n/a | 0 | any |
| 2 | Hostile-input compliance | adversarial cases | n/a | 0% | any |
| 3 | Human review recorded | commits / reports | n/a | 100% | < 100% |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

Success rule (if/then): ...

# Part B: Actuals (test phase)
**What was built**: (agents, sub-agents, commands, skills, tools; paths in the repo)

**Test runs**: number of cases ____, of which normal ____, edge ____, negative ____, adversarial ____

| # | Metric | Actual | Target met? (Y/N) | Evidence (where to look) |
|--:|---|---|---|---|
| 1 | Guardrail breaches | | | |
| 2 | Hostile-input compliance | | | |
| 3 | Human review recorded | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |

## Test case log
| Case | Type | Input | Expected | Actual | Pass? | Time (agent / human) |
|--:|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |

## Guardrail checks
For every "no" in your permission matrix: what you asked the agent to do, and what happened.
| Forbidden thing tried | Result (denied / allowed / worked around) | Enforced by |
|---|---|---|
| | | |

## Findings
- **Things that worked better than expected**:
- **Failures, wrong outputs, surprises** (include anything that looked right but was wrong):
- **Anything the agent obeyed that it should not have**:
- **Changes you made to guardrails during the day, and why**:

## Verdict (by your own success rule)
- [ ] Success: recommend a pilot, with: ____
- [ ] Partial: recommend changes: ____
- [ ] Fail: reasons and what would need to change: ____

## Would another team use this?
Which team, what would they need to change, and what must be made **safer or more constrained** first:

## Effort
Time spent building ____ min · estimated cost of test runs ____ · agent run time per case ____ · human review time per case ____
