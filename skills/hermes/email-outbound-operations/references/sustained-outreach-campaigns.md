# Sustained outreach campaigns

Use when the task is not one email but a campaign: write to a set of
organisations, then handle whatever comes back until a real human who can decide
the matter is in live contact with the user. Typical classes: university
admission enquiries, bursary or supplier outreach, regulatory and admin
correspondence, lead generation with a named-contact requirement.

## Procedure

1. Build the target list with addresses verified against each organisation's own
   contact, staff or department page. Prefer named individuals (department
   contacts, programme coordinators, faculty officers, heads of school) with role
   mailboxes as Cc.
2. Write one reusable enquiry body: who the user is, their qualifications or
   situation, the precise questions asked of everyone, and an offer of the
   supporting documents they can supply. Adapt only the opening paragraph per
   recipient so each letter names the specific programme or service.
3. Send from the user's own account and verify each send from Sent; report the
   sent item ids. Keep the composed messages on disk under a `sent/` directory so
   later re-routes can reuse the body verbatim.
4. Classify every reply before acting:
   - *Automated receipt* - record the ticket/case reference, mine it for a
     redirect (a different office, a mailbox that will not answer, an
     away-until date), and never report it as an answer.
   - *Bounce* - the address is wrong. Research the organisation's own pages for a
     named person who can decide, re-send to them, and say in the message that
     the general address bounced.
   - *Human reply* - answer every question asked, supply the user's details and
     documents, and ask what their reply leaves open. Then tell the user who is
     now in contact and what the next step is.
   - *Redirect* - email the named person or office directly, keeping the thread
     subject.
5. Stop only when the user is in live contact with a named human who can rule on
   the matter. Short of that, keep re-routing.

## Commands that work

```bash
# send an enquiry from a header/body file
himalaya template send < sent/<campaign>-<recipient>.eml

# verify it landed
himalaya envelope list --folder Sent --page-size 8 --output json

# scan the inbox for replies (metadata only - no body)
himalaya envelope list --folder INBOX --page-size 40 --output json

# read one message in full to see what is being asked
himalaya message read <id> --folder INBOX
```

Filter the envelope listing in Python by sender domain (or `postmaster` /
`mailer-daemon` for bounces); the JSON carries id, date, from and subject, so a
script can do the triage and the agent only reads what matters.

## Scheduled watch recipe

To keep the campaign running past the session, create a cron job that:

- runs a small script that lists only relevant new mail (sender-domain filter,
  id/date/from/subject) and prints it for the agent;
- carries the full campaign context in its prompt: the user's profile, the goal,
  every address already contacted with the reference numbers issued, the
  standing rules for classifying and answering replies, and the log file path;
- sets `continuity` (so each run sees the previous run's output) and
  `attach_to_session` (so the user can reply into the thread from chat);
- appends a dated entry per run to a log file in the campaign directory and is
  told never to repeat an action already recorded there;
- reports only substantive developments, with permission to stay quiet when a
  run brings nothing but automated receipts.

A short script is worth writing rather than asking the agent to run the listing
by hand each time: it keeps token cost low and makes each run deterministic.

## Pitfalls

- Sending the same text to a generic mailbox at every organisation gets
  auto-replies at best. Go to people.
- A campaign with no log file repeats itself: the same re-route, the same
  courtesy reply, twice.
- Document requirements differ per organisation (some want certified copies as
  PDFs, some cap file size, some accept online uploads only). State the specific
  requirement when asking the user for documents.
- Deadlines published by an organisation may already have passed for the current
  cycle; quote the intake the user can actually apply for, not the one printed on
  the page today.
