#!/usr/bin/env python3
"""Export curriculum modules to structured JSON for downstream applications.

The repository is authored as Markdown and notebooks because that is what renders on GitHub
and runs on Colab. An application should not parse `.ipynb`. This tool turns each module into
one JSON document with an explicit schema, plus the figures as PNG files.

Usage
-----
    python3 tools/export_json.py linear_algebra -o build/
    python3 tools/export_json.py --all -o build/
    python3 tools/export_json.py linear_algebra --report   # coverage only, write nothing

Output layout
-------------
    build/index.json                       every module's metadata and the prerequisite edges
    build/<area>/<NN_slug>.json            one module
    build/<area>/<NN_slug>/fig-<n>.png     figures referenced from the module JSON

Anything that fails to parse is reported, never silently dropped. Exit code is non-zero when
coverage is incomplete, so a build can gate on it.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCHEMA_VERSION = "1.0"

SECTION_RE = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s*$", re.MULTILINE)
# `### Theorem 4.1 — Title`, `### Theorem 4.1 (Title)`, and `### Theorem 4.1` all occur.
OBJECT_RE = re.compile(
    r"^###\s+(Definition|Theorem|Proposition|Lemma|Corollary|Proof|Example|Algorithm|Remark)"
    r"\s+([\d.]+)\s*(?:[—–:-]\s*(.*?)|\((.*?)\))?\s*$",
    re.MULTILINE,
)
# The title is optional: most modules write `### Problem L0.1 — Title`, a few write
# `### Problem L0.1` alone.
PROBLEM_RE = re.compile(
    r"^###\s+Problem\s+(L([0-3])\.(\d+))\s*(?:[—–:.-]\s*(.+?))?\s*$", re.MULTILINE)
TIER_RE = re.compile(r"^##\s+(L[0-3])\s*[—–-]\s*(.+?)\s*$", re.MULTILINE)

# The repository grew several block dialects: bold-with-period (`**Statement.**`),
# bold-with-colon (`**Problem Statement:**`), italic (`*Intuition:*`), h4 headings
# (`#### First-Principles Intuition`) and blockquoted (`> **Key Takeaway:**`). Content may
# sit on the same line as its label or on the next. Rather than one regex per dialect,
# locate every KNOWN label, then slice the text between consecutive labels. Only known
# labels count as boundaries, so ordinary bold text inside a solution is never mistaken
# for one.
FIELD_LABELS = {
    "statement": [r"Problem\s+Statement", r"Statement", r"Problem"],
    "intuition": [r"(?:First[-\s]Principles\s+)?Intuition(?:\s*[/&]\s*[\w\s]+)?",
                  r"Idea", r"Setup", r"Why\s+this\s+matters"],
    "solution": [r"(?:Step[-\s]by[-\s]Step\s+)?Solution(?:\s*[&/]\s*Proof)?",
                 r"Proof(?:\s*[&/]\s*Solution)?", r"Derivation", r"Working", r"Answer"],
    "takeaway": [r"Key\s+Insight\s*/\s*Takeaway", r"Key\s+Takeaway", r"Takeaway",
                 r"Key\s+Insight", r"Key\s+idea", r"Lesson"],
}

_ALT = "|".join(p for pats in FIELD_LABELS.values() for p in pats)
# line start, optional decoration, a known label, optional trailing punctuation/decoration
BOUNDARY_RE = re.compile(
    rf"^[ \t]{{0,3}}(?:>[ \t]*)?(?:\*\*|\*|#{{3,6}}[ \t]+)?[ \t]*"
    rf"(?P<label>{_ALT})"
    rf"[ \t]*[.:]?[ \t]*(?:\*\*|\*)?[ \t]*[.:]?",
    re.MULTILINE | re.IGNORECASE,
)


def extract_fields(body: str) -> dict[str, str | None]:
    hits = []
    for m in BOUNDARY_RE.finditer(body):
        label = m.group("label")
        for field, patterns in FIELD_LABELS.items():
            if any(re.fullmatch(p, label, re.IGNORECASE) for p in patterns):
                hits.append((field, m.start(), m.end()))
                break

    found: dict[str, str | None] = {k: None for k in FIELD_LABELS}
    for i, (field, start, end) in enumerate(hits):
        stop = hits[i + 1][1] if i + 1 < len(hits) else len(body)
        if found[field] is None:
            text = body[end:stop].strip()
            if text:
                found[field] = text

    # A problem with no statement label still has one: the text before the first label.
    if found["statement"] is None:
        lead = (body[: hits[0][1]] if hits else body).strip()
        if lead:
            found["statement"] = lead
    return found


def boxed_answer(body: str) -> str | None:
    r"""Extract the content of the first `\boxed{...}`, matching braces properly.

    `$$\boxed{x}$$` is only the simplest form; the repository also writes
    `$$\text{Result: } \boxed{x}$$` and puts the box inside an aligned block, so anchoring
    on `$$` fails. Scan for the macro and balance its braces instead.
    """
    i = body.find(r"\boxed{")
    if i < 0:
        return None
    j = i + len(r"\boxed{")
    depth = 1
    while j < len(body) and depth:
        if body[j] == "{":
            depth += 1
        elif body[j] == "}":
            depth -= 1
        j += 1
    return body[i + len(r"\boxed{"): j - 1].strip() if depth == 0 else None


class Coverage:
    def __init__(self) -> None:
        self.problems = 0
        self.missing: dict[str, int] = {}
        self.notes: list[str] = []

    def miss(self, field: str) -> None:
        self.missing[field] = self.missing.get(field, 0) + 1

    def note(self, msg: str) -> None:
        self.notes.append(msg)


def cells(nb: dict, kind: str | None = None) -> list[dict]:
    return [c for c in nb.get("cells", []) if kind is None or c.get("cell_type") == kind]


def src(cell: dict) -> str:
    return "".join(cell.get("source", []))


def text_outputs(cell: dict) -> str:
    out = []
    for o in cell.get("outputs", []) or []:
        if o.get("output_type") == "stream":
            out.append("".join(o.get("text", [])))
        elif "text/plain" in (o.get("data") or {}):
            out.append("".join(o["data"]["text/plain"]))
    return "".join(out).rstrip()


def png_outputs(cell: dict) -> list[str]:
    return [
        o["data"]["image/png"]
        for o in cell.get("outputs", []) or []
        if "image/png" in (o.get("data") or {})
    ]


# --------------------------------------------------------------------------- theory


def parse_theory(nb: dict, out_dir: Path, write: bool, cov: Coverage) -> dict:
    md = "\n\n".join(src(c) for c in cells(nb, "markdown"))

    sections = []
    marks = list(SECTION_RE.finditer(md))
    for i, m in enumerate(marks):
        body = md[m.end(): marks[i + 1].start() if i + 1 < len(marks) else len(md)]
        sections.append({"number": int(m.group(1)), "title": m.group(2), "body": body.strip()})
    if len(sections) != 10:
        cov.note(f"theory has {len(sections)} numbered sections, expected 10")

    objects = []
    omarks = list(OBJECT_RE.finditer(md))
    for i, m in enumerate(omarks):
        body = md[m.end(): omarks[i + 1].start() if i + 1 < len(omarks) else len(md)]
        objects.append({
            "kind": m.group(1),
            "number": m.group(2),
            "title": (m.group(3) or m.group(4) or "").strip(),
            "body": body.strip(),
        })

    code, figures = [], []
    for i, c in enumerate(cells(nb, "code")):
        entry = {"index": i, "source": src(c), "stdout": text_outputs(c)}
        pngs = png_outputs(c)
        for j, b64 in enumerate(pngs):
            name = f"fig-{len(figures) + 1}.png"
            if write:
                out_dir.mkdir(parents=True, exist_ok=True)
                (out_dir / name).write_bytes(base64.b64decode(b64))
            figures.append({"file": name, "from_code_cell": i})
        entry["figures"] = [f["file"] for f in figures[len(figures) - len(pngs):]]
        code.append(entry)

    return {"sections": sections, "objects": objects, "code": code, "figures": figures}


# --------------------------------------------------------------------------- problems


def parse_problems(nb: dict, cov: Coverage) -> list[dict]:
    """Collect each problem from the heading cell through every cell before the next problem.

    Areas differ: some keep statement, solution and takeaway in one markdown cell, others
    split them across several, with the checking code cell in between. Accumulate until the
    next `### Problem` heading appears.
    """
    problems: list[dict] = []
    tier_titles: dict[str, str] = {}
    groups: list[dict] = []          # {"head": match, "md": [...], "code": [...]}
    current: dict | None = None

    for c in nb.get("cells", []):
        s = src(c)
        if c.get("cell_type") == "markdown":
            for t in TIER_RE.finditer(s):
                tier_titles[t.group(1)] = t.group(2)
            m = PROBLEM_RE.search(s)
            if m:
                current = {"head": m, "md": [s[m.end():]], "code": []}
                groups.append(current)
                continue
            if current is not None:
                current["md"].append(s)
        elif c.get("cell_type") == "code" and current is not None:
            current["code"].append({"source": s, "stdout": text_outputs(c)})

    for g in groups:
        m = g["head"]
        body = "\n\n".join(g["md"])
        p = {
            "id": m.group(1),
            "tier": f"L{m.group(2)}",
            "number": int(m.group(3)),
            "title": (m.group(4) or "").strip() or None,
            "checks": g["code"],
        }
        for field, value in extract_fields(body).items():
            p[field] = value
            if value is None:
                cov.miss(field)
        p["answer"] = boxed_answer(body)
        if p["answer"] is None:
            cov.miss("answer")
        p["tier_title"] = tier_titles.get(p["tier"])
        problems.append(p)
        cov.problems += 1

    return problems


# --------------------------------------------------------------------------- readme


def parse_readme(path: Path) -> dict:
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    title_m = re.search(r"^#\s+(.+?)\s*$", text, re.MULTILINE)

    def links_under(block: str) -> list[dict]:
        """Module links in a block, ignoring links into docs/ or to files."""
        out = []
        for label, href in re.findall(r"\[([^\]]+)\]\((\.{1,2}/[^)]+)\)", block):
            if "/docs/" in href or href.endswith(".md"):
                continue
            out.append({"label": label.strip(), "path": href.strip("/").rstrip("/")})
        return out

    prereqs, downstream = [], []
    pre_sec = re.search(r"^##\s+.*Prerequisit.*?$(.*?)(?=^## |\Z)", text,
                        re.MULTILINE | re.DOTALL)
    if pre_sec:
        block = pre_sec.group(1)
        # the section holds two labelled halves; split on the downstream heading
        split = re.split(r"\*\*Downstream[^*]*\*\*", block, maxsplit=1)
        prereqs = links_under(split[0])
        downstream = links_under(split[1]) if len(split) > 1 else []

    mermaid = re.findall(r"```mermaid\n(.*?)```", text, re.DOTALL)

    def table_after(pattern: str) -> list[list[str]]:
        m = re.search(pattern + r"[^\n]*$(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
        if not m:
            return []
        rows = []
        for line in m.group(1).split("\n"):
            if line.strip().startswith("|") and not re.match(r"^\s*\|[\s:|-]+\|\s*$", line):
                rows.append([c.strip() for c in line.strip().strip("|").split("|")])
        return rows[1:] if rows else []

    return {
        "title": title_m.group(1) if title_m else None,
        "prerequisites": prereqs,
        "downstream": downstream,
        "concept_map": mermaid[0].strip() if mermaid else None,
        "notation": table_after(r"^##\s+.*Notation"),
        "core_results": table_after(r"^##\s+(?:.*\s)?(?:Core|Main|Key) results"),
        "references": [
            l.strip("- ").strip()
            for l in (re.search(r"^##\s+.*References.*?$(.*)", text, re.MULTILINE | re.DOTALL)
                      or re.match("", "")).group(1).split("\n")
            if l.strip().startswith("-")
        ] if re.search(r"^##\s+.*References", text, re.MULTILINE) else [],
    }


# --------------------------------------------------------------------------- driver


def export_module(mod: Path, out_root: Path, write: bool) -> tuple[dict, Coverage]:
    cov = Coverage()
    area, name = mod.parent.name, mod.name
    fp = json.loads((mod / "first_principles.ipynb").read_text(encoding="utf-8"))
    ex = json.loads((mod / "exercises.ipynb").read_text(encoding="utf-8"))

    fig_dir = out_root / area / name
    doc = {
        "schema_version": SCHEMA_VERSION,
        "area": area,
        "module": name,
        "index": int(name[:2]),
        "readme": parse_readme(mod / "README.md"),
        "theory": parse_theory(fp, fig_dir, write, cov),
        "problems": parse_problems(ex, cov),
    }
    counts: dict[str, int] = {}
    for p in doc["problems"]:
        counts[p["tier"]] = counts.get(p["tier"], 0) + 1
    doc["problem_counts"] = counts

    if write:
        (out_root / area).mkdir(parents=True, exist_ok=True)
        (out_root / area / f"{name}.json").write_text(
            json.dumps(doc, indent=1, ensure_ascii=False), encoding="utf-8")
    return doc, cov


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("areas", nargs="*", help="area names, e.g. linear_algebra")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("-o", "--out", default="build")
    ap.add_argument("--report", action="store_true", help="parse and report, write nothing")
    args = ap.parse_args()

    areas = (sorted(p.name for p in REPO.iterdir()
                    if p.is_dir() and any(q.is_dir() and re.match(r"^\d\d_", q.name)
                                          for q in p.iterdir()))
             if args.all else args.areas)
    if not areas:
        ap.error("give one or more area names, or --all")

    out_root = (REPO / args.out).resolve()
    write = not args.report
    index, problems, missing_total = [], 0, 0

    for area in areas:
        mods = sorted(p for p in (REPO / area).iterdir()
                      if p.is_dir() and re.match(r"^\d\d_", p.name))
        for mod in mods:
            doc, cov = export_module(mod, out_root, write)
            problems += cov.problems
            miss = sum(cov.missing.values())
            missing_total += miss
            flag = "" if not (miss or cov.notes) else "   <-- " + ", ".join(
                [f"{k}x{v}" for k, v in cov.missing.items()] + cov.notes)
            print(f"  {area}/{mod.name:<46} problems={cov.problems:>3} "
                  f"objects={len(doc['theory']['objects']):>3} "
                  f"figs={len(doc['theory']['figures'])}{flag}")
            index.append({
                "area": area, "module": mod.name, "index": doc["index"],
                "title": doc["readme"].get("title"),
                "prerequisites": doc["readme"].get("prerequisites", []),
                "downstream": doc["readme"].get("downstream", []),
                "problem_counts": doc["problem_counts"],
                "path": f"{area}/{mod.name}.json",
            })

    if write:
        out_root.mkdir(parents=True, exist_ok=True)
        (out_root / "index.json").write_text(
            json.dumps({"schema_version": SCHEMA_VERSION, "modules": index},
                       indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"\n  modules: {len(index)}   problems: {problems}   "
          f"unparsed fields: {missing_total}")
    if write:
        print(f"  written to {out_root}")
    return 1 if missing_total else 0


if __name__ == "__main__":
    raise SystemExit(main())
