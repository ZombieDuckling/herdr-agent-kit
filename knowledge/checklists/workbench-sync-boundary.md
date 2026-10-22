# workbench sync boundary checklist

Use before exposing a folder workbench through a connector, shared workspace, or multi-client editing layer.

## template and state

- [ ] Canonical template and mutable workbench copy are separate.
- [ ] Front desk names the canonical source, active copy, owner role, and current status.
- [ ] Manifest lists files included in import/export and files deliberately excluded.
- [ ] Generated artifacts and review outputs have stable paths.

## authority boundary

- [ ] Connector is scoped to a single org/project/workspace boundary.
- [ ] Actor identity is recorded for reads, writes, exports, and privileged tool calls.
- [ ] Roles define who may read, write, export, invite, approve, and administer.
- [ ] Cross-workspace access is tested and fails closed.

## integration and secrets

- [ ] Secrets, provider keys, account tokens, cookies, and connection strings are outside editable/exportable files.
- [ ] Tool calls use scoped server-side integration records or brokers.
- [ ] Export and grep checks prove no credential-shaped material travels with the package.
- [ ] Logs redact protected values and do not become a backdoor export.

## convergence and review

- [ ] Two approved clients can see the same file list and current file contents.
- [ ] A permitted edit from one client is visible to another with actor, time, and diff.
- [ ] Stale reads, failed writes, and partial exports are surfaced as errors, not silent success.
- [ ] Reviewer can inspect changed files, request slip, artifact, and rollback path.

## portability

- [ ] Export contains a manifest, source files, derived files, artifacts, and review ledgers.
- [ ] Export excludes caches, secrets, session-only chat state, provider internals, and raw private data that should not travel.
- [ ] Re-import or fresh-client open test succeeds from the exported package.
