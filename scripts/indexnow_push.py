#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""基于正文哈希变更的 IndexNow 增量推送脚本。

仅对比 <main> 正文归一化文本的 SHA-256 哈希，避免导航/外围微调触发无效 ping。
默认只做干跑检查（--dry-run）；传入 --submit 才会向 api.indexnow.org 发送 POST。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
DEFAULT_STATE_FILE = DOCS_DIR / ".indexnow-hashes.json"

SITE_BASE = "https://ouxxyy.github.io/ouba-classmate"
HOST = "ouxxyy.github.io"
INDEXNOW_KEY = "ouba20261106indexnowkey8f9a2b4c"
KEY_LOCATION = f"{SITE_BASE}/{INDEXNOW_KEY}.txt"
INDEXNOW_ENDPOINT = "https://api.indexnow.org/indexnow"
MAX_URLS_PER_DAY = 10000


def extract_main_hash(html_text: str) -> str:
    """提取 <main>（缺省回退 <body>）去脚本后的归一化正文文本并计算 SHA-256。"""
    match = re.search(r"<main\b[^>]*>(.*?)</main>", html_text, re.S | re.I)
    if not match:
        match = re.search(r"<body\b[^>]*>(.*?)</body>", html_text, re.S | re.I)
    fragment = match.group(1) if match else html_text
    fragment = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", fragment, flags=re.S | re.I)
    plain = re.sub(r"<[^>]+>", " ", fragment)
    normalized = re.sub(r"\s+", " ", plain).strip()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def _url_to_local_html(docs_dir: pathlib.Path, url: str) -> pathlib.Path | None:
    if not url.startswith(SITE_BASE):
        return None
    rel = url[len(SITE_BASE) :].lstrip("/")
    if not rel:
        return docs_dir / "index.html"
    if rel.endswith("/"):
        return docs_dir / rel / "index.html"
    candidate = docs_dir / rel
    if candidate.is_dir():
        return candidate / "index.html"
    return candidate


def _read_sitemap_urls(sitemap_path: pathlib.Path) -> list[str]:
    if not sitemap_path.exists():
        return []
    raw = sitemap_path.read_text(encoding="utf-8")
    try:
        root_el = ET.fromstring(raw)
        return [el.text.strip() for el in root_el.iter() if el.tag.endswith("loc") and el.text]
    except ET.ParseError:
        return [u.strip() for u in re.findall(r"<loc>(.*?)</loc>", raw, re.I) if u.strip()]


def collect_changed_urls(
    docs_dir: pathlib.Path, state_file: pathlib.Path
) -> tuple[list[str], dict[str, str]]:
    """对比 sitemap.xml 中各页面正文哈希与历史基线，返回发生变更的 URL 与最新哈希映射。"""
    urls = _read_sitemap_urls(docs_dir / "sitemap.xml")
    prev: dict[str, str] = {}
    if state_file.exists():
        try:
            loaded = json.loads(state_file.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                prev = {str(k): str(v) for k, v in loaded.items()}
        except (OSError, json.JSONDecodeError):
            prev = {}

    current: dict[str, str] = {}
    changed: list[str] = []
    for url in urls:
        html_path = _url_to_local_html(docs_dir, url)
        if not html_path or not html_path.exists():
            continue
        digest = extract_main_hash(html_path.read_text(encoding="utf-8"))
        current[url] = digest
        if prev.get(url) != digest:
            changed.append(url)
    return changed, current


def submit_indexnow(urls: list[str], timeout: float = 10.0) -> tuple[int, str]:
    """向 api.indexnow.org 发送批量 URL 变更通知。"""
    payload = {
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls[:MAX_URLS_PER_DAY],
    }
    req = urllib.request.Request(
        INDEXNOW_ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "ignore")
            return getattr(resp, "status", 200), body
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "ignore")
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, str(exc)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="基于正文哈希变更的 IndexNow 增量推送")
    parser.add_argument("--docs-dir", type=pathlib.Path, default=DOCS_DIR)
    parser.add_argument("--state-file", type=pathlib.Path, default=DEFAULT_STATE_FILE)
    parser.add_argument("--dry-run", action="store_true", help="仅检查变更 URL，不发送网络请求")
    parser.add_argument("--save-state", action="store_true", help="在 --dry-run 时同步保存哈希基线")
    parser.add_argument("--submit", action="store_true", help="将变更 URL 提交到 api.indexnow.org")
    args = parser.parse_args(argv)

    changed, current = collect_changed_urls(args.docs_dir, args.state_file)
    print(f"IndexNow 正文哈希检查：共扫描 {len(current)} 个 URL，正文变更 {len(changed)} 个")
    for url in changed:
        print(f"  - {url}")

    if args.submit and not args.dry_run:
        if not changed:
            print("无正文变更 URL，跳过 IndexNow 提交。")
            return 0
        status, body = submit_indexnow(changed)
        print(f"IndexNow POST 响应：HTTP {status} {body}".strip())
        if status not in (200, 202):
            return 1
        args.state_file.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"已更新哈希基线：{args.state_file}")
        return 0

    if args.save_state:
        args.state_file.write_text(
            json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        print(f"已保存哈希基线（dry-run）：{args.state_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
