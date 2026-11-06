# 《中文 AI 求职 Skill 公开横评》评测方法论（METHOD v0.1）

> **先公开标准，再跑数据**：本文件定义 `ouba-classmate/benchmark` 的样本收录规则、6 大客观评测维度、合成测试数据集规范与利益冲突披露原则。任何人均可通过 `python3 benchmark/scripts/run_benchmark.py` 复现核验。

---

## 1. 样本收录规则（Inclusion Criteria）

我们使用 `gh search repos` 固定查询词（`求职 skill`、`简历 skill`、`resume skill`、`job search skill`、`mock interview skill`），按以下客观条件筛选 v0.1 首批 12 个评测对象：

1. **形态要求**：仓库内包含标准 `SKILL.md`（支持 Claude Code / Codex / Cursor 等 Agent Skills 宿主调用）。
2. **活跃度要求**：最近一次提交（`updatedAt`）在 180 天以内（2026-05 至 2026-11）。
3. **赛道覆盖**：覆盖「简历诊断与改写」「可投递简历排版生成」「招聘岗位搜索」「模拟面试陪练」「入职前公司调查」五个求职子环节，并纳入英文头部项目 `Paramchoudhary/ResumeSkills` 作为跨语言基准对照。

---

## 2. 六大评测维度与计分口径（每项 0–2 分，满分 12 分）

为避免“用主观印象给竞品打低分”，所有维度均采用**仓库源码树可核验特征 + 3 组合成案例实测输出**的双重客观标准：

| 维度代码 | 维度名称 | 0 分标准 | 1 分标准 | 2 分标准 |
| --- | --- | --- | --- | --- |
| **D1** | **证据引用与反幻觉门禁** (`evidence_citation`) | 无原文引用要求，允许模型自由润色或扩写未提及的经历数字 | Prompt 中口头要求“基于事实、不编造”，但无行号/段落定位或校验脚本 | 强制要求绑定简历原文行号/段落引用（或 Claim Ledger 账本），且配备脚本校验缺口 |
| **D2** | **评分与逻辑可复算性** (`reproducibility`) | 纯 Prompt 驱动，无任何本地脚本，或由 LLM 直接拍脑袋给匹配分 | 含辅助处理/校验脚本，但核心评价仍由 LLM 生成，多次运行结果存在波动 | 评分或核验状态机由确定性代码（Python/JS）计算，同输入必得同分数 |
| **D3** | **可投递 PDF 简历排版与视觉模板** (`pdf_typesetting`) | **不提供可投递的简历 PDF 排版导出**（仅输出诊断报告或纯文本建议） | 提供单一固定格式导出或基础 Markdown 转 HTML | 内置多套精美 HTML/PDF/RenderCV 视觉模板，支持一页纸自动缩放或版式校验 |
| **D4** | **隐私保护与脱敏机制** (`privacy_protection`) | 未声明数据流向，或需将完整简历上传至不明第三方服务端 | 声明本地运行或提示用户注意隐私，但无自动脱敏/红线扫描脚本 | 本地脚本处理 + 内置 PII（姓名/电话/邮箱/公司）脱敏门禁或显式隐私告知页 |
| **D5** | **中文求职生态适配度** (`cn_ecosystem_fit`) | 仅面向英文简历与海外平台（LinkedIn / Greenhouse） | 支持中文输入输出，但未针对国内招聘平台/大厂职级/中文 JD 黑话做专门适配 | 深度适配中文 JD 话术、国内平台（BOSS直聘/猎聘/脉脉）或中国职场追问场景 |
| **D6** | **工程完备度与一键可安装性** (`installability`) | 仅单文件 Prompt，无自动化测试、无插件清单或安装工具 | 具备标准 `SKILL.md` 目录结构或安装脚本 | 同时具备标准 `SKILL.md`、自动化单元测试（`tests/`）及插件/MCP/CLI 入口 |

---

## 3. 合成测试数据集（Synthetic Cases）

为严格遵守个人信息保护（风险规则 R11），本横评**严禁使用任何真实求职者简历**。`benchmark/cases/` 下提供 3 组 100% 虚构的合成简历与目标 JD：

- `case-01-ai-pm.json`：3 年经验互联网产品经理转型 AI Agent 产品岗（含“参与项目但未写清个人动作”的典型证据缺口，测试工具是否会擅自把“参与”改写成“独立负责”及编造转化率数字）。
- `case-02-backend-go.json`：5 年后端开发投递高并发交易系统岗（含“JD 要求 Kafka 事务与分库分表，但简历仅有 Redis 缓存经验”的硬性技能缺失，测试工具是否会凭空捏造中间件经验）。
- `case-03-campus-ops.json`：应届生投递内容运营岗（含两段校园与短期实习经历，测试工具对初级求职者经历挖掘与追问的适配度）。

---

## 4. 利益冲突披露与申诉复测机制（COI & Appeal Policy）

1. **利益冲突声明**：本横评由 `ouxxyy/ouba-classmate` 维护者（欧八同学）发起并维护。表中标记 `[自家项目·利益相关]` 的 4 个仓库（`jd-resume-match`、`job-search`、`ai-interviewer`、`sherlock-company`）均为作者本人开发。
2. **显式公开自家短板**：我们在维度设计中专门纳入了 **D3（可投递 PDF 简历排版与视觉模板）**——在这项求职者高频刚需上，自家的 `jd-resume-match` 等全部 4 个项目得分均为 **0 分**（明显输给 `KevinYoung-Kw/vibe-resume-skill`、`StoneLL1/resume-builder`、`Claycui828/ASu-resume-skills` 与 `wangyafu/resume-skills`）。此外，`jd-resume-match` 对中文 CID 字体 PDF 不做内置解码（需转文本或 DOCX）。
3. **无条件申诉与复测**：任何被收录仓库的维护者或第三方读者，如认为某项打分与最新代码不符，只需在 [`ouxxyy/ouba-classmate/issues`](https://github.com/ouxxyy/ouba-classmate/issues) 提交 Issue 并附上 commit 链接，我们将在 72 小时内重跑脚本并更新 `results.csv`。
