# Outreach engine (Explore -> Campaigns -> Prospects -> Decision makers -> Emails -> Send -> Meetings -> Learn)
| Step | What to do | Artifact |
|---|---|---|
| 1 Explore competitors | Fill 10-15 rows from public pages only | competitors-template.csv |
| 2 Define campaigns | Six campaigns with offer, signal, titles, cap | campaigns.csv |
| 3 Find companies | Use the signal column; Job Intelligence sheet for hiring signals | prospects-template.csv |
| 4 Find decision makers | Titles per campaign; source from public profiles or a licensed vendor | prospects-template.csv |
| 5 Find and verify emails | Waterfall: Hunter, then Findymail, then LeadMagic; send only to "valid"; skip "catch_all" or review first; never guess addresses | email_verification column |
| 6 Write emails | Three-email sequences with one real signal each | sequences.md |
| 7 Send | Extend docs/autopilot workflow: Sheet -> score -> Claude draft -> Gmail DRAFT -> you approve -> send; cap per campaign | docs/autopilot |
| 8 Book meetings | Calendar link in email 1; log meeting in status | status column |
| 9 Learn | Weekly: open/reply/meeting by campaign; pause campaigns under 1% reply after 200 sends; edit the signal or offer | dashboard sheet |
## Compliance (must follow)
- Business-to-business only, to role-relevant work addresses; identify yourself; include opt-out and a postal address; honour STOP within 2 working days and keep a suppression list (do_not_contact, unsubscribed).
- Check rules for the recipient's country (for example CAN-SPAM, GDPR/PECR, India DPDP). Seek legal advice for EU/UK mail; consent may be required for some recipients.
- Do not buy scraped lists, guess emails, or send to unverified or catch-all addresses at volume. Warm up the sending domain, set SPF, DKIM, DMARC; start at 20 per day.
- No LinkedIn automation. No claims of results, clients or certifications without proof.
- Credentials for Hunter, Findymail, LeadMagic, Gmail and Anthropic live in n8n credentials only.
## Metrics to review weekly
Sent, delivered, bounced (target under 2%), replies, positive replies, meetings booked, meetings held, proposals, enrolments, STOP requests.
## Sample data
The screenshot you shared belongs to another tool's campaign; its people and emails are not used here.

## HTML email templates (cold, one-to-one B2B)
- Generate: `python3 scripts/build_emails.py` -> `docs/outreach/email-html/{enterprise,cxo,training,capacity}.html` + `.txt` + `preview.html`. Fee and cohort come from `content/cxo-hive.json`.
- Merge tags: `{{first}} {{company}} {{signal}} {{postal_address}}`. Fill `{{postal_address}}` (required) and one sourced `{{signal}}` per prospect before sending.
- Each CTA links to `lp/adobe-martech-conversation.html?utm_content=<segment>`: the page preselects the form interest, and UTMs are saved with the enquiry (same form as the rest of the site).
- Segments: enterprise, cxo, training, capacity (cold B2B) and career (opted-in or enquiring learners only). See deliverability.md before the first send.
- Send flow: paste into the Gmail DRAFT step of the autopilot, approve, send. Start at 20 a day; SPF, DKIM, DMARC first. Pause a segment under 1% reply after 200 sends.
