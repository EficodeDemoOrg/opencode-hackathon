---
name: spec-writing
description: How to turn a ticket or feature request for the inventory app into a reviewable spec in specs/<TICKET-ID>.md — scope, WHEN/THEN scenarios with concrete values, and a task list — before any code is written. Use whenever you are asked to write, draft or propose a spec, plan a feature from a ticket, or refine a vague ticket into acceptance criteria.
---

# Writing a spec for the inventory app

A spec is a contract: whoever implements it, tests it and reviews it works only from what is written here. Anything left vague will be guessed.

**Do not write or change any code.** Your only output is the spec file.

## 1. Read before you write
- The ticket (for example `tickets/INV-142.md`) and `AGENTS.md`.
- The code the feature touches. Look for behaviour that **already exists** and reuse it: for example `InventoryItem` already has `stockStatus()` and `reorderShortage()`. Name the existing method in the spec instead of describing a new calculation.

## 2. Write `specs/<TICKET-ID>.md`
Read `template.md` in this skill's folder and fill it in. Keep every section; write "none" if a section is empty.

Rules for scenarios:
- **Concrete values, never adjectives.** "quantity 5, reorder level 5 → `LOW`", not "items that are running low".
- **Every boundary.** For a threshold: zero, exactly at it, one below, one above.
- **Separate Domain, API and UI scenarios.** Domain and API scenarios become Java tests. UI scenarios are checked by a person (or a browser agent), so give the exact text the user sees, using the seed data in `src/main/resources/db/seed.sql`.
- **Say what does not change**: existing JSON fields, the database schema, other pages.

Rules for tasks:
- Small steps, each ending with how to check it ("… and `mvn -q test -Dtest=InventoryItemTest` passes").
- Mark the tasks for other roles: **(test-writer)** for tests, **(doc-writer)** for documentation.

## 3. Open questions
If the ticket leaves a decision open (a field name, what an empty state shows), **do not decide silently**. Pick a sensible default, write it into the spec, and list it under "Open questions" so a person confirms it.

## 4. Report
Give the path of the spec, the number of scenarios per group, and the open questions.
