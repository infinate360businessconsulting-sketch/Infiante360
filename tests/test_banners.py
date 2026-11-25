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


class TopSliderTests(unittest.TestCase):
    def test_content_matching_and_exclusions(self):
        import banners
        page = lambda path, title, kw=(): dict(path=path, title=title, category="", keywords=list(kw))
        names = lambda pg: [b["image"] for b in banners.select(pg)]
        self.assertEqual(names(page("agentic/x.html", "MCP agents"))[0], "agentic-ai-mcp-program.webp")
        self.assertEqual(names(page("research/a.html", "Market research intelligence"))[0], "research-ai-agent-orchestration.webp")
        self.assertGreaterEqual(len(names(page("zzz.html", "unrelated"))), 3)
        self.assertNotIn("training/corporate-training.html", [b["link"] for b in banners.select(page("training/corporate-training.html", "Corporate training"))])
        self.assertEqual(banners.top_slider(page("lp/x.html", "Landing")), "")
        self.assertIn("../assets/banners/", banners.top_slider(page("a/b.html", "AEP")))
