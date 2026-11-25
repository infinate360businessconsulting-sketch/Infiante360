# Marketing operating system (internal, not published)
Source: owner brief 2026-11-25 (nine core agents plus eleven proposed roles). Status: **plan only**; nothing here is deployed or running.

## Mapping to what exists
| Brief agent | Existing in repo | Gap |
|---|---|---|
| 01 Positioning, 09 Competitor monitor | `agents/registry.json` research specs | Evidence-cited reports, owner review |
| 02 Content strategist | `data/seo/page_generation_queue.json`, keyword maps | 300-article calendar (distinct angles only) |
| 03 Copywriter, 04 Repurposing | research engine (ADR-001), social queue spec | Approved drafts; no autonomous posting |
| 05 SEO/AEO, 12 Technical auditor | `scripts/seo_*.py`, validator, CI inventory | Search Console baselines (owner access) |
| 06 Distribution, 13 Community | community-tracks, events pages | Consent and channel rules |
| 07 Analyst, 19 CRM | none | GA4/GSC/CRM access from owner |
| 08 Lead magnets, 17 Nurture | none | Resource content, consent flow |
| 10, 11, 14-16, 18, 20 | partial | Defined, not built |

## Rules kept
- Editorial approval before publish; explicit owner go-ahead for external messages, deployments, paid campaigns.
- No fabricated results, reviews, certifications, volumes, rankings, jobs, speakers, dates or fees.
- 300 articles / 30 pillars / 705 images / 2,400 repurposed assets are **targets**, not commitments to publish. One page per distinct intent; near-duplicates stay out of the index.
- Jobs: official portal links only until a feed source's terms or API permit use.

## Needed from owner
SkillSurf production domain; registered legal entity details for legal pages; Search Console and GA4 access; permitted job-feed sources; event dates, speakers, fees.
