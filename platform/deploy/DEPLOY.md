# Deploy on a Linux server (Hetzner or similar)

Placeholders: `SERVER_IP`, `api.infinate360.com`. Do not paste secrets into chat; type them on the server.

1. DNS: create an A record `api` -> `SERVER_IP`.
2. Server: install Docker, Docker Compose and Caddy; allow only ports 22, 80, 443 in the firewall; use SSH keys, not passwords.
3. `git clone` the repo, `cd infiante360/platform`.
4. `cp .env.example .env`, then edit on the server: `PUBLIC_ORIGIN`, `DATABASE_URL` (matches the compose Postgres password), `ADMIN_API_KEY` and `SESSION_SECRET` (random, 32+ chars: `openssl rand -hex 32`), `WEBINAR_GG_API_TOKEN` (a new token, after revoking the one shared in chat), `ANTHROPIC_API_KEY` and `ANTHROPIC_MODEL` (optional until the assistant goes live).
5. `export POSTGRES_PASSWORD=...` then `docker compose up -d --build`.
6. Copy `deploy/Caddyfile` to `/etc/caddy/Caddyfile`, `systemctl reload caddy`.
7. Smoke test: `curl https://api.infinate360.com/healthz` returns `{"ok":true}`.
8. Create a test code: `curl -X POST https://api.infinate360.com/v1/admin/codes -H "x-admin-key: $ADMIN_API_KEY" -H "content-type: application/json" -d '{"plan":"aep","batch":"test","count":1}'`, create one test webinar, join with a test learner.
9. Back up the Postgres volume daily; rotate keys if ever exposed.
