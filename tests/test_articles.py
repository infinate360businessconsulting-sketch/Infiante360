"""Article batches: queue integrity, length limits, unique metadata, no invented proof."""
import json, os, re, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))
from content_articles import A  # noqa: E402
from content_articles2 import B  # noqa: E402

ALL = A + B
Q = json.load(open(os.path.join(ROOT, "data", "seo", "article_queue.json"), encoding="utf-8"))


class Articles(unittest.TestCase):
    def test_counts(self):
        self.assertEqual(len(ALL), 20)
        self.assertEqual(Q["total"], 365)
        self.assertEqual(Q["published"], 20)

    def test_queue_matches_pages(self):
        pub = {x["url"].lstrip("/") for x in Q["queue"] if x["status"].startswith("published")}
        self.assertEqual(pub, {p["path"] for p in ALL})

    def test_unique_and_limits(self):
        for k in ("title", "h1", "desc", "path"):
            self.assertEqual(len({p[k] for p in ALL}), len(ALL), k)
        for p in ALL:
            self.assertLessEqual(len(p["title"]), 65, p["path"])
            self.assertTrue(70 <= len(p["desc"]) <= 160, p["path"])
            self.assertTrue(25 <= len(p["answer"].split()) <= 90, p["path"])
            self.assertTrue(p["sources"] and p["faqs"], p["path"])

    def test_no_invented_proof(self):
        blob = json.dumps([p["sections"] for p in ALL]) + json.dumps([p["answer"] for p in ALL])
        self.assertIsNone(re.search(r"\b\d+\+? (clients|learners|projects)\b|guarantee|Solution Partner|testimonial", blob, re.I))


if __name__ == "__main__":
    unittest.main()
