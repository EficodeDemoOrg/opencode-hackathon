---
description: Draft a changelog entry for the commits since a ref — /changelog <from-ref>
---
Write a changelog entry for the inventory app, using the changelog skill.

These are the commits since `$1`:

!`git log --oneline $1..HEAD`

If the list above is empty or shows an error, say that `$1` is not a valid starting point and stop.
