# automation readiness checklist

Use this before replacing a human workflow, markdown procedure, or simple script
with an agentic loop or full integration.

## workflow proof

- [ ] The business/job outcome is named without tool or model jargon.
- [ ] Any expected time or spend savings have a named reinvestment target, such
      as a deferred backlog item, quality gate, internal capability, faster
      delivery path, or reduced dependency.
- [ ] Accepted and rejected examples exist.
- [ ] A markdown workflow describes inputs, steps, assumptions, outputs, and
      review criteria.
- [ ] A fresh operator can reproduce the result from the files without live
      narration from the original expert.
- [ ] Human judgment points are explicitly marked.

## mechanism fit

- [ ] Deterministic parsing, formatting, validation, and file movement have been
      considered before model calls.
- [ ] Repeated label, yes/no, score, route, and readiness judgments have been
      considered as decision gates before full LLM or agent calls.
- [ ] One-shot model calls have been considered before agentic loops.
- [ ] Agentic loops are justified by bounded tool choice, retries, branching, or
      source navigation.
- [ ] Full integration is justified by repeated volume, value, and stable edge
      cases.
- [ ] Simpler mechanisms rejected are recorded with reasons.

## controls

- [ ] Review artifacts are visible before any irreversible action.
- [ ] Intermediate stage artifacts are visible and covered by the
      [stage artifact validation checklist](stage-artifact-validation.md) before
      a green run is treated as a correct run.
- [ ] Approval gates remain on high-consequence or ambiguous steps.
- [ ] Cost, latency, and review time are measured.
- [ ] Tests or truth-deck cases cover representative inputs.
- [ ] Monitoring, rollback, and ownership are defined for integrated automation.

## acceptance

- [ ] The automated version passes the same pressure test as the manual workflow.
- [ ] The change reduces a real bottleneck rather than only adding technical
      sophistication.
- [ ] The post-adoption receipt can show where released capacity was used.
- [ ] Remaining manual steps are intentional, named, and reviewable.
