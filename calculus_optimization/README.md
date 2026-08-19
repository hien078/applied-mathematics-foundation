# Calculus for Optimization

This area is the bridge from differential calculus to the algorithms that train machine-learning
models. It starts at the limit definition of a derivative and ends with a gradient-descent loop
whose step size is justified by a theorem rather than found by a sweep.

Four modules carry that arc. Module 01 builds the derivative objects — gradient, Jacobian, Hessian,
subgradient — and the chain rule that becomes backpropagation. Module 02 turns them into local models
with honest remainder bounds. Module 03 analyses what repeating a single gradient step actually does.
Module 04 asks where those iterations can possibly stop.

It is written for readers who already have single-variable calculus and basic linear algebra and now
want the optimization theory behind training, at the level of Boyd & Vandenberghe and
Nocedal & Wright rather than a framework tutorial.

The sibling area [`../optimization/`](../optimization/) carries the same subject further — line
search, quasi-Newton, constraints, KKT and duality, stochastic methods. This area deliberately stops
at the unconstrained calculus core those results assume, and the two overlap by design; see the
duplication table in [`../docs/prerequisites.md`](../docs/prerequisites.md).

---

## Prerequisites

[`../docs/prerequisites.md`](../docs/prerequisites.md) is the repository-wide dependency graph and is
authoritative on reading order. The per-module column in the index below is drawn from it.

This area depends on three others:

- [`../calculus/`](../calculus/) — module [09](../calculus/09_taylor_and_power_series/) (Taylor and
  power series), [11](../calculus/11_gradients_directional_derivatives/) (gradients and directional
  derivatives), [12](../calculus/12_hessian_jacobian_curvature/) (Hessian, Jacobian, curvature)
- [`../linear_algebra/`](../linear_algebra/) — module
  [02](../linear_algebra/02_linear_maps_and_matrix_transformations/) (linear maps and matrices),
  [06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/) (eigenvalues and the spectral
  theorem)
- [`../numerical_computing/`](../numerical_computing/) — module
  [03](../numerical_computing/03_conditioning_and_condition_numbers/) (conditioning and condition
  numbers)

---

## Module index

| Module | What it covers | Prerequisites | Problems |
|---|---|---|---:|
| [`01_derivatives_and_gradients_for_ml/`](01_derivatives_and_gradients_for_ml/) | $\nabla f$ as steepest ascent via Cauchy–Schwarz; the gradient normal to a level set; Jacobian and the vector chain rule behind backpropagation; least-squares gradient and Hessian; subgradients for ReLU and $L^1$; forward- and reverse-mode autodiff; central-difference gradient checking | [calculus/11](../calculus/11_gradients_directional_derivatives/), [linear_algebra/02](../linear_algebra/02_linear_maps_and_matrix_transformations/) | 20 |
| [`02_taylor_approximation_and_local_models/`](02_taylor_approximation_and_local_models/) | Taylor's theorem with Lagrange remainder; the multivariate second-order expansion; the descent lemma from $L$-smoothness; quadratics are $L$-smooth with $L = \lambda_{\max}$; Newton exact on quadratics and its local quadratic rate; model errors of order $O(h^2)$ and $O(h^3)$ | [calculus/09](../calculus/09_taylor_and_power_series/), [calculus/12](../calculus/12_hessian_jacobian_curvature/), [01](01_derivatives_and_gradients_for_ml/) | 20 |
| [`03_gradient_descent_mechanics/`](03_gradient_descent_mechanics/) | Error dynamics $e_{k+1} = (I - \eta H)e_k$ and the stability window $\eta \lt 2/\lambda_{\max}$; the optimal step and the $(\kappa-1)/(\kappa+1)$ rate; sufficient decrease at $\eta = 1/L$; $O(1/k)$ convex and geometric strongly convex rates; gradient flow as explicit Euler; heavy-ball momentum; the minibatch noise ball and step-size schedules | [linear_algebra/06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/), [numerical_computing/03](../numerical_computing/03_conditioning_and_condition_numbers/), [02](02_taylor_approximation_and_local_models/) | 20 |
| [`04_optimization_landscapes_and_convexity/`](04_optimization_landscapes_and_convexity/) | Convex sets and functions; the first- and second-order characterizations; local minima are global; second-order optimality conditions and the classification of critical points by Hessian spectrum; degenerate cases; saddle dominance in high dimension; escape from strict saddles; Jensen's inequality; sharp versus flat minima | [03](03_gradient_descent_mechanics/) | 20 |
| **Total** | 4 modules | — | **80** |

Counts come from `python3 tools/curriculum_stats.py`, not from prose.

The condition number $\kappa$, the narrow-valley zigzag and the $O(\kappa\log(1/\epsilon))$ iteration
count are developed in module 03. Module 04 only cites them.

---

## Module architecture

Each numbered folder holds exactly three files, as [`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20
requires.

| File | Role |
|---|---|
| `README.md` | Overview, key-result callout, prerequisite and downstream links, learning outcomes, Mermaid concept map, notation table, core-results table, misconceptions, exercise index, references |
| `first_principles.ipynb` | Intuition, definitions, theorem statements, full proofs, algorithmic insights, applications, closing Key Takeaways cell |
| `exercises.ipynb` | Twenty fully solved problems in four tiers |

Both notebooks are `.ipynb` files, never `.md`. Each opens with a Colab badge pointing at its own
path.

### Exercise tiers

STYLE_GUIDE §20 fixes exactly four:

- **L0** — concept checks
- **L1** — foundations
- **L2** — AI/ML and physics applications
- **L3** — challenge proofs

Every module in this area carries 4 / 6 / 6 / 4 problems across L0–L3, twenty in all. Each problem
gives a statement, an intuition, a full derivation, a `$$\boxed{...}$$` answer, and a key takeaway.

### Code, figures, and what exists today

The contract in STYLE_GUIDE §20 and §21 is demanding. `first_principles.ipynb` must carry executable
code cells that verify each major theorem numerically, two to four figures showing the geometry or
dynamics of the central idea, worked numerical examples with concrete small matrices, and a closing
Key Takeaways cell. `exercises.ipynb` must carry a checking code cell wherever an answer is numeric
or algorithmic.

The eight module notebooks in this area are still markdown throughout: no code cells, no
figures. Run `python3 tools/check_module.py --all --failing` for the modules that still fall short, and `python3 tools/curriculum_stats.py` for the live code-cell and figure counts.

So the theory here is read, not run. An upgrade wave is adding the code and the figures; until it
lands, the paragraphs above describe the contract, not the tree. The only executed code in this area
sits in the three legacy notebooks at the area root, described under Companion resources.

---

## Notation

[`../docs/notation.md`](../docs/notation.md) fixes the symbols. Its *Calculus and optimization*
section is the one this area answers to: $\eta$ step size, $L$ smoothness constant, $\mu$
strong-convexity modulus, $\kappa = L/\mu$, $M$ Hessian Lipschitz constant,
$\Delta_k = f(x_k) - f^\star$, and $\lambda_{\min}$, $\lambda_{\max}$ for the extreme Hessian
eigenvalues.

Three rulings bind this area in particular.

**$L$-smoothness** means the gradient is $L$-Lipschitz:

$$
\lVert \nabla f(x) - \nabla f(y) \rVert_2 \le L \lVert x - y \rVert_2 .
$$

For $f \in C^2$ that is equivalent to the operator-norm bound
$\lVert \nabla^2 f(x) \rVert_{\mathrm{op}} \le L$, i.e. $-LI \preceq \nabla^2 f(x) \preceq LI$.
Module 02 states this correctly. Module 03 currently states the weaker
$\lambda_{\max}(\nabla^2 f) \le L$, which fails for the nonconvex functions it then analyses; that
line is scheduled to change.

**The descent-lemma quadratics** that sandwich an $L$-smooth $f$ are

$$
f(x) + \nabla f(x)^\top (y - x) \pm \tfrac{L}{2}\lVert y - x \rVert_2^2 ,
$$

whose second derivative is $\pm L$. Where a module uses the informal word *opening*, it must say
which of the two quantities it names.

**$\mu$** without a constraint index, appearing beside $L$ or $\kappa$, is the strong-convexity
modulus — never a Lagrange multiplier.

---

## Suggested order

The four modules form a chain: each uses the previous one's main result.

1. [`01_derivatives_and_gradients_for_ml/`](01_derivatives_and_gradients_for_ml/) — build the
   derivative objects and the chain rule that produces them at scale.
2. [`02_taylor_approximation_and_local_models/`](02_taylor_approximation_and_local_models/) — turn
   those objects into local models with remainder bounds, and derive the descent lemma.
3. [`03_gradient_descent_mechanics/`](03_gradient_descent_mechanics/) — spend the descent lemma on
   step sizes, stability and convergence rates.
4. [`04_optimization_landscapes_and_convexity/`](04_optimization_landscapes_and_convexity/) — ask
   what the resulting stationary points are, and what convexity buys.

Read `first_principles.ipynb` first in each module, then work `exercises.ipynb`.

If the prerequisites above are unfamiliar, read [`../calculus/`](../calculus/) 09–12 and
[`../linear_algebra/`](../linear_algebra/) 02 and 06 first; the staged order in
[`../docs/prerequisites.md`](../docs/prerequisites.md) places this area after both.

After module 04, continue into [`../optimization/`](../optimization/) for line search, quasi-Newton,
constrained problems, duality, and stochastic methods.

---

## Companion resources

Four files predate the numbered modules and still sit at the area root. They are legacy: no numbered
module depends on them and their theory is superseded. They are kept because three of them hold the
only executed code in this area.

| File | What it actually contains |
|---|---|
| [`derivatives_gradients.md`](derivatives_gradients.md) | A single-page note with no code: derivative and gradient definitions, directional derivatives, Jacobian and chain rule, Hessian and $\kappa$, the least-squares gradient, a four-row matrix-calculus identity table, central-difference checking, subgradients, gradient flow. Superseded by module 01. |
| [`gradient_descent.ipynb`](gradient_descent.ipynb) | 5 code cells, 4 figures, executed with no stored errors. Four experiments on $H = \operatorname{diag}(1, 8)$: the stability boundary, optimal versus sub-optimal step size, a 2D trajectory plot, and a condition-number sweep. No momentum, no stochastic gradients, no schedules, no gradient-flow or implicit-Euler experiment. |
| [`taylor_approximation.ipynb`](taylor_approximation.ipynb) | 5 code cells, 4 figures, executed clean. $e^x$ at $a = 0.5$ against its degree-1 and degree-2 models with their errors, a log-log slope regression recovering orders 2 and 3, $\sin x$ at $a = 1$, and a 2D multivariate expansion on a grid. |
| [`optimization_landscape.ipynb`](optimization_landscape.ipynb) | 5 code cells, 4 figures, executed clean. 3D surfaces for bowl, saddle and maximum; contour plots with Hessian-eigenvalue assertions; gradient descent on the ill-conditioned bowl $x^2 + 8y^2$; two runs near the saddle $x^2 - y^2$, one converging onto it and one escaping after a tiny perturbation. No filter-normalized loss-surface slices and no edge-of-stability experiment. |

Modules 03 and 04 currently promise more of these notebooks than they deliver — module 03 says
`gradient_descent.ipynb` "runs each of these experiments end to end" when it runs four of them, and
module 04 makes a similar claim for `optimization_landscape.ipynb`. Those sentences are wrong and are
being corrected in the module wave. The table above is the accurate inventory.

Applied implementations that consume this area live in the sister repository
[Machine-Learning-from-scratch](https://github.com/hien078/Machine-Learning-from-scratch).

---

## References

Benchmark texts for this area, per [`../CLAUDE.md`](../CLAUDE.md).

**Calculus**

1. **Spivak, M.** *Calculus*, 4th ed. Publish or Perish. — Ch. 9–11 (the derivative, its rules, and
   the significance of the derivative); Ch. 20 (approximation by polynomials: Taylor's theorem with
   Lagrange and Cauchy remainders).
2. **Spivak, M.** *Calculus on Manifolds*. Benjamin. — Ch. 2 (the total derivative, the chain rule,
   the inverse and implicit function theorems).
3. **Apostol, T. M.** *Calculus*, 2nd ed. Wiley. — Vol. I Ch. 7 (polynomial approximation and error
   estimates); Vol. II Ch. 8–9 (differential calculus of scalar and vector fields; implicit functions
   and extremum problems).
4. **Hubbard, J. H., & Hubbard, B. B.** *Vector Calculus, Linear Algebra, and Differential Forms*. —
   Ch. 1 (the derivative as a linear map); Ch. 2 (Newton's method, the inverse and implicit function
   theorems); Ch. 3 (Taylor polynomials in several variables, quadratic forms, and the classification
   of critical points).

**Optimization**

5. **Boyd, S., & Vandenberghe, L.** *Convex Optimization*. Cambridge University Press. — Ch. 2
   (convex sets); Ch. 3 (convex functions, operations preserving convexity, conjugates); Ch. 9
   (unconstrained minimization: descent methods, line search, Newton's method, §9.6
   self-concordance); App. A (matrix calculus).
6. **Nocedal, J., & Wright, S. J.** *Numerical Optimization*, 2nd ed. Springer. — Ch. 2 (Taylor-based
   models and optimality conditions); Ch. 3 (line-search methods, Wolfe conditions, Zoutendijk);
   Ch. 4 (trust regions and the Cauchy point); Ch. 8 (calculating derivatives).
7. **Bertsekas, D. P.** *Nonlinear Programming*, 3rd ed. Athena Scientific. — Ch. 1 (unconstrained
   optimization: gradient methods, rates of convergence, Newton and quasi-Newton).

**Also cited by the modules**

8. **Nesterov, Y.** *Lectures on Convex Optimization*, 2nd ed. Springer. — §1.2 (the class
   $C_L^{1,1}$ and the descent lemma, Lemma 1.2.3); Ch. 2 (lower bounds and accelerated rates).
9. **Goodfellow, I., Bengio, Y., & Courville, A.** *Deep Learning*. MIT Press. — Ch. 4 (numerical
   computation, ill-conditioning, gradient-based optimization); §6.5 (back-propagation); Ch. 8
   (optimization for training deep models).
10. **Polyak, B. T.** (1964). *Some Methods of Speeding up the Convergence of Iteration Methods*.
    USSR Comp. Math. and Math. Physics 4(5). — the heavy-ball method and the $\sqrt{\kappa}$ rate.
11. **Bottou, L., Curtis, F. E., & Nocedal, J.** (2018). *Optimization Methods for Large-Scale
    Machine Learning*. SIAM Review 60(2). — the smoothness-based analysis from GD to SGD.
12. **Baydin, A. G., Pearlmutter, B. A., Radul, A. A., & Siskind, J. M.** (2018). *Automatic
    Differentiation in Machine Learning: a Survey*. JMLR 18(153). — §2–3, forward and reverse mode.
13. **Griewank, A., & Walther, A.** (2008). *Evaluating Derivatives*, 2nd ed. SIAM. — Ch. 12
    (checkpointing and the memory-versus-recompute tradeoff).
14. **Dauphin, Y., et al.** (2014). *Identifying and Attacking the Saddle Point Problem in
    High-Dimensional Non-Convex Optimization*. NeurIPS. — saddle dominance and saddle-free Newton.
15. **Lee, J. D., Simchowitz, M., Jordan, M. I., & Recht, B.** (2016). *Gradient Descent Converges to
    Minimizers*. COLT. — strict-saddle escape under $0 \lt \eta \lt 1/L$.
16. **Dinh, L., Pascanu, R., Bengio, S., & Bengio, Y.** (2017). *Sharp Minima Can Generalize for Deep
    Nets*. ICML. — the reparameterization critique of sharpness measures.
17. **Li, H., Xu, Z., Taylor, G., Studer, C., & Goldstein, T.** (2018). *Visualizing the Loss
    Landscape of Neural Nets*. NeurIPS. — filter normalization and 2D loss-surface slices.
18. **Petersen, K. B., & Pedersen, M. S.** (2012). *The Matrix Cookbook*. — matrix-derivative
    identity tables.
