# macOS agent heat triage — July 2026 example

## Situation

The user reported a Mac Mini getting very hot while multiple agent/browser automation surfaces were running.

## Useful observed signals

- Load average around 4 on Apple Silicon while the machine still showed idle CPU in broad `top` snapshots.
- `ps` gave better attribution than `top` sorting in this case.
- A short-lived `openclaw` gateway process repeatedly appeared hot, sometimes over 100% CPU.
- `fseventsd` consumed very high CPU and large memory, indicating filesystem-event churn rather than being the real root cause.
- A temporary Chrome automation profile under `/tmp/hermes-linkedin-chrome-...` was several GB and actively modifying IndexedDB/WebStorage/Safe Browsing/extension state.
- The hot `openclaw` process respawned, and `launchctl list` revealed `ai.openclaw.gateway` as the supervisor.

## Durable pattern

When heat comes from agent/browser automation:

1. Identify hot processes with `ps`, not only `top`.
2. Check for large `/tmp` Chrome profiles using `--user-data-dir`.
3. Treat `fseventsd` as a write-storm symptom and find which temp profile or app is changing files.
4. If a hot process respawns, inspect `launchctl list` and LaunchAgent plists before repeated `pkill`.
5. Stop the supervising LaunchAgent only if the user wants that surface parked.
6. Kill the browser processes before deleting the temp profile.
7. Verify load/process state after cleanup.

## Approval pitfall

A bundled cleanup command that stops LaunchAgents, kills processes, and deletes a profile may trigger or time out under command approval. For future sessions, split into:

- inventory;
- explicit summary of exact PIDs/paths/labels;
- approved cleanup;
- verification.

Do not route around an approval timeout by attempting the same destructive cleanup through another mechanism.
