# Foundations of Calculus & Optimization — ML Optimization Bridge Curriculum

Welcome to the **Calculus & Optimization Bridge Curriculum** under `foundations/calculus_optimization/`.

This module is the bridge between differential calculus and the optimization algorithms that train machine learning models: it takes the derivative from a limit definition all the way to a working gradient-descent loop with a justified learning rate. It provides a comprehensive, first-principles learning system spanning derivatives and gradients for ML, Taylor approximation as the universal local model, the mechanics and convergence of gradient descent, and the geometry of optimization landscapes and convexity. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

---

## 🗺️ Master Index of 4 Calculus & Optimization Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Derivatives & Gradients for Machine Learning | [`01_derivatives_and_gradients_for_ml/`](01_derivatives_and_gradients_for_ml/) | Limit definition, chain rule and backpropagation, partial derivatives, gradient $\nabla f$ as steepest ascent, Jacobians, directional derivatives, automatic differentiation | 20 |
| **Topic 02** | Taylor Approximation & Local Models | [`02_taylor_approximation_and_local_models/`](02_taylor_approximation_and_local_models/) | First- and second-order expansions, Lagrange remainder, multivariate Taylor with Hessian $\nabla^2 f$, quadratic surrogate models, linearization, error scaling and truncation | 20 |
| **Topic 03** | Gradient Descent Mechanics | [`03_gradient_descent_mechanics/`](03_gradient_descent_mechanics/) | Update rule $x_{k+1} = x_k - \eta \nabla f(x_k)$, descent lemma, $L$-smoothness and the stability bound $\eta \lt 2/L$, convergence rates, momentum, batch vs stochastic gradients, learning-rate schedules | 20 |
| **Topic 04** | Optimization Landscapes & Convexity | [`04_optimization_landscapes_and_convexity/`](04_optimization_landscapes_and_convexity/) | Convex sets and functions, Jensen's inequality, second-order convexity test $\nabla^2 f \succeq 0$, critical-point classification, saddle points, condition number and valley geometry, non-convex deep-learning landscapes | 20 |
| **TOTAL** | **4 Calculus & Optimization Modules** | — | **Complete First-Principles Curriculum** | **80 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `04_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., the chain rule behind backpropagation, Taylor's theorem with remainder, the descent lemma and the $\eta \lt 2/L$ stability threshold, first-order characterizations of convexity), Computational and Algorithmic Insights, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## 🔗 Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`derivatives_gradients.md`](derivatives_gradients.md) | Legacy theory file: derivative definitions, the chain rule, and the Jacobian — the seed document the 4 modules expand upon |
| [`gradient_descent.ipynb`](gradient_descent.ipynb) | Executable companion notebook: the gradient-descent algorithm and convergence demonstrations |
| [`taylor_approximation.ipynb`](taylor_approximation.ipynb) | Executable companion notebook: Taylor series and local-approximation demonstrations |
| [`optimization_landscape.ipynb`](optimization_landscape.ipynb) | Executable companion notebook: convexity, saddle points, and landscape visualizations |
| [`../calculus/`](../calculus/) | Parent module developing the full single- and multi-variable calculus this bridge draws on |
| [`../optimization/`](../optimization/) | Sibling module continuing into constrained optimization, KKT/duality, and stochastic methods for large-scale ML |
| [`../numerical_computing/`](../numerical_computing/) | Sibling module explaining the floating-point limits on finite-difference gradients and step sizes |

### Used By

- [02 Gradient Descent](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/02_gradient_descent/README.md)
- [03 Regularization](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/03_regularization/README.md)
- [13 Neural Networks](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/13_neural_networks/README.md) — backpropagation

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy notebooks to watch descent trajectories, Taylor approximations, and landscape geometry come alive.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*, Chapters 4 and 8 (MIT Press)
- **Boyd, S., & Vandenberghe, L.** — *Convex Optimization* (Cambridge University Press)
- **Nocedal, J., & Wright, S. J.** — *Numerical Optimization*, 2nd Edition (Springer)
- **Baydin, A. G., Pearlmutter, B. A., Radul, A. A., & Siskind, J. M.** — *Automatic Differentiation in Machine Learning: A Survey* (JMLR, 2018)
- **Dauphin, Y., Pascanu, R., Gulcehre, C., Cho, K., Ganguli, S., & Bengio, Y.** — *Identifying and Attacking the Saddle Point Problem in High-Dimensional Non-Convex Optimization* (NeurIPS, 2014)
- **Spivak, M.** — *Calculus* (Publish or Perish)
- **Nesterov, Y.** — *Lectures on Convex Optimization* (Springer)
- **Bottou, L., Curtis, F. E., & Nocedal, J.** — *Optimization Methods for Large-Scale Machine Learning* (SIAM Review, 2018)
