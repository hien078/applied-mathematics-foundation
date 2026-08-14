# Foundations of Differential Equations — ODE Mastery Curriculum

Welcome to the **Differential Equations Mastery Curriculum** under `foundations/differential_equations/`.

This module provides a comprehensive, first-principles learning system for ordinary differential equations — the mathematical language of continuous change. It spans classification and analytic solution techniques, rigorous existence-uniqueness theory, linear structure and matrix exponentials, qualitative phase-plane dynamics, operational transform methods, boundary value problems, and the deep connections between ODEs and modern machine learning (Neural ODEs, diffusion models, optimization dynamics). Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

> **Prerequisites:** [Calculus](../calculus/) (especially [Topic 15: Ordinary Differential Equations](../calculus/15_ordinary_differential_equations/), the survey-level companion of this curriculum) and [Linear Algebra](../linear_algebra/) (especially [Topic 06: Eigenvalues, Eigenvectors, and Spectral Theory](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/)).

---

## 🗺️ Master Index of 8 Differential Equations Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Classification & First-Order ODEs | [`01_classification_and_first_order_odes/`](01_classification_and_first_order_odes/) | Order/linearity/autonomy taxonomy, separable equations, integrating factor $\mu(t)=e^{\int p}$, exact equations, Bernoulli & Riccati substitutions | 20 |
| **Topic 02** | Existence, Uniqueness & Picard–Lindelöf | [`02_existence_uniqueness_picard_lindelof/`](02_existence_uniqueness_picard_lindelof/) | Lipschitz conditions, Banach fixed point, Picard iteration convergence, Grönwall's inequality, blow-up & non-uniqueness | 20 |
| **Topic 03** | Second-Order Linear ODEs | [`03_second_order_linear_odes/`](03_second_order_linear_odes/) | Solution vector spaces, Wronskian & Abel's theorem, characteristic equations, variation of parameters, damped/forced oscillators & resonance | 20 |
| **Topic 04** | Systems of ODEs & the Matrix Exponential | [`04_systems_of_odes_matrix_exponential/`](04_systems_of_odes_matrix_exponential/) | Companion-matrix reduction, $e^{At}$ series and properties, diagonalization/Jordan/Putzer computation, Duhamel variation of constants | 20 |
| **Topic 05** | Phase Plane & Stability Analysis | [`05_phase_plane_and_stability_analysis/`](05_phase_plane_and_stability_analysis/) | Trace-determinant classification, Hartman–Grobman linearization, Lyapunov direct method, limit cycles, Lotka–Volterra first integrals | 20 |
| **Topic 06** | Laplace Transform Methods | [`06_laplace_transform_methods/`](06_laplace_transform_methods/) | Operational calculus, derivative & convolution theorems, unit step & Dirac delta forcing, transfer functions, pole-based stability | 20 |
| **Topic 07** | Boundary Value Problems & PDE Preview | [`07_boundary_value_problems_and_pde_preview/`](07_boundary_value_problems_and_pde_preview/) | Sturm–Liouville eigenproblems, orthogonal eigenfunctions, Green's functions, separation of variables for the heat equation | 20 |
| **Topic 08** | ODEs in Machine Learning | [`08_odes_in_machine_learning/`](08_odes_in_machine_learning/) | Gradient flow & momentum ODEs, ResNets as Euler steps, Neural ODE adjoint method, continuous normalizing flows, probability flow ODEs | 20 |
| **TOTAL** | **8 Differential Equations Modules** | — | **Complete First-Principles Curriculum** | **160 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `08_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, and canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition & Motivation, Rigorous Definitions & Theorem Statements, Step-by-Step Proofs & Derivations (integrating factors, Picard iteration, Abel's identity, $e^{At}$ properties, Lyapunov theorems, adjoint sensitivity, and more), Computational & Algorithmic Insights, Real-World Physics & AI/ML Applications, and Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

All notebooks open directly in Google Colab via the badge in their first cell.

---

## 🔗 Companion Resources

The original single-file foundation materials remain available and are fully compatible with the new curriculum:

| Resource | Description |
|---|---|
| [`first_principles.md`](first_principles.md) | Legacy single-document theory: classification, first/second-order solution methods, systems, qualitative analysis, and numerical methods (Euler, Heun, RK4, stiffness) in one linear read. |
| [`computation.ipynb`](computation.ipynb) | Executable computational companion: `solve_ivp` workflows, Euler vs RK4 convergence experiments, phase portraits, Lotka–Volterra simulation, and stability visualization. |
| [`../calculus/15_ordinary_differential_equations/`](../calculus/15_ordinary_differential_equations/) | Survey-level ODE module inside the calculus curriculum — a compact single-module tour of the same landscape. The 8 modules here go deeper on each topic and add Laplace transforms, BVPs, and a dedicated ML capstone. |

**Suggested path:** skim the legacy `first_principles.md` for the panoramic view, then work Modules 01–08 in order; run `computation.ipynb` alongside Modules 01, 04, and 05 for numerical intuition.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Arnold, V. I.** — *Ordinary Differential Equations* (geometric phase flows and vector fields)
- **Boyce, W. E., & DiPrima, R. C.** — *Elementary Differential Equations and Boundary Value Problems* (canonical solution techniques and BVPs)
- **Hirsch, M. W., Smale, S., & Devaney, R. L.** — *Differential Equations, Dynamical Systems, and an Introduction to Chaos*
- **Strogatz, S. H.** — *Nonlinear Dynamics and Chaos* (phase planes, stability, bifurcations)
- **Tenenbaum, M., & Pollard, H.** — *Ordinary Differential Equations* (problem-driven classical techniques)
- **Coddington, E. A., & Levinson, N.** — *Theory of Ordinary Differential Equations* (rigorous existence-uniqueness theory)
- **Perko, L.** — *Differential Equations and Dynamical Systems*
- **Schiff, J. L.** — *The Laplace Transform: Theory and Applications*
- **Evans, L. C.** — *Partial Differential Equations* (PDE preview foundations)
- **Chen, R. T. Q., Rubanova, Y., Bettencourt, J., & Duvenaud, D.** (2018) — *Neural Ordinary Differential Equations*, NeurIPS
- **Su, W., Boyd, S., & Candès, E. J.** (2016) — *A Differential Equation for Modeling Nesterov's Accelerated Gradient Method*, JMLR
- **Song, Y., et al.** (2021) — *Score-Based Generative Modeling through Stochastic Differential Equations*, ICLR
- **Premier Competitions**: William Lowell Putnam Mathematical Competition, Cambridge Mathematical Tripos Part IA/IB Differential Equations.
