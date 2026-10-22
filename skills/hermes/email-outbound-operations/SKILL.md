---
name: email-outbound-operations
description: Send/reply to emails with safe attachments and verification.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [email, outbound, attachments, verification, himalaya]
    related_skills: [himalaya, email-inbox-triage, google-workspace]
---

# Email outbound operations

## When to Use

Use this skill when the task is to send, reply to, or follow up on an email,
especially when attachments, thread context, or verification matter.

Connector skills own provider-specific commands. This skill owns the outbound
safety pattern: compose, attach, send, and read back proof before telling the
user it landed.

## Core procedure

1. **Confirm the mutation boundary.** Sending email is an external side effect.
   Use the latest user instruction as the approval scope: recipients, attachment,
   thread, and message intent. If the user says to send them the attachment first
   for approval, create and deliver only the local/user-facing artifact, then stop;
   a later approval such as "send it" authorizes sending that exact approved file
   to the previously named recipient unless the user changes scope.
2. **Keep thread context.** Preserve `Subject`, `In-Reply-To`, and `References`
   when replying so the mail stays on the original thread.
3. **Resolve attachment exposure before sending.** If a spreadsheet, export, or
   report may expose secrets, credentials, IDs, private paths, or personal data,
   create an email-safe version and state what was withheld.
4. **Prefer raw MIME for attachments.** Generate a real MIME email with Python's
   `email.message.EmailMessage`, attach bytes with the correct MIME type, and send
   with `himalaya message send < message.eml`.
5. **Verify from Sent.** Export or read back the sent item and verify the raw MIME
   contains `Content-Type: multipart/mixed`, `Content-Disposition: attachment`,
   and the expected filename. Envelope `has_attachment` metadata can be false even
   when the raw sent MIME has the attachment.
6. **Report provider-confirmed results.** Include sent item id/time when available
   and mention the exact attachment filename.

## Himalaya attachment pattern

`himalaya template send` is reliable for plain text templates, but for attachments
prefer raw MIME. Some MML attachment markup can be preserved as visible body text
rather than compiled into a real attachment, depending on usage/version.

Use this pattern:

```python
from pathlib import Path
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

attachment = Path('/path/to/report.xlsx')
msg = EmailMessage()
msg['From'] = 'Sender <sender@example.com>'
msg['To'] = 'Recipient <recipient@example.com>'
msg['Cc'] = 'Other <other@example.com>'
msg['Subject'] = 'Re: Original subject'
msg['In-Reply-To'] = '<original-message-id>'
msg['References'] = '<original-message-id>'
msg['Date'] = formatdate(localtime=True)
msg['Message-ID'] = make_msgid()
msg.set_content('Attached is the corrected spreadsheet.\n')
msg.add_attachment(
    attachment.read_bytes(),
    maintype='application',
    subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    filename=attachment.name,
)
Path('/tmp/outbound.eml').write_bytes(msg.as_bytes())
```

Then send and verify:

```bash
himalaya message send < /tmp/outbound.eml
himalaya envelope list --folder '[Gmail]/Sent Mail' --page-size 5 --output json
himalaya message export --folder '[Gmail]/Sent Mail' SENT_ID --full > /tmp/sent.eml
python3 - <<'PY'
from pathlib import Path
raw = Path('/tmp/sent.eml').read_text(errors='ignore')
for term in ['Content-Type: multipart/mixed', 'Content-Disposition: attachment', 'report.xlsx']:
    assert term in raw, term
print('attachment verified')
PY
```

## Sustained outreach campaigns

When one send is not the job — writing to many organisations and then handling
whatever comes back until a real human who can decide the matter is in live
contact with the user — the campaign has its own rules. See
`references/sustained-outreach-campaigns.md` for the full playbook and the
scheduled-watch recipe.

- Verify every address against the institution's own contact, staff or
department page before sending. Never guess a first-name or initial pattern.
- Send to a NAMED person wherever one exists — department contacts, faculty
officers, heads of school — with role mailboxes as Cc only. Where no named
address surfaces, send role mailboxes anyway and expect to escalate.
- Treat replies in three classes: automated receipt (record the reference and
mine it for the redirect, never call it an answer), bounce (research the right
person and re-send, stating plainly that the general address bounced), and human
reply (answer every question asked, supply the user's profile, and steer back to
the goal).
- Keep a matter-scoped log of what arrived, what you did, and what is
outstanding so later runs do not repeat actions.
- When the campaign must outlive the session, schedule it as a cron job with
`continuity` and `attach_to_session` so the user can reply into the thread, and
deliver to the chat they are already in.
- Report only substantive developments: a human answer, a document request aimed
at the user, a fixed bounce, a named person now able to help, or a deadline.
Automated receipts get one line or nothing; never pad.

## Pitfalls

- Do not send externally during an approval-first workflow just because the intended recipient is already known; the approval step is the safety boundary.
- Do not trust a successful send command alone for attachment delivery.
- Do not trust `has_attachment` envelope metadata alone; inspect raw MIME.
- Do not resend after ambiguous failure until Sent has been checked. SMTP may have
  succeeded while save-to-Sent failed.
- Do not send a full working spreadsheet if only an email-safe version belongs on
  the thread.
- Do not expose raw credentials, login sheets, private paths, or personal IDs in
  attachments. Withhold rows or produce a sanitized copy.
- Role mailboxes (`admissions@`, `rpl@`, `enquiries@`, `ssc@`, `info@`) routinely
  bounce or auto-reply without answering. A bounce is a signal to find a person,
  not to retry the same address.
- Do not read a ticket receipt as an answer, and do not discard auto-replies:
  they often carry the actionable redirect — a different office, a mailbox that
  will not answer, or a wait-until date.
- `himalaya envelope list --output json` returns envelope metadata only, with no
  body; read the individual message to see what is actually being asked.

## Verification checklist

- [ ] Recipients and CC match the user's instruction.
- [ ] Thread headers are present for replies.
- [ ] Attachment file exists and opens or has a verified format/signature.
- [ ] Exposure review completed for the attachment.
- [ ] Sent raw MIME contains the attachment filename and attachment disposition.
- [ ] Final report distinguishes sent email from local file creation.
