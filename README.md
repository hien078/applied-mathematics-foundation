# Applied Mathematics Foundation 🧮

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange.svg)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.4+-blue.svg)](https://numpy.org/)

First-principles mathematical foundations for machine learning and artificial intelligence.

Eleven areas, 87 numbered modules, and a few thousand fully solved problems. Derivation-first
prose, with a complete solution and a boxed answer under every exercise.

Everything is written to be read directly on GitHub and opened in Google Colab.

> [!NOTE]
> **Sister repository.** Applied algorithm implementations and full ML model pipelines live in
> [Machine-Learning-from-scratch](https://github.com/hien078/Machine-Learning-from-scratch).

---

## What is here today

Each of the 87 modules is a directory holding a `README.md` and two notebooks: one for theory,
one for exercises.

The exercises sit under tier headings running from concept checks to challenge proofs, and
every one of them is solved in full immediately below its statement.

Tier naming is not yet uniform: most modules use Level 0 to Level 3, a few still carry an
older five-name scheme. [`STYLE_GUIDE.md`](STYLE_GUIDE.md) §20 fixes the target as **L0**
to **L3**.

### Executable verification is being added

The curriculum was written as prose and is being upgraded module by module so that every
theorem is checked by a code cell and every central idea is drawn.

For the live count of code cells and figures, run `python3 tools/curriculum_stats.py`.
`python3 tools/check_module.py --all --failing` lists the modules that still fall short of
the contract.

In a module that has not been reached yet, the notebooks are markdown only: no residual is
printed, no convergence rate is measured, no geometry is drawn. Treat a numeric answer in
such a module as unchecked until a code cell computes it.

The module contract in [`STYLE_GUIDE.md`](STYLE_GUIDE.md) §20–21 requires executable
verification and figures. Adding them is the current upgrade, and it is not done:
`python3 tools/check_module.py --all` reports **0 of 87 modules** meeting the contract.

---

## Curriculum at a glance

<!-- curriculum-table:start -->
| Area | Modules | Solved Problems | Code Cells | Figures |
|---|:---:|:---:|:---:|:---:|
| [Calculus](calculus/README.md) | 15 | 605 | 128 | 14 |
| [Calculus to Optimization](calculus_optimization/README.md) | 4 | 80 | 0 | 0 |
| [Differential Equations](differential_equations/README.md) | 8 | 160 | 0 | 0 |
| [Graph Theory](graph_theory/README.md) | 7 | 140 | 0 | 0 |
| [Information Theory](information_theory/README.md) | 6 | 176 | 247 | 19 |
| [Linear Algebra](linear_algebra/README.md) | 10 | 458 | 576 | 32 |
| [Mathematical Reasoning](mathematical_reasoning/README.md) | 6 | 120 | 0 | 0 |
| [Numerical Computing](numerical_computing/README.md) | 5 | 100 | 0 | 0 |
| [Numerical Methods](numerical_methods/README.md) | 8 | 160 | 0 | 0 |
| [Optimization](optimization/README.md) | 8 | 160 | 28 | 0 |
| [Probability and Statistics](probability_statistics/README.md) | 10 | 200 | 41 | 15 |
| **TOTAL** | **87** | **2,359** | **1020** | **80** |
<!-- curriculum-table:end -->

This table is generated. Regenerate it, never edit it by hand:

```bash
python3 tools/curriculum_stats.py --markdown
```

---

## Curriculum

### 1. Linear Algebra

[`linear_algebra/`](linear_algebra/README.md) — 10 modules

- **01.** [Vector Spaces & Subspaces](linear_algebra/01_vectors_spaces_and_subspaces/README.md)
- **02.** [Linear Maps & Matrix Transformations](linear_algebra/02_linear_maps_and_matrix_transformations/README.md)
- **03.** [Linear Systems & Direct Factorizations (LU, Cholesky)](linear_algebra/03_linear_systems_and_direct_factorizations/README.md)
- **04.** [Orthogonality, Projections & QR Decomposition](linear_algebra/04_orthogonality_projections_and_qr/README.md)
- **05.** [Determinants, Trace & Matrix Polynomials](linear_algebra/05_determinants_trace_and_matrix_polynomials/README.md)
- **06.** [Eigenvalues, Eigenvectors & Spectral Theory](linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/README.md)
- **07.** [Canonical Forms & Singular Value Decomposition](linear_algebra/07_canonical_forms_and_svd/README.md)
- **08.** [Numerical Linear Algebra & Iterative Solvers (CG, GMRES)](linear_algebra/08_numerical_linear_algebra_iterative_solvers/README.md)
- **09.** [Numerical Spectrum Algorithms (QR Algorithm, Power Method)](linear_algebra/09_numerical_spectrum_algorithms/README.md)
- **10.** [Matrix Calculus, Graph Theory & AI Applications](linear_algebra/10_matrix_calculus_graph_and_ai_applications/README.md)

### 2. Single & Multivariable Calculus

[`calculus/`](calculus/README.md) — 15 modules

- **01.** [Functions & Fundamental Properties](calculus/01_functions_and_properties/README.md)
- **02.** [Limits & Continuity](calculus/02_limits_and_continuity/README.md)
- **03.** [Single-Variable Derivatives & Chain Rule](calculus/03_single_variable_derivatives/README.md)
- **04.** [Derivative Applications & Optimization](calculus/04_derivative_applications_optimization/README.md)
- **05.** [Indefinite & Definite Integrals](calculus/05_indefinite_and_definite_integrals/README.md)
- **06.** [Integral Applications in Geometry & Physics](calculus/06_integral_applications_geometry_physics/README.md)
- **07.** [Improper Integrals & Special Functions (Gamma, Beta)](calculus/07_improper_integrals_special_functions/README.md)
- **08.** [Sequences, Series & Convergence Tests](calculus/08_sequences_series_convergence/README.md)
- **09.** [Taylor & Power Series](calculus/09_taylor_and_power_series/README.md)
- **10.** [Multivariable Functions & Partial Derivatives](calculus/10_multivariable_functions_partials/README.md)
- **11.** [Gradients & Directional Derivatives](calculus/11_gradients_directional_derivatives/README.md)
- **12.** [Hessian, Jacobian & Curvature](calculus/12_hessian_jacobian_curvature/README.md)
- **13.** [Multiple Integrals & Coordinate Transformations](calculus/13_multiple_integrals_coordinate_transforms/README.md)
- **14.** [Vector Calculus & Field Theorems (Green, Stokes, Divergence)](calculus/14_vector_calculus_field_theorems/README.md)
- **15.** [Ordinary Differential Equations](calculus/15_ordinary_differential_equations/README.md)

### 3. Optimization

[`optimization/`](optimization/README.md) — 8 modules

- **01.** [Problem Formulation & Convexity](optimization/01_problem_formulation_and_convexity/README.md)
- **02.** [Unconstrained Optimality Conditions](optimization/02_unconstrained_optimality_conditions/README.md)
- **03.** [Gradient Descent & Convergence Analysis](optimization/03_gradient_descent_and_convergence/README.md)
- **04.** [Line Search, Newton & Quasi-Newton (BFGS, L-BFGS)](optimization/04_line_search_newton_quasi_newton/README.md)
- **05.** [Constrained Optimization & Lagrange Multipliers](optimization/05_constrained_optimization_lagrange/README.md)
- **06.** [KKT Conditions & Duality](optimization/06_kkt_conditions_and_duality/README.md)
- **07.** [Linear, Quadratic & Conic Programs](optimization/07_linear_quadratic_conic_programs/README.md)
- **08.** [Stochastic Optimization for Machine Learning](optimization/08_stochastic_optimization_for_ml/README.md)

### 4. Calculus to Optimization Bridge

[`calculus_optimization/`](calculus_optimization/README.md) — 4 modules

- **01.** [Derivatives & Gradients for Machine Learning](calculus_optimization/01_derivatives_and_gradients_for_ml/README.md)
- **02.** [Taylor Approximation & Local Models](calculus_optimization/02_taylor_approximation_and_local_models/README.md)
- **03.** [Gradient Descent Mechanics](calculus_optimization/03_gradient_descent_mechanics/README.md)
- **04.** [Optimization Landscapes & Convexity](calculus_optimization/04_optimization_landscapes_and_convexity/README.md)

### 5. Probability & Statistics

[`probability_statistics/`](probability_statistics/README.md) — 10 modules

- **01.** [Sample Spaces & Probability Axioms](probability_statistics/01_sample_spaces_and_probability_axioms/README.md)
- **02.** [Conditional Probability & Bayes' Theorem](probability_statistics/02_conditional_probability_and_bayes/README.md)
- **03.** [Random Variables & Distribution Functions](probability_statistics/03_random_variables_and_distribution_functions/README.md)
- **04.** [Discrete Distributions](probability_statistics/04_discrete_distributions/README.md)
- **05.** [Continuous Distributions](probability_statistics/05_continuous_distributions/README.md)
- **06.** [Expectation, Variance & Moments](probability_statistics/06_expectation_variance_and_moments/README.md)
- **07.** [Joint Distributions & the Multivariate Normal](probability_statistics/07_joint_distributions_and_multivariate_normal/README.md)
- **08.** [Law of Large Numbers & Central Limit Theorem](probability_statistics/08_law_of_large_numbers_and_clt/README.md)
- **09.** [Maximum Likelihood & MAP Estimation](probability_statistics/09_maximum_likelihood_and_map_estimation/README.md)
- **10.** [Bayesian Inference](probability_statistics/10_bayesian_inference/README.md)

### 6. Information Theory

[`information_theory/`](information_theory/README.md) — 6 modules

- **01.** [Self-Information & Entropy](information_theory/01_self_information_and_entropy/README.md)
- **02.** [Joint & Conditional Entropy](information_theory/02_joint_and_conditional_entropy/README.md)
- **03.** [Cross-Entropy & Loss Functions](information_theory/03_cross_entropy_and_loss_functions/README.md)
- **04.** [KL Divergence & $f$-Divergences](information_theory/04_kl_divergence_and_f_divergences/README.md)
- **05.** [Mutual Information](information_theory/05_mutual_information/README.md)
- **06.** [Information Theory in Deep Learning (IB, ELBO, InfoNCE)](information_theory/06_information_theory_in_deep_learning/README.md)

### 7. Numerical Methods

[`numerical_methods/`](numerical_methods/README.md) — 8 modules

- **01.** [Error Analysis & Floating Point](numerical_methods/01_error_analysis_and_floating_point/README.md)
- **02.** [Root-Finding Methods](numerical_methods/02_root_finding_methods/README.md)
- **03.** [Fixed-Point Iteration & Convergence](numerical_methods/03_fixed_point_iteration_and_convergence/README.md)
- **04.** [Polynomial & Spline Interpolation](numerical_methods/04_polynomial_and_spline_interpolation/README.md)
- **05.** [Numerical Differentiation](numerical_methods/05_numerical_differentiation/README.md)
- **06.** [Numerical Integration (Quadrature)](numerical_methods/06_numerical_integration_quadrature/README.md)
- **07.** [Linear Least Squares](numerical_methods/07_linear_least_squares/README.md)
- **08.** [Numerical ODE Solvers](numerical_methods/08_numerical_ode_solvers/README.md)

### 8. Numerical Computing

[`numerical_computing/`](numerical_computing/README.md) — 5 modules

- **01.** [IEEE 754 Floating-Point Representation](numerical_computing/01_ieee754_floating_point_representation/README.md)
- **02.** [Error Propagation & Stability Tricks](numerical_computing/02_error_propagation_and_stability_tricks/README.md)
- **03.** [Conditioning & Condition Numbers](numerical_computing/03_conditioning_and_condition_numbers/README.md)
- **04.** [Vectorization & NumPy Performance](numerical_computing/04_vectorization_and_numpy_performance/README.md)
- **05.** [Numerical Stability in Deep Learning](numerical_computing/05_numerical_stability_in_deep_learning/README.md)

### 9. Differential Equations

[`differential_equations/`](differential_equations/README.md) — 8 modules

- **01.** [Classification & First-Order ODEs](differential_equations/01_classification_and_first_order_odes/README.md)
- **02.** [Existence, Uniqueness & Picard-Lindelof](differential_equations/02_existence_uniqueness_picard_lindelof/README.md)
- **03.** [Second-Order Linear ODEs](differential_equations/03_second_order_linear_odes/README.md)
- **04.** [Systems of ODEs & the Matrix Exponential](differential_equations/04_systems_of_odes_matrix_exponential/README.md)
- **05.** [Phase Plane & Stability Analysis](differential_equations/05_phase_plane_and_stability_analysis/README.md)
- **06.** [Laplace Transform Methods](differential_equations/06_laplace_transform_methods/README.md)
- **07.** [Boundary Value Problems & PDE Preview](differential_equations/07_boundary_value_problems_and_pde_preview/README.md)
- **08.** [ODEs in Machine Learning (Neural ODEs)](differential_equations/08_odes_in_machine_learning/README.md)

### 10. Graph Theory

[`graph_theory/`](graph_theory/README.md) — 7 modules

- **01.** [Graph Fundamentals & Representations](graph_theory/01_graph_fundamentals_and_representations/README.md)
- **02.** [Traversal & Connectivity](graph_theory/02_traversal_and_connectivity/README.md)
- **03.** [Trees & Minimum Spanning Trees](graph_theory/03_trees_and_minimum_spanning_trees/README.md)
- **04.** [Shortest Path Algorithms](graph_theory/04_shortest_paths_algorithms/README.md)
- **05.** [Flows, Matchings & Bipartite Graphs](graph_theory/05_flows_matchings_and_bipartite_graphs/README.md)
- **06.** [Graph Laplacian & Spectral Theory](graph_theory/06_graph_laplacian_and_spectral_theory/README.md)
- **07.** [Spectral Clustering & GNN Applications](graph_theory/07_spectral_clustering_and_gnn_applications/README.md)

### 11. Mathematical Reasoning

[`mathematical_reasoning/`](mathematical_reasoning/README.md) — 6 modules

- **01.** [Propositional & Predicate Logic](mathematical_reasoning/01_propositional_and_predicate_logic/README.md)
- **02.** [Sets, Relations & Functions](mathematical_reasoning/02_sets_relations_and_functions/README.md)
- **03.** [Proof Techniques](mathematical_reasoning/03_proof_techniques/README.md)
- **04.** [Induction & Recursion](mathematical_reasoning/04_induction_and_recursion/README.md)
- **05.** [Combinatorics & Counting](mathematical_reasoning/05_combinatorics_and_counting/README.md)
- **06.** [Asymptotics & Algorithmic Reasoning](mathematical_reasoning/06_asymptotics_and_algorithmic_reasoning/README.md)

---

## Module architecture

Every `<area>/NN_slug/` directory contains exactly three files. The contract below is
[`STYLE_GUIDE.md`](STYLE_GUIDE.md) §20, and it is the definition of a finished module.

### `README.md`

Eleven items, in this order:

1. `# Module NN — Title`
2. Overview: 2–4 short paragraphs on why the module exists
3. A `> [!NOTE]` callout carrying the single most important result
4. Prerequisites and downstream links, as relative paths
5. Learning outcomes, as a bullet list
6. A Mermaid concept map
7. A notation table
8. A core results table
9. Common misconceptions
10. An exercise index matching the real tiers and counts in `exercises.ipynb`
11. References with chapter-level precision

### `first_principles.ipynb`

Theory, following the WHY → INTUITION → WHAT → DEFINITION → DERIVATION → INTERPRETATION →
EXAMPLE → CONNECTION → KEY TAKEAWAYS progression of §5.

- markdown cells for the theory
- executable code cells that verify each major theorem numerically
- 2–4 figures showing the geometry or dynamics of the central idea
- worked numerical examples on small concrete matrices and numbers
- a closing **Key Takeaways** cell

### `exercises.ipynb`

Fully solved problems in four tiers:

- **L0** concept checks
- **L1** foundations
- **L2** AI/ML and physics applications
- **L3** challenge proofs

Each problem carries a statement, a short intuition, a full derivation, a `$$\boxed{...}$$`
answer, and a key takeaway. Where the answer is numeric or algorithmic, a code cell checks it.

The tier names and counts stated in the module `README.md` must equal what the notebook
contains.

> [!IMPORTANT]
> The code cells, the figures, the Key Takeaways cell and the `L0`–`L3` tier names above are
> the contract, not the present state of the tree.
> See [What is not here yet](#what-is-not-here-yet).

---

## Repository standards

Four documents govern content. Where a module contradicts one of them, the module is what
changes.

| Document | Authority |
|---|---|
| [`STYLE_GUIDE.md`](STYLE_GUIDE.md) | Presentation, GitHub rendering rules, and the three-file module contract. Overrides every older convention in the repository. |
| [`docs/notation.md`](docs/notation.md) | Symbols and contested conventions, with one ruling per collision and the modules the losing convention still lives in. |
| [`docs/prerequisites.md`](docs/prerequisites.md) | The dependency graph over all 87 modules, plus one valid study order through them. |
| [`CLAUDE.md`](CLAUDE.md) | Working instructions and the benchmark texts each area is measured against. |

### Reference standard

Content is measured against the leading applied-mathematics texts, not against lecture
handouts.

| Area | Reference texts |
|---|---|
| Linear algebra | Strang, *Linear Algebra and Learning from Data*; Trefethen & Bau; Axler |
| Calculus | Spivak; Apostol; Hubbard & Hubbard |
| Optimization | Boyd & Vandenberghe; Nocedal & Wright; Bertsekas |
| Probability & statistics | Wasserman; Casella & Berger; Durrett; Bishop |
| Information theory | Cover & Thomas; MacKay |
| Numerical methods & computing | Trefethen & Bau; Higham, *Accuracy and Stability*; Heath |
| Differential equations | Strogatz; Hirsch, Smale & Devaney; Teschl |
| Graph theory | Bollobas; Chung, *Spectral Graph Theory*; Newman |
| Mathematical reasoning | Velleman; Rosen; Graham, Knuth & Patashnik |

---

## How to read it

The material is a graph, not a list. [`docs/prerequisites.md`](docs/prerequisites.md) states
what each module depends on and gives one valid order through all 87 of them, in
thirteen stages from proof technique to information theory.

Start there if you intend to work straight through.

---

## Legacy files at area roots

Twenty-three files sit at area roots, outside every numbered module: `first_principles.md`,
`exercises.md`, `computation.ipynb` and a handful of demo notebooks.

They predate the numbered curriculum and are **not** maintained against the module notebooks.
They are not part of the module contract and no module depends on one.

They are listed in [`docs/prerequisites.md`](docs/prerequisites.md#files-outside-the-graph).

---

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/hien078/applied-mathematics-foundation.git
cd applied-mathematics-foundation
```

### 2. Set up the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Launch JupyterLab

```bash
jupyter lab
```

GitHub and Colab both render the notebooks as they are, so a local environment is needed only
for authoring and validation.

---

## Validation

Run the content validator before every commit:

```bash
python3 tools/validate_content.py
```

It checks notebook JSON, KaTeX compilation of every math span, Mermaid parsing, GitHub table
hazards, relative links, and Colab badge targets.

The KaTeX and Mermaid checks need `node` with three packages available on disk:

```bash
npm install katex mermaid jsdom
VALIDATE_NODE_MODULES="$PWD/node_modules" python3 tools/validate_content.py
```

Exit code 0 means the whole repository renders.

### Structural gate

`validate_content.py` answers *does it render?*. This answers *does it meet the module
contract?*:

```bash
python3 tools/check_module.py linear_algebra/06_eigenvalues_eigenvectors_spectral_theory
python3 tools/check_module.py --all --failing
```

### Authoring notebooks

Never edit notebook JSON by hand: a `\right` spliced into a JSON string decodes as a
carriage return. Round-trip through the helper instead.

```bash
python3 tools/nbtool.py to-text   path/to/notebook.ipynb -o draft.txt
python3 tools/nbtool.py from-text draft.txt -o path/to/notebook.ipynb
python3 tools/nbtool.py exec      path/to/notebook.ipynb
python3 tools/validate_content.py path/to/notebook.ipynb
```

Write `draft.txt` with a quoted heredoc (`<<'EOF'`) so backslashes stay literal.

---

## License

Released under the MIT License — see [LICENSE](LICENSE) for details.
