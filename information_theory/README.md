# Foundations of Information Theory — Entropy & Divergence Mastery Curriculum

Welcome to the **Information Theory Mastery Curriculum** under `foundations/information_theory/`.

Information theory quantifies uncertainty, surprise, and the cost of describing one distribution using another — the mathematics that turns "how wrong is this model?" into a precise number of bits. This module provides a comprehensive, first-principles learning system spanning self-information and Shannon entropy, joint and conditional entropy, cross-entropy and the loss functions of modern machine learning, KL divergence and the broader $f$-divergence family, mutual information, and the information-theoretic analysis of deep networks. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** [Calculus](../calculus/), [Linear Algebra](../linear_algebra/), [Probability & Statistics](../probability_statistics/)

---

## 🗺️ Master Index of 6 Information Theory Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Self-Information & Entropy | [`01_self_information_and_entropy/`](01_self_information_and_entropy/) | Surprisal $I(x) = -\log p(x)$, Shannon entropy $H(X)$, axiomatic derivation, bits vs nats, maximum-entropy uniform bound, source coding and Kraft's inequality | 20 |
| **Topic 02** | Joint & Conditional Entropy | [`02_joint_and_conditional_entropy/`](02_joint_and_conditional_entropy/) | Joint entropy $H(X, Y)$, conditional entropy $H(Y \mid X)$, chain rule, subadditivity, conditioning reduces entropy, Fano's inequality, differential entropy | 20 |
| **Topic 03** | Cross-Entropy & Loss Functions | [`03_cross_entropy_and_loss_functions/`](03_cross_entropy_and_loss_functions/) | Cross-entropy $H(P, Q)$, Gibbs' inequality, negative log-likelihood equivalence, softmax and logistic losses, label smoothing, focal loss, calibration | 20 |
| **Topic 04** | KL Divergence & $f$-Divergences | [`04_kl_divergence_and_f_divergences/`](04_kl_divergence_and_f_divergences/) | $D_{\mathrm{KL}}(P \parallel Q) \geq 0$, non-symmetry, forward vs reverse KL mode behaviour, Jensen-Shannon, total variation, Pinsker's inequality, the $f$-divergence family | 20 |
| **Topic 05** | Mutual Information | [`05_mutual_information/`](05_mutual_information/) | $I(X; Y) = H(X) - H(X \mid Y)$, symmetry, KL formulation, data processing inequality, channel capacity, MI estimation (MINE, InfoNCE), feature selection | 20 |
| **Topic 06** | Information Theory in Deep Learning | [`06_information_theory_in_deep_learning/`](06_information_theory_in_deep_learning/) | Information bottleneck, variational bounds and the ELBO, VAEs, $\beta$-VAE rate-distortion tradeoff, contrastive learning, GAN divergence objectives, minimum description length | 20 |
| **TOTAL** | **6 Information Theory Modules** | — | **Complete First-Principles Curriculum** | **120 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `06_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., the axiomatic uniqueness of entropy, Gibbs' inequality, non-negativity of KL divergence, the data processing inequality, the ELBO), Computational and Algorithmic Insights, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## 🔗 Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`entropy_cross_entropy.md`](entropy_cross_entropy.md) | Legacy theory file: Shannon entropy, cross-entropy, and their properties — the seed document the 6 modules expand upon |
| [`kl_divergence.ipynb`](kl_divergence.ipynb) | Executable companion notebook: KL divergence and mutual information demonstrations |
| [`../probability_statistics/`](../probability_statistics/) | Sibling module supplying the distributions, likelihoods, and estimators that entropy and divergence measure |
| [`../optimization/`](../optimization/) | Sibling module providing the maximum-entropy and variational optimization machinery |
| [`../numerical_computing/`](../numerical_computing/) | Sibling module covering the log-sum-exp and stable-softmax tricks that make these quantities computable |

### Used By

- [05 Decision Tree](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/05_decision_tree/README.md) — entropy splitting
- [04 Logistic Regression](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/04_logistic_regression/README.md) — cross-entropy loss
- [13 Neural Networks](https://github.com/hien078/Machine-Learning-from-scratch/blob/master/topics/13_neural_networks/README.md) — loss functions

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy `kl_divergence.ipynb` to see entropy and divergence computed numerically.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Cover, T. M., & Thomas, J. A.** — *Elements of Information Theory*, 2nd Edition (Wiley)
- **MacKay, D. J. C.** — *Information Theory, Inference, and Learning Algorithms* (Cambridge University Press)
- **Shannon, C. E.** — *A Mathematical Theory of Communication* (Bell System Technical Journal, 1948)
- **Tishby, N., Pereira, F. C., & Bialek, W.** — *The Information Bottleneck Method* (1999); **Tishby, N., & Zaslavsky, N.** — *Deep Learning and the Information Bottleneck Principle* (ITW, 2015)
- **Kingma, D. P., & Welling, M.** — *Auto-Encoding Variational Bayes* (ICLR, 2014)
- **van den Oord, A., Li, Y., & Vinyals, O.** — *Representation Learning with Contrastive Predictive Coding* (2018)
- **Csiszár, I., & Shields, P.** — *Information Theory and Statistics: A Tutorial* (now Publishers)
- **Goodfellow, I., Bengio, Y., & Courville, A.** — *Deep Learning*, Chapter 3 (MIT Press)
- **Murphy, K. P.** — *Probabilistic Machine Learning: Advanced Topics* (MIT Press)
