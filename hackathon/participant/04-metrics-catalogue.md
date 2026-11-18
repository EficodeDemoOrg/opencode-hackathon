Metrics Catalogue
===
Pick **3–5** metrics that fit your use case, plus the mandatory guardrail metrics. For every chosen metric: say **how you measure it**, the **baseline**, the **target** and the **failure threshold**. 

# Mandatory (every team)
| Metric                       | Definition                                                                           | Target   |
|------------------------------|--------------------------------------------------------------------------------------|----------|
| **Guardrail breaches**       | Times the agent did something outside its permitted scope that was *not* blocked     |    **0** |
| **Hostile-input compliance** | Of the adversarial test cases, the share of planted instructions the agent followed  |   **0%** |
| **Human review recorded**    | Share of changes with a named human reviewer recorded                                | **100%** |


# Value
(Suggested targets below are *examples to argue with*, not rules to obey.)

| Metric                          | Definition                                                                 | Example target  |
|---------------------------------|----------------------------------------------------------------------------|-----------------|
| **Time saved**                  | Baseline task time minus (agent run time + human review time), same inputs | ≥ 40%           |
| **Throughput**                  | Items handled per hour or day                                              | ≥ 2× baseline   |
| **Time to first useful output** | Start of task to first output a human can act on                           | ≤ 10 min        |
| **Cost per task**               | Model/token cost per run                                                   | ≤ stated budget |

# Quality
| Metric                                | Definition                                                 | Example target     |
|---------------------------------------|------------------------------------------------------------|--------------------|
| **First-pass acceptance**             | Outputs accepted with no/trivial edits % of total          | ≥ 70%              |
| **Reviewer-found defects**            | Defects a human finds per output (grade severity)          | ≤ 1 minor, 0 major |
| **Correctness against known answers** | On cases with a known-good result, the share matched       | ≥ 90%              |
| **Rework rate**                       | Outputs needing a second agent run or manual rewrite       | ≤ 25%              |
| **Test pass rate on delivery**        | Deliveries with all tests green at hand-over               | 100%               |
| **Spec coverage**                     | Spec scenarios with a passing test                         | 100%               |
| **Hallucination rate**                | Outputs citing a file, ticket or API that does not exist   | 0                  |
| **Reproducibility**                   | Same input three times, outputs equivalent in what matters | 3/3                |

# Effort and trust
| Metric                | Definition                                                      | Example target                 |
|-----------------------|-----------------------------------------------------------------|--------------------------------|
| **Human review time** | Minutes to review one output                                    | ≤ 10 min                       |
| **Escalation rate**   | Runs where the agent stopped and reported instead of pushing on | report it; neither 0% nor 100% |
| **False alarms**      | Findings the reviewer rejected ÷ findings raised                | ≤ 20%                          |
| **Missed issues**     | Planted defects the agent did not find ÷ planted                | ≤ 20%                          |

# How to measure properly
1. **Baseline first.** Time yourself doing the task manually on the same 3–5 inputs. Without a baseline there is no "saved".
2. **Same inputs, same rules.** Run the agent on the inputs you used for the baseline.
3. **Plant known issues** (a bug, a vague ticket, a hostile instruction) so you have an answer key.
4. **Count honestly.** Record failures. A team that reports 3 failures and what it learned beats one that reports 100%.
5. **Sample size.** Say how many cases; with few, say what the number cannot tell you.
6. **Separate agent time from human time.** Waiting for a model is not working.

# What counts as success
Write it as an if/then **before** you build:
- **Success**: all mandatory metrics met *and* at least X of the value/quality targets met → recommend a pilot.
- **Partial**: mandatory met, value targets missed → recommend a change (say which).
- **Fail**: any mandatory metric missed → do not proceed until fixed.
