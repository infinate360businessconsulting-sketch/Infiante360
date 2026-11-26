# Paid practice labs: scope and phases

Status: scoping only. Nothing is built or on sale. The page `lp/labs.html` is a waitlist, no price, no checkout.

## Decision for the owner
Build as a separate project, phased, with the first lab sold only when it works end to end. Do not sell labs before payment, delivery and refund terms exist.

## What is real today
- Simulator scenarios described on `academy/simulators.html` (hosting and access unverified).
- Learning platform and test series at techacademy.infinate360.in (TrainerCentral; feature set unverified).
- Cashfree is the preferred gateway; integration status unconfirmed. Refund, cancellation and payment terms not supplied.
- Static site on GitHub Pages / Vercel: no user accounts, no database, no per-learner state.

## Phases
| Phase | Deliverable | Needs |
|---|---|---|
| 0 (done) | Waitlist page and lead capture | Form to CRM (webhook confirmed?) |
| 1 | One paid lab (suggest identity and XDM): browser-based scenario with built-in answer checks, access through the LMS after payment | Lab content, payment path (TrainerCentral + Cashfree or payment link), refund terms |
| 2 | More labs (RTCDP, AJO, CJA, Web SDK) and per-learner progress | Accounts, database, hosting, support process |
| 3 | Verifiable credentials | Credential issuer design, legal wording, identity checks; only if real assessment exists |
| 4 | Team licences and hiring assessments | Admin view, contracts, privacy review |

## Key decisions needed
1. Delivery: browser-only simulated scenarios (cheaper, safe) or real vendor sandboxes (licence, terms and cost issues; not recommended).
2. Where learners log in: LMS or a new app.
3. Pricing, validity period, refund terms (all unknown; keep null until set).
4. Who builds and supports the labs, and the support hours.
5. Data and privacy: what learner data is stored and where.

## Risks
- Selling before delivery works: refund and consumer-law exposure.
- Calling something "AEP lab" or "Adobe" implies affiliation: keep the independence line, no vendor logos, no copied lab text or branding from other providers.
- Credential claims need real assessment to back them.
- Cost and support time grow with every lab.

## Next step
Owner picks Phase 1 topic, delivery model and price, and supplies refund terms. Then build the lab, test with five known learners, and only then open sales.
