# Sales autopilot (Gojiberry-style, compliant)
Flow: signals sheet -> score (scoring.json) -> filter/dedupe/cap -> Claude drafts -> Gmail DRAFT -> you review and send -> logged.
Signals sheet columns: email,name,company,title,signal,touches,consent,unsubscribed,do_not_contact. Fill from: form/WhatsApp enquiries, webinar/demo registrations, attendance, page views from analytics, job-pipeline hiring signals, Clay enrichment (consented/business data only).
Setup (you do in n8n, never paste keys in chat/Git): create credentials for Google Sheets, Gmail, and an HTTP Header Auth named for the Anthropic key (header x-api-key). Replace SIGNALS_SHEET_ID. Import JSON, test with 2 rows.
Not included on purpose: LinkedIn auto-connect/auto-message bots (breach LinkedIn terms, risk account bans) and fully automatic sending. Drafts stay human-approved; every mail carries a STOP line; honour unsubscribes; check India DPDP/GDPR/CAN-SPAM for each region; caps in scoring.json.
Untested in a live n8n instance: JSON parses, but node parameters may need small adjustments for your n8n version.
