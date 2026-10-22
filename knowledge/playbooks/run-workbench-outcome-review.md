# run a workbench outcome review

Use this after a training session, workbench build, pilot, or internal AI workflow has had enough time to affect real work. The goal is not a satisfaction survey. The goal is to inspect what changed, prove the outcome, and feed the finding back into the reusable system.

## inputs

- Original request, proposal, or acceptance criteria.
- Current workbench, artifacts, or deployed workflow.
- User/operator notes since the original delivery.
- Usage, defect, support, cycle-time, cost, or adoption evidence.
- Known blockers, abandoned paths, and follow-on builds.

## review steps

1. **Recover the original promise**
   - What was the work supposed to make possible?
   - What counted as done at the time?
   - Which constraints, risks, or review gates were named?

2. **Inspect the current architecture**
   - Inputs: what source material enters the workflow?
   - Stages: what files, scripts, tools, model calls, and human checks transform it?
   - Outputs: what artifacts, records, decisions, or user-facing changes are produced?
   - Ownership: who maintains each stage?
   - Failure modes: what breaks, stalls, leaks, confuses users, or remains manual?

3. **Capture actual outcomes**
   - Direct outcome: time saved, risk reduced, errors prevented, revenue enabled, or cycle shortened.
   - Follow-on outcome: new work created because the team learned the pattern.
   - Adoption evidence: who used it, how often, and where behavior changed.
   - Negative evidence: where the work was unused, misunderstood, blocked, or too costly.

4. **Extract reusable learning**
   - Which definitions or concepts were misunderstood?
   - Which stage needed a missing template, checklist, script, example, or interface?
   - Which operator judgment is still tacit and should be encoded?
   - Which part belongs in a template, mutable workbench, archive, product backlog, or stop decision?

5. **Assign one next change**
   - Owner.
   - Target artifact or system surface.
   - Verification evidence.
   - Deadline or review trigger.

## output

Write an outcome review record with:

- original promise,
- current architecture map,
- outcome evidence,
- blockers and failure modes,
- reusable changes made or queued,
- owner and next verification.

## acceptance test

A second operator can read the record and explain what changed in the real workflow, what evidence supports the claim, what failed or remains blocked, and which reusable asset must be updated next.
