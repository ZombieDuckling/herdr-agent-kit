#!/bin/bash
# Put the kit's override block at the top of named third-party skills (after their frontmatter).
# Usage: scripts/apply-overrides.sh <skill-name> [...]. Safe to run again.
set -euo pipefail
K="$(cd "$(dirname "$0")/.." && pwd)"; BLOCK="$K/rules/overrides/awwwards-jury.md"
for name in "$@"; do
  for f in "$HOME"/.claude/skills/"$name"/SKILL.md "$HOME"/.agents/skills/"$name"/SKILL.md "$HOME"/.config/opencode/skills/"$name"/SKILL.md "$HOME"/.codex/skills/"$name"/SKILL.md; do
    [ -f "$f" ] || continue
    f=$(python3 -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' "$f")
    grep -q 'Local overrides (from herdr-agent-bootstrap)' "$f" && continue
    python3 - "$f" "$BLOCK" <<'PY'
import sys,re
p,b=sys.argv[1],open(sys.argv[2]).read()
t=open(p).read(); m=re.match(r'^---\n.*?\n---\n',t,re.S)
t=(t[:m.end()]+'\n'+b+'\n'+t[m.end():]) if m else (b+'\n'+t)
open(p,'w').write(t)
PY
    echo "override added: $f"
  done
done
