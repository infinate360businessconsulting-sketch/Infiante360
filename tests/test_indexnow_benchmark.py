"""IndexNow key file is well-formed; benchmark has 100 unique questions and no pre-filled results."""
import csv, glob, os, re, unittest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Discovery(unittest.TestCase):
    def test_indexnow_key(self):
        f = glob.glob(os.path.join(ROOT, "indexnow", "*.txt"))
        self.assertEqual(len(f), 1)
        k = os.path.basename(f[0])[:-4]
        self.assertRegex(k, r"^[0-9a-f]{32}$")
        self.assertEqual(open(f[0]).read().strip(), k)

    def test_benchmark_has_no_results(self):
        rows = list(csv.DictReader(open(os.path.join(ROOT, "data", "seo", "ai_citation_benchmark.csv"), encoding="utf-8")))
        self.assertEqual(len(rows), 100)
        self.assertEqual(len({r["question"] for r in rows}), 100)
        for r in rows:
            for c in ("platform", "test_date", "observed_answer", "cited_domains", "cited_page_url", "our_domain_cited", "competitor_visibility"):
                self.assertEqual(r[c], "", c)


if __name__ == "__main__":
    unittest.main()
