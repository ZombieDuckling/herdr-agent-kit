# Dashboard visual pass checklist

Session-derived orchestration note for utility-first dashboard redesigns.

## Working split
- **Design pass:** source edits, asset wiring, spacing, hierarchy, and layout simplification.
- **Audit pass:** look for landing-page residue, promo copy, oversized whitespace, decorative noise, and generic SaaS visuals.

## Defaults that worked
- Start from the repo’s own `CLAUDE.md` / project instructions.
- Keep the first view dashboard-first: status, evidence, logs, readiness, fleet summary.
- Prefer compact widgets and evidence blocks over hero composition.
- Keep imagery functional and subordinate to data.
- Reduce anything that reads like a sales page, product brochure, or marketing landing.

## Verification
1. Run tests.
2. Restart or reuse the live server.
3. Fetch the rendered page.
4. Grep for old hero/marketing strings.
5. Confirm the compact dashboard markers are present.
