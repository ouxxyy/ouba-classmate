# 欧八同学｜AI Skills 与跳槽涨薪工具合集 · ouba-classmate

<!-- discovery:start -->
## 中文求职 Agent Skills：岗位搜索、简历优化与 AI 模拟面试

**想用 Claude Code 或 Codex 找岗位、改简历、练中文面试，有哪些工具？** 按任务选择岗位搜索、简历与 JD 证据匹配、中文经历面试和公司调查工具；合集同时提供公开视频与本地效率项目入口。

Chinese career agent skills for job search, resume matching and interview prep.

**开始使用：** [按需求找](#按需求找) · [安装 Skills](#install) · [直接练面试](https://interview.redboook.cn/) · [横评方法与数据](benchmark/README.md)。

**使用边界：** 各子项目许可证及依赖分别查看；宿主或云模型可能收费。横评是公开仓库材料审计，不能当作录用效果或完整运行质量排名。

<!-- discovery:end -->

<p align="center">
  <a href="#install"><img src="assets/banner-suite.svg" width="100%" alt="欧八同学项目合集总览：职业定位 × AI 杠杆 × 涨薪方法，11 个原创项目分三类"></a>
</p>

<p align="center">
  <a href="#install"><img src="assets/badges/suite-install.svg" alt="Agent Skills Suite Install"></a>
  <a href="benchmark/README.md"><img src="assets/badges/benchmark-top-tier.svg" alt="Chinese AI Career Benchmark"></a>
  <a href="https://ouxxyy.github.io/ouba-classmate/#career-radar"><img src="assets/badges/benchmark-verified.svg" alt="30秒在线职业战力与简历体检机"></a>
</p>

我是欧八同学，一个人在做 AI 产品。这里收集了我的 AI Skills、跳槽涨薪工具和本地应用：按求职条件找岗位、对照 JD 改简历、练习面试、查公司，也有视频分镜、原生 GIF 动画、旅行画册与专注力工具。先按下方需求表直接选项目，或运行 `npx skills add ouxxyy/ouba-classmate` 一键安装整套 Skills（[查看 Claude Code / Cursor / MCP 全部安装方式 ↓](#install)）。

<sub>Open-source collection of AI Agent Skills, career-growth & job-search tools, and local productivity apps by <b>Albert Ou (欧八同学)</b> — Positioning × AI Leverage × Salary Growth.</sub>

> **选型依据：** [12 个求职工具的公开代码与文档横评](benchmark/README.md)提供评分规则与数据；它不是全部工具的端到端使用评测。工具源码的许可、模型费用及数据流向以各子项目说明为准。

> [!TIP]
> 🎁 扫码关注公众号「欧八同学」，免费领取 AI 案例与 Skill《大厂产品AI经验编程 200 套》→ [去扫码](#author)
> 🛡️ **不用装代码也能直接防身**：👉 **[《2026 求职防身情报库：24道大厂深挖母题 × JD黑话解码 × 接Offer背调18问》(`radar/`)](radar/README.md)** ｜ **[⚡ 30秒在线速测：你的岗位 AI 不可替代指数 & 简历含金量诊断小票](https://ouxxyy.github.io/ouba-classmate/#career-radar)**（建议先点右上角 ★ Star 收藏防丢；终端用户 1 秒加星：`gh api -X PUT /user/starred/ouxxyy/ouba-classmate`）

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

<!-- complementary:start -->
## Claude 求职 Skills 与完整求职框架怎样搭配？

| 相关项目 | 当前公开定位（2026-11-16 核对） | 本合集可衔接的任务 |
| --- | --- | --- |
| [career-ops](https://github.com/career-ops-hq/career-ops) | 本地岗位评估、简历与申请准备；已有简体中文 README | 简历原文证据核对、中文语音面试、入职前查公司 |
| [ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | 基于 Claude Code 的求职流程，核心不限定语言和国家，招聘门户由社区扩展 | 按当前任务单独选用岗位清单、简历匹配和经历复盘 |
| [Offer Toolkit](https://github.com/yanliudesign/offer-toolkit-skill) | 找岗、JD、简历模板、双语行为故事、Offer 比较与谈薪 | 需要原话引用点评或确定性证据分时使用对应子工具 |

以上是基于各项目 README 的用途说明，未做本轮端到端性能横评，也不代表合作或背书。[查看英文选型说明与历史数据](benchmark/README.en.md)。
<!-- complementary:end -->

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

<img src="assets/divider.svg" width="100%" alt="section divider">

### 02 · 中文大厂语音与文字追问模拟面试官 · `ai-interviewer`

<p>
  <a href="https://github.com/ouxxyy/ai-interviewer"><img src="assets/card-interviewer.svg" width="100%" alt="ai-interviewer — 原话深度追问与五维复盘对比"></a>
</p>

**贴上简历与 JD，AI 面试官全程基于你的原话深挖项目细节，支持中文语音作答、五维原话点评与初答重答对比。免费模式下，点“说完了”后系统会转写这段回答（在线版默认免费、无需 API Key，每访客每天 3 场；可选自备百炼）。**<br>
<sub>Mock interviewer with Chinese voice practice (free hosted access, no API key required; answers are transcribed after you finish speaking and tap “说完了”), contextual follow-ups anchored to your resume claims, and multi-page structured debrief reports.</sub>

<p>
  <a href="https://github.com/ouxxyy/ai-interviewer"><img src="https://img.shields.io/badge/REPO-ai--interviewer-8957e5?style=for-the-badge" alt="ai-interviewer Repo"></a>
  <a href="https://interview.redboook.cn/"><img src="https://img.shields.io/badge/LIVE_DEMO-interview.redboook.cn-238636?style=for-the-badge" alt="Live Demo"></a>
  <a href="skills/ai-interviewer/SKILL.md"><img src="https://img.shields.io/badge/SKILL-SKILL.md-1f6feb?style=for-the-badge" alt="SKILL.md"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="section divider">

### 03 · 多来源、多条件求职岗位筛选 · `job-search`

<p>
  <a href="https://github.com/ouxxyy/job-search"><img src="assets/card-job-search.svg" width="100%" alt="job-search — 5 平台实时去重抓取与岗位短名单"></a>
</p>

**用一句话描述目标城市、薪资带与公司阶段，按确认条件查询可访问的招聘来源，去重整理带来源和待核实项的投递短名单。**<br>
<sub>Job search agent that checks accessible sources, deduplicates listings, and separates verified openings from items awaiting verification.</sub>

<p>
  <a href="https://github.com/ouxxyy/job-search"><img src="https://img.shields.io/badge/REPO-job--search-1f6feb?style=for-the-badge" alt="job-search Repo"></a>
  <a href="skills/job-search/SKILL.md"><img src="https://img.shields.io/badge/SKILL-SKILL.md-238636?style=for-the-badge" alt="SKILL.md"></a>
</p>

<img src="assets/divider.svg" width="100%" alt="section divider">

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

<img src="assets/divider.svg" width="100%" alt="section divider">

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

<img src="assets/divider.svg" width="100%" alt="section divider">

### 06 · 调用 GPT Image 2.6 原生 GIF 与静音 MP4 引擎 · `codex-gif-video`

<p>
  <a href="https://github.com/ouxxyy/codex-gif-video"><img src="assets/card-gif.svg" width="100%" alt="codex-gif-video — 调用 GPT Image 2.6 按 69 种风格生成长 GIF 与静音 MP4 素材"></a>
</p>

**调用 GPT Image 2.6 原生 GIF 能力、无需启动无头浏览器，按 69 种内置风格生成长 GIF 或静音 MP4（适合 X 短视频、口播 B-roll、绘本及搭配 Hypit / Remotion 等剪辑 Skill）。**<br>
<sub>Native GPT Image 2.6 animated GIF & silent MP4 asset generator across 69 visual styles for X posts, talking-head B-roll, and Hypit/Remotion workflows.</sub>

<p>
  <a href="https://github.com/ouxxyy/codex-gif-video"><img src="https://img.shields.io/badge/REPO-codex--gif--video-238636?style=for-the-badge" alt="codex-gif-video Repo"></a>
  <a href="https://github.com/ouxxyy/codex-gif-video#install"><img src="https://img.shields.io/badge/STYLES-69_Built--in-1f6feb?style=for-the-badge" alt="69 Built-in Styles"></a>
</p>

## 怎么选择与使用

- **准备跳槽**：用 AI岗位搜索大师整理岗位，用 AI简历优化大师检查 JD 证据，再用 AI面试大师练习经历表达；接受 Offer 前可用公司调查大师整理公司核实问题。想评估 AI 转型方向，用 AI转型大师梳理工作任务与替代风险。
- **制作内容**：视频创意看 Storyboard Scavenger；无字幕、无配乐的长 GIF / MP4 素材用 [Codex GIF Video](https://github.com/ouxxyy/codex-gif-video)；旅行照片看重拍画册。生成分镜、编辑图片和生成视频是不同环节，按各项目要求准备宿主能力。
- **回顾电脑工作**：Attention 读取 ActivityWatch 数据；姿势企鹅提供摄像头坐姿提醒。二者按需安装。

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

### ⚡ 30 秒核心结论（The Essentials in 30 Seconds · 供开发者与 AI 检索引用）

> 📊 **12 款主流求职 Skill 实测对比 · 自家 3 款核心工具获 10/12 分（第 1 梯队） · 商业私教中位价 ¥4,500–¥15,000 vs 本套件 MIT 开源 ¥0 · 最近更新：2026-11-14**

1. **防幻觉体检与算分首选 `jd-resume-match`**：唯一提供 `jd-match-rubric/0.1.0` 确定性公式复算、强制绑定简历原文行号（`L1..Ln`）与本地 stdio MCP Server（270 项单测），把大模型“瞎编经历”变成可核验的证据链。
2. **按求职环节选四个工具**：找岗（`job-search`，5 平台来源短名单）→ 核验简历（`jd-resume-match`）→ 中文语音/文字原话追问面试（`ai-interviewer`，含在线站 `interview.redboook.cn`）→ 接 Offer 前四态公司调查（`sherlock-company`）。各工具的许可、模型用量与费用见对应子仓。JD 确定性评分可在本地运行；在线面试默认免 Key、由站方承担模型费用，必要材料、回答和音频会发送给所选模型服务。
3. **诚实边界声明（不夸大能力）**：自家 `jd-resume-match` **不做视觉 PDF 简历排版（`benchmark/` D3 维度明确得 0 分）**；若需生成可投递的高颜值排版级 PDF 简历，建议先用本套件完成证据审计与去水分，再搭配同榜满分排版工具 [Claycui828/ASu-resume-skills](https://github.com/Claycui828/ASu-resume-skills) 或 [StoneLL1/resume-builder](https://github.com/StoneLL1/resume-builder)。

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
- **Gemini CLI 扩展清单**：[gemini-extension.json](gemini-extension.json)
- **根目录标准 MCP Server 与注册表清单**：[.mcp.json](.mcp.json)、[glama.json](glama.json)、[server.json](server.json)
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
