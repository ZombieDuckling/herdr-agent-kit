# abstraction boundary review checklist

Use this before trusting an AI/software workflow whose result depends on several
layers: prompts, files, model calls, scripts, APIs, storage, runtime, or human
approval.

- [ ] The user-visible job is stated without vendor or model jargon.
- [ ] Every active layer is named: interface, context, instruction,
      deterministic code, model, tool/API, state, substrate, and human review.
- [ ] Each boundary says what crosses it: instruction, data, evidence, state,
      authority, or secret.
- [ ] Secrets and private data stay outside editable/exportable workspace files.
- [ ] Public method/process files are auditable without granting secret access.
- [ ] Exact, current, arithmetic, file, git, hash, date, and external-state
      claims have tool/source/test/read-back evidence.
- [ ] Model confidence is treated as a hypothesis until another layer verifies
      the claim.
- [ ] API/tool contracts list inputs, outputs, permissions, side effects,
      failure modes, idempotency, and read-back verification.
- [ ] Raw retrieved/source text is labeled as data, not instruction authority.
- [ ] Deterministic validators parse model output before it becomes trusted
      state or a side effect.
- [ ] Lower-layer failures are considered: stale cache, dropped network call,
      clock drift, partial write, storage corruption, process timeout, or
      hardware/runtime error.
- [ ] Human review sees artifacts, diffs, source handles, logs, or receipts, not
      only a prose summary.
- [ ] The final acceptance note names which boundary checks passed and which
      assumptions remain open.
