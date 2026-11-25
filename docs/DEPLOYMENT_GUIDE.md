# Deployment guide

Production: GitHub Pages, deployed by `.github/workflows/pages.yml` on every push to `main`. Custom domain via `CNAME` (infiante360techacademy.com). DNS and domain settings are not changed by this workflow.

## Release steps
1. Make changes on a branch or `main` in small commits.
2. Local checks: `python3 -I -m unittest discover -s tests`.
3. Push. CI runs dataset tests, build with validation (fails on broken links, duplicate titles/descriptions/H1, invalid JSON-LD), SEO inventory, agent pipeline, LMS copy, then deploys.
4. Read the run: `gh run view <id> --log`. Confirm success and the SEO health counts.
5. Verify the live site (homepage canonical, a changed page, `sitemap.xml`, `robots.txt`). Do not report "live" until that is done.

## Not automated
Search Console and Bing sitemap submission, DNS, payment settings, social posting, and anything needing credentials.
