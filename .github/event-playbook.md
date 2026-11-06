# P5 事件劫持 24 小时响应手册（Event Playbook）

> **目标**：热点窗口通常不超过 2–3 周。本手册预先固定 5 类高确定性触发事件的判定阈值、承接仓库、24 小时内交付物骨架与 Release 归因路径（M2），确保事件出现后 12 小时内由 Agent 生成完整草稿、24 小时内上线。

---

## 一、五类触发事件与响应矩阵

| 触发编号 | 触发事件类型 | 判定阈值（满足才响应） | 承接仓库（同时回流 `ouba-classmate`） | 24 小时内标准交付物 | M2 唯一落地路径 |
| --- | --- | --- | --- | --- | --- |
| **E1** | **AI 视频生成模型重大版本发布**（可灵 Kling、即梦 Seedance、Google Veo、OpenAI Sora 等） | 官方发布新版本公告或开放新多模态控制参数 | `storyboard-scavenger` + `ouba-classmate` | 在 `storyboard-scavenger/models/` 新增或更新对应模型 `.md` 规范 + 3 个实测七要素提示词示例 + 打 Release tag | `/releases/tag/model-<name>-<date>` |
| **E2** | **主流 Agent 宿主更新 Skill / Plugin 规范**（Claude Code、Codex、Cursor、skills CLI） | 官方 Changelog 提及 `skills`、`plugin`、`marketplace.json` 或 `MCP` 新字段 | `ouba-classmate` | 同步更新 `.claude-plugin/marketplace.json` 与 `scripts/sync_skills.py` + 发布中文《迁移与兼容说明》Release | `/releases/tag/spec-<host>-<date>` |
| **E3** | **招聘季与职场节点**（春招启动、年后跳槽、秋招提前批、大厂年终奖与组织调整热议） | 微博/知乎/脉脉热榜出现春招、跳槽、裁员或年终奖话题 | `ouba-classmate` + `ai-interviewer` | 更新 `ai-interviewer/seasonal/` 题库包 + 发布 `benchmark/` 季节版（如 v0.3 春招版） | `/releases/tag/seasonal-<tag>` |
| **E4** | **权威机构发布 AI 替代就业报告**（WEF、麦肯锡、高盛、智联/猎聘年度报告等） | 报告原文或核心工种数据可公开获取 | `mbai` + `ouba-classmate` | 用报告中的高危/低危任务分类与 `mbai` 的「工作任务 AI 不可替代指数」做对照表与自评案例 | `/releases/tag/report-<org>-<date>` |
| **E5** | **GitHub 中文区新一轮「XX.skill / 角色蒸馏」热潮** | GitHub Trending 或检索在 7 天内出现 ≥2 个单日增长 >100 Star 的中文 Skill 新仓 | `mystery-skill` 或新建角色蒸馏旗舰仓 | 对齐热点形态推出职场/面试官认知蒸馏专题，首屏挂 `ouba-classmate` 套件入口 | `/tree/main/workplace` 或新仓 Release |

---

## 二、24 小时响应执行检查清单（Checklist）

- [ ] **T+0h ~ T+2h（事实核验）**：确认官方公告或一手报告原文链接，绝不基于二手截图或传言编造参数；严禁使用真实个人姓名或针对单一公司负面丑闻做营销（遵守 R10）。
- [ ] **T+2h ~ T+10h（资产构建）**：
  - 若为 E1：在 `storyboard-scavenger/models/<model>.md` 补齐参数表与 3 个可直接复制的分镜提示词，更新 `CHANGELOG.md`。
  - 若为 E2/E3/E4：在对应目录生成可复现数据或配置，并同步运行 `ouba-classmate/scripts/sync_skills.py` 与 `scripts/build_docs.py`。
- [ ] **T+10h ~ T+12h（Release 与渠道草稿）**：
  - 在 GitHub 创制带唯一标识的 Release Tag（作为 M2 归因落地页）。
  - 生成公众号/V2EX/X/小红书摘要卡片草稿，**交由本人审阅确认后再对外发布**（遵守硬性规则第 4 条）。
- [ ] **T+12h ~ T+24h（日志登记）**：将 UTC 发布时间、改动文件与落地路径写入 `ouxxyy/growth-metrics/LOG.md`。
- [ ] **T+96h（72 小时复盘与止损检查）**：运行 `collect_metrics.py` 检查承接仓 + 合集 72 小时净增 Star（有效标准：≥10 Star；若连续 2 次触发响应 <3 Star，则关闭非招聘季触发器）。

---

## 三、Release 页标准文案模板

```markdown
# [事件适配] <事件/模型/节点名称> 专属适配版（<YYYY-MM-DD>）

## 本次更新解决什么具体问题？
- 针对 <官方公告/报告/节点名称>（一手来源：<官方链接>），新增了……
- 提供 3 组可直接复制运行的配置 / 提示词 / 合成评测案例：

## 30 秒快速体验（通过 ouba-classmate 套件安装）
\`\`\`bash
claude plugin marketplace add ouxxyy/ouba-classmate
npx skills add ouxxyy/ouba-classmate
\`\`\`

## 关联资源
- 主套件仓库：[ouxxyy/ouba-classmate](https://github.com/ouxxyy/ouba-classmate)
- 《中文 AI 求职 Skill 公开横评》：[查看最新数据](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark)
```
