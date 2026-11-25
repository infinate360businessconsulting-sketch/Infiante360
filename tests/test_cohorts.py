"""Cohort config tests: evergreen switching, consistency with detail files, no stale dates in evergreen mode."""
import importlib, json, os, re, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
J = lambda p: json.load(open(os.path.join(ROOT, p), encoding="utf-8"))


def load(today):
    os.environ["COHORT_TODAY"] = today
    for m in ("cohorts", "content_sme", "content_demo", "content_entdemo"):
        sys.modules.pop(m, None)
    return [importlib.import_module(m) for m in ("cohorts", "content_sme", "content_demo", "content_entdemo")]


class Cohorts(unittest.TestCase):
    def tearDown(self):
        os.environ.pop("COHORT_TODAY", None)

    def test_required_fields(self):
        need = {"program_id", "program_name", "registration_status", "start_date", "end_date", "session_timings", "time_zone",
                "program_fees", "registration_url", "promotional_banner", "expiration_date", "next_cohort"}
        for p in J("content/cohorts.json")["programs"]:
            self.assertTrue(need <= set(p), p["program_id"])

    def test_dates_match_detail_files(self):
        c = {p["program_id"]: p for p in J("content/cohorts.json")["programs"]}
        for pid, f in (("martech-sme-accelerator", "content/sme-accelerator.json"), ("martech-demo-bootcamp", "content/demo-bootcamp.json")):
            days = [d["date"] for d in J(f)["days"]]
            self.assertEqual((days[0], days[-1]), (c[pid]["start_date"], c[pid]["end_date"]), pid)

    def test_next_cohort_never_invented(self):
        for p in J("content/cohorts.json")["programs"]:
            n = p["next_cohort"]
            if n["status"] == "dates_to_be_announced":
                self.assertIsNone(n["start_date"]); self.assertIsNone(n["end_date"])

    def test_evergreen_after_end(self):
        cohorts, *_ = load("2026-11-25")
        for pid in ("martech-sme-accelerator", "martech-demo-bootcamp", "cxo-hive"):
            self.assertTrue(cohorts.evergreen(pid), pid)
        cohorts, *_ = load("2026-11-12")
        self.assertFalse(cohorts.evergreen("martech-sme-accelerator"))

    def test_no_stale_dates_when_evergreen(self):
        _, sme, demo, ent = load("2026-11-25")
        pages = sme.PAGES_SME + demo.PAGES_DEMO + ent.PAGES_ENTDEMO
        blob = " ".join(str(p.get(k)) for p in pages for k in ("title", "desc", "kicker", "answer", "sections", "faqs"))
        self.assertIsNone(re.search(r"\b\d{1,2}\s*(?:–|-|to)?\s*\d{0,2}\s*Nov(?:ember)?\b|\b(?:Mon|Tues|Wednes|Thurs|Fri|Satur|Sun)day \d", blob))
        self.assertIn("Registrations Open", blob)
        self.assertNotIn("sme-accelerator.ics", " ".join(str(p["sections"]) for p in sme.PAGES_SME))
        self.assertNotIn("demo-pay", " ".join(str(p["sections"]) for p in demo.PAGES_DEMO))


if __name__ == "__main__":
    unittest.main()
