"""Verification tests for growth assets: SVG badges, radar intelligence hub, dataset card, and interactive career receipt."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def _load_script(rel_path: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(mod)
    return mod


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

    def test_affiseo_geo_upgrades_and_guardrails(self):
        build_docs = _load_script("scripts/build_docs.py", "build_docs")
        indexnow_push = _load_script("scripts/indexnow_push.py", "indexnow_push")

        # 1. 严格维持 8 个 HTML 页面，且全部页面包含可引用头、<details> 折叠、JSON-LD 与最新更新日期
        html_files = sorted((ROOT / "docs").rglob("*.html"))
        self.assertEqual(len(html_files), 8, "Must strictly keep 8 HTML pages in docs/ per R5")
        for p in html_files:
            text = p.read_text(encoding="utf-8")
            self.assertIn('class="quotable-summary"', text, f"Missing quotable-summary in {p}")
            self.assertIn("<details", text, f"Missing <details> interactive block in {p}")
            self.assertIn("application/ld+json", text, f"Missing JSON-LD in {p}")
            self.assertIn("2026-11-14", text, f"Missing fresh build date in {p}")
            build_docs.check_guardrails(str(p), text)

        # 2. robots.txt 显式放行 AI 搜索/实时阅读 Bot 与 Bingbot
        robots = (ROOT / "docs" / "robots.txt").read_text(encoding="utf-8")
        for bot in ("OAI-SearchBot", "ChatGPT-User", "Bingbot"):
            self.assertIn(bot, robots)

        # 3. 诚实护栏能拦截夸大承诺
        bad_html = '<div class="quotable-summary">10</div><details><summary>Q</summary><p>100%包过，边界</p></details>'
        with self.assertRaises(ValueError):
            build_docs.check_guardrails("bad-page", bad_html)

        # 4. IndexNow 正文哈希：正文不变返回空列表，正文变化准确触发变更
        with tempfile.TemporaryDirectory() as tmp:
            tmp_docs = Path(tmp) / "docs"
            tmp_docs.mkdir()
            (tmp_docs / "sitemap.xml").write_text(
                '<?xml version="1.0" encoding="UTF-8"?>'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                "<url><loc>https://ouxxyy.github.io/ouba-classmate/</loc></url>"
                "</urlset>",
                encoding="utf-8",
            )
            page = tmp_docs / "index.html"
            page.write_text("<html><header>v1</header><main><h1>Hello</h1><p>Data 1</p></main></html>", encoding="utf-8")
            state = tmp_docs / ".indexnow-hashes.json"

            changed_1, hashes_1 = indexnow_push.collect_changed_urls(tmp_docs, state)
            self.assertEqual(changed_1, ["https://ouxxyy.github.io/ouba-classmate/"])
            state.write_text(json.dumps(hashes_1), encoding="utf-8")

            # 外围 header 变动而 main 未变：不应重复推送
            page.write_text("<html><header>v2</header><main><h1>Hello</h1><p>Data 1</p></main></html>", encoding="utf-8")
            changed_2, _ = indexnow_push.collect_changed_urls(tmp_docs, state)
            self.assertEqual(changed_2, [])

            # main 正文改动：应触发推送
            page.write_text("<html><header>v2</header><main><h1>Hello</h1><p>Data 2</p></main></html>", encoding="utf-8")
            changed_3, _ = indexnow_push.collect_changed_urls(tmp_docs, state)
            self.assertEqual(changed_3, ["https://ouxxyy.github.io/ouba-classmate/"])


if __name__ == "__main__":
    unittest.main()
