# run a domain-expert discovery workbench

Use this when a client, team, or operator asks for an AI build but the practical
requirements live in the workarounds domain experts already created.

## steps

1. **Name the job.** Write the outcome, user, reviewer, value, failure mode, and
   first acceptance proof without naming an AI tool.
2. **Run or collect the cheap baseline.** Capture what ordinary chat, office
   tools, templates, scripts, or the existing manual process already achieve.
3. **Ingest source attempts.** Collect rough prompts, outputs, spreadsheets,
   screenshots, scripts, notes, examples, and failed automations into a private
   source-attempts area.
4. **Sanitize or isolate.** Keep private data out of shareable notes; use source
   classes and redrawn examples when the actual material identifies people,
   accounts, infrastructure, or businesses.
5. **Extract requirements.** Pull vocabulary, edge cases, repeated decisions,
   missing data, adoption blockers, and desired output shapes from the attempts.
6. **Build a mechanism map.** Classify each step as manual, checklist, script,
   ordinary software, one-shot model call, agent loop, managed tool, or custom
   integration.
7. **Reject simpler mechanisms explicitly.** For every model, agent, or
   integration, state why a process change, checklist, script, or one-shot call is
   insufficient.
8. **Build one prototype slice.** Implement the smallest workflow segment that
   closes a baseline gap and creates reviewable output.
9. **Evaluate with a truth deck.** Test representative examples, edge cases,
   must-include/must-avoid rules, latency, cost, and human review burden.
10. **Update the ledger.** Record the attempt that caused each change, the files
    or process touched, verification evidence, and remaining manual checkpoints.
11. **Decide whether to scale.** Expand only if the slice proves business value
    beyond the cheap baseline.

## outputs

The workbench should contain:

- front desk with job, impact, constraints, and acceptance proof;
- source-attempt manifest;
- questions-and-decisions log;
- mechanism map;
- prototype slice and review artifacts;
- truth deck/eval cases;
- implementation ledger;
- scale/no-scale decision.

## stop conditions

Stop before custom software if the cheap baseline already solves the job, if the
only missing layer is a prompt/template/checklist, or if source attempts reveal
that the requested tool is not the real business outcome.
