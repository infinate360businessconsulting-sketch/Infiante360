"""Pillar decisions and AI-visibility registry: no invented results, every target is a real or approved route."""
import json, os, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda f: json.load(open(os.path.join(ROOT, "data", "seo", f), encoding="utf-8"))


class Registries(unittest.TestCase):
    def test_pillars(self):
        p = J("pillar_decisions.json")["pillars"]
        self.assertEqual(len(p), 50)
        self.assertTrue(all(x["hub_exists"] and "no new pillar page" in x["decision"] for x in p))

    def test_ai_registry_untested(self):
        q = J("ai_visibility_registry.json")["queries"]
        self.assertEqual(len(q), 100)
        for r in q:
            self.assertEqual(r["result"], "Not tested", r["query_id"])
            for k in ("engine", "tested_on", "brand_mentioned", "cited_url", "evidence_ref"):
                self.assertIsNone(r[k], (r["query_id"], k))
            self.assertTrue(r["target_url"].startswith("/"), r["query_id"])

    def test_image_manifest_quality(self):
        m = J("image_quality_report.json")
        self.assertTrue(all(not x["issues"] for x in m))
        self.assertEqual(len({x["image_id"] for x in J("image_manifest.json")}), len(m))


if __name__ == "__main__":
    unittest.main()
