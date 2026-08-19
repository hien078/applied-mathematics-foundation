# Probability and Statistics

This area builds probability from the Kolmogorov axioms up to Bayesian inference, in ten
modules that are meant to be read in order.

The route is the one the benchmark texts take. A probability space is constructed, random
variables are defined as measurable maps, the canonical discrete and continuous families are
derived rather than tabulated, expectation and its inequalities are proved, the multivariate
normal is developed as the one fully tractable multivariate family, the limit theorems are
proved from characteristic functions, and estimation is carried from maximum likelihood
through MAP to the full posterior.

It is written for a reader who wants to be able to *check* a probabilistic claim, not merely
recognize it: someone doing machine-learning research, mathematical modeling, or physics who
needs the hypotheses of a theorem, not its slogan. Theorems are stated with their hypotheses
and the exercises are fully solved, statement through boxed answer.

The scope is deliberately bounded, and two boundaries matter. This area develops probability
and estimation; it does **not** develop frequentist hypothesis testing, nonparametric
inference, or stochastic processes. It also works at the level of Wasserman and Casella &
Berger, not at the measure-theoretic construction level of Durrett — the existence side of
measure theory is used, not built.

> [!NOTE]
> Not covered anywhere in this area, and not claimed by it: the Neyman–Pearson lemma, size
> and power, $p$-values, UMP tests, the empirical CDF, Glivenko–Cantelli, the DKW inequality,
> the bootstrap, Markov chains, martingales, and Brownian motion. Confidence intervals appear
> only as the Wald interval in module 09 and as credible intervals in module 10.

---

## Prerequisites

The authoritative dependency graph for all 87 modules in this repository is
[`../docs/prerequisites.md`](../docs/prerequisites.md). The per-module column in the index
below is taken from it.

At area level this one depends on three others:

- [`../mathematical_reasoning/`](../mathematical_reasoning/) — set algebra, proof technique, and counting, for module 01.
- [`../calculus/`](../calculus/) — integration, improper integrals and the Gamma function, series, Taylor expansion, the Hessian, and multiple integrals with a Jacobian.
- [`../linear_algebra/`](../linear_algebra/) — the spectral theorem and positive semidefiniteness, for the covariance matrix in module 07.

What it unlocks:

- [`../information_theory/`](../information_theory/) — entropy, cross-entropy and KL divergence rest on modules 06, 07, 09 and 10.
- [`../optimization/08_stochastic_optimization_for_ml/`](../optimization/08_stochastic_optimization_for_ml/) — stochastic gradient methods use the LLN and CLT from module 08.

---

## Module index

Ten modules, 200 fully solved problems. In-area prerequisites are given by module number;
cross-area prerequisites name the area.

| Module | What it covers | Prerequisites | Problems |
| :--- | :--- | :--- | ---: |
| [01 Sample spaces and probability axioms](01_sample_spaces_and_probability_axioms/) | Sample space, $\sigma$-algebra, Kolmogorov axioms, countable additivity, inclusion–exclusion, Boole's union bound, continuity of measure | [reasoning 02](../mathematical_reasoning/02_sets_relations_and_functions/), [reasoning 05](../mathematical_reasoning/05_combinatorics_and_counting/) | 20 |
| [02 Conditional probability and Bayes](02_conditional_probability_and_bayes/) | Conditioning as restrict-and-renormalize, chain rule, law of total probability, Bayes' theorem, odds and log-odds form, independence versus conditional independence, explaining away | 01 | 20 |
| [03 Random variables and distribution functions](03_random_variables_and_distribution_functions/) | Measurability, the pushforward law, characterization of CDFs, PMF and PDF, quantile function, inverse-transform sampling, probability integral transform, change of variables | [calculus 05](../calculus/05_indefinite_and_definite_integrals/), 02 | 20 |
| [04 Discrete distributions](04_discrete_distributions/) | Bernoulli, Binomial, Geometric, Negative Binomial, Poisson, categorical and multinomial; discrete memorylessness, the Poisson limit theorem, Le Cam's bound, generating functions, thinning and Gamma mixing | [calculus 08](../calculus/08_sequences_series_convergence/), 03 | 20 |
| [05 Continuous distributions](05_continuous_distributions/) | Uniform, Exponential, Gamma, Beta, Normal, Laplace, Student's $t$, Cauchy, Lognormal, Weibull; hazard functions, memorylessness and maximum-entropy characterizations, Gamma-to-Beta, $t$ as a Gaussian scale mixture | [calculus 07](../calculus/07_improper_integrals_special_functions/), 03 | 20 |
| [06 Expectation, variance and moments](06_expectation_variance_and_moments/) | Expectation as an integral, linearity without independence, LOTUS, tail formula, covariance and correlation, moments and cumulants, generating and characteristic functions, Jensen, Markov, Chebyshev, Chernoff, conditional expectation, tower property, law of total variance | [calculus 09](../calculus/09_taylor_and_power_series/), 04, 05 | 20 |
| [07 Joint distributions and the multivariate normal](07_joint_distributions_and_multivariate_normal/) | Joint, marginal and conditional densities, covariance matrix $\Sigma \succeq 0$, the four Gaussian identities, Schur-complement conditioning, precision matrix and conditional independence, whitening and PCA, Mahalanobis distance, Sklar's theorem and copulas | [calculus 13](../calculus/13_multiple_integrals_coordinate_transforms/), [linear algebra 06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/), 06 | 20 |
| [08 Law of large numbers and the CLT](08_law_of_large_numbers_and_clt/) | Three modes of convergence, Markov and Chebyshev, weak and strong LLN, characteristic functions, Lévy continuity, Lindeberg–Lévy CLT, Berry–Esseen, Slutsky, delta method, Monte Carlo error budget | [calculus 09](../calculus/09_taylor_and_power_series/), 06 | 20 |
| [09 Maximum likelihood and MAP estimation](09_maximum_likelihood_and_map_estimation/) | Likelihood, MLE and its invariance, score function, Fisher information, Cramér–Rao bound, consistency via KL divergence, asymptotic normality, MAP as penalized likelihood, exponential families, Fisher–Neyman factorization, EM | [calculus 12](../calculus/12_hessian_jacobian_curvature/), 07, 08 | 20 |
| [10 Bayesian inference](10_bayesian_inference/) | Bayes' theorem for densities, evidence, posterior predictive, credible sets, conjugate families and exponential-family conjugacy, Jeffreys prior, Bayes estimators under loss, Bayes factors, Bernstein–von Mises, the ELBO, Metropolis–Hastings | 05, 09 | 20 |

Counts are produced by `python3 tools/curriculum_stats.py --modules`, not written by hand.

---

## Module architecture

Every numbered directory holds exactly the three files that
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20 requires.

| File | Contract |
| :--- | :--- |
| `README.md` | Overview, a `> [!NOTE]` headline result, prerequisites and downstream links, learning outcomes, Mermaid concept map, notation table, core results table, common misconceptions, exercise index, references |
| `first_principles.ipynb` | Theory in the order intuition, definition, theorem, derivation, interpretation, application; executable code cells verifying each major theorem; 2 to 4 figures; a closing **Key Takeaways** cell |
| `exercises.ipynb` | 20 fully solved problems in four tiers, each with statement, intuition, derivation, a `$$\boxed{...}$$` answer, and a key takeaway |

The four exercise tiers are fixed by §20 and are the same in all ten modules:

- **L0** — concept checks
- **L1** — foundations
- **L2** — AI/ML and physics applications
- **L3** — challenge proofs

Every notebook opens with a Google Colab badge, so it can be read on GitHub and run in the
browser.

### Current state, stated plainly

The table above is the contract, not a full description of what is on disk today. Every module
carries a handful of verification code cells now (critical numeric claims from the audit were
fixed and checked in code), but not the full six-cell / two-to-four-figure contract yet. Run
`python3 tools/check_module.py --all --failing` for the modules that still fall short, and
`python3 tools/curriculum_stats.py --modules` for the live code-cell and figure counts.

No `first_principles.ipynb` ends with the required **Key Takeaways** cell; each currently ends
at its references section.

Every module `README.md` still uses an older six-section template and so omits four items
§20 requires: prerequisites and downstream links, learning outcomes, a notation table, and a
core results table. None of the ten contains a single relative link to a sibling module.

An upgrade wave is closing all three — adding the Binomial-to-Poisson total-variation curve
for 04, the hazard-function panel for 05, the Welford cancellation demo for 06, the confidence
ellipse for 07, the running-mean envelope for 08, and the MCMC trace with $\hat{R}$ for 10.

Until it lands, the only executable probability code in this area is the legacy
`computation.ipynb` at the area root, described under Companion resources.

---

## Notation

Symbols are fixed repository-wide by [`../docs/notation.md`](../docs/notation.md). Where a
module here contradicts it, the module is what changes.

Six rulings bind this area in particular:

| Symbol | Meaning | Ruling |
| :--- | :--- | :--- |
| $\mathbb{P}$ | probability measure | the letter $P$ alone is not the measure |
| $(n)_k$ | falling factorial, ordered selections | never $P(n, k)$, which collides with the measure |
| $\mathcal{N}(\mu, \Sigma)$ | Gaussian | the second argument is the **covariance**, never the precision |
| $\Sigma^{-1}$ or $\Theta$ | precision matrix | $\Lambda$ is reserved for the eigenvalue diagonal |
| $I(\theta)$ | Fisher information | distinct from mutual information $I(X; Y)$ |
| $d_{\mathrm{TV}}$ | total variation distance | $d_{\mathrm{TV}}(p, q) = \tfrac{1}{2}\lVert p - q \rVert_1$; the factor 2 is not optional |

Two further conventions:

Conditioning is written with `\mid`, so a conditional probability is $\mathbb{P}(A \mid B)$.

The Negative Binomial convention is named every time it is used. Modules 04 and 10 use
different ones — trials to the $r$-th success on $\lbrace r, r+1, \ldots \rbrace$, and
failures before the $r$-th success on $\lbrace 0, 1, 2, \ldots \rbrace$ — and only the second
admits non-integer $r$.

---

## Suggested order

The dependency graph is close to a chain and reading it straight through works:

1. **01 → 02 → 03.** The probability space, conditioning, and the random variable. Nothing later parses without these.
2. **04 and 05, in either order.** The discrete and continuous families. Both need 03; neither needs the other.
3. **06.** Expectation, moments and the tail inequalities. Needs both 04 and 05.
4. **07 and 08, in either order.** The multivariate normal and the limit theorems. Both need 06.
5. **09.** Estimation. Needs 07 for the multivariate score and 08 for asymptotic normality.
6. **10.** The posterior. Needs 09, and 05 for the conjugate families.

A reader who only wants the machinery behind a maximum-likelihood loss can take
01 → 02 → 03 → 05 → 06 → 08 → 09 and skip 04, 07 and 10.

---

## Companion resources

Three legacy files sit at the area root. They predate the numbered modules, they are **not**
maintained to `STYLE_GUIDE.md`, and the ten module directories supersede them. They are kept
because two of them still contain material the modules do not.

| File | What it actually contains |
| :--- | :--- |
| [`first_principles.md`](first_principles.md) | A 565-line single-file theory document in nine sections: axioms, conditional probability and Bayes, random variables, distribution families, expectation and limit theorems, parameter estimation, information theory, stochastic processes and SDEs, and an AI bridge. Sections 1–6 are superseded by modules 01–10. Sections 7 and 8 have no counterpart in the numbered modules |
| [`exercises.md`](exercises.md) | A 1,302-line legacy exercise set: 37 solved problems split 7 / 8 / 12 / 10 across four levels whose names differ from the L0–L3 tiers used in the modules. Fully superseded by the 200 problems in `exercises.ipynb` |
| [`computation.ipynb`](computation.ipynb) | The only runnable probability code in this area: 23 cells, 11 of them code, with 10 stored figures. Covers a distribution gallery, a Bayes medical-test calculator, a rejection-sampling check of conditional probability, Monte Carlo $\pi$, LLN and CLT demonstrations, random walks, a three-state Markov-chain weather model, MLE from scratch for the normal and exponential, and exponential memorylessness. It uses NumPy, SciPy and Matplotlib from `requirements.txt`. It is organised by theme rather than by module and does not follow the computational contract in `STYLE_GUIDE.md` §21 |

---

## References

The benchmark texts for this area are the four named in
[`../CLAUDE.md`](../CLAUDE.md), mapped to where each is actually used.

| Text | Chapters | Where it is the benchmark |
| :--- | :--- | :--- |
| Wasserman, *All of Statistics* | 1–2 | Modules 01–03: probability, random variables |
| Wasserman, *All of Statistics* | 3 | Module 06: expectation, variance, moment generating functions |
| Wasserman, *All of Statistics* | 4–5 | Module 08: inequalities, convergence, LLN and CLT |
| Wasserman, *All of Statistics* | 9 | Module 09: parametric inference, the delta method, MLE |
| Wasserman, *All of Statistics* | 11 | Module 10: Bayesian inference |
| Casella & Berger, *Statistical Inference*, 2nd ed. | 1–2 | Modules 01, 03: probability theory, transformations and expectations |
| Casella & Berger, *Statistical Inference*, 2nd ed. | 3 | Modules 04–05: common families of distributions |
| Casella & Berger, *Statistical Inference*, 2nd ed. | 4 | Module 07: multiple random variables, covariance, hierarchical models |
| Casella & Berger, *Statistical Inference*, 2nd ed. | 5–7 | Modules 06, 08, 09: sampling distributions, principles of data reduction, point estimation |
| Bishop, *Pattern Recognition and Machine Learning* | 1.2, 2.1–2.3 | Modules 02, 05, 07: probability for ML, distributions, the Gaussian in depth |
| Bishop, *Pattern Recognition and Machine Learning* | 2.4, 9–10 | Modules 09–10: exponential families, EM, variational inference |
| Durrett, *Probability: Theory and Examples*, 5th ed. | 1–3 | Modules 01, 03, 08: measure-theoretic foundations, laws of large numbers, central limit theorems |

Two honest caveats on that table.

Durrett is the stated benchmark but the current content does not reach it: Carathéodory
extension, the $\pi$–$\lambda$ theorem, Fubini–Tonelli, and the Radon–Nikodym construction of
conditional expectation are used or assumed in this area, never built. Read Durrett Ch. 1–2
alongside module 01 if you need the construction rather than the calculus.

Casella & Berger Ch. 8–9 and Wasserman Ch. 7–8, 10 — hypothesis testing, interval
estimation, the empirical CDF and the bootstrap — have no counterpart here, as the note above
the module index states. Casella & Berger Ch. 10 is covered only in part: module 09 has the
asymptotic efficiency of the MLE but none of the testing results built on it.

Individual module `README.md` files cite further texts at chapter precision, including
Blitzstein & Hwang, Gelman et al. *Bayesian Data Analysis* 3rd ed., Murphy, Feller, and
Boucheron, Lugosi & Massart.
