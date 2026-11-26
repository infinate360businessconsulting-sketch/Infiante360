# Batch registration: lead routing to the CRM

Page: `lp/batches.html` (src/content_batches.py). Reuses the site's form, so no new backend.

Flow: form submit -> FormSubmit email (existing) -> browser beacon to `/api/lead` (api/lead.js) -> `LEAD_WEBHOOK_URL` (n8n / Zapier / CRM webhook, set in Vercel env; optional `X-Webhook-Secret`).

Not verified: whether `LEAD_WEBHOOK_URL` is set on Vercel, and which CRM receives it. Owner to confirm. No credentials belong in this repo.

## Payload fields the relay forwards
first_name, last_name, email (required), phone, company, job_title, country, interest, preferred_contact, message, source_page, form_type, utm_source, utm_medium, utm_campaign, utm_term, utm_content, referrer, received_at.

## Suggested CRM mapping
| Form field | CRM field |
|---|---|
| first_name, last_name, email, phone | Name, Email, Phone |
| interest = "Batch registration" | Lead source detail / tag `batch-registration` |
| message | Notes (contains the preferred batch) |
| source_page = .../lp/batches.html | Landing page |
| utm_* | Campaign fields |
| preferred_contact | Contact preference |

Statuses to create: New, Contacted, Demo attended, Registered, Not now. Follow up within two business days (the page promises this).
Consent: only message people who ticked the consent boxes on the form.
