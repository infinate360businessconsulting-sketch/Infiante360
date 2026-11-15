# Registration scaling plan: Infinite360 Tech Academy

Scope: the next MarTech SME Accelerator cohort (the 10-15 Nov run ends today) and every program after it.
Rule: every number below is a target or a formula. Replace the "Actual" column with your own counts before deciding anything. No benchmark is claimed as fact.

## 1. Context: where registrations come from today

| Asset | Role in the funnel | Already built |
|---|---|---|
| Registration Google Form (mandatory) | Single capture point | Yes |
| `lp/martech-sme-accelerator.html` | Landing page, calendar file, form | Yes |
| `lp/enterprise-martech-demo.html` | Enterprise lead page, detailed form | Yes |
| WhatsApp community and CXO community | Retention, reminders, referrals | Yes |
| YouTube (pack, playlists) | Search and discovery | Pack written |
| Meta ads pack | Paid acquisition | Written, not confirmed live |
| `/lms` and the learning platform | Post-registration access | Yes |
| Outreach (email, LinkedIn SDR) | Outbound to named people | Docs and sequences exist |

Gap to close first: you cannot scale what you cannot measure. Before spending anything, capture the source of every registration.

## 2. Measure first (day 1, free)

1. Add a hidden "Source" question to the Google Form. Give each channel its own link with UTMs: `?utm_source=youtube|whatsapp|linkedin|meta|email|referral&utm_campaign=sme-nov`. The landing page already stores UTMs in `sessionStorage` (`i360_attr`); pass them into the form link or a prefilled field.
2. One sheet, one row per registrant: date, source, role, company, country, consent flags, attended (Y/N), day attended, enquired, paid.
3. Weekly funnel (fill Actual): 
   Reach > Landing visits > Registrations > Joined day 1 > Attended 3+ days > Enquired > Enrolled.
   Registration rate = registrations / landing visits. Show-up rate = joined / registered. Enrol rate = enrolled / attended 3+ days.
4. Decision rule: a channel is scaled only when its cost (or time) per registration and its show-up rate are both known for at least one full cohort.

## 3. Scale levers, in order of cost

### A. Free and fast (this week)
- **Referral inside the community.** Ask each attendee to bring one colleague, using a personal link with `utm_source=referral&ref=<name>`. Ask in the closing minute of every session and as a pinned WhatsApp message. Use only an incentive you will actually honour (for example a bonus resource), stated in writing.
- **Replay-to-registration.** Post the session replay or a 3-5 minute clip with the registration link in the first line of the description. Do not promise a replay unless the platform provides it.
- **YouTube search.** Publish using `docs/youtube/youtube-pack.md`: keyword title, first two description lines, chapters, `10b` links block, pinned comment with the registration link. One search-led video per week beats one large launch.
- **LinkedIn.** Three posts per cohort: problem (a real AEP troubleshooting pattern), session recap (what was covered, no client names), and an invitation. Personal profile posts usually reach further than a new company page; use both.
- **WhatsApp broadcast and community.** Reminders at T-24h and T-1h with the joining link. Use only people who opted in.

### B. Low cost (next 2 weeks)
- **Paid test, small.** Follow `docs/meta-ads/campaign-pack.md` and the policy checklist. Start with one daily budget you can afford to lose entirely, one audience, three creatives, one landing page. Judge after 7 days on cost per registration and show-up rate, not clicks.
- **Retarget** landing visitors who did not register and video viewers (consented audiences only; needs the consent banner decision for regulated regions).
- **Partners.** Co-host a session with a community, college alumni group or practitioner group. Share the audience, not a list. You give the content, they give the reach.
- **Webinar listings.** List the free session on events pages relevant to Adobe and MarTech professionals.

### C. Outbound for enterprise
- Use `docs/outreach/` sequences and the AI SDR workflow for named roles (CDO, VP MarTech, delivery heads). Send only to lawful, opted-in or business-contact recipients, with opt-out and postal address. Do not email a list you cannot source.

## 4. Raise conversion before adding traffic

Traffic is wasted if the page leaks. Check these in order:
1. Above the fold: date, time in IST and one visitor-local time, price (free or paid), one button.
2. Form length. The enterprise form is detailed on purpose; for the open accelerator keep it to name, email, WhatsApp, role, goal. Ask the rest after registration.
3. Confirmation: instant confirmation, calendar file, joining link and WhatsApp community in one message (`docs/demo/confirmation-email.md`).
4. Show-up: reminders at T-24h and T-1h and a "what you will leave with" line. Registration without attendance does not sell.
5. Time zones: 10 PM IST suits India. For the US/EU/Gulf, run one repeat session at a local-friendly time before paying to advertise there.

## 5. Capacity and trust (scale safely)

- Confirm the Webinar.gg seat limit and plan before a registration push. Do not market past it.
- Say clearly whether the session is free. Keep "no guaranteed job, salary or certification" and the Adobe-independence line on every page and ad.
- Learning API (`platform/`) is not deployed. Registration scaling does not depend on it; access today runs through the white-label platform's activation keys.

## 6. 4-week cadence

| Week | Focus | Output |
|---|---|---|
| 1 | Measure | UTM links, source field, funnel sheet, replay clip, 1 YouTube video, 3 LinkedIn posts |
| 2 | Referral + partners | Referral ask in every session, 1 partner session booked |
| 3 | Small paid test | 1 audience, 3 ads, review on day 7 |
| 4 | Review and decide | Keep, cut or scale each channel on cost per registration and show-up rate |

## 7. What to scale up, hold or cut (rules)

- Scale a channel by up to 20-30% per step only if cost per registration is stable and show-up rate holds.
- Hold when show-up rate drops: fix reminders and page before adding spend.
- Cut a channel that gives registrations without attendance or enquiries after two cohorts.

## 8. Inputs needed to tune this (replace with actuals)

Registrations so far (by source), attendance per day, enquiries and enrolments, budget you can test with, whether the sessions are free, Webinar.gg seat limit.
