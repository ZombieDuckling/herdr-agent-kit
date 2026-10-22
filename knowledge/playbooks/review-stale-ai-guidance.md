# review stale AI guidance

Use this when old advice, prompt packs, model notes, or workflow claims are being reused after tools or markets changed.

## inputs

- Candidate claim or note.
- Source pointer and source/retrieval date.
- Current workflow where the claim may be reused.
- Recent failures, model/provider changes, policy changes, or cost changes.

## steps

1. **State the claim without decoration.** If it cannot be written as an action-guiding sentence, leave it as background.
2. **Classify the layer.** Use durable primitive, current tactic, market observation, or unsupported source-limited claim.
3. **Extract the primitive.** Remove model names, UI details, creator names, private project details, buyer identities, and dated competitive claims.
4. **List changed assumptions.** Check model behavior, tool access, pricing, policy, user baseline, security posture, and review burden.
5. **Choose a promotion target.** Use a law only for a transferable invariant; use a playbook/checklist/template for repeatable structure; use local notes for volatile tactics.
6. **Set a review trigger.** Do not rely on calendar age alone when a provider release, policy shift, repeated failure, or cost swing is the real invalidation event.
7. **Record exclusions.** Write down what was left out because it was private, source-specific, thinly sourced, or too volatile.

## output format

```md
## Claim: <short claim>
- Source pointer:
- Source/retrieval date:
- Layer:
- Still true:
- Changed assumptions:
- Current action:
- Promotion target:
- Next review trigger:
- Intentionally not promoted:
```

## acceptance check

The reviewed guidance passes only when a fresh agent can tell which part is durable, which part is dated, what evidence supports it, and what event should force a revisit.
