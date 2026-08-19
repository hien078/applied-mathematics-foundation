#!/usr/bin/env python3
"""Repository content validator.

Checks that every Markdown file and every Jupyter notebook in the repository
renders correctly on GitHub and satisfies the hard requirements in STYLE_GUIDE.md.

Checks performed
----------------
1.  Notebook JSON is valid and passes ``nbformat.validate``.
2.  No stored error outputs in executed notebooks.
3.  Every ``$...$`` / ``$$...$$`` / ```` ```math ```` span compiles under KaTeX
    (requires ``node`` with ``katex`` installed; see ``--node-modules``).
4.  Every ```` ```mermaid ```` block parses under Mermaid.
5.  GitHub-Flavored-Markdown table hazards: raw ``|`` or ``\\|`` inside inline math.
6.  ``<`` immediately followed by a letter inside math.
7.  Unbalanced ``$``/``$$`` delimiters and spaces hugging inline delimiters.
8.  Fenced code blocks that open in one notebook cell and close in another.
9.  Relative links that point at a non-existent path.
10. Colab badge URLs that do not match the notebook's own repository path.

Usage
-----
    python3 tools/validate_content.py                 # validate everything
    python3 tools/validate_content.py linear_algebra  # validate a subtree
    python3 tools/validate_content.py --no-katex      # skip the node-based checks
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
# This guide quotes the very constructs it forbids, so it is not self-validating.
SKIP_FILES = {"STYLE_GUIDE.md", "MODULE_SPEC.md"}

COLAB_PREFIX = (
    "https://colab.research.google.com/github/hien078/"
    "applied-mathematics-foundation/blob/master/"
)

# Constructs KaTeX does not implement, or that break silently on GitHub.
FORBIDDEN_MACROS = [
    r"\iddots",
    r"\argmin",
    r"\argmax",
    r"\bm{",
    r"\DeclareMathOperator",
    r"\eqref",
    r"\label{",
    r"\intertext",
    r"\shortintertext",
]

# Glyphs with no KaTeX metrics: they render as empty boxes inside math.
BARE_GLYPHS = "✓✔✗✘★☆→←⇒⇐≈≠≤≥∈∉⊂⊆∪∩∀∃λμσπθαβγδεΔΣΩ"


@dataclass
class Problem:
    path: str
    where: str
    kind: str
    detail: str

    def __str__(self) -> str:
        return f"{self.path}::{self.where} [{self.kind}] {self.detail}"


@dataclass
class Unit:
    """One addressable chunk of markdown: a whole .md file or one notebook cell."""

    path: str
    where: str
    text: str


@dataclass
class Report:
    problems: list[Problem] = field(default_factory=list)
    math_spans: int = 0
    mermaid_blocks: int = 0
    units: int = 0

    def add(self, path: str, where: str, kind: str, detail: str) -> None:
        self.problems.append(Problem(path, where, kind, detail))


# --------------------------------------------------------------------------- #
# Collection
# --------------------------------------------------------------------------- #


def iter_targets(roots: list[Path]) -> list[Path]:
    out: list[Path] = []
    for root in roots:
        if root.is_file():
            out.append(root)
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [
                d
                for d in dirnames
                if d not in {".git", ".venv", "node_modules", ".ipynb_checkpoints", "__pycache__"}
            ]
            for name in sorted(filenames):
                if name in SKIP_FILES:
                    continue
                if name.endswith((".md", ".ipynb")):
                    out.append(Path(dirpath) / name)
    return sorted(set(out))


def load_units(path: Path, report: Report) -> list[Unit]:
    rel = str(path.relative_to(REPO))
    if path.suffix == ".md":
        return [Unit(rel, "file", path.read_text(encoding="utf-8"))]

    try:
        nb = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.add(rel, "file", "notebook-json", f"invalid JSON: {exc}")
        return []

    try:
        import nbformat

        nbformat.validate(nbformat.reads(json.dumps(nb), as_version=4))
    except ImportError:
        pass
    except Exception as exc:  # nbformat.ValidationError and friends
        report.add(rel, "file", "nbformat", str(exc).splitlines()[0])

    units: list[Unit] = []
    for idx, cell in enumerate(nb.get("cells", [])):
        source = "".join(cell.get("source", []))
        if cell.get("cell_type") == "markdown":
            units.append(Unit(rel, f"cell{idx}", source))
        for out in cell.get("outputs", []) or []:
            if out.get("output_type") == "error":
                report.add(
                    rel,
                    f"cell{idx}",
                    "error-output",
                    f"{out.get('ename')}: {out.get('evalue')}",
                )
    return units


# --------------------------------------------------------------------------- #
# Math extraction
# --------------------------------------------------------------------------- #

FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([A-Za-z0-9_+-]*)\s*$")


def strip_code(text: str) -> tuple[str, list[str], list[tuple[int, str]]]:
    """Split *text* into prose (fences blanked), mermaid blocks, and unclosed fences."""
    lines = text.split("\n")
    prose: list[str] = []
    mermaid: list[str] = []
    open_fence: str | None = None
    open_lang = ""
    buf: list[str] = []
    unclosed: list[tuple[int, str]] = []

    for lineno, line in enumerate(lines, 1):
        m = FENCE_RE.match(line)
        if open_fence is None:
            if m:
                open_fence = m.group(2)
                open_lang = m.group(3).lower()
                buf = []
                prose.append("")
                continue
            prose.append(line)
        else:
            if m and m.group(2)[0] == open_fence[0] and len(m.group(2)) >= len(open_fence):
                if open_lang in {"mermaid"}:
                    mermaid.append("\n".join(buf))
                elif open_lang == "math":
                    mermaid_math.append("\n".join(buf))
                open_fence = None
                open_lang = ""
                prose.append("")
                continue
            buf.append(line)
            prose.append("")

    if open_fence is not None:
        unclosed.append((len(lines), open_lang or "?"))
    return "\n".join(prose), mermaid, unclosed


mermaid_math: list[str] = []

DISPLAY_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
INLINE_RE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.DOTALL)


def extract_math(prose: str) -> tuple[list[str], list[str]]:
    # An escaped ``\$`` is a literal dollar sign in GFM, not a math delimiter.
    prose = prose.replace(r"\$", "\x01")
    display = DISPLAY_RE.findall(prose)
    remainder = DISPLAY_RE.sub(" ", prose)
    inline = INLINE_RE.findall(remainder)
    unescape = lambda spans: [x.replace("\x01", r"\$") for x in spans]
    return unescape(display), unescape(inline)


# --------------------------------------------------------------------------- #
# Static checks
# --------------------------------------------------------------------------- #


def check_unit(unit: Unit, report: Report) -> tuple[list[str], list[str], list[str]]:
    global mermaid_math
    mermaid_math = []
    prose, mermaid, unclosed = strip_code(unit.text)
    fenced_math = list(mermaid_math)

    for _, lang in unclosed:
        report.add(unit.path, unit.where, "unclosed-fence", f"fence '{lang}' never closed in this cell")

    display, inline = extract_math(prose)

    # Balance of $$ and $ (escaped dollars are literals, not delimiters).
    prose = prose.replace(r"\$", "\x01")
    if prose.count("$$") % 2 != 0:
        report.add(unit.path, unit.where, "unbalanced-display", "odd number of '$$'")
    if (prose.replace("$$", "").count("$")) % 2 != 0:
        report.add(unit.path, unit.where, "unbalanced-inline", "odd number of single '$'")

    # Inline delimiters must not hug whitespace.
    for span in inline:
        if span[:1] in " \t" or span[-1:] in " \t":
            report.add(
                unit.path, unit.where, "inline-space", f"space touching '$': {span[:60]!r}"
            )

    # Table-row hazards (only inside a real GFM table block).
    for line in table_rows(prose):
        for span in INLINE_RE.findall(line) + DISPLAY_RE.findall(line):
            if re.search(r"(?<!\\)\|", span):
                report.add(unit.path, unit.where, "table-pipe", f"raw '|' in table math: {span[:60]!r}")
            if r"\|" in span:
                report.add(unit.path, unit.where, "table-norm", f"'\\|' in table math: {span[:60]!r}")

    all_math = display + inline + fenced_math
    for span in all_math:
        if re.search(r"<[A-Za-z]", span):
            report.add(unit.path, unit.where, "lt-letter", f"'<' before a letter: {span[:60]!r}")
        for macro in FORBIDDEN_MACROS:
            if macro in span:
                report.add(unit.path, unit.where, "forbidden-macro", f"{macro} in {span[:50]!r}")
        for ch in span:
            if ch in BARE_GLYPHS:
                report.add(unit.path, unit.where, "bare-glyph", f"{ch!r} inside math: {span[:50]!r}")
                break
        if span.count("{") != span.count("}"):
            report.add(unit.path, unit.where, "brace-imbalance", f"{span[:60]!r}")

    report.math_spans += len(all_math)
    report.mermaid_blocks += len(mermaid)
    report.units += 1
    return display, inline + fenced_math, mermaid


SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$")


def table_rows(prose: str) -> list[str]:
    """Return the lines that GFM will actually parse as table rows.

    A GFM table is a header line, a delimiter line of dashes, then body lines,
    terminated by a blank line or a line without a pipe. Detecting the delimiter
    line is what separates a real table from prose that merely contains ``\|``
    inside a norm such as ``$\|x\|$``.
    """
    lines = prose.split("\n")
    rows: list[str] = []
    i = 0
    while i < len(lines):
        if SEPARATOR_RE.match(lines[i]) and i > 0 and "|" in lines[i - 1]:
            rows.append(lines[i - 1])
            j = i + 1
            while j < len(lines) and lines[j].strip() and "|" in lines[j]:
                rows.append(lines[j])
                j += 1
            i = j
            continue
        i += 1
    return rows


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)#\s]+)(?:#[^)\s]*)?\)")


def check_links(unit: Unit, report: Report) -> None:
    base = (REPO / unit.path).parent
    for target in LINK_RE.findall(unit.text):
        if target.startswith(("http://", "https://", "mailto:", "//", "data:")):
            continue
        resolved = (base / target).resolve()
        if not resolved.exists():
            report.add(unit.path, unit.where, "broken-link", target)


def check_colab(path: Path, report: Report) -> None:
    rel = str(path.relative_to(REPO))
    text = path.read_text(encoding="utf-8")
    if "colab.research.google.com" not in text:
        report.add(rel, "cell0", "colab-missing", "no Colab badge")
        return
    expected = COLAB_PREFIX + rel
    if expected not in text:
        report.add(rel, "cell0", "colab-path", f"badge does not point at {expected}")


# --------------------------------------------------------------------------- #
# Node-backed rendering checks
# --------------------------------------------------------------------------- #

NODE_SCRIPT = r"""
const fs = require('fs');
const katex = require('katex');
const payload = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const out = [];
for (const item of payload.math) {
  try {
    katex.renderToString(item.src, {displayMode: item.display, throwOnError: true,
                                    strict: false, trust: true});
  } catch (e) {
    out.push({id: item.id, kind: 'katex', msg: String(e.message).slice(0, 200)});
  }
}
(async () => {
  if (payload.mermaid.length) {
    try {
      const {JSDOM} = require('jsdom');
      const dom = new JSDOM('<!doctype html><body></body>', {pretendToBeVisual: true});
      global.window = dom.window; global.document = dom.window.document;
      global.navigator = dom.window.navigator;
      global.DOMPurify = undefined;
      const mermaid = require('mermaid').default || require('mermaid');
      mermaid.initialize({startOnLoad: false});
      for (const item of payload.mermaid) {
        try { await mermaid.parse(item.src); }
        catch (e) { out.push({id: item.id, kind: 'mermaid', msg: String(e.message || e).slice(0, 200)}); }
      }
    } catch (e) {
      out.push({id: -1, kind: 'mermaid-setup', msg: String(e.message || e).slice(0, 200)});
    }
  }
  process.stdout.write(JSON.stringify(out));
})();
"""


def run_node(items: list[dict], mermaid: list[dict], node_modules: Path) -> list[dict]:
    if not items and not mermaid:
        return []
    with tempfile.TemporaryDirectory() as td:
        payload = Path(td) / "payload.json"
        payload.write_text(json.dumps({"math": items, "mermaid": mermaid}), encoding="utf-8")
        script = Path(td) / "check.js"
        script.write_text(NODE_SCRIPT, encoding="utf-8")
        env = dict(os.environ, NODE_PATH=str(node_modules))
        proc = subprocess.run(
            ["node", str(script), str(payload)],
            capture_output=True,
            text=True,
            env=env,
            cwd=str(node_modules.parent),
        )
    if proc.returncode != 0:
        print(f"  ! node checker failed: {proc.stderr.strip()[:400]}", file=sys.stderr)
        return []
    try:
        return json.loads(proc.stdout or "[]")
    except json.JSONDecodeError:
        print(f"  ! node checker returned junk: {proc.stdout[:200]}", file=sys.stderr)
        return []


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", default=[], help="files or directories (default: repo root)")
    parser.add_argument("--no-katex", action="store_true", help="skip node-backed rendering checks")
    parser.add_argument(
        "--node-modules",
        default=os.environ.get("VALIDATE_NODE_MODULES", ""),
        help="directory containing katex/mermaid/jsdom (default: $VALIDATE_NODE_MODULES)",
    )
    parser.add_argument("--quiet", action="store_true", help="print only the summary")
    args = parser.parse_args()

    roots = [Path(p).resolve() for p in args.paths] or [REPO]
    targets = iter_targets(roots)
    report = Report()

    math_items: list[dict] = []
    mermaid_items: list[dict] = []
    index: dict[int, tuple[str, str]] = {}

    for path in targets:
        units = load_units(path, report)
        if path.suffix == ".ipynb":
            check_colab(path, report)
        for unit in units:
            display, inline, mermaid = check_unit(unit, report)
            check_links(unit, report)
            if args.no_katex:
                continue
            for src in display:
                i = len(math_items) + len(mermaid_items)
                index[i] = (unit.path, unit.where)
                math_items.append({"id": i, "src": src, "display": True})
            for src in inline:
                i = len(math_items) + len(mermaid_items)
                index[i] = (unit.path, unit.where)
                math_items.append({"id": i, "src": src, "display": False})
            for src in mermaid:
                i = len(math_items) + len(mermaid_items)
                index[i] = (unit.path, unit.where)
                mermaid_items.append({"id": i, "src": src})

    if not args.no_katex:
        nm = Path(args.node_modules) if args.node_modules else None
        if nm is None or not nm.exists():
            print(
                "warning: node_modules with katex/mermaid/jsdom not found; "
                "pass --node-modules or set VALIDATE_NODE_MODULES to enable render checks",
                file=sys.stderr,
            )
        else:
            for failure in run_node(math_items, mermaid_items, nm):
                path, where = index.get(failure["id"], ("?", "?"))
                report.add(path, where, failure["kind"], failure["msg"])

    by_kind: dict[str, int] = {}
    for problem in report.problems:
        by_kind[problem.kind] = by_kind.get(problem.kind, 0) + 1

    if not args.quiet:
        for problem in sorted(report.problems, key=lambda p: (p.kind, p.path, p.where)):
            print(problem)

    print()
    print(f"files checked      : {len(targets)}")
    print(f"markdown units     : {report.units}")
    print(f"math spans         : {report.math_spans}")
    print(f"mermaid blocks     : {report.mermaid_blocks}")
    print(f"problems           : {len(report.problems)}")
    for kind, count in sorted(by_kind.items(), key=lambda kv: -kv[1]):
        print(f"  {kind:<20} {count}")

    return 1 if report.problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
