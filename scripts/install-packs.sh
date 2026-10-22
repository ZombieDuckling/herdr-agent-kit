#!/bin/bash
# Install third-party skill packs from their own sources (see packs.json).
#   scripts/install-packs.sh --list
#   scripts/install-packs.sh design engineering
#   scripts/install-packs.sh --dry-run security
set -euo pipefail
K="$(cd "$(dirname "$0")/.." && pwd)"; DRY=0
[ "${1:-}" = "--dry-run" ] && { DRY=1; shift; }
if [ "${1:-}" = "--list" ] || [ $# -eq 0 ]; then
  python3 - "$K/packs.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1]))
for k, v in d['packs'].items():
    print(f"{k:12} {v['why']}")
    for i in v['items']: print(f"{'':12}  - {i['name']} ({i['license']})")
PY
  exit 0
fi
for pack in "$@"; do
  python3 - "$K/packs.json" "$pack" <<'PY' > /tmp/herdr-agent-pack.$$
import json, sys, shlex
d = json.load(open(sys.argv[1])); p = d['packs'].get(sys.argv[2])
if not p: print(f"echo 'unknown pack: {sys.argv[2]}'; exit 1"); raise SystemExit
for i in p['items']:
    cmd = i['run'] + (f" && {i['after']}" if i.get('after') else "")
    name = i['name'].replace("'", "")
    print(f"echo '>> {name}'")
    need = i.get('needs')
    test = f"command -v {need} >/dev/null" if need else "true"
    print(f"if {test}; then ({cmd}) || echo '   FAILED: {name}'; else echo '   skipped: needs {need}'; fi")
PY
  if [ $DRY = 1 ]; then sed 's/^/  [dry-run] /' /tmp/herdr-agent-pack.$$; else (cd "$K" && bash /tmp/herdr-agent-pack.$$); fi
  rm -f /tmp/herdr-agent-pack.$$
done
