# Chinese career Agent Skills: resume, job search and interview comparison

This is an English guide to the maintainer's **2026-11-06 snapshot** of 12 repositories. Editorial update: 2026-11-16. It is not a fresh benchmark run, independent certification, or a hiring-outcome study.

**Conflict of interest:** the maintainer owns ouba-classmate and the four rows marked “author's project”. Scores are stored in the existing dataset and reproduced below without changing the historical values. The three synthetic case records run the author's resume scorer; they do not prove that all 12 tools were executed or evaluated with the same live model.

Each dimension uses 0–2 points. D1: evidence citation; D2: reproducibility; D3: PDF typesetting; D4: privacy safeguards; D5: Chinese ecosystem fit; D6: installability. A zero for PDF layout may reflect a tool's different purpose, rather than lower overall usefulness. Code checks and privacy instructions are not proof that a selected cloud model keeps data local.

[Chinese report](README.md) · [Method](METHOD.md) · [Raw JSON](repos.json) · [CSV](results.csv) · [Recorded synthetic runs](runs/v0.1-runs.json) · [Data licence: CC BY 4.0](LICENSE-data)

| Repository | Relationship | D1 | D2 | D3 | D4 | D5 | D6 | Total /12 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| [Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills) | external project | 1 | 0 | 0 | 1 | 0 | 1 | 3 |
| [Claycui828/ASu-resume-skills](https://github.com/Claycui828/ASu-resume-skills) | external project | 2 | 1 | 2 | 1 | 2 | 2 | 10 |
| [wangyafu/resume-skills](https://github.com/wangyafu/resume-skills) | external project | 1 | 1 | 2 | 1 | 2 | 1 | 8 |
| [StoneLL1/resume-builder](https://github.com/StoneLL1/resume-builder) | external project | 1 | 1 | 2 | 2 | 2 | 1 | 9 |
| [KevinYoung-Kw/vibe-resume-skill](https://github.com/KevinYoung-Kw/vibe-resume-skill) | external project | 1 | 1 | 2 | 1 | 2 | 1 | 8 |
| [yicLionel/Easy-Job-Tutor](https://github.com/yicLionel/Easy-Job-Tutor) | external project | 1 | 1 | 0 | 1 | 2 | 1 | 6 |
| [u7-u7/developer-resume-writer](https://github.com/u7-u7/developer-resume-writer) | external project | 2 | 0 | 0 | 2 | 2 | 1 | 7 |
| [CJlovetypo/job-search-skill-pack](https://github.com/CJlovetypo/job-search-skill-pack) | external project | 1 | 2 | 0 | 2 | 2 | 2 | 9 |
| [ouxxyy/jd-resume-match](https://github.com/ouxxyy/jd-resume-match) | author's project | 2 | 2 | 0 | 2 | 2 | 2 | 10 |
| [ouxxyy/job-search](https://github.com/ouxxyy/job-search) | author's project | 2 | 2 | 0 | 2 | 2 | 2 | 10 |
| [ouxxyy/ai-interviewer](https://github.com/ouxxyy/ai-interviewer) | author's project | 2 | 2 | 0 | 2 | 2 | 2 | 10 |
| [ouxxyy/sherlock-company](https://github.com/ouxxyy/sherlock-company) | author's project | 2 | 1 | 0 | 2 | 2 | 1 | 8 |

## How these workflows can complement each other

Current README descriptions below were checked on 2026-11-16. These are descriptions of scope, not comparative performance tests. No affiliation or endorsement is implied.

| Workflow | What its README describes | Where the Ouba tools can complement it |
| --- | --- | --- |
| [career-ops](https://github.com/career-ops-hq/career-ops) | Local job evaluation and CV/application preparation; the README offers Simplified Chinese among its translations. | Use a focused resume-evidence check, Chinese voice interview practice or pre-offer company investigation when that is your next task. |
| [ai-job-search](https://github.com/ai-job-search-dev/ai-job-search) | A Claude Code application workflow with profiling, search, ranking, application drafting, interview prep and outcomes. It describes its core as language/country agnostic, with community job portals. | Use Ouba's individual task tools alongside a wider workflow; check current portal support rather than assuming a market is unsupported. |
| [Offer Toolkit](https://github.com/yanliudesign/offer-toolkit-skill) | Search, JD analysis, resume templates, bilingual behavioral stories, offer comparison and negotiation. | Choose Ouba's quote-cited interview feedback or deterministic resume evidence score where those specific outputs are needed. |

## Choose by the next output you need

- **A source-backed Chinese job shortlist:** [job-search](https://github.com/ouxxyy/job-search). It does not submit applications for you.
- **Resume/JD evidence review:** [jd-resume-match](https://github.com/ouxxyy/jd-resume-match). It does not supply an official ATS score or design a PDF resume.
- **Chinese voice interview practice:** [ai-interviewer](https://github.com/ouxxyy/ai-interviewer) or [the online app](https://interview.redboook.cn/). Bring your own Bailian API key; model usage is billed by the provider.
- **Pre-offer company research:** [sherlock-company](https://github.com/ouxxyy/sherlock-company). Unverified information remains unknown.
- **PDF layout:** examine the current documentation and licences of the external template-focused projects in the table; this dataset does not validate their current releases.

Read [the complete project directory](https://github.com/ouxxyy/ouba-classmate#按需求找) for installation, examples and project-specific limits. Historical scores do not guarantee interview, job-search or salary results.
