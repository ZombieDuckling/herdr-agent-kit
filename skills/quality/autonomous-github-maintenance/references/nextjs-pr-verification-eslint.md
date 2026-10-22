# Next.js PR verification with non-interactive ESLint

Use this pattern for small Next.js repos that have no pull-request checks or whose `npm run lint` still uses deprecated `next lint` and prompts interactively in automation.

## When it applies

- App is a Next.js project with `package.json` scripts like `build: next build` and `lint: next lint`.
- `npm run lint` prints the Next.js deprecation notice and asks how to configure ESLint instead of exiting cleanly.
- The repo has no GitHub Actions workflow for PR lint/build verification.

## Safe maintenance slice

1. Add a non-interactive ESLint config:
   ```json
   {
     "extends": ["next/core-web-vitals", "next/typescript"]
   }
   ```
   Save as `.eslintrc.json` when using ESLint 8-compatible Next config.

2. Add `.eslintignore` so generated files do not fail lint:
   ```text
   next-env.d.ts
   .next/
   node_modules/
   out/
   build/
   ```

3. Install lint dependencies compatible with the repo's Next major/minor. For a Next 15 app, prefer a matching `eslint-config-next@15.x` instead of accidentally pulling Next 16 peer expectations:
   ```bash
   npm install --save-dev eslint@^8.57.1 eslint-config-next@15.5.19
   npm pkg set scripts.lint='eslint . --ext .js,.jsx,.ts,.tsx'
   ```
   Adjust the exact `eslint-config-next` version to match the Next line present in `package-lock.json` or the resolved local Next version.

4. Add a pull-request workflow:
   ```yaml
   name: PR verification

   on:
     pull_request:
       branches: [main]

   permissions:
     contents: read

   jobs:
     verify:
       name: Lint and build
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v4

         - name: Set up Node
           uses: actions/setup-node@v6
           with:
             node-version: 22
             cache: npm

         - name: Install dependencies
           run: npm ci

         - name: Lint
           run: npm run lint

         - name: Build
           run: npm run build
   ```

5. Update README with the verification commands and any outdated deployment/storage notes discovered while inspecting the repo.

## Verification

Run locally before commit:

```bash
npm run lint
npm run build
git diff --check
git diff --stat
```

Then push a feature branch, open/update a PR, and watch the new GitHub Actions run with:

```bash
gh run watch <run-id> --repo OWNER/REPO --exit-status
```

## Pitfalls

- Do not leave `next lint` in `package.json`; it can become an interactive prompt in cron/CI and block automation.
- Do not install bare `eslint-config-next` without checking the repo's Next line; npm may select a newer major with incompatible peer dependency behavior.
- ESLint warnings like `@next/next/no-img-element` may be acceptable for a CI-restoration PR if they do not fail the command. Report them as follow-up rather than expanding the slice.
- Keep dependency/security upgrades separate if `npm audit` reveals high advisories requiring a broader Next upgrade. Do not bundle a major framework upgrade into a simple CI restoration PR unless that is the chosen slice.
