---
name: inventory-docs
description: How to document the Inventory App HTTP API — one Markdown file per endpoint in docs/api/ in a fixed template, plus the API table in README.md. Use whenever an endpoint is added or changed, or you are asked to document an endpoint, route or API call.
---

# Documenting the Inventory App API

Document exactly what the code does. Read the code; never guess.

## 1. Find the facts
- The route in `src/main/java/com/atlas/inventory/InventoryServer.java` (`route(...)`): its path, method and status codes
- Follow it into `InventoryService` for every validation rule and error message
- The JSON it returns (`toJson()` or the server's JSON helper)

## 2. Write `docs/api/<method>-<path>.md`
The file name is lowercase, with `/`, `{` and `}` replaced by `-` and repeated or trailing dashes removed. For example, `PUT /api/items/{id}` becomes `docs/api/put-api-items-id.md`.

Read `template.md` in this skill's folder and fill it in exactly. Don't add or remove sections.

Every status code must come from the code, including errors. Leave out the field table if the endpoint takes no body.

## 3. Update README.md
Add or update the endpoint's row in the "HTTP API" table, and link to the new file in `docs/api/`.

## 4. Report
List the files you wrote or changed, and anything surprising you found in the code, such as a rule that applies on create but not on update.
