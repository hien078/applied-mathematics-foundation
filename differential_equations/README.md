# Differential Equations

A differential equation states a local law of change. Solving one means reconstructing a global
function from that law — and, more often, understanding the solution without ever writing it down.

This area builds that understanding in two passes. The first is **constructive**: classify an
equation, then solve it by integrating factor, characteristic equation, matrix exponential, or
Laplace transform. The second is **qualitative**: when no formula exists, certify that a solution
exists and is unique, then read its long-run behaviour off a phase portrait or a Lyapunov function.

The area ends where continuous-time thinking has entered machine learning. Gradient descent is an
Euler step on a gradient flow, a residual network is an Euler step on a learned vector field, and a
diffusion sampler is an ODE run backwards. Those are not analogies here; they are theorems proved
from the same machinery as the rest of the area.

It is written for a reader who already has single- and multivariable calculus and the spectral
theory of matrices, and who wants ODE theory at the level of Strogatz, Hirsch–Smale–Devaney and
Teschl — not a recipe list. Eight modules, **160 fully solved problems**, four difficulty tiers.

> [!NOTE]
> **Executable code has not reached this area yet.** All 16 module notebooks here are still
> markdown-only. Several algorithms appear as fenced `text` pseudocode blocks
> inside markdown cells, and no `first_principles.ipynb` yet carries the closing "Key Takeaways" cell.
> An upgrade wave is adding the code cells and figures that `STYLE_GUIDE.md` §18, §20 and §21
> require. Until it lands, the only executable code in this area is the legacy
> [`computation.ipynb`](computation.ipynb) described under [Companion resources](#companion-resources).

---

## Prerequisites

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
It is the source of truth; the per-module column below is taken from it.

This area depends on three others:

- [`../calculus/`](../calculus/) — improper integrals and the Gamma function (Topic 07), series
  convergence (Topic 08), the Jacobian and Hessian (Topic 12), the field theorems (Topic 14), and
  the survey-level ODE module (Topic 15) that this area expands.
- [`../linear_algebra/`](../linear_algebra/) — vector spaces (Topic 01), the spectral theorem
  (Topic 06), and Jordan form and the SVD (Topic 07).
- [`../optimization/`](../optimization/) — gradient-descent convergence rates (Topic 03), used only
  by Module 08.

Nothing in this area is a prerequisite for another area except
[`../numerical_methods/08_numerical_ode_solvers/`](../numerical_methods/08_numerical_ode_solvers/),
which builds on the existence theory of Module 02.

---

## Module index

| Module | What it covers | Prerequisites | Problems |
|---|---|---|---:|
| [01 — Classification and First-Order ODEs](01_classification_and_first_order_odes/) | Order, linearity and autonomy as a routing table; direction fields and isoclines; separable equations; the integrating factor $\mu(t)=e^{\int p\,dt}$; exactness via $M_y=N_x$ on simply connected domains; Bernoulli, homogeneous-degree and Riccati substitutions | [calculus/15](../calculus/15_ordinary_differential_equations/) | 20 |
| [02 — Existence, Uniqueness and Picard–Lindelöf](02_existence_uniqueness_picard_lindelof/) | Lipschitz conditions; the integral-equation reformulation; Banach fixed point, with both the $T^N$ and the Bielecki-norm route; Grönwall and Osgood; Peano existence; maximal continuation and blow-up; the non-uniqueness fan of $y'=3y^{2/3}$ | [calculus/08](../calculus/08_sequences_series_convergence/), [de/01](01_classification_and_first_order_odes/) | 20 |
| [03 — Second-Order Linear ODEs](03_second_order_linear_odes/) | The solution set as a two-dimensional vector space; Wronskian and Abel's identity; characteristic equation with repeated and complex roots; undetermined coefficients and variation of parameters; Cauchy–Euler equations; damping regimes, forced response and resonance | [linear_algebra/01](../linear_algebra/01_vectors_spaces_and_subspaces/), [de/01](01_classification_and_first_order_odes/) | 20 |
| [04 — Systems of ODEs and the Matrix Exponential](04_systems_of_odes_matrix_exponential/) | Companion-matrix reduction; convergence and the semigroup law for $e^{At}$; diagonalizable, Jordan and Putzer computation on defective matrices; fundamental matrices and Abel–Liouville; Duhamel variation of constants; conditioning, scaling-and-squaring, Krylov products | [linear_algebra/07](../linear_algebra/07_canonical_forms_and_svd/), [de/02](02_existence_uniqueness_picard_lindelof/), [de/03](03_second_order_linear_odes/) | 20 |
| [05 — Phase Plane and Stability Analysis](05_phase_plane_and_stability_analysis/) | Nullclines and the trace–determinant classification; Hartman–Grobman; the Lyapunov direct method and LaSalle invariance; the Lyapunov equation for linearized stability; Bendixson–Dulac and Poincaré–Bendixson; van der Pol limit cycles; the Lotka–Volterra first integral; Hopf bifurcation as a labelled preview | [calculus/12](../calculus/12_hessian_jacobian_curvature/), [de/04](04_systems_of_odes_matrix_exponential/) | 20 |
| [06 — Laplace Transform Methods](06_laplace_transform_methods/) | Exponential order and the region of convergence; derivative, shifting and convolution theorems; Heaviside and Dirac forcing; partial fractions and periodic forcing; transfer functions; poles and BIBO stability; Talbot and Gaver–Stehfest inversion, discussed but not executed | [calculus/07](../calculus/07_improper_integrals_special_functions/), [de/03](03_second_order_linear_odes/) | 20 |
| [07 — Boundary Value Problems and PDE Preview](07_boundary_value_problems_and_pde_preview/) | Where BVP uniqueness fails; Sturm–Liouville eigenproblems; the Lagrange identity, weighted orthogonality and the Rayleigh quotient; Green's functions built and then verified; Fourier series; separation of variables for the heat and wave equations; shooting and finite differences | [calculus/14](../calculus/14_vector_calculus_field_theorems/), [linear_algebra/06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/), [de/03](03_second_order_linear_odes/) | 20 |
| [08 — ODEs in Machine Learning](08_odes_in_machine_learning/) | Gradient flow and its discretization; the heavy-ball and Nesterov ODEs with a Lyapunov proof; ResNets as Euler steps; the Neural ODE adjoint method, shown to be backpropagation; continuous normalizing flows and the instantaneous change-of-variables trace formula; the probability-flow ODE of diffusion samplers | [optimization/03](../optimization/03_gradient_descent_and_convergence/), [de/05](05_phase_plane_and_stability_analysis/) | 20 |
| **Total** | **8 modules** | | **160** |

Counts come from `python3 tools/curriculum_stats.py`, not from prose. Every module carries exactly
20 problems split **4 / 6 / 6 / 4** across the four tiers.

---

## Module architecture

Each `NN_slug/` directory holds exactly three files, per `STYLE_GUIDE.md` §20.

### `README.md`

Overview, a `> [!NOTE]` callout with the module's single most important result, prerequisites and
downstream links as working relative paths, learning outcomes, a Mermaid concept map, a notation
table, a core-results table, common misconceptions, an exercise index whose tiers and counts equal
the notebook's, and references at chapter precision.

### `first_principles.ipynb`

Theory in the order `WHY → INTUITION → WHAT → DEFINITION → FORMULATION → DERIVATION →
INTERPRETATION → EXAMPLE → CONNECTION → KEY TAKEAWAYS`.

It must contain executable code cells that verify each major theorem numerically, 2 to 4 figures
showing the geometry or dynamics of the central idea, and a closing **Key Takeaways** cell.

### `exercises.ipynb`

Twenty fully solved problems in four tiers:

- **L0** — concept checks (4 problems)
- **L1** — foundations (6 problems)
- **L2** — AI/ML and physics applications (6 problems)
- **L3** — challenge proofs (4 problems)

Each problem carries a statement, intuition, a full derivation, a `$$\boxed{...}$$` answer, a key
takeaway, and — where the answer is numeric or algorithmic — a code cell that checks it.

### What this area does not yet meet

Stated plainly, so the gap is not mistaken for a design choice:

- **No executable code and no figures yet.** All 16 notebooks here are still markdown-only. A
  phase-plane module with no phase portrait and a Gibbs-phenomenon section with no plot are
  defects, not minimalism.
- **No Key Takeaways cell** in any `first_principles.ipynb`.
- **Module READMEs use an older six-section layout** and are missing the prerequisites/downstream
  links, learning outcomes, notation table, core-results table, and tier-by-tier exercise index that
  the contract above requires.

Notebooks are written with `json.dump` or `nbformat` — never by editing JSON text by hand — and
every notebook opens in Google Colab from the badge in its first cell.

---

## Notation

The repository-wide register is [`../docs/notation.md`](../docs/notation.md). Four conventions are
fixed for this area:

| Symbol | Meaning | Convention |
|---|---|---|
| $t$ | independent variable | $x$ is used only as the spatial variable in boundary-value problems; $\dot{y}$ means $dy/dt$ |
| $\lambda_i$ | eigenvalues of $A$ or of the Jacobian $J$ | complex in general, so **no ordering is imposed** — name them by dynamical role: stable, unstable, centre |
| $L$ vs $L_s$ | differential operator vs smoothness constant | $L$ is the operator (Sturm–Liouville, for instance); an optimization smoothness constant is $L_s$, so Module 08 writes its stability window as $0 \lt \eta \lt 2/L_s$ |
| $\mathcal{L}\lbrace f \rbrace(s)$ | Laplace transform | a declared exception, Module 06 only, flagged at first use; the braces distinguish it from the Lagrangian, which never takes braces |

The step size $h$ matches [`../numerical_methods/`](../numerical_methods/).

---

## Suggested order

Work the modules in numerical order; the dependency graph is almost a chain.

1. **01 → 02 → 03.** Techniques, then the theorem that says the techniques were solving something
   well-posed, then the linear structure that the rest of the area reuses.
2. **04 → 05.** The matrix exponential, then the qualitative theory it makes possible. This is the
   spine of the area.
3. **08.** The machine-learning capstone. It depends on 05 and on
   [`../optimization/03`](../optimization/03_gradient_descent_and_convergence/), so take it last of
   the main line.

Modules **06** and **07** are side branches. Both need only 03, and neither is a prerequisite for
anything else, so read them whenever the application calls for them — 06 for control and signals,
07 for eigenfunction expansions and the step toward PDEs.

For a lighter first pass, [`../calculus/15_ordinary_differential_equations/`](../calculus/15_ordinary_differential_equations/)
covers the same landscape in one survey module.

---

## Companion resources

Two legacy files predate the numbered-module layout and sit at the area root. They are **not**
nodes in the prerequisite graph, no numbered module may depend on them, and they do not follow the
module contract above.

| File | What it actually contains |
|---|---|
| [`first_principles.md`](first_principles.md) | Legacy single-document theory, 521 lines in 7 sections: classification, first-order methods, second-order linear equations, systems and the $2\times 2$ classification, qualitative analysis, numerical methods (Euler, Heun, RK4, adaptive stepping, stiffness), and modelling connections. Superseded by Modules 01–05 and by [`../numerical_methods/08`](../numerical_methods/08_numerical_ode_solvers/). No proofs at the depth of the modules. |
| [`computation.ipynb`](computation.ipynb) | Legacy executable notebook: 23 cells, of which **10 are code cells** with 8 stored figures and no error output. It runs `solve_ivp` on the exponential and logistic equations against their closed forms, measures the observed order of Euler, Heun and RK4 on $y'=-2ty$, draws phase portraits for the four planar linear types, integrates Lotka–Volterra and its logistic variant, and reads stability off Jacobian eigenvalues. It uses its own preamble rather than the `STYLE_GUIDE.md` §21 standard one. |

Read `computation.ipynb` alongside Modules 04 and 05, where its phase portraits and Jacobian
eigenvalue analysis match the theory directly. Its Euler-versus-RK4 convergence study belongs to
[`../numerical_methods/08`](../numerical_methods/08_numerical_ode_solvers/), not to this area.

One sibling module is worth naming as well:

- [`../calculus/15_ordinary_differential_equations/`](../calculus/15_ordinary_differential_equations/)
  — the survey-level companion, and the declared prerequisite of Module 01.

---

## References

Benchmark texts for this area, per `CLAUDE.md`.

**Strogatz, *Nonlinear Dynamics and Chaos*, 2nd ed.**
Ch. 2 flows on the line and the phase line; Ch. 3 one-dimensional bifurcations; Ch. 5–6 linear
systems and the phase plane; Ch. 7 limit cycles, Bendixson–Dulac and Poincaré–Bendixson; Ch. 8
bifurcations in the plane, including Hopf.

**Hirsch, Smale & Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos*, 3rd ed.**
Ch. 1–4 first-order equations and planar linear systems; Ch. 5–7 higher-dimensional linear systems
and the exponential; Ch. 8–9 nonlinear systems, equilibria and Lyapunov functions; Ch. 11
Lotka–Volterra; Ch. 17 the existence–uniqueness proof in $\mathbb{R}^n$.

**Teschl, *Ordinary Differential Equations and Dynamical Systems*.**
Ch. 2 existence, uniqueness, the Bielecki-norm proof, Grönwall and Peano; Ch. 3 linear systems and
$e^{At}$; Ch. 5 Sturm–Liouville theory and oscillation; Ch. 7 Poincaré–Bendixson and Liénard
systems; Ch. 9 Hartman–Grobman and the stable manifold theorem.

### Supporting canonical texts

- **Coddington & Levinson**, *Theory of Ordinary Differential Equations* — Ch. 1–3 existence and
  linear theory; Ch. 7–8 Sturm–Liouville problems and Green's functions.
- **Boyce & DiPrima**, *Elementary Differential Equations and Boundary Value Problems* — Ch. 1–3
  first- and second-order equations; Ch. 6 Laplace transforms; Ch. 7 systems; Ch. 9 nonlinear
  systems and stability; Ch. 10–11 BVPs and Sturm–Liouville.
- **Arnold**, *Ordinary Differential Equations* — Ch. 1–3, the geometric view of an ODE as a
  direction field and of $e^{At}$ as a one-parameter group.
- **Perko**, *Differential Equations and Dynamical Systems* — Ch. 1 linear systems; §2.8
  Hartman–Grobman and the stable manifold theorem; §3.7 and §3.9 limit cycles and Bendixson–Dulac.
- **Khalil**, *Nonlinear Systems* — Ch. 3–4, the Lyapunov direct method and LaSalle's invariance
  principle.
- **Tenenbaum & Pollard**, *Ordinary Differential Equations* — Lessons 9–11, 20–23, 27, 57–58, 63,
  the widest classical catalogue of solution techniques.
- **Schiff**, *The Laplace Transform: Theory and Applications* — Ch. 1–2, existence, Lerch's
  theorem, convolution and the delta function.
- **Evans**, *Partial Differential Equations* — §2.3–2.4, separation of variables and energy
  methods for the heat and wave equations.
- **Higham**, *Functions of Matrices* — Ch. 10, computing the matrix exponential.
- **Putzer** (1966), *American Mathematical Monthly* 73(1) — the algorithm used in Module 04.
- **Moler & Van Loan** (2003), *SIAM Review* 45(1) — nineteen dubious ways to compute $e^{A}$.

### Machine-learning sources

- **Su, Boyd & Candès** (2016), *A Differential Equation for Modeling Nesterov's Accelerated
  Gradient Method*, JMLR 17(153) — Sections 2–3.
- **Chen, Rubanova, Bettencourt & Duvenaud** (2018), *Neural Ordinary Differential Equations*,
  NeurIPS — the adjoint method of Module 08.
- **Grathwohl et al.** (2019), *FFJORD*, ICLR — continuous normalizing flows and Hutchinson trace
  estimation.
- **Song et al.** (2021), *Score-Based Generative Modeling through Stochastic Differential
  Equations*, ICLR — the probability-flow ODE.
- **Gu, Goel & Ré** (2022), *Efficiently Modeling Long Sequences with Structured State Spaces*,
  ICLR — $e^{A\Delta}$ discretization inside a modern architecture.
