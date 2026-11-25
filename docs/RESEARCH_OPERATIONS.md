# Research operations runbook

Use this to add and publish a research piece. Design rationale: `docs/adr/ADR-001-research-publishing-engine.md`. Standards: `docs/EDITORIAL_STANDARDS.md`, `docs/SOURCE_VERIFICATION.md`.

## What exists today
- Topic registry: `data/research/topic_registry.json` (50 topics, each marked `exists`, `new`, `blocked_data` or `new_needs_sources`).
- Research module: `src/content_research.py` (hub page and one article).
- Diagram specs: `data/visuals/specs/*.json`, rendered by `scripts/visual_engine.py` and `scripts/image_pipeline.py`.
- Checks: `scripts/validate_research.py`, `python3 -I -m unittest discover -s tests`, and the CI build.
- LinkedIn draft files: `marketing/linkedin/research/` (status `pending_review`). Config in `marketing/config/`.

## What does not exist yet
Source registry, research RSS feeds, whitepaper export, scheduled research runs and a dashboard. Do not describe them as available.

## Add a research article
1. **Pick a topic** in the registry with status `new`. If status is `exists`, update that page instead. If `blocked_data`, stop.
2. **Collect sources** following `docs/SOURCE_VERIFICATION.md`. Record each URL and the date you opened it.
3. **Write the page** as a new entry in `src/content_research.py` using `art(...)`, then set `path` to `research/<slug>.html` and `category` to `"Guides"`. Include sections for research questions, analysis, architecture, security, limitations, recommendations, FAQs.
4. **Add a diagram spec** under `data/visuals/specs/<slug>.json`, then run:
   `python3 -I scripts/visual_engine.py build <slug>` and `python3 -I scripts/image_pipeline.py`
5. **Validate locally (safe commands only):**
   `python3 -I scripts/validate_research.py` and `python3 -I -m unittest discover -s tests`
6. **Update the registry**: set the topic's status and add the page URL. Keep `first_batch` accurate.
7. **Commit and push.** CI runs the build and validator. Read the result with `gh run view <id> --log`.
8. **Confirm live** by loading the URL in a browser. A passing CI run is not the same as a live page.

`src/build.py` cannot be run in the agent session. CI is the validator.

## Create LinkedIn drafts
1. Copy `marketing/linkedin/research/mcp-customer-data-platforms.md` as a template.
2. Use the tracked link pattern in `marketing/config/tracking.json`.
3. Leave status `pending_review`. The owner posts manually or with LinkedIn's own scheduler.
4. Do not write code that posts, comments, connects or messages. `publishing_permissions.json` forbids it and a test checks it.

## Rollback
Revert the commit and push. The next CI run redeploys the previous content. Do not edit the live site by hand.

## Escalation
Factual, legal, security or commercial claims need the owner's review before merge.
