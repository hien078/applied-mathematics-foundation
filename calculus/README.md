# Foundations of Calculus — Calculus Mastery Curriculum

Welcome to the **Calculus Mastery Curriculum** under `foundations/calculus/`. 

This repository branch provides a comprehensive, first-principles learning system spanning single-variable calculus, multivariable analysis, vector fields, and ordinary differential equations. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

---

## 🗺️ Master Index of 15 Calculus Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Functions, Mappings & Properties | [`01_functions_and_properties/`](01_functions_and_properties/) | Set-theoretic mappings, domain/range, monotonicity, parity, periodicity, inverse functions | 40 |
| **Topic 02** | Limits ($\varepsilon$-$\delta$), Continuity & Asymptotics | [`02_limits_and_continuity/`](02_limits_and_continuity/) | $\varepsilon$-$\delta$ proofs, Squeeze theorem, IVT/EVT, Softmax limits, Big-O asymptotics | 40 |
| **Topic 03** | Single-Variable Derivatives & Rules | [`03_single_variable_derivatives/`](03_single_variable_derivatives/) | Secant limits, Carathéodory chain rule, Leibniz rule, Dual Numbers AutoDiff | 40 |
| **Topic 04** | Derivative Applications & 1D Optimization | [`04_derivative_applications_optimization/`](04_derivative_applications_optimization/) | Fermat, Rolle, MVT, Cauchy MVT, L'Hôpital's rule, Newton's method quadratic rate | 40 |
| **Topic 05** | Indefinite & Definite Riemann Integrals | [`05_indefinite_and_definite_integrals/`](05_indefinite_and_definite_integrals/) | Darboux sums, FTC I & II, Leibniz rule, substitution, IBP, Weierstrass sub | 40 |
| **Topic 06** | Integral Applications: Geometry & Physics | [`06_integral_applications_geometry_physics/`](06_integral_applications_geometry_physics/) | Disk/Shell volumes, arc length, surface area, Pappus theorems, hydrostatics, PDFs | 40 |
| **Topic 07** | Improper Integrals & Special Functions | [`07_improper_integrals_special_functions/`](07_improper_integrals_special_functions/) | Type I/II improper integrals, $p$-tests, Gamma $\Gamma(x)$, Beta $B(x,y)$, Feynman trick | 40 |
| **Topic 08** | Sequences, Infinite Series & Convergence | [`08_sequences_series_convergence/`](08_sequences_series_convergence/) | Monotone convergence, ratio/root/Leibniz tests, Raabe's test, Kahan summation | 40 |
| **Topic 09** | Taylor, Maclaurin & Power Series | [`09_taylor_and_power_series/`](09_taylor_and_power_series/) | Integral/Lagrange/Cauchy remainders, Cauchy-Hadamard radius, Euler's formula | 40 |
| **Topic 10** | Multivariable Functions & Partials | [`10_multivariable_functions_partials/`](10_multivariable_functions_partials/) | Multivariable limits, Fréchet vs Gâteaux differentiability, Clairaut's theorem | 40 |
| **Topic 11** | Gradients, Directional Derivatives & Contours | [`11_gradients_directional_derivatives/`](11_gradients_directional_derivatives/) | Master formula $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$, level set orthogonality, Gradient Flow | 40 |
| **Topic 12** | Hessian, Jacobian & Multivariable Curvature | [`12_hessian_jacobian_curvature/`](12_hessian_jacobian_curvature/) | 2nd derivative test, Rayleigh quotient, Jacobian volume $\lvert\det J\rvert$, Softmax Hessian | 40 |
| **Topic 13** | Multiple Integrals & Coordinate Transformations | [`13_multiple_integrals_coordinate_transforms/`](13_multiple_integrals_coordinate_transforms/) | Fubini, Jacobians polar/spherical, 2D/$n$-D Gaussians, $n$-sphere volume $V_n(R)$ | 40 |
| **Topic 14** | Vector Calculus & Field Theorems | [`14_vector_calculus_field_theorems/`](14_vector_calculus_field_theorems/) | Line/surface integrals, Green, Stokes, Gauss Divergence, Helmholtz-Hodge | 40 |
| **Topic 15** | Ordinary Differential Equations (ODEs) | [`15_ordinary_differential_equations/`](15_ordinary_differential_equations/) | Picard-Lindelöf, matrix exponential $e^{At}$, phase space stability, Neural ODEs | 40 |
| **TOTAL** | **15 Calculus Modules** | — | **Complete First-Principles Curriculum** | **600 Problems** |

---

## 📚 Standard Module Architecture

Every single module folder (`01_...` through `15_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Index, First-Principles Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Recommended Literature References.
2. **`first_principles.md`**: First-Principles Intuition, Formal Mathematical Definitions, Step-by-Step Rigorous Proofs, Computational/Algorithmic Insights, Real-World Physics & AI/ML Applications.
3. **`exercises.md`**: **40 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Real-World/AI Applications $\to$ L3 Challenge/Olympiad/Putnam/Tripos) featuring explicit source attributions, intuition, complete KaTeX proofs, boxed final answers `$$\boxed{...}$$`, and key takeaways.

---

## 🎨 Visual Demos Notebook

[`visual_demos.ipynb`](visual_demos.ipynb) — Interactive Jupyter notebook with **matplotlib visualizations** complementing the theoretical modules:

| Demo | Related Modules | What You See |
|------|----------------|-------------|
| Numerical vs. Analytical Differentiation | Topics 03–04 | Forward/central difference convergence, roundoff error limits |
| Function & Derivative Plotting | Topics 03–04 | Critical points, concavity, exponential growth/decay curves |
| Numerical Integration | Topic 05 | Trapezoidal vs. Simpson's rule accuracy comparison |
| Taylor Series Approximation | Topic 09 | Animated polynomial approximations approaching $e^x$, $\sin x$ |
| 2D Gradient Visualization | Topic 11 | Contour plots, gradient vectors, gradient descent trajectories on quadratic & saddle surfaces |

> **Usage:** Read the theory in each module's `first_principles.md`, then open `visual_demos.ipynb` for interactive visual intuition.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:
- **Spivak, M.** — *Calculus* & *Calculus on Manifolds*
- **Apostol, T. M.** — *Calculus, Volumes I & II*
- **Stewart, J.** — *Calculus: Early Transcendentals*
- **Marsden, J. E., & Tromba, A. J.** — *Vector Calculus*
- **Demidovich, B. P.** — *Problems in Mathematical Analysis*
- **Pólya, G., & Szegő, G.** — *Problems and Theorems in Analysis*
- **Kaczor, W. J., & Nowak, M. T.** — *Problems in Real Analysis*
- **Boyd, S., & Vandenberghe, L.** — *Convex Optimization*
- **Nocedal, J., & Wright, S. J.** — *Numerical Optimization*
- **Arnold, V. I.** — *Ordinary Differential Equations*
- **Strogatz, S. H.** — *Nonlinear Dynamics and Chaos*
- **Boyce, W. E., & DiPrima, R. C.** — *Elementary Differential Equations*
- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*
- **Premier Competitions**: William Lowell Putnam Mathematical Competition, Cambridge Mathematical Tripos, IMO Shortlist, MIT Integration Bee.
