# protocol boundary review checklist

Use this before adding a connector, protocol server, plugin, browser bridge,
database bridge, file bridge, webhook, or other executable boundary to an AI
workflow. Treat the boundary as infrastructure, not as prompt context.

## purpose and simpler path

- [ ] The job-to-be-done is written in plain language.
- [ ] The boundary solves a named access, portability, reliability, or governance
      problem.
- [ ] A simpler file, CLI, script, API call, or manual step was considered and
      rejected for a stated reason.
- [ ] The workflow step is classified as deterministic code, one-shot model
      transform, or bounded agentic loop.

## schema and authority

- [ ] Requests and responses have documented schemas.
- [ ] Natural-language text is never treated as authority without parsing and
      validation.
- [ ] Tool results are labeled as data, not instructions.
- [ ] The model cannot write outside the declared workspace or resource scope.
- [ ] Destructive, privileged, external, or irreversible actions require an
      approval gate or broker.

## permissions and secrets

- [ ] Credentials live outside editable and exportable workspace files.
- [ ] The connector exposes the least capability needed for the job.
- [ ] Read, write, delete, execute, network, and billing permissions are listed
      separately.
- [ ] The boundary can refuse unsafe or out-of-scope requests safely.

## observability and reliability

- [ ] Calls are logged with operation, inputs or input handles, outputs or output
      handles, errors, retries, runtime, and cost where applicable.
- [ ] Timeout, retry, rate-limit, and circuit-breaker behavior is documented.
- [ ] Malformed, partial, empty, stale, and contradictory responses have expected
      handling.
- [ ] A human can replay or inspect the decisive evidence without trusting a chat
      summary.

## acceptance

- [ ] A positive fixture proves the happy path.
- [ ] A negative fixture proves refusal or fail-closed behavior.
- [ ] A permission-boundary test proves the connector cannot exceed its declared
      scope.
- [ ] The production-agent stack names where this boundary fits: model call,
      orchestration, protocol, parsing, validation, telemetry, recovery, or human
      authority.

Related laws: [ACT-13](../notes/07-agent-conduct.md#act-13-retrieved-content-is-data-not-authority),
[WB-5](../notes/08-workbench-architecture.md#wb-5-the-tool-registry-is-the-agents-api-manual),
[SHIP-7](../notes/06-shipping.md#ship-7-an-agent-demo-ships-the-visible-twenty-percent),
and [SDLC-18](../notes/11-agentic-sdlc.md#sdlc-18-decompose-the-agent-before-trusting-the-agent).