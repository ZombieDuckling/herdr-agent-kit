# build a truth deck

Use this before changing the model, provider, prompt, tools, or routing for a
repeated AI workflow.

## steps

1. Name the workflow outcome the deck protects.
2. Pick 5-20 representative cases from real work, not synthetic edge cases only.
3. For each case, record the input/context and expected output characteristics.
4. Add must-include items, must-avoid items, and the human rationale.
5. Set quality, latency, and cost thresholds.
6. Run the current system and record baseline results.
7. Run the proposed change on the same cases.
8. Compare pass/fail, cost delta, latency delta, and qualitative regressions.
9. Accept the change only if the tradeoff is explicit.

If the claim is about model behavior rather than one workflow's output quality,
use [the model-behavior matrix playbook](run-a-model-behavior-matrix.md) so the
subject, role framing, instruments, parameters, repeated runs, parsers, refusals,
and exports are explicit.

## keep it small

Do not build an evaluation bureaucracy for one-off research. Start with a few
cases that would be expensive to regress. Add cases only when new failures teach
the deck something useful.

## output

The change report must include:

- cases run;
- failures and regressions;
- quality changes;
- latency and cost deltas;
- accepted tradeoffs;
- rollback or fallback path.