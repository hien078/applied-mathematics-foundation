# Foundations of Optimization — Optimization Mastery Curriculum

Welcome to the **Optimization Mastery Curriculum** under `foundations/optimization/`.

This module provides a comprehensive, first-principles learning system spanning problem formulation, convex analysis, unconstrained and constrained optimality theory, iterative algorithms (gradient descent, Newton, quasi-Newton), Lagrangian duality and KKT theory, the convex programming hierarchy (LP, QP, SOCP, SDP), and stochastic optimization for large-scale machine learning. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

---

## Master Index of 8 Optimization Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Problem Formulation & Convexity | [`01_problem_formulation_and_convexity/`](01_problem_formulation_and_convexity/) | Standard form, feasible sets, local vs global optima, convex sets/functions, Jensen's inequality, epigraphs | 20 |
| **Topic 02** | Unconstrained Optimality Conditions | [`02_unconstrained_optimality_conditions/`](02_unconstrained_optimality_conditions/) | FONC/SONC/SOSC, Hessian eigenvalue classification, coercivity, Weierstrass existence, quadratic objectives | 20 |
| **Topic 03** | Gradient Descent & Convergence | [`03_gradient_descent_and_convergence/`](03_gradient_descent_and_convergence/) | Descent lemma, $L$-smoothness, $\mu$-strong convexity, rates $O(1/k)$ and $(1-\mu/L)^k$, condition number, momentum, Nesterov acceleration | 20 |
| **Topic 04** | Line Search, Newton & Quasi-Newton | [`04_line_search_newton_quasi_newton/`](04_line_search_newton_quasi_newton/) | Armijo/Wolfe conditions, Zoutendijk global convergence, Newton quadratic convergence, BFGS secant updates, L-BFGS | 20 |
| **Topic 05** | Constrained Optimization & Lagrange Multipliers | [`05_constrained_optimization_lagrange/`](05_constrained_optimization_lagrange/) | Lagrangian $\mathcal{L}(\mathbf{x},\boldsymbol{\lambda})$, tangent spaces, LICQ, sensitivity $\partial f^{\ast}/\partial b=-\lambda^{\ast}$, maximum entropy, Rayleigh quotient | 20 |
| **Topic 06** | KKT Conditions & Duality | [`06_kkt_conditions_and_duality/`](06_kkt_conditions_and_duality/) | KKT system, complementary slackness, weak/strong duality, Slater's condition, saddle points, SVM dual | 20 |
| **Topic 07** | Linear, Quadratic & Conic Programs | [`07_linear_quadratic_conic_programs/`](07_linear_quadratic_conic_programs/) | Polyhedral geometry, fundamental theorem of LP, simplex vs interior-point, normal equations, Markowitz QP, SOCP/SDP hierarchy | 20 |
| **Topic 08** | Stochastic Optimization for ML | [`08_stochastic_optimization_for_ml/`](08_stochastic_optimization_for_ml/) | Mini-batch estimators, Robbins-Monro schedules, SGD noise-ball analysis, variance reduction (SVRG), AdaGrad/Adam, saddle escape | 20 |
| **TOTAL** | **8 Optimization Modules** | — | **Complete First-Principles Curriculum** | **160 Problems** |

---

## Standard Module Architecture

Every module folder (`01_...` through `08_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., descent lemma, Newton quadratic convergence, weak/strong duality), Computational and Algorithmic Insights, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`first_principles.md`](first_principles.md) | Legacy master theory file: formulation, unconstrained/constrained optimization, convex hierarchy, duality, non-smooth and global optimization — the seed document the 8 modules expand upon |
| [`computation.ipynb`](computation.ipynb) | Executable companion notebook: golden section search, gradient descent and Newton on Rosenbrock, Armijo backtracking, convexity visualization, Lagrange/KKT worked examples, `scipy.optimize` validation |
| [`../calculus_optimization/`](../calculus_optimization/) | Sibling bridge module connecting differential calculus to optimization: derivative-based optimality, curvature, and 1D methods that motivate the multivariable theory developed here |

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy `computation.ipynb` to see the algorithms executing numerically.

---

## Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Boyd, S., & Vandenberghe, L.** — *Convex Optimization* (Cambridge University Press)
- **Nocedal, J., & Wright, S. J.** — *Numerical Optimization* (Springer)
- **Bertsekas, D. P.** — *Nonlinear Programming* & *Convex Optimization Theory* (Athena Scientific)
- **Nesterov, Y.** — *Lectures on Convex Optimization* (Springer)
- **Rockafellar, R. T.** — *Convex Analysis* (Princeton University Press)
- **Luenberger, D. G., & Ye, Y.** — *Linear and Nonlinear Programming* (Springer)
- **Ben-Tal, A., & Nemirovski, A.** — *Lectures on Modern Convex Optimization* (SIAM)
- **Dantzig, G. B.** — *Linear Programming and Extensions* (Princeton University Press)
- **Polyak, B. T.** — *Introduction to Optimization* (Optimization Software)
- **Bottou, L., Curtis, F. E., & Nocedal, J.** — *Optimization Methods for Large-Scale Machine Learning* (SIAM Review, 2018)
- **Robbins, H., & Monro, S.** — *A Stochastic Approximation Method* (Annals of Mathematical Statistics, 1951)
- **Kingma, D. P., & Ba, J.** — *Adam: A Method for Stochastic Optimization* (ICLR, 2015)
- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*, Chapter 8 (MIT Press)
