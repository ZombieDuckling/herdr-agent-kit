# House rules

Your standing preferences. Every agent reads this file (`~/.herdr-agent/house-rules.md`) at the start of
work, and these rules win over any skill. The bootstrap agent fills it in with you once; edit it any time.
Lines starting with `[x]` are on, `[ ]` are off.

## About you
- Name the agents should use for you: {{NAME}}
- How you like reports: result first, short, numbers as proof, at most one question. {{REPORT_STYLE}}
- How much to ask you: decide small reversible things alone; ask only about money, access, commitments
  to other people, irreversible actions, and taste. {{ASK_LEVEL}}

## Safety
- [x] Never push, deploy, merge, publish or send anything without my "yes" for that exact action.
- [x] Never print, copy or commit passwords, tokens or keys.
- [x] When a safety system refuses an action, do not work around it; give me the exact command and why.

## Credit and disclosure
- {{NO_AI_CREDIT}} No AI author or co-author lines in commits, pull requests, issues or contributor lists.
- {{EMAIL_DISCLOSE}} Any email sent from my accounts says it was written and sent by an AI on my behalf.

## Design taste
- {{NO_GRADIENTS}} No CSS gradients or gradient overlays in any design, not even for text legibility.
- [x] Real photos of the real business first; generated images only where no real one can do the job,
      and never presented as real photos.
- [x] Honest copy: no invented testimonials, logos, metrics, awards or prices.
- [x] Respect `prefers-reduced-motion`; fast on a phone.

## Workers and cost
- [x] Cheapest capable worker first: free/local (OpenCode) → small paid model → strong model only for
      judgement or vision.
- [x] Workers run in visible herdr tabs, never hidden.
- [x] Nothing a worker produced goes into a commit, PR, comment or email until the lead has checked it.

## Quality
- [x] Audits use real scanners (SonarQube or eslint+sonarjs, semgrep) and report numbers.
- [x] Anything that runs in a browser is checked running: console errors, 404s, dead buttons, axe, phone width.

## My projects
<!-- One line per project the agents should know about: name, folder, who answers business questions,
     how it deploys, traps. Example:
- Shop site: ~/Projects/shop. Business questions → the owner, by email. Deploy: push to main (Cloudflare Pages). Run the cache-bust script first.
-->

---
Example of a filled-in set (the kit author's): no AI credit lines, AI disclosure on every email, no
gradients ever, real photos first, OpenCode on a local model for labour, a Claude lead per project,
nothing pushed without an explicit yes.
