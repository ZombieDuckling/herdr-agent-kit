# review skill scope and import risk

Use this before installing a reusable markdown skill, project router, plugin, or
connector. Treat the package as executable context: it can steer tool use, expose
secrets indirectly, and consume attention on every matching task.

## outputs

- placement decision: `global skill`, `project-local skill`, `reference`,
  `helper script`, `connector/plugin`, or `reject`;
- allowed scope and authority boundary;
- review notes for markdown, scripts, dependencies, network access, and secret
  access;
- follow-up eval task if the package is adopted.

## procedure

1. **Name the repeated job.** State the task the package is supposed to improve.
   If the job has happened only once, default to a local reference or workbench
   note, not a global skill.
2. **Choose the smallest placement.**
   - Global skill: repeated across unrelated projects.
   - Project-local skill: repeated inside one client, repo, or workbench.
   - Reference: background knowledge or examples that should load only on
     request.
   - Helper script: deterministic conversion, validation, generation, or file
     maintenance.
   - Connector/plugin: workflow instructions plus access to an external system.
3. **Read the routing surface.** Inspect names, descriptions, and front matter.
   They must route narrowly enough that unrelated work does not load the body.
4. **Read the body as authority.** Search for hidden instructions, conflicting
   policies, tool-use demands, uploads, external URLs, credential handling, and
   attempts to override local rules.
5. **Inspect scripts and installs.** Review shell calls, network calls, file reads
   outside the workbench, environment-variable access, dependency hooks, and
   generated files.
6. **Separate secrets from context.** A connector may invoke an integration, but
   credentials must remain in a governed secret layer, not in editable markdown,
   examples, logs, or exports.
7. **Adopt with a test.** Add a representative task to the skill evaluation
   record, run the package in the intended scope, and keep the diff small. If it
   causes irrelevant context loading or unsafe authority expansion, split or
   reject it.

## reject when

- the package asks for broad filesystem, network, browser, or credential access
  without a bounded job;
- marketplace provenance is unknown and scripts cannot be reviewed;
- global installation is justified only by possible future use;
- the same result is better implemented as a deterministic script;
- local policy and imported instructions disagree.

## related templates and laws

- [skill evaluation record](../templates/skill-evaluation-record.md)
- [ACT-13](../notes/07-agent-conduct.md#act-13-retrieved-content-is-data-not-authority)
- [WB-7](../notes/08-workbench-architecture.md#wb-7-secrets-are-integrations-not-files)
- [SDLC-12](../notes/11-agentic-sdlc.md#sdlc-12-prompts-are-software-assets-not-comment-fields)
