# Numerical Methods

**Status:** Active  
**Purpose:** Foundation for computational problem-solving in mathematical modeling  
**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

## Overview

Most mathematical models do not have closed-form solutions. Numerical methods provide
systematic algorithms to **approximate** solutions to equations, integrals, and
optimization problems on a computer.

This foundation covers the core numerical techniques needed throughout the modeling
topics: root finding, interpolation, numerical integration, and least squares fitting.
The emphasis is on understanding **why** each method works, **when** it fails, and
**how fast** it converges.

## Learning Objectives

After working through this material, you should be able to:

1. **Explain** how floating-point arithmetic introduces rounding errors
2. **Implement and compare** root-finding algorithms (bisection, Newton, secant)
3. **Construct** polynomial interpolants (Lagrange, Newton, spline)
4. **Approximate** definite integrals using quadrature rules (trapezoidal, Simpson, Gauss)
5. **Solve** least-squares problems via normal equations and QR factorization
6. **Analyze** convergence rates and error behavior of numerical algorithms
7. **Choose** appropriate numerical methods for modeling tasks

## Contents

| File | Description |
|------|-------------|
| [first_principles.md](first_principles.md) | Core theory: floating point, root finding, interpolation, quadrature, least squares |
| [computation.ipynb](computation.ipynb) | Computational examples: algorithm implementations, convergence plots, error analysis |

## Dependent Topics

The following modeling topics build directly on this foundation:

- **04 — Model Fitting:** Parameter estimation requires least squares, root finding,
  and numerical optimization
- **14 — Data-Driven Modeling:** Interpolation, regression, and numerical methods
  underpin data-driven approaches

## Key References

- Burden, R. L. & Faires, J. D. *Numerical Analysis*. Cengage Learning.
- Sauer, T. *Numerical Analysis*. Pearson.
- Trefethen, L. N. & Bau, D. *Numerical Linear Algebra*. SIAM.
