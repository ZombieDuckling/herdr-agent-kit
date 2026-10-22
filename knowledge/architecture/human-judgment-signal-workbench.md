# human-judgment signal workbench

Use this shape when the decision depends on taste, perception, trust, risk
tolerance, or audience fit. The goal is not to pretend subjective judgment is
objective. The goal is to make human reactions concrete enough that AI can
translate them without replacing the humans who own the decision.

## package shape

```text
judgment-workbench/
  README.md                 # purpose, audience, protected source rules
  manifest.md               # artifacts, prompts, segments, review status
  artifacts/                # options, boards, prototypes, excerpts, screenshots
  reactions/                # structured marks, ratings, notes, or ballots
  segments/                 # role/audience definitions without personal data
  analysis/                 # AI summaries, disagreement maps, decision memos
  decisions/                # accepted choice, threshold, owner, date, rationale
```

## capture rules

1. Show people concrete artifacts, not only abstract adjectives.
2. Store the prompt or question beside every reaction set.
3. Record examples and anti-examples; both carry signal.
4. Segment by decision-relevant role or audience class, not by personal identity.
5. Preserve disagreement instead of averaging it away.
6. Name the threshold or risk tolerance before turning reaction data into a
   recommendation.

## AI role

Ask the model to:

- summarize patterns in likes, dislikes, and contested items;
- compare segments and identify where agreement breaks;
- translate vague preference language into concrete design or product claims;
- produce questions for the human decision owner;
- cite the reaction set and artifacts used.

Do not ask the model to declare the final subjective answer unless a human owner
has explicitly delegated that choice and provided an acceptance rule.

## done test

A recommendation is reviewable when it includes:

- the artifacts people reacted to;
- the prompt they answered;
- the structured reaction data or aggregate view;
- the segment or audience definition;
- the disagreement or risk-tolerance threshold;
- the human decision still required.