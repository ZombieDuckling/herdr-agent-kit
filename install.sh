#!/bin/bash
# herdr-agent-bootstrap installer.
# Installs herdr (with consent), links this kit's skills into every agent found on the machine, adds a short
# rules block to each agent's global instructions, writes ~/.herdr-agent/{house-rules.md,env}, and puts the
# kit's tools on PATH. Never overwrites a skill or file that is not its own. Safe to run again.
#
#   ./install.sh                 interactive (asks before installing herdr)
#   ./install.sh --yes           no questions (installs herdr if missing)
#   ./install.sh --dry-run       print what would happen, change nothing
#   ./install.sh --no-herdr      skip installing herdr
#   ./install.sh --packs design,engineering   also install third-party packs (see packs.json)
#   ./install.sh --uninstall     remove everything this kit added (keeps house-rules.md)
set -euo pipefail
KIT="$(cd "$(dirname "$0")" && pwd)"
HA="$HOME/.herdr-agent"
START='<!-- herdr-agent-bootstrap:start -->'; END='<!-- herdr-agent-bootstrap:end -->'
YES=0; DRY=0; NOHERDR=0; UNINSTALL=0; PACKS=""
while [ $# -gt 0 ]; do case "$1" in
  --yes|-y) YES=1;; --dry-run) DRY=1;; --no-herdr) NOHERDR=1;; --uninstall) UNINSTALL=1;;
  --packs) PACKS="$2"; shift;; --packs=*) PACKS="${1#*=}";;
  -h|--help) sed -n '2,13p' "$0"; exit 0;; *) echo "unknown option: $1" >&2; exit 2;; esac; shift; done

say() { printf '%s\n' "$*"; }
run() { if [ $DRY = 1 ]; then say "  [dry-run] $*"; else eval "$@"; fi; }
have() { command -v "$1" >/dev/null 2>&1; }

# Which agents live here. Each gets the skills and the rules block.
AGENTS=(); SKILL_DIRS=(); RULE_FILES=()
add_agent() { AGENTS+=("$1"); SKILL_DIRS+=("$2"); RULE_FILES+=("$3"); }
{ have claude || [ -d "$HOME/.claude" ]; } && add_agent claude "$HOME/.claude/skills" "$HOME/.claude/CLAUDE.md"
{ have opencode || [ -d "$HOME/.config/opencode" ]; } && add_agent opencode "$HOME/.config/opencode/skills" "$HOME/.config/opencode/AGENTS.md"
{ have codex || [ -d "$HOME/.codex" ]; } && add_agent codex "$HOME/.codex/skills" "$HOME/.codex/AGENTS.md"
{ have hermes || [ -d "$HOME/.hermes" ]; } && add_agent hermes "$HOME/.hermes/skills" "$HOME/.hermes/AGENTS.md"

strip_block() { [ -f "$1" ] || return 0; python3 - "$1" "$START" "$END" <<'PY'
import sys, re
p, s, e = sys.argv[1:4]
t = open(p).read()
t2 = re.sub(r'\n*' + re.escape(s) + r'.*?' + re.escape(e) + r'\n?', '\n', t, flags=re.S)
if t2 != t: open(p, 'w').write(t2.rstrip('\n') + '\n')
PY
}
our_link() { [ -L "$1" ] && [[ "$(readlink "$1")" == "$KIT"/* ]]; }

# ---------------------------------------------------------------- uninstall
if [ $UNINSTALL = 1 ]; then
  for d in "${SKILL_DIRS[@]}" "$HOME/.local/bin"; do
    [ -d "$d" ] || continue
    for l in "$d"/*; do our_link "$l" && run "rm '$l'" && say "removed $l"; done
  done
  for f in "${RULE_FILES[@]}"; do [ -f "$f" ] && { [ $DRY = 1 ] && say "  [dry-run] clean $f" || strip_block "$f"; } && say "cleaned $f"; done
  our_link "$HA/kit" && run "rm '$HA/kit'"
  say "Uninstalled. Kept $HA/house-rules.md and $HA/env (delete them by hand if you want)."
  exit 0
fi

say "herdr-agent-bootstrap: kit at $KIT"
say "agents found: ${AGENTS[*]:-none}"
[ ${#AGENTS[@]} -gt 0 ] || { say "No agent (claude, opencode, codex, hermes) found. Install one first, then run this again."; exit 1; }

# ---------------------------------------------------------------- 1. herdr
if have herdr; then say "herdr: $(herdr --version 2>/dev/null) already installed"
elif [ $NOHERDR = 1 ]; then say "herdr: not installed (skipped by --no-herdr)"
else
  ok=$YES
  if [ $ok = 0 ] && [ -t 0 ]; then read -r -p "Install herdr from https://herdr.dev/install.sh ? [y/N] " a; [[ "$a" =~ ^[Yy] ]] && ok=1; fi
  if [ $ok = 1 ]; then run "curl -fsSL https://herdr.dev/install.sh | sh"; else say "herdr: not installed. Install it later with: curl -fsSL https://herdr.dev/install.sh | sh"; fi
fi
export PATH="$HOME/.local/bin:$PATH"
if have herdr; then
  for a in "${AGENTS[@]}"; do case $a in claude|codex|opencode)
    run "herdr integration install $a >/dev/null 2>&1 || true"; say "herdr integration: $a";; esac; done
fi

# ---------------------------------------------------------------- 2. skills
linked=0; skipped=()
for i in "${!AGENTS[@]}"; do
  a=${AGENTS[$i]}; d=${SKILL_DIRS[$i]}
  run "mkdir -p '$d'"
  for s in "$KIT"/skills/*/*/; do
    s=${s%/}; n=$(basename "$s"); cat=$(basename "$(dirname "$s")")
    [ "$cat" = hermes ] && [ "$a" != hermes ] && continue        # hermes-only skills
    if [ -e "$d/$n" ] || [ -L "$d/$n" ]; then our_link "$d/$n" || skipped+=("$a:$n"); continue; fi
    run "ln -s '$s' '$d/$n'"; linked=$((linked+1))
  done
done
say "skills: $linked links added$([ ${#skipped[@]} -gt 0 ] && echo "; kept your own copies of: ${skipped[*]}")"

# ---------------------------------------------------------------- 3. ~/.herdr-agent
run "mkdir -p '$HA'"
our_link "$HA/kit" || [ -e "$HA/kit" ] || run "ln -s '$KIT' '$HA/kit'"
if [ ! -f "$HA/house-rules.md" ]; then run "cp '$KIT/rules/house-rules.template.md' '$HA/house-rules.md'"; say "house rules: $HA/house-rules.md (fill in the {{...}} items)"; else say "house rules: kept $HA/house-rules.md"; fi
if [ ! -f "$HA/env" ]; then
  om=""; [ -f "$HOME/.config/opencode/opencode.json" ] && om=$(python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.config/opencode/opencode.json'))).get('model',''))" 2>/dev/null || true)
  [ $DRY = 1 ] && say "  [dry-run] write $HA/env (OPENCODE_MODEL=$om)" || printf 'HERDR_AGENT_KIT=%s\nOPENCODE_MODEL=%s\n' "$KIT" "$om" > "$HA/env"
fi

# ---------------------------------------------------------------- 4. rules block
for f in "${RULE_FILES[@]}"; do
  if [ $DRY = 1 ]; then say "  [dry-run] add rules block to $f"; continue; fi
  mkdir -p "$(dirname "$f")"; touch "$f"; strip_block "$f"
  { printf '\n%s\n' "$START"; cat "$KIT/rules/global-block.md"; printf '%s\n' "$END"; } >> "$f"
  say "rules: $f"
done

# ---------------------------------------------------------------- 5. tools
run "mkdir -p '$HOME/.local/bin'"
for t in start-opencode-lead codex-image; do
  dest="$HOME/.local/bin/$t"
  if [ -e "$dest" ] && ! our_link "$dest"; then say "tool: kept your own $dest"; continue; fi
  our_link "$dest" || run "ln -s '$KIT/tools/$t' '$dest'"
done
run "mkdir -p '$HOME/.claude/handover/docs' '$HOME/.claude/handover/strikes'"
for s in "$KIT"/skills/core/lead-handover/scripts/*.sh; do
  dest="$HOME/.claude/handover/$(basename "$s")"; [ -e "$dest" ] || run "cp '$s' '$dest' && chmod +x '$dest'"
done
say "tools: start-opencode-lead, codex-image (needs Hermes), lead-handover scripts in ~/.claude/handover"

# ---------------------------------------------------------------- 6. packs
if [ -n "$PACKS" ]; then run "'$KIT/scripts/install-packs.sh' ${PACKS//,/ }"; fi

say ""
say "Done. Next:"
say "  1. Fill in $HA/house-rules.md (your agent can do it with you)."
say "  2. Open a terminal, run:  cd '$KIT' && herdr"
say "  3. In the herdr pane, start your agent and say:  Run the herdr-agent-bootstrap demo (read DEMO.md)."
