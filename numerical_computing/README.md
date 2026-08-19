# Numerical Computing

Every number a computer stores is an approximation, and every algorithm either tames that
approximation or amplifies it.

This area builds the theory of finite-precision computation from the bit layout upward:
what a floating-point number *is*, how rounding errors compose, which problems are
intrinsically sensitive, how data movement — not arithmetic — sets the runtime, and how the
narrow formats of deep learning break under all four pressures at once.

It is written for readers who already compute — in NumPy, in a training loop, in a solver —
and who need to know why a result is wrong, whether it can be fixed, and what the ceiling on
accuracy was before the first operation ran.

Five modules, `01_` through `05_`, in dependency order. Each is self-contained enough to read
alone once its prerequisites are met.

---

## Prerequisites

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
It is authoritative; the summary below is drawn from it.

At area level this material depends on [`../mathematical_reasoning/`](../mathematical_reasoning/)
— specifically proof technique, and asymptotic reasoning for module 04.

Two modules additionally reach outside the area:

- module 03 needs [`../calculus/`](../calculus/) (single-variable derivatives) and
  [`../linear_algebra/`](../linear_algebra/) (SVD and the pseudoinverse)
- module 04 needs [`../mathematical_reasoning/`](../mathematical_reasoning/) (asymptotics)

Downstream, this area feeds [`../numerical_methods/`](../numerical_methods/),
[`../linear_algebra/`](../linear_algebra/) (iterative solvers) and
[`../calculus_optimization/`](../calculus_optimization/) (gradient-descent conditioning).

---

## Module index

| Module | What it covers | Prerequisites | Problems |
|---|---|---|:---:|
| [`01_ieee754_floating_point_representation/`](01_ieee754_floating_point_representation/) | Bit layout, normalized and subnormal values, $\varepsilon_{\mathrm{mach}}$ versus unit roundoff, ulp, the four IEEE rounding modes, Inf/NaN, exact integer range, Sterbenz, fp16 versus bfloat16 | [`../mathematical_reasoning/03`](../mathematical_reasoning/03_proof_techniques/) | 20 |
| [`02_error_propagation_and_stability_tricks/`](02_error_propagation_and_stability_tricks/) | Forward versus backward error, the $\gamma_n$ calculus, the cancellation bound and digit-loss rule, pairwise and Kahan summation, Fast2Sum, the stable quadratic formula, `log1p`/`expm1`/`hypot`, Welford's variance | [`01`](01_ieee754_floating_point_representation/) | 20 |
| [`03_conditioning_and_condition_numbers/`](03_conditioning_and_condition_numbers/) | Relative condition number, $\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$, the linear-system perturbation theorem, $\kappa(X^\top X) = \kappa(X)^2$ and the normal-equation trap, Wilkinson's digit rule, eigenvalue conditioning, ridge as a conditioning repair, Hilbert matrices | [`02`](02_error_propagation_and_stability_tricks/), [`../calculus/03`](../calculus/03_single_variable_derivatives/), [`../linear_algebra/07`](../linear_algebra/07_canonical_forms_and_svd/) | 20 |
| [`04_vectorization_and_numpy_performance/`](04_vectorization_and_numpy_performance/) | Strides and contiguity, views versus copies, broadcasting and the temporaries it materializes, ufuncs, BLAS levels 1–3 and arithmetic intensity, the roofline, cache blocking and the Hong–Kung bound, `einsum` contraction order, benchmarking methodology | [`01`](01_ieee754_floating_point_representation/), [`../mathematical_reasoning/06`](../mathematical_reasoning/06_asymptotics_and_algorithmic_reasoning/) | 20 |
| [`05_numerical_stability_in_deep_learning/`](05_numerical_stability_in_deep_learning/) | Format ranges from fp32 down to fp8, the log-sum-exp theorem and its error bound, fused cross-entropy from logits, loss scaling, mixed precision with fp32 master weights, normalization numerics, Adam's $\epsilon$ as a conditioning cap, vanishing and exploding gradients, gradient clipping | [`03`](03_conditioning_and_condition_numbers/), [`04`](04_vectorization_and_numpy_performance/) | 20 |
| **Total** | **5 modules** | — | **100** |

Counts come from `python3 tools/curriculum_stats.py --modules`. Every module holds exactly
20 solved problems in 4 tiers.

Two topics are easy to look for in the wrong place:

- **Reproducibility and reduction order** is module 01 §5.4, not module 05.
- **The log-sum-exp identity** is proved with its error bound in module 05 (Theorem 2.2,
  Derivation 3.2). Module 02 §5.2 states it as an application and defers the proof.

---

## Module architecture

Every numbered folder holds exactly three files, as fixed by
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20.

| File | Contract |
|---|---|
| `README.md` | Overview, a `> [!NOTE]` with the module's single most important result, prerequisites and downstream links, learning outcomes, a Mermaid concept map, a notation table, a core-results table, misconceptions, an exercise index matching the notebook, and chapter-level references |
| `first_principles.ipynb` | Theory in the WHY → INTUITION → DEFINITION → DERIVATION → APPLICATION order, executable code cells verifying each major theorem, 2–4 figures showing the geometry of the central idea, and a closing **Key Takeaways** cell |
| `exercises.ipynb` | 20 fully solved problems in four tiers, each carrying statement, intuition, full derivation, a `$$\boxed{...}$$` answer, and a key takeaway |

The four tiers are the same in every module of the repository.

| Tier | Contract | Problems per module |
|---|---|:---:|
| L0 | Concept checks | 4 |
| L1 | Foundations | 6 |
| L2 | AI/ML and physics applications | 6 |
| L3 | Challenge proofs | 4 |

Every notebook opens with a Google Colab badge, so it can be read on GitHub and run in Colab
without a local install.

### What is not built yet

> [!IMPORTANT]
> **The upgrade has not reached this area yet.** All ten notebooks here are still markdown-only:
> no code cells, no figures, and no `Key Takeaways` cell — each `first_principles.ipynb` currently
> ends at its literature-mapping section. Until a module reports `PASS` from
> `python3 tools/check_module.py`, read the numbers in it as asserted, not as verified.

Two further gaps, recorded so they are not mistaken for the standard:

- Several derivations carry commented-out Python inside fenced blocks in markdown cells.
  §18 forbids this; those blocks become real code cells in the same wave.
- The L2 heading in the notebooks reads *Applications in AI/ML*, dropping the physics half of
  the tier name §20 fixes. The heading is what changes, not the tier.

---

## Notation

The repository-wide register is [`../docs/notation.md`](../docs/notation.md), which is
authoritative on symbols. The rulings that bind this area:

| Symbol | Meaning | Value for binary64 |
|---|---|---|
| $t$ | significand bits, **including** the hidden bit | $t = 53$ |
| $u = 2^{-t}$ | unit roundoff | $2^{-53} \approx 1.11 \times 10^{-16}$ |
| $\varepsilon_{\mathrm{mach}} = 2u$ | gap between $1$ and the next float | $2^{-52} \approx 2.22 \times 10^{-16}$ |
| $\operatorname{ulp}(x) = 2^{e - t + 1}$ | unit in the last place at exponent $e$ | |
| $\gamma_n = nu/(1 - nu)$ | accumulated rounding factor, defined for $nu \lt 1$ | |
| $\kappa(A) = \Vert A \Vert \, \Vert A^{-1} \Vert$ | condition number; subscript the norm when it matters | $\kappa_2 = \sigma_{\max}/\sigma_{\min}$ |
| $d$ | decimal digits of precision | $u \approx 10^{-d}$ |
| $q$ | operand count in an `einsum`-style expression | |

Three conventions this area fixes, following Higham:

- The rounding axiom is $\operatorname{fl}(x \circ y) = (x \circ y)(1 + \delta)$ with
  $\lvert \delta \rvert \le u$, valid when $x \circ y$ neither overflows nor underflows.
- Machine epsilon and unit roundoff are **different quantities** differing by a factor of two.
  Anything writing $\varepsilon_{\mathrm{mach}} = 2^{-53}$ is wrong.
- The letter $p$ is **retired** in this area. It carried four incompatible meanings across the
  five modules; significand length is $t$, decimal digits are $d$, operand count is $q$.

> [!NOTE]
> The notebooks have not yet been migrated to these rulings. Modules 01 and 05 still use $p$
> for quantities that differ by one bit. Read the register, not the notebooks, when the two
> disagree.

---

## Suggested order

1. **[`01`](01_ieee754_floating_point_representation/) — IEEE 754.** The axiom every later
   module quotes. Nothing else here makes sense without $\operatorname{fl}(x) = x(1+\delta)$.
2. **[`02`](02_error_propagation_and_stability_tricks/) — Error propagation.** Turns the axiom
   into a calculus, and blames the *algorithm* when an answer is wrong.
3. **[`03`](03_conditioning_and_condition_numbers/) — Conditioning.** Blames the *problem*.
   The master identity, forward error $\lesssim$ condition number $\times$ backward error,
   joins the two verdicts.
4. **[`04`](04_vectorization_and_numpy_performance/) — Vectorization.** Independent of 02 and
   03; readable straight after 01 if speed is the immediate question.
5. **[`05`](05_numerical_stability_in_deep_learning/) — Deep learning.** Applies all four at
   once, in arithmetic where $u$ is $2^{-8}$ rather than $2^{-53}$.

A reader who only wants the accuracy story can stop after 03. A reader who only wants the
performance story can read 01 then 04.

---

## Companion resources

Three files sit at the area root, outside every numbered module. They **predate** the
numbered curriculum, are shallower than the modules that replaced them, and are not
maintained against them. [`../docs/prerequisites.md`](../docs/prerequisites.md) lists them as
outside the dependency graph: no numbered module may depend on one.

| Legacy file | What it actually contains |
|---|---|
| [`floating_point_stability.md`](floating_point_stability.md) | A one-page note: the rounding model, the conditioning-versus-stability distinction, $\kappa_2(A) = \sigma_{\max}/\sigma_{\min}$, the normal-equation remark, a bullet list of stable ML patterns, and the stable-softmax formula. No bit layout, no derivations, no exercises. Modules 01–03 and 05 supersede all of it. |
| [`conditioning_stability.ipynb`](conditioning_stability.ipynb) | Four cells, two of them code. One experiment: a cubic monomial fit on $x \in [0.99, 1.01]$, printing $\kappa(X)$, $\kappa(X^\top X)$, and the solution error of `lstsq` against the normal equations. It imports matplotlib but draws no figure. Module 03 Derivation 3.4 is the same experiment with a proof attached. |
| [`vectorization_numpy.ipynb`](vectorization_numpy.ipynb) | Four cells, two of them code. Times a Python-loop matrix–vector product against `X @ w` on a $2000 \times 20$ matrix, then asserts the two agree. **It is not a benchmark**: a single untimed-warm-up `perf_counter` pair, no repeats and no minimum — the exact methodology module 04 Problem L2.6 rejects. Treat the equality assertion as its only reliable output. |

Related areas:

- [`../numerical_methods/`](../numerical_methods/) applies this error analysis to root
  finding, interpolation, quadrature and linear solvers.
- [`../linear_algebra/`](../linear_algebra/) supplies the norms, SVD and factorizations behind
  the condition number.
- [`../optimization/`](../optimization/) and
  [`../calculus_optimization/`](../calculus_optimization/) are where conditioning turns into a
  convergence rate.

---

## References

Benchmarks for this area, per [`../CLAUDE.md`](../CLAUDE.md): Trefethen & Bau; Higham,
*Accuracy and Stability*; Heath.

**Core**

- **Higham, N. J.** (2002). *Accuracy and Stability of Numerical Algorithms* (2nd ed.). SIAM.
  Ch. 1–2 (finite-precision principles, the rounding model), Ch. 3 (the $\gamma_n$ calculus),
  Ch. 4 (summation, incl. Thm 4.8 for compensated summation), Ch. 6–7 (norms and perturbation
  theory for linear systems), Ch. 13 (blocked algorithms), Ch. 20 (least squares).
- **Trefethen, L. N., & Bau, D.** (1997). *Numerical Linear Algebra*. SIAM.
  Lecture 12 (conditioning), Lecture 13 (floating-point arithmetic), Lectures 14–15
  (stability, backward stability), Lectures 18–19 (conditioning and stability of least squares).
- **Heath, M. T.** (2018). *Scientific Computing: An Introductory Survey* (rev. 2nd ed.). SIAM.
  Ch. 1 (approximations, computer arithmetic, conditioning and stability), Ch. 2 §2.3 (norms
  and the condition number of a linear system), Ch. 3 (linear least squares, normal equations
  versus QR).

**Floating point in detail**

- **Goldberg, D.** (1991). *What Every Computer Scientist Should Know About Floating-Point
  Arithmetic*. ACM Computing Surveys, 23(1), 5–48. §1–3: formats, guard digits, cancellation.
- **IEEE Computer Society** (2019). *IEEE Standard for Floating-Point Arithmetic*
  (IEEE 754-2019). Clauses 3–4 (formats, rounding), Clause 7 (exceptions).
- **Muller, J.-M., et al.** (2018). *Handbook of Floating-Point Arithmetic* (2nd ed.).
  Birkhäuser. Ch. 2–3 (formats), Ch. 4 (error-free transformations), Ch. 12 (correctly rounded
  elementary functions).

**Conditioning and linear algebra**

- **Golub, G. H., & Van Loan, C. F.** (2013). *Matrix Computations* (4th ed.). Johns Hopkins.
  §1.1–1.5 (BLAS levels, blocking, data reuse), §2.6–2.7 (sensitivity), §5.3 (least squares).
- **Demmel, J. W.** (1997). *Applied Numerical Linear Algebra*. SIAM. Ch. 2: perturbation theory.
- **Wilkinson, J. H.** (1963). *Rounding Errors in Algebraic Processes*. Prentice-Hall.

**Performance**

- **Williams, S., Waterman, A., & Patterson, D.** (2009). *Roofline: an insightful visual
  performance model for multicore architectures*. Communications of the ACM, 52(4), 65–76.
- **Goto, K., & van de Geijn, R. A.** (2008). *Anatomy of high-performance matrix
  multiplication*. ACM TOMS, 34(3). Packing, blocking, and the micro-kernel.
- **Harris, C. R., et al.** (2020). *Array programming with NumPy*. Nature, 585, 357–362.
  The strided-array model, ufuncs, broadcasting.

**Low precision**

- **Micikevicius, P., et al.** (2018). *Mixed Precision Training*. ICLR. Master weights, loss
  scaling, fp32 accumulation.
- **Micikevicius, P., et al.** (2022). *FP8 Formats for Deep Learning*. arXiv:2209.05433.
  E4M3 and E5M2 definitions, per-tensor scaling.
- **Higham, N. J., & Mary, T.** (2022). *Mixed precision algorithms in numerical linear
  algebra*. Acta Numerica, 31, 347–414.
