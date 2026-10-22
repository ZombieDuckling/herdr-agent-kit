# build a decision gate

Use this when a repeated AI step only needs a label, yes/no answer, bounded score, route, or readiness judgment.

## 1. Name the bounded question

Write the exact question the workflow needs answered. If the answer is prose, synthesis, explanation, or invention, this is not a decision gate.

Good gate questions:

- Which document type is this?
- Is this artifact ready for human review?
- Does this request belong in route A, route B, or `other`?
- Should this run report, fail, or stay silent?

## 2. Remove exact work

Move deterministic checks out of the classifier path:

- file existence;
- schema validity;
- counts, dates, totals, hashes;
- allowlist/denylist membership;
- required-field presence;
- external-state read-backs.

If a script can know it, do not ask a model to feel it.

## 3. Write the decision file

Create `DECISION.<gate-name>.md` beside the workflow stage. Include:

- scope and input paths;
- output path and result schema;
- allowed answers;
- confidence thresholds;
- deterministic exclusions;
- high-consequence escalation rules;
- fallback when the worker is unavailable;
- override-to-eval loop.

## 4. Choose the smallest worker

Prefer the cheapest qualified mechanism that can return the bounded answer with confidence and stable formatting. This may be rules, a small classifier, a one-shot model constrained to a schema, or a larger model only when the boundary is still being discovered.

## 5. Bind thresholds to actions

Do this before running the gate:

- high confidence: act automatically only inside the authorized scope;
- middle confidence: proceed with visible flag, or require review before external action;
- low confidence: stop for human review;
- high consequence: require review even if confidence is high unless separately delegated.

## 6. Persist results beside sources

Store the result record where the next worker or reviewer can find it. Include the source pointer, answer, confidence, exact checks run, action taken, and review requirement.

## 7. Convert overrides into evals

Every human override should produce a regression case: source pointer, original answer, corrected answer, reason, and whether labels/rubrics changed.

## Done means

- exact checks and fuzzy judgments are separated;
- outputs are bounded and machine-readable;
- threshold behavior is explicit;
- results and overrides are durable files;
- the gate can fail closed without losing the workflow;
- review cases improve the next run instead of staying in chat.
