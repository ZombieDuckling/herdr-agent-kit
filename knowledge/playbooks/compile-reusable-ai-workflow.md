# compile a reusable AI workflow

Use this when a prompt, chat routine, or ad hoc agent task is being repeated and
needs to become a durable workflow without prematurely becoming a custom agent.
Use `../templates/prompt-workflow-compiler-map.md` as the fill-in record.

## steps

1. **Name the job.** Write the user, outcome, acceptance proof, and non-goals.
2. **Run the cheap baseline.** Try the simplest manual, chat, script, or existing
   software route first. Record what it already solves and what gap remains.
3. **Separate fixed from variable.** Move stable instructions into the workflow;
   store changing source data in files, tables, manifests, forms, or records.
4. **Define the role/context slot.** State which audience, tone, domain frame, or
   local assumptions may vary per run.
5. **Choose the output contract.** Prefer a schema, named sections, filenames, or
   fields when another worker or program must consume the result.
6. **Pick the execution envelope.** Record the model/provider class, context
   budget, tool access, temperature, retry budget, and privacy boundary.
7. **Add validation before trust.** Use parse checks, source-link checks, diffs,
   tests, truth-deck cases, review handles, or human approval thresholds.
8. **Write the error policy.** Decide when to retry, narrow the task, fall back to
   a simpler mechanism, escalate to a human, or stop with a failure receipt.
9. **Persist accepted state.** Store the accepted output, source pointers,
   verification receipt, and unresolved risks outside the chat session.
10. **Reassess mechanism fit.** If copy/paste, volume, validation, or retry logic
    dominates, graduate the stable parts into scripts or a governed harness.

## done means

- A fresh worker can run the workflow from files without reading the original
  chat.
- The prompt does not mix source data with authority instructions.
- The accepted artifact can be checked against its output contract.
- The cost comparison includes human search/review, retries, rework, latency, and
  privacy exposure, not just token spend.
