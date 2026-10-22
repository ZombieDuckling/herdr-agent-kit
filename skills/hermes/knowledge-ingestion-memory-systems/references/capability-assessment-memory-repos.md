# Capability assessment across private/shared memory repos

Use this when the user asks whether the current Hermes/the user knowledge estate has enough skill/context to complete a complex project correctly.

## Source order

1. Load relevant class skills first.
2. Inspect private high-context repos for project-specific context.
3. Inspect shared/sanitized agent-memory repos for transferable laws and safety constraints.
4. Inspect source project repos and their governing docs directly.
5. Treat session history and persistent memory as routing/context, not as proof of current repo/source state.

## Assessment structure

Answer in layers:

- **Capability:** whether the team/agent can do it.
- **Domain grounding:** what internal/source material proves the project rules are understood.
- **Technical tooling:** what scripts/tools/repos exist and what needs building.
- **Functional blockers:** missing source files, credentials, network access, or human decisions.
- **Correctness constraints:** the rules that must not be violated.
- **Human finish boundary:** what the agent can produce versus what a domain owner/counsel/client-facing reviewer must adjudicate.

## Guardrails

- Do not overclaim because a memory says something exists; inspect the repo/file/source when accessible.
- Do not turn private knowledge into shared-memory content unless it is sanitized and generalized.
- Separate feedstock from final product when the operating model says a human/domain expert performs a finishing pass.
- If credentials are part of the project, assess the vault/tooling shape but never ask memory to supply or preserve secrets.
- Prefer blunt verdicts: `yes`, `yes with blockers`, or `no`, followed by exact reasons.
