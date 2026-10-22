# action workflow prerequisites

An assistant cannot safely act just because the requested verb is clear. Operational
work needs a visible gate that proves the workbench has the procedure, context,
access, authority, and verification path required for the action.

Use this shape for email triage, calendar changes, CRM follow-up, monitoring,
admin operations, codebase edits, and any workflow where the system is expected
to read current state or write back to another system.

## prerequisite stack

### 1. procedure

The workbench must name the actual process, not only the desired result.

Record:

- trigger conditions;
- normal steps;
- allowed shortcuts;
- escalation cases;
- done criteria.

If the procedure cannot be written, the system is still in discovery mode.

### 2. role and domain context

The same action means different things under different priorities. Capture the
role-specific rules before allowing automation.

Record:

- owner or role whose preferences govern the action;
- priority rules;
- examples and anti-examples;
- tone or communication constraints when applicable;
- domain terms that change the meaning of the request.

### 3. source and connector access

The workbench must know which source is authoritative and whether access is
live, stale, simulated, or absent.

Record:

- source system or file class;
- required read scope;
- required write scope;
- freshness expectation;
- fallback when the connector is unavailable.

A missing connector is not a reason to invent state. It is a blocker or a request
for narrower offline work.

### 4. permission and blast radius

Before write actions, state what the assistant may change and what remains human
approval only.

Record:

- allowed actions;
- prohibited actions;
- approval thresholds;
- maximum batch size or cost;
- rollback or correction path.

### 5. read-back verification

Every action workflow needs a way to prove what happened from the target system
or artifact.

Record:

- expected output or state change;
- exact read-back source;
- artifact or log path;
- reviewer action;
- unresolved follow-up format.

## gate states

Use one of four states before execution:

| state | meaning | allowed next step |
| --- | --- | --- |
| `ready` | all five prerequisite layers are present and current | execute within scope |
| `read-only` | procedure/context/source exist but write permission is missing | inspect, summarize, or draft for approval |
| `offline` | procedure/context exist but live connector access is absent | prepare a plan/template from static sources only |
| `blocked` | procedure, authority, source, or verification is missing | stop and record the missing prerequisite |

## anti-patterns

- Treating a broad natural-language request as permission to infer priorities.
- Building more named agents when one workbench lacks sources or procedures.
- Returning generic advice after claiming to perform a live action.
- Relying on the tool call result without reading back the target state.
- Storing credentials or live access material inside the editable workspace.

## promotion test

A fresh operator should be able to answer, before execution:

1. What procedure governs this action?
2. Whose priorities and domain context apply?
3. Which source or connector is authoritative?
4. What is the maximum permitted write scope?
5. Where will the system read back proof?

If any answer is missing, the action should not run as an agentic workflow yet.
