# Foundations of Numerical Computing — Floating-Point & Stability Mastery Curriculum

Welcome to the **Numerical Computing Mastery Curriculum** under `foundations/numerical_computing/`.

Every number a computer stores is an approximation, and every algorithm either tames or amplifies that approximation error. This module provides a comprehensive, first-principles learning system spanning the IEEE 754 floating-point standard, error propagation and the classic stability tricks, conditioning and condition numbers, vectorization and NumPy performance engineering, and the numerical stability techniques that keep deep networks training. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

---

## 🗺️ Master Index of 5 Numerical Computing Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | IEEE 754 Floating-Point Representation | [`01_ieee754_floating_point_representation/`](01_ieee754_floating_point_representation/) | Sign-exponent-mantissa layout, normalized and subnormal numbers, machine epsilon $\varepsilon_{\mathrm{mach}} = 2^{-53}$, rounding modes, Inf/NaN semantics, float32/bfloat16/float16 formats | 20 |
| **Topic 02** | Error Propagation & Stability Tricks | [`02_error_propagation_and_stability_tricks/`](02_error_propagation_and_stability_tricks/) | Absolute vs relative error, catastrophic cancellation, the standard model $\mathrm{fl}(x \circ y) = (x \circ y)(1 + \delta)$, stable quadratic formula, log-sum-exp, Kahan summation, backward error analysis | 20 |
| **Topic 03** | Conditioning & Condition Numbers | [`03_conditioning_and_condition_numbers/`](03_conditioning_and_condition_numbers/) | Relative condition number of a function, matrix condition number $\kappa(A) = \Vert A \Vert \, \Vert A^{-1} \Vert$, singular values, rule of thumb on lost digits, ill-conditioned Hilbert and Vandermonde systems, normal equations vs QR | 20 |
| **Topic 04** | Vectorization & NumPy Performance | [`04_vectorization_and_numpy_performance/`](04_vectorization_and_numpy_performance/) | Strided memory layout, broadcasting rules, contiguity and cache locality, BLAS levels 1–3, in-place operations, einsum, temporaries and memory bandwidth, benchmarking discipline | 20 |
| **Topic 05** | Numerical Stability in Deep Learning | [`05_numerical_stability_in_deep_learning/`](05_numerical_stability_in_deep_learning/) | Stable softmax and cross-entropy fusion, vanishing/exploding gradients, gradient clipping, normalization layers, mixed-precision training with loss scaling, Adam's $\epsilon$, reproducibility | 20 |
| **TOTAL** | **5 Numerical Computing Modules** | — | **Complete First-Principles Curriculum** | **100 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `05_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., the floating-point standard model, the cancellation error bound, forward error $\leq$ condition number $\times$ backward error, Kahan compensated summation), Computational and Algorithmic Insights, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## 🔗 Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`floating_point_stability.md`](floating_point_stability.md) | Legacy theory file: IEEE 754 representation and error analysis — the seed document the 5 modules expand upon |
| [`conditioning_stability.ipynb`](conditioning_stability.ipynb) | Executable companion notebook: condition-number demonstrations on ill-conditioned systems |
| [`vectorization_numpy.ipynb`](vectorization_numpy.ipynb) | Executable companion notebook: NumPy vectorization and performance benchmarks |
| [`../numerical_methods/`](../numerical_methods/) | Sibling module applying this error analysis to root finding, interpolation, quadrature, and linear solvers |
| [`../linear_algebra/`](../linear_algebra/) | Sibling module supplying norms, SVD, and factorizations behind the condition number |
| [`../optimization/`](../optimization/) | Sibling module where conditioning governs gradient-descent convergence rates |

### Used By

All topics benefit from numerical stability awareness. Critical for:

- [13 Neural Networks](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/13_neural_networks/README.md) — gradient stability
- [02 Gradient Descent](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/02_gradient_descent/README.md) — convergence issues

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy notebooks to watch conditioning and vectorization effects measured on real hardware.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Goldberg, D.** — *What Every Computer Scientist Should Know About Floating-Point Arithmetic* (ACM Computing Surveys, 1991)
- **Higham, N. J.** — *Accuracy and Stability of Numerical Algorithms*, 2nd Edition (SIAM)
- **Trefethen, L. N., & Bau, D.** — *Numerical Linear Algebra* (SIAM)
- **Harris, C. R., et al.** — *Array Programming with NumPy* (Nature, 2020)
- **Micikevicius, P., et al.** — *Mixed Precision Training* (ICLR, 2018)
- **Overton, M. L.** — *Numerical Computing with IEEE Floating Point Arithmetic* (SIAM)
- **Golub, G. H., & Van Loan, C. F.** — *Matrix Computations*, 4th Edition (Johns Hopkins University Press)
- **IEEE** — *Standard for Floating-Point Arithmetic (IEEE 754-2019)*
- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*, Chapter 4 (MIT Press)
