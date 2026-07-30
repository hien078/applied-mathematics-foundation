# Foundations of Linear Algebra & Computational Linear Algebra

Welcome to the **Linear Algebra Reference Curriculum** under `foundations/linear_algebra/`.

This branch provides a comprehensive, first-principles learning system spanning vector spaces, linear transformations, matrix factorizations, canonical forms, numerical solvers, matrix calculus, and graph linear algebra. It is designed specifically for **Mathematical Modeling**, **AI/Machine Learning Research**, **Scientific Computing**, and **Quantitative Engineering**.

---

## 🗺️ Master Index of 10 Linear Algebra Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Vectors, Vector Spaces & Subspaces | [`01_vectors_spaces_and_subspaces/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/01_vectors_spaces_and_subspaces/) | Vector space axioms, subspaces, affine sets, dual spaces, span, basis, dimension | 40 |
| **Topic 02** | Linear Maps & Matrix Transformations | [`02_linear_maps_and_matrix_transformations/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/02_linear_maps_and_matrix_transformations/) | Linear operators, matrix representations, kernel $\ker(T)$, image $\text{im}(T)$, Rank-Nullity, similarity | 40 |
| **Topic 03** | Linear Systems & Direct Factorizations | [`03_linear_systems_and_direct_factorizations/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/03_linear_systems_and_direct_factorizations/) | $Ax=b$, Rouché-Capelli, 4 fundamental subspaces, LU / PLU factorizations, Cholesky, $LDL^T$ | 40 |
| **Topic 04** | Orthogonality, Projections & QR | [`04_orthogonality_projections_and_qr/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/04_orthogonality_projections_and_qr/) | Inner products, Cauchy-Schwarz, projection matrices, Gram-Schmidt (CGS/MGS), Householder, Givens, QR, Least Squares | 40 |
| **Topic 05** | Determinants, Trace & Matrix Polynomials | [`05_determinants_trace_and_matrix_polynomials/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/05_determinants_trace_and_matrix_polynomials/) | Determinants, trace, volume scaling, Kronecker & Hadamard products, Cayley-Hamilton theorem, minimal polynomial | 40 |
| **Topic 06** | Eigenvalues, Eigenvectors & Spectral Theory | [`06_eigenvalues_eigenvectors_spectral_theory/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/) | Characteristic equation, multiplicities, defective matrices, Spectral Theorem, Rayleigh quotient, perturbation theory | 40 |
| **Topic 07** | Canonical Forms & SVD | [`07_canonical_forms_and_svd/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/07_canonical_forms_and_svd/) | Jordan Canonical Form (JCF), Schur triangularization, SVD, Eckart-Young approximation, pseudoinverse, randomized SVD | 40 |
| **Topic 08** | Numerical Linear Algebra & Iterative Solvers | [`08_numerical_linear_algebra_iterative_solvers/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/08_numerical_linear_algebra_iterative_solvers/) | Flop complexity, forward/backward stability, condition number $\kappa(A)$, Jacobi, Gauss-Seidel, SOR, CG, GMRES, TDMA | 40 |
| **Topic 09** | Numerical Spectrum Algorithms | [`09_numerical_spectrum_algorithms/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/09_numerical_spectrum_algorithms/) | Power iteration, inverse power iteration, Rayleigh quotient iteration, QR algorithm, Arnoldi & Lanczos iterations | 40 |
| **Topic 10** | Matrix Calculus, Graph & AI Applications | [`10_matrix_calculus_graph_and_ai_applications/`](file:///home/hien/Study/AI/Mathematical%20Modeling/foundations/linear_algebra/10_matrix_calculus_graph_and_ai_applications/) | Matrix calculus (Jacobians, Hessians, trace gradients), Markov chains, Graph Laplacian, matrix exponential $e^{At}$, neural layers | 40 |
| **TOTAL** | **10 Master Modules** | — | **Complete 20-Part First-Principles Reference Curriculum** | **400 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `10_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Index, First-Principles Mermaid Concept Map, Core Knowledge Pillars, Common Misconceptions Table, Directory Inventory, Literature References.
2. **`first_principles.md`**: Comprehensive 20-Part Reference Document (Motivation $\to$ History $\to$ Intuition $\to$ Geometry $\to$ Algebra $\to$ Computation $\to$ Formal Definitions $\to$ Properties $\to$ Theorems $\to$ Proof Sketches $\to$ Examples $\to$ Counterexamples $\to$ Applications $\to$ Algorithms $\to$ Numerical Stability $\to$ Python Code $\to$ Connections $\to$ Misconceptions $\to$ Summary $\to$ References).
3. **`exercises.md`**: **5-Level Solved Exercise Package** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Real-World/AI Applications $\to$ L3 Advanced $\to$ L4 Research) featuring explicit proofs, boxed final answers `$$\boxed{...}$$`, and key takeaways.

---

---

## 🏛️ Benchmark Literature References

- **Strang, G.** — *Introduction to Linear Algebra*, 6th Edition & *Linear Algebra and Learning from Data*.
- **Axler, S.** — *Linear Algebra Done Right*, 4th Edition.
- **Trefethen, L. N., & Bau, D.** — *Numerical Linear Algebra*.
- **Golub, G. H., & Van Loan, C. F.** — *Matrix Computations*, 4th Edition.
- **Boyd, S., & Vandenberghe, L.** — *Introduction to Applied Linear Algebra*.
- **Nocedal, J., & Wright, S. J.** — *Numerical Optimization*.
- **Saad, Y.** — *Iterative Methods for Sparse Linear Systems*, 2nd Edition.
- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*, Chapter 2.
