# team/workflow map architecture

A second brain for an organization or recurring operation should model work before
it accumulates notes. Start with addressable nouns and verbs so humans and agents
can answer who does what, what each workflow consumes, and what it produces.

This is a lightweight graph expressed as files and tables. It is not a reason to
install graph infrastructure before the workflow has proved its shape.

## minimum files

```text
workflow-map/
  README.md              # scope, freshness, source method, how to read the map
  entities.md            # teams, roles, systems, inputs, outputs, artifacts
  workflows.md           # named workflows, owners, status, acceptance criteria
  relationships.md       # consumes / produces / hands-off-to / reviews / blocks
  evidence.md            # interviews, documents, observations, and confidence
  questions.md           # unresolved edges, missing owners, risky assumptions
```

## entity table

| id | type | label | description | owner/steward role | evidence | confidence |
| --- | --- | --- | --- | --- | --- | --- |
| ENT-001 | team / role / system / input / output / artifact |  |  |  |  | unknown |

## relationship table

| from | verb | to | workflow | evidence | confidence | review note |
| --- | --- | --- | --- | --- | --- | --- |
| ENT-001 | consumes / produces / hands-off-to / reviews / blocks | ENT-002 | WF-001 |  | unknown |  |

## build order

1. Name the outcome the map must support.
2. List the nouns: teams, roles, systems, inputs, outputs, artifacts, and
   external dependencies.
3. List the verbs: consumes, produces, reviews, approves, blocks, hands off to,
   escalates to, and updates.
4. Attach each relationship to evidence and confidence instead of writing broad
   prose from memory.
5. Create one workflow row that a fresh operator can follow end-to-end.
6. Only add semantic search, graph views, or automation after the file map answers
   real onboarding and routing questions.

## anti-patterns

- dumping relationship sentences into random notes with no stable entity id;
- building embeddings before the team can name its workflows and outputs;
- drawing a beautiful graph with no evidence or freshness fields;
- mapping every possible relationship instead of the ones needed to route work;
- hiding human judgment, review, or approval in prose instead of edges.

## verification

A fresh human or agent should be able to answer:

- which role owns the workflow;
- which inputs it consumes;
- which outputs it produces;
- who reviews or accepts the output;
- which evidence supports each claim;
- where confidence is low or the map is stale.
