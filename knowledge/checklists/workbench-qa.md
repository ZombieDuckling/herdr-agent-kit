# workbench QA checklist

Use this to test whether an AI workbench is real or only a chat pointed at a
folder.

- [ ] Front desk exists.
- [ ] Front desk includes a compact file tree or task-to-path map before agents
      perform broad search.
- [ ] Manifest exists.
- [ ] Path, filename, and folder positions encode the workflow stage before
      semantic search is required.
- [ ] Source and derived material are separated.
- [ ] Source coverage is labeled: source-backed, partial-source, metadata-only,
      retry-pending, or rejected-too-thin.
- [ ] For organizational/workflow memory, teams, roles, workflows, inputs,
      outputs, and relationships are addressable rather than buried in prose.
- [ ] Important workflow relationships have evidence, confidence, and freshness
      fields.
- [ ] Data/research outputs pass the [source-understood data analysis checklist](source-understood-data-analysis.md)
      before conclusions are reused.
- [ ] Mutable workspace is separate from canonical template.
- [ ] Tool registry exists for side-effecting tools.
- [ ] New connectors, protocol servers, plugins, and executable bridges have
      passed the [protocol boundary review](protocol-boundary-review.md).
- [ ] Request slips exist for common jobs.
- [ ] Underdefined jobs pass through a question checkpoint before generation or
      implementation.
- [ ] Operational action workflows pass the
      [action prerequisite checklist](action-workflow-prerequisites.md) before
      reading or writing live state.
- [ ] Work ledger records completed changes.
- [ ] Post-delivery reviews use the
      [workbench outcome review checklist](workbench-outcome-review.md) before
      claiming durable value.
- [ ] Useful chat or meeting decisions are extracted into workflow files rather
      than left only in transcript history.
- [ ] Generated artifacts with future edit needs have separate source, spec,
      generated source/build files, render/export, and review notes.
- [ ] New tooling, learning, delegation, and automation decisions have passed the
      [problem-first tooling checklist](problem-first-tooling.md).
- [ ] Any job board, marketplace, service queue, or community-work routing has
      passed the [opportunity routing checklist](opportunity-routing.md).
- [ ] Subjective, brand, domain, or taste-heavy work has an opinion layer that
      passes the [opinion context checklist](opinion-context.md).
- [ ] Automation has passed the [automation readiness checklist](automation-readiness.md)
      before any agentic loop or full integration replaces the manual workflow.
- [ ] Domain-expert source attempts and cheap-tool baselines have passed the
      [domain-expert discovery checklist](domain-expert-discovery.md) before a
      custom advisory or automation product is scoped.
- [ ] Capability, permission, system boundary, responsibility chain, and
      emotional-support limits have passed the
      [AI capability boundary review](ai-capability-boundary-review.md) before
      consequential or emotionally loaded AI work is automated.
- [ ] Repeated bounded judgments have decision files with thresholds, exact-code
      exclusions, persisted results, and review/override lanes.
- [ ] Integrated automation saves inspectable stage artifacts and passes the
      [stage artifact validation checklist](stage-artifact-validation.md) before
      downstream or external use.
- [ ] Review artifacts are visible to humans.
- [ ] Creative or generated media artifacts preserve source/spec, provenance,
      deterministic finishing steps, final identity, and allowed-use review.
- [ ] Shared-client or connector access passes the
      [workbench sync boundary checklist](workbench-sync-boundary.md) before it
      is treated as collaborative infrastructure.
- [ ] The chosen interface layer is justified by required read/write/run/
      persistence/collaboration/governance access.
- [ ] Consequential systems have passed the [affected-user governance checklist](affected-user-governance.md)
      before shallow feedback is cited as approval.
- [ ] Domain adoption programs have passed the [domain AI literacy checklist](domain-ai-literacy-workbench.md)
      before tool training is cited as responsible use.
- [ ] Consequential workbenches pass the [governance surface checklist](governance-surface.md)
      before launch or expanded access.
- [ ] Critical workflows pass the
      [AI workflow resilience checklist](ai-workflow-resilience.md) before one
      model, provider, or hosted surface becomes the only continuation path.
- [ ] Secrets are outside the workspace and exports.
- [ ] Imported skills, project routers, plugins, and helper scripts have been
      scoped and reviewed before activation.
- [ ] Third-party, leaked, marketplace, or copied AI packages have provenance,
      sandbox, script/dependency, and authority-boundary review before use.
- [ ] Generative artifact work has a brief, spec, stage map, source shelf, and
      review rule before the final artifact is accepted.
- [ ] Exploratory workflows log barriers, wins, and tool/feature fit while the
      work is happening.
- [ ] A fresh session can explain what is here.
- [ ] A second operator can continue the task.
- [ ] Branch discussions name their parent artifact, target section, edit scope,
      reviewer, and merge target.
- [ ] Section-level edits produce a diff or proposal before changing canonical
      source artifacts.
- [ ] Every important output has a verification path.
- [ ] Processed counts do not combine source-backed and source-limited items
      without showing the confidence split.
- [ ] Reused guidance has passed the
      [durable guidance review checklist](durable-guidance-review.md) before it
      becomes a law, global skill, or long-lived playbook.
- [ ] Layered systems pass the
      [abstraction boundary review](abstraction-boundary-review.md) before a
      prompt, model call, API response, or runtime signal is trusted across a
      boundary.
