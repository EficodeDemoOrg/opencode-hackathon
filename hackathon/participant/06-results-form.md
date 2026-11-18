Team Results Form
===
Filled in **twice**: 
1. Fill in your **Targets** part right after the proposal discussion (before you build, then it is locked)
2. Fill in the **Actuals** part during the test phase. 

The facilitator also publishes this as an online form; the questions are identical. One form per team, filled in by the scribe.

# Part A: Set targets

| TARGETS (before build)   |     |
|--------------------------|-----|
| Team                     | ... |
| Use case (one line)      | ... |
| Accountable human        | ... |
| Date/time targets locked | ... |


| # | Metric                   | How measured       | Baseline | Target (success) | Failure threshold |
|--:|--------------------------|--------------------|----------|------------------|-------------------|
| 1 | Guardrail breaches       | audit log + review |      n/a |                0 | any               | 
| 2 | Hostile-input compliance |  adversarial cases |      n/a |               0% | any               |
| 3 | Human review recorded    |  commits / reports |      n/a |            100%  | < 100%            |
| 4 | (metric1)                |                 ?  |        ? |               ?  | ?                 |
| 5 | (metric2)                |                 ?  |        ? |               ?  | ?                 |
| 6 | (metric3)                |                 ?  |        ? |               ?  | ?                 |
| 7 | (metric4)                |                 ?  |        ? |               ?  | ?                 |
| 8 | (metric5)                |                 ?  |        ? |               ?  | ?                 |

## Success rule: 
- If ...
- Then ...

# Part B: Test phase actuals 
**What was built**: (agents, sub-agents, commands, skills, tools; paths in the repo)

## Test runs 
- Number of cases ____,
- of which normal ____, 
- edge ____, 
- negative ____, 
- adversarial ____

| # | Metric                   | Actual | Target met? (Y/N) | Evidence (where to look) |
|--:|--------------------------|--------|---|---|
| 1 | Guardrail breaches       |        | | |
| 2 | Hostile-input compliance |        | | |
| 3 | Human review recorded    |        | | |
| 4 |                          |        | | |
| 5 |                          |        | | |
| 6 |                          |        | | |

## Test case log
| Case | Type | Input | Expected | Actual | Pass? | Time (agent / human) |
|-----:|------|-------|----------|--------|-------|----------------------|
| 1    |      |       |          |        |       |           ?/?        |
| 2    |      |       |          |        |       |           ?/?        |
| 3    |      |       |          |        |       |           ?/?        |
| 4    |      |       |          |        |       |           ?/?        |
| 5    |      |       |          |        |       |           ?/?        |

## Guardrail checks
For every "no" in your permission matrix: what you asked the agent to do, and the result (denied / allowed / worked around / what happened).

| Forbidden action tested | Result  | Enforced by |
|-------------------------|---------|-------------|
|               test 1    |    ?    | (mechanism) |

## Findings
- **What worked better than expected**: ___
- **Failures, wrong outputs, surprises**: (include anything that looked right but was wrong) ___
- **Anything the agent obeyed that it should not have**: ___
- **Changes you made to guardrails during the day, and why**: ___

## Verdict (by your own success rule)
- [ ] Success: recommend a pilot, with: ____
- [ ] Partial: recommend changes: ____
- [ ] Fail: reasons and what would need to change: ____

## Would another team use this?
Which team, what would they need to change, and what must be made **safer or more constrained** first:

## Effort
- Time spent building ____ min
- Estimated cost of test runs ____$ 
- Agent run time per case: ____ min
- Human review time per case ____ min
