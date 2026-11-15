# Infiante360 LMS site (separate from the main academy site)

Static site. Edit `data.py` (ribbon, simulators, knowledge base), run `python3 build.py`, commit, push. Hosted on GitHub Pages from the repo root.

Live today: home, student login (links to the learning platform), simulators, searchable knowledge base, community page (WhatsApp), admin access page (no credentials held), notification ribbon, search-based assistant, image placeholders in `assets/images/`.

Not built (needs a server and database): in-site admin panel, student accounts, single sign-on, WhatsApp Business API notifications, threaded trainer community. Starter API: the `platform/` folder in the main academy repo.

Set `base_url` in `data.py` once the custom domain exists (enables sitemap and canonical URLs).
