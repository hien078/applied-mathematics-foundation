# Project Instructions

Repository: a first-principles applied-mathematics curriculum for machine learning,
read directly on GitHub and in Google Colab.

## Authoritative standard

[`MODULE_SPEC.md`](MODULE_SPEC.md) is the complete, self-contained contract for one module —
read it before writing or editing a module, and check the result with
`python3 tools/check_module.py <area>/<NN_slug>`.

[`STYLE_GUIDE.md`](STYLE_GUIDE.md) is the single source of truth for how content is written.
It **overrides every earlier convention** in this repository. If existing content conflicts
with it, the existing content is the thing that must change.

Read `STYLE_GUIDE.md` before editing any `.md` or `.ipynb` file.

## Quality bar

Content is benchmarked against the leading applied-mathematics texts, not against
lecture handouts. Reference points per area:

| Area | Benchmark texts |
|---|---|
| Linear algebra | Strang, *Linear Algebra and Learning from Data*; Trefethen & Bau; Axler; Horn & Johnson |
| Calculus | Spivak; Apostol; Hubbard & Hubbard |
| Optimization | Boyd & Vandenberghe; Nocedal & Wright; Bertsekas |
| Probability & statistics | Wasserman; Casella & Berger; Durrett; Bishop |
| Information theory | Cover & Thomas; MacKay |
| Numerical methods / computing | Trefethen & Bau; Higham, *Accuracy and Stability*; Heath |
| Differential equations | Strogatz; Hirsch, Smale & Devaney; Teschl |
| Graph theory | Bollobás; Chung, *Spectral Graph Theory*; Newman |
| Mathematical reasoning | Velleman; Rosen; Graham, Knuth & Patashnik |

Every statement must be one a careful reader could check. No hand-waving, no circular proofs,
no theorem stated without its hypotheses.

## Non-negotiables

- Math must render on GitHub. See `STYLE_GUIDE.md` §19.
- Notebooks are written with `json.dump` or `nbformat`, never by editing JSON text by hand.
- Notebook code cells must run top-to-bottom from a fresh kernel using only `requirements.txt`.
- What a `README.md` claims about a module must equal what the module actually contains:
  file names, tier names, and problem counts.

## Validation

Before any commit:

```bash
python3 tools/validate_content.py
```

The node-backed KaTeX and Mermaid checks need `katex`, `mermaid` and `jsdom` installed
somewhere on disk; point the validator at them:

```bash
npm install katex mermaid jsdom
VALIDATE_NODE_MODULES="$PWD/node_modules" python3 tools/validate_content.py
```

Exit code 0 means every math span compiles, every Mermaid diagram parses, every notebook is
valid `nbformat`, every relative link resolves, and every Colab badge points at its own file.

That checks rendering. The module contract is checked separately:

```bash
python3 tools/check_module.py <area>/<NN_slug>   # one module — the definition of done
python3 tools/check_module.py --all --failing    # repository-wide progress
```

It enforces `STYLE_GUIDE.md` §20 and §21: the eleven README sections, the ten
`first_principles.ipynb` headings, at least six code cells, two to four figures, the four
`L0`–`L3` exercise tiers, no retired headings, no stored error outputs, and README counts
equal to what the notebook actually contains.

Counts come from a script, never from memory:

```bash
python3 tools/curriculum_stats.py            # modules, problems, code cells, figures
python3 tools/curriculum_stats.py --markdown # the README table
```

Modules are exported for downstream applications with:

```bash
python3 tools/export_json.py linear_algebra -o build/   # one area
python3 tools/export_json.py --all -o build/            # everything
python3 tools/export_json.py linear_algebra --report    # coverage only, writes nothing
```

It emits `build/index.json` (metadata plus the prerequisite edges), one JSON document per
module, and the figures as PNG files. Anything that fails to parse is reported and the exit
code is non-zero, so a build can gate on complete coverage. `build/` is generated and gitignored.

Notebooks are authored through the round-trip helper, never by editing JSON:

```bash
python3 tools/nbtool.py to-text  <nb>.ipynb -o draft.txt
python3 tools/nbtool.py from-text draft.txt -o <nb>.ipynb
python3 tools/nbtool.py exec      <nb>.ipynb
```
