# <TICKET-ID>: <title>

## Why
<Two or three sentences: who has the problem, and what it costs them today.>

## Scope
**In scope**
- <what changes, from the user's point of view>

**Out of scope / does not change**
- <existing behaviour, JSON fields, schema, pages that must stay as they are>

**Reuses**
- <existing classes and methods the change builds on>

## Scenarios
### Domain
- **WHEN** <concrete input> **THEN** <exact result>

### API
- **WHEN** <request> **THEN** <status code and exact JSON field/value>

### UI
- **WHEN** <what the user does, with seed data values> **THEN** <exact text or element the user sees>

## Tasks
- [ ] 1. <production change> — check: <command or observation>
- [ ] 2. **(test-writer)** <tests for which scenarios> — check: `mvn -q test` passes
- [ ] 3. **(doc-writer)** <docs to update> — check: <file>

## Open questions
- <decision the ticket left open, and the default this spec uses>
