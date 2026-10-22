# map a team workflow before adding AI

Use this when a team asks for a second brain, assistant, automation, or agent but
cannot yet explain the work as stable inputs, outputs, owners, and review points.

## steps

1. **State the paid or operational outcome.** Name the decision, delivery, saved
   time, risk reduction, or quality improvement the map must support.
2. **Collect source evidence.** Use interviews, existing documents, tickets,
   calendars, forms, logs, or observed walkthroughs. Mark claims that are only
   guesses.
3. **Inventory nouns.** Capture teams, roles, systems, inputs, outputs,
   artifacts, queues, and recurring decisions in an entity table.
4. **Inventory verbs.** Capture consumes, produces, reviews, approves, blocks,
   hands off to, escalates to, and updates in a relationship table.
5. **Trace one workflow end-to-end.** Prefer one real high-value path over a
   complete organization diagram.
6. **Mark confidence and freshness.** Each important node or edge needs evidence,
   confidence, and a review date or stale marker.
7. **Test with a fresh operator.** They should be able to explain who does what,
   with which inputs, and where outputs go without replaying the interview.
8. **Choose the mechanism last.** Only after the workflow map works should you
   decide whether the next step is a checklist, template, script, one-shot model
   call, agent loop, integration, or shared workbench.

## acceptance criteria

- A fresh operator can follow one workflow from trigger to accepted output.
- Human judgment and approval points are visible as edges, not buried in prose.
- Automation candidates are based on repeated stable steps, not hoped-for scale.
- Unknown or contested relationships are labeled rather than silently filled in.
- The map is useful as files before any graph, vector, or agent infrastructure is
  added.
