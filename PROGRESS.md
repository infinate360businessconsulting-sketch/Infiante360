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
