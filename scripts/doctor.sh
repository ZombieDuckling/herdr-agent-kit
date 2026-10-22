#!/bin/bash
# Report what this machine has for the kit. Changes nothing. One line per item: ok / missing / note.
K="$(cd "$(dirname "$0")/.." && pwd)"
ok()   { printf '  %-14s ok       %s\n' "$1" "$2"; }
miss() { printf '  %-14s MISSING  %s\n' "$1" "$2"; }
note() { printf '  %-14s note     %s\n' "$1" "$2"; }
v() { "$@" 2>/dev/null | head -1; }
echo "herdr-agent-bootstrap doctor ($(uname -s) $(uname -m))"
echo "required"
command -v git >/dev/null && ok git "$(v git --version)" || miss git "install git"
command -v python3 >/dev/null && ok python3 "$(v python3 --version)" || miss python3 "install Python 3"
if command -v node >/dev/null; then n=$(node -v); [ "${n#v}" \> "19" ] && ok node "$n" || miss node "$n is too old: need 20+"; else miss node "install Node.js 20+ (the demo site checks need it)"; fi
command -v herdr >/dev/null && ok herdr "$(v herdr --version)" || miss herdr "install.sh can install it (curl -fsSL https://herdr.dev/install.sh | sh)"
echo "agents (at least one)"
n=0
command -v claude   >/dev/null && { ok claude "$(v claude --version)"; n=$((n+1)); } || note claude "not found (https://claude.com/claude-code)"
command -v opencode >/dev/null && { ok opencode "$(v opencode --version) - free workers"; n=$((n+1)); } || note opencode "not found: recommended for free workers (https://opencode.ai)"
command -v codex    >/dev/null && { ok codex "$(v codex --version)"; n=$((n+1)); } || note codex "not found (optional)"
command -v hermes   >/dev/null && { ok hermes "found - no-key image backend: hermes auth codex"; n=$((n+1)); } || note hermes "not found (optional)"
[ $n -gt 0 ] || miss agent "install at least one of claude, opencode, codex"
echo "optional"
command -v gh >/dev/null && { gh auth status >/dev/null 2>&1 && ok gh "signed in" || note gh "installed, not signed in (gh auth login)"; } || note gh "not found (GitHub work)"
command -v semgrep >/dev/null && ok semgrep "$(v semgrep --version)" || note semgrep "not found (pipx install semgrep) for code audits"
img="none"; [ -n "${OPENAI_API_KEY:-}${IMAGE_API_KEY:-}" ] && img="OpenAI-compatible key"
[ -x "$HOME/.hermes/hermes-agent/venv/bin/python" ] && img="Hermes codex sign-in (codex-image)"
[ "$img" = none ] && note images "no image backend: the demo uses SVG and CSS art instead (see docs/06-images.md)" || ok images "$img"
[ -d "$HOME/.herdr-agent" ] && ok kit "installed ($HOME/.herdr-agent)" || note kit "not installed yet: ./install.sh"
[ "${HERDR_ENV:-}" = 1 ] && ok inside-herdr "pane $HERDR_PANE_ID in $HERDR_WORKSPACE_ID" || note inside-herdr "no: the demo must run inside herdr"
