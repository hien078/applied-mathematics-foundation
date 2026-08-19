# Module Specification

The complete, self-contained contract for one curriculum module. This file is the only
specification an author needs; `python3 tools/check_module.py <area>/<NN_slug>` checks it
mechanically and must print `PASS`.

`STYLE_GUIDE.md` gives the prose and rendering rules that sit underneath this contract.

---

## 1. Files

Each `<area>/NN_slug/` holds exactly three files:

```
README.md               the module's front page
first_principles.ipynb  theory
exercises.ipynb         fully solved problems
```

Never edit notebook JSON by hand — a single `\right` spliced into JSON decodes as
carriage-return + `ight` and silently destroys the formula. Round-trip instead:

```bash
python3 tools/nbtool.py to-text  <nb>.ipynb -o /tmp/draft.txt
# edit /tmp/draft.txt, write it back with a QUOTED heredoc (<<'EOF') so backslashes stay literal
python3 tools/nbtool.py from-text /tmp/draft.txt -o <nb>.ipynb
python3 tools/nbtool.py exec      <nb>.ipynb
```

---

## 2. `first_principles.ipynb`

Cell 0 keeps its Colab badge and carries `# Module NN — Title`.

Then exactly these ten `##` headings, in this order, spelled exactly like this:

```
## 1. Why This Module Exists
## 2. Intuition
## 3. Definitions
## 4. Main Results
## 5. Derivations and Proofs
## 6. Worked Examples
## 7. Computational Practice
## 8. Applications
## 9. Key Takeaways
## 10. References
```

Number every formal object and cite it by number, never by position:

```
### Definition 3.2
### Theorem 4.1
### Proof 5.1 (of Theorem 4.1)
### Example 6.3
```

Write "by Proof 5.1", never "as shown above".

**Forbidden headings** (retired; delete on sight): `Phenomenon`, `Goal`, `Assumptions`,
`Variables and Parameters`, `Units and Dimensions`, `Domain Constraints`.

### Content rules

- Sections 1 and 2 contain no proofs. Section 5 contains no implementation detail.
  Section 3 contains no history.
- State every theorem in Section 4 with its hypotheses inline, then one sentence per
  hypothesis saying why it is needed.
- **Prove the theorem the module is named after, in Section 5.** Not deferred to the exercises,
  not deferred to a later module, not an infinitesimal heuristic closed with a QED, and never
  by assuming its own conclusion. If a full proof is genuinely out of scope, mark it
  `### Theorem 4.k (cited, not proved here)` with a page-precise reference and prove in full
  the strongest special case the module supports.
- Every `$$\boxed{...}$$` is followed by an **Interpretation** paragraph: meaning, then consequence.
- Section 6 carries one fully worked numerical example per main theorem, on deliberately small
  objects — a 2x2 or 3x3 matrix, a 4-node graph, a 2-3 outcome distribution, one explicit integral —
  computed by hand in markdown showing intermediates, then a code cell that recomputes the same
  numbers and asserts agreement.
- Section 9 is 5 to 8 one-line results, each with its hypotheses.

### Code: at least 6 cells

The first code cell is this preamble, verbatim, extended with whatever else the module needs:

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.figsize": (7.0, 4.0),
    "figure.dpi": 110,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 11,
})
rng = np.random.default_rng(0)
np.set_printoptions(precision=4, suppress=True)
```

Seed randomness only through `rng`. Never call `np.random.*` anywhere else.

Every code cell is preceded by a short markdown cell saying what it checks and followed by a
short markdown cell interpreting the printed output. Code exists to make a claim checkable,
never for decoration.

The cells must include all four of these kinds:

| kind | what it does |
|---|---|
| **(a) identity residual** | verify a boxed identity numerically; print the residual, `assert` it, and say in words that it sits at machine-epsilon level |
| **(b) measured rate** | measure a derived convergence rate or order; print observed versus predicted |
| **(c) counterexample** | run the case where a hypothesis is dropped and show the breakage |
| **(d) hand-rolled vs library** | your implementation against the corresponding NumPy/SciPy routine |

Import only from `requirements.txt`. Never import from `tools/` — notebooks must run on Colab.

### Figures: 2 to 4

The Section 2 figure is mandatory. Each figure shows the geometry or dynamics of the central
idea, never decoration. Every figure needs axis labels, a title, a legend when more than one
series is drawn, and `ax.set_aspect("equal")` for anything geometric. No seaborn.

---

## 3. `exercises.ipynb`

Exactly four tiers, spelled exactly like this:

```
## L0 — Concept Checks
## L1 — Foundations
## L2 — Applications (AI/ML and Physics)
## L3 — Challenge Proofs
```

Every problem heading is `### Problem L2.3 — Short Title`. No other numbering scheme survives.

Each problem carries these blocks, in this order:

1. **Statement**
2. **Intuition** — 1 to 2 sentences
3. **Solution** — Step 1 … Step n
4. `$$\boxed{...}$$`
5. **Key takeaway** — one sentence
6. a code cell recomputing the answer, whenever the answer is numeric or algorithmic

L0 holds genuine one-liners. A three-condition verification belongs in L1. If the L2 heading
says physics, L2 must contain at least two genuine physics problems.

**Every numeric answer must come from a code cell that ran, not from memory.** Boxed answers in
this repository have been wrong by three orders of magnitude where one library call would have
caught it.

---

## 4. `README.md`

Eleven items, in this order:

1. `# Module NN — Title`
2. Overview — 2 to 4 short paragraphs on why the module exists
3. `> [!NOTE]` callout carrying the single most important result
4. `## Prerequisites` and downstream links, as working relative paths, taken from
   [`docs/prerequisites.md`](docs/prerequisites.md)
5. `## Learning outcomes` — bullets
6. A Mermaid concept map
7. `## Notation` — a table drawn from [`docs/notation.md`](docs/notation.md)
8. `## Core results` — a table
9. `## Common misconceptions`
10. `## Exercise index` — tier names and counts equal to what `exercises.ipynb` actually contains
11. `## References` — chapter-and-theorem precision, e.g. `Axler, *LADR*, §7.B (Thm 7.29)`

Every cross-module reference is a working relative markdown link, never the prose "Topic NN",
and never a `.md` sibling that does not exist.

---

## 5. Dependency discipline

A result may cite only modules with a lower index in the same area, or a module in a declared
prerequisite area per [`docs/prerequisites.md`](docs/prerequisites.md). Delete every
"proved in Topic NN" that points forward — prove the lemma inline instead; a three-line
tangent-line bound is cheaper than a forward reference.

---

## 6. Rendering constraints

Content is read on GitHub. Math that does not render is a bug.

- No space touching `$`: write `$x$`, never `$ x $`.
- Display math: `$$` alone on its own line, blank line before and after, none inside.
- **Never** a raw `|` inside `$...$` in a table row — it splits the cell. Use `\mid` or `\vert`.
- Norms are `\lVert x \rVert`. Never `\Vert`, never `\|`.
- Never `<` immediately before a letter inside math; use `\lt`.
- KaTeX only: no `\argmin`, `\bm`, `\DeclareMathOperator`, `\eqref`. Use `\operatorname{...}`.
- A fenced code block opens and closes inside the same markdown cell.

---

## 7. Definition of done

All four must pass, and the real output must be shown:

```bash
python3 tools/nbtool.py exec <mod>/first_principles.ipynb     # no stored error output
python3 tools/nbtool.py exec <mod>/exercises.ipynb            # no stored error output
VALIDATE_NODE_MODULES=$NODE python3 tools/validate_content.py <mod>   # exit 0
python3 tools/check_module.py <mod>                           # PASS
```
