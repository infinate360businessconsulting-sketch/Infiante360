#!/usr/bin/env python3
"""Agent orchestrator: registry, ledger, resource locks, emergency stop, approval gate.

Usage:
  python3 agents/orchestrator.py list
  python3 agents/orchestrator.py run <agent_id> [--built DIR]
  python3 agents/orchestrator.py pipeline [--built DIR]
  python3 agents/orchestrator.py stop | resume | status

Rules enforced here (not just described):
  * `data/agents/STOP` present  -> every run is refused (global emergency stop).
  * One writer per output resource (lock file); a competing run is refused, never queued silently.
  * Agents that are not implemented, or need credentials, record BLOCKED in the ledger. They never fabricate output.
  * No agent deploys, posts, sends or creates accounts. The publishing agent only checks approvals.
Override the data directory with AGENT_DATA_DIR (used by tests).
"""
import collections, datetime, glob, json, os, re, subprocess, sys, uuid

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.environ.get("AGENT_DATA_DIR") or os.path.join(ROOT, "data", "agents")
SEO = os.path.join(ROOT, "data", "seo")
REG = json.load(open(os.path.join(ROOT, "agents", "registry.json"), encoding="utf-8"))["agents"]
BY_ID = {a["id"]: a for a in REG}
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
J = lambda p: json.load(open(p, encoding="utf-8"))


def paths():
    for sub in ("out", "locks"):
        os.makedirs(os.path.join(DATA, sub), exist_ok=True)
    return os.path.join(DATA, "ledger.jsonl"), os.path.join(DATA, "STOP"), os.path.join(DATA, "approvals.json")


def ledger(rec):
    lp, _, _ = paths()
    with open(lp, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


class Locked(Exception):
    pass


class lock:
    def __init__(self, name):
        self.p = os.path.join(DATA, "locks", name + ".lock")

    def __enter__(self):
        paths()
        try:
            self.fd = os.open(self.p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            raise Locked(self.p)
        return self

    def __exit__(self, *a):
        os.close(self.fd); os.unlink(self.p)


def write_out(agent, obj):
    p = os.path.join(DATA, "out", agent + ".json")
    with lock("out-" + agent):
        json.dump(obj, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    return os.path.relpath(p, ROOT) if p.startswith(ROOT) else p


# ---------------------------------------------------------------- implemented agents
def website_inventory(a):
    r = J(os.path.join(SEO, "route_snapshot.json"))
    sec = collections.Counter((x["route"].strip("/").split("/")[0] or "home") for x in r["routes"])
    return {"source": r["source"], "routes": r["count"], "indexable": sum(1 for x in r["routes"] if x["indexable"]), "by_section": dict(sec)}


def keyword_intelligence(a):
    r = J(os.path.join(SEO, "reconciliation.json"))
    return {"all_counts_reconciled": r["all_counts_reconciled"], "datasets": {k: [v["imported"], v["expected"]] for k, v in r["datasets"].items()}, "problems": r["problems"]}


def search_intent(a):
    out = collections.defaultdict(collections.Counter)
    for k in J(os.path.join(SEO, "keywords.json")):
        out[k["cluster"]][k["intent"]] += 1
    return {"clusters": len(out), "intent_by_cluster": {c: dict(v) for c, v in out.items()}}


def url_mapping(a):
    p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "seo_keyword_map.py")], capture_output=True, text=True, timeout=120)
    if p.returncode: raise RuntimeError(p.stderr[-400:])
    return json.loads(p.stdout.strip().splitlines()[-1])


def content_gap(a):
    g = J(os.path.join(SEO, "content_gap_registry.json"))["gaps"]; q = J(os.path.join(SEO, "page_generation_queue.json"))["queue"]
    return {"gaps": len(g), "queued_items": len(q), "queue_generated": sum(1 for x in q if x["generated"]), "needs_owner_input": [x["cluster"] for x in g if x.get("needs_owner_input")]}


def internal_linking(a):
    rs = J(os.path.join(SEO, "route_snapshot.json"))["routes"]
    low = sorted((x["inbound"], x["route"]) for x in rs if x["indexable"] and x["inbound"] < 6)
    return {"threshold": 6, "pages_below_threshold": len(low), "lowest": low[:25]}


def content_quality(a):
    rs = J(os.path.join(SEO, "route_snapshot.json"))["routes"]
    thin = sorted((x["words"], x["route"]) for x in rs if x["indexable"] and x["words"] < 250)
    return {"thin_threshold_words": 250, "thin_pages": thin}


def brand_authority(a):
    t = J(os.path.join(SEO, "authority_50.json"))
    key = next((k for k in t[0] if "status" in k), None)
    return {"targets": len(t), "status_field": key, "status_counts": dict(collections.Counter(str(x.get(key)) for x in t)) if key else None}


def _need_built(a):
    b = a.get("built")
    if not b or not os.path.isdir(b): raise Blocked("needs --built DIR (a built site directory); none given")
    return b


class Blocked(Exception):
    pass


def technical_seo(a):
    b = _need_built(a); out = os.path.join(DATA, "out", "seo_report")
    p = subprocess.run([sys.executable, "-I", os.path.join(ROOT, "scripts", "seo_inventory.py"), b, out], capture_output=True, text=True, timeout=300)
    if p.returncode: raise RuntimeError(p.stderr[-400:])
    h = J(os.path.join(out, "seo-health.json"))
    return {k: (len(v) if isinstance(v, (list, dict)) else v) for k, v in h.items() if k not in ("robots_txt",)}


def structured_data(a):
    b = _need_built(a); bad, types = [], collections.Counter()
    for f in glob.glob(os.path.join(b, "**", "*.html"), recursive=True):
        for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', open(f, encoding="utf-8", errors="ignore").read(), re.S):
            try:
                j = json.loads(blk)
                for n in (j if isinstance(j, list) else j.get("@graph", [j])):
                    t = n.get("@type"); types.update(t if isinstance(t, list) else [t])
            except Exception:
                bad.append(os.path.relpath(f, b))
    return {"invalid_blocks_in": bad, "types": dict(types)}


MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def content_freshness(a):
    b = _need_built(a); today = datetime.date.today(); hits = []
    pat = re.compile(r"\b(\d{1,2})(?:\s*[-–]\s*\d{1,2})?\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?,?\s+(20\d\d)\b")
    for f in glob.glob(os.path.join(b, "**", "*.html"), recursive=True):
        txt = re.sub(r"<[^>]+>", " ", open(f, encoding="utf-8", errors="ignore").read())
        for d, m, y in pat.findall(txt):
            try: dt = datetime.date(int(y), MONTHS.index(m) + 1, int(d))
            except ValueError: continue
            if dt < today: hits.append((os.path.relpath(f, b), f"{d} {m} {y}"))
    by = collections.defaultdict(set)
    for f, d in hits: by[f].add(d)
    return {"as_of": today.isoformat(), "pages_with_past_dates": len(by), "note": "Past dates may be legitimate history; review before changing", "pages": {k: sorted(v) for k, v in sorted(by.items())[:60]}}


SECRET = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|xox[baprs]-[A-Za-z0-9-]{10,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|AIza[0-9A-Za-z_-]{35})")
PRIVATE_EXT = (".zip", ".pem", ".key", ".p12", ".env", ".sqlite", ".db")


def security_privacy(a):
    files = subprocess.run(["git", "-C", ROOT, "ls-files"], capture_output=True, text=True).stdout.split("\n")
    secrets, private = [], []
    for f in filter(None, files):
        if f.lower().endswith(PRIVATE_EXT) or os.path.basename(f).startswith(".env"): private.append(f)
        p = os.path.join(ROOT, f)
        if os.path.isfile(p) and os.path.getsize(p) < 2_000_000 and not f.lower().endswith((".png", ".jpg", ".jpeg", ".webp", ".ico", ".xlsx", ".pdf")):
            m = SECRET.search(open(p, encoding="utf-8", errors="ignore").read())
            if m: secrets.append({"file": f, "pattern": SECRET.pattern[:12] + "..."})  # never echo the match
    return {"files_scanned": len([f for f in files if f]), "secret_pattern_hits": secrets, "private_file_types_tracked": private}


def qa_regression(a):
    p = subprocess.run([sys.executable, "-I", "-m", "unittest", "discover", "-s", os.path.join(ROOT, "tests")], capture_output=True, text=True, timeout=300)
    tail = (p.stderr or p.stdout).strip().splitlines()[-3:]
    if p.returncode: raise RuntimeError(" | ".join(tail))
    return {"passed": True, "summary": tail}


def publishing(a):
    _, _, ap = paths()
    items = J(ap) if os.path.exists(ap) else []
    approved = [i for i in items if i.get("status") == "approved"]
    return {"deploys": False, "note": "Gate check only. Deployment goes through the reviewed GitHub Actions workflow after the owner approves.",
            "approval_records": len(items), "approved": len(approved), "pending": len(items) - len(approved)}


IMPL = {n: f for n, f in globals().items() if n in BY_ID and callable(f)}


def run_agent(agent_id, args=None, retry=0):
    args = args or {}
    lp, stop, _ = paths()
    a = BY_ID.get(agent_id)
    rec = {"task_id": uuid.uuid4().hex[:10], "agent": agent_id, "started": now(), "inputs": args, "retry": retry, "cost_usd": 0.0, "review": "not_required"}
    if os.path.exists(stop):
        rec.update(status="REFUSED_EMERGENCY_STOP", finished=now()); ledger(rec); return rec
    if not a:
        rec.update(status="FAILED", error="unknown agent", finished=now()); ledger(rec); return rec
    fn = IMPL.get(agent_id)
    if not a["implemented"] or fn is None:
        why = "needs credentials/authorised provider" if a["status"] == "blocked_needs_credentials" else "specification only; not implemented"
        rec.update(status="BLOCKED", error=why, output=None, finished=now()); ledger(rec); return rec
    try:
        res = fn(args)
        rec.update(status="OK", output_file=write_out(agent_id, res), summary=res, finished=now())
    except Blocked as e:
        rec.update(status="BLOCKED", error=str(e), finished=now())
    except Locked as e:
        rec.update(status="REFUSED_RESOURCE_LOCKED", error=str(e), finished=now())
    except Exception as e:
        if retry < a["retry_limit"]:
            return run_agent(agent_id, args, retry + 1)
        rec.update(status="FAILED", error=str(e)[:400], finished=now())
    ledger(rec)
    return rec


PIPELINE = ["website_inventory", "keyword_intelligence", "search_intent", "url_mapping", "content_gap", "internal_linking", "content_quality",
            "brand_authority", "technical_seo", "structured_data", "content_freshness", "security_privacy", "qa_regression", "publishing"]


def pipeline(args):
    results = []
    for aid in PIPELINE:
        r = run_agent(aid, args); results.append({"agent": aid, "status": r["status"], "error": r.get("error")})
        if r["status"] == "REFUSED_EMERGENCY_STOP": break
    return results


IMPL["growth_orchestrator"] = pipeline


def main(argv):
    cmd = argv[1] if len(argv) > 1 else "list"
    args = {}
    if "--built" in argv: args["built"] = argv[argv.index("--built") + 1]
    _, stop, _ = paths()
    if cmd == "list":
        for a in REG: print(f"{a['status']:26} {a['id']:26} {a['summary']}")
    elif cmd == "run":
        print(json.dumps(run_agent(argv[2], args), indent=1)[:3000])
    elif cmd == "pipeline":
        for r in pipeline(args): print(r)
    elif cmd == "stop":
        open(stop, "w").write(now()); print("STOP set")
    elif cmd == "resume":
        if os.path.exists(stop): os.unlink(stop)
        print("STOP cleared")
    elif cmd == "status":
        lp = paths()[0]
        rows = [json.loads(l) for l in open(lp)] if os.path.exists(lp) else []
        print(json.dumps({"stopped": os.path.exists(stop), "runs": len(rows), "by_status": dict(collections.Counter(r["status"] for r in rows))}))
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
