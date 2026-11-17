---
name: changelog
description: How to write release notes / a changelog entry for the inventory app from git history, in the team's fixed format (Added, Changed, Fixed, with ticket ids). Use whenever you are asked for release notes, a changelog, "what changed since X", or a summary of commits for a release.
---

# Writing a changelog entry

## 1. Get the facts from git
- The commits are in `git log --oneline <from>..HEAD`. If you were not told where to start, use the latest tag (`git describe --tags --abbrev=0`), and if there is no tag, ask.
- For any commit whose one-line message is unclear, read it with `git show --stat <hash>`. Never describe a change you have not seen in a commit.

## 2. Sort each commit into one section
| Section | Goes here |
|---|---|
| Added | a new endpoint, field, page or option a user can see |
| Changed | existing behaviour that now works differently, including API changes |
| Fixed | a bug fix |
| (leave out) | refactoring, tests only, course material (`exercises/`, `prep_scripts/`), formatting |

If a commit touches the API (`InventoryServer`, JSON fields), say so explicitly: other teams depend on it.

## 3. Write it in the template
Read `template.md` in this skill's folder and fill it in exactly.
- One line per change, written for a user of the app, not for a developer: "Items that need reordering are now marked in the list", not "Add stockStatus to toJson()".
- Put the ticket id (for example `INV-142`) at the end of the line if the commit message or branch mentions one.
- Leave out a section that has no entries.

## 4. Report
Return the finished entry, then a short list of the commits you left out and why.
