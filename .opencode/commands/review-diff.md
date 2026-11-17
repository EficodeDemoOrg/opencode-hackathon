---
description: Review the uncommitted changes against AGENTS.md (read-only) — /review-diff [what to focus on]
agent: plan
---
You are reviewing uncommitted changes. Do not change any files.

The repository rules:

!`git show HEAD:AGENTS.md`

Changed files:

!`git status --short`

The diff:

!`git diff HEAD`

If the diff above is empty, answer only "Nothing to review." and stop.

Otherwise review the change against the repository rules. If a focus is given here, pay special attention to it: $ARGUMENTS

List your findings, most serious first. For each: file and line, what is wrong, why it matters, and a concrete fix. End with one line: `APPROVE` or `REQUEST CHANGES`.
