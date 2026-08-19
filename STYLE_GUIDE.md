# Authoring Style Guide

This document is the **single authoritative standard** for every file in this repository:
area `README.md`, module `README.md`, `first_principles.ipynb`, and `exercises.ipynb`.

Where this guide conflicts with any older convention used in the repository, **this guide wins**
and the older convention must be migrated.

---

## 1. Overall Visual Style

Write clean, academic, minimal, highly readable prose.

Priorities, in order:

- visual clarity
- whitespace
- short logical blocks
- mathematical readability
- easy screen scanning
- progressive explanation

A page must read like a **clear technical lecture note**, never like a conventional essay.

Dense walls of text are a defect, not a style choice.

---

## 2. Paragraph Length

Keep paragraphs short.

- 1–3 sentences per paragraph
- roughly 20–60 words per paragraph
- split the paragraph as soon as it carries more than one independent idea

One conceptual idea occupies one visual block.

---

## 3. Vertical Spacing

Use whitespace aggressively.

Insert a blank line between:

- different ideas
- paragraphs
- equations
- examples
- conclusions
- conceptual transitions

Preferred rhythm:

Text

Formula

Interpretation

Never compress that rhythm into a single paragraph.

---

## 4. Headings

Use Markdown headings hierarchically and never skip a level.

- exactly one `#` per document (or per notebook, in cell 0)
- `##` for major conceptual sections
- `###` for meaningful subsections
- never jump from `#` straight to `###`

Do not create headings for decoration, and do not put a heading on a two-line remark.

---

## 5. Conceptual Flow

Every explanatory unit follows this progression:

```
WHY
  -> INTUITION
  -> WHAT
  -> FORMAL DEFINITION
  -> MATHEMATICAL FORMULATION
  -> DERIVATION
  -> INTERPRETATION
  -> EXAMPLE
  -> CONNECTION
  -> KEY TAKEAWAYS
```

Do not mix the layers:

- intuition never contains a long proof
- a proof never contains implementation details
- a definition never contains historical context
- an example never introduces unrelated theory

---

## 6. Intuition First

Open every new concept with intuition.

State:

- why the concept exists
- what problem it solves
- how to picture it mentally

Keep it to 2–5 short paragraphs. Intuition is an on-ramp, not an essay.

---

## 7. Mathematical Expressions

Use LaTeX consistently, in the **GitHub-compatible** delimiters:

- inline: `$X^\top X$`
- display: `$$ ... $$` on its own lines, blank line before and after

Important equations always appear on their own line. Never bury a long equation inside prose.

---

## 8. Equation Spacing

Preferred:

> The objective function is:
>
> $$
> L(\theta) = \lVert y - X\theta \rVert^2
> $$
>
> It measures the squared distance between observation and prediction.

Not: one line containing prose, equation and explanation together.

---

## 9. Equation to Interpretation

Every important equation is followed by a short interpretation.

Pattern:

```
Formula
  -> Meaning
  -> Consequence
```

A boxed result with no sentence explaining what it means is incomplete.

---

## 10. Derivations

Split derivations into meaningful logical steps, each on its own display line.

```
$$
L(\theta) = \lVert y - X\theta \rVert^2
$$

Expand:

$$
L(\theta) = (y - X\theta)^\top (y - X\theta)
$$

Then:

$$
L(\theta) = y^\top y - 2\theta^\top X^\top y + \theta^\top X^\top X \theta
$$
```

Never collapse a long derivation into one giant equation unless compactness genuinely helps.

---

## 11. Short Explanations Between Steps

Insert one short connective sentence between important steps.

Do **not** narrate trivial algebra.

---

## 12. One Idea, One Block

Avoid:

> "OLS is a projection of y onto Col(X), so the residual is orthogonal to Col(X), which means Xᵀe = 0 and therefore gives the normal equation..."

Prefer:

> OLS is an orthogonal projection.
>
> $$
> \hat{y} = X\hat{\theta}
> $$
>
> The residual is orthogonal to the column space of $X$.
>
> $$
> X^\top e = 0
> $$
>
> This orthogonality condition produces the normal equation.

---

## 13. Bold

Bold only for semantic emphasis: **normal equation**, **key idea**, **important distinction**.

Never bold whole paragraphs. Never bold for decoration.

---

## 14. Italics

Use italics sparingly, for subtle distinctions, informal intuition, or naming a mental model.

---

## 15. Bullets

Use bullets for independent facts.

- $X$: design matrix
- $y$: observation vector
- $\theta$: parameter vector

Bullets are not a container for prose blocks.

---

## 16. Numbered Lists

Numbered lists only when order matters.

1. Define the objective.
2. Compute the gradient.
3. Set the gradient to zero.
4. Solve for the parameter.

Otherwise use bullets.

---

## 17. Tables

Tables only for genuine comparison, classification, or notation summary.

Keep cells short. Long explanations do not belong in a table cell.

---

## 18. Code

Multi-line code always goes in a fenced block with a language tag.

```python
theta = np.linalg.solve(X.T @ X, X.T @ y)
```

In notebooks, executable code lives in real `code` cells, not in fenced blocks inside markdown.

Every code cell must:

- be runnable top-to-bottom from a fresh kernel
- depend only on `requirements.txt`
- print or plot something that verifies the mathematics just derived
- be preceded by a short markdown cell saying what it checks
- be followed by a short markdown cell interpreting the output

---

## 19. GitHub Rendering Constraints (hard requirements)

All content is read directly on GitHub. Math that does not render is a bug.

- No space touching the `$` delimiters: `$x$`, never `$ x $`.
- Display math: `$$` alone on its own line, blank line before and after, no blank line inside.
- **Never** a raw `|` inside `$...$` in a table row: it splits the cell.
  Use `\mid`, `\vert ... \vert`, or `\parallel`.
- For norms use `\lVert ... \rVert`, never `\Vert` and never `\|`. `\lVert`/`\rVert` are true
  delimiters, so they scale with their content; inside a table `\|` loses its backslash to GFM
  and collapses to a cell separator. See [`docs/notation.md`](docs/notation.md).
- Never `<` immediately followed by a letter inside math. Use `\lt` or add a space.
- KaTeX only. Forbidden: `\iddots`, `\argmin`, `\bm`, `\DeclareMathOperator`, `\eqref`.
  Use `\operatorname{...}`. Bare glyphs such as the check mark have no KaTeX metrics.
- In `.ipynb`, LaTeX backslashes must be escaped in the JSON (`\\right`).
  Write notebooks with `json.dump` or `nbformat`, never by splicing JSON text by hand.
- A fenced code block must open and close inside the **same** markdown cell.

Run `python3 tools/validate_content.py` before every commit.

---

## 20. Module Contract

Each `<area>/NN_slug/` directory contains exactly three files.

### `README.md`

1. `# Module NN — Title`
2. Overview: 2–4 short paragraphs, why the module exists
3. `> [!NOTE]` callout with the single most important result
4. Prerequisites and downstream links (relative paths)
5. Learning outcomes as a bullet list
6. Mermaid concept map
7. Notation table
8. Core results table
9. Common misconceptions
10. Exercise index that **matches the real tiers and counts** in `exercises.ipynb`
11. References with chapter-level precision

### `first_principles.ipynb`

Follows Section 5 flow. Contains:

- markdown cells for theory
- **executable code cells** that verify each major theorem numerically
- at least one figure that shows the geometry of the central idea
- worked numerical examples with concrete small matrices or numbers
- a closing "Key Takeaways" cell

### `exercises.ipynb`

Fully solved problems in four tiers:

- **L0** concept checks
- **L1** foundations
- **L2** AI/ML and physics applications
- **L3** challenge proofs

Each problem carries: statement, intuition, full derivation, `$$\boxed{...}$$` answer,
key takeaway, and — where the answer is numeric or algorithmic — a code cell that checks it.

The counts and tier names stated in the module `README.md` must equal what the notebook contains.

---

## 21. Computational Contract

Notebooks are read on GitHub and run on Colab. A code cell must therefore be self-contained:
it may import only from `requirements.txt`, and it may not import anything from `tools/`.

### Authoring notebooks

Never edit notebook JSON by hand. Use the helper:

```bash
python3 tools/nbtool.py to-text  path/to/notebook.ipynb -o draft.txt   # read / start from existing
python3 tools/nbtool.py from-text draft.txt -o path/to/notebook.ipynb  # build
python3 tools/nbtool.py exec      path/to/notebook.ipynb               # run and store outputs
python3 tools/validate_content.py path/to/notebook.ipynb               # verify rendering
```

The text form separates cells with marker lines:

```
# %% [markdown]
## Section title

# %% [code]
import numpy as np
```

Write the draft with a quoted heredoc (`<<'EOF'`) so backslashes stay literal.

### Standard preamble

The first code cell of every notebook is this preamble, extended with whatever else the
module needs:

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

Randomness is always seeded through `rng`. Never call `np.random.*` directly: outputs are
committed to the repository and must be reproducible.

### What code must do

Code exists to make a claim checkable, never for decoration.

- **Verify a theorem numerically.** Print the residual of the identity just derived, and
  state the tolerance in words: reconstruction error near machine epsilon confirms the result.
- **Show a rate.** When a convergence rate is derived, measure it and print the observed order.
- **Exhibit a counterexample.** When a hypothesis is claimed necessary, run the case where it
  fails and show the breakage.
- **Compare against the library.** Hand-rolled implementations are checked against the
  corresponding NumPy or SciPy routine.

### Figures

Each `first_principles.ipynb` carries **2 to 4 figures**, and each one must show the geometry
or dynamics of the central idea — not a decorative plot.

- axis labels and a title on every figure
- a legend whenever more than one series is drawn
- `ax.set_aspect("equal")` for anything geometric
- no seaborn, no styles beyond the preamble

### Output hygiene

Committed notebooks store their outputs. Before committing, `tools/nbtool.py exec` must run
clean: any stored error output is a build failure.
