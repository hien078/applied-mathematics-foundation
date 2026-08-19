#!/usr/bin/env python3
"""Count what the curriculum actually contains.

The root and area READMEs advertise module and problem counts. Those numbers must be
generated, not remembered: the last hand-written table was wrong by 72 problems.

Usage
-----
    python3 tools/curriculum_stats.py             # human-readable table
    python3 tools/curriculum_stats.py --markdown  # the Curriculum-at-a-Glance table
    python3 tools/curriculum_stats.py --json      # machine-readable
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

AREA_TITLES = {
    "linear_algebra": "Linear Algebra",
    "calculus": "Calculus",
    "optimization": "Optimization",
    "calculus_optimization": "Calculus to Optimization",
    "probability_statistics": "Probability and Statistics",
    "information_theory": "Information Theory",
    "numerical_methods": "Numerical Methods",
    "numerical_computing": "Numerical Computing",
    "differential_equations": "Differential Equations",
    "graph_theory": "Graph Theory",
    "mathematical_reasoning": "Mathematical Reasoning",
}

# Every problem-heading dialect currently present in the repository.
# A problem heading, not a sub-heading inside one. `#### Problem Statement` and
# `#### Problem Setup` are parts of a problem; `### Problem L2.3` is the problem.
PROBLEM_RE = re.compile(
    r"^#{3,4}[ \t]*(?:Exercise|Problem)[ \t]+(?=[0-9LP])"
    r"|^#{3,4}[ \t]*(?:L[0-3]|P)[ \t]*[0-9.]+",
    re.MULTILINE,
)
TIER_RE = re.compile(
    r"^##\s*(?:L[0-3]\b.*|Level\s*[0-3]\b.*|Foundation Level|Understanding Level|"
    r"Advanced Level|Olympiad(?:\s*Level)?|Research Level)$",
    re.MULTILINE,
)


def notebook_text(path: Path) -> tuple[str, int, int, int]:
    """Return (all markdown source, n_code_cells, n_figures, n_cells)."""
    nb = json.loads(path.read_text(encoding="utf-8"))
    md, code, figs = [], 0, 0
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "markdown":
            md.append("".join(cell.get("source", [])))
        elif cell.get("cell_type") == "code":
            code += 1
            for out in cell.get("outputs", []) or []:
                if "image/png" in (out.get("data") or {}):
                    figs += 1
    return "\n".join(md), code, figs, len(nb.get("cells", []))


def scan() -> list[dict]:
    rows = []
    for area in sorted(p.name for p in REPO.iterdir() if p.is_dir() and p.name in AREA_TITLES):
        modules = sorted(
            p for p in (REPO / area).iterdir() if p.is_dir() and re.match(r"^\d\d_", p.name)
        )
        entry = {
            "area": area,
            "title": AREA_TITLES[area],
            "modules": len(modules),
            "problems": 0,
            "tiers": 0,
            "code_cells": 0,
            "figures": 0,
            "module_rows": [],
        }
        for mod in modules:
            ex = mod / "exercises.ipynb"
            fp = mod / "first_principles.ipynb"
            n_prob = n_tier = 0
            code = figs = 0
            if ex.exists():
                text, c, f, _ = notebook_text(ex)
                n_prob = len(PROBLEM_RE.findall(text))
                n_tier = len(TIER_RE.findall(text))
                code += c
                figs += f
            if fp.exists():
                _, c, f, _ = notebook_text(fp)
                code += c
                figs += f
            entry["problems"] += n_prob
            entry["tiers"] += n_tier
            entry["code_cells"] += code
            entry["figures"] += figs
            entry["module_rows"].append(
                {"module": mod.name, "problems": n_prob, "tiers": n_tier,
                 "code_cells": code, "figures": figs}
            )
        rows.append(entry)
    return rows


def markdown_table(rows: list[dict]) -> str:
    lines = ["| Area | Modules | Solved Problems | Code Cells | Figures |",
             "|---|:---:|:---:|:---:|:---:|"]
    for r in rows:
        lines.append(f"| [{r['title']}]({r['area']}/README.md) | {r['modules']} "
                     f"| {r['problems']} | {r['code_cells']} | {r['figures']} |")
    lines.append(f"| **TOTAL** | **{sum(r['modules'] for r in rows)}** "
                 f"| **{sum(r['problems'] for r in rows):,}** "
                 f"| **{sum(r['code_cells'] for r in rows)}** "
                 f"| **{sum(r['figures'] for r in rows)}** |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--markdown", action="store_true", help="emit the README table")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--modules", action="store_true", help="break down per module")
    ap.add_argument("--sync-readme", action="store_true",
                    help="rewrite the table between the markers in README.md")
    args = ap.parse_args()

    rows = scan()

    if args.sync_readme:
        table = markdown_table(rows)
        readme = REPO / "README.md"
        text = readme.read_text(encoding="utf-8")
        start, end = "<!-- curriculum-table:start -->", "<!-- curriculum-table:end -->"
        if start not in text or end not in text:
            print(f"error: {start} / {end} markers not found in README.md", file=sys.stderr)
            return 1
        head, rest = text.split(start, 1)
        _, tail = rest.split(end, 1)
        readme.write_text(f"{head}{start}\n{table}\n{end}{tail}", encoding="utf-8")
        print(f"README.md table synced: {sum(r['modules'] for r in rows)} modules, "
              f"{sum(r['problems'] for r in rows):,} problems")
        return 0

    if args.json:
        print(json.dumps(rows, indent=2))
        return 0

    if args.markdown:
        print(markdown_table(rows))
        return 0

    head = f"{'area':<26}{'mods':>5}{'probs':>7}{'tiers':>7}{'code':>6}{'figs':>6}"
    print(head)
    print("-" * len(head))
    for r in rows:
        print(f"{r['area']:<26}{r['modules']:>5}{r['problems']:>7}{r['tiers']:>7}"
              f"{r['code_cells']:>6}{r['figures']:>6}")
        if args.modules:
            for m in r["module_rows"]:
                print(f"  {m['module']:<24}{'':>5}{m['problems']:>7}{m['tiers']:>7}"
                      f"{m['code_cells']:>6}{m['figures']:>6}")
    print("-" * len(head))
    print(f"{'TOTAL':<26}{sum(r['modules'] for r in rows):>5}"
          f"{sum(r['problems'] for r in rows):>7}{sum(r['tiers'] for r in rows):>7}"
          f"{sum(r['code_cells'] for r in rows):>6}{sum(r['figures'] for r in rows):>6}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
