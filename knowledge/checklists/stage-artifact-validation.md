# stage artifact validation checklist

Use this when an automation, cron, report generator, proposal workflow, or agent
pipeline is green but a wrong intermediate input would still produce a polished
wrong output.

## stage boundaries

- [ ] The workflow is split at the points where a competent human would naturally
      pause and inspect before continuing.
- [ ] Each stage has one named input set and one named output artifact.
- [ ] A failed stage can be rerun from its last trusted artifact without rerunning
      the whole pipeline.
- [ ] Stage size is small enough that checking it is faster than doing it
      manually; otherwise split it again.

## artifact contract

For every stage, record:

| stage | input artifact | output artifact | cheap check | rerun-from-here command/procedure | reviewer/gate |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Minimum checks:

- [ ] Source freshness is checked where stale input would be harmful.
- [ ] The expected identity, count, date, revision, or row set is asserted before
      downstream stages consume the artifact.
- [ ] Output existence is not enough; shape and key content are checked.
- [ ] Any external or high-consequence delivery has a human sign-off gate after
      the last inspectable artifact and before the side effect.

## monitoring claim

- [ ] Process health is labeled as process health, not content correctness.
- [ ] Final reports distinguish "the job ran" from "the source and output were
      checked."
- [ ] A green dashboard/run status is never the only acceptance evidence.
- [ ] Failed checks name the artifact and stage that blocked progress.

## acceptance

- [ ] A fresh reviewer can inspect the artifact registry and verify each stage
      without replaying chat history.
- [ ] The pipeline has at least one seeded stale/wrong-input case that fails at
      the right stage.
- [ ] The runbook states whether to stop, rerun a stage, ask for human review, or
      continue in degraded/manual mode.
