Before You Arrive
===
About 20 minutes, ideally two days before. Nothing here needs Node.js.

# 1. Install and check
You need **JDK 17+, Maven 3.9+, git and opencode 2.x**. From the repository root, run the preflight check and send the output to the facilitator:

Bash:
```bash
./scripts/preflight.sh
```
PowerShell:
```powershell
.\scripts\preflight.ps1
```
Everything must be `OK` except the Atlassian rows, which may be `WARN` until you receive your tokens.

# 2. Install the git hooks
They stand in for plugins (which need Node): they block commits that fail the tests or contain a secret, and require a ticket key and a `Reviewed-by:` trailer.
```bash
git config core.hooksPath scripts/githooks
```

# 3. Try the Atlassian tool without credentials
Fixture mode uses canned tickets and repositories.

Bash:
```bash
export ATLASSIAN_FIXTURES=tools/atlassian/fixtures
java tools/atlassian/Atlassian.java jira get INV-143
java tools/atlassian/Atlassian.java bitbucket repos
```
PowerShell:
```powershell
$env:ATLASSIAN_FIXTURES = "tools/atlassian/fixtures"
java tools/atlassian/Atlassian.java jira get INV-143
java tools/atlassian/Atlassian.java bitbucket repos
```
Read [`tools/atlassian/README.md`](../../tools/atlassian/README.md) for the environment variables that point it at the real sandbox. **Set them in the shell you start opencode from**, and never put a token in a file.

# 4. Think about your own work
Bring **two or three ideas** from your real day-to-day work for something an agent could do. Good ones are frequent, rule-bound and checkable. Do not bring anything that needs production access or data you may not share. You will fill in an idea card ([`01-idea-card.md`](01-idea-card.md)) in the first hour.

# 5. Ground rules for the day
- Sandbox Jira project and Bitbucket workspace only.
- Read-only tokens, in environment variables, never in chat, files or commits.
- Agents do not commit or push. A person reads the diff and commits.
- Text from tickets and PRs is untrusted. If an agent starts obeying it, tell us: that is a finding.
- If a permission is denied, report it; do not route around it.
