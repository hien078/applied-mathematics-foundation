# Numerical Methods — Algorithms for Approximate Computation

Welcome to the **Numerical Methods** foundation under `numerical_methods/`.

Most mathematical models admit no closed-form solution. Numerical methods supply systematic algorithms that **approximate** the answers — roots, derivatives, integrals, fits, and trajectories — on a finite-precision machine, together with the theory that says *why* each algorithm works, *when* it fails, and *how fast* it converges. This module builds that theory from first principles, from the bit-level behaviour of IEEE 754 arithmetic to the ODE solvers inside Neural ODEs and diffusion-model samplers, with a consistent emphasis on error analysis, conditioning, stability, and convergence order.

---

## 🗺️ Master Index of 8 Numerical Methods Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Error Analysis & Floating Point | [`01_error_analysis_and_floating_point/`](01_error_analysis_and_floating_point/) | IEEE 754, machine epsilon, absolute/relative error, cancellation, conditioning vs stability, backward error | 16 |
| **Topic 02** | Root-Finding Methods | [`02_root_finding_methods/`](02_root_finding_methods/) | Bisection and the IVT, Newton's quadratic rate, secant order $\varphi$, multiple roots, Brent hybridization | 16 |
| **Topic 03** | Fixed-Point Iteration & Convergence | [`03_fixed_point_iteration_and_convergence/`](03_fixed_point_iteration_and_convergence/) | Contraction mapping theorem, Banach fixed point, convergence order, Aitken and Steffensen acceleration | 16 |
| **Topic 04** | Polynomial & Spline Interpolation | [`04_polynomial_and_spline_interpolation/`](04_polynomial_and_spline_interpolation/) | Lagrange and Newton forms, divided differences, Runge phenomenon, Chebyshev nodes, cubic splines, Bézier curves | 16 |
| **Topic 05** | Numerical Differentiation | [`05_numerical_differentiation/`](05_numerical_differentiation/) | Forward/central differences, Richardson extrapolation, truncation vs round-off trade-off, complex-step and automatic differentiation | 16 |
| **Topic 06** | Numerical Integration (Quadrature) | [`06_numerical_integration_quadrature/`](06_numerical_integration_quadrature/) | Newton–Cotes, Simpson, Romberg, Gauss–Legendre, adaptive quadrature, Monte Carlo and high-dimensional integrals | 16 |
| **Topic 07** | Linear Least Squares | [`07_linear_least_squares/`](07_linear_least_squares/) | Normal equations and orthogonal projection, $\kappa_2(A^{\top}A) = \kappa_2(A)^2$, Householder/Givens/Gram–Schmidt QR, SVD and pseudoinverse, ridge and truncated SVD | 16 |
| **Topic 08** | Numerical ODE Solvers | [`08_numerical_ode_solvers/`](08_numerical_ode_solvers/) | Euler and Runge–Kutta, Butcher tableaux, Dahlquist equivalence, absolute stability and stiffness, adaptive and symplectic integrators, Neural ODEs | 16 |
| **TOTAL** | **8 Numerical Methods Modules** | — | **Complete First-Principles Curriculum** | **128 Problems** |

---

## 📐 Standard Module Architecture

Every numbered module folder (`01_...` through `08_...`) follows the same three-file architecture:

1. **`README.md`** — Master overview, first-principles framework, a Mermaid concept map, a common-misconceptions table, a directory inventory, and recommended literature references.
2. **`first_principles.ipynb`** — A markdown-only notebook developing the theory: first-principles intuition and motivation, rigorous definitions and theorem statements, four to six complete step-by-step proofs, computational and algorithmic insights, real-world physics and AI/ML applications, and a canonical literature mapping.
3. **`exercises.ipynb`** — **16 fully solved problems** across four levels: **L0** concept checks, **L1** foundations, **L2** AI/ML and physics applications, and **L3** challenge proofs. Every problem carries a complete derivation, a boxed final answer `$$\boxed{...}$$`, and a key-takeaway line.

Every notebook opens with an **Open In Colab** badge, so any topic can be read or run directly in the browser.

---

## 📎 Companion Resources

| File | Description |
|---|---|
| [first_principles.md](first_principles.md) | Legacy single-file overview: floating point, root finding, interpolation, quadrature, least squares. |
| [computation.ipynb](computation.ipynb) | Legacy computational notebook: algorithm implementations, convergence plots, error analysis. |

**Prerequisites.** [`../calculus/`](../calculus/) supplies Taylor series, the mean value theorem, and the ODE background; [`../linear_algebra/`](../linear_algebra/) supplies orthogonality, the SVD, matrix norms, and eigenvalues — both are assumed throughout Topics 04–08.

**Closest neighbour.** [`../numerical_computing/`](../numerical_computing/) is the *practice* of reliable fast computing — floating-point representation, error propagation tricks, and condition numbers at the level of the machine — where this module is the *theory* of the algorithms that run on it. Read the two together: Topic 01 here and the numerical-computing modules cover the same ground from complementary directions.

**Downstream.** [`../optimization/`](../optimization/) builds on Topics 02, 03, 05 and 07 (Newton, line search, least squares); [`../differential_equations/`](../differential_equations/) supplies the analytical ODE theory that Topic 08 discretizes; and [`../probability_statistics/`](../probability_statistics/) and [`../information_theory/`](../information_theory/) use least squares, quadrature, and Monte Carlo estimation throughout.

---

## 🎯 Learning Objectives

After working through this material, you should be able to:

1. **Explain** how IEEE 754 floating-point arithmetic introduces rounding error, and distinguish *conditioning* (a property of the problem) from *stability* (a property of the algorithm).
2. **Implement and compare** root-finding algorithms — bisection, Newton, secant, fixed-point iteration, Brent — and state their convergence orders and failure modes.
3. **Construct** polynomial and spline interpolants (Lagrange, Newton, cubic splines), and explain the Runge phenomenon and why Chebyshev nodes cure it.
4. **Approximate** derivatives and definite integrals with difference formulas and quadrature rules (trapezoidal, Simpson, Romberg, Gauss–Legendre, adaptive, Monte Carlo), and choose the step size that balances truncation against round-off.
5. **Solve** least-squares problems via the normal equations, QR factorization, and the SVD, and explain why forming $A^{\top}A$ squares the condition number.
6. **Integrate** initial value problems with explicit and implicit methods, analyse local and global truncation error, and select a solver based on stiffness, adaptivity, and structure preservation.
7. **Analyse** convergence rates and error behaviour rigorously, and **choose** an appropriate numerical method for a given modeling or machine-learning task.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites the canonical literature:

- **Burden, R. L., & Faires, J. D.** — *Numerical Analysis*
- **Sauer, T.** — *Numerical Analysis*
- **Heath, M. T.** — *Scientific Computing: An Introductory Survey*
- **Trefethen, L. N., & Bau, D.** — *Numerical Linear Algebra*
- **Golub, G. H., & Van Loan, C. F.** — *Matrix Computations*
- **Björck, Å.** — *Numerical Methods for Least Squares Problems*
- **Higham, N. J.** — *Accuracy and Stability of Numerical Algorithms*
- **Hansen, P. C.** — *Rank-Deficient and Discrete Ill-Posed Problems*
- **Hairer, E., Nørsett, S. P., & Wanner, G.** — *Solving Ordinary Differential Equations I & II*
- **Hairer, E., Lubich, C., & Wanner, G.** — *Geometric Numerical Integration*
- **Butcher, J. C.** — *Numerical Methods for Ordinary Differential Equations*
- **Iserles, A.** — *A First Course in the Numerical Analysis of Differential Equations*
- **LeVeque, R. J.** — *Finite Difference Methods for Ordinary and Partial Differential Equations*
- **Quarteroni, A., Sacco, R., & Saleri, F.** — *Numerical Mathematics*
- **Press, W. H., et al.** — *Numerical Recipes*
- **Goldberg, D.** — *What Every Computer Scientist Should Know About Floating-Point Arithmetic*
- **Chen, R. T. Q., et al.** — *Neural Ordinary Differential Equations* (NeurIPS 2018)
