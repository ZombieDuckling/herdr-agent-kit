# decision-gate control plane

Use this shape when a repeated workflow step needs a bounded judgment rather than open-ended generation.

A decision gate is a folder-local policy file plus a result record. It turns questions like "what type is this?", "is this ready?", "which route should this take?", or "should this stop for review?" into a small, auditable contract.

## components

- **Decision file:** the local markdown spec for the gate: scope, inputs, questions, allowed outputs, thresholds, deterministic exclusions, and escalation behavior.
- **Exact checks:** scripts or schema validators for facts that must not be guessed: counts, dates, hashes, totals, file presence, parse validity, or policy allowlists.
- **Classifier-shaped worker:** the smallest qualified mechanism that returns a label, yes/no answer, bounded score, or route with confidence.
- **Result record:** a machine-readable output beside the source artifact, including answer, confidence, worker/version, evidence pointer, and action taken.
- **Review lane:** where low-confidence, high-consequence, or overridden cases go before external action.
- **Override ledger:** reviewer corrections that become future truth-deck/eval cases.

## routing rule

1. If the answer is exact, use code or a tool.
2. If the answer is a bounded fuzzy judgment, use a decision gate.
3. If the answer requires synthesis, explanation, writing, or novel design, use an LLM with review.
4. If the outcome changes authority, money, safety, reputation, or external state, require human approval unless a separate policy explicitly delegates it.

## folder layout

```text
workflow/
  DECISION.<gate-name>.md
  inputs/
  results/
    <artifact-id>.decision.json
  overrides/
    <artifact-id>.override.md
  evals/
    cases.jsonl
```

## result fields

- `gate_id`
- `source_ref`
- `question_id`
- `allowed_output`
- `confidence`
- `threshold_band`
- `action_taken`
- `exact_checks_run`
- `review_required`
- `worker_ref`
- `created_at`
- `override_ref`

## acceptance tests

- A fresh worker can find the decision file from the workbench map.
- Exact checks run outside the language judgment path.
- The gate can return only the allowed outputs plus a declared fallback such as `other` or `needs_review`.
- Threshold bands map to actions before the worker runs.
- Low-confidence and high-consequence cases cannot disappear into chat history.
- Reviewer overrides are stored beside the source and are usable as regression cases.
