# Probability & Statistics Foundation

**Status:** Complete & Extended  
**Purpose:** Comprehensive mathematical foundation for stochastic modeling, parameter estimation, Bayesian inference, information theory, stochastic differential equations (SDEs), and AI/machine learning architectures.

---

## Learning Objectives

After working through this foundation, you should be able to:

1. **State and apply** Kolmogorov axioms, conditional probability, and Bayes' theorem.
2. **Handle univariate & multivariate random variables**, joint/marginal/conditional distributions, and Covariance Matrices $\mathbf{\Sigma}$.
3. **Work with the fundamental distribution family**: Bernoulli, Binomial, Poisson, Uniform, Normal, Exponential, Beta, Gamma, and Multivariate Normal.
4. **Compute expectations, variances, moments (via MGFs)**, and master the Law of Large Numbers (LLN) and Central Limit Theorem (CLT).
5. **Formulate and solve parameter estimation problems** using Maximum Likelihood Estimation (MLE) and Maximum A Posteriori (MAP), analyzing estimator bias, variance, and confidence intervals.
6. **Apply Information Theory concepts**: Shannon Entropy, Cross-Entropy Loss, and KL Divergence ($D_{\text{KL}}$).
7. **Model stochastic processes**: Discrete-Time Markov Chains, Poisson processes, Brownian motion, and Stochastic Differential Equations (SDEs).
8. **Bridge probability & statistics to AI/ML**: Connect MLE/MAP to loss functions/regularization, KL divergence to VAEs, and SDEs to generative Diffusion Models.

---

## Prerequisites

| Prerequisite | Why Needed |
|---|---|
| **Calculus** | Multi-variable integration for joint continuous densities, differentiation for MLE |
| **Linear Algebra** | Covariance matrix operations, positive semi-definiteness, eigenvectors of $\mathbf{\Sigma}$ |
| **Set Theory** | Sample spaces, events, $\sigma$-algebras, unions, intersections, complements |

---

## Dependent Topics

This foundation is used directly by:

| Topic | How Probability & Statistics Are Used |
|---|---|
| **Probabilistic Models** | Bayesian inference, stochastic processes, hidden Markov models |
| **Simulation & Monte Carlo** | Random sampling, variance reduction, MCMC, score-based sampling |
| **Model Fitting** | Maximum likelihood estimation, MAP, confidence intervals |
| **Data-Driven Models & ML** | Statistical learning theory, cross-entropy loss, bias-variance tradeoff |
| **Stochastic Dynamical Systems** | Stochastic difference equations, Brownian motion, SDEs |

---

## Contents

| File | Description |
|---|---|
| [`theory.md`](theory.md) | Axioms, Bayes' theorem, multivariate distributions, parameter estimation (MLE/MAP), information theory, SDEs, AI bridge |
| [`computation.ipynb`](computation.ipynb) | Distribution plotting, Monte Carlo $\pi$, CLT demo, Bayes example, random walks |
| [`exercises.md`](exercises.md) | Topic 13 Curriculum Module & 4-Level Exercise Package (L0–L3) with first-principles intuitions & detailed solutions |

---

## How This Connects to Mathematical Modeling and AI

Deterministic models assume perfect knowledge: given initial conditions, the future is determined exactly. But real systems and intelligent agents face:

- **Measurement & Environmental Noise** — state measurements are corrupted by random fluctuations.
- **Inherent Stochasticity** — quantum mechanics, molecular dynamics, individual decision-making.
- **Uncertainty Quantification in AI** — probabilistic predictions, generative modeling, and Bayesian decision theory.

This foundation equips modelers with the mathematical tools to transition from deterministic ODEs to stochastic SDEs, from heuristic loss functions to rigorous Likelihood/Posterior optimization, and from manual heuristics to probabilistic AI principles.

---

## References

- Ross, S. *A First Course in Probability*, 10th Edition.
- Blitzstein, J. K., & Hwang, J. *Introduction to Probability*, 2nd Edition.
- Billingsley, P. *Probability and Measure*, 3rd Edition.
- Feller, W. *An Introduction to Probability Theory and Its Applications*, Volumes 1 & 2.
- Bertsekas, D. & Tsitsiklis, J. *Introduction to Probability*, 2nd Edition.
- Wasserman, L. *All of Statistics: A Concise Course in Statistical Inference*.
- Casella, G., & Berger, R. L. *Statistical Inference*, 2nd Edition.
- Bishop, C. M. *Pattern Recognition and Machine Learning*.
- Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*.
- Cover, T. M., & Thomas, J. A. *Elements of Information Theory*, 2nd Edition.
- Oksendal, B. *Stochastic Differential Equations: An Introduction with Applications*.
