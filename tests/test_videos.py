"""Video sitemap generator: empty registry writes nothing; only complete, approved, transcribed videos qualify."""
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))
import videos as V  # noqa: E402

OK = dict(approved=True, has_transcript=True, page="videos/aep.html", title="AEP", description="d", thumbnail="https://x/t.jpg", content_url="https://x/v.mp4", duration=60, published="2026-11-25", tags=["a&b"])


class Videos(unittest.TestCase):
    def test_registry_is_empty_so_no_sitemap(self):
        self.assertIsNone(V.video_sitemap("https://x/"))

    def test_eligibility(self):
        self.assertTrue(V.eligible(OK))
        for k in ("approved", "has_transcript", "page", "duration", "published"):
            self.assertFalse(V.eligible({**OK, k: None}), k)
        self.assertFalse(V.eligible({**OK, "duration": "60"}))

    def test_xml_and_jsonld(self):
        x = V.video_sitemap("https://x/", [OK, {**OK, "approved": False}])
        self.assertEqual(x.count("<video:video>"), 1)
        self.assertIn("a&amp;b", x)
        self.assertEqual(V.video_jsonld(OK, "https://x/")["duration"], "PT1M0S")


if __name__ == "__main__":
    unittest.main()
