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
