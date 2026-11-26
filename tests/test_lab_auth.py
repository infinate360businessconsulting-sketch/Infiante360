import json, os, subprocess, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JS = """
const a=require('./api/_labauth');const s='unit-test-secret',n=Date.parse('2026-12-01T00:00:00Z');
const day=Math.floor(n/86400000)+5;const c=a.makeInvite(s,'A@x.com',day);
const t=a.makeSession(s,'A@x.com',n,12);
console.log(JSON.stringify({ok:a.checkInvite(s,'a@x.com',c,n),wrongEmail:a.checkInvite(s,'b@x.com',c,n),wrongSecret:a.checkInvite('other','a@x.com',c,n),
expired:a.checkInvite(s,'a@x.com',c,n+9*86400000),sess:a.checkSession(s,t,n+1000),sessExp:a.checkSession(s,t,n+13*3600000),sessBad:a.checkSession(s,t+'x',n),noSecret:a.checkInvite('', 'a@x.com',c,n)}));
"""
class LabAuth(unittest.TestCase):
    def test_tokens(self):
        r = json.loads(subprocess.run(["node", "-e", JS], cwd=ROOT, capture_output=True, text=True, check=True).stdout)
        self.assertTrue(r["ok"]); self.assertEqual(r["sess"], "a@x.com")
        for k in ("wrongEmail", "wrongSecret", "expired", "sessExp", "sessBad", "noSecret"): self.assertFalse(r[k], k)
if __name__ == "__main__": unittest.main()
