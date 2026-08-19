# Numerical Methods

Most mathematical models admit no closed-form solution. This area builds the algorithms that
produce an answer anyway — roots, interpolants, derivatives, integrals, fits, and trajectories —
on a machine that carries only finitely many digits.

The organising question is never "what does the algorithm compute". It is "how wrong is the
answer, and why". Every module therefore carries an error theorem: a convergence order, an
absolute-stability region, or a bound of the form forward error $\lesssim$ condition number
$\times$ backward error.

The intended reader is someone who will run these methods inside a larger system — a solver, a
training loop, a simulation — and who needs to know in advance which method breaks, on what
input, and how the failure looks.

Eight modules, 160 fully solved problems. The area assumes calculus and linear algebra and
repays them immediately: the Taylor remainder, the SVD, and the matrix exponential are the
working tools here, not background.

---

## Prerequisites

The repository-wide dependency graph, with a per-module breakdown and a suggested global study
order, is in [`../docs/prerequisites.md`](../docs/prerequisites.md).

This area depends on three others:

- [`../calculus/`](../calculus/) — Taylor's theorem with remainder, the mean value theorem,
  the Riemann integral, and the ODE background that module 08 discretises.
- [`../linear_algebra/`](../linear_algebra/) — orthogonality and projection, QR, the SVD,
  matrix norms, eigenvalues, and the spectral radius.
- [`../numerical_computing/`](../numerical_computing/) — bit-level IEEE-754 practice,
  error-propagation technique, and condition numbers at the level of the machine.

Module 08 additionally assumes
[`../differential_equations/02_existence_uniqueness_picard_lindelof/`](../differential_equations/02_existence_uniqueness_picard_lindelof/):
this area covers only the *numerics* of initial value problems, never the existence theory.

The closest neighbour is [`../numerical_computing/`](../numerical_computing/). That area is the
*practice* of reliable fast computing; this one is the *theory* of the algorithms that run on it.
Module 01 here and `numerical_computing/01`–`03` cover the same ground from opposite directions.

Downstream, [`../optimization/`](../optimization/) builds on modules 02, 03, 05 and 07.

---

## Module index

| Module | What it covers | Prerequisites | Problems |
| :--- | :--- | :--- | :---: |
| [01 Error Analysis and Floating Point](01_error_analysis_and_floating_point/) | The floating-point system $F(\beta, t, e_{\min}, e_{\max})$, the standard model $\operatorname{fl}(a \circ b) = (a \circ b)(1+\delta)$, machine epsilon versus unit roundoff, catastrophic cancellation, the Sterbenz lemma, scalar conditioning versus algorithmic stability, forward and backward error | [calculus/09](../calculus/09_taylor_and_power_series/), [numerical_computing/03](../numerical_computing/03_conditioning_and_condition_numbers/) | 20 |
| [02 Root-Finding Methods](02_root_finding_methods/) | Bisection and the intermediate value theorem, Newton's quadratic rate, the secant order $\varphi = (1+\sqrt{5})/2$, Newton at a root of multiplicity $m$, stopping criteria and achievable accuracy, Brent-style hybrid safeguards | [calculus/04](../calculus/04_derivative_applications_optimization/), [01](01_error_analysis_and_floating_point/) | 20 |
| [03 Fixed-Point Iteration and Convergence](03_fixed_point_iteration_and_convergence/) | The Banach fixed-point theorem and contraction constants, a priori and a posteriori error bounds, the order-$p$ characterisation via vanishing derivatives, Aitken $\Delta^2$ and Steffensen acceleration, spectral radius for affine iterations | [linear_algebra/06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/), [02](02_root_finding_methods/) | 20 |
| [04 Polynomial and Spline Interpolation](04_polynomial_and_spline_interpolation/) | Lagrange and Newton forms, divided differences, the barycentric formula, the interpolation error theorem, Lebesgue constants, the Runge phenomenon and the Chebyshev cure, Hermite interpolation, cubic splines and B-splines | [linear_algebra/03](../linear_algebra/03_linear_systems_and_direct_factorizations/), [01](01_error_analysis_and_floating_point/) | 20 |
| [05 Numerical Differentiation](05_numerical_differentiation/) | Forward, backward and central differences, stencil weights by undetermined coefficients, Richardson extrapolation, the truncation-versus-round-off V-curve and the optimal step $h^{\ast} \sim u^{1/3}$, complex-step differentiation | [01](01_error_analysis_and_floating_point/) | 20 |
| [06 Numerical Integration (Quadrature)](06_numerical_integration_quadrature/) | Newton–Cotes and composite rules, Euler–Maclaurin and Romberg, Gauss–Legendre exactness and optimality, adaptive quadrature, the curse of dimensionality, Monte Carlo and quasi-Monte Carlo | [calculus/05](../calculus/05_indefinite_and_definite_integrals/), [05](05_numerical_differentiation/) | 20 |
| [07 Linear Least Squares](07_linear_least_squares/) | Normal equations and orthogonal projection, the condition-squaring identity $\kappa_2(A^{\top}A) = \kappa_2(A)^2$, Gram–Schmidt, Householder and Givens QR, the SVD and the pseudoinverse, ridge regression and truncated SVD | [linear_algebra/07](../linear_algebra/07_canonical_forms_and_svd/), [01](01_error_analysis_and_floating_point/) | 20 |
| [08 Numerical ODE Solvers](08_numerical_ode_solvers/) | Euler and Runge–Kutta methods, Butcher tableaux and order conditions, the Dahlquist equivalence theorem and barriers, absolute stability and stiffness, embedded adaptive pairs, symplectic integrators, Neural ODEs and the adjoint method | [differential_equations/02](../differential_equations/02_existence_uniqueness_picard_lindelof/), [06](06_numerical_integration_quadrature/) | 20 |
| **Total** | **8 modules** | — | **160** |

Two topics that neighbouring texts place here are deliberately **absent**, and are not claimed
above: Bézier and Bernstein curves (module 04 mentions them once, in a one-line aside on font
rendering) and automatic differentiation (module 05 uses it only as the cost comparison against
complex-step differentiation). Classical iterative linear solvers — Jacobi, Gauss–Seidel, SOR —
appear in module 03's concept map but are not developed there.

---

## Module architecture

Each `NN_slug/` directory holds exactly three files, per
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20.

**`README.md`** — module overview, a `> [!NOTE]` callout carrying the single most important
result, prerequisite and downstream links as relative paths, learning outcomes, a Mermaid concept
map, a notation table, a core-results table, common misconceptions, an exercise index matching
the notebook tier for tier, and references at chapter precision.

**`first_principles.ipynb`** — theory in the WHY $\to$ INTUITION $\to$ WHAT $\to$ DEFINITION
$\to$ DERIVATION $\to$ INTERPRETATION $\to$ EXAMPLE $\to$ KEY TAKEAWAYS order of §5. Each of the
eight notebooks develops five to seven complete step-by-step proofs: five in modules 01–03, six
in modules 05–08, seven in module 04. §20 further requires executable code cells verifying each
major theorem numerically, two to four figures showing the geometry of the central idea, worked
numerical examples, and a closing **Key Takeaways** cell.

**`exercises.ipynb`** — 20 fully solved problems in four tiers, identical in shape across all
eight modules:

| Tier | Purpose | Problems per module |
| :--- | :--- | :---: |
| **L0** | Concept checks | 4 |
| **L1** | Foundations | 6 |
| **L2** | AI/ML and physics applications | 6 |
| **L3** | Challenge proofs | 4 |

Every problem carries a statement, an intuition paragraph, a full derivation, a
`$$\boxed{...}$$` answer, and a key-takeaway line. Where an answer is numeric or algorithmic,
§20 requires a code cell that recomputes it.

Both notebooks in every module open with an **Open in Colab** badge, so any module can be read
on GitHub or run in the browser.

> [!IMPORTANT]
> **Current state — read before trusting a printed number.** No notebook in this area contains
> an executable code cell or a figure today, and no `first_principles.ipynb` ends with the
> required Key Takeaways cell. Every table labelled "measured", "computed on a fine grid" or
> "empirical confirmation" is therefore an assertion, not a verified result. An upgrade wave is
> adding the code cells, figures and closing cells that §20 and §21 require. Until it lands,
> treat printed numbers as claims to check.

---

## Notation

The repository-wide register, including every contested convention and its ruling, is
[`../docs/notation.md`](../docs/notation.md). Two rulings are fixed there specifically for this
area.

**Machine epsilon versus unit roundoff.** $\varepsilon_{\mathrm{mach}} = \beta^{1-t}$ is the gap
between $1$ and the next representable number, so $\varepsilon_{\mathrm{mach}} = 2^{-52}$ in
binary64. The unit roundoff is
$u = \tfrac{1}{2}\varepsilon_{\mathrm{mach}} = 2^{-53}$, and it is $u$ that appears in the
standard model. The symbol $\varepsilon_M$ is retired.

**Significand length versus convergence order.** The significand carries $t$ digits, following
Higham; $p$ is reserved for the order of convergence, $\lvert e_{n+1} \rvert \approx C \lvert e_n \rvert^{p}$.

Both rulings have outstanding migrations inside this area. Module 05 still writes
$\varepsilon_M$ and assigns it $2^{-53}$, contradicting module 01 and its own exercises; module
01 still writes $\beta^{1-p}$ for the significand gap. Prefer `docs/notation.md` where a module
disagrees with it.

Elsewhere the area follows the usual conventions: $h$ for a step size or mesh width,
$e_n = x_n - x^{\star}$ for iteration error, $\kappa$ for a condition number, $T_k$ for the
Chebyshev polynomial of the first kind, and $\rho$ for the Bernstein-ellipse parameter.

---

## Suggested order

1. **[01 Error Analysis and Floating Point](01_error_analysis_and_floating_point/)** — first,
   without exception. Every later module quotes its conditioning and backward-error vocabulary.
2. **[02 Root-Finding Methods](02_root_finding_methods/)**, then
   **[03 Fixed-Point Iteration and Convergence](03_fixed_point_iteration_and_convergence/)**.
   Module 03 generalises what module 02 does concretely, so reading them in the other order
   makes the Banach theorem look abstract for no reason.
3. **[04 Polynomial and Spline Interpolation](04_polynomial_and_spline_interpolation/)** — the
   approximation-theory spine. Modules 05 and 06 are both corollaries of its error theorem.
4. **[05 Numerical Differentiation](05_numerical_differentiation/)**, then
   **[06 Numerical Integration (Quadrature)](06_numerical_integration_quadrature/)**. Read them
   as a pair: differentiation amplifies error by $1/h$, integration averages it away.
5. **[07 Linear Least Squares](07_linear_least_squares/)** — independent of 02–06. It can be
   read straight after module 01 by anyone who already has the SVD.
6. **[08 Numerical ODE Solvers](08_numerical_ode_solvers/)** — last. It consumes the quadrature
   rules of module 06, the Newton solves of module 02, and the stability language of module 01.

Short paths through the area: for optimisation, take 01, 02, 03, 05, 07. For scientific
computing and simulation, take 01, 04, 06, 08.

---

## Companion resources

Two legacy files predate the numbered modules and still sit at the area root. They are kept
until their content is migrated, and they are **not** the current standard — the numbered
modules are.

| File | What it actually contains |
| :--- | :--- |
| [`first_principles.md`](first_principles.md) | A 374-line single-file Markdown overview: floating point, root finding, interpolation, quadrature, least squares, and a short section on modelling. It duplicates modules 01, 02, 04, 06 and 07 at markedly lower depth, has no fixed-point, differentiation or ODE material, and carries no cross-references to the numbered modules. |
| [`computation.ipynb`](computation.ipynb) | A 26-cell legacy notebook with 13 executable code cells and stored outputs — the only executable code in the area today. It covers a machine-epsilon loop, a cancellation plot, bisection / Newton / secant with a convergence comparison, Lagrange interpolation, the Runge phenomenon, a natural cubic spline via the Thomas algorithm, composite trapezoid and Simpson, and a finite-difference error sweep. Nothing on least squares or ODEs. |

`computation.ipynb` carries one known error: its opening cell defines machine epsilon as the
smallest $\varepsilon$ with $\operatorname{fl}(1 + \varepsilon) \gt 1$. That is exactly the
misconception module 01's own table exists to refute — under round-to-nearest-even the threshold
is $2^{-53} + 2^{-105}$, not $\varepsilon_{\mathrm{mach}} = 2^{-52}$. Read module 01 for the
correct definition.

---

## References

Benchmarks for this area, per [`../CLAUDE.md`](../CLAUDE.md): Trefethen & Bau; Higham; Heath.

**Primary**

- Trefethen, L. N., & Bau, D. — *Numerical Linear Algebra*. Lectures 6–11 (projection, QR,
  least squares); Lectures 12–15 (conditioning, stability, backward error); Lecture 18
  (least-squares perturbation); Lecture 37 (Golub–Welsch).
- Higham, N. J. — *Accuracy and Stability of Numerical Algorithms*. Chs. 1–2 (standard model);
  Ch. 4 (summation, Kahan); Chs. 19–20 (least squares).
- Heath, M. T. — *Scientific Computing: An Introductory Survey*. Ch. 1.3 (floating point);
  Ch. 3 (least squares); Ch. 5 (nonlinear equations); Ch. 8.6 (differentiation); Ch. 9 (ODEs).

**Per-topic canon**

- Burden, R. L., & Faires, J. D. — *Numerical Analysis*. Ch. 1 (error); Ch. 2 (root finding,
  fixed points, Aitken and Steffensen); Ch. 3 (interpolation and splines); Ch. 4
  (differentiation, quadrature, Romberg, adaptive, Gauss); Ch. 5 (ODEs).
- Quarteroni, A., Sacco, R., & Saleri, F. — *Numerical Mathematics*. Ch. 2 (conditioning);
  Chs. 4 and 6 (iterative and nonlinear solvers); Ch. 8 (interpolation); Ch. 10 (extrapolation
  and quadrature).
- Trefethen, L. N. — *Approximation Theory and Approximation Practice*. Chs. 12–15 (minimax,
  Lebesgue constants); Chs. 13 and 18 (Runge phenomenon, potential theory); Ch. 19
  (Clenshaw–Curtis versus Gauss).
- de Boor, C. — *A Practical Guide to Splines*. Ch. 4 (cubic splines and end conditions);
  Chs. 9–11 (B-splines, Cox–de Boor, knot insertion).
- Davis, P. J., & Rabinowitz, P. — *Methods of Numerical Integration*. Chs. 2–4.
- Golub, G. H., & Van Loan, C. F. — *Matrix Computations*. Chs. 5.1–5.5 (Householder and Givens
  QR, least squares, pivoting); Ch. 11 (iterative methods).
- Björck, Å. — *Numerical Methods for Least Squares Problems*. Chs. 1–4.
- Hansen, P. C. — *Rank-Deficient and Discrete Ill-Posed Problems*. Chs. 3–7 (Tikhonov, TSVD,
  filter factors, the L-curve).
- Hairer, E., Nørsett, S. P., & Wanner, G. — *Solving Ordinary Differential Equations I*.
  Chs. II.1–II.6. Hairer, E., & Wanner, G. — *Solving Ordinary Differential Equations II*.
  Chs. IV.1–IV.8 (stiffness, A- and L-stability, BDF, Radau).
- Hairer, E., Lubich, C., & Wanner, G. — *Geometric Numerical Integration*. Chs. VI and IX
  (symplectic methods, backward error analysis).
- Butcher, J. C. — *Numerical Methods for Ordinary Differential Equations*. Chs. 2–3 (order
  conditions, rooted trees).
- Iserles, A. — *A First Course in the Numerical Analysis of Differential Equations*. Chs. 2
  and 4 (zero-stability, Dahlquist equivalence and barriers).
- LeVeque, R. J. — *Finite Difference Methods for Ordinary and Partial Differential Equations*.
  Chs. 5–8.
- Press, W. H., et al. — *Numerical Recipes*. Ch. 3 (interpolation); Ch. 5.7 (optimal step
  size); Chs. 7.8–7.9 (low-discrepancy sequences).

**Papers**

- Goldberg, D. (1991). What every computer scientist should know about floating-point
  arithmetic. *ACM Computing Surveys*, 23(1).
- Fornberg, B. (1988). Generation of finite difference formulas on arbitrarily spaced grids.
  *Mathematics of Computation*, 51(184).
- Squire, W., & Trapp, G. (1998). Using complex variables to estimate derivatives of real
  functions. *SIAM Review*, 40(1). Martins, J. R. R. A., Sturdza, P., & Alonso, J. J. (2003).
  The complex-step derivative approximation. *ACM TOMS*, 29(3).
- Berrut, J.-P., & Trefethen, L. N. (2004). Barycentric Lagrange interpolation.
  *SIAM Review*, 46(3).
- Trefethen, L. N., & Weideman, J. A. C. (2014). The exponentially convergent trapezoidal rule.
  *SIAM Review*, 56(3).
- Dormand, J. R., & Prince, P. J. (1980). A family of embedded Runge–Kutta formulae.
  *Journal of Computational and Applied Mathematics*, 6(1).
- Chen, R. T. Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D. (2018). Neural ordinary
  differential equations. *NeurIPS*.
