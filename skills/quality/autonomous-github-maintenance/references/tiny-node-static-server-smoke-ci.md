# Tiny Node static-server smoke CI pattern

Use this pattern for small JavaScript/Node portfolio repos that have a hand-written `http.createServer(...)` static server, no `package.json`, and no CI/tests.

## High-value slice

Add a zero-dependency test and PR workflow before changing product/UI behavior:

- `package.json` with `type: module`, `start: node server.mjs`, and `test: node --test`.
- `test/server.test.mjs` using built-in `node:test` and `node:assert/strict`.
- `.github/workflows/ci.yml` running `npm test` on PRs and pushes to the base branch.
- A `PORT` env override in the server so tests can spawn it on a free local port without colliding with the default port.

## Test structure

1. Allocate a free port with `node:net`.
2. Spawn `node server.mjs` with `PORT=<free port>` and capture stdout/stderr.
3. Poll `GET /` until the server accepts connections.
4. Assert:
   - `GET /` returns `200`, `text/html`, and a known page title/string.
   - API/status route returns JSON with stable top-level keys; accept offline upstream failures when the server is designed to keep listening after refresh errors.
   - Missing static files return a sanitized `404` body, not raw `ENOENT`, absolute temp paths, or source content.
   - Encoded traversal such as `/%2e%2e/server.mjs` does not expose server source.
5. Always kill the child process in `finally` and wait briefly for exit.

## Static-serving hardening to pair with tests

If the server currently uses a brittle prefix check like:

```js
const safePath = path.normalize(filePath);
if (!safePath.startsWith(publicDir)) { ... }
```

prefer:

```js
const requestedPath = url.pathname === '/' ? 'index.html' : decodeURIComponent(url.pathname.replace(/^\//, ''));
const safePath = path.normalize(path.join(publicDir, requestedPath));
const relativePath = path.relative(publicDir, safePath);

if (relativePath.startsWith('..') || path.isAbsolute(relativePath)) {
  res.statusCode = 403;
  res.end('Forbidden');
  return;
}
```

Also convert `ENOENT` read failures to sanitized `404 Not found` JSON instead of returning raw filesystem errors.

## Pitfalls

- Browser/fetch clients may normalize encoded dot-segments before the request reaches Node. For encoded traversal assertions, use `node:http.request` with the raw path rather than `fetch()` if you need to preserve `/%2e%2e/...`.
- Some frameworks/Node internals may resolve encoded traversal into a missing in-root path and return `404` rather than `403`. The durable security assertion is that the response does not include source content or absolute filesystem/`ENOENT` details; accepting either `403` or sanitized `404` can be reasonable.
- Remove incidental agent metadata such as `.omc/` before staging.
- Keep the PR small: test/CI/static-serving hardening only; defer UI/product changes and upstream fetch timeout work to follow-up slices.