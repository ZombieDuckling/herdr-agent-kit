# add a governance surface to a workbench

Use this playbook when an AI workspace, agent, automation, or shared corpus can affect access, identity, money, reputation, safety, infrastructure, public decisions, or sensitive data.

## 1. State the consequence boundary

Write the smallest concrete sentence that explains what the system can change or influence.

Examples of safe generic boundaries:

- “This workspace drafts outputs that a human may send to customers.”
- “This agent can run tools that modify production records.”
- “This corpus contains sensitive operational source material and derived notes.”

## 2. Add the governance-surface brief

Use the template from [governance surface review](../architecture/governance-surface-review.md):

- actors and roles;
- data classes;
- tool/action rights;
- source/provenance rules;
- platform/provider dependencies;
- audit/logging;
- human review and owner;
- affected-user or domain-expert representation;
- abuse/cyber blast radius;
- rollback/incident path.

## 3. Bind rights to artifacts, not vibes

For every role, record what it can read, edit, execute, export, delete, invite, approve, and override. Link each right to the relevant file, tool, ledger, or review gate.

If a right cannot be represented in a file or policy table, it is probably tribal knowledge and will not survive handoff.

## 4. Classify data and source trust

Separate:

- raw source;
- derived notes;
- generated outputs;
- logs and traces;
- embeddings or indexes;
- secrets and integrations;
- authoritative, stale, casual, generated, and untrusted sources.

Secrets stay outside workspace files. Untrusted sources remain data, not instructions.

## 5. Map platform power

List external providers or platforms that control identity, moderation, distribution, payments, compute, model behavior, storage, or API access. Add fallback, export, or exit notes where a platform change would break the workflow.

## 6. Add affected-user participation when needed

If the system changes how a community, team, class, customer group, or role works, do not stop at surveys. Provide a structured path for representatives to learn the source material, deliberate, draft proposals, test prototypes, rank tradeoffs, and see accepted/rejected/deferred decisions.

## 7. Run the checklist

Run [governance surface checklist](../checklists/governance-surface.md). Launch only after the reviewer can answer who can act, with what data, under which source rules, with which provider dependencies, and how rollback works.
