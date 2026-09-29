#!/usr/bin/env python3
"""同步欧八同学项目索引。

拉取 ouxxyy 名下全部公开仓库，过滤 fork 和排除清单，重新生成
README.md 里 <!-- projects:start/end --> 之间的项目区块，并刷新
projects.json（机器可读目录）。

用法：python3 scripts/update_projects.py
可选环境变量：GITHUB_TOKEN（GitHub Actions 里自带，本地可不留）。
"""

import datetime as _dt
import json
import os
import re
import sys
import urllib.request

OWNER = "ouxxyy"
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
README_PATH = os.path.join(ROOT, "README.md")
JSON_PATH = os.path.join(ROOT, "projects.json")

START_MARK = "<!-- projects:start -->"
END_MARK = "<!-- projects:end -->"

# 不收录的原创仓库（皮肤类、隐私政策托管页、早期实验仓库等）
EXCLUDE = {
    "ouba-classmate",
    "codex-luce",
    "posture-penguin-privacy-policy",
    "learn-python",
    "agenteam",
    "hilingge",
}

CATEGORY_LABELS = {
    "career": "职场 · 跳槽涨薪",
    "skill": "AI Skill · 装进你的 Agent",
    "app": "智能体应用 · 打开就用",
    "local": "本地工具 · 装在自己电脑",
    "more": "更多项目",
}
CATEGORY_ORDER = ["career", "skill", "app", "local", "more"]

# 描述为各仓库 README/描述的中文摘编；stars 与更新时间每次从 API 实时刷新
REPO_META = {
    "storyboard-scavenger": {
        "category": "skill",
        "desc": "把混乱的创意清理成可拍摄的 AI 视频分镜：输入一堆想法，输出有序的分镜表",
    },
    "jd-resume-match": {
        "category": "career",
        "desc": "简历 vs JD 匹配度打分器：可复算评分、原文证据引用、HTML 体检单与脱敏分享卡",
    },
    "mbai": {
        "category": "career",
        "desc": "工作任务 AI 不可替代指数：复制 PROMPT.md 到任意 AI 对话即用，也能装成 Agent Skill",
    },
    "mystery-skill": {
        "category": "skill",
        "desc": "Mystery 思维操作系统：从 11 篇著作、10+ 访谈、20+ 外部评论提炼的心智模型、决策启发式与表达 DNA",
    },
    "travel-art-album-skill": {
        "category": "skill",
        "desc": "旅行照片艺术化工作流 + 单文件离线翻页相册 Skill",
    },
    "ai-interviewer": {
        "category": "career",
        "desc": "基于 JD 与经历的中文语音 AI 面试陪练：逐题五维点评、原话引用、初答重答对比",
    },
    "sherlock-company": {
        "category": "career",
        "desc": "Offer 前的公司证据调查智能体：已证实/有线索/说法冲突/还不知道四态报告 + 离线 HTML 侦探档案",
    },
    "Attention": {
        "category": "local",
        "desc": "本地专注力仪表盘：读 ActivityWatch 数据，算分心程度、切换次数与心流时段，数据不出本机",
    },
    "postapp": {
        "category": "local",
        "desc": "姿势企鹅：Chrome 坐姿监测插件，工作时提醒你别头前倾、驼背",
    },
}


def api(path):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={"Accept": "application/vnd.github+json",
                 "User-Agent": "ouba-classmate-sync"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    # 空代理表：强制直连，避免本机系统代理（可能已死）咬住 urllib
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=30) as resp:
        return json.load(resp)


def fetch_repos():
    repos, page = [], 1
    while True:
        batch = api(f"/users/{OWNER}/repos?per_page=100&page={page}&type=owner&sort=updated")
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1


def render_readme_block(repos):
    by_cat = {}
    for repo in repos:
        meta = REPO_META.get(repo["name"])
        cat = meta["category"] if meta else "more"
        by_cat.setdefault(cat, []).append(repo)

    lines = []
    for cat in CATEGORY_ORDER:
        items = by_cat.get(cat)
        if not items:
            continue
        items.sort(key=lambda r: r["updated_at"], reverse=True)
        lines.append(f"### {CATEGORY_LABELS[cat]}")
        lines.append("")
        lines.append("| 项目 | 它做什么 | 最近更新 |")
        lines.append("| --- | --- | --- |")
        for repo in items:
            meta = REPO_META.get(repo["name"], {})
            desc = meta.get("desc") or repo["description"] or "—"
            name_cell = f'[{repo["name"]}]({repo["html_url"]})'
            if repo["stargazers_count"]:
                name_cell += f' ★{repo["stargazers_count"]}'
            lines.append(f'| {name_cell} | {desc} | {repo["updated_at"][:10]} |')
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main():
    repos = [r for r in fetch_repos()
             if not r["fork"] and r["name"] not in EXCLUDE]
    repos.sort(key=lambda r: r["updated_at"], reverse=True)
    print(f"collected {len(repos)} original repos "
          f"(excluded {len(EXCLUDE)} + forks)")

    readme = open(README_PATH, encoding="utf-8").read()
    if START_MARK not in readme or END_MARK not in readme:
        sys.exit("README.md 缺少 projects 标记，退出")
    block = render_readme_block(repos)
    new_readme = re.sub(
        re.escape(START_MARK) + r".*?" + re.escape(END_MARK),
        START_MARK + "\n" + block + END_MARK,
        readme, flags=re.S)
    open(README_PATH, "w", encoding="utf-8").write(new_readme)

    catalog = {
        "generated_at": _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds"),
        "owner": OWNER,
        "projects": [
            {
                "name": r["name"],
                "url": r["html_url"],
                "description": REPO_META.get(r["name"], {}).get("desc") or r["description"] or "",
                "category": REPO_META.get(r["name"], {}).get("category", "more"),
                "language": (r.get("language") or ""),
                "stars": r["stargazers_count"],
                "updated_at": r["updated_at"],
            }
            for r in repos
        ],
    }
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"README block + projects.json updated ({len(repos)} projects)")


if __name__ == "__main__":
    main()
