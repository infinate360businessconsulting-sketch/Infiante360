# PROGRESS (checkpoint file; update after every batch)

Canonical site: https://infiante360techacademy.com/ (GitHub Pages, workflow `.github/workflows/pages.yml`). Build and validation run in CI only; `src/build.py` cannot be run in the agent session because of the privacy plugin.

## Done and verified in CI
- Workbook ingest to `data/seo/*` (12 datasets reconciled). `scripts/seo_ingest.py`.
- CI health inventory (`scripts/seo_inventory.py`, `scripts/seo_report_print.py`). Run 45557767016: 249 pages, 0 long titles, 0 orphans, 0 sitemap gaps, 0 missing H1/description/canonical, 0 broken links.
  - The earlier "46 long titles / 19 missing sitemap pages" were measurement bugs (SVG title text; the corporate section has its own sitemap). Fixed in the script, not by rewriting pages.
  - Real fixes: 3 corporate titles shortened, 2 corporate H1s made distinct, site-verification file excluded as a utility page.
- `SITE_BASE` set in the workflow; live canonical host confirmed in Chrome.
- 1,000-keyword mapping (`scripts/seo_keyword_map.py`), gap registry, generation queue, coverage report. Run 45558101783 passed.
- Agent framework: 40-agent registry, orchestrator, 15 working deterministic agents, 18 unit tests. Run 45558298932 passed: tests 18/18, pipeline 14/14 OK, JSON-LD all valid, no secret-pattern hits.

## Findings needing owner action
- Past-dated promotional content (as of 2026-11-25): `lp/martech-sme-accelerator`, `lp/enterprise-martech-demo`, `lp/martech-demo-bootcamp`, `academy/community`. Needs the next batch dates before copy is changed. No dates have been invented.
- `platform/.env.example` is tracked; confirm it holds placeholders only (the scan found no key patterns).

## Not started
New guide pages (5 queued service pages await approval; Adobe Commerce blocked on confirmation), image pipeline, social queue (90 posts), AI-visibility registry (100 queries, none tested), per-page content enhancement, admin dashboard, remaining docs.

## Needs owner input
- Open gaps in `docs/KEYWORD_COVERAGE_REPORT.md`; programme fees, schedules and durations (approved catalogue).
- Whether Adobe Commerce delivery is a real offering.
- Adobe partner-badge authorization: the supplied banners show partner wording; none is used until documented.

## 2026-11-25 batch (CI run for af98f2b: success; 231 pages built, 230 sitemap URLs, 0 orphans, 24 tests)
- Done: evergreen cohort config (CI-verified); Google verification tags served (served, NOT verified until Search Console confirms).
- Done: image engine (scripts/visual_engine.py, scripts/image_pipeline.py): deterministic SVG + Pillow, approved logo composited, WebP/PNG, manifests in data/seo/image_*.json. No generative model available here (no GPU, model hosts unreachable); vendor logos not embedded (no official files or permission on record).
- Done: five consulting pages (Snowflake, BigQuery, Databricks, Kafka, enterprise architecture) with per-page og:image and Service schema; queue PG-001..005 marked generated. Adobe Commerce stays pending_confirmation (data/seo/service_registry.json).
- Drafted, not sent/submitted: RSS submission kit (data/distribution/), press release draft (docs/PRESS_RELEASE_DRAFT.md), white-label footer link fixes (docs/WHITE_LABEL_FOOTER_LINKS.md).
- Remaining: 365 articles / 50 pillars / 30 landing intentions / 26 use cases in controlled batches; child sitemaps; 100 AI-discovery questions; AI-visibility registry (Not tested); 90-day social queue; admin dashboard; more agents; replace entdemo placeholder visuals; owner items (partner documentation, dates, fees, legal address, SPF/DKIM/DMARC).

## 2026-11-25 article batch 1
- 20 articles (A-001..A-020) from the 365-idea plan (ids 351-365, 21, 22, 235, 246, 243): src/content_articles.py, content_articles2.py, queue in data/seo/article_queue.json (345 still queued, none generated).
- Child sitemaps (sitemaps/<category>.xml, images.xml) and sitemap-index.xml added; sitemap.xml remains the complete list. robots.txt lists the index. Submission to Search Console is the owner's step.
- Article hero images not yet generated (pipeline supports it; next batch).

## 2026-11-25 batch 2
- Article diagrams: 20 specs (scripts/make_article_specs.py) -> SVG/WebP/OG via visual_engine + image_pipeline (25 images total, quality gate 0 failures); each article now has its own og:image and an inline diagram.
- data/seo/pillar_decisions.json: all 50 pillars map to an existing hub (no new pillar pages; decision per pillar recorded).
- data/seo/ai_visibility_registry.json/.csv: 100 neutral queries mapped to target URLs, every result "Not tested" (no fabricated results).

## 2026-11-25 research engine (phase 1)
- data/research/topic_registry.json: 50 topics checked against existing pages (26 exist, 21 new candidates, 2 blocked on data, 1 needs sources).
- /research/ hub + first research article (MCP and CDPs) with diagram; scripts/validate_research.py + tests (33 pass).
- docs/adr/ADR-001 (approval-gated pipeline; proposed), RESEARCH_OPERATIONS, EDITORIAL_STANDARDS, SOURCE_VERIFICATION.
- marketing/config/* and one LinkedIn draft set (pending_review; auto-publish/comment/connect/message all false, tested).
- NOT built: 25 research agents (only deterministic checks exist), source registry, research RSS, whitepapers, dashboard, scheduled runs, daily LinkedIn routines. Need owner decisions in ADR-001.

## 2026-11-25 demo video + banner slider
- Created: assets/media/infinate360-demo.mp4 (+poster), src/banners.py, content/banners.json (empty), assets/banners/, tests/test_banners.py
- Updated: src/content_home.py (Watch the demo section; slider only if approved banners), assets/site.css, assets/site.js
- Banners NOT published: supplied banners carry unverified claims (Adobe Solution Partner badge, learner counts, placement, salary, lifetime access). Add with approved=true after owner review.
- 8 banners published in slider (content/banners.json). Held back: CJA (invented dashboard figures), Agentic dark (third-party logos), 'certification'/'Get Certified'/'Industry Certification' banners, 'Download Syllabus/Curriculum' banners, 'Career/Interview/Talent support' banners, duplicates.

## 2026-11-25 use-case library
- Created: data/usecases/martech_use_cases.csv (4000 rows, owner-supplied, all 'Illustrative design pattern'), src/content_usecase_library.py (hub + 40 industry pages at use-cases/library/), tests/test_usecase_library.py
- Updated: banners slider prefix, content_growth.py hub link, content_kb.py, build.py (sitemap2.xml = all use-cases/ URLs; in sitemap-index + robots)
- Decision: 4000 rows published as 40 industry pages x 100 patterns, NOT 4000 pages (rows repeat across industries: 1686 distinct patterns; per-row pages would be near-duplicates, CLAUDE.md rule).
- Not used: 50,000-keyword sitemap/CSV in the website zips (mass keyword pages); Trustpilot quotes about another company (OAD Solutions) in career-accelerator HTML; Unsplash stock images.

## 2026-11-25 extra pages (sitemap3)
- Created: src/content_extra.py (2 academy pages, flagged sitemap3), data/seo/extra_pages_register.json (disposition of every supplied file), data/distribution/rss_source_candidates.csv (unvalidated), tests/test_extra_pages.py
- Updated: build.py (sitemap3.xml + robots), content_kb.py, content_industry.py (inbound links)
- Not published: duplicate about/contact pages, standalone package site, other company's Trustpilot reviews, 50k keyword files, apps/agents (not run). See register.

## 2026-11-25 top-of-page rolling slider
- Created: assets/banners/research-ai-agent-orchestration.webp (9th banner, "TM" mark only)
- Updated: src/banners.py (select() matches banner `topics` to page path/title/category/keywords, skips self-link, fallback fill to 3; top_slider()), content/banners.json (topics, fallback), build.py (top_slider first in <main>), assets/site.css, assets/site.js (5s auto-roll, pause button, swipe, arrow keys, pauses off-screen/hidden tab, none under reduced-motion), tests
- Removed in-body sliders from home, use-case library and extra pages (now one slider per page, at top). No slider on lp/, corporate/, 404, legal pages.
- Held: new "Explore Courses" banner (Industry Certification + Adobe logo), 5 research banners carrying the registered-trademark symbol (no registration documented), research banner with "RDSEARCH" typo, text-free globe, plus earlier 12 held.

## 2026-11-25 community and events (from 2027 strategy docs)
- Phone: +91 82968 93895 / wa.me/918296893895 confirmed as the only number in src, lms-site, assets (no change needed).
- Created: academy/community-tracks.html (10 Adobe/MarTech/AI topic tracks), academy/event-calendar.html (3 proposed weekly slots, 10 event concepts, none scheduled); both in sitemap3.xml, in content_extra.py
- Updated: content_cases.py (inbound links from academy/community.html), extra_pages_register.json, tests
- Not published: SkillSurf 500-course catalog, Startup Studio, Explorer, other-brand communities/events, LinkedIn member counts (unverified, overlapping). Needs owner: legal entity/domain per brand.

## 2026-11-25 ecosystem + locations (sitemap4.xml)
- Owner said "yes add more pages as my company names ... localities ... sitemap4.xml". Legal entities/domains still unconfirmed, so brand pages claim no structure, offices, counts, dates or fees.
- Created: src/content_group.py (24 pages: ecosystem hub, SkillSurf, Infinate360Explorer, Startup Studio, CXO Hive; locations hub, 17 countries, Bengaluru), data/seo/sitemap4_keyword_map.csv (page -> keywords), tests/test_group_pages.py
- Updated: build.py (sitemap4.xml in index + robots; footer links to ecosystem/ and locations/), content_kb.py, extra_pages_register.json
- Country pages: real law + regulator + channel rule + design note per country, guidance not legal advice, no local office claimed. Sources are regulator home pages (not link-checked from CI).
- Deferred: jobs RSS/newsroom/PR engines (need sources/approvals), city pages (thin duplicates).

## 2026-11-25 products + events (sitemap4.xml)
- Owner: "create my company website as separate products ... go-ahead ... build it, make it live, create multiple events" (+ MarTechJobs-style Explorer spec). Legal entity/domain per brand still unconfirmed, so "being confirmed" wording stays.
- Created: src/content_products.py (16 pages: products hub; Explorer jobs-by-technology, jobs-by-role, resume scanner, employers, course-to-role map; CXO Hive programme; events hub + 8 proposed events across the 4 products), tests/test_product_pages.py; 16 rows in data/seo/sitemap4_keyword_map.csv
- Updated: content_group.py (hub rows, inbound links), content_kb.py, build.py (footer links to products/ and events/)
- Events: all "date to be announced", no fees, speakers, counts. Startup events: no funding/investor promise.
- Not built/claimed: live jobs feed (needs owner-named sources with checked terms), resume upload/scanner, employer portal, salary data, CXO fees (Rs 1,00,000 vs 1,50,000 conflict unresolved), Salesforce/Braze courses.

## 2026-11-25 jobs, event categories, 180-day plan, marketing OS
- Owner prompts: remove "being confirmed" from marketing pages (done in content_group.py/content_products.py; no legal-entity claims made); job portal only via permitted sources; events platform; master execution.
- Created: jobs/index.html (7 official portal links, no scraped listings), events/categories.html (20 categories), events/180-day-calendar.html (relative months, no dates), docs/MARKETING_OS.md; 3 keyword rows.
- Not done: 300 articles/30 pillars (backlog, distinct angles only), live job feed, event registration/payment/attendance (needs backend), SkillSurf domain, legal pages' entity details, analytics access.

## 2026-11-25 SEO/AEO/GEO + video-sitemap brief
- Already in place (reused, not regenerated): robots.txt with AI search bots separated from AI training bots, llms.txt + llms-full.txt + answers.json, sitemap-index + category sitemaps (events/ in sitemaps/training.xml) + images.xml, RSS feeds, JSON-LD validation in CI.
- Created: src/videos.py (video sitemap + VideoObject generator from content/videos.json), content/videos.json (empty), tests/test_videos.py. build.py writes sitemaps/videos.xml only when a video is approved + transcribed.
- Not registered: infinate360-demo.mp4 / promo.mp4 (10 s, silent, same footage, garbled on-screen text, no transcript): decorative, not educational; fake video watch pages would be thin.
- Not done: 300 articles/30 pillars/705 images/one-minute videos (backlog), IndexNow key + submissions and Search Console/Bing submission (owner accounts), AI-citation benchmark of 100 questions (needs permitted sampling, owner go-ahead), admin dashboard, feed.json.

## 2026-11-25 approval-to-proceed: batch 1 of the article programme + IndexNow + benchmark
- Owner approved content/images/videos/IndexNow/benchmark/dashboard. Done this session:
  - Guide batch 1 (10 distinct guides, XDM, sandboxes, audience evaluation, destinations, governance, CJA vs AA, Web SDK datastreams, MCP vs REST, AI coworker scope, Customer 360 layers): src/content_batch1.py, scripts/make_batch1_specs.py, 10 specs + 40 image files (deterministic SVG -> WebP/PNG via visual_engine + image_pipeline), tests/test_batch1.py. Images auto-listed in image sitemap (og_image).
  - IndexNow: indexnow/<key>.txt (public token), scripts/indexnow.py (dry run by default), pages.yml copies key to site root and runs a best-effort post-deploy submit of URLs with lastmod in the last 2 days.
  - AI citation benchmark: 100 questions in data/seo/ai_citation_benchmark.csv (results EMPTY), docs/AI_CITATION_BENCHMARK.md manual workflow.
- Blocked: voiceover (Piper installs but voice models cannot be downloaded: huggingface/github blocked from this workspace; no TTS engine present) => no narrated videos, no video-sitemap entries; admin dashboard (not started; admin/ is the CMS config); Search Console/Bing need owner accounts.
- Remaining article programme: 290 articles + 30 pillars + ~695 images, in batches of 25 (this batch: 10).
- Fix: live domain is served by Vercel (vercel.json, build output only), not GitHub Pages; key file copy moved into build.py so both hosts serve it. IndexNow submit step runs after the GitHub Pages deploy only, so confirm the key URL serves before relying on it. An admin/dashboard.html already exists in build.py (dashboard_html()).

## Identity update (legal name)
- Legal name PAVAN BABU GANDLA; brand "Infiante360 Business Consulting & Tech Academy"; email + phone (+91 82968 93895) shown in footer (mailto/tel links), privacy, about, contact, FAQ, corporate training, services and legal pages; corporate/, lms-site/ and email templates updated.
- Second number +91 9490164044 only in Organization JSON-LD (not visible). Structured data normally should match visible content - review.
- Open: payment/billing and refund terms not supplied (no policy invented); no checkout pages exist; SEO section of the brief not received.

## Course catalogue (2026-11-26)
- `data/catalogue/catalogue.json`: owner's 15 categories / 150 topics from the TrainerCentral brief. All draft except 11 mapped to existing live pages.
- `src/content_catalogue.py` renders `academy/catalogue.html`: names only published courses (Know more links), counts the rest as "in planning". Linked from links.html.
- Open: SAP, Guidewire, Microsoft, IBM, cybersecurity, software courses need curriculum, instructor, fee, schedule before any page. Banners for them not made. TrainerCentral email not sent (recipient not given). Not built locally (CI validates).

## Batches landing (2026-11-26)
- `lp/batches.html` from `src/content_batches.py` (reuses `landing()`); linked from links.html. No dates or fees stated (none confirmed).
- Lead routing doc: `docs/growth/batch-lead-routing.md`. Open: confirm `LEAD_WEBHOOK_URL` is set on Vercel and which CRM; supply next batch dates and fees.

## Social calendar (2026-11-26)
- `data/social/calendar-100.csv` (100 posts, 27 Nov 2026 to 24 Jan 2027), `scripts/build_social_calendar.py`, `docs/growth/social-calendar-guide.md`, 20 banner PNGs in `assets/social/` (new, deploy with the site). Nothing posted. Open: confirm upload tool timezone, owner review before upload, specific YouTube video URLs, batch dates.
- YouTube titles and descriptions for all 100 calendar posts: `data/social/youtube-descriptions-100.csv` (+ script). Chapters to be added after recording.

## Practice hub (2026-11-26)
- Owner shared another company's site (AdsBot) as reference. Not copied. Built an original `academy/practice.html` (src/content_practice.py) that links only existing resources: simulators, lab guides, quiz, handout, interview questions, LMS test series. No sandbox, badge or graded-mission claims. Linked from links.html.
- Not built: private per-learner sandboxes, auto-checked missions, verifiable credentials, MCP lab access. These need product work; scope and owner decision pending.

## Practice labs (2026-11-26)
- Owner wants paid labs. Not built. Added waitlist `lp/labs.html` (src/content_labs.py) and `docs/labs/LABS_PRODUCT_SCOPE.md`. No price, no checkout, no feature claims. Open: Phase 1 topic, delivery model, price, refund terms, payment path.
