# Installs the deliver/ship demo agents, commands and skills from preparation/deliver_ship into .opencode/.
# Never overwrites a file that already exists. Plugins are NOT copied (they need Node.js); scripts/githooks replaces them.
# Run from the repository root: .\scripts\stage-demo.ps1
Set-Location (Split-Path -Parent $PSScriptRoot)
$src = "preparation/deliver_ship"
foreach ($kind in "agents","commands","skills") {
  $base = Join-Path $src $kind
  Get-ChildItem $base -Recurse -File | Where-Object { $_.Name -ne ".DS_Store" } | ForEach-Object {
    $rel = $_.FullName.Substring((Resolve-Path $base).Path.Length + 1)
    $dest = Join-Path ".opencode/$kind" $rel
    if (Test-Path $dest) { Write-Host "  keep   $dest" }
    else { New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null; Copy-Item $_.FullName $dest; Write-Host "  add    $dest" }
  }
}
git config core.hooksPath scripts/githooks
Write-Host "  hooks  core.hooksPath = scripts/githooks"
