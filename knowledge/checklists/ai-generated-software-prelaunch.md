# AI-generated software pre-launch audit

Use this before software substantially generated or modified by an AI assistant is
shown to customers, connected to production data, or granted production authority.
A working app, green build, or generated explanation is not enough.

## secrets and history

- [ ] Search current tracked files for secret-shaped material.
- [ ] Search commit history and generated logs for removed secrets.
- [ ] Check deployment/provider configuration where access is available.
- [ ] Rotate any credential that may have crossed a chat, generated artifact,
      repository push, public log, or tool transcript.
- [ ] Verify exported/downloadable workspace files do not contain credentials.

## auth and security primitives

- [ ] Prefer official provider SDKs, session APIs, webhook validators, and access
      control primitives over custom implementations.
- [ ] Flag hand-rolled JWT validation, cryptography, password handling, session
      stores, and permission systems for senior review.
- [ ] Verify issuer, audience, tenant/project, expiry, and signature checks for
      tokens.
- [ ] Confirm route guards are centralized and consistently applied.

## route and data exposure

- [ ] Enumerate public routes, methods, callbacks, webhooks, health checks, and
      static/generated assets.
- [ ] Verify admin, operations, customer-data, and internal-report routes require
      the intended authentication and authorization.
- [ ] Check CORS and callback behavior against the actual frontend and provider
      boundaries.
- [ ] Confirm error pages, logs, previews, and debug endpoints do not leak data.

## generated artifacts as executable context

- [ ] Review generated task plans, markdown notes, prompts, issue lists, and
      execution logs.
- [ ] Remove or quarantine unsafe instructions such as broad requests to "build
      auth," "add encryption," or "make this public" without constraints.
- [ ] Preserve useful decisions in maintained workflow files rather than stale
      generated plans.

## human threat model

- [ ] State what a malicious user, accidental user, or competitor could do with
      the current interface.
- [ ] Identify business-specific data, workflow, and reputation risks static
      code tools cannot infer.
- [ ] Classify each finding as fix-before-launch, accepted risk, or blocked by
      inaccessible context.

## acceptance

Launch is blocked until critical/high findings are fixed or explicitly accepted,
and the reviewer can answer: what is public, what requires auth, who verifies
identity, where secrets live, what generated instructions shaped the code, and
how invalid or leaked credentials are rejected.

Related laws: [SHIP-7](../notes/06-shipping.md#ship-7-an-agent-demo-ships-the-visible-twenty-percent),
[SHIP-11](../notes/06-shipping.md#ship-11-a-green-build-is-not-a-security-review),
and [SDLC-5](../notes/11-agentic-sdlc.md#sdlc-5-separate-generation-from-authority).
