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
