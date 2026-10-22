# multiplayer workbench architecture

Multiplayer AI is not multiple chat windows. It is shared context, visible
artifacts, identity, permissions, continuity, and review.

## required surfaces

### participant identity

Every action must belong to a role. Personal names are not required in shareable
notes, but the live system needs accountability.

Track:

- actor role;
- permissions;
- tool access;
- workspace access;
- last active state;
- handoff status.

### shared artifact tree

Participants need the same view of files and outputs. The file tree must show:

- canonical inputs;
- mutable work files;
- generated artifacts;
- exports;
- logs;
- review outputs.

If the agent can see files but the human cannot, the workbench is lying.

### active conversations

Chats are work surfaces, not private memory. Preserve enough state that another
authorized operator can continue:

- goal;
- decisions;
- files consulted;
- current blockers;
- open questions;
- next action.

Do not rely on raw chat history as the only memory.

### handoff and takeover

A handoff must include:

- current objective;
- what changed;
- what was verified;
- what must not be touched;
- where the next operator starts.

A takeover must not require credentials from the previous operator.

### permissions and secrets

Keep secrets outside the editable workspace. Agents get governed tools, not raw
keys in files.

The export path must prove that secrets, private source material, and integration
credentials are not included.

## failure tests

Run these before claiming the workbench is collaborative:

1. Create a fresh account or clean session.
2. Open the front desk.
3. Locate the same files the first operator used.
4. Ask what changed yesterday.
5. Review a generated artifact.
6. Continue a task without raw chat access.
7. Export the deliverable without private credentials.

If any step fails, the system is still single-player.
