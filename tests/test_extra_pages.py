"""Extra pages (sitemap3): metadata limits, flagged for sitemap3, no unverified claims."""
import os, re, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
import content_extra as X  # noqa: E402


class Extra(unittest.TestCase):
    def test_metadata_and_flag(self):
        self.assertEqual(len(X.EXTRA_PAGES), 2)
        for p in X.EXTRA_PAGES:
            self.assertTrue(p["sitemap3"])
            self.assertLessEqual(len(p["title"]), 65)
            self.assertTrue(70 <= len(p["desc"]) <= 160, p["path"])
            self.assertTrue(25 <= len(p["answer"].split()) <= 90, p["path"])
            self.assertGreaterEqual(len(p["faqs"]), 2)

    def test_no_unverified_claims(self):
        bad = re.compile(r"100%|10K\+|\$\d|guaranteed (job|placement)|solution partner|60\+? hours|September 2026", re.I)
        for p in X.EXTRA_PAGES:
            blob = p["answer"] + " ".join(s[1] for s in p["sections"])
            self.assertIsNone(bad.search(blob), p["path"])


if __name__ == "__main__":
    unittest.main()
