# Agentic delivery operating model

Use this reference when the user frames software delivery as **agentic-driven development**: one strong builder, or a builder pair, orchestrating coding agents across a larger value slice or whole project instead of behaving like one developer assigned to a narrow Agile ticket.

## Core lesson

The delivery workflow should become build-centered and evidence-centered, not meeting-centered. The human remains accountable for judgment, acceptance, risk, and final verification. Coding agents increase implementation bandwidth; they do not own business risk, security risk, release risk, or truth.

## Human-agent delivery cell

Treat the operating unit as a **human-agent delivery cell**:

- One accountable human operator, optionally with a human partner.
- A bounded pool of coding agents for implementation, testing, review, documentation, research, release prep, and red-team/security checks.
- A value slice large enough to matter, but still small enough to verify and ship.
- A build ledger that records prompts/task briefs, files changed, commands run, evidence produced, risks remaining, and decisions needed.

This replaces the classic pattern where many people each take a small ticket and synchronize through stand-ups. Meetings do not disappear, but they become decision forums rather than status extraction rituals.

## Agent roles

Use explicit roles instead of a vague swarm:

- **Builder Agent:** implements a bounded slice.
- **Test Agent:** writes/runs verification for changed behavior.
- **Review Agent:** inspects diffs for defects, maintainability, and security.
- **Research Agent:** gathers technical options, standards, and migration constraints.
- **Documentation Agent:** updates operator notes, API docs, and user-facing docs.
- **Release Agent:** prepares release evidence, changelogs, deployment checks, and rollback notes.
- **Red-Team Agent:** probes AI/LLM abuse cases, prompt injection, insecure output handling, excessive agency, and unsafe tool permissions.

## Meeting-light control pattern

Prefer asynchronous evidence over routine meetings:

1. Define the value slice, risk tier, non-goals, allowed files/systems, and verification commands.
2. Assign non-overlapping agent missions.
3. Capture each agent's task brief and outputs in a build ledger.
4. Run direct verification: tests, builds, screenshots, endpoint checks, security scans, or artifact inspection.
5. Hold a live call only for judgment points: scope conflict, risk acceptance, architecture trade-off, blocked access, or stakeholder decision.
6. Record decisions and return to building.

A good rule: if a meeting does not change a decision, remove it; if it changes a decision, capture the decision and return to build work.

## Risk controls

Agentic development needs extra controls because agents can produce plausible but wrong output and may have tool access:

- Keep workspaces, branches, and file ownership bounded.
- Limit tools and secrets exposed to agents.
- Keep prompt/task briefs for high-risk work.
- Serialize edits to shared files.
- Treat every agent self-report as unverified until Hermes or the human operator verifies the artifact directly.
- Add independent review for Tier 2+ work and independent security/release evidence for Tier 3 work.
- Record residual AI-generated-code risk in the release evidence pack when relevant.

## SDLC framing

When adapting GF-SDLC or similar corporate workflow material for agentic delivery, explicitly add:

- **Agentic leverage** as a framework criterion.
- **Meeting efficiency** as a framework criterion.
- A **solo builder with coding agents** scenario in any comparative test.
- Human-agent delivery cells in the operating model.
- Build ledgers as a replacement for daily stand-up status reports.
- Human acceptance gates for agent output.

The thesis position: corporate software delivery should be governed by evidence, not ceremony. Agentic development makes this more urgent because the bottleneck moves from typing capacity to orchestration, verification, and risk acceptance.
