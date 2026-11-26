"""Makes invite codes for the practice lab. Reads LAB_SECRET from the environment (never from a file, never printed).
Usage: LAB_SECRET=... python3 -I scripts/make_lab_invites.py emails.txt [days=14]
Writes lab-invites.csv (email, code, expires) and lab-invite-emails.md (drafts only). Nothing is sent. Keep the outputs out of Git."""
import csv, datetime as dt, hashlib, hmac, os, sys, time
secret = os.environ.get("LAB_SECRET")
if not secret or len(sys.argv) < 2: sys.exit("Set LAB_SECRET and pass a file with one email per line.")
days = int(sys.argv[2]) if len(sys.argv) > 2 else 14
exp_day = int(time.time() // 86400) + days
exp_date = (dt.date(1970, 1, 1) + dt.timedelta(days=exp_day)).isoformat()
rows = []
for line in open(sys.argv[1]):
    e = line.strip().lower()
    if "@" in e:
        sig = hmac.new(secret.encode(), f"invite|{e}|{exp_day}".encode(), hashlib.sha256).hexdigest()[:20]
        rows.append((e, f"{exp_day}.{sig}", exp_date))
with open("lab-invites.csv", "w", newline="") as f: csv.writer(f).writerows([("email", "code", "expires")] + rows)
with open("lab-invite-emails.md", "w") as f:
    for e, c, x in rows:
        f.write(f"To: {e}\nSubject: Your Infiante360 Practice Lab invite (free beta)\n\nHi,\n\nYou are invited to the Infiante360 Practice Lab, a free beta. The first lab is on identity and XDM.\n\n1. Open https://infiante360techacademy.com/lab/login\n2. Sign in with this email address and the invite code {c}\n3. The code works until {x}. Your progress is saved in the browser you use.\n\nThe lab is a learning simulation. Use made-up data only. No credential, job or exam result is promised, and Infiante360 is independent of Adobe.\n\nQuestions? WhatsApp +91 82968 93895.\n\nPavan Babu Gandla\nInfiante360 Tech Academy\n\n---\n\n")
print(len(rows), "invites written; expiry", exp_date)
