"""
Parse YFull export files (SNP/STR/matches) saved locally.

These exports are often semicolon-delimited and may contain semicolons inside
SNP synonym tokens (e.g., "Y125387;FGC33327"). The parsers here are designed
to be tolerant of that formatting.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Dict, Iterable, List, Optional


@dataclass(frozen=True)
class YFullSnpCall:
    name: str
    status: str
    reads: Optional[str] = None
    stars: Optional[str] = None
    extra: Optional[str] = None


def _read_lines(path: Path) -> List[str]:
    return [line.rstrip("\n") for line in path.read_text(encoding="utf-8", errors="replace").splitlines()]


def parse_snp_calls_file(path: Path) -> Dict[str, Any]:
    """
    Parse `SNP_for_<ID>_<date>.csv` exported by YFull.

    Format is generally:
      Haplogroup;I-Yxxxx
      Terminal SNPs;Yxxxx | ...
      YTree v13.xx;
      SNP_NAME;positive;9 read;*****;
    """
    lines = _read_lines(path)
    if not lines:
        return {"path": str(path), "haplogroup": None, "terminal_snps": [], "ytree_version": None, "calls": []}

    haplogroup = None
    terminal_snps: List[str] = []
    ytree_version = None
    calls: List[Dict[str, Any]] = []

    for line in lines:
        if not line.strip():
            continue

        if line.startswith("Haplogroup;"):
            haplogroup = line.split(";", 1)[1].strip() or None
            continue

        if line.startswith("Terminal SNPs;"):
            raw = line.split(";", 1)[1].strip()
            terminal_snps = [part.strip() for part in raw.split("|") if part.strip()]
            continue

        if line.startswith("YTree"):
            ytree_version = line.split(";", 1)[0].strip() or None
            continue

        # SNP call lines
        parts = line.split(";")
        if len(parts) >= 2:
            name = (parts[0] or "").strip()
            status = (parts[1] or "").strip()
            if name and status and name not in {"Haplogroup", "Terminal SNPs"}:
                reads = parts[2].strip() if len(parts) >= 3 and parts[2].strip() else None
                stars = parts[3].strip() if len(parts) >= 4 and parts[3].strip() else None
                extra = ";".join(parts[4:]).strip() if len(parts) >= 5 else None
                calls.append(
                    {
                        "name": name,
                        "status": status,
                        "reads": reads,
                        "stars": stars,
                        "extra": extra or None,
                    }
                )

    return {
        "path": str(path),
        "haplogroup": haplogroup,
        "terminal_snps": terminal_snps,
        "ytree_version": ytree_version,
        "calls": calls,
    }


def parse_novel_snps_file(path: Path) -> Dict[str, Any]:
    """
    Parse `NovelSNP_for_<ID>_<date>.csv` exported by YFull.

    Header example:
      Name;Position T2T;Reference;Derived;Q;Qual;Reads;T2T only
    """
    lines = _read_lines(path)
    if not lines:
        return {"path": str(path), "novel_snps": []}

    header = lines[0].split(";")
    rows: List[Dict[str, Any]] = []
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split(";")
        row = {header[i].strip(): (parts[i].strip() if i < len(parts) else "") for i in range(len(header))}
        rows.append(row)
    return {"path": str(path), "novel_snps": rows}


def parse_str_file(path: Path) -> Dict[str, Any]:
    """
    Parse `STR_for_<ID>_<date>.csv` exported by YFull.
    Format: DYSxxx;value;
    """
    lines = _read_lines(path)
    markers: Dict[str, str] = {}
    for line in lines:
        if not line.strip():
            continue
        parts = line.split(";")
        if len(parts) >= 2 and parts[0].strip():
            markers[parts[0].strip()] = parts[1].strip()
    return {"path": str(path), "markers": markers}


def parse_str_statistics_file(path: Path) -> Dict[str, Any]:
    """
    Parse `STR_statistic_for_<ID>.csv` exported by YFull.
    Header: HG/SAMPLES;STRs;Detected;Mutation rate;ANC;DER
    """
    lines = _read_lines(path)
    if not lines:
        return {"path": str(path), "rows": []}
    header = [h.strip() for h in lines[0].split(";")]
    rows: List[Dict[str, str]] = []
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split(";")
        rows.append({header[i]: (parts[i].strip() if i < len(parts) else "") for i in range(len(header))})
    return {"path": str(path), "rows": rows}


def parse_snp_matches_file(path: Path) -> Dict[str, Any]:
    """
    Parse `SNP_matches_for_<ID>.csv` exported by YFull.

    This file is semicolon-delimited at the column level, but SNP synonym tokens
    may contain semicolons inside the "Shared SNPs" field. To stay robust, we:
      - split the line into 7 parts (first 6 semicolons fixed), then
      - split the remainder from the right once to separate the last field.
    """
    lines = _read_lines(path)
    if not lines:
        return {"path": str(path), "matches": []}

    header = [h.strip() for h in lines[0].split(";")]
    matches: List[Dict[str, Any]] = []
    for line in lines[1:]:
        if not line.strip():
            continue

        # First 6 fields are stable.
        parts = line.split(";", 6)
        if len(parts) < 7:
            continue

        fixed = parts[:6]
        shared_and_last = parts[6]
        shared_snps_raw, last_field = (shared_and_last.rsplit(";", 1) + [""])[:2]

        row = {
            header[0] if len(header) > 0 else "MRCA branch": fixed[0].strip(),
            header[1] if len(header) > 1 else "TMRCA (ybp)": fixed[1].strip(),
            header[2] if len(header) > 2 else "Most distant ancestor": fixed[2].strip(),
            header[3] if len(header) > 3 else "Country of origin": fixed[3].strip(),
            header[4] if len(header) > 4 else "ID": fixed[4].strip(),
            header[5] if len(header) > 5 else "Terminal Hg": fixed[5].strip(),
            header[6] if len(header) > 6 else "Shared SNPs": shared_snps_raw.strip(),
            header[7] if len(header) > 7 else "Assumed shared SNPs": last_field.strip(),
        }
        matches.append(row)

    return {"path": str(path), "matches": matches}


def infer_yfull_id_from_filenames(paths: Iterable[Path]) -> Optional[str]:
    """
    Best-effort inference of the YFull kit/sample ID from filenames like:
      SNP_for_YF079056_20260110.csv
    """
    for path in paths:
        name = path.name
        match = re.search(r"(?:^|_)YF(\d{4,})(?:_|\\.|$)", name)
        if match:
            return f"YF{match.group(1)}"
    return None


def load_yfull_exports(input_dir: Path) -> Dict[str, Any]:
    """
    Load all known YFull export files from a directory.
    """
    input_dir = input_dir.expanduser().resolve()
    if not input_dir.exists():
        raise FileNotFoundError(f"Input directory not found: {input_dir}")

    all_files = sorted([p for p in input_dir.iterdir() if p.is_file()])
    yfull_id = infer_yfull_id_from_filenames(all_files)

    snp_calls = None
    for p in all_files:
        if p.name.startswith("SNP_for_") and p.suffix.lower() == ".csv":
            snp_calls = parse_snp_calls_file(p)
            break

    novel_snps = None
    for p in all_files:
        if p.name.startswith("NovelSNP_for_") and p.suffix.lower() == ".csv":
            novel_snps = parse_novel_snps_file(p)
            break

    str_markers = None
    for p in all_files:
        if p.name.startswith("STR_for_") and p.suffix.lower() == ".csv":
            str_markers = parse_str_file(p)
            break

    snp_matches = None
    for p in all_files:
        if p.name.startswith("SNP_matches_for_") and p.suffix.lower() == ".csv":
            snp_matches = parse_snp_matches_file(p)
            break

    str_stats = None
    for p in all_files:
        if p.name.startswith("STR_statistic_for_") and p.suffix.lower() == ".csv":
            str_stats = parse_str_statistics_file(p)
            break

    return {
        "input_dir": str(input_dir),
        "yfull_id": yfull_id,
        "snp_calls": snp_calls,
        "novel_snps": novel_snps,
        "str_markers": str_markers,
        "snp_matches": snp_matches,
        "str_statistics": str_stats,
        "other_files": [str(p) for p in all_files if p.suffix.lower() not in {".csv"}],
    }
