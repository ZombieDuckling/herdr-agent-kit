# graduate automation deliberately

Use this playbook when a team wants an agent, integration, or full automation but
has not yet proved the underlying human workflow.

## principle

Automate only the parts of the workflow whose inputs, outputs, review criteria,
and failure handling are stable. Keep human judgment where taste, accountability,
missing context, or high consequence still matter.

## ladder

| level | use when | evidence to advance |
| --- | --- | --- |
| Human-only execution | The operator is still learning what good looks like | Accepted examples and rejected examples exist |
| Markdown workflow | The steps can be described but are still changing | A fresh operator can follow the file and produce a comparable result |
| Template or copy/paste bridge | Frequency is low or integration cost is high | The manual transfer is now the bottleneck |
| Deterministic helper | The step is parsing, formatting, validation, movement, or conversion | Same input shape repeatedly yields the same expected output |
| One-shot model call | The step is bounded classification, summarization, rewriting, or drafting | A truth deck passes under human review |
| Agentic loop | The step requires tool choice, retries, branching, or source navigation | Logs show simpler scripts or single calls fail for predictable reasons |
| Full integration | Volume and value justify maintenance | Tests, monitoring, rollback, cost controls, and ownership exist |

## procedure

1. Write the job, output, review surface, failure cost, and reinvestment target
   for any time or spend the automation is expected to release.
2. Capture the successful manual workflow in markdown.
3. Run a fresh-operator pressure test on a new input.
4. Mark each step as judgment, transfer, deterministic rule, bounded model call,
   agentic loop, or integration.
5. Automate the cheapest stable bottleneck first.
6. Keep approval gates on steps whose errors have high consequence or ambiguous
   accountability.
7. Add inspectable stage artifacts and cheap checks before downstream stages
   consume the output.
8. Re-run the same pressure test after each automation change.
9. After adoption, check whether released capacity actually moved into the named
   backlog item, quality gate, internal capability, faster delivery, or reduced
   dependency.

## stop conditions

Do not advance the mechanism when:

- nobody can state what accepted output looks like;
- the ROI case counts saved time but cannot name where that capacity will go;
- the proposed agent repeats the same deterministic steps every run;
- a plain file, template, or checklist would solve the current friction;
- the workflow still depends on tacit expert narration;
- the system cannot expose a review artifact and rollback path.

## receipt

A graduated automation change should leave behind:

- the original workflow file;
- the step classification table;
- the simpler mechanisms rejected and why;
- the stage artifact table and checks that distinguish process liveness from
  content correctness;
- test or truth-deck results;
- cost and review-time impact;
- the reinvestment target and delivered higher-level outcome;
- remaining human intervention points.
