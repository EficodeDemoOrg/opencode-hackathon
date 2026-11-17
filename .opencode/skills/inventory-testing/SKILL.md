---
name: inventory-testing
description: How to write and run automated tests for the inventory app (JUnit 5, SQLite, JDK HttpServer) — which test class to use, the required test setup, and which cases to cover. Use whenever you write, fix or review tests in src/test.
---

# Testing the inventory app

## 1. Pick the test class
Put the test in the class that matches the layer that holds the behaviour. **Don't create new test classes.**

| Behaviour lives in | Test class | Setup to reuse |
|---|---|---|
| `InventoryItem` (pure logic) | `InventoryItemTest` | none. Build items with `new InventoryItem(...)` or the `item(quantity, reorderLevel)` helper |
| `InventoryService` (validation, rules) | `InventoryServiceTest` | the existing `@TempDir` + `setUp()`, which creates a real SQLite file |
| `InventoryRepository` (SQL) | `InventoryRepositoryTest` | the existing `@TempDir` setup |
| `InventoryServer` (HTTP routes, status codes, JSON) | `InventoryServerTest` | the existing server started on port `0`. Use `server.port()`, never a fixed port |

Rules (from AGENTS.md): never use `jdbc:sqlite::memory:`, and never use the runtime database `data/inventory.db`.

## 2. Choose the cases
For each behaviour, write **one test per case**, named after the behaviour (`rejectsAQuantityAboveTheMaximumOnCreate`, not `test3`):
- the normal case
- **boundaries**: exactly at a limit, one below, one above (0, the maximum, the maximum + 1)
- the empty case: empty list, empty string, no matching items
- for HTTP routes: the success status and body, the error statuses the route can return (400, 404, 405, 409), and the wrong HTTP method

Assert on exact values: status codes, error messages and JSON fields. Don't just check that "it didn't throw".

## 3. Run
- While working, run only the class you changed: `mvn -q test -Dtest=<ClassName>`
- Before finishing, run everything: `mvn -q test`

## 4. When a test fails
Decide which one is wrong **before** changing anything:
- The test is wrong (a wrong expectation or a setup mistake): fix the test.
- The production code is wrong: **don't weaken the test to make it pass.** Report the bug with the test name, expected and actual values, and the file and line you suspect.

## 5. Report
Finish with a list of tests you added (class and method), what each covers, and the result of the last test run.
