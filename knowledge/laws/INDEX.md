# Law index

Each law is a transferable rule plus the sanitised incident that produced it.

## [02 · deadlocks, watchdogs, and the machinery that was supposed to save you](02-control-loops.md)

- **LOOP-1** · never gate a consumer on state only the consumer can produce
- **LOOP-2** · automation behind an allowlist fails silently
- **LOOP-3** · a restart loop is not a crash loop
- **LOOP-4** · counters reset, progress watchdogs must survive it
- **LOOP-5** · every self-healing loop needs a circuit breaker
- **LOOP-6** · a timed-out write is ambiguous

## [03 · the box is not what the documentation says it is](03-host-reality.md)

- **HOST-1** · architecture mismatch is the default failure, not the exception
- **HOST-2** · accelerators fail open to the slow path
- **HOST-3** · pkill over SSH can kill the SSH session
- **HOST-4** · a service whose port is taken may disable itself silently
- **HOST-5** · LISTEN does not mean reachable
- **HOST-6** · shared installs must be self-contained
- **HOST-7** · prove it is hardware before you touch a working config

## [06 · shipping](06-shipping.md)

- **SHIP-1** · ephemeral filesystems eat local stores
- **SHIP-2** · credential scope is not resource scope
- **SHIP-3** · a migrated zone carries live records you did not create
- **SHIP-4** · know which machine holds the only copy
- **SHIP-5** · review artifacts must come from the thing being reviewed
- **SHIP-6** · a folder is not a product until it has a manifest and a workbench
- **SHIP-7** · an agent demo ships the visible twenty percent
- **SHIP-8** · specificity is the antidote to generated slop
- **SHIP-9** · never ship the scaffold as the message
- **SHIP-10** · choose the mechanism after naming the job
- **SHIP-11** · a green build is not a security review
- **SHIP-12** · buyers pay for a resolved constraint, not a mechanism

## [08 · workbench architecture](08-workbench-architecture.md)

- **WB-1** · a front desk is part of the product
- **WB-2** · preserve the template and work in a copy
- **WB-3** · multiplayer means shared artifacts, not shared vibes
- **WB-4** · request slips beat vague prompts
- **WB-5** · the tool registry is the agent's API manual
- **WB-6** · chat is not durable state
- **WB-7** · secrets are integrations, not files
- **WB-8** · the review surface is a first-class component
- **WB-9** · build context layers around workflows, not around everything
- **WB-10** · successful dialogue is source code for the next workflow
- **WB-11** · try position-addressed memory before semantic memory
- **WB-12** · export the workbench, not the hosted session
- **WB-13** · route context in three layers before building agents
- **WB-14** · make the spec the control surface for generated artifacts
- **WB-15** · build control surfaces over workflows, not over vibes
- **WB-16** · shallow feedback is not governance
- **WB-17** · domain AI literacy teaches boundaries, not buttons
- **WB-18** · branch discussions from artifacts, not from vibes
- **WB-19** · every consequential workbench has a governance surface
- **WB-20** · model relationships as files before adding retrieval
- **WB-21** · encode opinion as portable context
- **WB-22** · make the workbench portable before the runtime fails
- **WB-23** · verify the boundary between layers
- **WB-24** · creative artifacts need source lanes, not just final renders
- **WB-25** · connectors are the sync plane, not the workbench
- **WB-26** · action requests need prerequisite gates
- **WB-27** · follow-up is an architecture review, not a satisfaction survey

## [09 · corpus engineering and review](09-corpus-and-review.md)

- **CORP-1** · the surrogate is a map, not the territory
- **CORP-2** · compression ratio is an architecture decision
- **CORP-3** · generated output must carry review handles
- **CORP-4** · source tables beat prose summaries during discovery
- **CORP-5** · preserve bad versions when the task is inventory
- **CORP-6** · semantic catalogs are for repeated navigation, not decoration
- **CORP-7** · confidence is a field, not a vibe
- **CORP-8** · dated claims need outcome reviews
- **CORP-9** · analysis is not grounded until the data semantics are grounded
- **CORP-10** · source readiness is part of generation
- **CORP-11** · separate durable principles from volatile tactics

## [10 · mechanism selection](10-mechanism-selection.md)

- **MECH-1** · name the job before naming the tool
- **MECH-2** · deterministic work does not need an agent
- **MECH-3** · split agents for boundaries, not aesthetics
- **MECH-4** · cost telemetry is part of the feature
- **MECH-5** · impressive metrics can be leakage
- **MECH-6** · model changes need truth decks, not vibes
- **MECH-7** · automate only after the manual workflow teaches its boundary
- **MECH-8** · choose the interface by required access
- **MECH-9** · physical parts start at the mating interface
- **MECH-10** · let AI translate structured human judgment before replacing it
- **MECH-11** · sell the layer above the commoditized output
- **MECH-12** · prove the chat baseline before building the product
- **MECH-13** · source attempts are requirements, not noise
- **MECH-14** · learn or delegate only against a valued bottleneck
- **MECH-15** · route demand before building supply
- **MECH-16** · separate capability from permission
- **MECH-17** · bounded fuzzy judgments need decision gates
