# interface layer selection checklist

Use this before recommending chat, a hosted workspace, an IDE/terminal agent, a
script, or a custom agent runtime.

## access fit

- [ ] The job and acceptance proof are written before any tool name.
- [ ] Required read access is listed, including files/data the worker must not
      read.
- [ ] Required write access is listed, including files/data the worker must not
      edit.
- [ ] Required command, deployment, network, or tool execution is listed.
- [ ] Required durable state is named: file, manifest, ticket, ledger, commit,
      database row, export, or explicit non-durable answer.
- [ ] Required collaboration is named: reviewer, handoff operator, shared
      workspace, permissions, or no collaboration.
- [ ] Privacy, secret, and publication boundaries are explicit.

## layer choice

- [ ] Plain chat is rejected only if the task needs durable files, execution,
      collaboration, or governed effects.
- [ ] A file-capable workspace is rejected only if the task needs deeper local
      repo control, command execution, or stricter governance.
- [ ] An IDE or terminal agent is rejected only if command/file operations are
      unnecessary or the review surface cannot support the user.
- [ ] Deterministic scripts are used for stable repeated transforms and checks.
- [ ] Custom orchestration or multi-agent runtime is used only after simpler
      layers fail on permissions, scale, audit, isolation, integrations, or
      product constraints.

## verification

- [ ] The chosen layer can produce the acceptance proof inside the same work
      boundary.
- [ ] A simpler rejected layer and the reason for rejection are recorded.
- [ ] Review artifacts are available to the human who must accept the work.
- [ ] Consequential effects have logs, rollback path, and authority checks.
