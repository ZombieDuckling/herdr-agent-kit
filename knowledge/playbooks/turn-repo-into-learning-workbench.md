# turn a repository into a learning workbench

Use this when onboarding to a codebase or teaching a workflow from real source. The goal is not a generic tutorial; it is a runnable path through the actual system.

## prerequisites

- Repository or source package available in a safe local workspace.
- Read-only source map of the main directories, commands, and entry points.
- Permission boundary for what learners may edit, run, or publish.

## steps

1. **Map the source first.** List entry points, core modules, tests, build commands, fixtures, and unsafe paths to avoid.
2. **Define the learner outcome.** State the job the learner must be able to do: run the app, change a component, fix a bug, add a route, inspect data, or operate a workflow.
3. **Create staged lessons.** Each lesson should include explanation, source pointers, a small exercise, expected output, and a verification command or review handle.
4. **Use notebooks only when execution helps.** A notebook is useful for runnable examples, inspection, and incremental exercises; plain markdown is enough for orientation or review-only tasks.
5. **Add failure-safe exercises.** Prefer tiny reversible edits, local fixtures, test-only changes, and deliberate failure cases that reveal how the system behaves.
6. **Record gap discoveries.** When the learner fails, capture the missing concept, source area, command, or assumption as a learning backlog item.
7. **Keep generated lessons source-linked.** Every exercise must point back to real files, tests, commands, or docs; remove generic filler.

## lesson unit template

```md
## Lesson N: <outcome>
- Source pointers:
- Concept:
- Exercise:
- Expected output:
- Verification:
- Common failure:
- Follow-up gap:
```

## verification

The workbench passes when a new learner can run the lessons, modify a safe part of the system, explain the relevant control flow, and name the remaining gaps without rereading the entire repository.
