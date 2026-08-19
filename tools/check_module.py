#!/usr/bin/env python3
"""Structural gate for one curriculum module.

`validate_content.py` answers "does it render?". This answers "does it meet the module
contract in STYLE_GUIDE.md section 20 and 21?" — the definition of done for an upgrade.

Usage
-----
    python3 tools/check_module.py linear_algebra/06_eigenvalues_eigenvectors_spectral_theory
    python3 tools/check_module.py --all            # every module, summary table
    python3 tools/check_module.py --all --failing  # only modules with failures
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# STYLE_GUIDE section 20: the eleven README items, matched loosely on the heading text.
README_SECTIONS = [
    ("overview", r"^#\s"),
    ("note callout", r"^>\s*\[!NOTE\]"),
    ("prerequisites", r"^##\s.*\bPrerequisit"),
    ("downstream", r"\bDownstream\b|\bUnlocks\b|\bLeads to\b"),
    ("learning outcomes", r"^##\s.*\b(Learning outcomes|What you will be able to do)\b"),
    ("concept map", r"```mermaid"),
    ("notation table", r"^##\s.*\bNotation\b"),
    ("core results", r"^##\s.*\b(Core results|Main results|Key results)\b"),
    ("misconceptions", r"^##\s.*\bMisconception"),
    ("exercise index", r"^##\s.*\bExercise"),
    ("references", r"^##\s.*\bReferences\b"),
]

# STYLE_GUIDE section 5 / upgrade recipe item 3: the theory-notebook skeleton.
FP_SECTIONS = [
    r"^##\s*1\.\s*Why This Module Exists",
    r"^##\s*2\.\s*Intuition",
    r"^##\s*3\.\s*Definitions",
    r"^##\s*4\.\s*Main Results",
    r"^##\s*5\.\s*Derivations and Proofs",
    r"^##\s*6\.\s*Worked Examples",
    r"^##\s*7\.\s*Computational Practice",
    r"^##\s*8\.\s*Applications",
    r"^##\s*9\.\s*Key Takeaways",
    r"^##\s*10\.\s*References",
]

TIERS = [
    r"^##\s*L0\s*[-—–]\s*Concept Checks",
    r"^##\s*L1\s*[-—–]\s*Foundations",
    r"^##\s*L2\s*[-—–]\s*Applications",
    r"^##\s*L3\s*[-—–]\s*Challenge Proofs",
]

# Headings retired by STYLE_GUIDE section 5.
RETIRED = [
    r"^##\s*\d*\.?\s*Phenomenon\b",
    r"^##\s*\d*\.?\s*Units and Dimensions\b",
    r"^##\s*\d*\.?\s*Domain Constraints\b",
    r"^##\s*\d*\.?\s*Variables and Parameters\b",
    r"^##\s*(Foundation|Understanding|Advanced|Olympiad|Research)\s*Level\b",
]

PROBLEM_RE = re.compile(r"^#{3,4}\s*Problem\s+L[0-3]\.\d+", re.MULTILINE)
ANY_PROBLEM_RE = re.compile(
    r"^#{3,4}[ \t]*(?:Exercise|Problem)[ \t]+(?=[0-9LP])"
    r"|^#{3,4}[ \t]*(?:L[0-3]|P)[ \t]*[0-9.]+",
    re.MULTILINE,
)
PROSE_TOPIC_RE = re.compile(r"(?<!\[)\bTopic\s+\d\d\b(?!\])")
MD_SIBLING_RE = re.compile(r"`?(first_principles|exercises)\.md`?")


class Module:
    def __init__(self, path: Path):
        self.path = path
        self.rel = str(path.relative_to(REPO))
        self.fail: list[str] = []
        self.warn: list[str] = []

    def bad(self, msg: str) -> None:
        self.fail.append(msg)

    def soft(self, msg: str) -> None:
        self.warn.append(msg)


def read_nb(path: Path) -> tuple[str, list[dict]]:
    nb = json.loads(path.read_text(encoding="utf-8"))
    cells = nb.get("cells", [])
    md = "\n".join(
        "".join(c.get("source", [])) for c in cells if c.get("cell_type") == "markdown"
    )
    return md, cells


def count_figures(cells: list[dict]) -> int:
    n = 0
    for c in cells:
        for out in c.get("outputs", []) or []:
            if "image/png" in (out.get("data") or {}):
                n += 1
    return n


def check(mod_dir: Path) -> Module:
    m = Module(mod_dir)
    readme = mod_dir / "README.md"
    fp = mod_dir / "first_principles.ipynb"
    ex = mod_dir / "exercises.ipynb"

    for f in (readme, fp, ex):
        if not f.exists():
            m.bad(f"missing {f.name}")
    if m.fail:
        return m

    # ---- README ------------------------------------------------------------
    rtext = readme.read_text(encoding="utf-8")
    for name, pat in README_SECTIONS:
        if not re.search(pat, rtext, re.MULTILINE | re.IGNORECASE):
            m.bad(f"README missing section: {name}")

    for hit in set(MD_SIBLING_RE.findall(rtext)):
        if not (mod_dir / f"{hit}.md").exists():
            m.bad(f"README references {hit}.md which does not exist")

    for hit in set(PROSE_TOPIC_RE.findall(rtext)):
        m.soft(f"README uses prose cross-reference {hit!r} instead of a relative link")

    # ---- first_principles.ipynb -------------------------------------------
    fp_md, fp_cells = read_nb(fp)
    code_cells = [c for c in fp_cells if c.get("cell_type") == "code"]
    figs = count_figures(fp_cells)

    if len(code_cells) < 6:
        m.bad(f"first_principles has {len(code_cells)} code cells, contract requires at least 6")
    if not 2 <= figs <= 4:
        m.bad(f"first_principles has {figs} figures, contract requires 2 to 4")
    for pat in FP_SECTIONS:
        if not re.search(pat, fp_md, re.MULTILINE):
            m.bad("first_principles missing heading: " + pat.strip("^$").replace(r"\s*", " "))
    for pat in RETIRED:
        if re.search(pat, fp_md, re.MULTILINE | re.IGNORECASE):
            m.bad("first_principles still uses a retired heading: " + pat.strip("^"))
    # `rng = np.random.default_rng(0)` is the STYLE_GUIDE section 21 preamble and is required
    # verbatim; every other np.random.* entry point touches global state and is forbidden.
    fp_code = "\n".join("".join(c.get("source", [])) for c in code_cells)
    if re.search(r"np\.random\.(?!default_rng\b)", fp_code):
        m.bad("first_principles calls np.random.* directly; seed through rng only")
    for i, c in enumerate(fp_cells):
        for out in c.get("outputs", []) or []:
            if out.get("output_type") == "error":
                m.bad(f"first_principles cell {i} stores an error output: {out.get('ename')}")

    # ---- exercises.ipynb ---------------------------------------------------
    ex_md, ex_cells = read_nb(ex)
    for pat in TIERS:
        if not re.search(pat, ex_md, re.MULTILINE):
            m.bad("exercises missing tier heading: " + pat.strip("^$").replace(r"\s*", " "))
    for pat in RETIRED:
        if re.search(pat, ex_md, re.MULTILINE | re.IGNORECASE):
            m.bad("exercises still uses a retired tier name: " + pat.strip("^"))
    for i, c in enumerate(ex_cells):
        for out in c.get("outputs", []) or []:
            if out.get("output_type") == "error":
                m.bad(f"exercises cell {i} stores an error output: {out.get('ename')}")

    n_problems = len(PROBLEM_RE.findall(ex_md))
    n_any = len(ANY_PROBLEM_RE.findall(ex_md))
    if n_problems != n_any:
        m.bad(f"exercises: {n_any} problem headings but only {n_problems} use the "
              f"'### Problem L<t>.<n>' form")

    # README's stated count must equal reality.
    stated = [int(x) for x in re.findall(r"(\d+)\s*(?:problems|Problems)", rtext)]
    if stated and n_any and not any(s == n_any for s in stated):
        m.bad(f"README states problem counts {stated} but exercises contains {n_any}")

    return m


# Sentences an area README must not keep once its modules are upgraded.
STALE_CLAIMS = [
    (r"markdown[ -]only", "claims its notebooks are markdown-only"),
    (r"zero code cells|no code cells|0 code cells", "claims there are no code cells"),
    (r"zero figures|no figures|0 figures", "claims there are no figures"),
    (r"Foundation, Understanding, Advanced", "claims the legacy five-level tier naming"),
    (r"missing prerequisites|no prerequisites block", "claims module READMEs lack prerequisites"),
]


def check_area(area: Path) -> Module:
    """An area README must agree with the modules underneath it."""
    m = Module(area)
    readme = area / "README.md"
    if not readme.exists():
        m.bad("missing README.md")
        return m
    text = readme.read_text(encoding="utf-8")

    mods = sorted(p for p in area.iterdir() if p.is_dir() and re.match(r"^\d\d_", p.name))
    real_total = 0
    upgraded = 0
    for mod in mods:
        ex = mod / "exercises.ipynb"
        if not ex.exists():
            continue
        md, _ = read_nb(ex)
        real_total += len(ANY_PROBLEM_RE.findall(md))
        if not check(mod).fail:
            upgraded += 1

    stated = {int(x.replace(",", "")) for x in re.findall(r"\*\*([\d,]{2,6})\*\*", text)}
    if real_total and stated and real_total not in stated:
        m.bad(f"README states totals {sorted(stated)} but the modules hold {real_total} problems")

    if upgraded == len(mods) and mods:
        for pat, why in STALE_CLAIMS:
            if re.search(pat, text, re.IGNORECASE):
                m.bad(f"every module here passes, but the README still {why}")
    return m


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("module", nargs="?", help="path to a module directory")
    ap.add_argument("--all", action="store_true", help="check every module")
    ap.add_argument("--areas", action="store_true", help="check area READMEs against their modules")
    ap.add_argument("--failing", action="store_true", help="with --all, list only failures")
    args = ap.parse_args()

    if args.areas:
        areas = sorted(
            p for p in REPO.iterdir()
            if p.is_dir() and not p.name.startswith(".")
            and any(q.is_dir() and re.match(r"^\d\d_", q.name) for q in p.iterdir())
        )
        rows = [check_area(a) for a in areas]
        for r in rows:
            print(f"{'PASS' if not r.fail else f'FAIL ({len(r.fail)})':<10} {r.rel}")
            for x in r.fail:
                print(f"    x {x}")
        ok = sum(1 for r in rows if not r.fail)
        print(f"\nareas: {len(rows)}   passing: {ok}   failing: {len(rows) - ok}")
        return 0 if ok == len(rows) else 1

    if args.all:
        mods = sorted(
            p for area in REPO.iterdir() if area.is_dir() and not area.name.startswith(".")
            for p in area.iterdir() if p.is_dir() and re.match(r"^\d\d_", p.name)
        )
    elif args.module:
        mods = [Path(args.module).resolve()]
    else:
        ap.error("give a module path or --all")

    results = [check(p) for p in mods]
    total_fail = 0
    for m in results:
        total_fail += len(m.fail)
        if args.all and args.failing and not m.fail:
            continue
        status = "PASS" if not m.fail else f"FAIL ({len(m.fail)})"
        print(f"{status:<10} {m.rel}")
        if not args.all or not args.failing or m.fail:
            for x in m.fail:
                print(f"    x {x}")
            for x in m.warn:
                print(f"    ! {x}")

    passed = sum(1 for m in results if not m.fail)
    print(f"\nmodules: {len(results)}   passing: {passed}   failing: {len(results) - passed}"
          f"   total failures: {total_fail}")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
