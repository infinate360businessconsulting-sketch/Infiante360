# Source verification

## Allowed sources
Vendor documentation (Adobe Experience League, Snowflake, Databricks, Google Cloud, AWS, Microsoft Learn), Apache projects, the Model Context Protocol site, standards bodies (NIST, OWASP), peer-reviewed papers, government statistics, and your own labelled tests.

## Not allowed
Scraped or paywalled reports, copied articles, forum posts as proof, unattributed statistics, and any source you have not opened.

## Procedure for each source
1. Open the page. Note the exact URL, title, publisher and the date you opened it.
2. Find the sentence that supports the claim. Paraphrase it. Do not paste more than a short phrase.
3. Check the product version or edition the page applies to.
4. Record it (until `data/research/source_registry.json` exists, keep this in the commit message or the draft's notes).
5. If a claim has no source, delete it or rewrite it as an opinion or a question.

## Link checks
- Use only URLs you have opened. Documentation sites move pages; prefer top-level documentation links when a deep link is uncertain.
- CI checks internal links only. External links need a manual check before release and again every quarter.

## Pricing and vendor comparisons
Quote published prices only with date, edition and region. Say plainly when information is unavailable. Do not infer a competitor's weakness.

## Job-market data
Use only the authorised Infinate360Explorer dataset. State methodology, sample size, coverage limits and freshness, and never present the sample as the whole market. Never publish resumes or personal data.
