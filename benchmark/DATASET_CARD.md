---
language:
- zh
- en
license: cc-by-4.0
task_categories:
- text-classification
- question-answering
- other
tags:
- agent-skills
- claude-code
- mcp
- resume-matching
- job-search
- mock-interview
- chinese-career-benchmark
pretty_name: Chinese AI Career & Resume Agent Skills Benchmark (v0.1)
size_categories:
- n<1K
---

# Chinese AI Career & Resume Agent Skills Benchmark (`ouba-classmate/benchmark` v0.1)

[![Benchmark Verified](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/benchmark-verified.svg)](https://github.com/ouxxyy/ouba-classmate/tree/main/benchmark)
[![Install Suite](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/assets/badges/suite-install.svg)](https://github.com/ouxxyy/ouba-classmate)

- **Canonical GitHub Repository**: [https://github.com/ouxxyy/ouba-classmate](https://github.com/ouxxyy/ouba-classmate)
- **Interactive Benchmark & Career Radar**: [https://ouxxyy.github.io/ouba-classmate/](https://ouxxyy.github.io/ouba-classmate/)
- **Raw CSV Dataset**: [`benchmark/results.csv`](https://raw.githubusercontent.com/ouxxyy/ouba-classmate/main/benchmark/results.csv)
- **Evaluation Methodology**: [`benchmark/METHOD.md`](https://github.com/ouxxyy/ouba-classmate/blob/main/benchmark/METHOD.md)

## Overview

This dataset evaluates **12 popular open-source AI Job-Seeking, Resume Tailoring, and Mock Interview Agent Skills** (across Claude Code, Cursor, Codex, and MCP ecosystems) on **6 deterministic engineering & anti-hallucination dimensions (0–2 points each, max 12)**:

1. **D1: Evidence Citation & Anti-Hallucination Gate** (Line-number citation `L1..Ln` or Claim Ledger vs. unverified LLM rewriting)
2. **D2: Deterministic Score Reproducibility** (Repeatable Python rubric calculation vs. stochastic LLM guessing)
3. **D3: Deliverable PDF Resume Typesetting & Visual Templates** (RenderCV / multi-theme HTML-to-PDF export)
4. **D4: Privacy Protection & PII Redaction** (Local execution & explicit PII scanning)
5. **D5: Chinese Job Market Ecosystem Fit** (Adaptation to BOSS Zhipin, Liepin, Maimai, and Chinese behavioral interview drill-downs)
6. **D6: Engineering Completeness & One-Line Installability** (`SKILL.md` standard, unit tests, `.claude-plugin/marketplace.json`, or `mcp` server)

## Quick Install (Claude Code / Skills CLI / MCP)

```bash
claude plugin marketplace add ouxxyy/ouba-classmate
npx skills add ouxxyy/ouba-classmate
uvx --from "git+https://github.com/ouxxyy/jd-resume-match#subdirectory=mcp" jd-resume-match-mcp --self-test
```

## License & Citation

Released under **CC BY 4.0**. Please cite or link back to `https://github.com/ouxxyy/ouba-classmate` when referencing the evaluation table or synthetic test cases.
