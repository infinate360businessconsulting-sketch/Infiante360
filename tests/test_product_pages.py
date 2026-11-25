"""Product and event pages (sitemap4): limits, uniqueness, linking, honest claims."""
import os, re, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import content_products as P  # noqa: E402
import content_group as G  # noqa: E402


class Products(unittest.TestCase):
    def test_counts_and_flag(self):
        self.assertEqual(len(P.PRODUCT_PAGES), 8)
        self.assertEqual(len(P.EVENT_PAGES), 11)
        self.assertTrue(all(p["sitemap4"] for p in P.PRODUCT_ALL))

    def test_metadata_unique_and_within_limits(self):
        allp = P.PRODUCT_ALL + G.GROUP_PAGES
        for k in ("title", "desc", "h1", "path"):
            self.assertEqual(len({p[k] for p in allp}), len(allp), k)
        for p in P.PRODUCT_ALL:
            self.assertLessEqual(len(p["title"]), 65, p["path"])
            self.assertTrue(70 <= len(p["desc"]) <= 160, (p["path"], len(p["desc"])))
            self.assertTrue(25 <= len(p["answer"].split()) <= 90, (p["path"], len(p["answer"].split())))
            self.assertGreaterEqual(len(p["faqs"]), 2)
            self.assertGreaterEqual(len(p["keywords"]), 5)

    def test_every_page_linked_from_a_hub(self):
        linked = {u for _, u in P.HUB_PROD["list_items"] + P.HUB_EV["list_items"]}
        for p in P.PRODUCT_ALL:
            if p["path"] not in ("products/index.html", "events/index.html"):
                self.assertIn(p["path"], linked, p["path"])
        eco = {u for _, u in G.HUB_ECO["list_items"]}
        self.assertTrue({"products/index.html", "events/index.html"} <= eco)

    def test_events_have_no_dates_or_fees(self):
        for p in P.EVENTS:
            blob = " ".join(s[1] for s in p["sections"])
            self.assertIn("To be announced", blob)
            self.assertNotRegex(blob, r"₹|\$\d|Rs\.? ?\d|\b20\d\d\b")

    def test_no_unverified_claims(self):
        bad = re.compile(r"100%|10K\+|guaranteed (job|placement)|solution partner|official partner of|\d[\d,]*\+? (learners|members|students)|₹\s?\d|\bplacement assured", re.I)
        for p in P.PRODUCT_ALL:
            blob = p["answer"] + " ".join(s[1] for s in p["sections"]) + " ".join(a for _, a in p["faqs"])
            self.assertIsNone(bad.search(blob), p["path"])


if __name__ == "__main__":
    unittest.main()
