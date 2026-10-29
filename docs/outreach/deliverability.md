# Sending-domain setup (do before the first send)
Status: NOT verified. DNS could not be checked from this workspace. Fill the table, then run the checks.

| Item | Value to fill |
|---|---|
| Sending domain (not gmail.com; use a domain you own, ideally a subdomain such as mail.<domain>) | |
| ESP / sender (name the provider whose include and DKIM keys you use) | |
| Postal address for the footer ({{postal_address}}) | |

## DNS records (publish at the domain's DNS host)
1. **SPF** (one TXT per name; never two): `v=spf1 include:<ESP-spf-host> ~all` (use the exact include your ESP documents).
2. **DKIM**: add the CNAME/TXT records your ESP gives you (selector._domainkey.<domain>); then enable signing in the ESP.
3. **DMARC** at `_dmarc.<domain>` (TXT): start `v=DMARC1; p=none; rua=mailto:<your-address>; adkim=r; aspf=r`; after 2 clean weeks use `p=quarantine`, later `p=reject`.
4. **Reply-To / From** on the same domain; add a working mailbox so STOP replies are received.

## Verify (from any machine with dig)
`dig +short TXT <domain>` (SPF) | `dig +short TXT <selector>._domainkey.<domain>` (DKIM) | `dig +short TXT _dmarc.<domain>` (DMARC). Then send a test to a Gmail inbox, open "Show original" and confirm SPF, DKIM and DMARC = PASS.

## Warm-up and list rules
Start at 20 a day, double weekly while bounce stays under 2% and complaints near zero. Verify every address, never buy lists, keep a suppression list, honour STOP within 2 working days.
The `career` template is for people who enquired or opted in, not for scraped lists.
