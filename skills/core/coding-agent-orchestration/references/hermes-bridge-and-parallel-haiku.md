# Hermes ⇄ Claude Code bridge and parallel Haiku orchestration

Session-derived pattern for using Claude Code from Hermes as a low-cost worker pool.

## Bridge plugin pattern

A user plugin can expose Claude Code print mode as Hermes tools without editing Hermes core:

- Plugin path: `~/.hermes/plugins/claude-code-bridge/`
- Manifest: `plugin.yaml`
- Register tools from `__init__.py` with `ctx.register_tool(...)`
- Tool handler runs local `claude -p <prompt>` via `subprocess.run(...)`
- Preserve `HOME` in the subprocess env so Claude Code can use the existing OAuth store
- Add common GUI-launched paths (`/opt/homebrew/bin`, `/usr/local/bin`, Node/NVM paths) so `claude` resolves in desktop sessions
- Enable with `hermes plugins enable claude-code-bridge`
- Start a fresh Hermes session before expecting newly registered tools in the LLM tool schema

Useful tool split:

- `claude_code_status`: run `claude --version` and `claude auth status --text`
- `claude_code`: run `claude -p` with `--output-format json`, `--max-turns`, optional model/effort/tool allowlists, cwd, and timeout

## Parallel Haiku worker pattern

For quick multi-agent tests, run several independent Claude Code print-mode calls concurrently using Hermes parallel tool calls, not shell `&` in one foreground terminal command. Hermes terminal rejects foreground commands that background subprocesses with `&`.

Good pattern:

- Scaffold the project first with clear file boundaries.
- Launch 2-3 Claude Code workers in parallel via multiple `terminal(...)` calls in one `multi_tool_use.parallel` call.
- Give each worker non-overlapping ownership to reduce conflicts, e.g.:
  - Backend worker: only `server.js`
  - Frontend worker: only `public/*`
  - Integration worker: only `README.md`, `docs/*`, `test/*`
- Use cheap model: `--model haiku`
- Use print mode: `claude -p '<self-contained task>' --model haiku --output-format json`
- Restrict tools: `--allowedTools 'Read,Edit,Write'` or add narrowly-scoped Bash only when necessary.

## Pitfalls observed

- Too-low `--max-turns` can return `error_max_turns` after Claude has already written useful partial files. Do not discard partial work; inspect the filesystem and continue only the missing slice.
- For small build tests, `--max-turns 4` may be too tight. Prefer `6-8` for workers expected to create multiple files.
- If one worker fails or stalls, run a focused follow-up worker for that layer instead of rerunning all workers.
- After workers finish, Hermes must verify the artifact directly: run tests, start the server if relevant, hit endpoints, and then stop the process.
- Do not report success from Claude's self-report alone; inspect files and run the project.

## Minimal verification loop for Node webapp tests

1. `npm test` or equivalent smoke test.
2. Start server with `terminal(background=true)` for long-lived process.
3. Poll until startup log appears.
4. Hit `/`, key API endpoints, and one write path (`POST`, form action, etc.).
5. Kill the background server before final response.
