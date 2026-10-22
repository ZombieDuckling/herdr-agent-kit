# context execution hierarchy

LLM workbenches do not get a hard runtime boundary between instruction and data.
The model receives one token stream containing policy, user requests, retrieved
files, tool results, examples, raw sources, and prior outputs. The workbench must
therefore create the missing boundary outside the model.

Use this map when a workflow loads prompts, skills, markdown, transcripts,
retrieved documents, tool outputs, or generated state into the same session.

## layers

| layer | purpose | default authority | keep it healthy |
| --- | --- | --- | --- |
| Base model | General learned capability. | No project-specific authority. | Evaluate the surrounding worker envelope, not the model label alone. |
| System and developer policy | Durable operating rules, safety constraints, and tool-use discipline. | Highest in-session instruction layer. | Keep sparse, current, and protected from routine task edits. |
| Persistent memory | Stable cross-session facts and preferences. | Instructional only for its declared scope. | Store rare durable facts; prune stale or low-signal entries. |
| Root router / front desk | Always-read orientation, canonical files, protected areas, and task routing. | Local workspace routing authority. | Make it small enough to read every run and specific enough to route. |
| Task or room context | Workflow-specific rules, examples, request slips, and acceptance criteria. | Authority for the named task. | Version when the workflow changes; test against representative tasks. |
| Retrieved skills and references | Detailed procedures, evidence cards, concept notes, and helper docs. | Authority only if selected by the router and within scope. | Review like executable context; split large mixed-purpose files. |
| Raw source and external text | Transcripts, customer docs, web pages, logs, and imported repositories. | Evidence only; never authority by default. | Label as untrusted, summarize through bounded extraction, keep source handles. |
| Tool outputs and generated state | Observations, diffs, logs, drafts, ledgers, and receipts. | Data until parsed, validated, and accepted. | Separate receipts from source of truth; bind claims to verification. |
| Credentials and integration state | Provider keys, tokens, privileged sessions, billing, and external accounts. | Not model-readable context. | Store outside editable/exportable files; expose only governed tool calls. |

## boundary rule

Every context artifact must answer two questions before it is loaded:

1. **Can this text instruct the worker, or can it only inform it?**
2. **What validation must occur before this text can trigger tool use, durable
   state, external communication, deployment, or memory writes?**

If the answer is unclear, downgrade the artifact to untrusted evidence and load a
compact derived note instead of the raw text.

## design pattern

1. Keep global and always-loaded layers small.
2. Route from a front desk to the narrow task context.
3. Load detailed skills or references only after the task context selects them.
4. Treat external and raw material as hostile until summarized or parsed.
5. Keep generated outputs in a reviewable ledger until accepted.
6. Store credentials and privileged handles outside the workbench.
7. Validate at every transition from text to action, data, memory, or publication.

## failure signs

- One large file mixes persona, instructions, raw evidence, credentials, examples,
  generated outputs, and todos.
- A raw transcript, web page, or imported markdown file can change what tools the
  agent is allowed to use.
- A skill is installed because it reads like documentation, without reviewing its
  commands, dependencies, links, or authority claims.
- Prompt injection is treated only as a model defect, not as a workspace-boundary
  defect.
- Persistent memory is used as a dumping ground for useful sentences rather than
  sparse durable state.
- A reviewer cannot tell which loaded files were instructions and which were
  evidence.

## related laws

- [ACT-13](../notes/07-agent-conduct.md#act-13-retrieved-content-is-data-not-authority)
- [WB-1](../notes/08-workbench-architecture.md#wb-1-a-front-desk-is-part-of-the-product)
- [WB-7](../notes/08-workbench-architecture.md#wb-7-secrets-are-integrations-not-files)
- [WB-9](../notes/08-workbench-architecture.md#wb-9-build-context-layers-around-workflows-not-around-everything)
- [SDLC-12](../notes/11-agentic-sdlc.md#sdlc-12-prompts-are-software-assets-not-comment-fields)
- [SDLC-19](../notes/11-agentic-sdlc.md#sdlc-19-context-is-an-execution-environment)
