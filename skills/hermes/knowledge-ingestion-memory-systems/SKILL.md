---
name: knowledge-ingestion-memory-systems
description: Use for recurring knowledge ingestion into memory repos.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [knowledge-ingestion, memory, cron, youtube, github, agent-memory, briefing]
    related_skills: [youtube-content, github-repo-management, daily-communications-briefing, self-improvement]
---

# Knowledge Ingestion + Memory Systems

## Purpose

Build and maintain durable learning systems that convert external sources, transcripts, project lessons, and operational fixes into structured repositories, recurring ingestion jobs, sanitized shared memories, and concise briefings.

Use this for class-level workflows like:

- ingesting a whole YouTube channel or long-form source corpus over time;
- creating a private GitHub knowledgebase with manifests, indexes, notes, and memory exports;
- chaining cron jobs so ingestion feeds implementation, implementation feeds briefings, and safe lessons feed a shared memory repo;
- distilling private operational knowledge into sanitized transferable laws without leaking people, paths, repos, domains, or private project identity.

## Core principles

1. **Do not fake completion.** For large corpora, inventory first, process in verified batches, and report exact processed counts.
2. **Separate private knowledge from shareable memory.** Raw transcripts, user memory exports, private project details, and exact source identities belong only in private repos. Shared memory repos get sanitized universal laws only.
3. **Prefer plain-file auditability.** Use manifests, markdown notes, theme indexes, problem/solution logs, scripts, diffs, commits, and cron outputs instead of opaque chat history.
4. **Turn learning into operations.** A useful learning loop has: source ingestion → distilled notes → theme/problem indexes → implementation or skill/memory updates → morning/status briefing.
5. **Apply lessons where they belong.** If a lesson improves Hermes behavior, save a compact memory/skill. If it improves a software project, implement a small verified change. Do not conflate separate projects.
6. **Depth beats speed when the user asks for depth.** Increase batch size only if it does not turn notes into shallow summaries.

## Repository shape

For a private knowledge repo, prefer:

```text
README.md
video-manifest.json              # or source-manifest.json
knowledge/
  videos/                        # one note per source item
  themes/INDEX.md                # cross-source synthesis
  problems-and-solutions.md      # recurring problems and fixes
  hermes-implementation-log.md   # concrete implementation claims
memory-export/
  MEMORY.md
  USER.md
  EXPORT-METADATA.md
scripts/
  inventory_channel.py
  fetch_transcript.py
  next_unprocessed.py
raw/
  channel/                       # source metadata OK if private
  transcripts/                   # usually gitignored unless safe/private
logs/
```

## Per-item note format

Each processed item should include:

- source title / ID / URL;
- transcript or metadata status;
- core thesis;
- key lessons;
- implications for Hermes, the relevant project, and the user;
- recurring problems/solutions;
- candidate durable memories or skills;
- explicit caveats if transcript was unavailable or source was partial.

Do not hallucinate missing source content. Label transcript failures and move on.

## Cron choreography

When the user wants continuous background learning, use separate jobs with clear order:

1. **Ingestion job** — processes a bounded batch and updates the private knowledge repo.
2. **Implementation job** — runs after ingestion and receives its output via `context_from`; implements one safe useful change or writes a verified runbook/backlog note.
3. **Sanitized shared-memory job** — distills only transferable laws into a strict shared repo if rules allow.
4. **Morning briefing job** — receives upstream outputs via `context_from` and reports the top lesson, implementation status, gaps, and next target.

Every cron prompt must include: no recursive cron management, protect secrets/data, inspect git status first, verify before commit/push, and report exact artifacts.

## Applying agent-memory lifecycle rules to another project

When the user says to follow an agent-memory SDLC, lifecycle, or workbench pattern, treat that repository as the current rule source for the target project's delivery workflow, not as a vague citation.

1. Clone or update the memory repo, then read its `AGENTS.md`, `CONTRIBUTING.md`, the relevant SDLC note, and the current workbench templates before editing the target project.
2. Record the memory repo commit hash and source files used. Put this in the target project's lifecycle records or generated assurance data so future workers know which rule revision was applied.
3. Add plain lifecycle records to the target project when it becomes an operational artifact: `lifecycle/REQUEST.md`, `PLAN.md`, `STATUS.md`, and `HANDOFF.md`. Capture the outcome contract, route, authority boundary, untrusted-content boundary, verification checks, validation status, rollback, and next action.
4. Expose a compact lifecycle or assurance status in the artifact itself when useful, but keep detailed receipts in files so they survive chat compaction.
5. Re-run the target project's acceptance checks after adding lifecycle records; adding governance files is not acceptance unless the current head still refreshes, builds, serves, or otherwise works.

Pitfall: do not copy agent-memory entries into the target project as prose decoration. Apply the workflow shape and cite the rule revision; the target project needs an outcome contract and receipts, not a pasted philosophy.

## Shared agent-memory distillation

Some repos are intentionally sanitized and irreversible. Before writing there:

- read the repo's `AGENTS.md`, `CONTRIBUTING.md`, and index every run;
- obey its ID and index conventions;
- strip names, handles, repo owners, personal paths, project names, domains, credentials, IDs, and private business identity entirely;
- write one transferable law per entry;
- run the repo's preflight before commit and after rebase;
- pull/rebase before allocating IDs and again before push;
- never force-push or amend pushed commits;
- leave out anything unsafe or too source-specific and say why.

See supporting references:

- `references/agent-memory-distillation.md` for a reusable shared-memory contribution protocol.
- `references/public-auxiliary-knowledge-corpus.md` for building public-source software/IT/security learning corpora without copying textbooks.
- `references/agent-memory-auxiliary-pdf-corpus.md` for the direct-PDF-only manifest pattern when the user asks for actual textbook/PDF corpora.

## Verification checklist

- [ ] Source inventory count is recorded and reproducible.
- [ ] Processed count is truthful and machine-verifiable.
- [ ] Raw private content is excluded from public/shared repos.
- [ ] Notes cite the source item they came from.
- [ ] Theme/problem indexes were updated when a cross-source pattern emerged.
- [ ] Durable memory/skill updates are compact and high-signal, not a dump of every lesson.
- [ ] Cron ordering and `context_from` make the learning available where it is used.
- [ ] Git status is clean or intentionally documented after commit/push.
- [ ] Morning briefing tells the user what was learned, what was implemented, and what remains.

## Pitfalls

- **Mistaking a knowledge repo for memory.** The repo can hold detail; Hermes memory should hold only compact durable operating facts.
- **Over-agentifying ingestion.** Use scripts/manifests for deterministic inventory/transcript work; use agents for synthesis and judgment.
- **Conflating projects.** If a dashboard is separate from Hermes, say so in the cron prompt and implementation log.
- **Publishing source identities into sanitized repos.** Even private shared-memory repos may have stricter rules; follow the target repo, not the source repo.
- **Reporting summaries as implementation.** Maintain an implementation log so "learned" and "implemented" remain distinct.
