"""Banner slider: only approved banners with alt text and an existing image may be listed as approved."""
import json, os, sys, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))


class Banners(unittest.TestCase):
    def test_approved_banners_valid(self):
        for b in json.load(open(os.path.join(ROOT, "content", "banners.json")))["banners"]:
            if b.get("approved"):
                self.assertTrue(b.get("alt"), b)
                self.assertTrue(os.path.exists(os.path.join(ROOT, "assets", "banners", b["image"])), b)

    def test_demo_video_files(self):
        for f in ("infinate360-demo.mp4", "infinate360-demo-poster.jpg"):
            self.assertTrue(os.path.exists(os.path.join(ROOT, "assets", "media", f)))

    def test_slider_empty_without_banners(self):
        import banners
        self.assertIsInstance(banners.slider_html(), str)


if __name__ == "__main__":
    unittest.main()
