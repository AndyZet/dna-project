#!/usr/bin/env python3
"""
Parse YFull exports and write a local (private) summary report.

Default input:
  data/raw/y_dna_results/

Default outputs:
  data/processed/y_dna/yfull_exports_summary.json
  output/private_reports/yfull_exports_summary.md
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root / "src"))

from y_dna.yfull_exports import load_yfull_exports


def _safe_str(value: Optional[str]) -> str:
    return value if value is not None else "n/a"

def _tokenize_snp_list(value: str) -> set[str]:
    # YFull uses comma-separated SNPs, but occasionally includes semicolons in synonym tokens.
    # We treat both as separators for a best-effort keyword search.
    tokens: set[str] = set()
    for raw in value.replace(";", ",").split(","):
        tok = raw.strip()
        if tok:
            tokens.add(tok)
    return tokens


def _write_markdown(report: Dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    snp_calls = report.get("snp_calls") or {}
    snp_matches = report.get("snp_matches") or {}
    novel_snps = report.get("novel_snps") or {}
    str_markers = report.get("str_markers") or {}

    haplogroup = snp_calls.get("haplogroup")
    terminal_snps = snp_calls.get("terminal_snps") or []
    ytree_version = snp_calls.get("ytree_version")

    # project-relevant SNP keywords (best-effort string match)
    project_snps = {"Y45113", "S2077", "I1-S2077"}
    found_project_snps: set[str] = set()
    for row in snp_matches.get("matches") or []:
        shared = row.get("Shared SNPs") or ""
        tokens = _tokenize_snp_list(shared)
        found_project_snps |= (tokens & project_snps)

    md_lines = [
        "# YFull exports summary (local)",
        "",
        f"- Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"- Input dir: `{report.get('input_dir')}`",
        f"- Inferred YFull ID: `{_safe_str(report.get('yfull_id'))}`",
        "",
        "## High-level",
        f"- Haplogroup: `{_safe_str(haplogroup)}`",
        f"- Terminal SNPs: `{', '.join(terminal_snps) if terminal_snps else 'n/a'}`",
        f"- YTree version: `{_safe_str(ytree_version)}`",
        "",
        "## Counts",
        f"- SNP calls: `{len((snp_calls.get('calls') or []))}`",
        f"- Novel SNPs: `{len((novel_snps.get('novel_snps') or []))}`",
        f"- STR markers: `{len((str_markers.get('markers') or {}))}`",
        f"- SNP matches rows: `{len((snp_matches.get('matches') or []))}`",
        f"- Project SNP keywords found in matches: `{', '.join(sorted(found_project_snps)) if found_project_snps else 'none'}`",
        "",
        "## Notes for this project",
        "- This report is meant to stay local/private (it may contain sensitive genetic info).",
        "- Use it to ground statements about your own Y-line (haplogroup, terminal SNPs, match TMRCA) when comparing to ancient samples like VK157.",
        "- For BAM-based comparisons (VK155/VK157), we still need: BAM paths in this workspace, BAM indexes (`.bai`), and the reference build used for alignment.",
        "",
    ]

    output_path.write_text("\n".join(md_lines), encoding="utf-8")


def main() -> int:
    input_dir = project_root / "data/raw/y_dna_results"
    output_json = project_root / "data/processed/y_dna/yfull_exports_summary.json"
    output_md = project_root / "output/private_reports/yfull_exports_summary.md"

    report = load_yfull_exports(input_dir)
    report["generated_at"] = datetime.now().isoformat(timespec="seconds")

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    _write_markdown(report, output_md)

    print(f"Wrote: {output_json}")
    print(f"Wrote: {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
