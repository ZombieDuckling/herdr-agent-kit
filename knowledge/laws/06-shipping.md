# 06 · shipping

Things that bite between "works locally" and "works for other people."

---

## SHIP-1: ephemeral filesystems eat local stores

**Law.** On serverless and container platforms, the filesystem is scratch space.
Anything written there is gone at the next deploy, scale event, or cold start.

A signup form persisted records to a JSON file on disk. Correct in development,
silently lossy in production — and the data in question was being collected
specifically because there needed to be a durable record of it. The failure mode
is the worst kind: no error, no alert, just an empty file where the last week
went.

- Swap to managed storage (Postgres, KV, object storage) **before** the first
  real user, not after.
- Rule: if losing the file would matter, the file cannot live on the compute.
- Watch for this specifically in prototypes that get promoted. Nobody revisits
  the storage layer once the feature "works."

---

## SHIP-2: credential scope is not resource scope

**Law.** "Can authenticate" and "can touch this resource" are independent, and
the error text will actively mislead you about which one failed.

Account-scoped API tokens could list a provider's zones perfectly well, but every
call against records *inside* a zone returned an authentication error. The
token-verification endpoint reported the tokens as **invalid** — they were not;
they were real, working tokens that simply carried account-level scope and no
zone-level scope. The vendor CLI had no equivalent command at all, so there was
no command-line path either.

- Before generating new credentials, confirm the existing ones are actually
  *invalid* rather than *insufficient*. Regenerating fixes nothing if scope is
  the problem, and costs you a rotation.
- Test a credential against the exact resource class you need, not against a
  generic verify endpoint.
- When the API path is closed, the console is a legitimate answer. Record that
  decision and which browser profile / account holds the session, because the
  next person will assume automation exists.



---

## SHIP-3: a migrated zone carries live records you did not create

**Law.** Before editing DNS on a transferred domain, enumerate what is already
there and find out what it serves.

A zone migrated from a previous registrar still held that registrar's **live
email records** — MX, an SPF include, DMARC, and an autodiscover SRV. Editing the
apex to point at new hosting is routine; deleting those records as "leftovers"
silently destroys the domain's inbound mail, and the failure is invisible from
the website you were working on.

- Email records are the classic casualty. They are unrelated to web hosting,
  they look vestigial, and they are load-bearing.
- Apex `CNAME` with flattening coexists with MX records — you do not need to
  remove mail records to point the apex at a hosting provider.
- Snapshot the whole zone before any change. It is one export and it is the
  difference between a mistake and an outage.

---

## SHIP-4: know which machine holds the only copy

**Law.** If it exists in one place and that place is temporary, it does not exist.

Working scripts from a long execution session lived in a session scratch
directory and were deleted with it. Recoverable in principle, gone in practice.
What survived was the written-down *method*, which turned out to be the part
worth keeping anyway — but that was luck, not design.

Decide at creation time whether an artifact is disposable. If it is not, move it
somewhere durable immediately, while you still remember what it was for. See
[ACT-7](07-agent-conduct.md#act-7-the-script-is-disposable-the-method-is-the-artifact).

---

## SHIP-5: review artifacts must come from the thing being reviewed

**Law.** If the human is judging production quality, capture the production-like
surface, not the developer convenience surface.

A visual review was blocked by screenshots that were technically correct but
captured the wrong surface: the local development server added tooling chrome and
runtime overlays that would never ship. The feedback would have been about the
artifact of the test harness, not the page. The fix was to build the static output,
serve it locally without the development server, and recapture the same desktop
and mobile views.

- Treat screenshots, PDFs, exports, and previews as deliverables, not incidental
  evidence. The capture path is part of the product being reviewed.
- For static sites, verify the build first, then serve the built directory when
  screenshots are for client review.
- For any review artifact, name the surface: development, staging, production
  preview, or final export. If that label would change the human's judgment, you
  are not ready to send it.

---

## SHIP-6: a folder is not a product until it has a manifest and a workbench

**Law.** Plain files become useful software only when the system can inventory,
copy, govern, and operate on them without destroying the source.

A collection of markdown, scripts, decisions, and process notes was useful for a
single operator, but awkward to share: copies went stale, collaborators could not
tell which version was canonical, and active work risked mutating the reference
material. The durable shape was to treat the folder as a template, give it a
manifest and indexes, then create a separate workbench for execution.

- Keep the template human-readable and versioned. The manifest is the map; the
  notes and scripts are the terrain.
- Active work belongs in a copied workbench with its own chat, edits, artifacts,
  and audit trail. Do not let experiments rewrite the baseline.
- The test is onboarding: a new authorized operator can ask what the workspace is,
  find the relevant files, and make a bounded edit without touching the template.

---

## SHIP-7: an agent demo ships the visible twenty percent

**Law.** Treat a working agent demo as evidence of interaction design, not as
evidence of production readiness.

The prototype looked useful because it could read a workspace and produce
plausible work. The missing work was less exciting and more important: access
control, logging, monitoring, validation, cost limits, rollback, secret
isolation, and a clear risk envelope. The demo proved the user flow; it did not
prove the system could be trusted.

- Before promotion, classify each step as deterministic code, one-shot model
  transform, or agentic decision loop. Do not wrap rules in agents for theater.
- Require an owner-visible audit trail: inputs, files consulted, tools called,
  outputs written, errors, retries, and human overrides.
- If the system cannot answer who did what, under which policy, at what cost,
  and how failure is recovered, it is still a demo.

---

## SHIP-8: specificity is the antidote to generated slop

**Law.** A polished surface still fails if it could belong to any customer in
the category.

A client-facing site was technically complete but read as generated: generic
benefit copy, fake-looking metrics, interchangeable service cards, category
cliches, and decorative motion standing in for evidence. The fix was not more
polish. The fix was to make the surface answer who this is for, what actually
happens, what proof exists, and which choices are constrained by the domain.

- Remove claims whose evidence is not present in the artifact. A number without a
  source is decoration, not proof.
- Replace generic benefit language with the operational path a real customer or
  operator would follow.
- Use visual systems that carry identity and structure: real assets, domain
  constraints, differentiated page rhythm, and motion that explains hierarchy or
  state rather than hiding sameness.
- If a page could be rebranded by changing the logo and color, the work is not
  finished.

---

## SHIP-9: never ship the scaffold as the message

**Law.** Internal planning language, placeholders, and critique notes are not
unfinished copy; they are leaks from the build process.

Several otherwise usable pages exposed their own construction: placeholder proof,
notes about future testimonials, labels describing the redesign strategy, and
calls to action whose destination had not been confirmed. Those lines were more
damaging than missing content because they told the reader the artifact was a
mockup pretending to be finished.

- Search every route, not just the homepage, for planning words: placeholder,
  coming soon, todo, prompt, future proof, fake proof, and meta-explanations of
  the design pass.
- A contact affordance is a live promise. Do not add forms, floating buttons, QR
  codes, or direct-message links until the destination and expected handling are
  confirmed.
- Delete uncertain proof rather than styling it. Empty honesty is better than a
  convincing-looking lie.

---

## SHIP-10: choose the mechanism after naming the job

**Law.** "Best" is undefined until the job, constraints, value, data shape, and
failure mode are explicit.

A requested AI build looked like a model-selection problem: which tool, agent,
or benchmark leader should be used? The useful discovery question was earlier:
what outcome is worth buying, what risk is being reduced, what data is actually
available, and whether the workflow is deterministic enough for ordinary
software. Some steps that first looked agentic became scripts or schemas once the
repeated behavior was understood.

- Detect: the brief asks for "AI," "the best model," or "an agent" before it
  states the user outcome, expected value, constraints, review owner, and
  acceptable failure modes.
- Fix: write the job-to-be-done first, then classify the mechanism: process
  change, rule/script, one-shot model transform, predictive model, or bounded
  agent loop. Pick the simplest mechanism that can satisfy the job.
- Review consequential systems for leakage and bias with domain partners. A
  highly predictive signal can be an artifact of the data source rather than a
  legitimate fact about the world.

Cheap generation makes solutioning feel free, but review, risk, and adoption are
not free. The right answer may be the boring one.

---

## SHIP-11: a green build is not a security review

**Law.** AI-generated software is not launch-ready until secrets, history, auth,
public routes, generated task artifacts, deployment configuration, and business
threats have been reviewed by a responsible human.

The app ran, tests passed, and the demo looked convincing. The launch risk lived
elsewhere: credentials might have crossed chats or commits, custom identity code
might have bypassed managed-provider checks, admin routes might have been public,
and generated planning notes might steer the next agent back toward the unsafe
implementation.

- Detect: acceptance evidence is limited to "it runs," a generated summary, or a
  standard build/test result.
- Fix: audit current files and history for secrets, prefer managed auth/session
  primitives, enumerate public routes and methods, review generated markdown and
  task logs as executable context, and threat-model the real user/data boundary.
- Verification: critical and high findings are fixed or explicitly accepted, and
  the reviewer can state what is public, what requires auth, who verifies
  identity, where secrets live, and what generated instructions shaped the code.

---

## SHIP-12: buyers pay for a resolved constraint, not a mechanism

**Law.** Package technical work around the buyer's expensive constraint: speed,
friction, risk, revenue, or confidence. The mechanism is supporting evidence, not
the offer.

A working AI, automation, security, or data capability still failed as an offer
when it was priced as effort or described as a tool. The buyer needed a concrete
job, an anchored alternative, proof, a smaller first step, and a credible plan for
failure points. The technical mechanism mattered only after the value driver was
clear.

- Detect: the proposal leads with a model, agent, integration, audit, or build
  method before it names who pays, what pain changes, and why now.
- Fix: write the buyer, painful job, value driver, current workaround, expensive
  alternative, proof artifact, first paid step, and remediation promise.
- Verification: a nontechnical buyer can explain what constraint is resolved and
  why this package is faster, safer, cheaper, or more trustworthy than the
  current alternative.
