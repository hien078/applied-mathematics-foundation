# Notation Register

This file fixes the symbols and the mathematical conventions used by every module in this
repository.

It is subordinate to [`STYLE_GUIDE.md`](../STYLE_GUIDE.md) on presentation and
authoritative on notation.

Where a module contradicts a ruling below, **the module is what changes**, exactly as
[`CLAUDE.md`](../CLAUDE.md) requires.

---

## Why this register exists

Eighty-seven modules were written without a shared notation table. The symbols drifted,
and in several places the drift produced statements that are simply false.

Three confirmed examples, each verified against the current tree:

**Smoothness.** `calculus_optimization/03` defines $L$-smoothness as
$\lambda_{\max}(\nabla^2 f) \le L$, while `calculus_optimization/02` defines it as
$\lVert \nabla^2 f \rVert_{\mathrm{op}} \le L$. The first is wrong for indefinite
Hessians: a Hessian with spectrum $\lbrace -100, 1 \rbrace$ satisfies it and is not
$1$-smooth. Module 03 then applies the definition to nonconvex functions.

**InfoNCE.** `information_theory/05` defines the contrastive loss with a $\tfrac{1}{K}$
normalizer inside the softmax denominator, then asserts $\mathcal{L}_{\mathrm{NCE}} \ge 0$
and uses the bound $I(X; Y) \ge \log K - \mathcal{L}_{\mathrm{NCE}}$. Both statements hold
only for the unnormalized loss. The module's headline theorem is off by $\log K$.

**Eigenvalue ordering.** Eigenvalues run ascending in `linear_algebra/06` and descending
in `linear_algebra/04` and `linear_algebra/09`, so Courant–Fischer is stated once as a
min-max and once as a max-min with no note that anything changed.

None of these is a typo. Each is what happens when the same symbol carries two meanings on
adjacent pages and no document arbitrates.

### What a ruling is

Each ruling states three things:

1. the convention this repository uses,
2. the benchmark text it matches,
3. where the losing convention currently lives.

Item 3 is a work list. **Nothing in this file has been migrated yet.** A later agent takes
each ruling, greps for the loser, and rewrites it.

### Scope

Run `python3 tools/curriculum_stats.py` for the current shape of the tree.

Every ruling below governs prose and LaTeX. Variable names inside code cells follow the same
tables, so a symbol ruled here keeps its meaning when it becomes an identifier.

### Two standing rules

**Declare, then use.** Every module `README.md` carries a notation table drawn from this
file, listing only the symbols that module actually uses.

**Collisions that survive get a callout.** A few genuine collisions cannot be removed
without fighting the literature. Each is named below as a *declared exception*, is confined
to the modules listed, and must carry a `> [!NOTE]` callout at its first use in the module.

---

## Rulings at a glance

| Ruling | Losing convention currently lives in |
|---|---|
| Eigenvalues descending, $\lambda_1 \ge \cdots \ge \lambda_n$ | `linear_algebra/06`, `calculus/12`, `calculus_optimization/04`, `optimization/03` |
| Graph Laplacian spectra ascending (declared exception) | already consistent in `graph_theory/06`, `graph_theory/07` |
| Markov matrices column-stochastic, $P\pi = \pi$ | `linear_algebra/06` §27, `linear_algebra/08` exercises |
| Lagrangian $\mathcal{L} = f + \lambda^\top h$, sensitivity $dp^{\star}/db = -\lambda$ | `optimization/05` Proofs 5–6, `optimization/07` exercises, `calculus/06` exercises |
| $L$-smoothness as $\lVert \nabla^2 f \rVert_{\mathrm{op}} \le L$ | `calculus_optimization/03` Definition 2.2 |
| $H(X, Y)$ joint entropy; $H_{\times}(p, q)$ cross-entropy | `information_theory/03`, `information_theory/01` exercises, `information_theory/06` |
| InfoNCE unnormalized, chance level $\log K$ | `information_theory/05` Proof 3.7 |
| Negative Binomial: name the convention, never bare $\mathrm{NB}$ | `probability_statistics/04`, `probability_statistics/10` |
| Chebyshev polynomials $T_k$; Taylor polynomials $P_n$ | `linear_algebra/08` exercises ($C_k$), `calculus/09` and `calculus_optimization/02` ($T_n$, $T_k$) |
| Transpose written $A^\top$ | `linear_algebra`, `optimization`, `calculus`, `differential_equations`, `probability_statistics` |
| Norms written $\lVert x \rVert$ | `linear_algebra`, `calculus`, `optimization` |
| $\varepsilon_{\mathrm{mach}} = 2^{-52}$, unit roundoff $u = 2^{-53}$ | `numerical_computing/README.md`, `numerical_methods/05`, `linear_algebra/08` |
| $\Lambda$ is the eigenvalue diagonal; precision matrix is $\Sigma^{-1}$ or $\Theta$ | `probability_statistics/07` |
| $\mathcal{L}$ is the Lagrangian; losses are $J$ and $\ell$ | `linear_algebra/08`, `calculus/06`, `probability_statistics` |
| $\mathbb{P}$ for the probability measure; $(n)_k$ for permutation counts | `probability_statistics/01`, `mathematical_reasoning/05` |
| $\mathbb{E}$, $\operatorname{Var}$, $\operatorname{Cov}$ | bare $E[\cdot]$ and $\mathrm{Var}$ / $\text{Var}$ repo-wide |
| $O$, $\Omega$, $\Theta$, $o$ for asymptotics | $\mathcal{O}$ in `numerical_methods`, `numerical_computing`, `calculus` |

---

## General symbols

These bind in every area unless an area section below declares an exception.

### Objects

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $x$, $y$, $v$, $\theta$, $w$ | vectors | lowercase italic; a vector is a **column** vector in $\mathbb{R}^n$ |
| $A$, $X$, $H$, $Q$ | matrices | uppercase italic; $A \in \mathbb{R}^{m \times n}$ has $m$ rows, $n$ columns |
| $x_i$ | $i$-th component of $x$ | subscript indexes coordinates |
| $x_k$ | $k$-th iterate of an algorithm | subscript indexes iterations; never mix the two roles in one derivation |
| $A_{ij}$ | entry of $A$ in row $i$, column $j$ | row index first |
| $I$, $I_n$ | identity matrix | |
| $\mathbf{1}$, $e_i$ | all-ones vector, $i$-th standard basis vector | |
| $\delta_{ij}$ | Kronecker delta | |
| $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$, $\mathbb{C}$ | number systems | $\mathbb{N} = \lbrace 0, 1, 2, \ldots \rbrace$ **includes zero** |
| $\blacksquare$ | end of proof | only after a complete argument, never after a heuristic |

### Operations

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $A^\top$ | transpose | `\top`, never `^T` |
| $A^{-1}$, $A^{+}$ | inverse, Moore–Penrose pseudoinverse | |
| $\langle x, y \rangle = x^\top y$ | inner product | `\langle ... \rangle`, never `\left<` |
| $\lVert x \rVert_2$, $\lVert x \rVert_1$, $\lVert x \rVert_\infty$ | vector norms | `\lVert ... \rVert`, never `\Vert`, never `\|` |
| $\lVert A \rVert_{\mathrm{op}}$ | operator (spectral) norm | the default matrix norm |
| $\lVert A \rVert_F$ | Frobenius norm | |
| $\lvert S \rvert$ | cardinality; also absolute value of a scalar | `\lvert ... \rvert`, never a bare `\|` |
| $\operatorname{tr}$, $\det$, $\operatorname{rank}$ | trace, determinant, rank | `\operatorname{...}`, never `\text{...}` |
| $\operatorname{diag}(a_1, \ldots, a_n)$ | diagonal matrix | |
| $A \succeq 0$, $A \succ 0$ | positive semidefinite, positive definite | Löwner order |

### Calculus

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $\nabla f(x)$ | gradient | a **column** vector in $\mathbb{R}^n$ |
| $\nabla^2 f(x)$ | Hessian | always written $\nabla^2 f$; $H$ only as a local abbreviation defined in the same cell |
| $J_f(x)$ | Jacobian of $f : \mathbb{R}^n \to \mathbb{R}^m$ | an $m \times n$ matrix, so $J_f = (\nabla f)^\top$ when $m = 1$ |
| $D_u f(x)$ | directional derivative along a unit $u$ | |
| $P_n$, $R_n$ | degree-$n$ Taylor polynomial and its remainder | **not** $T_n$: $T_k$ is reserved for Chebyshev |
| $O$, $\Omega$, $\Theta$, $o$, $\omega$ | asymptotic notation | bare capitals, not `\mathcal{O}` |

### Probability

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $\mathbb{P}(A)$, $\mathbb{P}(A \mid B)$ | probability, conditional probability | `\mathbb{P}`, and `\mid` for the conditioning bar |
| $\mathbb{E}[X]$, $\mathbb{E}_{X \sim p}[\cdot]$ | expectation | `\mathbb{E}`, never bare $E$ |
| $\operatorname{Var}(X)$, $\operatorname{Cov}(X, Y)$ | variance, covariance | `\operatorname`, never `\mathrm` or `\text` |
| $X \sim p$ | $X$ is distributed according to $p$ | |
| $\Omega$, $\mathcal{F}$, $\mathbb{P}$ | sample space, $\sigma$-algebra, measure | |
| $\mathcal{N}(\mu, \Sigma)$ | Gaussian with mean $\mu$, covariance $\Sigma$ | second argument is the **covariance**, never the precision |

### Optimization

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $x^{\star}$, $p^{\star}$, $d^{\star}$ | minimizer, primal optimal value, dual optimal value | |
| $\mathcal{L}$ | Lagrangian | see the optimization section for the sign |
| $\eta$ | step size (learning rate) | $\eta$ repo-wide, not $\alpha$ |
| $L$, $\mu$ | smoothness constant, strong-convexity modulus | $\mu I \preceq \nabla^2 f \preceq L I$ |
| $\kappa = L/\mu$ | condition number of an objective | |
| $\operatorname{argmin}$, $\operatorname{argmax}$ | argument of the extremum | `\operatorname{...}`; the bare macros `\argmin` / `\argmax` are forbidden by KaTeX |

### Contested conventions (general)

**Transpose.** Ruling: $A^\top$.

Matches [`STYLE_GUIDE.md`](../STYLE_GUIDE.md) §7, whose own worked example is `$X^\top X$`,
and Boyd & Vandenberghe throughout.

Evidence: `^\top` appears 1,359 times, `^T` 4,265 times. The losers are concentrated by
area: `linear_algebra` (2,256), `optimization` (1,208), `calculus` (492),
`differential_equations` (121), `probability_statistics` (121), `numerical_methods` (44).
`calculus_optimization`, `graph_theory`, `numerical_computing` and most of
`probability_statistics` already comply.

**Norm delimiters.** Ruling: $\lVert x \rVert$, built from `\lVert` and `\rVert`.

Matches STYLE_GUIDE §19, which forbids `\|` outright because GitHub-Flavored Markdown eats
the backslash inside a table cell and splits the row.

Evidence: `\|` appears 2,768 times, overwhelmingly in `linear_algebra` (1,968) and
`calculus` (736); `\Vert` 1,285 times; `\lVert` 1,271 times.

None of those 2,768 sites currently breaks a table — `tools/validate_content.py` exits 0 on
the whole tree — because they all sit in prose or display math. The ruling still binds: the
moment a module lifts one of those norm expressions into a core-results table or a notation
table, which STYLE_GUIDE §20 now requires of all 87 modules, the row splits. Migrating to
`\lVert ... \rVert` makes every expression safe to move.

**Expectation and variance.** Ruling: $\mathbb{E}[X]$, $\operatorname{Var}(X)$,
$\operatorname{Cov}(X, Y)$.

Bare $E$ collides with the edge set $E$ in `graph_theory`, with energy levels $E_i$ in the
maximum-entropy derivations of `optimization/05` and `information_theory`, and with the
error functional $E(h)$ in `numerical_methods/05` and `calculus/03`.

Evidence: `\mathbb{E}` 632 sites, bare `E[` 743 sites. Variance is spelled three ways:
`\mathrm{Var}` 214, `\operatorname{Var}` 127, `\text{Var}` 58. All three render identically,
so this is a hygiene ruling, not a correctness one; STYLE_GUIDE §19 asks for `\operatorname`.

**Probability measure.** Ruling: $\mathbb{P}(\cdot)$.

Bare $P$ is the transition matrix in `linear_algebra/06`, `linear_algebra/10`,
`graph_theory/06` and `numerical_methods/03`, the projection matrix in
`linear_algebra/04`, and the permutation count $P(n, k)$ in `probability_statistics/01` and
`mathematical_reasoning/05`. In `probability_statistics/01` the two meanings appear three
cells apart.

Evidence: bare `P(` 1,700 sites, `\mathbb{P}` 51, `\Pr` 38. This is the largest single
migration in this file; it is mechanical and low risk, and it can be deferred behind the
correctness rulings.

**Permutation counts.** Ruling: the falling factorial $(n)_k = n!/(n-k)!$.

Graham, Knuth & Patashnik, *Concrete Mathematics* §2.6 write it $n^{\underline{k}}$; either
is acceptable inside `mathematical_reasoning/05`, where GKP is the benchmark. What is not
acceptable is $P(n, k)$ anywhere.

Loser: `mathematical_reasoning/05` (7 sites, plus the README misconception row) and
`probability_statistics/01` §Definition 2.7.

**Asymptotic notation.** Ruling: $O$, $\Omega$, $\Theta$, $o$, $\omega$ as bare symbols.

Matches Graham, Knuth & Patashnik Ch. 9, Cormen et al. Ch. 3 and Rosen Ch. 3 — the
benchmark texts for `mathematical_reasoning`.

Evidence: bare `O(` 1,628 sites, `\mathcal{O}` 190 (concentrated in `numerical_methods`,
`numerical_computing` and `calculus`).

Residual ambiguity, accepted: $\Omega$ is also the sample space in `probability_statistics`,
and $\Theta$ is also a parameter set. Neither area uses asymptotic bounds, and an asymptotic
$\Omega(g(n))$ always carries a function of $n$ as its argument, so the reading is
recoverable from the argument. Any file that genuinely needs both must say so in its
notation table.

**The symbol $\mathcal{L}$.** Ruling: $\mathcal{L}$ is the **Lagrangian**.

Training losses are $J(\theta)$ for the empirical risk and $\ell(y, \hat{y})$ for the
per-example loss. A subscripted $\mathcal{L}_{\text{name}}$ naming a specific literature
objective — $\mathcal{L}_{\mathrm{NCE}}$, $\mathcal{L}_{\mathrm{ELBO}}$ — is permitted,
because the subscript removes the ambiguity.

Evidence: 756 occurrences carrying at least five meanings — Lagrangian (`optimization` 219,
`calculus/06`), training loss (`linear_algebra/08`, `probability_statistics`,
`information_theory`), Laplace transform (`differential_equations/06`, 159 sites), the space
of linear maps $\mathcal{L}(V, W)$ (`linear_algebra/02`, 14 sites), and a line in the plane
(`calculus/06` exercises).

Two declared exceptions, each with a callout:

- $\mathcal{L}\lbrace f \rbrace(s)$ — the Laplace transform operator, `differential_equations/06`
  only. The brace-delimited argument makes it unmistakable.
- $\mathcal{L}(V, W)$ — the space of linear maps, `linear_algebra/02` only. This is Axler's
  notation (*Linear Algebra Done Right*, "Vector Space of Linear Maps").

The line in `calculus/06` has no such defence and should simply be renamed $\ell$.

---

## Linear algebra

Benchmarks: Strang, *Linear Algebra and Learning from Data*; Trefethen & Bau; Axler;
Horn & Johnson.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $A \in \mathbb{R}^{m \times n}$ | matrix | $m$ rows, $n$ columns |
| $\operatorname{Col}(A)$, $\operatorname{Null}(A)$, $\operatorname{Row}(A)$ | column space, null space, row space | `\operatorname` |
| $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$ | eigenvalues of a symmetric matrix | **descending** |
| $\Lambda$ | $\operatorname{diag}(\lambda_1, \ldots, \lambda_n)$ | eigenvalue matrix, never the precision matrix |
| $\sigma_1 \ge \sigma_2 \ge \cdots \ge \sigma_r \gt 0$ | singular values | **descending** |
| $A = U \Sigma V^\top$ | singular value decomposition | $\Sigma$ inside a factorization is the singular-value matrix |
| $\kappa_2(A) = \sigma_1/\sigma_n$ | 2-norm condition number | |
| $A = QR$, $A = LU$, $A = LL^\top$ | QR, LU, Cholesky factorizations | |
| $P$ | column-stochastic transition matrix | $P\pi = \pi$ |
| $\pi$ | stationary distribution | a column vector with $\mathbf{1}^\top \pi = 1$ |
| $T_k$ | Chebyshev polynomial of the first kind | $T_0 = 1$, $T_1(y) = y$, $T_{k+1} = 2yT_k - T_{k-1}$ |
| $\rho(A)$ | spectral radius | |
| $\gamma_n = nu/(1 - nu)$ | Wilkinson's rounding-error accumulator | see the numerical-computing section for $u$ |

### Contested conventions

**Eigenvalue ordering.** Ruling: **descending**, $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$.

Matches the singular-value ordering $\sigma_1 \ge \cdots \ge \sigma_r$ of Trefethen & Bau,
*Numerical Linear Algebra*, Lecture 4, and Strang's PCA ordering in *Linear Algebra and
Learning from Data*, so that `linear_algebra/07`'s SVD and the eigenvalue chapters agree
without re-indexing. Under this ordering Courant–Fischer reads
$\lambda_k = \max_{\dim S = k} \min_{0 \ne x \in S} \frac{x^\top A x}{x^\top x}$,
and PCA's "first $k$ principal components" are $\lambda_1, \ldots, \lambda_k$ with no
re-indexing.

Stated honestly, this is a divergence from one benchmark: Horn & Johnson, *Matrix Analysis*,
order Hermitian eigenvalues **ascending** in their variational-characterization chapter. A
module citing Horn & Johnson for Courant–Fischer must therefore transcribe the statement into
the descending form and say in one sentence that it did.

Evidence: 10 descending sites (`linear_algebra/04` Ex. 30, `05`, `06` exercises,
`07` first_principles, `08`, `09` in three places, `optimization/05`,
`differential_equations/01`) against 19 ascending sites.

Losers to migrate, all ascending:

- `linear_algebra/06/first_principles.ipynb` §16 — states Courant–Fischer as a **min-max**
  with $\lambda_1 \le \cdots \le \lambda_n$, contradicting the **max-min** proved in
  `linear_algebra/09/exercises.ipynb` Exercise 26.
- `calculus/12/first_principles.ipynb` (2 sites) and `calculus/12/exercises.ipynb` (1 site)
  — Rayleigh quotient and Courant–Fischer, both ascending.
- `calculus_optimization/04/first_principles.ipynb` (2 sites) — the critical-point taxonomy
  table, $\lambda_1 \le \cdots \le \lambda_d$.
- `optimization/03/first_principles.ipynb` — $\mu = \lambda_1 \le \cdots \le \lambda_n = L$.
- `differential_equations/08/exercises.ipynb` — $0 \lt \lambda_1 \le \cdots \le \lambda_p$.

For the three optimization-flavoured sites the fix is not to renumber but to **drop the
indices**: write $\mu = \lambda_{\min}(\nabla^2 f)$ and $L = \lambda_{\max}(\nabla^2 f)$,
which is what the surrounding proofs actually use.

**Declared exception — graph Laplacian spectra.** Laplacian eigenvalues are written
**ascending**, $0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$, so that $\lambda_2$
is the algebraic connectivity (Fiedler value) and multiplicity of $0$ counts components.

This matches Chung, *Spectral Graph Theory*, and von Luxburg's spectral-clustering tutorial
(2007) on the ordering, and it is already consistent across `graph_theory/06`,
`graph_theory/07` and `linear_algebra/10`. Every module using it carries a callout saying the
ordering is reversed from the repository default.

Index from $1$, not from $0$. Chung indexes from $0$; von Luxburg and Fiedler's own papers
index from $1$, which puts the algebraic connectivity at $\lambda_2$, and that is what this
repository uses. The legacy `graph_theory/first_principles.md` writes
$0 = \lambda_0 \le \cdots \le \lambda_{n-1}$ and must be brought to $1$-indexing.

**Markov transition matrices.** Ruling: **column-stochastic**, one step is
$\pi_{t+1} = P\pi_t$, and stationarity is $P\pi = \pi$.

This keeps distributions as column vectors, matching the column-vector convention used
everywhere else in the area, and makes $\pi$ the Perron right eigenvector for $\lambda = 1$
with $\mathbf{1}^\top P = \mathbf{1}^\top$.

Evidence: 17 column-stochastic sites (`linear_algebra/06` exercises, `09`, `10`,
`numerical_methods/03`) against 8 row-stochastic ones.

Losers to migrate:

- `linear_algebra/06/first_principles.ipynb` §27 — "$\pi^\top P = \pi^\top$ (or
  $P^\top \pi = \pi$)", offering both and fixing neither.
- `linear_algebra/08/exercises.ipynb` — the PageRank problem builds
  $(I - \alpha P^\top)x$ from a row-stochastic $P$; restate with the column convention so it
  agrees with the PageRank problems in `linear_algebra/09` and `linear_algebra/10`.

Two declared exceptions, each already flagged or to be flagged with a callout:

- The **continuous-time generator** $Q$ in `linear_algebra/10` §21, where
  $\sum_j Q_{ij} = 0$ and $e^{Qt}$ is row-stochastic. The module already carries a
  Convention Note; keep it.
- The **graph random-walk operator** $P = D^{-1}A$ in `graph_theory/06` and
  `graph_theory/07`, which is row-stochastic by construction because
  $L_{\mathrm{rw}} = I - P$ requires it. Here stationarity is written $\pi^\top P = \pi^\top$.
  This site was not named in the audit and is a third instance of the same collision.

**Chebyshev polynomials.** Ruling: $T_k$, the polynomials of the first kind, with
$T_0 = 1$, $T_1(y) = y$, $T_{k+1}(y) = 2yT_k(y) - T_{k-1}(y)$.

Matches Trefethen & Bau, *Numerical Linear Algebra*, Lecture 38, and Trefethen, *ATAP*.

Loser: `linear_algebra/08/exercises.ipynb` writes $C_k$ in six places for the same object
that `linear_algebra/08/first_principles.ipynb` calls $T_k$ five cells earlier. The
$T_k$ spelling is also already used in `linear_algebra/10` and `graph_theory/07`
(ChebNet), so $C_k$ is isolated.

**Collision found here, not on the audit list — $T_n$ also means the Taylor polynomial.**
`calculus/09` uses $T_n(x)$ for the degree-$n$ Taylor polynomial in 20 places, and
`calculus_optimization/02` uses $T_k(h)$ with remainder $R_k(h)$.

Ruling: $T_k$ belongs to Chebyshev; the Taylor polynomial is $P_n$ with remainder $R_n$.
`calculus_optimization/02` already pairs its polynomial with $R_k$, so renaming
$T_k \to P_k$ there is a one-symbol edit.

**The symbol $\Sigma$.** Ruling: inside a factorization $A = U\Sigma V^\top$, $\Sigma$ is
the singular-value matrix; standing alone, in $\mathcal{N}(\mu, \Sigma)$ or
$\operatorname{Cov}(X)$, it is a covariance matrix.

Where a passage genuinely needs both — a PCA derivation that takes the SVD of a centred data
matrix — write the sample covariance $S$ and keep $\Sigma$ for the population covariance.

---

## Calculus

Benchmarks: Spivak; Apostol; Hubbard & Hubbard.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $f : \mathbb{R}^n \to \mathbb{R}^m$ | function, domain first | |
| $P_n(x)$, $R_n(x)$ | degree-$n$ Taylor polynomial and remainder | **not** $T_n$ |
| $M_n(x)$ | Maclaurin polynomial, i.e. $P_n$ with $a = 0$ | keep only where the distinction is the point |
| $\nabla f$, $\nabla^2 f$, $J_f$ | gradient, Hessian, Jacobian | as in the general table |
| $\varepsilon$, $\delta$ | the limit quantifiers | $\varepsilon$, never $\epsilon$, in limit arguments |
| $\limsup$, $\liminf$ | upper and lower limits | must be defined in `calculus/08` before the root test uses them |
| $\int_a^b f\, dx$ | Riemann integral | `\,` before the differential |
| $\lvert \cdot \rvert$ | absolute value | `\lvert ... \rvert` |

### Contested conventions

**Taylor polynomial symbol.** Ruling: $P_n$, remainder $R_n$. See the linear-algebra section
for why $T_n$ is unavailable.

Loser: `calculus/09` (README, first_principles, exercises) and
`calculus_optimization/02` (README, first_principles).

**Machine epsilon inside calculus.** `calculus/02` and `calculus/03` use
$\varepsilon_{\text{mach}}$ and $\epsilon_{\text{mach}}$ interchangeably, and quote its
value as "$\approx 2 \times 10^{-16}$", "$2.2 \times 10^{-16}$" and "$10^{-16}$" in three
different problems.

Ruling: $\varepsilon_{\mathrm{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}$ and
$u = \tfrac{1}{2}\varepsilon_{\mathrm{mach}} = 2^{-53}$, exactly as fixed in the
numerical-computing section. Finite-difference step-size arguments should be written in
terms of $u$, because that is the constant in the standard model
$\operatorname{fl}(a \circ b) = (a \circ b)(1 + \delta)$ with $\lvert \delta \rvert \le u$.

**Transpose and norms.** `calculus` has migrated neither: 492 sites of `^T` and 736 of
`\|`, the second-largest backlog after `linear_algebra`. See the general section.

---

## Calculus and optimization

Benchmarks: Boyd & Vandenberghe; Nocedal & Wright.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $f$, $f^{\star}$, $x^{\star}$ | objective, optimal value, minimizer | star, not asterisk-free superscript |
| $\eta$ | step size | |
| $L$ | smoothness constant | $\lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x - y \rVert_2$ |
| $\mu$ | strong-convexity modulus | $\nabla^2 f \succeq \mu I$ |
| $\kappa = L/\mu$ | condition number of the objective | |
| $M$ | Hessian Lipschitz constant | $\lVert \nabla^2 f(u) - \nabla^2 f(v) \rVert_{\mathrm{op}} \le M \lVert u - v \rVert_2$ |
| $\Delta_k = f(x_k) - f^{\star}$ | optimality gap | |
| $\lambda_{\min}$, $\lambda_{\max}$ | extreme Hessian eigenvalues | use these names, not indices |

### Contested conventions

**$L$-smoothness.** Ruling: $f$ is $L$-smooth when its gradient is $L$-Lipschitz, and for
$f \in C^2$ this is equivalent to the **operator-norm bound**

$$
\lVert \nabla^2 f(x) \rVert_{\mathrm{op}} \le L \quad \text{for all } x,
$$

equivalently $-L I \preceq \nabla^2 f(x) \preceq L I$, i.e. every Hessian eigenvalue lies in
$[-L, L]$.

Matches Nesterov's class $C_L^{1,1}$ of functions with $L$-Lipschitz gradient, whose standard
equivalent for $f \in C^2$ is $\lVert \nabla^2 f(x) \rVert_{\mathrm{op}} \le L$.

Loser: `calculus_optimization/03/first_principles.ipynb` cell 5, Definition 2.2, which
states the equivalence as $\lambda_{\max}(\nabla^2 f) \le L$. That condition is strictly
weaker: a Hessian with eigenvalues $\lbrace -100, 1 \rbrace$ satisfies it and is not
$1$-smooth. Module 03 then applies the definition in Theorem 2.7.1 and Proof 3.3(c) to
nonconvex functions, where the gap is real. `calculus_optimization/02` Definition 2.4 has
the correct statement and is the model to copy.

**The descent-lemma parabolas.** `calculus_optimization/02/README.md` says the graph "fits
between two parabolas of opening $\pm L$"; the module's own `exercises.ipynb` boxes
"opening $\pm \frac{L}{2}$".

Ruling: state the bound, not the word. The bounding quadratics are
$f(x) + \nabla f(x)^\top (y - x) \pm \tfrac{L}{2} \lVert y - x \rVert_2^2$, whose second
derivative is $\pm L$. Where a module wants the informal phrasing, it must say which
quantity "opening" names.

**$\mu$ carries two meanings.** In this area and in `optimization/03` and `optimization/08`,
$\mu$ is the strong-convexity modulus. In `optimization/06` and `optimization/07`, $\mu_i$
is an inequality multiplier.

Ruling: $\mu$ **without a constraint index**, appearing next to $L$ or $\kappa$, is the
strong-convexity modulus; that reading wins because it spans nine modules across four areas
against two modules for the multiplier reading. $\mu_i$ **with a constraint index**, next to
$g_i(x) \le 0$ and complementary slackness, is the inequality multiplier. A module that
needs both in the same derivation renames the multipliers to $\nu_i \ge 0$ and says so in
its notation table.

---

## Optimization

Benchmarks: Boyd & Vandenberghe; Nocedal & Wright; Bertsekas.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $\min f(x)$ s.t. $h(x) = 0$, $g(x) \le 0$ | standard form | every problem is a **minimization**; maximize $f$ by minimizing $-f$ |
| $\mathcal{L}(x, \lambda, \mu)$ | Lagrangian | $\mathcal{L} = f + \lambda^\top h + \mu^\top g$ |
| $\lambda$ | equality multipliers | free in sign |
| $\mu$ | inequality multipliers | $\mu \succeq 0$ |
| $p^{\star}$, $d^{\star}$ | primal and dual optimal values | weak duality is $d^{\star} \le p^{\star}$ |
| $g(\lambda, \mu) = \inf_x \mathcal{L}$ | dual function | |
| $\mathcal{A}(x)$ | active set at $x$ | |
| $\eta$ | step size | |

### Contested conventions

**Lagrangian sign.** Ruling: constraints enter with a **plus**,

$$
\mathcal{L}(x, \lambda, \mu) = f(x) + \lambda^\top h(x) + \mu^\top g(x), \qquad \mu \succeq 0,
$$

and for the parametrized problem $\min f(x)$ s.t. $h(x) = b$ the sensitivity theorem reads

$$
\frac{d p^{\star}}{d b} = -\lambda^{\star}.
$$

Matches Boyd & Vandenberghe §5.1 and §5.6, where the perturbed problem $g_i(x) \le u_i$
gives $\partial p^{\star}/\partial u_i = -\lambda_i^{\star}$.

Evidence: the plus form appears 25 times, the minus form 7.

Losers to migrate:

- `optimization/05/first_principles.ipynb` — Definition 4 fixes the plus form, then Proof 6
  writes $\mathcal{L} = x^\top A x - \lambda(x^\top x - 1)$ and Proof 5 uses
  $-\beta(\sum_i p_i E_i - \bar{E})$. The text papers over this with the parenthetical
  "mind the sign convention of the subtracted constraint"; delete that phrase and fix the
  algebra.
- `optimization/05/exercises.ipynb` — three sites, including L2.6's
  $\mathcal{L} = w^\top \Sigma w - \alpha(w^\top w - 1) - \beta(v_1^\top w)$.
- `optimization/07/exercises.ipynb` L2.3 — the mean-variance portfolio Lagrangian.
- `calculus/06/exercises.ipynb` — the catenary problem's augmented Lagrangian.
- `probability_statistics/exercises.md` (legacy area-root file) — the PCA Lagrangian.

The mechanical rule that prevents recurrence: rewrite every maximization as the
minimization of $-f$ **before** forming $\mathcal{L}$, so the sensitivity sign never has to
flip mid-notebook.

**Multiplier letters.** Ruling: $\lambda$ for equalities, $\mu \succeq 0$ for inequalities.

This is what `optimization/06` already does, and it deliberately differs from Boyd &
Vandenberghe, who write $\lambda$ for inequalities and $\nu$ for equalities, and from Nocedal
& Wright, who use a single indexed $\lambda_i$ for both. The repository's equality-only module
(`optimization/05`) is written entirely in $\lambda$, so adopting Boyd's letters would mean
rewriting that module to gain nothing. The divergence is stated once here and must be repeated
in `optimization/06`'s notation table alongside its Boyd citation, because a reader holding
Boyd open will otherwise read every sign backwards.

**Which theorem the multiplier signs come from.** `optimization/05`'s range-space KKT
formula carries a sign error flagged by the audit. That is a mathematical defect, not a
notational one, but it is downstream of the same drift, and it should be re-derived from the
plus-form Lagrangian above rather than patched.

---

## Probability and statistics

Benchmarks: Wasserman; Casella & Berger; Durrett; Bishop.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $(\Omega, \mathcal{F}, \mathbb{P})$ | probability space | $\Omega$ is the sample space |
| $\mathbb{P}(A \mid B)$ | conditional probability | `\mid`, never a raw pipe |
| $X$, $Y$, $Z$ | random variables | uppercase; realizations lowercase |
| $F_X$, $f_X$, $p_X$ | CDF, density, pmf | |
| $\mathbb{E}[X]$, $\operatorname{Var}(X)$, $\operatorname{Cov}(X, Y)$ | moments | |
| $\mathcal{N}(\mu, \Sigma)$ | Gaussian | second argument is the **covariance** |
| $\Sigma$, $\Sigma^{-1}$ | covariance, precision | precision written out, or named $\Theta$ |
| $S$ | sample covariance | keeps $\Sigma$ for the population covariance |
| $(n)_k$ | falling factorial, ordered selections | never $P(n, k)$ |
| $\hat{\theta}$, $\theta_0$ | estimator, true parameter | |
| $I(\theta)$ | Fisher information | not to be confused with mutual information $I(X; Y)$ |
| $\xrightarrow{p}$, $\xrightarrow{d}$, $\xrightarrow{\text{a.s.}}$ | convergence modes | always label the arrow |

### Contested conventions

**Negative Binomial.** Ruling: **name the convention every time**. A bare
$\mathrm{NB}(r, p)$ is forbidden.

Three parameterizations currently coexist and are silently mixed:

| Name | Support | pmf | Mean | Variance |
|---|---|---|---|---|
| $\operatorname{NB}_{\mathrm{t}}(r, p)$, trials to the $r$-th success | $k \in \lbrace r, r+1, \ldots \rbrace$ | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ | $r/p$ | $r(1-p)/p^2$ |
| $\operatorname{NB}_{\mathrm{f}}(r, p)$, failures before the $r$-th success | $k \in \lbrace 0, 1, 2, \ldots \rbrace$ | $\binom{k+r-1}{k}p^r(1-p)^k$ | $r(1-p)/p$ | $r(1-p)/p^2$ |
| NB2, mean–dispersion $(\mu, r)$ | $k \in \lbrace 0, 1, 2, \ldots \rbrace$ | reparameterization of $\operatorname{NB}_{\mathrm{f}}$ with $p = r/(r+\mu)$ | $\mu$ | $\mu + \mu^2/r$ |

Two facts the register fixes, because getting them wrong is what the audit caught:

- $\operatorname{NB}_{\mathrm{t}}$ and $\operatorname{NB}_{\mathrm{f}}$ differ by the shift
  $k \mapsto k - r$, so they have the same variance and means differing by $r$.
- Only $\operatorname{NB}_{\mathrm{f}}$ admits **non-integer** $r$. The Gamma–Poisson
  mixture produces exactly that, so a Bayesian predictive can never be
  $\operatorname{NB}_{\mathrm{t}}$. NB2 is a reparameterization of
  $\operatorname{NB}_{\mathrm{f}}$, not a third family.

Casella & Berger §3.2 gives $\operatorname{NB}_{\mathrm{t}}$ first and
$\operatorname{NB}_{\mathrm{f}}$ as the standard alternative; both names above are theirs.

Where each loser lives:

- `probability_statistics/04/first_principles.ipynb` Definition 2.3 and the family table use
  $\operatorname{NB}_{\mathrm{t}}$ under the unqualified name "NegBinomial".
- `probability_statistics/04/exercises.ipynb` L0.3 and L2.5 use NB2, quoting
  $\operatorname{Var} = \mu + \mu^2/r$ against a Definition 2.3 whose variance is
  $r(1-p)/p^2$.
- `probability_statistics/10/first_principles.ipynb` Proof 3.4 and
  `probability_statistics/10/exercises.ipynb` L1.3 produce
  $\mathrm{NB}(a', b'/(b'+1))$ on $\lbrace 0, 1, \ldots \rbrace$ with non-integer shape —
  i.e. $\operatorname{NB}_{\mathrm{f}}$ — while citing module 04's definition.

**Precision matrix.** Ruling: $\Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$
is the eigenvalue matrix repo-wide. The precision matrix is written $\Sigma^{-1}$, or given
the standalone name $\Theta$ in graphical-model contexts where it is estimated as an object
in its own right (Friedman, Hastie & Tibshirani, graphical lasso).

This overrides Bishop PRML §2.3, which writes $\Lambda = \Sigma^{-1}$, because
$\lambda_i \to \Lambda$ is a forced pairing that $\Sigma^{-1}$ is not.

Loser: `probability_statistics/07` uses $\Lambda$ for the precision matrix in roughly 82
places. The module has already felt the collision and worked around it: Proof 3.6
diagonalizes $\Sigma = Q\Lambda_{\text{eig}}Q^\top$ with an invented subscript, purely to
avoid clashing with its own precision matrix. Adopting the ruling deletes that workaround.

**The letter $P$.** `probability_statistics/01` Definition 2.4 fixes $P$ as the probability
measure, then Definition 2.7 introduces $P(n, k) = n!/(n-k)!$ for permutations three cells
later. Ruling: $\mathbb{P}$ for the measure, $(n)_k$ for the count. See the general section.

**Total variation versus $\ell_1$.** `probability_statistics/04` L1.1 labels a Le Cam bound
"total variation" while L3.4 in the same module correctly labels the same quantity $\ell_1$.

Ruling: for two distributions $p$ and $q$ on a discrete space,

$$
d_{\mathrm{TV}}(p, q) = \sup_A \lvert p(A) - q(A) \rvert = \tfrac{1}{2}\lVert p - q \rVert_1 .
$$

The factor $\tfrac{1}{2}$ is the whole content of the distinction. Every bound must say which
of the two quantities it controls, because Le Cam's inequality is usually quoted in the
$\ell_1$ form and is therefore twice the total-variation bound.

---

## Information theory

Benchmarks: Cover & Thomas; MacKay.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $H(X)$ | entropy of a random variable | |
| $H(X, Y)$ | **joint** entropy | two random-variable arguments |
| $H(Y \mid X)$ | conditional entropy | `\mid` |
| $H_b(p)$ | binary entropy function | |
| $H_{\times}(p, q)$ | **cross-entropy** between distributions | distinct symbol; see the ruling |
| $D_{\mathrm{KL}}(p \parallel q)$ | Kullback–Leibler divergence | `\parallel`, never a raw pipe or `\|` |
| $D_f(p \parallel q)$ | $f$-divergence with generator $f$ | |
| $I(X; Y)$, $I(X; Y \mid Z)$ | mutual information | semicolon between the two variables |
| $h(X)$ | differential entropy | lowercase $h$, distinct from $H$ |
| $C = \max_{p(x)} I(X; Y)$ | channel capacity | |
| $\mathcal{X}$, $K$ | alphabet and its size | $K = \lvert \mathcal{X} \rvert$ everywhere, including Fano |
| $\mathcal{L}_{\mathrm{NCE}}$ | InfoNCE loss | unnormalized; see the ruling |

### Contested conventions

**Joint entropy versus cross-entropy.** Ruling: $H(X, Y)$ is joint entropy;
cross-entropy is $H_{\times}(p, q) = -\sum_x p(x)\log q(x)$.

Matches Cover & Thomas §2.2, which defines $H(X, Y)$ as the joint entropy of a pair. Cover &
Thomas never assign a symbol to cross-entropy, so nothing is being overruled on that side —
the two-argument $H$ is simply already taken.

Evidence: $H(X, Y)$ appears 61 times across `information_theory/02`, `05` and the area
README; $H(p, q)$ appears 46 times across `information_theory/01` exercises, `03` (README,
first_principles, exercises), `06` and the legacy `information_theory/entropy_cross_entropy.md`.
The two-argument $H$ therefore means two different things in adjacent modules, and no file
warns the reader.

Losers to migrate: every $H(p, q)$ site listed above becomes $H_{\times}(p, q)$. The
decomposition then reads

$$
H_{\times}(p, q) = H(p) + D_{\mathrm{KL}}(p \parallel q),
$$

which is unambiguous in a way the current $H(p, q) = H(p) + D_{\mathrm{KL}}(p \parallel q)$
is not. `information_theory/03` already writes $\mathrm{CE}$ twice in its perplexity
discussion; keep that as the *name of the training loss* in applications prose, introduced
once as "the cross-entropy $H_{\times}(p, q)$, written $\mathrm{CE}$ in the ML literature",
never as a competing definition.

**InfoNCE normalization.** Ruling: the loss is the plain $K$-way softmax cross-entropy,
with **no** $\tfrac{1}{K}$:

$$
\mathcal{L}_{\mathrm{NCE}} = -\mathbb{E}\left[\log \frac{e^{f(x_1, y_1)}}{\sum_{j=1}^{K} e^{f(x_1, y_j)}}\right].
$$

Under this convention $\mathcal{L}_{\mathrm{NCE}} \ge 0$, chance level is $\log K$, and the
bound is $I(X; Y) \ge \log K - \mathcal{L}_{\mathrm{NCE}}$.

Matches van den Oord, Li & Vinyals (2018), eq. (4), and Poole et al. (2019).

Loser: `information_theory/05/first_principles.ipynb` Proof 3.7 defines the loss **with**
the $\tfrac{1}{K}$ and then, in Step 4, asserts $\mathcal{L}_{\mathrm{NCE}} \ge 0$ "because
it is a cross-entropy over $K$ classes" and uses
$I \ge \log K - \mathcal{L}_{\mathrm{NCE}}$. Both claims belong to the unnormalized loss.
With the $\tfrac{1}{K}$ in place the correct statements are
$\mathcal{L}_{\mathrm{NCE}} \ge -\log K$ and $I \ge -\mathcal{L}_{\mathrm{NCE}}$, so the
module's headline theorem and its ceiling argument are each off by exactly $\log K$. Steps 2
and 3 inherit the same $\tfrac{1}{K}$ and change with it.

Every *use* elsewhere already assumes the unnormalized convention, which is why the ruling
goes this way: `information_theory/05` L2.3 computes
$I \ge \log 256 - 0.5$, and `information_theory/06` L0.3 reads a converged loss of $4.85$
nats against a chance level of $\log 128 = 4.852$. Fixing the definition fixes the module;
fixing the uses would break four problems.

**Logarithm base.** Ruling: every numerical answer carries its unit — **bits** for
$\log_2$, **nats** for $\ln$ — and no single derivation mixes the two.

A bare $\log$ is permitted only in a base-free statement (one where the base cancels, such
as Fano's $P_e \ge (H(X) - I(X; Y) - \log 2)/\log M$). This is the current de facto split —
`information_theory/01`, `02` and `03` work in bits, `05` and `06` in nats — and the split
is fine; what is not fine is a numeric answer with no unit attached.

**Fano's inequality.** Ruling: alphabet size is $K$ throughout, and
`information_theory/02` Proof 3.6 is the canonical statement.

Fano is currently proved three times with three notations: $K$ values in `01` exercises L3.2
(mislabelled "Weak Form for Zero Side Information" although it is the standard statement),
$Y \in \lbrace 1, \ldots, K \rbrace$ in `02` Proof 3.6, and an alphabet of size $M$ in `05`
Proof 3.6. Modules `01` and `05` should state the result, link to `02`, and add only their
own new content.

---

## Numerical methods

Benchmarks: Trefethen & Bau; Higham, *Accuracy and Stability*; Heath.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $t$ | significand digits, hidden bit included | $t = 53$ for binary64 |
| $\varepsilon_{\mathrm{mach}} = \beta^{1-t}$ | gap between $1$ and the next float | $2^{-52}$ for binary64 |
| $u = \tfrac{1}{2}\beta^{1-t}$ | unit roundoff | $2^{-53}$ for binary64 |
| $\operatorname{fl}(x)$ | the floating-point value of $x$ | standard model $\operatorname{fl}(a \circ b) = (a \circ b)(1 + \delta)$, $\lvert \delta \rvert \le u$ |
| $\kappa_f(x)$ | condition number of the problem | forward error $\lesssim \kappa \times$ backward error |
| $e_n = x_n - x^{\star}$ | error of the $n$-th iterate | |
| $p$ | order of convergence | $\lvert e_{n+1} \rvert \approx C \lvert e_n \rvert^p$ |
| $h$ | step size or mesh width | |
| $T_k$ | Chebyshev polynomial of the first kind | as in linear algebra |
| $\rho$ | Bernstein-ellipse parameter | |

### Contested conventions

**Machine epsilon.** Ruling: $\varepsilon_{\mathrm{mach}} = \beta^{1-t}$, the gap between
$1$ and the next representable number, so $\varepsilon_{\mathrm{mach}} = 2^{-52}$ for
binary64; the **unit roundoff** is $u = \tfrac{1}{2}\varepsilon_{\mathrm{mach}} = 2^{-53}$.

Matches Higham, *Accuracy and Stability of Numerical Algorithms*, §2.1, and
`numpy.finfo(np.float64).eps`.

Spelling: `\varepsilon_{\mathrm{mach}}` and `u`. The symbol $\varepsilon_M$ is retired.

Losers to migrate:

- `numerical_methods/05/first_principles.ipynb` Definition 4 — "$\varepsilon_M = 2^{-53}$
  (unit roundoff)", which conflates the two quantities and contradicts its own
  `exercises.ipynb` L2.1 ("float64: $\varepsilon_M = 2^{-52}$"). The module then prints two
  contradictory tables of the same quantity: L1.6 gives
  $\varepsilon_M^{1/3} = 6.1 \times 10^{-6}$ and L3.1 gives $4.8 \times 10^{-6}$.
- `numerical_computing/README.md` line 15 — "$\varepsilon_{\mathrm{mach}} = 2^{-53}$",
  contradicting `numerical_computing/01`.
- `linear_algebra/08/first_principles.ipynb` §7 — "$\epsilon_{\text{mach}} = 2^{-53}$".
- `numerical_methods/computation.ipynb` (legacy, area root) — defines machine epsilon as
  "the smallest number such that $\operatorname{fl}(1 + \varepsilon) \gt 1$", which is the
  misconception `numerical_methods/01`'s own table exists to refute. Under
  round-to-nearest-even that threshold is $2^{-53} + 2^{-105}$, not $2^{-52}$. Repair the
  definition where it stands; the legacy file is not to be deleted here.
- `calculus/02` and `calculus/03` — see the calculus section.

**Order of convergence.** Ruling: $p$ names the order,
$\lvert e_{n+1} \rvert \approx C \lvert e_n \rvert^p$, with $C$ the asymptotic error
constant.

$p$ therefore may **not** also name the significand length, which is what
`numerical_methods/01` currently does when it writes $\varepsilon_{\mathrm{mach}} = \beta^{1-p}$
three modules before `numerical_methods/02` uses $p$ for the convergence order. Following
Higham, the significand length is $t$; the substitution is mechanical and touches one
definition. See the numerical-computing section for the full four-way split of $p$.

---

## Numerical computing

Benchmarks: Higham; Goldberg; Muller.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $t$ | significand bits **including** the hidden bit | Higham's convention; $t = 53$ for binary64 |
| $u = 2^{-t}$ | unit roundoff | $2^{-53}$ for binary64 |
| $\varepsilon_{\mathrm{mach}} = 2u$ | gap at $1$ | $2^{-52}$ for binary64 |
| $\operatorname{ulp}(x) = 2^{e-t+1}$ | unit in the last place | |
| $\gamma_n = nu/(1 - nu)$ | accumulated rounding factor | |
| $\kappa(A)$ | condition number | subscript the norm when it matters: $\kappa_2$, $\kappa_\infty$ |
| $q$ | number of operands in an einsum-style expression | |
| $d$ | decimal digits of precision | $u \approx 10^{-d}$ |

### Contested conventions

**The letter $p$.** Ruling: $p$ is not used in this area. Significand length is $t$
(including the hidden bit), decimal digits are $d$, and operand count is $q$.

The audit found $p$ carrying four incompatible meanings:
`numerical_computing/01` Definition 2.1 ("the significand is a $(p+1)$-bit number", with
"fraction bits $p = 52$"), `05` Definition 2.1 ("$p$ significand bits including the implicit
leading bit", $p = 53$), `03` Derivation 3.5 ("$u = 10^{-p}$, so $p \approx 15.95$"), and
`04` Theorem 2.3 (shapes $S^{(1)}, \ldots, S^{(p)}$).

Higham uses $t$ for the significand length throughout, which is why $t$ wins.

**Machine epsilon.** Same ruling as the numerical-methods section.
`numerical_computing/01` already has the values right — $\varepsilon_{\mathrm{mach}} = 2^{-52}$,
$u = 2^{-53}$ — and is the model for them; only its use of $p$ for the 52 fraction bits changes,
to $t = 53$. The area README, which states $\varepsilon_{\mathrm{mach}} = 2^{-53}$ and thereby
contradicts its own first module, is the loser.

---

## Differential equations

Benchmarks: Strogatz; Hirsch, Smale & Devaney; Teschl.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $t$ | the independent variable in dynamics | $x$ only for spatial boundary-value problems |
| $y$, $\mathbf{x}$ | scalar solution, state vector | $\dot{y} = dy/dt$ |
| $A$, $e^{At}$ | system matrix, matrix exponential | |
| $\lambda_i$ | eigenvalues of $A$ | complex, so **no ordering is imposed**; name them by role (stable, unstable, centre) |
| $J$ | Jacobian at a fixed point | |
| $V$ | Lyapunov function | $\dot{V}$ its orbital derivative |
| $\mathcal{L}\lbrace f \rbrace(s)$, $F(s)$ | Laplace transform | declared exception, module 06 only |
| $L$ | the differential operator, e.g. Sturm–Liouville | |
| $L_s$ | smoothness constant when a gradient-flow argument needs one | keeps $L$ free for the operator |
| $h$ | numerical step size | matches `numerical_methods` |

### Contested conventions

**$L$ has two jobs.** Ruling: inside this area $L$ is the differential operator; the
smoothness constant of an optimization analogy is $L_s$.

This is already what `differential_equations/08` does — its stability window is
$0 \lt \eta \lt 2/L_s$ — and the register ratifies it rather than forcing the area onto the
optimization letter.

**$\mathcal{L}$ as the Laplace transform.** Declared exception, `differential_equations/06`
only, with a callout at first use. The brace-delimited argument
$\mathcal{L}\lbrace f \rbrace(s)$ distinguishes it from the Lagrangian
$\mathcal{L}(x, \lambda, \mu)$, which never takes braces.

**Eigenvalue ordering does not apply.** The repository default orders eigenvalues
descending, but that presupposes real eigenvalues. Linear systems here have complex spectra,
so modules must name eigenvalues by dynamical role and never write
$\lambda_1 \ge \cdots \ge \lambda_n$ for a non-symmetric $A$. The one place this area does
sort — `differential_equations/01` exercises, for a symmetric positive-definite $A$ — is
already descending and already compliant. `differential_equations/08` exercises is ascending
and is a loser under the linear-algebra ruling.

---

## Graph theory

Benchmarks: Bollobás; Chung, *Spectral Graph Theory*; Newman.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $G = (V, E)$ | graph | $n = \lvert V \rvert$, $m = \lvert E \rvert$ |
| $A$ | adjacency matrix | inside this area $A$ is always the adjacency matrix; a generic matrix is $M$ |
| $D$ | degree matrix | $D = \operatorname{diag}(d_1, \ldots, d_n)$ |
| $L = D - A$ | combinatorial Laplacian | |
| $L_{\mathrm{sym}} = D^{-1/2} L D^{-1/2}$ | symmetric normalized Laplacian | spectrum in $[0, 2]$ |
| $L_{\mathrm{rw}} = D^{-1} L = I - P$ | random-walk Laplacian | |
| $P = D^{-1}A$ | random-walk operator | **row**-stochastic; declared exception |
| $B$ | incidence matrix | $L = BB^\top$ |
| $0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$ | Laplacian spectrum | ascending; declared exception |
| $\lambda_2$ | algebraic connectivity (Fiedler value) | index from $1$, not from $0$ |
| $h(G)$ | Cheeger constant / conductance | say which normalization every time |
| $\kappa(G)$, $\kappa'(G)$ | vertex and edge connectivity | distinct from the numerical $\kappa(A)$ |
| $\tau(G)$ | number of spanning trees | |
| $\nu(G)$ | maximum matching size | |
| $\delta(s, v)$ | shortest-path distance | |

### Contested conventions

**Ascending Laplacian spectra.** Declared exception to the repository's descending default,
for the reason given in the linear-algebra section. Every module using it carries a callout.

Loser on indexing only: the legacy `graph_theory/first_principles.md` writes
$0 = \lambda_0 \le \cdots \le \lambda_{n-1}$ and states the matrix-tree theorem as
$\tau(G) = \tfrac{1}{n}\lambda_1 \cdots \lambda_{n-1}$. Under $1$-indexing that is
$\tau(G) = \tfrac{1}{n}\lambda_2 \cdots \lambda_n$. The two forms are the same theorem; the
file must pick the repository's indexing so the formula transfers.

**Row-stochastic $P$.** Declared exception, `graph_theory/06` and `graph_theory/07`, because
$L_{\mathrm{rw}} = I - P$ forces it. Stationarity is written $\pi^\top P = \pi^\top$ here,
and the callout must say so explicitly, because the repository default is
$P\pi = \pi$. This site was not on the audit's collision list; it is a third instance of the
Markov-orientation problem.

**Normalized versus unnormalized Cheeger.** The audit found `linear_algebra/10` mixing the
two conventions inside one inequality.

Ruling: state the normalization in the same sentence as the constant. Write
$h(G) = \min_{S} \frac{\lvert \partial S \rvert}{\min(\operatorname{vol} S, \operatorname{vol} \bar{S})}$
for the conductance form and pair it with $\lambda_2(L_{\mathrm{sym}})$; write the
cut-size-over-vertex-count form only with $\lambda_2(L)$. A Cheeger sandwich that mixes them
is false.

**$\kappa$.** Vertex connectivity in this area, condition number in the numerical areas.
Accepted as a surviving collision: the two never co-occur, and both spellings are universal
in their own literature. Each area's notation table must name its own reading.

---

## Mathematical reasoning

Benchmarks: Velleman; Rosen; Graham, Knuth & Patashnik.

| Symbol | Meaning | Convention fixed here |
|---|---|---|
| $\land$, $\lor$, $\lnot$, $\to$, $\leftrightarrow$ | connectives | |
| $\forall$, $\exists$, $\exists!$ | quantifiers | |
| $\vdash$, $\models$ | derivability, semantic entailment | |
| $\mathbb{N} = \lbrace 0, 1, 2, \ldots \rbrace$ | natural numbers | **includes zero** |
| $\lvert A \rvert$ | cardinality | `\lvert ... \rvert`, never `\#A` |
| $\mathcal{P}(A)$ | power set | |
| $(n)_k$, $\binom{n}{k}$ | falling factorial, binomial coefficient | never $P(n, k)$ |
| $D_n$ | derangement count | |
| $C_n$ | Catalan number | distinct from Chebyshev, which is $T_k$ |
| $T(n) = aT(n/b) + f(n)$ | divide-and-conquer recurrence | |
| $\alpha = \log_b a$ | Master-theorem exponent | local to module 06 |
| $O$, $\Omega$, $\Theta$, $o$, $\omega$ | asymptotics | bare capitals |

### Contested conventions

**$\mathbb{N}$ contains zero.** Already consistent: `mathematical_reasoning/02` and the
legacy `mathematical_reasoning/first_principles.md` both state
$\mathbb{N} = \lbrace 0, 1, 2, \ldots \rbrace$, and `mathematical_reasoning/04` builds
induction from $0$. Ratified so that later modules cannot drift.

**Cardinality.** Ruling: $\lvert A \rvert$. `\#` appears 15 times repo-wide and should be
migrated. The audit noted that `02` writes $\lvert A \rvert$ while `05` writes $\lvert S \rvert$;
that is a letter choice, not a collision, and needs no ruling.

**Permutation counts.** Ruling: $(n)_k$. Loser: `mathematical_reasoning/05`
first_principles (7 sites, including Definition 2.4 and the Section 3 statements table) and
its README misconception row. See the general section.

**$\Omega$ and $\Theta$.** This is the only area that uses $\Omega$ and $\Theta$ as
asymptotic symbols. `probability_statistics` uses $\Omega$ for the sample space and $\Theta$
for a parameter set. Accepted as a surviving collision, since the areas do not overlap and
the argument type disambiguates.

**$\alpha$.** `mathematical_reasoning/06` uses $\alpha = \log_b a$ in the Master theorem.
Ratified as local to that module, and it must appear in module 06's notation table because
$\alpha$ is a significance level in `probability_statistics` and a damping factor in the
PageRank problems of `linear_algebra/08` and `linear_algebra/09`.

---

## Enforcement

Three checks make this file self-policing. None exists yet; all three belong in
`tools/validate_content.py`.

1. **Banned spellings.** `tools/validate_content.py` already rejects `\argmin` and
   `\argmax`. Extend the same list with `^T`, `\|`, `\mathcal{O}`, `\text{Var}`,
   `\mathrm{Var}`, `\varepsilon_M`, and a bare `P(n,` in any `.md` or `.ipynb` file.
2. **Notation table present.** Every module `README.md` must carry a notation table, per
   [`STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20 item 7. Eight of 87 have one today.
3. **Declared exceptions carry callouts.** Any file using an ascending eigenvalue ordering,
   a row-stochastic transition matrix, or $\mathcal{L}$ for anything but the Lagrangian must
   contain a `> [!NOTE]` callout within the same file.

Until those checks exist, the rulings are enforced by reading. A module is compliant when
its notation table is a subset of this file and every symbol in its notebooks appears in
that table.
