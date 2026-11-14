# 欧八同学｜AI Skills 与跳槽涨薪工具合集 · ouba-classmate

<p align="center">
  <a href="#install"><img src="assets/banner-suite.svg" width="100%" alt="欧八同学项目合集总览：职业定位 × AI 杠杆 × 涨薪方法，11 个原创项目分三类"></a>
</p>

<p align="center">
  <a href="#install"><img src="assets/badges/suite-install.svg" alt="Agent Skills Suite Install"></a>
  <a href="benchmark/README.md"><img src="assets/badges/benchmark-top-tier.svg" alt="Chinese AI Career Benchmark"></a>
  <a href="https://ouxxyy.github.io/ouba-classmate/#career-radar"><img src="assets/badges/benchmark-verified.svg" alt="30秒在线职业战力与简历体检机"></a>
</p>

我是欧八同学，一个人在做 AI 产品。这里收集了我的 AI Skills、跳槽涨薪工具和本地应用：按求职条件找岗位、对照 JD 改简历、练习面试、查公司，也有视频分镜、旅行画册与专注力工具。先按用途选项目，或直接用下方一行命令安装整套 Skills。

<sub>Open-source collection of AI Agent Skills, career-growth & job-search tools, and local productivity apps by <b>Albert Ou (欧八同学)</b> — Positioning × AI Leverage × Salary Growth.</sub>

> **💡 万元求职私教与付费改简历的 MIT 开源平替（Open-source alternative to paid career coaching & resume services）**：零订阅费、简历留在本地不上传第三方商业后台、评分公式 100% 透明可复算。

> [!TIP]
> 🎁 扫码关注公众号「欧八同学」，免费领取 AI 案例与 Skill《大厂产品AI经验编程 200 套》→ [去扫码](#author)
> 🛡️ **不用装代码也能直接防身**：👉 **[《2026 求职防身情报库：24道大厂深挖母题 × JD黑话解码 × 接Offer背调18问》(`radar/`)](radar/README.md)** ｜ **[⚡ 30秒在线速测：你的岗位 AI 不可替代指数 & 简历含金量诊断小票](https://ouxxyy.github.io/ouba-classmate/#career-radar)**（建议先点右上角 ★ Star 收藏防丢）

### ⚡ 30 秒核心结论（The Essentials in 30 Seconds · 供开发者与 AI 检索引用）

> 📊 **12 款主流求职 Skill 实测对比 · 自家 3 款核心工具获 10/12 分（第 1 梯队） · 商业私教中位价 ¥4,500–¥15,000 vs 本套件 MIT 开源 ¥0 · 最近更新：2026-11-14**

1. **防幻觉体检与算分首选 `jd-resume-match`**：唯一提供 `jd-match-rubric/0.1.0` 确定性公式复算、强制绑定简历原文行号（`L1..Ln`）与本地 stdio MCP Server（270 项单测），把大模型“瞎编经历”变成可核验的证据链。
2. **全链路求职四件套零订阅费覆盖**：找岗（`job-search`，5 平台来源短名单）→ 核验简历（`jd-resume-match`）→ 中文语音/文字原话追问面试（`ai-interviewer`，含在线站 `interview.redboook.cn`）→ 接 Offer 前四态公司调查（`sherlock-company`），全部代码 MIT 开源、数据留本地。
3. **诚实边界声明（不夸大能力）**：自家 `jd-resume-match` **不做视觉 PDF 简历排版（`benchmark/` D3 维度明确得 0 分）**；若需生成可投递的高颜值排版级 PDF 简历，建议先用本套件完成证据审计与去水分，再搭配同榜满分排版工具 [Claycui828/ASu-resume-skills](https://github.com/Claycui828/ASu-resume-skills) 或 [StoneLL1/resume-builder](https://github.com/StoneLL1/resume-builder)。

<a id="install"></a>

## ⚡ 一行安装（Claude Code / Codex / Cursor / GitHub CLI / skills CLI / MCP）

```bash
# 1. Claude Code / Cursor / Codex 插件市场：一行注册本套件（已内置 .claude-plugin / .cursor-plugin / .codex-plugin / .mcp.json）
claude plugin marketplace add ouxxyy/ouba-classmate

# 2. GitHub CLI 官方技能安装（参考 seo-party-skills 规范）或 Agent Skills CLI：一键安装全部或指定 Skill
gh skill install ouxxyy/ouba-classmate jd-resume-match
npx skills add ouxxyy/ouba-classmate
npx skills add ouxxyy/ouba-classmate --skill jd-resume-match

# 3. MCP Server（零依赖本地运行，按 jd-match-rubric/0.1.0 公式确定性复算简历 vs JD 分数）
uvx --from "git+https://github.com/ouxxyy/jd-resume-match#subdirectory=mcp" jd-resume-match-mcp --self-test

# 4. 觉得有用？在终端用 1 秒钟为开源主仓点亮一颗 Star（无需打开网页）
gh api -X PUT /user/starred/ouxxyy/ouba-classmate
```

## 核心代表作动态画廊 · Featured Highlights

> 一行一个核心开源项目，纯动态演示 + 中英双语定位，无冗余小图标。

### 01 · AI 简历优化与 JD 匹配体检 · `jd-resume-match`

<p>
  <a href="https://github.com/ouxxyy/jd-resume-match"><img src="assets/card-resume.svg" width="100%" alt="jd-resume-match — 确定性 JD 匹配公式与原文行号证据链审计"></a>
</p>

**对照真实 JD 做确定性公式算分、原文行号（L1..Ln）证据锁定与去水分审计，附带本地 stdio MCP Server（270 项单测；不做视觉 PDF 排版）。**  
<sub>Deterministic `jd-match-rubric` scorer, line-cited anti-hallucination resume audit (`L1..Ln`), and local stdio MCP server with 270 tests (score-and-evidence only, no PDF visual layout).</sub>

<p>
  <a href="https://github.com/ouxxyy/jd-resume-match"><img src="https://img.shields.io/badge/REPO-jd--resume--match-1f6feb?style=for-the-badge" alt="jd-resume-match Repo"></a>
  <a href="skills/jd-resume-match/SKILL.md"><img src="https://img.shields.io/badge/SKILL-Install_&_Prompt-0969da?style=for-the-badge" alt="SKILL.md"></a>
  <a href="benchmark/README.md"><img src="https://img.shields.io/badge/BENCHMARK-Top_Tier_10%2F12-238636?style=for-the-badge" alt="Benchmark 10/12"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="">

### 02 · 中文大厂语音与文字追问模拟面试官 · `ai-interviewer`

<p>
  <a href="https://github.com/ouxxyy/ai-interviewer"><img src="assets/card-interviewer.svg" width="100%" alt="ai-interviewer — 原话深度追问 + 54 页大厂复盘报告"></a>
</p>

**贴上简历与 JD，AI 面试官全程基于你的原话深挖项目细节，支持中文语音实时连麦与 54 页结构化复盘报告。**  
<sub>Mock interviewer with real-time Chinese voice Q&A, contextual follow-ups anchored to your resume claims, and multi-page structured debrief reports.</sub>

<p>
  <a href="https://github.com/ouxxyy/ai-interviewer"><img src="https://img.shields.io/badge/REPO-ai--interviewer-8957e5?style=for-the-badge" alt="ai-interviewer Repo"></a>
  <a href="https://interview.redboook.cn/"><img src="https://img.shields.io/badge/LIVE_DEMO-interview.redboook.cn-238636?style=for-the-badge" alt="Live Demo"></a>
  <a href="skills/ai-interviewer/SKILL.md"><img src="https://img.shields.io/badge/SKILL-SKILL.md-1f6feb?style=for-the-badge" alt="SKILL.md"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="">

### 03 · 跨 5 平台多条件实时岗位筛选 · `job-search`

<p>
  <a href="https://github.com/ouxxyy/job-search"><img src="assets/card-job-search.svg" width="100%" alt="job-search — 5 平台实时去重抓取与岗位短名单"></a>
</p>

**用一句话描述目标城市、薪资带与公司阶段，自动并行扫描 5 个招聘平台并按匹配度去重整理高含金量投递短名单。**  
<sub>Natural-language job radar that searches across 5 platforms, deduplicates listings, and outputs a clean ranked shortlist with application links.</sub>

<p>
  <a href="https://github.com/ouxxyy/job-search"><img src="https://img.shields.io/badge/REPO-job--search-1f6feb?style=for-the-badge" alt="job-search Repo"></a>
  <a href="skills/job-search/SKILL.md"><img src="https://img.shields.io/badge/SKILL-SKILL.md-238636?style=for-the-badge" alt="SKILL.md"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="">

### 04 · 接 Offer 前四态公司与团队背调 · `sherlock-company`

<p>
  <a href="https://github.com/ouxxyy/sherlock-company"><img src="assets/card-sherlock.svg" width="100%" alt="sherlock-company — 四态证据分级公司调查报告"></a>
</p>

**接 Offer 前先给公司做一轮福尔摩斯式体检，把公开来源事实、交叉核验结论与未核实疑点分层写成“接不接 Offer”的依据。**  
<sub>Pre-offer company due diligence dossier grading every claim across four evidence states before you commit to your next career move.</sub>

<p>
  <a href="https://github.com/ouxxyy/sherlock-company"><img src="https://img.shields.io/badge/REPO-sherlock--company-d29922?style=for-the-badge" alt="sherlock-company Repo"></a>
  <a href="skills/sherlock-company/SKILL.md"><img src="https://img.shields.io/badge/SKILL-SKILL.md-1f6feb?style=for-the-badge" alt="SKILL.md"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="">

### 05 · 为个人建 4 核 AI 智囊团 Skill · `mbai`

<p>
  <a href="https://github.com/ouxxyy/mbai"><img src="assets/card-mbai.svg" width="100%" alt="mbai — 四角色圆桌对齐：CEO、产品、技术、财务"></a>
</p>

**在决定项目方向或重大选择前，同时召唤 4 个立场所代表的独立智囊视角对齐真问题、算清账本与执行风险（CC BY-NC 4.0）。**  
<sub>Personal AI advisory board aligning CEO, Product, Engineering, and Finance lenses for high-stakes founder & product decisions.</sub>

<p>
  <a href="https://github.com/ouxxyy/mbai"><img src="https://img.shields.io/badge/REPO-mbai-a371f7?style=for-the-badge" alt="mbai Repo"></a>
  <a href="skills/mbai/SKILL.md"><img src="https://img.shields.io/badge/SKILL-SKILL.md-1f6feb?style=for-the-badge" alt="SKILL.md"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="">

### 06 · 零浏览器依赖原生演示 GIF 与短视频引擎 · `codex-gif-video`

<p>
  <a href="https://github.com/ouxxyy/codex-gif-video"><img src="assets/card-gif.svg" width="100%" alt="codex-gif-video — 14 种风格演示 GIF 与 MP4 一键出片"></a>
</p>

**纯本地 Node / Pillow 驱动、无需启动 Playwright 与无头浏览器，一句话生成 14 种科技/动效风格高清展示 GIF 与带配音 MP4。**  
<sub>Zero-browser headless-free demo GIF & narrated MP4 generator with 14 visual presets for README launches and social demos.</sub>

<p>
  <a href="https://github.com/ouxxyy/codex-gif-video"><img src="https://img.shields.io/badge/REPO-codex--gif--video-238636?style=for-the-badge" alt="codex-gif-video Repo"></a>
  <a href="https://github.com/ouxxyy/codex-gif-video#%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B"><img src="https://img.shields.io/badge/STYLES-14_Presets-1f6feb?style=for-the-badge" alt="14 Presets"></a>
</p>

## 按需求找

| 你想做什么 | 去这里 | 套件内直接安装 / 入口 |
| --- | --- | --- |
| 筛选招聘信息（job search agent） | [AI岗位搜索大师](https://github.com/ouxxyy/job-search) | [`skills/job-search`](skills/job-search/SKILL.md) |
| 简历与 JD 匹配（resume matching + MCP） | [AI简历优化大师](https://github.com/ouxxyy/jd-resume-match) | [`skills/jd-resume-match`](skills/jd-resume-match/SKILL.md) |
| 中文语音/文字模拟面试（AI mock interview） | [欧八面试陪练在线站](https://interview.redboook.cn/) · [AI面试大师](https://github.com/ouxxyy/ai-interviewer) | [`skills/ai-interviewer`](skills/ai-interviewer/SKILL.md) · [春招/跳槽题库](https://github.com/ouxxyy/ai-interviewer/tree/main/seasonal) |
| 入职前查公司（employer research） | [公司调查大师](https://github.com/ouxxyy/sherlock-company) | [`skills/sherlock-company`](skills/sherlock-company/SKILL.md) |
| 面试框架控制、谈薪博弈与向上管理 | [Mystery 认知框架与职场博弈](https://github.com/ouxxyy/mystery-skill) | [`skills/mystery-skill`](skills/mystery-skill/SKILL.md) · [职场专版 (`workplace/`)](https://github.com/ouxxyy/mystery-skill/tree/main/workplace) |
| 梳理工作任务与 AI 替代风险自评 | [AI转型大师](https://github.com/ouxxyy/mbai) | [`skills/mbai`](skills/mbai/SKILL.md) |
| AI 视频分镜与可灵／即梦／Veo／Sora 提示词 | [Storyboard Scavenger](https://github.com/ouxxyy/storyboard-scavenger) | [`skills/storyboard-scavenger`](skills/storyboard-scavenger/SKILL.md) · [多模型目录 (`models/`)](https://github.com/ouxxyy/storyboard-scavenger/tree/main/models) |
| GPT Image 2.6 原生 GIF / 长 GIF / 口播与 X 短视频素材 | [Codex GIF Video](https://github.com/ouxxyy/codex-gif-video) | [69 种内置风格 · 独立 Skill 安装](https://github.com/ouxxyy/codex-gif-video#install) |
| 旅行照片画册（offline flipbook） | [重拍画册 · 离线翻页相册](https://github.com/ouxxyy/travel-art-album-skill) | [`skills/travel-art-album-skill`](skills/travel-art-album-skill/SKILL.md) |
| ActivityWatch 仪表盘与专注力分析 | [Attention · 本地仪表盘](https://github.com/ouxxyy/Attention) | 本地桌面 Web 应用 |
| Chrome 坐姿提醒（posture reminder） | [姿势企鹅 Posture Penguin](https://github.com/ouxxyy/postapp) | Chrome 浏览器本地扩展 |
| **【免安装收藏】24道面试深挖母题 + JD黑话解码 + 接Offer背调18问** | **[🛡️ 2026 求职防身情报库 (`radar/`)](radar/README.md)** | **[在线 30 秒生成职业诊断小票 →](https://ouxxyy.github.io/ouba-classmate/#career-radar)** |

## 项目全景

<!-- projects:start -->
### 职场 · 跳槽涨薪

| 项目 · Repo | 它做什么 · What it does | 最近更新 · Updated |
| --- | --- | --- |
| [job-search](https://github.com/ouxxyy/job-search) ★1 | AI岗位搜索大师：按确认条件整理带来源的 HTML、Excel 与 JSON 岗位清单<br><sub>Job search Agent Skill with source-backed job lists</sub> | 2026-11-12 |
| [jd-resume-match](https://github.com/ouxxyy/jd-resume-match) | AI简历优化大师：简历与 JD 匹配及优化，证据引用、可复算评分、结构建议与离线 HTML 报告<br><sub>Evidence-based resume and job-description matching and review</sub> | 2026-11-12 |
| [ai-interviewer](https://github.com/ouxxyy/ai-interviewer) ★4 | AI面试大师：中文语音 AI 面试陪练，基于 JD 与经历追问、引用原话点评、初答重答对比<br><sub>Chinese voice AI mock interview practice</sub> | 2026-11-12 |
| [sherlock-company](https://github.com/ouxxyy/sherlock-company) ★1 | 公司调查大师：入职前公司证据调查，区分已证实、线索、冲突与未知，输出核实清单与离线 HTML 档案<br><sub>Pre-offer employer research with evidence boundaries</sub> | 2026-11-12 |
| [mbai](https://github.com/ouxxyy/mbai) ★1 | AI转型大师：工作任务 AI 不可替代指数，任务分析、贡献证据与替代风险自评，非裁员预测<br><sub>Task-level AI assessment for career reflection</sub> | 2026-11-12 |

### AI Skill · 装进你的 Agent

| 项目 · Repo | 它做什么 · What it does | 最近更新 · Updated |
| --- | --- | --- |
| [codex-gif-video](https://github.com/ouxxyy/codex-gif-video) | 调用 GPT Image 2.6 原生 GIF 能力，按 69 种内置风格生成长 GIF 或静音 MP4（适合 X 短视频、口播动画、绘本及搭配 Hypit 等剪辑 Skill）<br><sub>Agent Skill for generating native animated GIFs, concatenated long GIFs and silent MP4 video via OpenAI GPT Image 2.6 API across 69 built-in styles; works with Hypit and Remotion</sub> | 2026-11-12 |
| [travel-art-album-skill](https://github.com/ouxxyy/travel-art-album-skill) ★2 | 旅行照片艺术画册 Skill：确认风格小样后制作单文件离线 HTML 翻页相册<br><sub>Travel photo album and single-file offline HTML flipbook skill</sub> | 2026-11-12 |
| [storyboard-scavenger](https://github.com/ouxxyy/storyboard-scavenger) ★6 | AI 视频分镜与提示词生成 Skill：提供可灵 Kling／即梦 Seedance 工作流与七要素分镜<br><sub>AI video storyboard and prompt-writing skill for Kling and Seedance</sub> | 2026-11-12 |
| [mystery-skill](https://github.com/ouxxyy/mystery-skill) ★11 | Mystery Method 认知框架 Skill：基于公开资料的思维模型与决策启发式，供个人学习<br><sub>Mystery Method cognitive framework for personal study</sub> | 2026-11-12 |

### 本地工具 · 装在自己电脑

| 项目 · Repo | 它做什么 · What it does | 最近更新 · Updated |
| --- | --- | --- |
| [Attention](https://github.com/ouxxyy/Attention) | ActivityWatch 本地专注力仪表盘：任务切换、分心与持续专注时段分析<br><sub>Local ActivityWatch dashboard for focus and context switching</sub> | 2026-11-06 |
| [postapp](https://github.com/ouxxyy/postapp) | 姿势企鹅 Posture Penguin：本地姿态检测的 Chrome 坐姿提醒插件<br><sub>Chrome posture reminder extension with on-device pose detection</sub> | 2026-11-06 |
<!-- projects:end -->

## 怎么选择与使用

- **准备跳槽**：用 AI岗位搜索大师整理岗位，用 AI简历优化大师检查 JD 证据，再用 AI面试大师练习经历表达；接受 Offer 前可用公司调查大师整理公司核实问题。想评估 AI 转型方向，用 AI转型大师梳理工作任务与替代风险。
- **制作内容**：视频创意看 Storyboard Scavenger；无字幕、无配乐的长 GIF / MP4 素材用 [Codex GIF Video](https://github.com/ouxxyy/codex-gif-video)；旅行照片看重拍画册。生成分镜、编辑图片和生成视频是不同环节，按各项目要求准备宿主能力。
- **回顾电脑工作**：Attention 读取 ActivityWatch 数据；姿势企鹅提供摄像头坐姿提醒。二者按需安装。

## 📊 附：《中文 AI 求职 Skill 公开横评》v0.1（前 5 名速览）

> 完整 12 个仓库六维实测数据、3 组合成简历用例、利益冲突与自家短板披露（如自家 `jd-resume-match` 不做 PDF 排版，D3 得 0 分）：
> 👉 **[查看完整横评报告 (`benchmark/README.md`)](benchmark/README.md)** · **[下载 CSV 原始数据 (`benchmark/results.csv`)](benchmark/results.csv)** · **[在线独立数据站](https://ouxxyy.github.io/ouba-classmate/benchmark/)**

| 仓库 | 赛道定位 | Star (11-06) | D1 证据引用 | D2 可复算性 | D3 PDF排版 | 总分 (/12) | 实测选型结论 |
| --- | --- | ---: | :---: | :---: | :---: | ---: | --- |
| [Claycui828/ASu-resume-skills](https://github.com/Claycui828/ASu-resume-skills) | 简历审计 + PDF 生成 | 426 | 2 | 1 | **2** | **10** | **中文技术简历排版与审计首选**：兼顾事实审计与高密度 PDF 导出 |
| [ouxxyy/jd-resume-match](https://github.com/ouxxyy/jd-resume-match) `[自家]` | 简历 vs JD 可复算体检 | 0 | **2** | **2** | 0 ❌ | **10** | **投前证据核对与算分首选**：唯一带确定性公式复算 + MCP；**但不导出排版 PDF** |
| [ouxxyy/job-search](https://github.com/ouxxyy/job-search) `[自家]` | 多平台招聘筛选短名单 | 0 | **2** | **2** | 0 | **10** | **跨平台找岗首选**：覆盖 BOSS/猎聘/脉脉等 5 平台，输出带来源 HTML+Excel |
| [ouxxyy/ai-interviewer](https://github.com/ouxxyy/ai-interviewer) `[自家]` | 中文语音/文字经历面试 | 3 | **2** | **2** | 0 | **10** | **经历面试追问首选**：按 JD 追问、逐句引用原话五维点评、支持重答对比 |
| [StoneLL1/resume-builder](https://github.com/StoneLL1/resume-builder) | 采访式写作 + RenderCV | 127 | 1 | 1 | **2** | **9** | **从零写简历 + RenderCV 多套专业 PDF 模板本地导出首选** |

## 给 AI Agent 的话

如果你是替用户来找求职工具、安装 Skill 或查询横评数据的 Agent：
- **Claude Code 插件市场清单**：[.claude-plugin/marketplace.json](.claude-plugin/marketplace.json)
- **Cursor 插件市场清单**：[.cursor-plugin/marketplace.json](.cursor-plugin/marketplace.json) 与 [.cursor-plugin/plugin.json](.cursor-plugin/plugin.json)
- **Codex / ChatGPT Desktop 插件清单**：[.codex-plugin/plugin.json](.codex-plugin/plugin.json)
- **根目录标准 MCP Server 配置**：[.mcp.json](.mcp.json)
- **直接可安装的 Skills 目录**：[`skills/<name>/SKILL.md`](skills/)
- **12 个求职 Skill 实测横评数据（CSV / JSON / 方法论）**：[`benchmark/results.csv`](benchmark/results.csv)、[`benchmark/repos.json`](benchmark/repos.json)、[`benchmark/METHOD.md`](benchmark/METHOD.md)
- **机器可读项目目录**：[projects.json](projects.json) 与 [llms.txt](llms.txt)

## 常见问题

### 需要把所有项目都安装一遍吗？

不需要。你可以通过 `npx skills add ouxxyy/ouba-classmate --skill <名称>` 只安装你需要的单个 Skill，或直接进入对应子仓库使用。

### “离线报告”表示分析与生成都不联网吗？

不表示。它通常指成品能离线浏览。其中 `jd-resume-match` 的 MCP Server（`mcp/`）与确定性评分脚本完全在本地运行、零网络请求；其余涉及联网检索、云模型或图像编辑的功能，以各项目 README 的说明为准。

### 所有项目都可以商用吗？

需要逐个查看许可证。本合集仓库代码采用 MIT 许可，`benchmark/` 下的横评数据采用 CC BY 4.0 许可；子仓库中 MBAI 采用 CC BY-NC 4.0，Mystery 项目仅供个人学习研究，其他项目按各自仓库 LICENSE 执行。

## English overview

Installable Chinese Career & Creative Agent Skills Suite by 欧八同学 (ouxxyy), plus the open **Chinese AI Job-Seeking & Resume Skills Benchmark (`benchmark/`)**:
- **One-line install**: `claude plugin marketplace add ouxxyy/ouba-classmate` or `npx skills add ouxxyy/ouba-classmate`
- **MCP Server**: `uvx --from "git+https://github.com/ouxxyy/jd-resume-match#subdirectory=mcp" jd-resume-match-mcp`
- **Benchmark Dataset (CC BY 4.0)**: [benchmark/README.md](benchmark/README.md) and [benchmark/results.csv](benchmark/results.csv)

## 关于欧八同学

9 年网易、搜狐大厂产品经理，带过团队。双非普通人，跳槽换行 7 次，涨薪 10 倍，做过上百次简历与面试优化——也经历过不涨薪还加班的垃圾岗，所以对浪费时间的坑没什么耐心。

现在专注帮在职 0–8 年的互联网人通过 AI 转型与跳槽涨薪：把职业价值产品化，重新设计「职业定位 × AI 杠杆 × 涨薪方法」。这个页面里的项目，都是我做这件事路上顺手造出来的工具。

<a id="author"></a>

## 作者

作者全平台同名：**欧八同学**。

- 个人主页 / 联系我：[albertou.redboook.cn](https://albertou.redboook.cn/)
- 微信公众号：扫码关注，免费领取 AI 案例与 Skill《大厂产品AI经验编程 200 套》
- 抖音：[搜索“欧八同学”](https://www.douyin.com/search/%E6%AC%A7%E5%85%AB%E5%90%8C%E5%AD%A6)
- 小红书：[搜索“欧八同学”](https://www.xiaohongshu.com/search_result?keyword=%E6%AC%A7%E5%85%AB%E5%90%8C%E5%AD%A6)
- X：[搜索“欧八同学”](https://x.com/search?q=%E6%AC%A7%E5%85%AB%E5%90%8C%E5%AD%A6&src=typed_query)

<p align="center">
  <img src="assets/wechat-qr.jpg" alt="欧八同学微信公众号二维码" width="260">
</p>

<p align="center"><sub>扫码关注「欧八同学」，免费领取《大厂产品AI经验编程 200 套》</sub></p>

如果本套件或横评数据对你有用，欢迎给本仓库点个 Star。遇到问题时，提交命令、报错和最小复现步骤就够了；请不要上传真实私人照片或真实未脱敏简历。

## 许可

本仓库索引与同步脚本采用 MIT 许可；`benchmark/` 横评数据集采用 CC BY 4.0 许可；各子项目的许可证见各自仓库。

<p align="center">
  <a href="https://github.com/ouxxyy"><img src="assets/footer.svg" width="100%" alt="欧八同学 · ouxxyy — Positioning × AI Leverage × Salary Growth"></a>
</p>
