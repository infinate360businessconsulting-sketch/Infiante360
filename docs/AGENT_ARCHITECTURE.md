# Agent architecture

Application-level workflows, not claims about native Adobe or vendor capabilities.

## Components
- `agents/registry.json`: 40 agent specs. Each has input/output contract, allowed tools, permissions, trigger, retry limit, cost budget, evidence, validation, human-approval policy and failure recovery.
- `agents/orchestrator.py`: runs agents, writes `data/agents/ledger.jsonl`, holds per-output lock files, honours the emergency stop, never deploys.

## Status (from the registry)
- Implemented, deterministic (15): website inventory, keyword intelligence, search intent, URL mapping, content gap, internal linking, content quality, brand authority, technical SEO, structured data, content freshness, security and privacy, QA and regression, publishing (gate check only), growth orchestrator.
- Blocked until credentials or an authorised provider exist (7): SERP research, competitor intelligence, video/transcripts, AI visibility testing, analytics, conversion optimisation, image generation.
- Specification only (18): AI-drafting agents (content, GEO/AEO, fact-checking, social, creative direction, prompts) and the image/diagram/branding/QA tooling. Running one records `BLOCKED` in the ledger; it never produces made-up output.

## Guarantees enforced in code (see `tests/test_agents.py`)
1. `data/agents/STOP` makes every run `REFUSED_EMERGENCY_STOP`.
2. One writer per output; a competing run is `REFUSED_RESOURCE_LOCKED`.
3. Unimplemented or credential-dependent agents are `BLOCKED`, with no output.
4. The publishing agent reports approvals and `deploys: false`.
5. Agents that need a built site report `BLOCKED` when none is supplied, instead of guessing.

## Workflow
Source ingestion, keyword mapping, gap analysis, then (not yet automated) brief, draft, image, fact-check, SEO/GEO/AEO validation, human approval, CI validation, authorised deployment, monitoring. Only the first stages are automated today.

## Run
`python3 agents/orchestrator.py list | run <id> [--built DIR] | pipeline [--built DIR] | stop | resume | status`
