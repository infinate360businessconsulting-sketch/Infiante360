"""Group-brand and country pages (sitemap4): limits, uniqueness, honest claims, real regulators."""
import os, re, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import content_group as G  # noqa: E402


class Group(unittest.TestCase):
    def test_counts_and_flag(self):
        self.assertEqual(len(G.COUNTRY_PAGES), 17)
        self.assertEqual(len(G.GROUP_PAGES), 24)
        self.assertTrue(all(p["sitemap4"] for p in G.GROUP_PAGES))

    def test_metadata_unique_and_within_limits(self):
        for k in ("title", "desc", "h1", "path"):
            self.assertEqual(len({p[k] for p in G.GROUP_PAGES}), len(G.GROUP_PAGES), k)
        for p in G.GROUP_PAGES:
            self.assertLessEqual(len(p["title"]), 65, p["path"])
            self.assertTrue(70 <= len(p["desc"]) <= 160, p["path"])
            self.assertTrue(25 <= len(p["answer"].split()) <= 90, p["path"])
            self.assertGreaterEqual(len(p["faqs"]), 2)
            self.assertGreaterEqual(len(p["keywords"]), 5)

    def test_every_page_is_linked_from_a_hub(self):
        hubs = G.HUB_ECO["list_items"] + G.HUB_LOC["list_items"]
        linked = {u for _, u in hubs}
        for p in G.GROUP_PAGES:
            if not p["path"].endswith("/index.html"):
                self.assertIn(p["path"], linked, p["path"])

    def test_no_unverified_claims(self):
        bad = re.compile(r"100%|10K\+|guaranteed (job|placement)|solution partner|official partner of|\d[\d,]*\+? (learners|members|students)|we have an office|offices in", re.I)
        for p in G.GROUP_PAGES:
            blob = p["answer"] + " ".join(s[1] for s in p["sections"]) + " ".join(a for _, a in p["faqs"])
            self.assertIsNone(bad.search(blob), p["path"])

    def test_country_pages_name_law_regulator_and_no_office(self):
        for p in G.COUNTRY_PAGES:
            blob = " ".join(s[1] for s in p["sections"])
            self.assertIn("not legal advice", blob.lower())
            self.assertIn("local office", p["answer"].lower())
            self.assertTrue(p["sources"], p["path"])
        self.assertEqual(len({c[5] for c in G.C}), 17)

    def test_phone(self):
        self.assertIn("82968 93895", " ".join(s[1] for s in G.SKILLSURF["sections"]))


if __name__ == "__main__":
    unittest.main()
