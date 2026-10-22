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
REPO_META = {'job-search': {'category': 'career',
               'desc': '求职岗位筛选 Agent Skill：按确认条件整理带来源的 HTML、Excel 与 JSON 岗位清单',
               'description_en': 'Job search Agent Skill with source-backed job lists',
               'keywords': ['求职岗位筛选', '招聘信息整理', '岗位清单', 'job search agent', 'job shortlist'],
               'use_cases': ['按岗位城市薪资筛选招聘信息', '保存带来源证据的岗位清单']},
 'storyboard-scavenger': {'category': 'skill',
                          'desc': 'AI 视频分镜与提示词生成 Skill：提供可灵 Kling／即梦 Seedance 工作流与七要素分镜',
                          'description_en': 'AI video storyboard and prompt-writing skill for Kling and '
                                            'Seedance',
                          'keywords': ['AI 视频分镜',
                                       '可灵提示词',
                                       '即梦分镜',
                                       'AI video storyboard',
                                       'Kling',
                                       'Seedance'],
                          'use_cases': ['把创意拆成逐镜头提示词', '规划多个镜头的环境与运镜']},
 'jd-resume-match': {'category': 'career',
                     'desc': '简历与 JD 匹配及简历优化：证据引用、可复算评分、结构建议与离线 HTML 报告',
                     'description_en': 'Evidence-based resume and job-description matching and review',
                     'keywords': ['简历 JD 匹配', '简历优化', '证据匹配', 'resume matching', 'resume review'],
                     'use_cases': ['对照岗位要求查简历证据缺口', '调整简历结构与经历表达']},
 'mbai': {'category': 'career',
          'desc': '工作任务 AI 不可替代指数：任务分析、贡献证据与替代风险自评，非裁员预测',
          'description_en': 'Task-level AI assessment for career reflection',
          'keywords': ['AI 替代风险自评', '工作任务分析', '职业规划', 'AI task assessment', 'career planning'],
          'use_cases': ['拆解工作任务中的自动化空间', '梳理个人贡献和职业证据缺口']},
 'mystery-skill': {'category': 'skill',
                   'desc': 'Mystery Method 认知框架 Skill：基于公开资料的思维模型与决策启发式，供个人学习',
                   'description_en': 'Mystery Method cognitive framework for personal study',
                   'keywords': ['Mystery 思维模型',
                                '迷男方法分析',
                                'Mystery Method',
                                'Erik von Markovik',
                                'cognitive framework'],
                   'use_cases': ['研究 Mystery 的认知框架', '分析社交情境与决策边界']},
 'travel-art-album-skill': {'category': 'skill',
                            'desc': '旅行照片艺术画册 Skill：确认风格小样后制作单文件离线 HTML 翻页相册',
                            'description_en': 'Travel photo album and single-file offline HTML flipbook '
                                              'skill',
                            'keywords': ['旅行照片画册',
                                         '离线翻页相册',
                                         '照片艺术化',
                                         'travel photo album',
                                         'offline flipbook'],
                            'use_cases': ['把旅行照片制作成艺术画册', '离线翻阅相册并用浏览器打印 PDF']},
 'ai-interviewer': {'category': 'career',
                    'desc': '中文语音 AI 面试陪练：基于 JD 与经历追问、引用原话点评、初答重答对比',
                    'description_en': 'Chinese voice AI mock interview practice',
                    'keywords': ['AI 面试官',
                                 '中文语音模拟面试',
                                 '面试陪练',
                                 'AI mock interview',
                                 'voice interview practice'],
                    'use_cases': ['练习自我介绍与经历面试', '通过原话点评和重答改进回答']},
 'sherlock-company': {'category': 'career',
                      'desc': '入职前公司证据调查：区分已证实、线索、冲突与未知，输出核实清单和离线 HTML 档案',
                      'description_en': 'Pre-offer employer research with evidence boundaries',
                      'keywords': ['入职前查公司', 'Offer 公司调查', '公司证据调查', 'employer research', 'company research'],
                      'use_cases': ['接受 Offer 前核查公司信息', '整理冲突证据与待核验问题']},
 'Attention': {'category': 'local',
               'desc': 'ActivityWatch 本地专注力仪表盘：任务切换、分心与持续专注时段分析',
               'description_en': 'Local ActivityWatch dashboard for focus and context switching',
               'keywords': ['ActivityWatch 仪表盘',
                            '专注力分析',
                            '任务切换',
                            'ActivityWatch dashboard',
                            'context switching'],
               'use_cases': ['查看一天的专注与分心模式', '分析任务切换和持续专注时段']},
 'postapp': {'category': 'local',
             'desc': '姿势企鹅 Posture Penguin：本地姿态检测的 Chrome 坐姿提醒插件',
             'description_en': 'Chrome posture reminder extension with on-device pose detection',
             'keywords': ['Chrome 坐姿提醒', '姿势企鹅', 'Posture Penguin', 'posture reminder', 'Chrome extension'],
             'use_cases': ['在电脑前设置坐姿提醒', '查看本地坐姿记录']}}


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


def replace_project_block(readme, repos):
    """Replace the generated block without modifying either handwritten section."""
    if (readme.count(START_MARK) != 1 or readme.count(END_MARK) != 1
            or readme.index(START_MARK) >= readme.index(END_MARK)):
        raise ValueError("README.md 需要一对有序且唯一的 projects 标记")
    start = readme.index(START_MARK) + len(START_MARK)
    end = readme.index(END_MARK)
    return readme[:start] + "\n" + render_readme_block(repos) + readme[end:]


def build_catalog(repos, generated_at=None):
    """Keep existing catalog fields and add task-oriented discovery information."""
    return {
        "generated_at": generated_at if generated_at is not None else _dt.datetime.now(
            _dt.timezone.utc).isoformat(timespec="seconds"),
        "owner": OWNER,
        "projects": [
            {
                "name": r["name"],
                "url": r["html_url"],
                "description": REPO_META.get(r["name"], {}).get("desc") or r["description"] or "",
                "category": REPO_META.get(r["name"], {}).get("category", "more"),
                "language": r.get("language") or "",
                "stars": r["stargazers_count"],
                "updated_at": r["updated_at"],
                "description_en": REPO_META.get(r["name"], {}).get("description_en", ""),
                "keywords": list(REPO_META.get(r["name"], {}).get("keywords", [])),
                "use_cases": list(REPO_META.get(r["name"], {}).get("use_cases", [])),
            }
            for r in repos
        ],
    }


def main():
    repos = [r for r in fetch_repos()
             if not r["fork"] and r["name"] not in EXCLUDE]
    repos.sort(key=lambda r: r["updated_at"], reverse=True)
    print(f"collected {len(repos)} original repos "
          f"(excluded {len(EXCLUDE)} + forks)")

    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()
    try:
        new_readme = replace_project_block(readme, repos)
    except ValueError as error:
        sys.exit(str(error))
    catalog = build_catalog(repos)
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_readme)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"README block + projects.json updated ({len(repos)} projects)")


if __name__ == "__main__":
    main()
