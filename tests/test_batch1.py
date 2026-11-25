"""Guide batch 1: metadata limits, uniqueness, existing related targets, assets present, no unverified claims."""
import os, re, sys, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import content_batch1 as B  # noqa: E402
import content_kb as K  # noqa: E402


class Batch1(unittest.TestCase):
    def test_count_and_limits(self):
        self.assertEqual(len(B.BATCH1), 10)
        for p in B.BATCH1:
            self.assertLessEqual(len(p["title"]), 65, p["path"])
            self.assertTrue(70 <= len(p["desc"]) <= 160, (p["path"], len(p["desc"])))
            self.assertTrue(25 <= len(p["answer"].split()) <= 90, (p["path"], len(p["answer"].split())))
            self.assertGreaterEqual(len(p["faqs"]), 3)
            self.assertGreaterEqual(len(p["sources"]), 3)

    def test_unique_across_site(self):
        allp = K.KB_PAGES
        for k in ("title", "desc", "h1", "path"):
            self.assertEqual(len({p[k] for p in allp}), len(allp), k)

    def test_related_targets_exist(self):
        paths = {p["path"] for p in K.KB_PAGES}
        for p in B.BATCH1:
            for r in p["related"]:
                if r.startswith(("guides/", "use-cases/")) and r != "guides/what-is-mcp.html":  # what-is-mcp is defined outside KB_PAGES
                    self.assertIn(r, paths, (p["path"], r))

    def test_images_exist(self):
        for p in B.BATCH1:
            slug = p["path"].split("/")[-1][:-5]
            for f in ("hero.webp", "hero-800.webp", "og.png", "diagram.svg"):
                self.assertTrue(os.path.exists(os.path.join(ROOT, "assets", "visuals", slug, f)), (slug, f))

    def test_no_unverified_claims(self):
        bad = re.compile(r"\d+(\.\d+)?%|\bguarantee|best-in-class|official partner|\bour clients\b|case study shows", re.I)
        for p in B.BATCH1:
            blob = p["answer"] + " ".join(s[1] for s in p["sections"]) + " ".join(a for _, a in p["faqs"])
            self.assertIsNone(bad.search(blob), p["path"])


if __name__ == "__main__":
    unittest.main()
