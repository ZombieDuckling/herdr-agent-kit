# governance surface checklist

Use this before deploying or materially changing an AI workspace, agent, or product that affects identity, access, money, reputation, public decisions, infrastructure, safety, or sensitive data.

## gate

- [ ] The project brief has a governance-surface section.
- [ ] Actors and roles are named by role, not by private identifiers.
- [ ] Read, edit, execute, export, delete, invite, override, and approval rights are explicit.
- [ ] Data classes are inventoried, including raw source, derived notes, logs, embeddings, exports, and provider traces.
- [ ] Secrets and credentials are outside editable/exportable workspace files.
- [ ] Source/provenance rules distinguish authoritative, casual, generated, stale, and untrusted material.
- [ ] Platform/provider dependencies are listed with the powers they hold: identity, moderation, distribution, payments, compute, model behavior, storage, or API access.
- [ ] Human accountability is mapped: reviewer, approver, operator, escalation owner, incident owner.
- [ ] Affected users or domain experts have a route to learn, deliberate, propose, test, and see implementation decisions when the system materially affects them.
- [ ] Abuse paths are sketched, including weak auth, prompt injection, unsafe exports, overbroad tools, and low-skill misuse.
- [ ] Audit logs and artifact ledgers can prove accepted/rejected/deferred decisions.
- [ ] Rollback and incident paths are documented before launch.
- [ ] Capability is graded by inputs, memory, tools, feedback loops, reliability, reversibility, and ownership rather than labelled only as “safe,” “autonomous,” or “AI.”

## reject if

- The system is called “just a chat” while it can make or shape consequential decisions.
- Survey feedback is used as a substitute for affected-user governance.
- A source, provider, or agent can silently change the answer without traceability.
- The person accountable for a decision cannot inspect the sources, tools, and artifact history behind it.
