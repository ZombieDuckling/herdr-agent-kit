# Originality Refactor Waves

Use this reference when the user asks for a very large number of coding agents (for example, "fire off 100 agents") to make a repo substantially more original, less derivative, safer, or more production-worthy.

## Pattern

1. **Do not literally spawn an uncontrolled swarm.** Treat the number as intensity/urgency. Explain briefly that uncontrolled parallel edits create conflicts, then run a structured wave.
2. **Start with read-only specialist fan-out.** Use 3–5 planning/review workers with non-overlapping lenses:
   - product architecture / differentiation,
   - security and safety posture,
   - UX/CLI/reporting identity,
   - implementation risk / migration path,
   - optional docs/packaging.
3. **Extract consensus into one Phase 1 implementation brief.** Prioritize changes that prove the repo is no longer a thin port: stale upstream strings, wrong platform assumptions, unsafe inherited behavior, first-run/doctor workflow, branding/reporting, dependency installability.
4. **Assign a bounded build worker, but do not wait on agent permission dead-ends.** If a coding agent refuses or asks for file-write approval inside its own run, take over directly or rerun with the right force/permission mode. The deliverable is changed code, not a worker request for approval.
5. **Verify with real commands, not self-reports.** At minimum run compile/static checks, CLI smoke tests, safety behavior tests, environment/doctor output, and dependency install checks when requirements changed.
6. **Use a review worker after implementation.** Ask for merge-blocking bugs only. Patch anything actionable, then rerun the targeted verification.
7. **Commit and push a coherent first wave.** Open a PR with summary + exact verification commands so the work is visible and reviewable.

## Useful Phase 1 targets for de-porting a repo

- Replace stale upstream branding/links in reports, prompts, banners, docs, and filenames.
- Remove wrong platform instructions (`apt`, `systemctl`, MariaDB on a SQLite/macOS project, etc.).
- Add a `doctor`/environment-check command for the target platform.
- Convert unsafe inherited dispatch patterns from denylist/raw shell to explicit allowlists.
- Add authorization/scope guardrails for security tools.
- Enforce privacy-sensitive local defaults, with explicit opt-in env vars for remote endpoints.
- Make requirements/install steps actually resolve on the active supported runtime.

## Pitfalls

- A successful `py_compile` is not enough. Import-time dependency failures can still break the CLI; run an actual noninteractive smoke test such as `printf '4\n' | python3 metatron.py`.
- Dependency install fixes can create host environment conflicts. If pip reports a resolver conflict, adjust the requirements and restore compatibility before finalizing.
- External agent scratch directories (for example `.omc/`) may be created during reviews. Remove generated scratch state before committing.
- A review worker can be wrong about already-safe code. Apply the spirit of the finding if cheap, but verify rather than blindly accepting it.
