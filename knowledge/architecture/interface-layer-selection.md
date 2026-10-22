# interface layer selection

Use this architecture note when a project says it needs an AI tool, assistant,
agent, workflow platform, or custom runtime. The first choice is not the brand or
model. The first choice is the interface layer: what the worker can see, edit,
run, persist, collaborate through, deploy, and govern.

## layer map

| layer | use when | durable proof | common failure |
| --- | --- | --- | --- |
| Plain chat | thinking, critique, short transformation, planning, or a one-off explanation | decision note, copied answer, or explicit non-durable result | copy/paste drift and missing project state |
| File-capable workspace | the worker must read/write several files but command execution is not central | changed files, manifest update, exported package | stale uploads, weak file tree visibility, vendor lock-in |
| IDE agent | repo edits need human-visible diffs, tests, search, and local code context | commit, diff, test log, review artifact | workspace scope gives too much file access |
| Terminal agent | batch file work, command execution, repository operations, validation, or deploy checks | command transcript, generated files, commit, receipt | actions are hard for nontechnical reviewers to inspect |
| Deterministic script | the task is a repeated rule, transform, fetch, lint, or validation | repeatable command and stable output | brittle assumptions hidden as automation |
| Custom runtime or multi-agent system | production needs custom permissions, scaling, audit logs, tool isolation, policy, or integrations | qualified worker envelope, logs, evals, cost telemetry, rollback path | competing with simpler hosted or file-based tools |

## selection sequence

1. State the job and the acceptance proof.
2. List what the worker must read.
3. List what it must edit or create.
4. List what it must run, deploy, or call.
5. List what state must outlive the session.
6. List who else must review, continue, or collaborate.
7. List privacy, secret, and publication boundaries.
8. Choose the smallest layer that can complete and verify the job.
9. Record which simpler layer was rejected and why.

## design consequences

- If persistence matters, move state out of chat and into files, manifests,
  tickets, ledgers, commits, or databases.
- If deployment matters, the review artifact must come from the deployed target,
  not from the generated draft.
- If collaboration matters, expose shared artifacts, identity, permissions, and
  handoff state instead of sharing one private chat.
- If governance matters, route consequential effects through typed tools,
  allowlists, logs, cost limits, and rollback paths.
- If a deterministic step keeps recurring, extract it from the agent path into a
  script or check.

## anti-patterns

- Choosing a custom agent runtime before proving that chat, file workspace, IDE,
  terminal, or scripts cannot satisfy the job.
- Treating a hosted session as the artifact instead of exporting the workbench.
- Loading all voice, brand, source, and audience context into every task instead
  of routing the smallest needed layer.
- Using more agents to compensate for missing manifests, request slips, tool
  descriptions, or review surfaces.
