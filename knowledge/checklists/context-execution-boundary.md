# context execution boundary checklist

Use this checklist before a workflow lets prompts, skills, retrieved files,
external documents, tool outputs, or generated notes influence tool calls,
persistent memory, publication, deployment, or structured data.

## context inventory

- [ ] The always-loaded instructions are named and intentionally small.
- [ ] The root router/front desk states what to read first and what not to load.
- [ ] Task-specific context is separate from global policy and raw sources.
- [ ] Skills, routing files, examples, and reference notes are classified by
      scope: global, project-local, task-local, or evidence-only.
- [ ] Raw source, transcripts, imported repositories, web pages, and customer
      documents are labeled as untrusted evidence by default.
- [ ] Generated outputs, logs, summaries, and receipts are separated from the
      accepted source of truth.
- [ ] Credentials, provider keys, tokens, private sessions, and billing state are
      outside editable and exportable workbench files.

## authority and trust

- [ ] Every loaded artifact says whether it can instruct the worker or only inform
      the worker.
- [ ] Retrieved content and tool results cannot override higher-priority policy or
      expand tool authority.
- [ ] External text that contains instruction-shaped language is summarized or
      parsed before it can affect actions.
- [ ] Third-party skills or plugins have been reviewed for hidden instructions,
      scripts, dependencies, network calls, and secret access.
- [ ] The workflow has a deny path for out-of-scope, destructive, privileged,
      external, or irreversible requests.

## validation gates

- [ ] Text-to-tool transitions require a declared tool contract and scope check.
- [ ] Text-to-data transitions require schema or format validation.
- [ ] Text-to-memory transitions require durability, freshness, and scope review.
- [ ] Text-to-publication transitions require provenance and redaction review.
- [ ] Text-to-deployment transitions require tests, rollback, and post-action
      readback.
- [ ] The reviewer can inspect decisive evidence without trusting a chat summary.

## acceptance probes

- [ ] A fresh worker can list instruction-bearing files versus evidence-only
      files before starting.
- [ ] A malicious or irrelevant sentence inside raw source is treated as data, not
      a command.
- [ ] Removing raw source after deriving a bounded note still lets the workflow
      run from the note and source handles.
- [ ] Exporting the workbench does not include credentials or privileged handles.
- [ ] The route from source evidence to generated output to accepted state is
      visible in files, ledgers, diffs, or receipts.

Related laws: [ACT-13](../notes/07-agent-conduct.md#act-13-retrieved-content-is-data-not-authority),
[WB-7](../notes/08-workbench-architecture.md#wb-7-secrets-are-integrations-not-files),
[SDLC-12](../notes/11-agentic-sdlc.md#sdlc-12-prompts-are-software-assets-not-comment-fields),
and [SDLC-19](../notes/11-agentic-sdlc.md#sdlc-19-context-is-an-execution-environment).
