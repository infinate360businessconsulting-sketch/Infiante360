# Known limitations (honest status)

- `src/build.py` cannot be run in the agent session (privacy plugin). CI is the only validator there; local runs need the owner.
- Keyword volume, difficulty, rankings and competitor data are unmeasured. The mapping is rule-based from cluster decisions and real routes, not SERP research.
- Per-page content quality, GEO and AEO status are "not assessed". Only structural SEO is measured.
- 5 planned service pages (Snowflake, BigQuery, Databricks, Kafka, enterprise architecture) and the Adobe Commerce cluster await owner confirmation; nothing is generated.
- The 365 articles, 50 pillars and 30 landing-page intentions are ingested as data, not written. Writing them well needs sourced, reviewed content; mass generation would create thin duplicates.
- No image-generation provider is configured; no images were generated or branded.
- AI-visibility testing, Search Console, GA4, SERP and competitor agents need authorised access; none is connected.
- The live site's pages were confirmed by CI results and one homepage check in Chrome, not a full crawl of the live domain (direct fetches from the agent session are blocked).
- Programme fees, schedules, durations and any Adobe partner status are unverified against an approved catalogue.
