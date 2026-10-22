---
name: plain-technical-explanation
description: "Use when explaining technical things clearly and plainly."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [macos, linux]
metadata:
  hermes:
    tags: [explaining, writing, asd-ste100, plain-language, clarity, tone]
    category: copywriting
---

# Plain Technical Explanation (80% ASD-STE100)

The user asked for this directly: when explaining technical things, follow ASD-STE100 (they writes it as "ASDSE 100" or "STE100") about 80% of the way, and keep a natural speaking tone. The standard makes text unambiguous but also robotic; the goal here is clarity without the machine voice.

## When to Use

Use it when the reader needs to *understand* something: how a system works, why something failed, what the options are, what a trade-off costs, or what you found in an investigation. Anything they will act on, repeat to someone else, or decide from benefits.

## When Not to Use

- One-line factual answers, status pings, terse confirmations.
- Code, logs, diffs, command output.
- Quick acknowledgements and chat plumbing.

The point is that clarity is *earned* depth. Applying it to "what time is it?" is noise.

**Exception:** if they ask for "ASD-STE100" by name, go the whole way — approved vocabulary, "Do not" instead of "don't", no first person, labelled as such. They asked that way once and meant it.

## Keep (the 80% that helps)

1. One idea per sentence. Aim under about 20 words for steps, 25 for description.
2. Active voice with real verbs. "Decide" beats "make a decision".
3. One term per thing, and keep using it. If you call something "the daemon" and then "the service" and then "the agent", the reader spends attention working out whether those are the same thing or three things.
4. Define a term the first time it appears. Spell out an acronym once.
5. Name concrete numbers, paths, commands and IDs. "2 h 46 m, 17.3 m of filament" beats "a few hours".
6. Separate what you observed from what you inferred, and say plainly what you could not check.
7. Numbered steps for anything the reader will run themselves.

## Drop (the 20% that sounds robotic)

1. The approved-word dictionary. "Get" and "before" are fine; you do not need "obtain" and "prior to".
2. Contractions are banned in STE. Use them. "Don't" reads like a person.
3. STE discourages first person. Allow it — "I checked the exit node" is clearer than a passive construction.
4. Not every line has to be a command. A normal explanatory sentence is allowed.
5. Rigid "Do not" phrasing everywhere. Use a natural imperative instead.
6. STE restricts you to "must". Keep "should" and "might" where honesty needs them — never fake certainty to satisfy a style rule.
7. Do not force the mechanical structure onto something short. If three sentences say it, send three.

## Shape of a good explanation

1. Lead with the answer or outcome. State it plainly, no build-up.
2. Then the mechanism — how it actually works, so the answer is not a black box.
3. Then the limits: what could break, what you could not verify, what depends on someone else.
4. Then the next action, if there is one.
5. Add the proof where it matters: the actual command result, the file hash, the IP, the status code.

## Checklist before sending

- Does the first sentence answer the question?
- Any sentence over ~25 words? Split it.
- Does one term change meaning partway through?
- Is every claim backed by something you actually observed?
- Did you mark inference as inference?
- Would the reader know what to do next?

See `references/before-after-examples.md` for paired rewrites taken from real sessions.
