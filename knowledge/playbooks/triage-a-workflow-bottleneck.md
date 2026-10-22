# triage a workflow bottleneck before choosing the mechanism

Use this before learning a new tool, buying a course, hiring help, writing a
script, adding model calls, or building an agent. The goal is to spend attention
only on mechanisms that remove a valuable bottleneck.

## output

Produce a short bottleneck decision note with:

- problem and user or buyer;
- blocked outcome and why it matters now;
- current manual path;
- bottleneck type;
- scarce human time at stake;
- candidate mechanisms and rejected mechanisms;
- first accepted result that will prove the choice worked.

## procedure

1. **Name the valuable problem.** State the outcome in user terms, not tool or
   learning terms.
2. **Find the blocker.** Classify it as missing judgment, missing taste, missing
   data, deterministic repetition, transfer/copy work, source navigation, review
   load, permission boundary, or delivery capacity.
3. **Price the constrained hour.** Estimate whose time is scarce, what that hour
   could otherwise produce, and what quality or authority cannot be delegated.
4. **List mechanisms from cheap to heavy.** Consider doing nothing, checklist,
   markdown workflow, template, delegation, deterministic script, one model call,
   bounded agent, or full integration.
5. **Reject tools explicitly.** For every attractive tool, course, hire, or
   automation, write the bottleneck it would remove. If there is no bottleneck,
   reject it for now.
6. **Keep judgment visible.** Preserve checkpoints for taste, authority,
   consequential review, or missing context instead of automating through them.
7. **Run one real case.** Do the smallest real task that can produce an accepted
   output and show that the bottleneck moved.
8. **Record the next escalation trigger.** Only move to a heavier mechanism when
   repetition, volume, quality, speed, governance, or sharing creates a new
   constraint.

## mechanism ladder

| blocker | first mechanism to try | escalate when |
| --- | --- | --- |
| unclear goal | request slip | repeated slips share the same structure |
| repeated explanation | markdown workflow or skill | a fresh operator still cannot reproduce it |
| deterministic transformation | script | exceptions require bounded judgment |
| data transfer or prep | template or delegation | volume or error rate justifies automation |
| source navigation | index or manifest | corpus size makes manual lookup unreliable |
| taste or strategy | expert first draft and review checkpoint | variants are needed from a stable direction |
| bounded tool choice | one model call or agent | branch/retry behavior is frequent and valuable |
| permissions or scale | governed integration | manual operation becomes the delivery risk |

## stop conditions

Stop before investing when:

- no buyer, user, or accountable outcome is named;
- no first accepted result can be tested this week;
- the proposed mechanism only teaches a tool without moving the problem;
- the scarce human hour is not actually constrained;
- the mechanism would hide a human authority or taste decision.

Related laws: [MECH-1](../notes/10-mechanism-selection.md#mech-1-name-the-job-before-naming-the-tool),
[MECH-7](../notes/10-mechanism-selection.md#mech-7-automate-only-after-the-manual-workflow-teaches-its-boundary),
and [MECH-14](../notes/10-mechanism-selection.md#mech-14-learn-or-delegate-only-against-a-valued-bottleneck).
