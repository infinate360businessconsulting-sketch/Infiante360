"""Use-case library: all 4000 CSV rows published, metadata unique and within limits, slider present, rows labelled illustrative."""
import os, re, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import content_usecase_library as L  # noqa: E402


class Library(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(len(L.LIBRARY_PAGES), 41)
        rows = sum(sum(h.count('<th scope="row" id="uc-') for _, h, *_ in p["sections"]) for p in L.LIBRARY_PAGES[1:])
        self.assertEqual(rows, 4000)

    def test_metadata(self):
        for k in ("title", "desc", "h1"):
            vals = [p[k] for p in L.LIBRARY_PAGES]
            self.assertEqual(len(vals), len(set(vals)), k)
        for p in L.LIBRARY_PAGES:
            self.assertLessEqual(len(p["title"]), 65, p["title"])
            self.assertTrue(70 <= len(p["desc"]) <= 160, (len(p["desc"]), p["path"]))
            self.assertTrue(25 <= len(p["answer"].split()) <= 90, p["path"])
            self.assertIn("not delivered client results", p["answer"])

    def test_slider_when_banners_exist(self):
        import banners
        if banners.load():
            for p in L.LIBRARY_PAGES:
                self.assertTrue(any("data-slider" in s[1] for s in p["sections"]), p["path"])

    def test_internal_links_resolve(self):
        paths = {p["path"] for p in L.LIBRARY_PAGES}
        for p in L.LIBRARY_PAGES:
            for r in p["related"]:
                if r.startswith("use-cases/library/"):
                    self.assertIn(r, paths)
            # external/target existence is checked by the CI build validator (broken-link gate)


if __name__ == "__main__":
    unittest.main()
