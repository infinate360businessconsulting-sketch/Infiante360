# PROGRESS (checkpoint file; update after every batch)

Canonical site: https://infiante360techacademy.com/ (GitHub Pages, workflow `.github/workflows/pages.yml`). Build and validation run in CI only; `src/build.py` cannot be run in the agent session because of the privacy plugin.

## Done and verified in CI
- Workbook ingest to `data/seo/*` (12 datasets reconciled). Script: `scripts/seo_ingest.py`.
- CI health inventory (`scripts/seo_inventory.py`, `scripts/seo_report_print.py`). Run 45557767016: 249 pages, 0 long titles, 0 orphans, 0 sitemap gaps, 0 broken links.
  - The earlier "46 long titles / 19 missing sitemap pages" were measurement bugs (SVG title text counted as page title; the corporate section has its own sitemap). Fixed in the script, not by rewriting pages.
  - Real fixes: 3 corporate titles shortened, 2 corporate H1s made distinct, the site-verification file excluded as a utility page.
- `SITE_BASE` set in the workflow; live canonical host confirmed in Chrome.

## Done, awaiting CI confirmation
- 1,000-keyword mapping (`scripts/seo_keyword_map.py`): `keyword_url_mapping.json/.csv`, `content_gap_registry.json`, `page_generation_queue.json`, `keyword_coverage_report.json`, `docs/KEYWORD_COVERAGE_REPORT.md`.
- `tests/test_seo_data.py` (8 tests pass locally) wired into CI.

## Not started
Agent framework, new guide pages, image pipeline, social queue, AI-visibility registry, remaining docs, per-page content enhancement.

## Needs owner input
- Open gaps in `docs/KEYWORD_COVERAGE_REPORT.md`.
- Programme fees, schedules and durations (approved catalogue).
- Whether Adobe Commerce delivery is a real offering.
- Adobe partner-badge authorization: the supplied banners show partner wording; none is used until documented.
