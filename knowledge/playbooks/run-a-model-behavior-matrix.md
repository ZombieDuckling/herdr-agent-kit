# run a model-behavior matrix

Use this when the claim is about how a model or agent behaves across tasks,
roles, instruments, or settings, not merely whether one workflow output passed.

## define the matrix first

Before collection, write the dimensions:

- subject: model or worker profile, harness, tools, and verifier version;
- items: task cases, survey items, scales, prompts, or scenarios;
- role framing: system prompt, persona, policy frame, or neutral baseline;
- parameters: temperature, decoding settings, context length, retries, timeout;
- run count per cell;
- parser and scorer version;
- success, refusal, parse-error, timeout, exclusion, and rate-limit categories;
- export locations for raw and normalized records.

## collect

1. Freeze the subject profiles and item set.
2. Run every planned cell or record an explicit exclusion.
3. Store raw outputs privately when needed for audit.
4. Parse and score with deterministic code wherever the response shape allows.
5. Preserve malformed outputs instead of overwriting them with cleaned prose.
6. Export normalized JSON or CSV with enough metadata to reproduce the cell.

## report

The report should separate:

- collection success rate;
- refusals;
- parse errors;
- timeouts and unavailable subjects;
- per-item or per-task scores;
- variance across repeated runs;
- limitations and confounders;
- interpretation that follows from the data.

Do not let the interpretation layer become the evidence. The reusable artifact is
the matrix and its preserved records.
