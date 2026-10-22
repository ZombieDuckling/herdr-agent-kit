# choose the mechanism before the agent

Use this before adding an agent, model, automation platform, or workflow tool.

## questions

1. What job is being bought?
2. What decision or risk is being improved?
3. What data is actually available?
4. What happens if the system is wrong?
5. Can a checklist or process change solve it?
6. Can deterministic code solve it?
7. Is the remaining judgment only a bounded label, yes/no, score, route, or
   readiness decision that belongs in a decision gate?
8. Can a one-shot model transform solve it?
9. Has a plain-chat baseline been run with representative inputs?
10. If the chat baseline works partly, which missing layer justifies product
    work: source feed, editable reference data, scoring, persistence, governance,
    privacy, scale, or review evidence?
11. Is prediction needed?
12. Is a bounded tool-using agent genuinely needed?
13. Is the visible output likely to become a commodity platform feature?
14. What context, workflow, data, governance, or human judgment makes the next
    layer defensible?
15. What must the worker see, edit, run, persist, share, deploy, or govern?
16. Which interface layer is the smallest one that can produce the acceptance
    proof?
17. Who reviews the output?

## mechanism classes

- process change;
- checklist;
- plain-chat baseline;
- deterministic script;
- scheduled job;
- decision gate for bounded fuzzy judgment;
- one-shot model transform;
- predictive model;
- bounded agent loop;
- multi-agent system.

Pick the simplest class that can pass the acceptance test.

## interface layers

After choosing the mechanism class, choose the access layer:

- plain chat for non-durable thinking or critique;
- file-capable workspace when the artifact must live in files;
- IDE agent when repo edits, diffs, and tests need a human-visible code surface;
- terminal agent when commands, batch file work, or deployment checks are central;
- deterministic script when the step is a repeated rule or validation;
- custom runtime or multi-agent system only when permissions, scale, audit,
  isolation, integrations, or production policy require it.

Record the simpler layer rejected and the specific missing access or proof.

If the selected mechanism mainly sells raw AI output or a thin wrapper around an
existing runtime, run [the abstraction-layer risk check](run-an-abstraction-layer-risk-check.md)
before building.
