#!/bin/bash
# Serve the demo site locally. Usage: serve.sh <site-dir> [port]. Prints the URL. Stops with Ctrl-C.
set -euo pipefail
SITE="${1:-$HOME/herdr-agent-demo/site}"; PORT="${2:-4321}"
cd "$SITE"
echo "http://localhost:$PORT/"
exec python3 -m http.server "$PORT" --bind 127.0.0.1
