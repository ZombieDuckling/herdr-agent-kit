# governance surface review

Use this shape when a workspace, agent, or AI-assisted product can affect identity, access, money, reputation, safety, public decisions, infrastructure, or sensitive data. At that point the software boundary is also a governance boundary.

## required surfaces

| surface | question | durable artifact |
| --- | --- | --- |
| Actors and roles | Who can enter, speak, edit, execute, invite, export, delete, override, or approve? | Role table and permission matrix. |
| Data classes | What source, personal, client, operational, secret, or regulated material enters? | Data-class inventory with storage and export rules. |
| Action rights | Which decisions are made by the system, and which are only drafted for review? | Tool/action registry with owner and approval level. |
| Provenance | Which sources can the system trust, cite, or ignore? | Source policy and citation/retrieval ledger. |
| Platform dependency | Which provider controls identity, moderation, distribution, payments, compute, or model access? | Dependency register with fallback or exit notes. |
| Audit and receipts | How can an operator prove who changed what, using which data and tools? | Event log, artifact registry, and decision ledger. |
| Human legitimacy | Which affected users or domain experts must be represented before deployment? | Participation plan and implementation ledger. |
| Abuse and blast radius | What harm can a low-skill actor cause through weak auth, prompt injection, exports, or tools? | Threat sketch and rollback/incident path. |

## minimum project brief section

```md
## Governance surface
- Actors/roles:
- Data classes:
- Tool/action rights:
- Source/provenance rules:
- Platform/provider dependencies:
- Audit/logging:
- Human review/owner:
- Affected-user/domain-expert representation:
- Abuse/cyber blast radius:
- Rollback/incident path:
```

## design rules

- Treat source choice, provider choice, and action authority as visible product decisions.
- Do not hide consequential power behind a polished chat UI.
- Keep secrets in governed integrations, not editable files.
- Make source traces and implementation decisions inspectable by the people accountable for them.
- Represent affected users with a route to learn, deliberate, propose, review prototypes, and see accepted/rejected/deferred outcomes; surveys alone are not governance.
- Map capability by degree: inputs, memory, action rights, feedback loops, reliability, reversibility, and owner accountability. Do not rely on binary labels such as “autonomous” or “safe.”

## acceptance test

A fresh reviewer can answer, from files rather than chat memory:

1. who is affected;
2. who can act;
3. what data and sources are in scope;
4. what providers or platforms can change the rules;
5. what decisions were accepted, rejected, or deferred;
6. what can go wrong;
7. who owns review, rollback, and incident response.
