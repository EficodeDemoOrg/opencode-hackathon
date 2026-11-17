# Pre-hackathon check. Run from the repository root: .\scripts\preflight.ps1
# Prints OK/WARN/FAIL per item and never prints secret values. Needs only PowerShell, java, git.
Set-Location (Split-Path -Parent $PSScriptRoot)
$script:fail = $false
function Ok($m)   { Write-Host "  OK    $m" }
function Warn($m) { Write-Host "  WARN  $m" }
function Bad($m)  { Write-Host "  FAIL  $m"; $script:fail = $true }

Write-Host "Tools"
$jv = (cmd /c "java -version 2>&1" | Select-Object -First 1)
if ($jv -match '"(\d+)' -and [int]$Matches[1] -ge 17) { Ok "java $($Matches[1])" } else { Bad "JDK 17 or later is required (found: $jv)" }
$mv = (cmd /c "mvn -version 2>&1" | Select-Object -First 1)
if ($mv -match 'Apache Maven') { Ok $mv } else { Bad "Maven 3.9+ not found" }
if (Get-Command git -ErrorAction SilentlyContinue) { Ok (git --version) } else { Bad "git not found" }
if (Get-Command opencode -ErrorAction SilentlyContinue) {
  $ov = (opencode --version)
  if ($ov -match '(?<![\d.])2\.\d+\.\d+') { Ok "opencode $($Matches[0])" } else { Warn "opencode $ov (this repository is written for 2.x)" }
} else { Bad "opencode not found on PATH" }
if (Get-Command node -ErrorAction SilentlyContinue) { Ok "node present (optional: only for plugins/MCP)" } else { Ok "no Node.js (fine: nothing in the hackathon requires it)" }

Write-Host "Project"
mvn -q -B test *> $null
if ($LASTEXITCODE -eq 0) { Ok "mvn test passes" } else { Bad "mvn test failed" }
$env:ATLASSIAN_FIXTURES = "tools/atlassian/fixtures"
java tools/atlassian/Atlassian.java jira get INV-143 *> $null
if ($LASTEXITCODE -eq 0) { Ok "Atlassian tool runs (fixture mode)" } else { Bad "Atlassian tool does not run" }
Remove-Item Env:ATLASSIAN_FIXTURES
Remove-Item logs/atlassian-audit.log -ErrorAction SilentlyContinue
if ((git config core.hooksPath) -eq "scripts/githooks") { Ok "git hooks installed" } else { Warn "git hooks not installed: git config core.hooksPath scripts/githooks" }

Write-Host "Atlassian access (optional until the build phase; values are never printed)"
foreach ($v in "JIRA_BASE_URL","JIRA_TOKEN","BITBUCKET_TOKEN") {
  if ([Environment]::GetEnvironmentVariable($v)) { Ok "$v is set" } else { Warn "$v is not set (use fixture mode, or ask the instructor)" }
}
if ($env:JIRA_ALLOWED_PROJECTS) { Ok "JIRA_ALLOWED_PROJECTS=$($env:JIRA_ALLOWED_PROJECTS)" } else { Warn "JIRA_ALLOWED_PROJECTS not set: searches are not scoped to a project" }

if ($script:fail) { Write-Host "`nFix the FAIL items before the session."; exit 1 } else { Write-Host "`nReady." }
