# source readiness before generation checklist

Use this before asking an agent or model to generate decks, reports, code, plans, or analysis from a folder of source material. The goal is to make the source usable before spending tokens on synthesis.

## source map

- [ ] The authoritative inputs are named separately from background material.
- [ ] Latest/current files are marked; stale, superseded, or uncertain files are labeled instead of silently omitted.
- [ ] Each source has a short purpose note: what it proves, constrains, or informs.
- [ ] The expected output names which sources it is allowed or required to use.

## cleanup

- [ ] Filenames and folder names are descriptive enough for a fresh worker to route itself.
- [ ] Duplicates, partial exports, and generated drafts are grouped or labeled.
- [ ] Raw source is preserved separately from cleaned or derived working files.
- [ ] Sensitive material is removed or routed through governed integrations before the workspace is exported or shared.

## meaning

- [ ] Important terms, fields, assets, roles, or statuses have definitions.
- [ ] Units, time ranges, audience, decision owner, and freshness limits are recorded where relevant.
- [ ] Contradictions between sources are listed as open questions, not resolved by guess.
- [ ] Human alignment notes capture taste, priorities, and must-avoid constraints when the output is subjective.

## generation contract

- [ ] The request states the job, audience, output format, acceptance criteria, and review handle.
- [ ] The worker is told which files to read first, which files to skip, and when to stop for clarification or human review.
- [ ] Required citations, source pointers, diffs, tests, previews, or row references are part of the deliverable.
- [ ] The output records which sources were used and which were ignored.

## acceptance

- [ ] A fresh worker can identify the core source set without scanning the whole folder.
- [ ] A reviewer can trace each important claim or design choice back to source material or a named human judgment.
- [ ] The final artifact does not rely on hidden chat context that is absent from the workspace.
