# action workflow prerequisite checklist

Use this gate before an assistant reads or writes live operational state.

## procedure

- [ ] The workflow names the exact action class.
- [ ] Normal steps are written.
- [ ] Edge cases and escalation cases are written.
- [ ] Done criteria are visible before execution.

## role and context

- [ ] The governing role or owner is identified without relying on chat memory.
- [ ] Priority rules are recorded.
- [ ] Examples and anti-examples exist for ambiguous cases.
- [ ] Tone, domain, or policy constraints are separated from raw sources.

## source and connector access

- [ ] Authoritative source is named.
- [ ] Current read access is verified.
- [ ] Required write scope is explicit.
- [ ] Connector failure mode is defined.
- [ ] The workflow refuses to invent live state when access is absent.

## permission and blast radius

- [ ] Allowed actions are listed.
- [ ] Prohibited actions are listed.
- [ ] Approval thresholds are listed.
- [ ] Batch size, cost, or quota limit is listed when relevant.
- [ ] Rollback/correction path is known.

## verification

- [ ] The exact read-back source is listed.
- [ ] Expected state change or artifact is listed.
- [ ] Tool success is not accepted as final proof without target read-back.
- [ ] Logs, receipts, diffs, screenshots, or review artifacts are retained.
- [ ] Unresolved follow-ups have an owner and next action.

## decision

- [ ] `ready`: all layers present and current; execute within scope.
- [ ] `read-only`: no write authority; inspect or draft only.
- [ ] `offline`: no live connector; prepare from static sources only.
- [ ] `blocked`: missing procedure, authority, source, or verification; stop.
