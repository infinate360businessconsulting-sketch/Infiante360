# Practice Lab Phase 1: setup and limits

Built: free beta, Lab 1 (identity and XDM), invite-only sign-in. Original scenario and text. Not the real Adobe product.

## Parts
- `labs-private/identity-xdm/index.html`: the lab (3 auto-checked missions, progress saved in the learner's browser).
- `api/lab-login.js`: checks email + invite code, sets a 12-hour HttpOnly cookie.
- `api/lab-app.js`: serves the lab only with a valid cookie (`/lab`), else redirects to `/lab/login`.
- `assets/lab-login.html`: the sign-in page (`/lab/login`, noindex).
- `api/_labauth.js`: stateless signed invite and session tokens. Test: `tests/test_lab_auth.py`.
- `scripts/make_lab_invites.py`: makes invite codes and draft emails locally.
- `vercel.json`: rewrites and `includeFiles` for the lab.

## Owner steps (nothing is sent automatically)
1. In Vercel project settings, add an environment variable `LAB_SECRET` (a long random value, never put it in Git or chat). Redeploy. Until it is set, sign-in answers "Labs are not open yet".
2. Put learners' emails in a text file, one per line. Run locally: `LAB_SECRET=... python3 -I scripts/make_lab_invites.py emails.txt 14`.
3. Open `lab-invite-emails.md`, edit if you like, and send each email yourself. The outputs are git-ignored.
4. Test with your own email first.

## Limits (be honest with learners)
- No passwords and no database: an invite code plus email signs in for 12 hours. Codes expire on the date in the email. Anyone with a code and the email can sign in; keep codes private. Revoking one learner early needs a new `LAB_SECRET` (which invalidates everyone).
- Progress is stored per browser, not per account.
- One lab only. No credentials, no payments, no leaderboards.
- Next phase needs accounts and a database (decision pending).
