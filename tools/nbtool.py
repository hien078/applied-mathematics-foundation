#!/usr/bin/env python3
r"""Notebook authoring helper.

Hand-splicing notebook JSON silently corrupts LaTeX: a single ``\right`` written into a
JSON string decodes as carriage-return + ``ight``. This tool removes the hazard by keeping
notebooks in a flat percent-delimited text form and doing every JSON conversion through
``nbformat``.

Text form
---------
A notebook is a plain text file whose cells are separated by marker lines::

    # %% [markdown]
    ## Why eigenvalues exist

    A linear map usually rotates a vector...

    # %% [code]
    import numpy as np
    A = np.array([[2.0, 1.0], [1.0, 2.0]])
    print(np.linalg.eigvalsh(A))

Backslashes are literal, so ``$\Vert x \Vert$`` survives untouched. Write these files with a
quoted heredoc (``<<'EOF'``) so the shell does not touch them either.

Commands
--------
    tools/nbtool.py to-text  NOTEBOOK.ipynb [-o OUT.txt]
        Dump an existing notebook to the text form, for reading or editing.

    tools/nbtool.py from-text SOURCE.txt -o NOTEBOOK.ipynb [--no-colab]
        Build a notebook. A Colab badge cell is prepended automatically unless the first
        cell already contains one.

    tools/nbtool.py exec NOTEBOOK.ipynb [--timeout N] [--python PATH]
        Run every code cell from a fresh kernel and save the outputs in place.
        Fails loudly if any cell raises.

    tools/nbtool.py check NOTEBOOK.ipynb
        nbformat validation plus a scan for stored error outputs.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COLAB_PREFIX = (
    "https://colab.research.google.com/github/hien078/"
    "applied-mathematics-foundation/blob/master/"
)
BADGE = "[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"

MARKER_RE = re.compile(r"^# %% \[(markdown|code|raw)\]\s*$")


def parse_text(text: str) -> list[tuple[str, str]]:
    cells: list[tuple[str, str]] = []
    kind: str | None = None
    buf: list[str] = []

    for line in text.split("\n"):
        m = MARKER_RE.match(line)
        if m:
            if kind is not None:
                cells.append((kind, "\n".join(buf).strip("\n")))
            kind = m.group(1)
            buf = []
            continue
        if kind is None:
            if line.strip():
                raise SystemExit(
                    "error: content before the first '# %% [markdown]' marker:\n  " + line
                )
            continue
        buf.append(line)

    if kind is not None:
        cells.append((kind, "\n".join(buf).strip("\n")))
    if not cells:
        raise SystemExit("error: no cells found; is the marker line exactly '# %% [markdown]'?")
    return cells


def build(cells: list[tuple[str, str]], colab_rel: str | None) -> "object":
    import nbformat

    nb = nbformat.v4.new_notebook()
    out = []

    if colab_rel:
        first = cells[0][1] if cells else ""
        if "colab.research.google.com" not in first:
            badge = f"{BADGE}({COLAB_PREFIX}{colab_rel})"
            out.append(nbformat.v4.new_markdown_cell(badge + "\n\n" + first))
            cells = cells[1:]

    for kind, src in cells:
        if not src.strip():
            continue
        if kind == "markdown":
            out.append(nbformat.v4.new_markdown_cell(src))
        elif kind == "code":
            out.append(nbformat.v4.new_code_cell(src))
        else:
            out.append(nbformat.v4.new_raw_cell(src))

    nb.cells = out
    nb.metadata = {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "pygments_lexer": "ipython3"},
    }
    nbformat.validate(nb)
    return nb


def to_text(path: Path) -> str:
    nb = json.loads(path.read_text(encoding="utf-8"))
    chunks = []
    for cell in nb.get("cells", []):
        kind = cell.get("cell_type", "markdown")
        chunks.append(f"# %% [{kind}]\n" + "".join(cell.get("source", [])).rstrip("\n"))
    return "\n\n".join(chunks) + "\n"


def cmd_to_text(args: argparse.Namespace) -> int:
    text = to_text(Path(args.notebook))
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"wrote {args.output}")
    else:
        sys.stdout.write(text)
    return 0


def cmd_from_text(args: argparse.Namespace) -> int:
    import nbformat

    src = Path(args.source).read_text(encoding="utf-8")
    dest = Path(args.output).resolve()
    colab_rel = None
    if not args.no_colab:
        try:
            colab_rel = str(dest.relative_to(REPO))
        except ValueError:
            colab_rel = None
    nb = build(parse_text(src), colab_rel)
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8") as fh:
        nbformat.write(nb, fh)
    md = sum(1 for c in nb.cells if c.cell_type == "markdown")
    code = sum(1 for c in nb.cells if c.cell_type == "code")
    print(f"wrote {dest.relative_to(REPO) if dest.is_relative_to(REPO) else dest}: "
          f"{md} markdown + {code} code cells")
    return 0


def cmd_exec(args: argparse.Namespace) -> int:
    import nbformat
    from nbclient import NotebookClient

    path = Path(args.notebook).resolve()
    nb = nbformat.read(path, as_version=4)
    resources = {"metadata": {"path": str(path.parent)}}
    kwargs = {"timeout": args.timeout, "kernel_name": "python3", "resources": resources}
    if args.python:
        kwargs["kernel_manager_class"] = None
    client = NotebookClient(nb, **{k: v for k, v in kwargs.items() if v is not None})
    try:
        client.execute()
    except Exception as exc:
        print(f"EXECUTION FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        with path.open("w", encoding="utf-8") as fh:
            nbformat.write(nb, fh)
        return 2
    with path.open("w", encoding="utf-8") as fh:
        nbformat.write(nb, fh)
    print(f"executed {path.name}: {sum(1 for c in nb.cells if c.cell_type == 'code')} code cells")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    import nbformat

    path = Path(args.notebook)
    nb = nbformat.read(path, as_version=4)
    nbformat.validate(nb)
    bad = 0
    for i, cell in enumerate(nb.cells):
        for out in cell.get("outputs", []) or []:
            if out.get("output_type") == "error":
                print(f"cell {i}: {out.get('ename')}: {out.get('evalue')}", file=sys.stderr)
                bad += 1
    print(f"{path.name}: valid nbformat, {len(nb.cells)} cells, {bad} error outputs")
    return 1 if bad else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("to-text", help="dump a notebook to percent-delimited text")
    p.add_argument("notebook")
    p.add_argument("-o", "--output")
    p.set_defaults(func=cmd_to_text)

    p = sub.add_parser("from-text", help="build a notebook from percent-delimited text")
    p.add_argument("source")
    p.add_argument("-o", "--output", required=True)
    p.add_argument("--no-colab", action="store_true")
    p.set_defaults(func=cmd_from_text)

    p = sub.add_parser("exec", help="execute a notebook in place")
    p.add_argument("notebook")
    p.add_argument("--timeout", type=int, default=300)
    p.add_argument("--python")
    p.set_defaults(func=cmd_exec)

    p = sub.add_parser("check", help="validate a notebook")
    p.add_argument("notebook")
    p.set_defaults(func=cmd_check)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
