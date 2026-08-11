# Differential Equations

**Status:** Active  
**Purpose:** Foundation for continuous-time mathematical modeling  
**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

## Overview

Differential equations are the language of continuous change. Any phenomenon where a
quantity evolves continuously in time or space — population growth, heat flow, mechanical
vibration, chemical reaction, neural dynamics — is naturally described by a differential
equation.

This foundation covers the essential theory needed for the modeling topics in this
repository, focusing on **ordinary differential equations (ODEs)** and their qualitative
analysis.

## Learning Objectives

After working through this material, you should be able to:

1. **Classify** differential equations by order, linearity, and type (ODE vs PDE)
2. **Solve** standard first-order ODEs (separable, linear with integrating factors)
3. **Solve** second-order linear ODEs using characteristic equations
4. **Analyze** systems of ODEs using matrix methods and eigenvalues
5. **Sketch** phase portraits and determine stability of equilibria
6. **Apply** numerical methods (Euler, RK4) to solve ODEs computationally
7. **Connect** differential equation models to real-world phenomena

## Contents

| File | Description |
|------|-------------|
| [first_principles.md](first_principles.md) | Core theory: classification, solution methods, systems, qualitative analysis |
| [computation.ipynb](computation.ipynb) | Computational examples: `solve_ivp`, phase portraits, numerical methods |

## Dependent Topics

The following modeling topics build directly on this foundation:

- **06 — Continuous Models:** Exponential growth, logistic equation, and other
  continuous-time population/process models formulated as ODEs
- **07 — Dynamical Systems:** Phase plane analysis, bifurcations, and long-term
  behavior of ODE systems (Lotka-Volterra, SIR, etc.)

## Key References

- Boyce, W. E. & DiPrima, R. C. *Elementary Differential Equations and Boundary Value Problems*. Wiley.
- Strogatz, S. H. *Nonlinear Dynamics and Chaos*. Westview Press.
- Hirsch, M. W., Smale, S., & Devaney, R. L. *Differential Equations, Dynamical Systems, and an Introduction to Chaos*. Academic Press.
