# Before / after — real rewrites

Each pair is the same technical content. The left column is the robotic
full-STE version. The right column is the 80% version: same clarity, natural
tone. Use these as calibration, not as templates to copy.

## 1. Why a keyboard cannot unlock a pattern lock

Robotic (full STE):

> A keyboard can write a PIN or a password. A keyboard cannot draw a pattern. A
> mouse can draw a pattern. Do not make many wrong attempts immediately.

80% version:

> A keyboard can type a PIN or a password, but it can't draw a pattern — Android's
> pattern grid isn't keyboard-navigable. A mouse can, because it drags. So if you
> want the Flipper to attack a pattern, the mouse mode is the only one that works.
> Go easy on the attempts: five wrong tries triggers a 30-second lockout.

## 2. Is the dark web safe to search?

Robotic:

> The local machine has no attack surface. No JavaScript executes. No cookies are
> stored. The exit node cannot read the traffic.

80% version:

> There's no attack surface on your machine when I read for you. Nothing executes
> — no JavaScript, no cookies, no logins, nothing opens a downloaded file. And on a
> `.onion` address the traffic is encrypted end to end inside Tor, so even the exit
> node can't see it. What's left is Tor's crypto failing, or the site lying to you.
> Neither can touch your machine.

## 3. A domain that has been dropped

Robotic:

> The registry returns No match. DNS over HTTPS returns status 3. Zero issuances
> exist in certificate transparency. Zero snapshots exist in the archive.

80% version:

> The domain is gone, not just unreachable. Four independent checks agree: the .net
> registry says "No match" for the name, both Google and Cloudflare DNS return
> NXDOMAIN, certificate transparency has nothing current, and the Wayback Machine
> holds no snapshot at all. The old hosting IP still answers, but its TLS handshake
> fails, so the edge has detached the hostname. Practically: the name is dropped and
> you can register it again.

## 4. Faulty assumption, stated honestly

Robotic:

> Filtering was not the cause. The domain does not resolve.

80% version:

> I first blamed DNS filtering, and that was wrong. The local resolver was telling
> the truth — the domain itself is gone. DNS-over-HTTPS, which bypasses the local
> resolver entirely, returned the same NXDOMAIN, and the registry has no record.

## 5. A trade-off with a real cost

Robotic:

> The procedure has a disadvantage. Time is lost.

80% version:

> The catch is the lockout timer. Android throttles the lock screen, so a full
> sweep of all 389,112 patterns at 30 seconds per five tries is a siege, not a
> brute force. That's why this only works from a shortlist.

## What the pairs have in common

- The outcome comes first.
- Numbers and concrete mechanisms carry the explanation.
- Uncertainty is named instead of hidden.
- Sentences are short, but they still sound like a person talking.
