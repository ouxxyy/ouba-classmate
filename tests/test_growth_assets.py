"""Verification tests for growth assets: SVG badges, radar intelligence hub, dataset card, and interactive career receipt."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class GrowthAssetsTests(unittest.TestCase):
    def test_svg_badges_exist_and_valid(self):
        badges = [
            "benchmark-top-tier.svg",
            "benchmark-pdf-leader.svg",
            "benchmark-verified.svg",
            "suite-install.svg",
        ]
        for b in badges:
            p = ROOT / "assets" / "badges" / b
            self.assertTrue(p.exists(), f"Missing badge {b}")
            content = p.read_text(encoding="utf-8")
            self.assertIn("<svg", content)
            self.assertIn("</svg>", content)

    def test_radar_handbook_contains_all_four_modules(self):
        radar = ROOT / "radar" / "README.md"
        self.assertTrue(radar.exists())
        text = radar.read_text(encoding="utf-8")
        self.assertIn("连环追问 24 道母题", text)
        self.assertIn("招聘 JD 15 大高频黑话解码表", text)
        self.assertIn("四态背调防踩坑 18 问", text)
        self.assertIn("工作任务 AI 不可替代指数", text)

    def test_docs_index_has_interactive_career_radar_and_r5_page_count(self):
        html_files = list((ROOT / "docs").rglob("*.html"))
        self.assertEqual(len(html_files), 8, "Must strictly keep 8 HTML pages in docs/ per R5")
        index_html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        self.assertIn('id="career-radar"', index_html)
        self.assertIn("copyReceiptText()", index_html)
        self.assertIn("downloadReceiptPng()", index_html)

    def test_dataset_card_has_huggingface_frontmatter(self):
        card = (ROOT / "benchmark" / "DATASET_CARD.md").read_text(encoding="utf-8")
        self.assertTrue(card.startswith("---\n"))
        self.assertIn("license: cc-by-4.0", card)
        self.assertIn("ouxxyy/ouba-classmate", card)


if __name__ == "__main__":
    unittest.main()
