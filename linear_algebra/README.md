# Linear Algebra

Linear algebra is the language the rest of this repository is written in.

A dataset is a matrix, a model layer is a linear map, a loss surface is a quadratic form, and
almost every algorithm that follows — least squares, PCA, gradient descent, spectral clustering,
backpropagation — is a statement about factorizing or diagonalizing something.

This area develops that language from the axioms of a vector space through to the numerical
algorithms that make it usable in floating-point arithmetic. Ten modules, 400 fully solved
problems.

It is written for a reader who wants to *check* the mathematics rather than accept it: every
theorem is stated with its hypotheses, and the proofs are meant to be followed line by line.
The benchmark is a chapter of Trefethen & Bau or Horn & Johnson, not a lecture handout.

---

## Prerequisites

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
It is the single source of truth for module order; the table below is drawn from it.

This area depends on one other area:

- [`../mathematical_reasoning/`](../mathematical_reasoning/) — module 01 assumes you can prove
  two sets equal by double inclusion and choose a proof shape deliberately.

Two later modules reach outside the area:

- Module 08 assumes [`../numerical_computing/03`](../numerical_computing/03_conditioning_and_condition_numbers/)
  for conditioning, which is that module's canonical topic.
- Module 10 assumes [`../calculus/12`](../calculus/12_hessian_jacobian_curvature/) for the
  Hessian and the Jacobian determinant.

No calculus is needed for modules 01 through 09.

---

## Module index

| Module | What it covers | Prerequisites | Problems |
| :--- | :--- | :--- | ---: |
| [01 — Vectors, Spaces and Subspaces](./01_vectors_spaces_and_subspaces/) | Vector space axioms; subspaces; affine and convex hulls with barycentric coordinates; span, independence, basis, dimension via Steinitz exchange; dual spaces and annihilators; sums, direct sums and quotients; tensor products; the coordinate isomorphism | [math. reasoning 02](../mathematical_reasoning/02_sets_relations_and_functions/), [03](../mathematical_reasoning/03_proof_techniques/) | 40 |
| [02 — Linear Maps and Matrix Transformations](./02_linear_maps_and_matrix_transformations/) | Linearity; the space $\mathcal{L}(V, W)$; the matrix $[T]_{C,B}$ of a map; composition as matrix product; kernel and image; rank-nullity; rank factorization; change of basis; similarity and its invariants | [01](./01_vectors_spaces_and_subspaces/) | 40 |
| [03 — Linear Systems and Direct Factorizations](./03_linear_systems_and_direct_factorizations/) | Solvability of $Ax = b$ and Rouché-Capelli; the four fundamental subspaces; LU, PLU, Cholesky and $LDL^\top$; the Schur complement; Sherman-Morrison-Woodbury; conditioning against stability; the growth factor | [02](./02_linear_maps_and_matrix_transformations/) | 40 |
| [04 — Orthogonality, Projections and QR](./04_orthogonality_projections_and_qr/) | Inner products and induced norms; Cauchy-Schwarz, triangle, Bessel, Parseval; the Gram matrix; the decomposition $V = W \oplus W^{\perp}$; orthogonal projections and best approximation; least squares; classical and modified Gram-Schmidt, Householder, Givens; QR existence and uniqueness | [03](./03_linear_systems_and_direct_factorizations/) | 40 |
| [05 — Determinants, Trace and Matrix Polynomials](./05_determinants_trace_and_matrix_polynomials/) | Trace; the determinant as an alternating multilinear form; Laplace expansion; Cramer's rule; outer, Hadamard, Kronecker and Khatri-Rao products with the vec identity; characteristic and minimal polynomials; companion matrices; Cayley-Hamilton | [02](./02_linear_maps_and_matrix_transformations/) | 40 |
| [06 — Eigenvalues, Eigenvectors and Spectral Theory](./06_eigenvalues_eigenvectors_spectral_theory/) | Characteristic equation; algebraic against geometric multiplicity; defective matrices; diagonalization; the spectral theorem for symmetric and for normal matrices; Rayleigh quotient and Courant-Fischer; Schur decomposition; positive definiteness; Gershgorin discs; Gelfand's formula; matrix functions | [04](./04_orthogonality_projections_and_qr/), [05](./05_determinants_trace_and_matrix_polynomials/) | 40 |
| [07 — Canonical Forms and SVD](./07_canonical_forms_and_svd/) | Schur triangularization; Jordan canonical form; the SVD by both an algebraic and a geometric proof; polar decomposition; matrix norms read off the singular values; Eckart-Young-Mirsky; the Moore-Penrose pseudoinverse; randomized SVD | [06](./06_eigenvalues_eigenvectors_spectral_theory/) | 40 |
| [08 — Numerical Linear Algebra and Iterative Solvers](./08_numerical_linear_algebra_iterative_solvers/) | Machine precision and flop counts; forward against backward stability; error amplification by $\kappa(A)$; the Thomas algorithm; Jacobi, Gauss-Seidel and SOR under the spectral-radius criterion; Krylov subspaces; conjugate gradients with the Chebyshev bound; GMRES; preconditioning; multigrid | [06](./06_eigenvalues_eigenvectors_spectral_theory/), [num. computing 03](../numerical_computing/03_conditioning_and_condition_numbers/) | 40 |
| [09 — Numerical Spectrum Algorithms](./09_numerical_spectrum_algorithms/) | Power, inverse power and Rayleigh-quotient iteration; the Jacobi eigenvalue algorithm; the QR algorithm with Hessenberg reduction and shifts; divide-and-conquer; Arnoldi, Lanczos and IRAM; Golub-Kahan bidiagonalization; loss of orthogonality and reorthogonalization | [07](./07_canonical_forms_and_svd/), [08](./08_numerical_linear_algebra_iterative_solvers/) | 40 |
| [10 — Matrix Calculus, Graph and AI Applications](./10_matrix_calculus_graph_and_ai_applications/) | Jacobians and Hessians; gradients of linear, quadratic and trace forms; $\nabla_X \ln \det X$; the differential method of Magnus and Neudecker; vec and Kronecker identities; adjacency, degree and graph Laplacians; spectral clustering and the Cheeger inequality; Markov chains and stationary distributions; the matrix exponential $e^{At}$; backpropagation and graph convolutions | [calculus 12](../calculus/12_hessian_jacobian_curvature/), [07](./07_canonical_forms_and_svd/) | 40 |
| **Total** | **10 modules** | — | **458** |

Counts come from `python3 tools/curriculum_stats.py --modules`: 40 problems per module.

---

## Module architecture

Every `NN_slug/` directory holds exactly three files, per
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20.

`README.md` carries the module overview, a `> [!NOTE]` callout with its single most important
result, prerequisite and downstream links, learning outcomes, a Mermaid concept map, a notation
table, a core-results table, common misconceptions, an exercise index that matches the notebook,
and references at chapter precision.

`first_principles.ipynb` develops the theory in the order WHY, INTUITION, WHAT, FORMAL
DEFINITION, MATHEMATICAL FORMULATION, DERIVATION, INTERPRETATION, EXAMPLE, CONNECTION, KEY
TAKEAWAYS. It must carry executable code cells that verify each major theorem numerically, two
to four figures showing the geometry of the central idea, worked examples on concrete small
matrices, and a closing Key Takeaways cell.

`exercises.ipynb` holds fully solved problems in exactly four tiers:

- **L0** — concept checks
- **L1** — foundations
- **L2** — AI/ML and physics applications
- **L3** — challenge proofs

Each problem carries a statement, intuition, a full derivation, a `$$\boxed{...}$$` answer, a key
takeaway, and — where the answer is numeric or algorithmic — a code cell that checks it.

> [!NOTE]
> **This area is complete.** All ten modules pass `python3 tools/check_module.py`: executable
> code cells, figures, the `L0`-`L3` tiers, and the full README section list — including
> prerequisites, learning outcomes and a notation table — are in place in every module.

Notebooks are authored with `tools/nbtool.py`, never by editing JSON by hand, and every code cell
must run top to bottom from a fresh kernel using only
[`../requirements.txt`](../requirements.txt).

---

## Notation

The repository-wide register is [`../docs/notation.md`](../docs/notation.md). Its linear-algebra
section fixes the conventions this area uses:

- Eigenvalues run **descending**, $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$, matching the
  singular-value ordering $\sigma_1 \ge \cdots \ge \sigma_r$ and PCA's "first $k$ components".
  Courant-Fischer is therefore the max-min form.
- Transpose is $A^\top$; norms are $\lVert x \rVert$; the condition number is
  $\kappa_2(A) = \sigma_1 / \sigma_n$.
- $\Lambda$ is the eigenvalue diagonal. Inside a factorization $A = U \Sigma V^\top$, $\Sigma$ is
  the singular-value matrix; standing alone it is a covariance matrix.
- Markov transition matrices are **column-stochastic**, one step is $\pi_{t+1} = P \pi_t$, and
  stationarity is $P \pi = \pi$.
- Chebyshev polynomials are $T_k$, with $T_0 = 1$, $T_1(y) = y$ and
  $T_{k+1}(y) = 2 y T_k(y) - T_{k-1}(y)$.

One **declared exception** applies inside module 10: graph Laplacian eigenvalues are written
ascending, $0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$, so that $\lambda_2$ is the
algebraic connectivity. Every module using that ordering must flag it.

Three sites in this area have not been migrated to the register yet: module 06 §16 states
Courant-Fischer ascending, module 06 §27 offers both Markov conventions and fixes neither, and
module 08's exercises write $C_k$ for the Chebyshev polynomials that its own notes call $T_k$.

---

## Suggested order

Modules 01 through 07 are the core sequence and are self-contained given
`mathematical_reasoning`. Work straight through.

1. [01 — Vectors, Spaces and Subspaces](./01_vectors_spaces_and_subspaces/)
2. [02 — Linear Maps and Matrix Transformations](./02_linear_maps_and_matrix_transformations/)
3. [03 — Linear Systems and Direct Factorizations](./03_linear_systems_and_direct_factorizations/)
4. [04 — Orthogonality, Projections and QR](./04_orthogonality_projections_and_qr/)
5. [05 — Determinants, Trace and Matrix Polynomials](./05_determinants_trace_and_matrix_polynomials/)
6. [06 — Eigenvalues, Eigenvectors and Spectral Theory](./06_eigenvalues_eigenvectors_spectral_theory/)
7. [07 — Canonical Forms and SVD](./07_canonical_forms_and_svd/)

Modules 04 and 05 are independent of each other. Module 05 needs only 02, so it can be read any
time after 02; module 06 needs both.

Then take the detour through
[`../numerical_computing/`](../numerical_computing/) modules 01 through 03, which supply the
floating-point model and the conditioning theory that module 08 assumes.

8. [08 — Numerical Linear Algebra and Iterative Solvers](./08_numerical_linear_algebra_iterative_solvers/)
9. [09 — Numerical Spectrum Algorithms](./09_numerical_spectrum_algorithms/)

Module 10 needs the Hessian and the Jacobian determinant from
[`../calculus/12`](../calculus/12_hessian_jacobian_curvature/), so it comes after the
multivariable-calculus stage.

10. [10 — Matrix Calculus, Graph and AI Applications](./10_matrix_calculus_graph_and_ai_applications/)

This matches Stage 3 and Stage 6 of the study order in
[`../docs/prerequisites.md`](../docs/prerequisites.md).

---

## Companion resources

The area root holds no legacy files: this `README.md` and the ten numbered module directories are
everything in `linear_algebra/`.

Everything else this area depends on lives at the repository root:

- [`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) — the authoritative presentation standard.
- [`../docs/prerequisites.md`](../docs/prerequisites.md) — the dependency graph over all 87
  modules, the forward references still to be removed, and the canonical owner of each
  duplicated topic. It records that Courant-Fischer belongs to module 06 and that the graph
  Laplacian and spectral clustering belong to
  [`../graph_theory/06`](../graph_theory/06_graph_laplacian_and_spectral_theory/) and
  [`../graph_theory/07`](../graph_theory/07_spectral_clustering_and_gnn_applications/), with
  module 10 linking out rather than re-deriving them.
- [`../docs/notation.md`](../docs/notation.md) — the notation register.
- [`../requirements.txt`](../requirements.txt) — the only dependencies a notebook may import.

Each notebook carries a Colab badge pointing at its own path, so any module can be opened in the
browser. Until the code cells land there is nothing in these notebooks to execute.

Two topics in this area are deliberately shared with other areas. Spectral graph theory is
developed in `graph_theory`, and the matrix exponential is developed in
[`../differential_equations/04`](../differential_equations/04_systems_of_odes_matrix_exponential/);
module 10 keeps only what it uses and links out.

---

## References

The benchmark texts for this area, from [`../CLAUDE.md`](../CLAUDE.md).

**Axler, S.** *Linear Algebra Done Right*, 4th ed.
Ch. 1-2 for the vector-space and dimension theory of module 01; Ch. 3, including the fundamental
theorem of linear maps, quotients and duality, for module 02; Ch. 5 and Ch. 7 for eigenvalues and
the spectral theorem in module 06; Ch. 8 for generalized eigenvectors and Jordan form in module
07; Ch. 9 for the multilinear treatment of determinants in module 05.

**Trefethen, L. N., and Bau, D.** *Numerical Linear Algebra*.
Lectures 1-5 for norms and the SVD (module 07); Lectures 6-11 for projectors, QR, Gram-Schmidt,
Householder and least squares (module 04); Lectures 12-19 for conditioning and stability (modules
03 and 08); Lectures 20-23 for Gaussian elimination, pivoting and Cholesky (module 03); Lectures
24-31 for eigenvalue algorithms, the QR algorithm and computing the SVD (module 09); Lectures
32-40 for Arnoldi, GMRES, Lanczos, conjugate gradients and preconditioning (module 08).

**Horn, R. A., and Johnson, C. R.** *Matrix Analysis*, 2nd ed.
Ch. 1 for eigenvalues and similarity and Ch. 6 for Gershgorin and eigenvalue perturbation (module
06); Ch. 2 for unitary similarity and Schur triangularization and Ch. 3 for the Jordan form
(module 07); Ch. 4 for Hermitian matrices, the variational characterizations and Sylvester's law
of inertia (modules 03 and 06); Ch. 5 for vector and matrix norms (module 08); Ch. 7 for positive
definiteness, the polar decomposition and the Schur product theorem (modules 05 and 07).

**Strang, G.** *Linear Algebra and Learning from Data*.
I.3-I.4 for the four fundamental subspaces and elimination (module 03); I.5 for orthogonal
matrices (module 04); I.6-I.7 for eigenvalues and positive definiteness (module 06); I.8-I.9 for
the SVD, PCA and the best low-rank matrix (module 07); I.11 and II.1-II.2 for norms, numerical
linear algebra and least squares (module 08); II.4 for randomized linear algebra (module 07);
IV.3 for the Kronecker product (module 05); IV.6 for graphs and Laplacians and VII.3 for
backpropagation and the chain rule (module 10).

Two texts from adjacent rows of the same benchmark table cover the applied end of this area.

**Higham, N. J.** *Accuracy and Stability of Numerical Algorithms*, 2nd ed.
Ch. 9 for LU and linear equations and Ch. 10 for Cholesky (module 03); Ch. 19 for the QR
factorization and Ch. 20 for the least-squares problem (module 04).

**Chung, F. R. K.** *Spectral Graph Theory*.
Ch. 1 for the Laplacian and its eigenvalues and Ch. 2 for isoperimetric problems and the Cheeger
inequality (module 10).

Individual module READMEs carry their own additional citations at chapter precision.
