Results Form Spec
===
One response per team, **per part**: 
- Part A (targets) is submitted before building, 
- Part B (actuals) in the test phase. 

Use the same **Team name** value to join them. The questions mirror [`participant/06-results-form.md`](../participant/06-results-form.md).

# Part A: Targets
| Field                          | Type                         | Notes              |
|--------------------------------|------------------------------|--------------------|
| Team name                      | short text, required         |                    |
| Use case (one line)            | short text, required         |                    |
| Accountable human              | short text, required         |                    |
| Metric 1–8 name                | short text                   |                    |
| Metric 1–8 how measured        | short text                   |                    |
| Metric 1–8 baseline            | short text                   |                    |
| Metric 1–8 target              | short text, required for 1–3 |                    |
| Metric 1–8 failure threshold   | short text, required for 1–3 |                    |
| Success rule (if...then...)    | long text, required          |                    |
| Adversarial test case planned? | choice yes/no, required      |                    |


# Part B: Actuals
| Field | Type |
|------------------                                              |-------------------|
| Team name                                                      | short text        |
| What was built                                                 | long text         |
| Cases run: normal                                              | count             |
| Cases run: edge                                                | count             |
| Cases run: negative                                            | count             |
| Cases run: adversarial                                         | count             |
| Metric 1 actual                                                | short text        |
| Metric 1 target met?                                           | yes/no/partly     |
| Metric 1 evidence                                              | short text        |
| Metric 2-8,+++                                                 | --                |
| Guardrail breaches                                             | count, required   |
| Times the agent followed hostile input                         | count, required   |
| Forbidden things tried, and result                             | long text         |
| Guardrail changes made during the day, and why                 | long text         |
| Most important finding                                         | long text         |
| Verdict                                                        | pilot/change/stop |
| Another team that could use it, and what to make safer first   | long text         |
| Build time (min)                                               | short text        |
| Agent run time per case                                        | short text        |
| human review time per case                                     | short text        |
| estimated cost                                                 | short text        |

# Settings
- Collect responses without sign-in if you want speed; otherwise require sign-in and record the name automatically.
- Allow editing after submission until 15:45.
- Create a shared spreadsheet from the responses, and give the facilitator view access to all rows.
