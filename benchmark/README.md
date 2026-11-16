# 《中文 AI 求职 Skill 公开横评》（v0.1 · 2026-11 资料快照版）

[English comparison guide](README.en.md) · 样本日期：2026-11-06；本页说明更新：2026-11-16。

> 📦 **所属主仓**：[ouxxyy/ouba-classmate（一行安装的中文求职与创作 Agent Skills 套件）](https://github.com/ouxxyy/ouba-classmate)
> 📊 **数据许可**：[CC BY 4.0](LICENSE-data)（欢迎媒体、博主、周刊与 AI 搜索引擎自由引用，引用请保留本页链接）· [评测方法论](METHOD.md) · [原始 CSV 下载](results.csv) · [3 组合成测试集](cases/) · [实测运行记录](runs/v0.1-runs.json)

---

## 一、首屏结论总表（12 个主流中英文求职 Skill 实测对比）

> **利益冲突与客观性声明（COI Disclosure）**：
> 1. 本横评由 `ouba-classmate` 维护者发起，表中标记 **`[自家·利益相关]`** 的 4 个仓库为作者本人项目。
> 2. 所有仓库的 Star 数、文件数、脚本数与模板数均于 **2026-11-06 通过 GitHub API 实测核验【API 已验证 11-06】**，评分规则在 [METHOD.md](METHOD.md) 中预先公开，任何人可运行 `python3 benchmark/scripts/run_benchmark.py` 复现。
> 3. **公开自家短板**：在求职者极其看重的 **D3（可投递 PDF 简历排版与多套视觉模板）** 维度上，自家的 `jd-resume-match` 等 4 个项目**全部得 0 分**，明确输给 `Claycui828/ASu-resume-skills`、`wangyafu/resume-skills`、`StoneLL1/resume-builder` 与 `KevinYoung-Kw/vibe-resume-skill`。

| 仓库（点击访问） | 赛道定位 | Star (11-06) | 脚本数 / 模板数 / 单测 | D1 证据引用 | D2 可复算性 | D3 PDF排版模板 | D4 隐私脱敏 | D5 中文生态 | D6 可安装性 | 总分 (/12) | 一句话选型建议 |
| --- | --- | ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | ---: | --- |
| **[Claycui828/ASu-resume-skills](https://github.com/Claycui828/ASu-resume-skills)** | 简历审计 + PDF 生成 | 426 | 5 / 6 / ✅ | **2** | 1 | **2** | 1 | **2** | **2** | **10** | **中文技术简历排版与审计首选**：兼顾事实审计与高密度 PDF 导出 |
| **[ouxxyy/jd-resume-match](https://github.com/ouxxyy/jd-resume-match)** `[自家·利益相关]` | 简历 vs JD 可复算体检 | 0 | 10 / 2 / ✅ | **2** | **2** | **0** ❌ | **2** | **2** | **2** | **10** | **投前证据核对与算分首选**：唯一带确定性公式复算 + MCP Server；**但不导出排版 PDF** |
| **[ouxxyy/job-search](https://github.com/ouxxyy/job-search)** `[自家·利益相关]` | 多平台招聘筛选短名单 | 0 | 8 / 1 / ✅ | **2** | **2** | 0 | **2** | **2** | **2** | **10** | **跨平台找岗首选**：覆盖 BOSS/猎聘/脉脉等 5 平台，生成带来源 HTML+Excel |
| **[ouxxyy/ai-interviewer](https://github.com/ouxxyy/ai-interviewer)** `[自家·利益相关]` | 中文语音/文字经历面试 | 3 | 12 / 3 / ✅ | **2** | **2** | 0 | **2** | **2** | **2** | **10** | **经历面试追问首选**：按 JD 追问、逐句引用原话五维点评、支持重答对比 |
| **[StoneLL1/resume-builder](https://github.com/StoneLL1/resume-builder)** | 采访式写作 + RenderCV | 127 | 6 / 8 / ❌ | 1 | 1 | **2** | **2** | **2** | 1 | **9** | **从零写简历 + 经典 LaTeX/RenderCV 风格导出首选** |
| **[CJlovetypo/job-search-skill-pack](https://github.com/CJlovetypo/job-search-skill-pack)** | 3000+ 中国招聘主体雷达 | 9 | 5 / 0 / ✅ | 1 | **2** | 0 | **2** | **2** | **2** | **9** | **批量检索国企/大厂招聘主体名录首选** |
| **[wangyafu/resume-skills](https://github.com/wangyafu/resume-skills)** | 一站式简历编写与 PDF | 232 | 3 / 5 / ❌ | 1 | 1 | **2** | 1 | **2** | 1 | **8** | **快速套用中文配色模板（极简纯白/典雅酒红）生成 PDF 简历** |
| **[KevinYoung-Kw/vibe-resume-skill](https://github.com/KevinYoung-Kw/vibe-resume-skill)** | 12 套 HTML/PDF 视觉模板 | 101 | 4 / 12 / ❌ | 1 | 1 | **2** | 1 | **2** | 1 | **8** | **追求高颜值多风格（Bauhaus/Editorial 等 12 套）简历排版首选** |
| **[ouxxyy/sherlock-company](https://github.com/ouxxyy/sherlock-company)** `[自家·利益相关]` | Offer 前公司证据背调 | 1 | 2 / 2 / ❌ | **2** | 1 | 0 | **2** | **2** | 1 | **8** | **接 Offer 前防踩坑首选**：区分已证实/线索/冲突/未知，查三类公司预警 |
| **[u7-u7/developer-resume-writer](https://github.com/u7-u7/developer-resume-writer)** | 研发简历提炼与强制脱敏 | 25 | 0 / 0 / ❌ | **2** | 0 | 0 | **2** | **2** | 1 | **7** | **轻量纯 Prompt 研发经历提炼**，强调脱敏但无本地校验脚本 |
| **[yicLionel/Easy-Job-Tutor](https://github.com/yicLionel/Easy-Job-Tutor)** | 浏览器侧边栏 + JD 分析 | 66 | 8 / 2 / ❌ | 1 | 1 | 0 | 1 | **2** | 1 | **6** | **习惯边刷招聘网页边在 Chrome 侧边栏看 JD 解析的用户** |
| **[Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)** | 英文求职全套 Prompt | 3049 | 0 / 0 / ❌ | 1 | 0 | 0 | 1 | 0 | 1 | **3** | **外企/海外英文求职参考**：22 个纯 Prompt 子技能，0 脚本，无中文适配 |

*(注：D1–D6 每项 0–2 分，评分标准详见 [METHOD.md](METHOD.md)。D3 专门衡量“可投递简历 PDF 排版模板”，用于区分“排版生成器”与“证据诊断/搜索/面试工具”。)*

---

## 二、怎样解读这份数据

表中分数是维护者依据公开项目资料给出的历史赋分。API 元数据检查、代码与文档审查、确定性脚本运行是不同证据，不能合并称为全部 12 个工具的真实使用横评。

仓库保留三组合成简历与 JD，以及自家 `jd-resume-match` 评分器的运行记录；生成脚本没有逐个执行表中外部工具。因此这些记录不支持“所有纯 Prompt 工具会产生某种幻觉”或“分数波动 12–20 分”等普遍结论。历史原始 JSON、CSV 和运行记录保持原样，可直接查看并复核。

选型时先看任务：证据核对、PDF 排版、岗位搜索和面试练习是不同用途。D3=0 仅表示该口径下不提供 PDF 排版，不代表工具总体无用。需要模板排版可看表中对应项目，需要中文语音追问可进入 [欧八面试陪练](https://interview.redboook.cn/)。模型费用与数据流向分别核对。

---

## 三、如何复现本横评或申请复测？

### 1. 本地一键复现
```bash
git clone https://github.com/ouxxyy/ouba-classmate.git
cd ouba-classmate
python3 benchmark/scripts/run_benchmark.py
```
运行后将自动重新生成 `benchmark/results.csv` 与 `benchmark/runs/v0.1-runs.json`。

### 2. 被评仓库申诉与新仓库提交（被动开放通道）
如果您是上述仓库的维护者，或希望将您的开源求职 Skill 纳入 `v0.2`（计划于 2026-12-10 发布，扩容至 20 个仓库），欢迎直接在 [Issues](https://github.com/ouxxyy/ouba-classmate/issues) 提交复测或收录申请。

---

## 四、🏅 项目资料标签（非官方认证）（Badge 一键嵌入）

所有在《中文 AI 求职 Skill 公开横评》中纳入历史资料比较的开源仓库，均可将以下 SVG 资料标签免费嵌入各自仓库的 `README.md` 首屏：

| 徽章预览 | 适用上榜仓库 | 一键嵌入 Markdown 代码 |
| :--- | :--- | :--- |
| [![Top Tier](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-top-tier.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark) | 总分 **≥ 9/12** 的第一梯队仓库（如 `Claycui828/ASu-resume-skills`、`StoneLL1/resume-builder`、`CJlovetypo/job-search-skill-pack` 等） | `[![Chinese AI Career Benchmark Top Tier](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-top-tier.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark)` |
| [![PDF Leader](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-pdf-leader.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark) | **D3（可投递 PDF 简历排版模板）满分 2/2** 仓库（如 `Claycui828/ASu-resume-skills`、`wangyafu/resume-skills`、`StoneLL1/resume-builder`、`KevinYoung-Kw/vibe-resume-skill`） | `[![Chinese AI Career Benchmark PDF Leader](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-pdf-leader.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark)` |
| [![Verified](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-verified.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark) | 全部已纳入 `v0.1` 实测数据集并完成 API 核验的开源仓库 | `[![Chinese AI Career Benchmark Verified](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-verified.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark)` |

