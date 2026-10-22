# workbench sync plane

A portable workbench becomes collaborative only when the folder state can move across clients without losing authority boundaries, reviewability, or secret isolation. Treat connector protocols as the sync and authorization plane around the workbench, not as the product itself.

## layers

| layer | purpose | required proof |
|---|---|---|
| Source template | Canonical package of maps, instructions, examples, schemas, and starter files | It can be copied without modifying the baseline |
| Mutable workbench | Active per-user or per-team copy where work happens | Current files, requests, decisions, and artifacts are visible |
| Workspace boundary | Explicit org/project/workspace scope and permissions | A caller can access only the intended workspace |
| Connector endpoint | Controlled read/write/export interface for approved clients | A second client sees the same current state |
| Import/export manifest | Inventory of files, versions, ignored paths, and generated artifacts | Export can be checked and re-imported without guesswork |
| Integration layer | Provider credentials, external accounts, and privileged tools outside the files | Workspace export contains no secrets, while tools still work through scoped calls |
| Review surface | Diffs, logs, artifacts, actor identity, and merge/approval state | A reviewer can answer who changed what and why |

## design rules

1. Start with the folder object: front desk, manifest, request slips, tool registry, artifacts, and review ledgers.
2. Preserve a template/copy split before enabling shared editing.
3. Scope every connector to one explicit workspace boundary; never let a generic endpoint imply global file access.
4. Keep credentials and external integrations outside editable/exportable files.
5. Require both import and export tests; a workbench that cannot leave its host is a hosted session, not a portable system.
6. Make cross-client state convergence observable: file list, file contents, current request, actor identity, and last changed time.
7. Treat connector failures as authority failures until proven otherwise; stale state can be more dangerous than no state.

## anti-patterns

- Calling a workspace production-ready because one client can chat with it.
- Letting protocol branding replace template/copy/export/review design.
- Exporting raw folders without an ignore policy, manifest, and secret scan.
- Sharing a connector endpoint before role, data, and tool rights are explicit.
- Relying on a provider session history as the handoff artifact.

## done test

An approved second client can list the intended workbench, read the same current files, make a permitted edit, see the diff or activity record, export the current package, and fail to access a different workspace or any credential material.

Related laws: [WB-2](../notes/08-workbench-architecture.md#wb-2-preserve-the-template-and-work-in-a-copy), [WB-3](../notes/08-workbench-architecture.md#wb-3-multiplayer-means-shared-artifacts-not-shared-vibes), [WB-7](../notes/08-workbench-architecture.md#wb-7-secrets-are-integrations-not-files), [WB-12](../notes/08-workbench-architecture.md#wb-12-export-the-workbench-not-the-hosted-session), [WB-25](../notes/08-workbench-architecture.md#wb-25-connectors-are-the-sync-plane-not-the-workbench).
