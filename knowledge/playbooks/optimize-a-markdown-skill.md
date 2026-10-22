# optimize a markdown skill

Use this playbook when a routing file, skill, project instruction, or reusable
prompt keeps receiving the same correction. The goal is not a longer instruction
file. The goal is a smaller operational asset that performs better on repeated
work.

## output

Produce a completed `templates/skill-evaluation-record.md` and, when a new
portable skill is needed, start from `templates/markdown-workflow-skill.md`.
When an existing skill is adopted, keep the diff small and tied to the evaluated
case.

## procedure

1. **Name the skill's job.** State the valuable problem and the one workflow,
   routing decision, voice constraint, or tool-use procedure the file is
   supposed to control.
2. **Freeze the current version.** Record the exact path, revision, included
   files, model or runner if relevant, and authority boundary.
3. **Collect representative tasks.** Use real requests, edge cases, and prior
   failures. Each task needs expected behavior, must-include rules, must-avoid
   rules, allowed sources/tools, and a review method.
4. **Run before editing.** Execute the frozen skill on the task set and preserve
   failures. Do not edit from vibes or from one impressive sample.
5. **Classify the failure.** Decide whether the problem is missing instruction,
   stale instruction, ambiguous routing, excess context, missing example,
   wrong tool contract, or an upstream workflow problem.
6. **Make the smallest structural edit.** Prefer deleting, clarifying, splitting,
   or moving instructions over appending another paragraph. If the file serves
   two unrelated jobs, split it.
7. **Rerun the same tasks.** Compare against the frozen baseline on correctness,
   review effort, token/context load, latency, and failure rate.
8. **Decide.** Keep, revise, split, or retire the skill. Adopt only when the
   revised version improves the repeated task set without adding new material
   review debt.
9. **Promote recurring failures.** Turn repeated misses into regression tasks,
   checklists, tool-registry updates, or stable laws. Do not place every incident
   into global memory.

## stop conditions

Stop and repair the evaluation when the task set is too small, expected behavior
is unwritten, the reviewer cannot distinguish better from different, or the
skill under test can mutate protected state during evaluation.

## compression rule

A skill edit that fixes one case by making every future run read irrelevant text
is a debt transfer, not an optimization. Measure the behavior gain and the
context cost together.
