#!/usr/bin/env bash
# Installs the deliver/ship demo agents, commands and skills from preparation/deliver_ship into .opencode/.
# Never overwrites a file that already exists. Plugins are NOT copied (they need Node.js); scripts/githooks replaces them.
# Run from the repository root: ./scripts/stage-demo.sh
set -euo pipefail
cd "$(dirname "$0")/.."
src=preparation/deliver_ship
for kind in agents commands skills; do
  (cd "$src/$kind" && find . -type f ! -name .DS_Store) | while read -r f; do
    f="${f#./}"
    if [ -e ".opencode/$kind/$f" ]; then echo "  keep   .opencode/$kind/$f"; else mkdir -p ".opencode/$kind/$(dirname "$f")"; cp "$src/$kind/$f" ".opencode/$kind/$f"; echo "  add    .opencode/$kind/$f"; fi
  done
done
git config core.hooksPath scripts/githooks && echo "  hooks  core.hooksPath = scripts/githooks"
