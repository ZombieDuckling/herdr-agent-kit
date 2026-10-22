# decision-gate readiness checklist

Use this before replacing a repeated model judgment with an automatic gate.

## fit

- [ ] The output is a label, yes/no answer, bounded score, route, or readiness decision.
- [ ] The allowed outputs are known before the run.
- [ ] The workflow repeats often enough that cost, latency, consistency, or auditability matters.
- [ ] Open-ended synthesis, explanation, writing, and novel design remain outside the gate.

## exact-work separation

- [ ] Counts, dates, totals, hashes, file presence, and schema validity are handled by code or tools.
- [ ] Required fields and allowlists are checked deterministically.
- [ ] The gate consumes exact-check results rather than re-inferring them.

## policy

- [ ] Confidence bands are explicit.
- [ ] Each band maps to an action before execution.
- [ ] High-consequence decisions have a human approval rule.
- [ ] There is a safe fallback if the classifier/model is unavailable.

## artifacts

- [ ] The decision file lives beside the workflow stage it governs.
- [ ] Result records are persisted beside source artifacts.
- [ ] Review and override records are linkable from the result.
- [ ] Overrides become eval/truth-deck cases.

## acceptance

- [ ] A fresh worker can explain when to use code, the gate, a full LLM, or a human.
- [ ] The gate cannot emit unlisted outputs silently.
- [ ] Low-confidence cases are visible and do not trigger irreversible action.
