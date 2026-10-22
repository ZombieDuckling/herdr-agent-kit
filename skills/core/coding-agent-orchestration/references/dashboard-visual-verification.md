# Dashboard Visual Verification Pattern

Use this when a task changes rendered HTML/CSS or any long-running web UI.

## Why this matters
A green test suite can still hide stale browser output if an old server process is still listening on the port.

## Minimal pattern
1. Have one worker make the source edits.
2. Have a second worker audit the rendered output or compare generated HTML/CSS.
3. Restart the actual listening process after the edit.
4. Verify the live page with `curl`/browser inspection, not just `go test` or build output.
5. Grep for the exact visual cues you intended to add or remove.

## Useful probes
- `lsof -nP -iTCP:<port> -sTCP:LISTEN`
- `curl -s http://127.0.0.1:<port> | grep -o '<needle>'`
- `go test ./...`
- `git diff --stat` and `git diff` for source review

## Common cue checks
- Rounded corners: `border-radius: 8px`, `border-radius: 999px`
- Glass/blur: `backdrop-filter`
- Transparent panels: `background: transparent`
- Soft shadow glass: `box-shadow`, `drop-shadow`
- Translucent panel fills: `rgba(..., 0.x)`
