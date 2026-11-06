#!/usr/bin/env python3
"""《中文 AI 求职 Skill 公开横评》可复现生成与核验脚本（v0.1）。

功能：
1. 读取 `benchmark/repos.json`（12 个经 GitHub API 实测核验的求职类 Skill 仓库元数据与六维打分）。
2. 读取 `benchmark/cases/*.json`（3 组 100% 虚构合成简历与 JD），调用确定性评分引擎跑出基线对照结果并存入 `benchmark/runs/v0.1-runs.json`。
3. 生成标准 `benchmark/results.csv` 供外部文章、数据分析与研究者直接引用。
"""

from __future__ import annotations

import csv
import datetime as dt
import json
import pathlib
import sys

BENCH_ROOT = pathlib.Path(__file__).resolve().parent.parent
REPOS_JSON = BENCH_ROOT / "repos.json"
CASES_DIR = BENCH_ROOT / "cases"
RUNS_DIR = BENCH_ROOT / "runs"
RESULTS_CSV = BENCH_ROOT / "results.csv"

# 引入本地 jd-resume-match MCP 的确定性评分函数作为可复算基准验证
MCP_DIR = BENCH_ROOT.parent.parent / "jd-resume-match" / "mcp"
if MCP_DIR.is_dir():
    sys.path.insert(0, str(MCP_DIR))
    from jd_resume_match_mcp.server import match_resume  # type: ignore
else:
    match_resume = None


def main() -> int:
    data = json.loads(REPOS_JSON.read_text(encoding="utf-8"))
    repos = data["repositories"]

    # 1. 生成 results.csv
    fieldnames = [
        "repo",
        "category",
        "is_self_project",
        "stars_2026_11_06",
        "updated_at",
        "skill_md_count",
        "script_count",
        "template_count",
        "has_tests",
        "D1_evidence_citation",
        "D2_reproducibility",
        "D3_pdf_typesetting",
        "D4_privacy_protection",
        "D5_cn_ecosystem_fit",
        "D6_installability",
        "total_score_12",
        "strengths",
        "limitations",
    ]

    rows = []
    for r in repos:
        sc = r["scores"]
        total = sum(sc.values())
        rows.append(
            {
                "repo": r["repo"],
                "category": r["category"],
                "is_self_project": "yes (COI disclosed)" if r["is_self"] else "no",
                "stars_2026_11_06": r["stars_verified_1106"],
                "updated_at": r["updated_at"],
                "skill_md_count": r["skill_md_count"],
                "script_count": r["script_count"],
                "template_count": r["template_count"],
                "has_tests": "yes" if r["has_tests"] else "no",
                "D1_evidence_citation": sc["D1_evidence_citation"],
                "D2_reproducibility": sc["D2_reproducibility"],
                "D3_pdf_typesetting": sc["D3_pdf_typesetting"],
                "D4_privacy_protection": sc["D4_privacy_protection"],
                "D5_cn_ecosystem_fit": sc["D5_cn_ecosystem_fit"],
                "D6_installability": sc["D6_installability"],
                "total_score_12": total,
                "strengths": r["strengths"],
                "limitations": r["limitations"],
            }
        )

    with RESULTS_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # 2. 对 3 组合成案例运行确定性评测并写入 runs/v0.1-runs.json
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    case_runs = []
    for case_file in sorted(CASES_DIR.glob("case-*.json")):
        case_obj = json.loads(case_file.read_text(encoding="utf-8"))
        det_result = (
            match_resume(case_obj["jd"], case_obj["resume"])
            if match_resume is not None
            else {"note": "standalone mode"}
        )
        case_runs.append(
            {
                "case_id": case_obj["case_id"],
                "synthetic": case_obj["synthetic"],
                "target_role": case_obj["target_role"],
                "ground_truth": case_obj["ground_truth"],
                "deterministic_run_output": det_result,
            }
        )

    run_artifact = {
        "benchmark_version": data["benchmark_version"],
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "verified_date": data["verified_date"],
        "synthetic_cases_evaluated": len(case_runs),
        "repositories_evaluated": len(repos),
        "case_runs": case_runs,
    }
    out_run = RUNS_DIR / "v0.1-runs.json"
    out_run.write_text(json.dumps(run_artifact, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"✔ 已生成 {RESULTS_CSV}（{len(rows)} 个仓库）与 {out_run}（{len(case_runs)} 组合成用例实测记录）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
