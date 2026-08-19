# Calculus

Calculus is the study of two limits and the theorem that ties them together. The derivative
is the limit of a difference quotient; the integral is the limit of a sum; the Fundamental
Theorem says each undoes the other.

Everything in this area is built from those two limits. The mean value theorem turns a local
derivative into a global statement. Taylor's theorem turns a derivative at one point into a
polynomial model with an error you can bound. The gradient turns the derivative into a
direction, the Hessian turns it into a curvature, and the Jacobian determinant turns it into
a volume factor. Green, Stokes and the divergence theorem are the Fundamental Theorem again,
one dimension at a time.

Those objects are the working vocabulary of machine learning. A loss surface is a scalar
field; backpropagation is the chain rule; a training step reads the gradient; a convergence
proof reads the Hessian spectrum; a change of variables in a normalizing flow is the Jacobian
factor; a neural ODE is an initial value problem.

This area is written for a reader who can already manipulate functions and quantifiers and
now wants the theorems with their hypotheses attached — not the formula sheet. Fifteen
modules run from the set-theoretic definition of a function to the matrix exponential and
the phase plane.

---

## Prerequisites

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
Every prerequisite in the table below is drawn from it, not from memory.

This area depends on two others:

- [`../mathematical_reasoning/`](../mathematical_reasoning/) — quantifier logic, set notation,
  injectivity and surjectivity, and induction. This is the hard prerequisite for Modules 01,
  02 and 08: an $\varepsilon$-$\delta$ definition is a nested quantifier statement, and you
  cannot negate one you cannot parse.
- [`../linear_algebra/`](../linear_algebra/) — Modules 10 through 15 only. Fréchet
  differentiability is a statement about linear maps, the Hessian is a symmetric matrix, the
  change-of-variables factor is a determinant, and $e^{At}$ needs a canonical form.

Modules 01 through 09 need no linear algebra. Modules 10 through 15 need
[`../linear_algebra/01`](../linear_algebra/01_vectors_spaces_and_subspaces/) through
[`../linear_algebra/07`](../linear_algebra/07_canonical_forms_and_svd/).

This area is a prerequisite for `calculus_optimization`, `optimization`,
`probability_statistics`, `differential_equations`, `numerical_methods`, `numerical_computing`
and `information_theory`.

---

## Module index

| Module | What it covers | Prerequisites | Problems |
| :--- | :--- | :--- | :---: |
| [`01_functions_and_properties/`](01_functions_and_properties/) | A function as a subset of $X \times Y$, natural domain, image and preimage, injectivity and bijectivity, monotonicity without derivatives, the unique even/odd decomposition, periodicity, inverse functions and reflection across $y = x$ | [mr/02](../mathematical_reasoning/02_sets_relations_and_functions/) | 40 |
| [`02_limits_and_continuity/`](02_limits_and_continuity/) | $\varepsilon$-$\delta$ limits and uniqueness, one-sided limits, the squeeze theorem, algebra of limits, classification of discontinuities, the intermediate and extreme value theorems, asymptotic notation $O$, $o$ and $\sim$, temperature-controlled softmax limits | [mr/01](../mathematical_reasoning/01_propositional_and_predicate_logic/), Module 01 | 45 |
| [`03_single_variable_derivatives/`](03_single_variable_derivatives/) | The derivative as a secant limit, the Carathéodory formulation and the chain rule proved from it, product and quotient rules, the Leibniz $n$-th derivative rule by induction, implicit differentiation, the inverse function theorem in one variable, dual-number automatic differentiation | Module 02 | 40 |
| [`04_derivative_applications_optimization/`](04_derivative_applications_optimization/) | Fermat's interior extremum theorem, Rolle, the mean value theorem, the Cauchy mean value theorem and L'Hôpital's rule derived from it, convexity through $f''$, Newton's method and its quadratic rate | Module 03 | 40 |
| [`05_indefinite_and_definite_integrals/`](05_indefinite_and_definite_integrals/) | Antiderivatives, Darboux upper and lower sums, the refinement lemma, both parts of the Fundamental Theorem, the Leibniz rule for differentiating under a variable limit, substitution, integration by parts, the Weierstrass $t = \tan(x/2)$ substitution | Module 03 | 40 |
| [`06_integral_applications_geometry_physics/`](06_integral_applications_geometry_physics/) | Area between curves, disk, washer and shell volumes, arc length, surfaces of revolution, centroids and both Pappus theorems, work, hydrostatic force, continuous probability densities and their moments | Module 05 | 40 |
| [`07_improper_integrals_special_functions/`](07_improper_integrals_special_functions/) | Type I and Type II improper integrals, comparison and $p$-tests, Dirichlet's test, the Gamma and Beta functions and their relation, differentiation under the integral sign, Frullani integrals, Fresnel integrals | Modules 02, 05 | 40 |
| [`08_sequences_series_convergence/`](08_sequences_series_convergence/) | Monotone convergence, the Cauchy criterion, comparison, ratio, root and integral tests with remainder bounds, alternating series and the Leibniz error bound, Raabe's test derived from Kummer's, Kahan compensated summation | [mr/04](../mathematical_reasoning/04_induction_and_recursion/), Module 02 | 40 |
| [`09_taylor_and_power_series/`](09_taylor_and_power_series/) | Taylor's theorem with the integral, Lagrange and Cauchy remainders, the Maclaurin catalogue, radius of convergence by Cauchy–Hadamard, Abel's lemma and Abel's theorem, Euler's formula from the exponential series | Modules 03, 08 | 40 |
| [`10_multivariable_functions_partials/`](10_multivariable_functions_partials/) | Limits in $\mathbb{R}^n$ and path dependence, partial derivatives, Gâteaux versus Fréchet differentiability as a linear map with $o(\lVert h \rVert)$ remainder, Clairaut's symmetry theorem and Peano's counterexample | Modules 02, 03, [la/01](../linear_algebra/01_vectors_spaces_and_subspaces/) | 40 |
| [`11_gradients_directional_derivatives/`](11_gradients_directional_derivatives/) | The master formula $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$, steepest ascent, the gradient orthogonal to level sets, tangent planes, gradient flow and its Lyapunov dissipation | Module 10, [la/04](../linear_algebra/04_orthogonality_projections_and_qr/) | 40 |
| [`12_hessian_jacobian_curvature/`](12_hessian_jacobian_curvature/) | The Hessian and the Jacobian, the second-derivative test, Sylvester's criterion, the Rayleigh quotient bound on curvature, $\lvert \det J \rvert$ as a local volume factor, Newton's method in $\mathbb{R}^n$, the softmax Hessian | Modules 09, 11, [la/06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/) | 40 |
| [`13_multiple_integrals_coordinate_transforms/`](13_multiple_integrals_coordinate_transforms/) | Jordan measurability, Fubini's theorem and its counterexample, polar, cylindrical and spherical coordinates, the Jacobian change-of-variables factor, the Gaussian integral in two and $n$ dimensions, the volume $V_n(R)$ of an $n$-ball through Gamma | Modules 06, 12, [la/05](../linear_algebra/05_determinants_trace_and_matrix_polynomials/) | 40 |
| [`14_vector_calculus_field_theorems/`](14_vector_calculus_field_theorems/) | Line and surface integrals, conservative fields and path independence, divergence and curl, Green's theorem for Type I and Type II regions, Stokes' theorem, the divergence theorem, the Helmholtz–Hodge decomposition | Modules 11, 13 | 40 |
| [`15_ordinary_differential_equations/`](15_ordinary_differential_equations/) | Separable equations and integrating factors, second-order linear equations, the Wronskian and Abel's identity, Picard–Lindelöf through the Banach fixed point theorem, the matrix exponential $e^{At}$, phase-plane classification by trace and determinant, Lyapunov stability, neural ODEs | Modules 05, 09, [la/07](../linear_algebra/07_canonical_forms_and_svd/) | 40 |
| **Total** | **15 modules** | — | **605** |

Every module carries 40 fully solved problems in four tiers (Module 02 carries 45), split
roughly 8 at L0, 10 to 13 at L1, 10 to 12 at L2, and 8 to 12 at L3.

> [!NOTE]
> **Module 06 formats its problems differently.** It is the only exercise notebook here that puts
> a `#### Problem Statement` sub-heading under each problem. It still holds 40 problems — 8, 12,
> 12 and 8 — like every other module in this area. The upgrade normalises the format.

> [!WARNING]
> **Scope gaps.** Several results the benchmark texts treat as central are absent or
> unproved. Uniform continuity and Heine–Cantor are never defined, though a Module 02
> exercise asks for a uniform-continuity proof. `\limsup` and Bolzano–Weierstrass are used by
> the root test in Module 08 without being stated. The multivariable chain rule is stated in
> Module 11 and omitted from Module 10, and neither the inverse nor the implicit function
> theorem appears anywhere. Lagrange multipliers appear only inside one Module 06 exercise.
> The Riemann–Stieltjes integral, which is how Apostol and Rudin frame the subject, is absent.
> Change of variables in $\mathbb{R}^n$, Stokes' theorem, term-by-term differentiation of a
> power series, the second-derivative test and Sylvester's criterion are all stated without
> proof. Read the chapters named under **References** alongside the modules that need them.

---

## Module architecture

Each numbered directory holds exactly the three files required by
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20.

### `README.md`

Module title, a short overview, a `> [!NOTE]` callout carrying the single most important
result, prerequisites and downstream links as relative paths, learning outcomes, a Mermaid
concept map, a notation table, a core-results table, common misconceptions, an exercise index
that matches the notebook, and references at chapter precision.

### `first_principles.ipynb`

Theory, following the WHY → INTUITION → WHAT → DEFINITION → DERIVATION → INTERPRETATION →
EXAMPLE → CONNECTION → KEY TAKEAWAYS progression of §5.

The contract requires executable code cells that verify each major theorem numerically, two
to four matplotlib figures showing the geometry or dynamics of the central idea, worked
numerical examples, and a closing **Key Takeaways** cell.

### `exercises.ipynb`

Forty fully solved problems in four tiers:

- **L0** — concept checks
- **L1** — foundations
- **L2** — AI/ML and physics applications
- **L3** — challenge proofs

Each problem carries a statement, an intuition note, a full derivation, a
`$$\boxed{...}$$` answer, and a key takeaway.

### Honest status

> [!WARNING]
> **This area got a lite pass, not the full contract.** Every module now carries a few verification
> code cells (added to check the numeric answers the audit flagged as wrong, plus each module's
> headline result), and some carry a figure, but not yet the full six-cell / two-to-four-figure
> contract. Run `python3 tools/curriculum_stats.py --modules` for the live counts and
> `python3 tools/check_module.py --all --failing` for what still falls short. The closing Key
> Takeaways cell exists only in Module 07 so far. The only other runnable code in this directory
> is the legacy notebook described under **Companion resources**.

Five further gaps between the contract and the current files:

- Geometry is drawn as ASCII art inside fenced text blocks rather than as figures — the
  $\varepsilon$-$\delta$ band in Module 02, the bowl and the saddle in Module 12, the
  differentiability hierarchy in Module 10, the trace-determinant plane and the Runge-Kutta
  stability region in Module 15. Modules 02, 04, 05, 07, 08, 11 and 12 tag these fences
  `text`; Modules 01, 03, 10 and 15 leave them untagged. Some of the diagrams are
  geometrically wrong, and some leak raw LaTeX into the fence, where it renders literally.
  Module 02 also carries a `python` fence holding a bisection routine that is not a code
  cell and therefore never runs.
- Fourteen of the fifteen module READMEs point the reader at `first_principles.md` and
  `exercises.md`. **Those files do not exist.** The real files are `first_principles.ipynb`
  and `exercises.ipynb`. Module 03 is the only one with the names right. Two cells inside
  `10_multivariable_functions_partials/exercises.ipynb` carry the same broken reference.
- No module README carries the `> [!NOTE]` callout, the prerequisites section, the notation
  table or the core-results table that §20 requires. Only Modules 03 and 05 state per-tier
  problem counts; both are correct.
- Three problem-numbering dialects coexist: `Problem L0.1` in Modules 01, 03, 11 and 12;
  `Problem 0.1` in Modules 02, 04, 05, 06, 08, 13 and 15; and a flat `Problem 1` through
  `Problem 40` in Modules 07, 09, 10 and 14.
- L3 competition attributions are **unverified and in places demonstrably wrong**. "Putnam
  1990 A1" is attached to four unrelated problems across Modules 04, 09, 13 and 14, and the
  same integral appears in Modules 05 and 07 under two different Putnam numbers. Treat every
  Putnam and Tripos label in this area as decoration until it has been checked against the
  MAA archive.

All 31 notebooks in this directory open with a working Google Colab badge.

---

## Notation

The repository-wide register is [`../docs/notation.md`](../docs/notation.md); its "Calculus"
section governs this area.

Four conventions matter here, and **the current notebooks do not yet follow the first two**:

- **The Taylor polynomial is $P_n$ and its remainder is $R_n$.** Not $T_n$, which is reserved
  for a linear map in the linear-algebra register. Module 09 currently writes $T_n$ in its
  README and both notebooks.
- **Machine epsilon is $\varepsilon_{\mathrm{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}$,
  and the unit roundoff is $u = \tfrac{1}{2}\varepsilon_{\mathrm{mach}} = 2^{-53}$.** Module 02
  spells the symbol $\varepsilon_{\mathrm{mach}}$ and Module 03 spells it
  $\epsilon_{\mathrm{mach}}$, and between them the same constant is quoted as
  $2.22 \times 10^{-16}$, $2.2 \times 10^{-16}$, $2 \times 10^{-16}$ and $10^{-16}$ in four
  different places. Finite-difference step-size arguments belong in terms of $u$.
- **The limit quantifiers are $\varepsilon$ and $\delta$, never $\epsilon$.** This is the one
  notation rule the area follows consistently.
- **Absolute value is `\lvert ... \rvert` and a norm is `\Vert ... \rVert`.** A raw pipe inside
  `$...$` in a table row splits the cell on GitHub, and `\|` loses its backslash there. The
  area still carries a large backlog of `\|` and `^T` spellings inside notebook cells; the
  ruling is `\Vert` and `^\top`.

---

## Suggested order

The fifteen modules split into two blocks, and
[`../docs/prerequisites.md`](../docs/prerequisites.md) places them in two different stages of
the repository-wide reading order.

**Single variable — Modules 01 to 09.** Read them in order. Nothing here needs linear algebra.

1. **01 — Functions and properties.** Domain, image, monotonicity, parity, inverses.
2. **02 — Limits and continuity.** The $\varepsilon$-$\delta$ machinery, IVT and EVT. This is
   the module everything after it leans on.
3. **03 — Single-variable derivatives.** The chain rule, proved rather than asserted.
4. **04 — Derivative applications.** Rolle through L'Hôpital and Newton's method.
5. **05 — Integrals.** Darboux sums and both halves of the Fundamental Theorem.
6. **06 — Integral applications.** Where the differential element comes from.
7. **07 — Improper integrals and special functions.** Gamma, Beta, and convergence tests.
8. **08 — Sequences and series.** Convergence tests and error bounds.
9. **09 — Taylor and power series.** Remainders with explicit bounds, and radius of convergence.

**Multivariable — Modules 10 to 15.** Interleave with linear algebra: Module 10 needs
[`../linear_algebra/01`](../linear_algebra/01_vectors_spaces_and_subspaces/), Module 12 needs
the spectral theorem from
[`../linear_algebra/06`](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/), and
Module 15 needs canonical forms from
[`../linear_algebra/07`](../linear_algebra/07_canonical_forms_and_svd/).

10. **10 — Multivariable functions and partials.** The differentiability hierarchy.
11. **11 — Gradients and directional derivatives.** The gradient as direction and as normal.
12. **12 — Hessian, Jacobian and curvature.** Classifying a critical point; the volume factor.
13. **13 — Multiple integrals and coordinate transforms.** Fubini and change of variables.
14. **14 — Vector calculus and field theorems.** Green, Stokes, divergence.
15. **15 — Ordinary differential equations.** Existence, the matrix exponential, phase portraits.

For a targeted read: 02 → 03 → 08 → 09 is the minimum for a Taylor-based error bound, and
09 → 10 → 11 → 12 is the minimum for reading an optimization convergence proof.

Two backward dependencies are unmet today. Module 04 proves Newton's quadratic convergence
using Taylor's theorem with Lagrange remainder, which is stated only in Module 09 — recorded
as a work item in [`../docs/prerequisites.md`](../docs/prerequisites.md). Module 08 applies
the root test through $\limsup$ and invokes Bolzano–Weierstrass in its Cauchy-criterion proof,
and neither is defined anywhere in the area;
[`../docs/notation.md`](../docs/notation.md) rules that $\limsup$ and $\liminf$ must be defined
in Module 08 before the root test uses them.

---

## Companion resources

One legacy file predates the numbered curriculum and sits at the root of this directory. It
is outside the dependency graph: no numbered module depends on it, and it is not maintained
against the module notebooks.

| File | What it actually contains |
| :--- | :--- |
| [`visual_demos.ipynb`](visual_demos.ipynb) | Twenty cells, eleven of them code, with nine stored matplotlib figures. Five sections: forward versus central differences on $\sin$ with the roundoff floor on a log-log plot; a polynomial and an exponential plotted beside their first and second derivatives; hand-written trapezoidal and Simpson routines compared on $\int_0^{\pi} \sin x \, dx$ with an error table; Taylor polynomials of $e^x$ and $\sin x$ at increasing degree, plus a printed remainder-bound table; and contour-plus-quiver plots for $x^2 + 4y^2$ and the saddle $x^2 - y^2$ with two gradient-descent trajectories. |

Three caveats on that notebook, all checkable:

- It is **not** a substitute for the missing module code cells. It touches five of the
  fifteen modules — 03, 04, 05, 09 and 11 — and verifies no theorem stated in any module
  notebook.
- Its first cell runs `from scipy import integrate, misc`. Neither name is used anywhere else
  in the file, and `scipy.misc` is deprecated and scheduled for removal — the stored output of
  that cell is the deprecation warning. The import should be dropped.
- Its preamble is not the §21 standard preamble, and its figures do not follow the §21 figure
  rules.

The file is kept because deleting it is the repository owner's decision, not a rewrite's.

---

## References

Benchmark texts for this area, per [`../CLAUDE.md`](../CLAUDE.md), at chapter precision.

**Primary — single variable.**

- **Spivak, M.** (2008). *Calculus*, 4th ed. Publish or Perish.
  Ch. 3–4 (functions, graphs) → Module 01;
  Ch. 5–7 (limits, continuous functions, the three hard theorems) → Module 02;
  Ch. 9–11 (derivatives, differentiation, the significance of the derivative) → Modules 03–04;
  Ch. 12 (inverse functions) → Modules 01, 03;
  Ch. 13–14 (integrals, the Fundamental Theorem) and Ch. 19 (integration in elementary terms)
  → Modules 05–06;
  Ch. 20 (approximation by polynomial functions) → Module 09;
  Ch. 22–24 (infinite sequences, infinite series, uniform convergence and power series)
  → Modules 08–09. Ch. 24 is the missing ingredient for Module 09's term-by-term
  differentiation theorem.
- **Apostol, T. M.** (1967). *Calculus, Vol. I*, 2nd ed. Wiley.
  Ch. 1–2 (the concepts of integral calculus, applications of integration) → Modules 05–06;
  Ch. 3 (continuous functions) → Module 02;
  Ch. 4 (differential calculus) → Modules 03–04;
  Ch. 5 (the relation between integration and differentiation) → Module 05;
  Ch. 7 (polynomial approximations to functions) → Module 09;
  Ch. 8 (introduction to differential equations) → Module 15;
  Ch. 10 (sequences, infinite series, improper integrals) → Modules 07–08;
  Ch. 11 (sequences and series of functions) → Module 09.

**Primary — multivariable.**

- **Apostol, T. M.** (1969). *Calculus, Vol. II*, 2nd ed. Wiley.
  Ch. 6–7 (linear differential equations, systems of differential equations) → Module 15;
  Ch. 8 (differential calculus of scalar and vector fields) → Modules 10–12;
  Ch. 9 (applications of differential calculus: implicit functions, extrema with constraints)
  → Modules 11–12;
  Ch. 10 (line integrals) and Ch. 12 (surface integrals) → Module 14;
  Ch. 11 (multiple integrals) → Module 13.
- **Hubbard, J. H., & Hubbard, B. B.** (2015). *Vector Calculus, Linear Algebra, and
  Differential Forms: A Unified Approach*, 5th ed. Matrix Editions.
  Ch. 1 (vectors, matrices, derivatives) → Module 10;
  Ch. 2 (solving equations: Newton, the inverse and implicit function theorems)
  → Modules 04, 10;
  Ch. 3 (manifolds, Taylor polynomials in several variables, quadratic forms, curvature,
  Lagrange multipliers) → Modules 11–12;
  Ch. 4 (integration: Fubini, change of variables) → Module 13;
  Ch. 5 (volumes of manifolds) → Modules 06, 14;
  Ch. 6 (forms and vector calculus) → Module 14.
- **Spivak, M.** (1965). *Calculus on Manifolds*. Benjamin.
  Ch. 2 (differentiation: the derivative as a linear map, the chain rule, inverse and implicit
  function theorems) → Modules 10–11;
  Ch. 3 (integration: Fubini, partitions of unity, change of variables) → Module 13;
  Ch. 4–5 (differential forms, the generalized Stokes theorem) → Module 14.

**Primary — differential equations (Module 15).**

- **Teschl, G.** (2012). *Ordinary Differential Equations and Dynamical Systems*. AMS.
  Ch. 2 (initial value problems: contraction, Picard–Lindelöf, Gronwall, extensibility,
  dependence on initial conditions);
  Ch. 3 (linear equations, the matrix exponential);
  Ch. 6–7 (dynamical systems, planar systems, Poincaré–Bendixson).
- **Hirsch, M. W., Smale, S., & Devaney, R. L.** (2013). *Differential Equations, Dynamical
  Systems, and an Introduction to Chaos*, 3rd ed. Academic Press.
  Ch. 2–4 (planar linear systems, phase portraits, classification by trace and determinant);
  Ch. 6 (higher-dimensional linear systems, the exponential of a matrix);
  Ch. 7–9 (nonlinear systems, equilibria, Lyapunov functions).
- **Strogatz, S. H.** (2015). *Nonlinear Dynamics and Chaos*, 2nd ed. Westview.
  Ch. 2 (flows on the line), Ch. 5 (linear systems), Ch. 6 (the phase plane),
  Ch. 7 (limit cycles).

**Supporting.**

- **Rudin, W.** (1976). *Principles of Mathematical Analysis*, 3rd ed. McGraw-Hill.
  Ch. 3 (numerical sequences and series, $\limsup$) and Ch. 4 (continuity, uniform continuity)
  supply what Modules 02 and 08 use without defining;
  Ch. 6 (the Riemann–Stieltjes integral) is the framing Module 05 omits;
  Ch. 7 (sequences and series of functions), Ch. 8 (special functions, the Gamma function),
  Ch. 9 (functions of several variables), Ch. 10 (integration of differential forms).
- **Marsden, J. E., & Tromba, A. J.** (2011). *Vector Calculus*, 6th ed. Freeman.
  Ch. 2–4 (differentiation, higher-order derivatives, vector-valued functions);
  Ch. 5–6 (double and triple integrals, the change-of-variables formula);
  Ch. 7–8 (integrals over paths and surfaces, the integral theorems of vector analysis).
- **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
  §3.1–3.2 for the convexity results Module 04 states and Module 12 uses.
- **Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization*, 2nd ed. Springer.
  Ch. 3 (line search) and Ch. 6 (quasi-Newton, the secant equation) behind Module 12's
  BFGS problems.

**Problem sources.**

- **Demidovich, B. P.** (1964). *Problems in Mathematical Analysis*. Mir.
- **Pólya, G., & Szegő, G.** (1972). *Problems and Theorems in Analysis I*. Springer.
  Part I, Ch. 1–2 for the asymptotics and sequence-limit problems in Modules 02 and 08.
- **Kaczor, W. J., & Nowak, M. T.** (2000–2003). *Problems in Real Analysis I–III*. AMS.

The L3 tiers additionally carry Putnam and Cambridge Tripos labels. As noted under **Honest
status**, those labels are unverified and several are known to be wrong; do not cite them.
