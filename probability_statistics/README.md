# Foundations of Probability & Statistics — Probability Mastery Curriculum

Welcome to the **Probability & Statistics Mastery Curriculum** under `foundations/probability_statistics/`.

This module provides a comprehensive, first-principles learning system spanning the Kolmogorov axioms, conditional probability and Bayes' theorem, random variables and their distribution functions, the canonical discrete and continuous distribution families, expectation/variance/moment machinery, joint distributions and the multivariate normal, the limit theorems (LLN and CLT), and the estimation hierarchy from maximum likelihood through MAP to full Bayesian inference. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/)

---

## 🗺️ Master Index of 10 Probability & Statistics Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Sample Spaces & Probability Axioms | [`01_sample_spaces_and_probability_axioms/`](01_sample_spaces_and_probability_axioms/) | Sample space $\Omega$, events, $\sigma$-algebras, Kolmogorov axioms, countable additivity, inclusion-exclusion, continuity of measure | 20 |
| **Topic 02** | Conditional Probability & Bayes' Theorem | [`02_conditional_probability_and_bayes/`](02_conditional_probability_and_bayes/) | $P(A \mid B)$, chain rule, law of total probability, Bayes' theorem, independence vs conditional independence, base-rate reasoning | 20 |
| **Topic 03** | Random Variables & Distribution Functions | [`03_random_variables_and_distribution_functions/`](03_random_variables_and_distribution_functions/) | Measurable maps, CDF axioms, PMF/PDF, quantile function, transformations, inverse-CDF sampling, mixed distributions | 20 |
| **Topic 04** | Discrete Distributions | [`04_discrete_distributions/`](04_discrete_distributions/) | Bernoulli, Binomial, Geometric, Negative Binomial, Hypergeometric, Poisson, Poisson limit theorem, categorical models | 20 |
| **Topic 05** | Continuous Distributions | [`05_continuous_distributions/`](05_continuous_distributions/) | Uniform, Exponential memorylessness, Gaussian, Gamma, Beta, Chi-square, Student-$t$, conjugate families | 20 |
| **Topic 06** | Expectation, Variance & Moments | [`06_expectation_variance_and_moments/`](06_expectation_variance_and_moments/) | LOTUS, linearity, variance decomposition, covariance, moment generating functions, skewness/kurtosis, tail bounds | 20 |
| **Topic 07** | Joint Distributions & the Multivariate Normal | [`07_joint_distributions_and_multivariate_normal/`](07_joint_distributions_and_multivariate_normal/) | Joint/marginal/conditional densities, covariance matrix $\mathbf{\Sigma} \succeq 0$, Gaussian conditioning, Mahalanobis distance, whitening | 20 |
| **Topic 08** | Law of Large Numbers & the CLT | [`08_law_of_large_numbers_and_clt/`](08_law_of_large_numbers_and_clt/) | Modes of convergence, Markov/Chebyshev, weak and strong LLN, characteristic functions, Lindeberg-Lévy CLT, delta method | 20 |
| **Topic 09** | Maximum Likelihood & MAP Estimation | [`09_maximum_likelihood_and_map_estimation/`](09_maximum_likelihood_and_map_estimation/) | Likelihood and log-likelihood, score function, Fisher information, Cramér-Rao bound, asymptotic normality, MAP as regularized MLE | 20 |
| **Topic 10** | Bayesian Inference | [`10_bayesian_inference/`](10_bayesian_inference/) | Posterior $p(\theta \mid \mathcal{D})$, conjugate priors, evidence and model comparison, credible intervals, posterior predictive, MCMC and variational bounds | 20 |
| **TOTAL** | **10 Probability & Statistics Modules** | — | **Complete First-Principles Curriculum** | **200 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `10_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., Bayes' theorem, Chebyshev's inequality, the Lindeberg-Lévy CLT, Cramér-Rao lower bound), Computational and Algorithmic Insights, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## 🎯 Learning Objectives

After working through this curriculum you should be able to:

1. **State and apply** the Kolmogorov axioms, conditional probability, and Bayes' theorem.
2. **Handle univariate and multivariate random variables**, joint/marginal/conditional distributions, and covariance matrices $\mathbf{\Sigma}$.
3. **Work fluently with the fundamental distribution family**: Bernoulli, Binomial, Poisson, Uniform, Normal, Exponential, Beta, Gamma, and the Multivariate Normal.
4. **Compute expectations, variances and moments** (via MGFs) and master the Law of Large Numbers and the Central Limit Theorem.
5. **Formulate and solve parameter-estimation problems** using MLE and MAP, analysing estimator bias, variance, and confidence intervals.
6. **Bridge probability to AI/ML**: connect MLE/MAP to loss functions and regularization, KL divergence to variational autoencoders, and stochastic processes to diffusion models.

---

## 🔗 Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`first_principles.md`](first_principles.md) | Legacy master theory file: axioms, Bayes' theorem, multivariate distributions, parameter estimation (MLE/MAP), information theory, stochastic processes and SDEs, plus the AI bridge — the seed document the 10 modules expand upon |
| [`exercises.md`](exercises.md) | Legacy 4-level exercise package (L0–L3) with first-principles intuitions and detailed solutions |
| [`computation.ipynb`](computation.ipynb) | Executable companion notebook: distribution plotting, Monte Carlo estimation of $\pi$, CLT demonstration, worked Bayes example, random walks |
| [`../information_theory/`](../information_theory/) | Sibling module developing entropy, cross-entropy and KL divergence — the information-theoretic view of the likelihoods built here |
| [`../numerical_methods/`](../numerical_methods/) | Sibling module covering Monte Carlo integration and numerical quadrature used to evaluate intractable expectations |
| [`../optimization/`](../optimization/) | Sibling module supplying the optimization machinery behind MLE, MAP, and variational inference |

### Used By

This foundation is used directly by:

| Downstream Topic | How Probability & Statistics Are Used |
|---|---|
| **Probabilistic Models** | Bayesian inference, stochastic processes, hidden Markov models |
| **Simulation & Monte Carlo** | Random sampling, variance reduction, MCMC, score-based sampling |
| **Model Fitting** | Maximum likelihood estimation, MAP, confidence intervals |
| **Data-Driven Models & ML** | Statistical learning theory, cross-entropy loss, bias-variance tradeoff |
| **Stochastic Dynamical Systems** | Stochastic difference equations, Brownian motion, SDEs |

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy `computation.ipynb` to see the distributions and estimators executing numerically.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Wasserman, L.** — *All of Statistics: A Concise Course in Statistical Inference* (Springer)
- **Casella, G., & Berger, R. L.** — *Statistical Inference*, 2nd Edition (Duxbury)
- **Blitzstein, J. K., & Hwang, J.** — *Introduction to Probability*, 2nd Edition (CRC Press)
- **Bishop, C. M.** — *Pattern Recognition and Machine Learning* (Springer)
- **Murphy, K. P.** — *Probabilistic Machine Learning: An Introduction* & *Advanced Topics* (MIT Press)
- **Gelman, A., Carlin, J., Stern, H., Dunson, D., Vehtari, A., & Rubin, D.** — *Bayesian Data Analysis*, 3rd Edition (CRC Press)
- **Durrett, R.** — *Probability: Theory and Examples*, 5th Edition (Cambridge University Press)
- **Ross, S.** — *A First Course in Probability*, 10th Edition (Pearson)
- **Billingsley, P.** — *Probability and Measure*, 3rd Edition (Wiley)
- **Feller, W.** — *An Introduction to Probability Theory and Its Applications*, Volumes 1 & 2 (Wiley)
- **Bertsekas, D. P., & Tsitsiklis, J. N.** — *Introduction to Probability*, 2nd Edition (Athena Scientific)
- **Cover, T. M., & Thomas, J. A.** — *Elements of Information Theory*, 2nd Edition (Wiley)
- **Øksendal, B.** — *Stochastic Differential Equations: An Introduction with Applications* (Springer)
- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*, Chapters 3 and 5 (MIT Press)
