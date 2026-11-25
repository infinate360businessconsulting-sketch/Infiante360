"""Data-integrity tests for the SEO datasets. Read-only; no network; no build."""
import json, os, re, unittest

D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "seo")
J = lambda n: json.load(open(os.path.join(D, n), encoding="utf-8"))


class Counts(unittest.TestCase):
    def test_reconciliation(self):
        r = J("reconciliation.json")
        self.assertTrue(r["all_counts_reconciled"], r["problems"])

    def test_expected_counts(self):
        for name, n in {"keywords": 1000, "commercial_100": 100, "longtail_100": 100, "pillars": 50, "articles": 365,
                        "ai_discovery": 100, "landing_pages": 30, "roadmap_90": 90, "social_90": 90, "authority_50": 50}.items():
            self.assertEqual(len(J(name + ".json")), n, name)


class Mapping(unittest.TestCase):
    def setUp(self):
        self.m = J("keyword_url_mapping.json")
        self.routes = {r["route"] for r in J("route_snapshot.json")["routes"]}

    def test_every_keyword_mapped_once(self):
        ids = {k["id"] for k in J("keywords.json")}
        self.assertEqual({r["keyword_id"] for r in self.m}, ids)
        self.assertEqual(len(self.m), len(ids))

    def test_targets_exist_or_are_planned(self):
        for r in self.m:
            if r["planned_new_url"]:
                self.assertNotIn(r["planned_new_url"], self.routes, "planned page already exists")
            else:
                self.assertIn(r["recommended_canonical"], self.routes, r["keyword_id"])
            self.assertIn(r["conversion_cta"], self.routes, r["keyword_id"])

    def test_no_invented_metrics(self):
        for r in self.m:
            self.assertIsNone(r["monthly_volume"]); self.assertIsNone(r["difficulty"]); self.assertIsNone(r["ranking"])

    def test_no_page_per_keyword(self):
        self.assertLessEqual(len({r["planned_new_url"] for r in self.m if r["planned_new_url"]}), 10)

    def test_queue_not_generated(self):
        for q in J("page_generation_queue.json")["queue"]:
            self.assertFalse(q["generated"])


class Secrets(unittest.TestCase):
    PAT = re.compile(r"(sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY)")

    def test_no_secret_like_strings_in_data(self):
        for dp, _, fs in os.walk(D):
            for f in fs:
                if f.endswith((".json", ".csv", ".md")):
                    self.assertIsNone(self.PAT.search(open(os.path.join(dp, f), encoding="utf-8", errors="ignore").read()), f)


if __name__ == "__main__":
    unittest.main()
