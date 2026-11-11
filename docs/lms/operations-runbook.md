# Learning suite: operations runbook

Public page: https://infiante360techacademy.com/lms (file `lms.html`). Login: https://techacademy.infinate360.in/ (white-label learning platform admin at `/wl_admin`).

## Roles
- Static website (this repo, GitHub Pages): marketing, enquiry forms, /lms landing page.
- Learning platform (white-label backend): accounts, courses, live classes, video courses, test series, e-library, activation keys, reports. Admin menu: Analytics, Content, Courses & Packages, Activation Keys & Coupons, Customization, Settings, Manage Users, Test Report, Add-ons Marketplace.
- Live classes: the classroom link already in use (the platform's live class / Webinar.gg session). Confirm with the vendor where recordings are stored and whether they can be exported before promising replay access.

## Activation workflow (back end)
1. Create or confirm the course/package and its test series in Courses & Packages.
2. Activation Keys & Coupons: generate keys per package, set validity/expiry and a batch label (for example `AEP-NOV26-A`). Generate in bulk for cohorts and corporate batches.
3. Share each key privately with the paid learner (email or WhatsApp). One key, one account.
4. Learner logs in, redeems the key. Check Manage Users and Test Report to confirm activation.
5. Expire or revoke keys when a plan ends; keep a sheet of key, buyer, plan, date, status (no payment card data).

## Scale
- The website is static and CDN-served, so traffic spikes do not touch the learning platform.
- Capacity of live classes, video bandwidth and test concurrency depends on the vendor plan. Ask the vendor for limits, load-test a mock exam before a big batch, and stagger test start times.
- Use batch-labelled keys and packages per cohort, so reports and expiry stay manageable at thousands of learners.

## Security and privacy
- Never post activation keys, API tokens or admin URLs publicly. Rotate any key that was shared publicly.
- The classroom link currently on public pages gives access to a test-series page; if it should be learner-only, remove it from public pages.
- Do not publish earnings or user counts from the admin dashboard without checking they are accurate and intended.

## AI roadmap (not live)
Phase 1 live: rule-based path finder on /lms. Phase 2: AI study assistant grounded in course material, called server-side (API key in server secrets, never in the page), with instructor-reviewed content and logging. Phase 3: AI-generated practice questions with human review before they enter a test series.
