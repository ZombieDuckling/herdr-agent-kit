# AI workflow resilience checklist

Use this before relying on an AI workflow for recurring, customer-facing, paid,
scheduled, or otherwise time-sensitive work.

## portable state

- [ ] The current goal, status, inputs, decisions, and outputs are stored outside
      the model chat.
- [ ] A fresh runtime can find the front desk, manifest, request slip, source
      material, and verification path.
- [ ] Important artifacts are written to durable storage before the session ends.

## model and provider boundary

- [ ] The preferred model/provider/tool is named as the current runtime, not as
      the workflow's source of truth.
- [ ] Model calls are behind a stable task contract, schema, or checklist.
- [ ] Business rules that must not drift are encoded in files, tests, or
      deterministic code.
- [ ] Provider-specific features have a plain-file equivalent or documented
      migration note.

## fallback paths

- [ ] At least one alternate hosted runtime is named.
- [ ] At least one local, scripted, or manual continuation path is named.
- [ ] The fallback path has access to the same source files and acceptance
      criteria.
- [ ] The workflow says what stops safely if no AI path is available.
- [ ] The operator/user message for degraded mode is honest and bounded.

## model-change evaluation

- [ ] A truth deck or representative task set exists for repeated work.
- [ ] The truth deck includes must-include, must-avoid, quality, cost, and latency
      expectations where relevant.
- [ ] Model, prompt, adapter, or provider changes are compared against the deck
      before becoming default.

## verification

- [ ] Verification does not depend on the same model's fluent self-report.
- [ ] Fallback output is checked with tests, schemas, source links, reviewer
      inspection, or other independent evidence.
- [ ] Incident notes identify the failing layer: prompt/context, model, adapter,
      tool, runtime, network, data source, or external service.

## fail condition

Do not call the workflow production-ready if an outage or model swap would leave
only an unrecoverable chat transcript and a vague promise to rerun the work later.
