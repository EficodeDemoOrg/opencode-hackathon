Results Form Spec
===
Build this in Microsoft Forms or Google Forms (about 10 minutes). One response per team **per part**: Part A (targets) is submitted before building, Part B (actuals) in the test phase. Use the same **Team name** value to join them. The questions mirror [`participant/06-results-form.md`](../participant/06-results-form.md).

# Part A: Targets
| Field | Type | Notes |
|---|---|---|
| Team name | short text, required | |
| Use case (one line) | short text, required | |
| Accountable human | short text, required | |
| Metric 1–6 name | short text (metric 1–3 pre-filled: guardrail breaches, hostile-input compliance, human review recorded) | |
| Metric 1–6 how measured | short text | |
| Metric 1–6 baseline | short text | |
| Metric 1–6 target | short text, required for 1–3 | |
| Metric 1–6 failure threshold | short text, required for 1–3 | |
| Success rule (if/then) | long text, required | |
| Adversarial test case planned? | choice yes/no, required | |

# Part B: Actuals
| Field | Type |
|---|---|
| Team name | short text (must match Part A) |
| What was built | long text |
| Cases run: normal / edge / negative / adversarial | four numbers |
| Metric 1–6 actual | short text |
| Metric 1–6 target met? | choice yes/no/partly |
| Metric 1–6 evidence | short text |
| Guardrail breaches (count) | number, required |
| Times the agent followed hostile input (count) | number, required |
| Forbidden things tried, and result | long text |
| Guardrail changes made during the day, and why | long text |
| Most important finding | long text |
| Verdict | choice: pilot / change / stop |
| Another team that could use it, and what to make safer first | long text |
| Build time (min), agent run time per case, human review time per case, estimated cost | four short texts |

# Settings
- Collect responses without sign-in if you want speed; otherwise require sign-in and record the name automatically.
- Allow editing after submission until 17:00.
- Create a shared spreadsheet from the responses, and give the facilitator view access to all rows.
