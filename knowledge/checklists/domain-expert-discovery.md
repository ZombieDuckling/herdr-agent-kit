# domain-expert discovery checklist

Use this before accepting a consulting, advisory, or product brief that claims it
needs AI.

## baseline and job

- [ ] The business outcome is written without model, vendor, or agent jargon.
- [ ] The current manual process or cheap-tool baseline has been observed or
      captured.
- [ ] The brief states what the baseline already solves.
- [ ] The brief states what the baseline cannot solve and why that gap matters.
- [ ] Expected value is tied to time, error rate, adoption, revenue, compliance,
      support cost, or another concrete business measure.

## source attempts

- [ ] Domain-expert attempts are collected or their absence is explained.
- [ ] Prompts, outputs, spreadsheets, screenshots, scripts, examples, and failed
      automations are treated as source evidence.
- [ ] Sensitive or identifying material is stripped, isolated, or replaced with
      safe source classes before the workbench is shared.
- [ ] Extracted requirements include vocabulary, edge cases, desired output
      shapes, constraints, and adoption blockers.

## mechanism fit

- [ ] Each workflow step is classified as manual, checklist, script, ordinary
      software, one-shot model call, agent loop, managed tool, or custom
      integration.
- [ ] Deterministic rules and reference data are outside prompts where practical.
- [ ] Every model call has a named reason: language ambiguity, extraction,
      synthesis, ranking, coaching, or bounded tool choice.
- [ ] Every agent loop is justified by branching, tool selection, recovery, or
      source navigation.
- [ ] Simpler rejected mechanisms are recorded with reasons.

## proof and scale

- [ ] A prototype slice proves one missing layer before platform scale-up.
- [ ] Truth-deck cases cover representative successes, failures, and edge cases.
- [ ] Cost, latency, reliability, and human review burden are measured.
- [ ] The implementation ledger links changes to source attempts or decisions.
- [ ] Remaining manual checkpoints are intentional, named, and reviewable.
- [ ] The scale decision is based on business receipts beyond the cheap baseline.
