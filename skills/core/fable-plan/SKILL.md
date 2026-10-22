---
name: fable-plan
description: Load when a task has more than 3 steps, involves workers, or touches something that cannot be undone. The Fable planning process - work backwards from the goal, put risky unknowns first, mark who does each step, name a check for every step, ask the user's decisions early and together, re-plan when facts change.
---

# Plan like Fable

A plan is a list of steps where **each step has a check**, the **riskiest step comes first**, and
**every decision that needs the user is found early**. A plan you keep after the facts proved it wrong is
worse than no plan.

## Procedure

1. **Start from DONE MEANS and work backwards.** What is the last step? What must be true before it?
   Repeat until you reach the current state. Then reverse the list.
2. **Find the risky step.** Which step, if it fails, makes the rest useless? (The right starting
   version, access to a server, a tool that may not work, a permission that may be refused.) Move it,
   or a check for it, to the front.
3. **Mark who does each step:**
   - `[me]` judgement, design, anything touching shared or live state, short command chains
   - `[worker]` long mechanical work to an exact spec (see the lead skill for limits)
   - `[the user]` their permission, their account, their decision, their hands (passwords, dashboards, devices)
4. **Mark what can run at the same time.** Independent steps: start the slow one first, do the fast
   one yourself meanwhile.
5. **Write the check for each step.** No check = not planned.
6. **Collect all `[the user]` items now.** Ask them together, in one message, each with your
   recommendation (`fable-decide`). Keep working on everything that does not depend on them.
7. **Write it down** (notes file):

```
PLAN: <goal>
1. [me]     <step>                       check: <command / number>
2. [worker] <step>                       check: <command / number>
3. [the user]   <decision or action>         asked: <time>
4. [me]     <step, needs 3>              check: <...>
RISKY FIRST: step <n>, because <reason>
CANNOT UNDO: steps <n> - need the user's word for each
```

## Rules

- **Size the plan to the task.** 1-3 steps: one line. A plan longer than the work is waste.
- **Prefer the simple path.** Fifteen commands you run yourself beat a worker that takes an hour. A
  worker beats you only for long, mechanical, well-specified work.
- **Reversible first.** Do everything that can be undone and checked locally before anything that
  cannot (push, deploy, send, delete).
- **Backups before destruction.** Before you delete or overwrite, save a copy and say where.
- **Re-plan on new facts.** When a check shows something unexpected, write
  `PLAN CHANGED: <what you learned>` and the new plan. Do not force the old plan.
- **Leave the plan visible.** The next agent or the user must be able to continue from it.

## Example

Task: "pull the published version and give it a UI upgrade, keep the vibe, do not push."

```
PLAN: UI upgrade of the live version, local only
1. [me]     find which commit is live           check: live bundle hashes = local build hashes
2. [me]     snapshot it as a branch             check: build hash matches again
3. [worker] before-screenshots, desktop+phone   check: files exist, I look at them
4. [me]     design changes, page by page        check: build passes after each page
5. [worker] WebP versions of client photos      check: count, sizes, verify script
6. [worker] axe + console + link sweep          check: I re-run them
7. [me]     after-screenshots, compare          check: vibe kept, contact facts identical
RISKY FIRST: step 1 - everything is wasted if we upgrade the wrong version
CANNOT UNDO: none planned; push/deploy wait for the user
```
