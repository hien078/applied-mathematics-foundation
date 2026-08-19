# Optimization

Optimization is where the rest of applied mathematics gets cashed in. A model becomes a
decision only when some objective is minimized over some feasible set.

Nearly every training procedure in machine learning is an instance of that one sentence, and
the difference between a method that works and one that stalls is almost always a property of
the objective rather than a property of the code.

This area develops the subject outward from the standard form: what an optimization problem
*is*, when a point is optimal, how iterative methods reach one, and what structure —
convexity, smoothness, duality — buys you in guarantees.

It is written for a reader who wants to know **why** a convergence rate is what it is, not
only which optimizer to call. Every rate here is derived from an explicit smoothness or
curvature hypothesis, and every duality statement carries the constraint qualification it
needs.

Eight modules, 160 fully solved problems.

> [!NOTE]
> Every module now carries a few verification code cells — added to check the numeric results the
> audit flagged as wrong, plus each module's headline identity — but not yet the full six-cell /
> two-to-four-figure contract that [`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20-21 require. Run
> `python3 tools/curriculum_stats.py --modules` for the live counts. The legacy
> [`computation.ipynb`](computation.ipynb) at this folder's root also still runs.

---

## Prerequisites

[`../docs/prerequisites.md`](../docs/prerequisites.md) is the repository-wide dependency graph
and the source of truth for what any module may depend on.

This area draws on three others:

- [`../calculus/`](../calculus/) — Taylor's theorem with remainder (module 09), gradients and
  directional derivatives (11), the Hessian and curvature (12).
- [`../linear_algebra/`](../linear_algebra/) — linear maps (02), direct factorizations (03),
  the spectral theorem (06), the SVD (07).
- [`../probability_statistics/`](../probability_statistics/) — the law of large numbers and the
  CLT (module 08). Needed only by optimization module 08.

[`../calculus_optimization/`](../calculus_optimization/) is the gentler on-ramp and sits
immediately before this area in the study order.

---

## Module index

Problem counts are from `tools/curriculum_stats.py`, not from prose.

| Module | What it covers | Prerequisites | Problems |
|---|---|---|:---:|
| [01 — Problem Formulation & Convexity](01_problem_formulation_and_convexity/) | Standard form, feasible sets, local versus global minimizers, convex sets and functions, epigraphs, Jensen, the first- and second-order characterizations, strong convexity | [calculus/12](../calculus/12_hessian_jacobian_curvature/), [linear_algebra/06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/) | 20 |
| [02 — Unconstrained Optimality Conditions](02_unconstrained_optimality_conditions/) | FONC, SONC, SOSC, Hessian classification of stationary points, coercivity and Weierstrass existence, the complete quadratic case, stationarity as global optimality when convex | [calculus/09](../calculus/09_taylor_and_power_series/), [01](01_problem_formulation_and_convexity/) | 20 |
| [03 — Gradient Descent & Convergence](03_gradient_descent_and_convergence/) | Descent lemma, $L$-smoothness and $\mu$-strong convexity, the rates $O(1/\sqrt{k})$, $O(1/k)$ and $(1-\mu/L)^k$, the PL inequality, optimal step $2/(L+\mu)$, gradient flow, heavy-ball and Nesterov momentum | [calculus/11](../calculus/11_gradients_directional_derivatives/), [02](02_unconstrained_optimality_conditions/) | 20 |
| [04 — Line Search, Newton & Quasi-Newton](04_line_search_newton_quasi_newton/) | Armijo and Wolfe conditions, Zoutendijk's theorem, Newton's quadratic convergence and affine invariance, the BFGS secant equation and SPD preservation, the L-BFGS two-loop recursion | [linear_algebra/03](../linear_algebra/03_linear_systems_and_direct_factorizations/), [03](03_gradient_descent_and_convergence/) | 20 |
| [05 — Constrained Optimization & Lagrange Multipliers](05_constrained_optimization_lagrange/) | Tangent spaces and LICQ, the Lagrangian, first-order necessity, sensitivity $dp^{\star}/db = -\lambda^{\star}$, second-order sufficiency on the tangent space, maximum entropy, the Rayleigh quotient | [calculus/11](../calculus/11_gradients_directional_derivatives/), [linear_algebra/02](../linear_algebra/02_linear_maps_and_matrix_transformations/), [02](02_unconstrained_optimality_conditions/) | 20 |
| [06 — KKT Conditions & Duality](06_kkt_conditions_and_duality/) | Active sets, the KKT system, concavity of the dual function, weak duality, complementary slackness from a zero gap, Slater strong duality, the saddle-point characterization, the hard-margin SVM dual | [01](01_problem_formulation_and_convexity/), [05](05_constrained_optimization_lagrange/) | 20 |
| [07 — Linear, Quadratic & Conic Programs](07_linear_quadratic_conic_programs/) | Polyhedral geometry and basic feasible solutions, the fundamental theorem of LP, LP weak duality, the normal equations, the equality-constrained QP KKT system, the Schur complement lemma, the embedding chain LP $\subseteq$ QP $\subseteq$ SOCP $\subseteq$ SDP | [linear_algebra/07](../linear_algebra/07_canonical_forms_and_svd/), [06](06_kkt_conditions_and_duality/) | 20 |
| [08 — Stochastic Optimization for ML](08_stochastic_optimization_for_ml/) | Mini-batch unbiasedness and the $1/B$ variance law, Robbins–Monro schedules, the constant-step noise ball, the $O(1/k)$ decaying-step rate, SVRG control variates, momentum, AdaGrad and Adam with bias correction, SGD as Langevin diffusion | [probability_statistics/08](../probability_statistics/08_law_of_large_numbers_and_clt/), [03](03_gradient_descent_and_convergence/) | 20 |
| **Total** | **8 modules** | — | **160** |

Every module carries the same tier split: 4 concept checks, 6 foundations, 6 applications,
4 challenge problems.

### What is stated but not proved, and what is absent

Each line below was checked against the notebook it describes, not inherited from an earlier
index.

- **Module 03** states Nesterov acceleration and the matching $\Omega(1/k^2)$ lower bound as
  Theorem 7. Neither is proved; the notebook's six proofs run from the descent lemma to the
  PL inequality.
- **Module 06** proves KKT necessity only under strong duality, not under LICQ. Farkas' lemma
  is load-bearing in the exercises of modules 06 and 07 but is stated in no theory notebook in
  this area.
- **Module 07** forms no conic dual and defines no dual cone, despite *conic* in its title.
  Simplex and interior-point methods are surveyed in prose, not analysed.
- **Module 08** treats saddle escape as one applications remark on Kramers' escape rate plus
  exercise L3.4. The Robbins–Monro conditions are defined without the almost-sure convergence
  theorem they are named for.
- **Non-smooth optimization** — subgradients, the subgradient method, proximal operators,
  ISTA and FISTA — appears in none of the eight modules. Only the legacy
  [`first_principles.md`](first_principles.md) covers it.
- **Trust-region methods** appear in module 04 as a single clause. Nocedal & Wright give them
  a full chapter.

---

## Module architecture

Every numbered folder `NN_slug/` holds exactly the three files
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20 requires. All eight folders here do.

| File | Contract |
|---|---|
| `README.md` | Title, overview, a `> [!NOTE]` headline result, prerequisite and downstream links, learning outcomes, a Mermaid concept map, a notation table, a core-results table, common misconceptions, an exercise index matching the notebook, chapter-level references |
| `first_principles.ipynb` | Theory in the WHY → INTUITION → DEFINITION → DERIVATION → INTERPRETATION order, executable code cells verifying each major theorem, two to four figures showing the geometry of the central idea, worked numerical examples, a closing Key Takeaways cell |
| `exercises.ipynb` | Fully solved problems in four tiers, each carrying statement, intuition, full derivation, a `\boxed{...}` answer and a key takeaway |

The four tiers, with this area's verified counts:

| Tier | Meaning | Per module |
|---|---|:---:|
| **L0** | Concept checks | 4 |
| **L1** | Foundations | 6 |
| **L2** | AI/ML and physics applications | 6 |
| **L3** | Challenge proofs | 4 |

Two parts of that contract are not met here yet.

The sixteen module notebooks in this area do not yet contain code cells or figures, so no
theorem here is verified numerically and no geometry is drawn. Run `python3 tools/check_module.py --all --failing` for the modules that still fall short, and `python3 tools/curriculum_stats.py` for the live code-cell and figure counts.

The eight module READMEs carry six fixed headings rather than §20's ten items: they have no
prerequisites block, no learning outcomes, no notation table and no core-results table. Both
gaps are on the upgrade list.

What does hold today: all sixteen notebooks open with a Google Colab badge pointing at their
own file, and every module's stated tier counts match its notebook.

---

## Notation

[`../docs/notation.md`](../docs/notation.md) fixes symbols repository-wide. Its optimization
section governs this area.

Two conventions are worth repeating here, because getting either backwards flips signs
everywhere downstream.

**Every problem is a minimization.** Maximize $f$ by minimizing $-f$, and do the rewrite
*before* forming a Lagrangian, never after.

**Constraints enter the Lagrangian with a plus:**

$$
\mathcal{L}(x, \lambda, \mu) = f(x) + \lambda^\top h(x) + \mu^\top g(x), \qquad \mu \succeq 0
$$

so the sensitivity theorem reads $dp^{\star}/db = -\lambda^{\star}$.

This area deliberately diverges from Boyd & Vandenberghe on multiplier letters: here $\lambda$
carries equalities and $\mu \succeq 0$ carries inequalities, where Boyd writes $\lambda$ for
inequalities and $\nu$ for equalities. A reader holding Boyd open will otherwise read every
sign backwards.

Two sign defects are still in the tree and are recorded in the register: module 05 subtracts
the constraint term in Proofs 5 and 6 after defining the plus form, and its range-space KKT
formula carries a sign error.

---

## Suggested order

Read the modules in numerical order. Each one is a prerequisite of the next.

1. **01 → 02 → 03** is the spine: formulate the problem, certify what optimality means, then
   converge to it with rates you can prove.
2. **04** extends 03 with line searches and second-order methods. Nothing downstream in this
   area depends on it, so it can be deferred.
3. **05 → 06 → 07** is the constrained track. Module 05 needs only 02, so a reader who came
   for duality can jump there straight after 02.
4. **08** needs 03 and the CLT from
   [`../probability_statistics/08`](../probability_statistics/08_law_of_large_numbers_and_clt/).
   It is the bridge from this theory to deep-learning practice.

---

## Companion resources

Two files predate the numbered curriculum and still sit at this folder's root. They are not
part of the three-file module contract and are **not** counted in the 160 problems.

| File | What it actually is |
|---|---|
| [`first_principles.md`](first_principles.md) | A single-file survey in nine sections, from problem formulation through ML applications. Sections 1–5 and 8–9 are superseded by modules 01–08. Sections 6 and 7 are not: subgradients and subdifferentials, the subgradient method, proximal operators and proximal gradient descent, mixed-integer programming and derivative-free search appear nowhere in the numbered modules. |
| [`computation.ipynb`](computation.ipynb) | The only executable notebook in this area: 27 cells, 16 of them code, with stored outputs and 8 figures. Golden-section search, gradient descent and Newton on Rosenbrock, Armijo backtracking, a convexity plot, worked Lagrange and KKT examples, a two-dimensional LP feasible region, and a `scipy.optimize` cross-check. Imports only `numpy`, `scipy` and `matplotlib`. |

Neither file is maintained against the current style guide, and whether to keep them is the
repository owner's decision, not this index's.

Sibling area: [`../calculus_optimization/`](../calculus_optimization/) — four modules and 80
problems bridging differential calculus to the theory developed here.

---

## References

The benchmark texts for this area, per [`../CLAUDE.md`](../CLAUDE.md), with the chapters the
modules actually draw on. Each module `README.md` carries its own full citation list.

**Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.

- Chapters 2–3 — convex sets and convex functions (module 01)
- §4.2.3 and Chapter 9 — unconstrained minimization, backtracking, Newton, self-concordance (modules 02–04)
- Chapter 5 — duality, Slater's condition, KKT, sensitivity (modules 05–06)
- Chapter 4 and Appendix A.5.5 — LP/QP/SOCP/SDP forms, Schur complements (module 07)

**Nocedal, J., & Wright, S. J.** (2006). *Numerical Optimization* (2nd ed.). Springer.

- Chapter 2 — Taylor's theorem, FONC, SONC, SOSC (module 02)
- Chapter 3 — line search and Zoutendijk; Chapters 6–7 — quasi-Newton and L-BFGS (module 04)
- Chapter 12 — constraint qualifications and KKT (modules 05–06)
- Chapters 13–14, 16 — simplex, interior point, quadratic programming (module 07)
- Chapter 4 (trust regions) and Chapter 17 (penalty, augmented Lagrangian) are cited but not developed

**Bertsekas, D. P.** *Nonlinear Programming* (3rd ed., 2016) and *Convex Optimization Theory*
(2009). Athena Scientific.

- NLP Chapter 1 — gradient methods, existence of minimizers (modules 02–03)
- NLP Chapters 3–5 — Lagrange multiplier theory, duality, saddle points (modules 05–06)
- COT Chapters 4–5 — min-common/max-crossing duality, cited in module 06 but not used

**Further sources cited across the area.**

- **Nesterov, Y.** (2018). *Lectures on Convex Optimization* (2nd ed.). Springer. Chapter 2 — smooth convex rates, estimating sequences, the $\Omega(1/k^2)$ lower bound (module 03).
- **Rockafellar, R. T.** (1970). *Convex Analysis*. Princeton University Press. Parts I–II — epigraphs and convex functions; Parts VI–VII — saddle functions and minimax.
- **Luenberger, D. G., & Ye, Y.** (2016). *Linear and Nonlinear Programming* (4th ed.). Springer. Chapter 7 — convex programming; Chapter 11 — constrained conditions and bordered Hessians; Chapters 2–5 — simplex, duality, interior point.
- **Ben-Tal, A., & Nemirovski, A.** (2001). *Lectures on Modern Convex Optimization*. SIAM. Lectures 2–4 — conic duality and the expressive power of SOCP and SDP, cited by module 07 but not yet developed there.
- **Dantzig, G. B.** (1963). *Linear Programming and Extensions*. Princeton University Press. Chapters 5–7 — the simplex method, degeneracy, LP duality (module 07).
- **Polyak, B. T.** (1987). *Introduction to Optimization*. Optimization Software. Chapter 3 — heavy-ball momentum and the PL inequality (modules 03–04).
- **Bottou, L., Curtis, F. E., & Nocedal, J.** (2018). Optimization Methods for Large-Scale Machine Learning. *SIAM Review* 60(2), 223–311. §4–5 — SGD analysis, the noise ball, variance reduction (module 08).
- **Robbins, H., & Monro, S.** (1951). A Stochastic Approximation Method. *Annals of Mathematical Statistics* 22(3), 400–407 (module 08).
- **Johnson, R., & Zhang, T.** (2013). Accelerating Stochastic Gradient Descent using Predictive Variance Reduction. *NeurIPS*. The SVRG estimator (module 08).
- **Kingma, D. P., & Ba, J.** (2015). Adam: A Method for Stochastic Optimization. *ICLR*. §2–3 — the update rule and bias correction (module 08).
- **Cortes, C., & Vapnik, V.** (1995). Support-Vector Networks. *Machine Learning* 20, 273–297. The SVM dual (module 06).
- **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press. Chapter 8 — optimization for training deep models (module 08).
