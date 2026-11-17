---
description: Run the test suite and explain any failures (read-only)
agent: plan
---
Here is the output of the test suite:

!`mvn -q -B test 2>&1`

If everything passed, say so in one line.
If anything failed, for each failing test give: the test name, what it expected versus what happened, and the most likely cause in the production code (file and line). Do not change any files.
