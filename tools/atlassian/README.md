Atlassian Tool (read-only Jira and Bitbucket)
===
One Java file, `Atlassian.java`. It needs only **JDK 17+** (already a prerequisite), no Node.js and no libraries. Agents call it through the `jira-issues` and `bitbucket-repos` skills; you can run it yourself the same way. Run from the repository root.

```bash
java tools/atlassian/Atlassian.java jira get INV-143
java tools/atlassian/Atlassian.java jira search "project = INV AND status = 'To Do'" --max 20
java tools/atlassian/Atlassian.java bitbucket repos
java tools/atlassian/Atlassian.java bitbucket file inventory-app README.md --ref main
java tools/atlassian/Atlassian.java bitbucket prs inventory-app
java tools/atlassian/Atlassian.java bitbucket pr inventory-app 57
java tools/atlassian/Atlassian.java bitbucket diff inventory-app 57
java tools/atlassian/Atlassian.java bitbucket clone inventory-app        # shallow, into repos/inventory-app
```

# Try it with no credentials
```bash
export ATLASSIAN_FIXTURES=tools/atlassian/fixtures      # PowerShell: $env:ATLASSIAN_FIXTURES = "tools/atlassian/fixtures"
```
Fixtures hold the inventory-app tickets `INV-142`, `INV-143`, `INV-150` (the last contains a **planted prompt-injection** for the demo), repositories `inventory-app`, `warehouse-reports`, `payroll-core`, and PR `57`. Add your own by dropping JSON files next to them (see the file names in `fixtures/`).

# Configure for the real sandbox
Set variables **in the shell you start opencode from**. Never write tokens into files, prompts or commits.

| Variable | Used for | Notes |
|---|---|---|
| `JIRA_BASE_URL` | Jira | `https://yourcompany.atlassian.net`, or your Data Center URL |
| `JIRA_FLAVOR` | Jira | `cloud` (default) or `server` (Data Center) |
| `JIRA_EMAIL`, `JIRA_TOKEN` | Jira Cloud | account e-mail + API token (Basic auth) |
| `JIRA_TOKEN` | Jira Data Center | personal access token (Bearer) |
| `JIRA_ALLOWED_PROJECTS` | Jira scope | `INV,OPS`. Issue keys outside it are refused and every JQL search is wrapped in `project in (...)` |
| `JIRA_EXTRA_FIELDS` | Jira | custom fields to show, e.g. `customfield_10042` for acceptance criteria |
| `BITBUCKET_FLAVOR` | Bitbucket | `cloud` (default) or `server` (Data Center) |
| `BITBUCKET_WORKSPACE` | Cloud | workspace slug |
| `BITBUCKET_USER`, `BITBUCKET_TOKEN` | Cloud | user name + token (Basic auth) |
| `BITBUCKET_GIT_USER` | Cloud clone | git user name if it differs from `BITBUCKET_USER` for your token type |
| `BITBUCKET_PROJECT`, `BITBUCKET_BASE_URL`, `BITBUCKET_TOKEN` | Data Center | project key, server URL, HTTP access token (Bearer) |
| `BITBUCKET_ALLOWED_REPOS` | Bitbucket scope | `inventory-app,warehouse-reports`; others are hidden from `repos` and refused everywhere |
| `BITBUCKET_DEFAULT_BRANCH` | file | default `main` |
| `ATLASSIAN_MAX_CHARS` | output | truncation limit for long text (default 8000) |

Use **read-only tokens scoped to the sandbox**. The tool's read-only design is a second line of defence, not the first.

# Guardrails in the code
- **Reads only.** GET requests, plus `git clone`. No code path writes to Jira or Bitbucket.
- **Credentials stay in the process.** Read from environment variables, sent only to the configured host, never printed or logged. For clones, the token goes in an environment-supplied header, so it is not in the command line or in `.git/config`.
- **No surprises on the network.** HTTPS only (plain HTTP just for `localhost`). Redirects to another host are refused. The clone URL's host must match the configured one.
- **Scope.** Optional allow-lists for Jira projects and Bitbucket repositories. Input validated: issue keys, repository slugs, numeric IDs, paths without `..`.
- **Clones are reference copies.** Shallow, into `repos/<name>` (ignored by git), push disabled. An existing directory is never overwritten.
- **Untrusted content is marked.** All text that comes from Jira or Bitbucket is printed between `<<< UNTRUSTED CONTENT ... >>>` markers, and the skills tell the agent to treat it as data.
- **Audit log.** Each call is appended to `logs/atlassian-audit.log` with a timestamp and arguments (no secrets). Use it as evidence of what the agent read.

# What it does not do
It cannot comment, transition, assign, approve or push, by design. Teams whose idea needs writes should say so in the proposal, as a risk, and design a **human-performed** step instead, for example "the agent drafts the comment to a file and a person posts it".

# Status and limits
- Tested against canned fixtures and a local mock HTTP server (auth header, same-host redirect, cross-host redirect refusal, allow-lists, error handling). **Not yet tested against a real Jira or Bitbucket**: try every command against your instances before the session. Likeliest adjustments: the default branch, the git user for Bitbucket Cloud clones, custom fields, and Data Center response details.
- Jira descriptions are shown as returned (wiki markup on API v2), not converted.
- Pagination is not followed: `search` returns up to 50 issues, `repos` the first 100.
- Needs `git` on the PATH for `clone`.
