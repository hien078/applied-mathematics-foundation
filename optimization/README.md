# Optimization

**Status:** Active  
**Purpose:** Foundation for optimization theory and algorithms in mathematical modeling  
**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

## Overview

Optimization is the mathematical framework for finding the **best** element from a set
of alternatives. In modeling, we optimize to fit parameters, allocate resources, design
systems, and train machine learning models.

This foundation covers the essential theory from unconstrained and constrained
optimization, with emphasis on the geometric and analytic ideas that connect to
modeling applications.

## Learning Objectives

After working through this material, you should be able to:

1. **Formulate** optimization problems: objective, constraints, feasible region
2. **State and apply** necessary and sufficient conditions for unconstrained optima
3. **Implement** gradient descent and understand its convergence behavior
4. **Identify** convex problems and explain why convexity guarantees global optimality
5. **Use** Lagrange multipliers and KKT conditions for constrained problems
6. **Set up** linear programs and understand feasible region geometry
7. **Connect** optimization to parameter estimation, resource allocation, and ML training

## Contents

| File | Description |
|------|-------------|
| [first_principles.md](first_principles.md) | Core theory: formulation, unconstrained/constrained optimization, convexity, LP |
| [computation.ipynb](computation.ipynb) | Computational examples: gradient descent, scipy.optimize, linear programming |

## Dependent Topics

The following modeling topics build directly on this foundation:

- **10 — Optimization Models:** Resource allocation, scheduling, and design problems
  formulated as mathematical programs
- **11 — Constrained Optimization & Lagrange Multipliers:** Comprehensive curriculum module, KKT theory, duality, SVM duals, MaxEnt, and 4-level exercise package

## Key References

- Boyd, S. & Vandenberghe, L. *Convex Optimization*. Cambridge University Press.
- Nocedal, J. & Wright, S. J. *Numerical Optimization*. Springer.
- Luenberger, D. G. & Ye, Y. *Linear and Nonlinear Programming*. Springer.
