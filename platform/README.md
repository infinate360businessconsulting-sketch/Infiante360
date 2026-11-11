# Infinite360 learning API (starter)

Backend for the /lms experience: activation-code redemption, entitlement checks, Webinar.gg live-class join tokens (embedded classroom) and a grounded AI study assistant. The static website stays on GitHub Pages; this runs on a server you control.

Status: built and tested locally (typecheck + 5 tests with mocked Webinar.gg and AI calls). Not deployed. Not tested against the real Webinar.gg or AI APIs.

## Endpoints
- `POST /v1/admin/codes` (header `x-admin-key`): create activation codes `{plan, batch, count, expiresAt?}`
- `POST /v1/redeem` `{email, code}` -> session token (single-use code)
- `POST /v1/admin/sessions`: create a Webinar.gg webinar and map it to plan + batch
- `GET /v1/sessions`: classes for the signed-in learner's plans
- `POST /v1/sessions/:id/join-token`: checks enrolment and class window, returns a short-lived Webinar.gg token
- `POST /v1/assistant` `{question}`: answers only from `knowledge/*.md`, requires sign-in, rate-limited
- `public/classroom.html`: sign-in + embedded classroom (validates postMessage origin)

## Run
1. `cp .env.example .env` and fill secrets on the server (never commit). Set `ANTHROPIC_MODEL` to a model id that exists on your account.
2. `docker compose up -d` (Postgres + API) behind Nginx/Caddy with HTTPS, e.g. `api.infinate360.com`.
3. Set `PUBLIC_ORIGIN` to the site that calls the API (CORS).

## Open items before production
- Confirm Webinar.gg endpoints, plan limits and, critically, whether recordings can be exported (adapter `UnconfirmedRecordingProvider` returns nothing until confirmed).
- Rate limiting is in-memory: use Redis for more than one instance.
- Decide how this activation flow relates to the white-label platform's own activation keys (two systems of record is a risk; pick one).
- Add the trainer-approved course notes to `knowledge/`.
