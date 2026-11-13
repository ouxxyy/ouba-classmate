"""Verification tests for growth assets: SVG badges, radar intelligence hub, dataset card, and interactive career receipt."""
import json
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

    def test_openseo_inspired_upgrades_present(self):
        # 1. 多宿主插件与 MCP 清单
        claude_market = json.loads(
            (ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8")
        )
        plugin_names = [p["name"] for p in claude_market["plugins"]]
        self.assertEqual(len(plugin_names), 8)
        self.assertIn("mbai", plugin_names)

        for rel in (
            ".cursor-plugin/marketplace.json",
            ".cursor-plugin/plugin.json",
            ".codex-plugin/plugin.json",
            ".mcp.json",
        ):
            p = ROOT / rel
            self.assertTrue(p.exists(), f"Missing {rel}")
            data = json.loads(p.read_text(encoding="utf-8"))
            self.assertIsInstance(data, dict)

        # 2. docs/index.html 中的 GEO FAQPage、gh skill install 与本地水分检测器
        html_files = list((ROOT / "docs").rglob("*.html"))
        self.assertEqual(len(html_files), 8)
        index_html = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
        self.assertIn("FAQPage", index_html)
        self.assertIn('id="resume-evidence-checker"', index_html)
        self.assertIn("checkResumeEvidence()", index_html)
        self.assertIn("gh skill install", index_html)

        # 3. benchmark 页按岗位人群选型矩阵
        bench_html = (ROOT / "docs" / "benchmark" / "index.html").read_text(encoding="utf-8")
        self.assertIn("按岗位与求职阶段怎么选", bench_html)


if __name__ == "__main__":
    unittest.main()
