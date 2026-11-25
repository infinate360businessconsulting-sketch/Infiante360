"""Central cohort configuration loader (content/cohorts.json).

evergreen(pid) is True when the cohort has no future date: pages must then show evergreen registration messaging
instead of dates. "Today" is the IST calendar date at build time (override with COHORT_TODAY=YYYY-MM-DD for tests).
A daily scheduled CI build re-evaluates this, so expired dates drop off automatically.
"""
import datetime, json, os

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(_ROOT, "content", "cohorts.json"), encoding="utf-8"))
M = CFG["evergreen_messages"]
PROGRAMS = {p["program_id"]: p for p in CFG["programs"]}
IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30))


def today():
    v = os.environ.get("COHORT_TODAY")
    return datetime.date.fromisoformat(v) if v else datetime.datetime.now(IST).date()


def evergreen(pid):
    p = PROGRAMS.get(pid)
    if not p:
        return True
    ref = p.get("expiration_date") or p.get("end_date") or p.get("start_date")
    return True if not ref else datetime.date.fromisoformat(ref) < today()
