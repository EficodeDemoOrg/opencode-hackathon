#!/usr/bin/env bash
# Pre-hackathon check. Run from the repository root: ./scripts/preflight.sh
# Prints OK/WARN/FAIL per item and never prints secret values. Needs only bash, java, git.
cd "$(dirname "$0")/.." || exit 1
fail=0
ok()   { printf '  OK    %s\n' "$*"; }
warn() { printf '  WARN  %s\n' "$*"; }
bad()  { printf '  FAIL  %s\n' "$*"; fail=1; }

echo "Tools"
if v=$(java -version 2>&1 | head -1) && n=$(printf '%s' "$v" | sed -E 's/.*"([0-9]+).*/\1/') && [ "$n" -ge 17 ] 2>/dev/null; then ok "java $n"; else bad "JDK 17 or later is required (found: ${v:-none})"; fi
if v=$(mvn -version 2>/dev/null | head -1); then ok "$v"; else bad "Maven 3.9+ not found"; fi
if v=$(git --version 2>/dev/null); then ok "$v"; else bad "git not found"; fi
if v=$(opencode --version 2>/dev/null); then n=$(printf '%s' "$v" | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' | head -1); case "$n" in 2.*) ok "opencode $n";; *) warn "opencode $v (this repository is written for 2.x)";; esac; else bad "opencode not found on PATH"; fi
command -v node >/dev/null 2>&1 && ok "node present (optional: only for plugins/MCP)" || ok "no Node.js (fine: nothing in the hackathon requires it)"

echo "Project"
if mvn -q -B -o test >/tmp/preflight-mvn.log 2>&1 || mvn -q -B test >/tmp/preflight-mvn.log 2>&1; then ok "mvn test passes"; else bad "mvn test failed (see /tmp/preflight-mvn.log)"; fi
if ATLASSIAN_FIXTURES=tools/atlassian/fixtures java tools/atlassian/Atlassian.java jira get INV-143 >/dev/null 2>&1; then ok "Atlassian tool runs (fixture mode)"; else bad "Atlassian tool does not run"; fi
rm -rf logs/atlassian-audit.log 2>/dev/null
[ "$(git config core.hooksPath)" = "scripts/githooks" ] && ok "git hooks installed" || warn "git hooks not installed: git config core.hooksPath scripts/githooks"

echo "Atlassian access (optional until the build phase; values are never printed)"
for v in JIRA_BASE_URL JIRA_TOKEN BITBUCKET_TOKEN; do
  [ -n "${!v}" ] && ok "$v is set" || warn "$v is not set (use fixture mode, or ask the instructor)"
done
[ -n "$JIRA_ALLOWED_PROJECTS" ] && ok "JIRA_ALLOWED_PROJECTS=$JIRA_ALLOWED_PROJECTS" || warn "JIRA_ALLOWED_PROJECTS not set: searches are not scoped to a project"

echo; [ $fail -eq 0 ] && echo "Ready." || echo "Fix the FAIL items before the session."
exit $fail
