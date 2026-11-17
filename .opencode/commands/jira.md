---
description: Summarise a Jira issue, or the result of a JQL search, read-only — /jira INV-143   or   /jira project = INV AND status = "To Do"
agent: plan
---
Use the `atlassian-reader` sub-agent to look up this in Jira: $ARGUMENTS

If it is an issue key, fetch that issue. Otherwise treat it as JQL and search. Then give me the sub-agent's report, and add one line saying what you would do next with it. Do not change any files.
