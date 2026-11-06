#!/usr/bin/env python3
"""从子仓库同步 SKILL.md 到合集仓 skills/<name>/SKILL.md，并校验 YAML frontmatter 格式。

支持两种同步源：
1. 本地同级仓库目录（默认 ../<repo>）
2. 远程 GitHub Raw（当本地同级仓库不存在时，用于 GitHub Actions CI）

用法：
  python3 scripts/sync_skills.py          # 同步并校验
  python3 scripts/sync_skills.py --check  # 仅校验 frontmatter 与文件存在性
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
REPOS_ROOT = ROOT.parent

# 子仓名 -> 子仓内 SKILL.md 相对路径
SKILL_SOURCES: dict[str, str] = {
    "job-search": "SKILL.md",
    "jd-resume-match": "SKILL.md",
    "ai-interviewer": "skills/ai-interviewer/SKILL.md",
    "sherlock-company": "skill/sherlock-company/SKILL.md",
    "mbai": "SKILL.md",
    "storyboard-scavenger": "SKILL.md",
    "travel-art-album-skill": "SKILL.md",
    "mystery-skill": "SKILL.md",
}

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def validate_frontmatter(skill_name: str, content: str) -> list[str]:
    """校验 SKILL.md 是否包含合法的 YAML frontmatter 及必填字段 name / description。"""
    errors: list[str] = []
    match = FRONTMATTER_RE.match(content)
    if not match:
        return [f"{skill_name}: 缺少以 --- 包裹的顶部 YAML frontmatter"]
    fm_text = match.group(1)
    if not re.search(r"^name:\s*\S+", fm_text, re.MULTILINE):
        errors.append(f"{skill_name}: frontmatter 缺少 name 字段")
    if not re.search(r"^description:\s*\S+", fm_text, re.MULTILINE):
        errors.append(f"{skill_name}: frontmatter 缺少 description 字段")
    return errors


def fetch_skill_content(repo_name: str, rel_path: str) -> str:
    """优先从本地同级目录读取，不存在时从 GitHub main 分支拉取。"""
    local_file = REPOS_ROOT / repo_name / rel_path
    if local_file.is_file():
        return local_file.read_text(encoding="utf-8")
    url = f"https://raw.githubusercontent.com/ouxxyy/{repo_name}/main/{rel_path}"
    req = urllib.request.Request(url, headers={"User-Agent": "ouba-classmate-skill-sync"})
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def add_suite_header(repo_name: str, content: str) -> str:
    """在 frontmatter 之后插入合集来源说明，引导需要脚本/参考资料的 Agent 访问完整仓库或使用合集。"""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return content
    header = (
        f"\n> 📦 **套件索引说明**：本 Skill 已收录于 [`ouxxyy/ouba-classmate`](https://github.com/ouxxyy/ouba-classmate) 套件。"
        f"完整执行脚本、`references/` 与示例数据位于子仓库 [`ouxxyy/{repo_name}`](https://github.com/ouxxyy/{repo_name})。\n"
    )
    end = match.end()
    if "套件索引说明" in content[end : end + 300]:
        return content
    return content[:end] + header + content[end:]


def main() -> int:
    parser = argparse.ArgumentParser(description="同步并校验合集 skills/ 目录")
    parser.add_argument("--check", action="store_true", help="仅校验已有 skills/<name>/SKILL.md")
    args = parser.parse_args()

    all_errors: list[str] = []
    for repo_name, rel_path in SKILL_SOURCES.items():
        target_dir = SKILLS_DIR / repo_name
        target_file = target_dir / "SKILL.md"
        if not args.check:
            raw = fetch_skill_content(repo_name, rel_path)
            synced = add_suite_header(repo_name, raw)
            target_dir.mkdir(parents=True, exist_ok=True)
            target_file.write_text(synced, encoding="utf-8")
            print(f"[已同步] skills/{repo_name}/SKILL.md <- {repo_name}/{rel_path}")

        if not target_file.is_file():
            all_errors.append(f"{repo_name}: 缺少文件 {target_file}")
            continue

        content = target_file.read_text(encoding="utf-8")
        all_errors.extend(validate_frontmatter(repo_name, content))

    if all_errors:
        for err in all_errors:
            print(f"[错误] {err}", file=sys.stderr)
        return 1

    print(f"✔ 全部 {len(SKILL_SOURCES)} 个 Skill 的 SKILL.md 校验通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
