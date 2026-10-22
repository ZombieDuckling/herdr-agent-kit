# Fabled Five Ship-Readiness Orchestration

Use this pattern when the user asks to run a multi-agent coding sprint across an org/repo set and the desired outcome is "ready to ship", not just cleanup.

## Core pattern

1. **Audit first, then dispatch.** Build or load a concrete audit/ship plan before launching workers. Include repo inventory, known blockers, and exact verification gates.
2. **Use a ship matrix as the source of truth.** Every repo must end with:
   - Repo
   - Status: Ship / Conditional Ship / No Ship / Archive / Vendor Mirror
   - Branch
   - PR
   - Build command
   - Test command
   - Security scan
   - Docs status
   - Known blockers
   - Next owner action
3. **Partition by ownership, not just file count.** A good five-agent split is:
   - Release manager / QA / ship matrix
   - Backend + security
   - Mobile
   - Frontend + product UX
   - Docs / ops / vendor hygiene
4. **Make prompts self-contained.** Include workspace paths, audit paths, allowed side effects, forbidden actions, final report path, and repo-specific gates in every worker prompt.
5. **Require real verification.** A worker may only call a repo ship-ready if it ran the relevant build/test/security/browser checks or documented a hard blocker.

## Claude Code rate-limit handling

Claude Code can be authenticated but still unable to run because the account is at a session limit. Do a tiny print-mode smoke test before launching an expensive fan-out:

```bash
claude -p 'Reply with READY only.' --max-turns 1 --output-format text
```

If it reports a reset time, do not abandon the job. For non-urgent work, queue a delayed launcher for just after reset, then notify the user that it is armed.

## Safe delayed tmux launcher pattern

When queueing delayed Claude Code workers:

- Write prompts to files under the project/audit workspace.
- Pass prompt files to `claude -p "$(cat prompt.md)"` inside tmux panes.
- Log every pane to a per-run logs directory.
- Have every worker write a final report file to a known reports directory.
- Monitor report-file completion from the launcher.
- Keep Hermes as verifier after the run completes.

## Shell quoting pitfall

Do **not** generate prompt files by executing markdown content through shell heredoc expansion. Markdown may contain backticks, `$()`, quotes, paths, or arbitrary snippets. Treat prompt content as data, not shell code.

Safer approach:

```bash
cat > "$PROMPTS/common.md" <<'EOF'
...literal prompt text...
EOF

{
  cat "$PROMPTS/common.md"
  printf '\n\n# %s\n\n%s\n' "$title" "$body"
} > "$prompt_file"
```

Then pass the prompt file to the coding agent from tmux.

## Ship-ready guardrails

Workers may create branches, edit files, run tests, commit, and push PR branches when the user has authorized it. They must not:

- merge to default branches,
- delete large code/vendor trees,
- expose secrets in docs/logs/PRs,
- call anything ship-ready without passing commands or a documented blocker,
- rewrite architecture unless required by a verified blocker.

## Reporting requirement

Each worker final report should include:

- repos touched,
- branches and commits,
- PR URLs if created,
- commands run and pass/fail summaries,
- ship/no-ship status,
- remaining blockers.

The release-manager worker should synthesize all reports into the final ship matrix.