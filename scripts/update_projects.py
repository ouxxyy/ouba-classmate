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
    "ouxxyy",
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

# 描述为各仓库 README/描述的中文摘编；stars 与更新时间每次从 API 实时刷新；
# order 为分类内固定展示顺序（缺省时分类内按更新时间倒序）
REPO_META = {'codex-gif-video': {'category': 'skill',
                     'desc': '调用 GPT Image 2.6 原生 GIF 能力，按 69 种内置风格生成长 GIF 或静音 MP4（适合 X 短视频、口播动画、绘本及搭配 Hypit '
                             '等剪辑 Skill）',
                     'description_en': 'Animated GIF generator and silent MP4 video assets for agents',
                     'keywords': ['GPT Image 2.6',
                                  '原生 GIF',
                                  'GIF 视频素材',
                                  '长 GIF',
                                  '静音 MP4',
                                  '口播动画素材',
                                  '儿童绘本',
                                  'X 短视频',
                                  '69 种风格',
                                  'Hypit 素材',
                                  '人物一致性',
                                  'animated GIF',
                                  'Codex Skill',
                                  'AI 动图生成',
                                  '长 GIF 生成',
                                  '静音 MP4 素材',
                                  '口播 B-roll 动画',
                                  'animated GIF generator',
                                  'silent video assets'],
                     'use_cases': ['调用 GPT Image 2.6 生成 X 爆款长 GIF 短视频、口播 B-roll 与儿童绘本动图',
                                   '为 Hypit、Remotion、Lemo-Opuscar 等热门 AI 剪辑 Skill 提供无字幕原生动画素材',
                                   '如何为口播、绘本或 X 内容生成长 GIF 和无声动画素材？']},
 'job-search': {'category': 'career',
                'order': 0,
                'desc': 'AI岗位搜索大师：按确认条件整理带来源的 HTML、Excel 与 JSON 岗位清单',
                'description_en': 'Chinese job search agent and source-backed job hunting shortlist',
                'keywords': ['AI岗位搜索大师',
                             '求职岗位筛选',
                             '招聘信息整理',
                             '岗位清单',
                             'job search agent',
                             'job shortlist',
                             '中文求职工具',
                             'AI 找工作',
                             '招聘信息筛选',
                             'BOSS 直聘岗位筛选',
                             'job hunting'],
                'use_cases': ['按岗位城市薪资筛选招聘信息', '保存带来源证据的岗位清单', '怎样按城市、薪资和发布日期筛选招聘岗位？']},
 'storyboard-scavenger': {'category': 'skill',
                          'desc': 'AI 视频分镜与提示词生成 Skill：提供可灵 Kling／即梦 Seedance 工作流与七要素分镜',
                          'description_en': 'AI video storyboard and prompts for Kling, Seedance, Veo and '
                                            'Sora',
                          'keywords': ['AI 视频分镜',
                                       '可灵提示词',
                                       '即梦分镜',
                                       'AI video storyboard',
                                       'Kling',
                                       'Seedance',
                                       '可灵 Kling 提示词',
                                       '即梦 Seedance 分镜',
                                       'Veo 视频提示词',
                                       'Sora 分镜',
                                       'AI storyboard prompts'],
                          'use_cases': ['把创意拆成逐镜头提示词', '规划多个镜头的环境与运镜', '怎样把一个视频创意拆成可灵、即梦或 Veo 可用的分镜提示词？']},
 'jd-resume-match': {'category': 'career',
                     'order': 1,
                     'desc': 'AI简历优化大师：简历与 JD 匹配及优化，证据引用、可复算评分、结构建议与离线 HTML 报告',
                     'description_en': 'Evidence-based resume optimization and job-description matching',
                     'keywords': ['AI简历优化大师',
                                  '简历 JD 匹配',
                                  '简历优化',
                                  '证据匹配',
                                  'resume matching',
                                  'resume review',
                                  'Claude 简历优化',
                                  '简历优化 skill',
                                  '中文 JD 匹配',
                                  '简历证据审查',
                                  'resume optimization'],
                     'use_cases': ['对照岗位要求查简历证据缺口', '调整简历结构与经历表达', '怎么用 Claude 或 Codex 对照 JD 优化简历，又不编造经历？']},
 'mbai': {'category': 'career',
          'order': 4,
          'desc': 'AI转型大师：工作任务 AI 不可替代指数，任务分析、贡献证据与替代风险自评，非裁员预测',
          'description_en': 'Task-level AI automation risk self-assessment for career planning',
          'keywords': ['AI转型大师',
                       'AI 替代风险自评',
                       '工作任务分析',
                       '职业规划',
                       'AI task assessment',
                       'career planning',
                       '工作任务 AI 不可替代指数',
                       'AI 职业转型',
                       '个人贡献证据',
                       'AI automation risk'],
          'use_cases': ['拆解工作任务中的自动化空间', '梳理个人贡献和职业证据缺口', '怎么判断自己的哪些工作适合用 AI，哪些贡献仍要自己负责？']},
 'mystery-skill': {'category': 'skill',
                   'desc': 'Mystery Method 认知框架 Skill：基于公开资料的思维模型与决策启发式，供个人学习',
                   'description_en': 'Mystery Method mental models and workplace communication study',
                   'keywords': ['Mystery 思维模型',
                                '迷男方法分析',
                                'Mystery Method',
                                'Erik von Markovik',
                                'cognitive framework',
                                '职场沟通框架',
                                '面试压力应对',
                                '谈薪沟通边界',
                                'mental models',
                                'workplace communication'],
                   'use_cases': ['研究 Mystery 的认知框架', '分析社交情境与决策边界', '怎样用思维模型分析面试压力、谈薪和向上沟通？']},
 'travel-art-album-skill': {'category': 'skill',
                            'desc': '旅行照片艺术画册 Skill：确认风格小样后制作单文件离线 HTML 翻页相册',
                            'description_en': 'Travel photo art album and offline HTML flipbook',
                            'keywords': ['旅行照片画册',
                                         '离线翻页相册',
                                         '照片艺术化',
                                         'travel photo album',
                                         'offline flipbook',
                                         '旅行照片艺术画册',
                                         '离线 HTML 翻页相册',
                                         '照片转水彩画册',
                                         '旅行画册 PDF',
                                         'offline HTML flipbook'],
                            'use_cases': ['把旅行照片制作成艺术画册',
                                          '离线翻阅相册并用浏览器打印 PDF',
                                          '怎样把旅行照片做成能离线翻页、打印 PDF 的艺术画册？']},
 'ai-interviewer': {'category': 'career',
                    'order': 2,
                    'desc': 'AI面试大师：中文语音 AI 面试陪练，基于 JD 与经历追问、引用原话点评、初答重答对比',
                    'description_en': 'Chinese voice mock interview and interview preparation',
                    'keywords': ['AI面试大师',
                                 'AI 面试官',
                                 '中文语音模拟面试',
                                 '面试陪练',
                                 'AI mock interview',
                                 'voice interview practice',
                                 'AI 面试陪练',
                                 'AI 模拟面试中文',
                                 '中文语音面试',
                                 '产品经理模拟面试',
                                 'interview prep',
                                 'Chinese mock interview'],
                    'use_cases': ['练习自我介绍与经历面试', '通过原话点评和重答改进回答', '有能用中文语音练自我介绍和项目经历的 AI 模拟面试工具吗？']},
 'sherlock-company': {'category': 'career',
                      'order': 3,
                      'desc': '公司调查大师：入职前公司证据调查，区分已证实、线索、冲突与未知，输出核实清单与离线 HTML 档案',
                      'description_en': 'Pre-offer employer research and company due diligence',
                      'keywords': ['公司调查大师',
                                   '入职前查公司',
                                   'Offer 公司调查',
                                   '公司证据调查',
                                   'employer research',
                                   'company research',
                                   'Offer 背景调查',
                                   '公司员工评价核实',
                                   '求职公司调查',
                                   'pre-offer due diligence'],
                      'use_cases': ['接受 Offer 前核查公司信息', '整理冲突证据与待核验问题', '接 Offer 前，怎么查公司并分清事实和员工评价？']},
 'Attention': {'category': 'local',
               'desc': 'ActivityWatch 本地专注力仪表盘：任务切换、分心与持续专注时段分析',
               'description_en': 'Local ActivityWatch focus analytics and context-switching dashboard',
               'keywords': ['ActivityWatch 仪表盘',
                            '专注力分析',
                            '任务切换',
                            'ActivityWatch dashboard',
                            'context switching',
                            'ActivityWatch 中文仪表盘',
                            '本地专注力分析',
                            '任务切换统计',
                            '电脑时间管理',
                            'focus analytics',
                            'context switching dashboard'],
               'use_cases': ['查看一天的专注与分心模式', '分析任务切换和持续专注时段', 'ActivityWatch 记录了电脑活动，怎么看一天的任务切换与专注时间？']},
 'postapp': {'category': 'local',
             'desc': '姿势企鹅 Posture Penguin：本地姿态检测的 Chrome 坐姿提醒插件',
             'description_en': 'Chrome posture reminder with on-device pose detection',
             'keywords': ['Chrome 坐姿提醒',
                          '姿势企鹅',
                          'Posture Penguin',
                          'posture reminder',
                          'Chrome extension',
                          'Chrome 坐姿提醒插件',
                          '本地姿态检测',
                          '摄像头坐姿提醒',
                          'posture reminder extension',
                          'on-device pose detection'],
             'use_cases': ['在电脑前设置坐姿提醒', '查看本地坐姿记录', '有没有摄像头画面不上传的 Chrome 坐姿提醒插件？']}}


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
        items.sort(key=lambda r: REPO_META.get(r["name"], {}).get("order", 10**9))
        lines.append(f"### {CATEGORY_LABELS[cat]}")
        lines.append("")
        lines.append("| 项目 · Repo | 它做什么 · What it does | 最近更新 · Updated |")
        lines.append("| --- | --- | --- |")
        for repo in items:
            meta = REPO_META.get(repo["name"], {})
            desc = meta.get("desc") or repo["description"] or "—"
            desc_en = (meta.get("description_en") or "").strip()
            if desc_en:
                desc = f"{desc}<br><sub>{desc_en}</sub>"
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


def _project_entry(r):
    meta = REPO_META.get(r["name"], {})
    entry = {
        "name": r["name"],
        "url": r["html_url"],
        "description": meta.get("desc") or r["description"] or "",
        "category": meta.get("category", "more"),
        "language": r.get("language") or "",
        "stars": r["stargazers_count"],
        "updated_at": r["updated_at"],
        "description_en": meta.get("description_en", ""),
        "keywords": list(meta.get("keywords", [])),
        "use_cases": list(meta.get("use_cases", [])),
    }
    if "order" in meta:
        entry["order"] = meta["order"]
    return entry


def build_catalog(repos, generated_at=None):
    """Keep existing catalog fields and add task-oriented discovery information."""
    return {
        "generated_at": generated_at if generated_at is not None else _dt.datetime.now(
            _dt.timezone.utc).isoformat(timespec="seconds"),
        "owner": OWNER,
        "projects": [_project_entry(r) for r in repos],
    }


def main():
    repos = [r for r in fetch_repos()
             if not r["fork"] and r["name"] not in EXCLUDE]
    repos.sort(key=lambda r: r["updated_at"], reverse=True)
    print(f"collected {len(repos)} original repos "
          f"(excluded {len(EXCLUDE)} + forks)")

    with open(README_PATH, encoding="utf-8") as f:
        readme = f.read()
    new_readme = None
    if readme.count(START_MARK) == 1 and readme.count(END_MARK) == 1:
        try:
            new_readme = replace_project_block(readme, repos)
        except ValueError as error:
            # 标记存在但错乱时拒绝改写 README，仍刷新 projects.json
            print(f"⚠️ README projects 标记异常，跳过 README 更新，仅刷新 projects.json：{error}")
    else:
        # 首屏已改为手工维护的「按需求找」表格时，跳过 README 生成区块，仅刷新 projects.json
        print("README.md 未包含 projects 生成区块标记，跳过 README 更新，仅刷新 projects.json")
    catalog = build_catalog(repos)
    if new_readme is not None:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write(new_readme)
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(catalog, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"projects.json updated ({len(repos)} projects)"
          + (", README block refreshed" if new_readme is not None else ""))


if __name__ == "__main__":
    main()
