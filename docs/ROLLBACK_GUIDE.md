# Rollback guide

The site is static, so rollback is a redeploy of an earlier commit.

1. Find the last good commit: `git log --oneline` and the CI run that deployed it.
2. Revert: `git revert <bad-commit>` (preferred, keeps history) and push to `main`. CI rebuilds and redeploys.
3. Or re-run the deploy workflow for the last good commit from the Actions tab.
4. Verify the live homepage, the affected pages and `sitemap.xml`.

Known good checkpoints (all passed CI): `4ab2c8c` (SEO health fixes), `8551469` (keyword mapping and tests).
Rolling back never changes DNS or the domain. A broken build fails CI before anything is deployed.
