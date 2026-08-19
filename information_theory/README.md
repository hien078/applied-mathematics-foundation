# Information Theory

Information theory measures uncertainty in bits. It begins with one question — how surprised
should you be by an outcome of probability $p$? — and answers it with a single function,
$-\log p$, forced by three axioms rather than chosen for convenience.

Everything after that is bookkeeping on that one quantity. Averaging it gives entropy.
Averaging it under the wrong model gives cross-entropy. The gap between the two is KL
divergence, and the KL between a joint distribution and the product of its marginals is
mutual information.

Those four numbers are the training objective of almost every classifier, language model,
variational autoencoder and contrastive encoder in use today. This area exists so that you
can derive them, bound them, and say exactly what each one costs — not merely recite the
definitions.

It is written for a reader who has finished basic probability and single-variable calculus,
and who wants to read a VAE loss, an InfoNCE objective or an RLHF KL penalty as
information-theoretic quantities with known limits.

---

## Prerequisites

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
Every module row below is drawn from it.

This area depends on three others:

- [`../probability_statistics/`](../probability_statistics/) — expectation, joint distributions,
  the multivariate normal, maximum likelihood, and Bayesian posteriors. This is the hard
  prerequisite: entropy is an expectation, and every theorem here is a statement about one.
- [`../calculus/`](../calculus/) — Jensen's inequality, concavity, and constrained optimization
  of a smooth objective.
- [`../optimization/`](../optimization/) — convexity certificates for Module 04, and stochastic
  optimization for Module 06.

Nothing in this area is a prerequisite for another area.

---

## Module index

Problem counts are produced by `python3 tools/curriculum_stats.py --modules`, not from memory.

| Module | What it covers | Prerequisites | Problems |
| :--- | :--- | :--- | :---: |
| [`01_self_information_and_entropy/`](01_self_information_and_entropy/) | Surprisal $-\log p(x)$, Shannon entropy, bits versus nats, the bound $H(X) \le \log K$ by Jensen, concavity, $H(g(X)) \le H(X)$, differential entropy, Gaussian maximum entropy | [calculus/04](../calculus/04_derivative_applications_optimization/), [prob/06](../probability_statistics/06_expectation_variance_and_moments/) | 20 |
| [`02_joint_and_conditional_entropy/`](02_joint_and_conditional_entropy/) | Joint and conditional entropy, the chain rule, conditioning reduces entropy, subadditivity, zero conditional entropy, Fano's inequality, entropy rate, Han's and Shearer's inequalities | [prob/07](../probability_statistics/07_joint_distributions_and_multivariate_normal/), Module 01 | 20 |
| [`03_cross_entropy_and_loss_functions/`](03_cross_entropy_and_loss_functions/) | Cross-entropy, Gibbs' inequality, equivalence with maximum likelihood, the softmax gradient $q - y$, proper scoring rules, label smoothing, focal loss, distillation, calibration | [prob/09](../probability_statistics/09_maximum_likelihood_and_map_estimation/), Module 02 | 20 |
| [`04_kl_divergence_and_f_divergences/`](04_kl_divergence_and_f_divergences/) | Nonnegativity of $D_{\mathrm{KL}}$ via Jensen, the chain rule, $f$-divergences and their data-processing inequality, the Gaussian closed form, Pinsker, forward versus reverse KL, Jensen–Shannon and the GAN objective, Donsker–Varadhan | [optimization/01](../optimization/01_problem_formulation_and_convexity/), Module 03 | 20 |
| [`05_mutual_information/`](05_mutual_information/) | Equivalent forms of $I(X; Y)$, the chain rule, the data-processing inequality and its sufficiency equality case, Gaussian MI and AWGN capacity, InfoNCE, plug-in bias, KSG, MINE, mRMR | Module 04 | 20 |
| [`06_information_theory_in_deep_learning/`](06_information_theory_in_deep_learning/) | The ELBO and its gap, rate and distortion of a stochastic encoder, the $D + R \ge H$ region, the information bottleneck, $\beta$-VAE, the KL-tilted RLHF policy, bits-back coding, MDL | [prob/10](../probability_statistics/10_bayesian_inference/), [optimization/08](../optimization/08_stochastic_optimization_for_ml/), Module 05 | 20 |
| **Total** | **6 modules** | — | **176** |

> [!NOTE]
> **Scope.** This area covers the *measurement* half of information theory thoroughly and the
> *coding* half thinly. Kraft's inequality appears only inside Module 03, exercise L3.2;
> Huffman coding is named but never constructed; the source-coding bound
> $H(X) \le \mathbb{E}[L] \lt H(X) + 1$ is asserted in passing and never derived; the
> noisy-channel coding theorem is stated in one sentence with no achievability or converse
> argument; and Shannon's rate–distortion function $R(D)$ is never defined, despite Module 06
> being organized around the phrase. Read Cover & Thomas Chapters 5,
> 7 and 10 alongside Modules 01, 05 and 06 if you need the operational theorems.

---

## Module architecture

Each numbered directory holds exactly the three files required by
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20.

### `README.md`

Module title, a short overview, a `> [!NOTE]` callout carrying the single most important
result, prerequisites and downstream links, learning outcomes, a Mermaid concept map, a
notation table, a core-results table, common misconceptions, an exercise index that matches
the notebook, and references at chapter precision.

### `first_principles.ipynb`

Theory, following the WHY → INTUITION → DEFINITION → DERIVATION → INTERPRETATION →
EXAMPLE → CONNECTION → KEY TAKEAWAYS progression of §5.

The contract requires executable code cells that verify each major theorem numerically,
two to four figures showing the geometry of the central idea, worked numerical examples,
and a closing **Key Takeaways** cell.

### `exercises.ipynb`

Twenty fully solved problems in four tiers, split **4 / 6 / 6 / 4** in every module of this
area:

- **L0** — concept checks
- **L1** — foundations
- **L2** — AI/ML and physics applications
- **L3** — challenge proofs

Each problem carries a statement, an intuition note, a full derivation, a
`$$\boxed{...}$$` answer, and a key takeaway.

### Status

All six modules pass `python3 tools/check_module.py`: executable verification cells, figures,
the `L0`-`L3` tiers, and the full README section list are in place. The L2 tier is
`## L2 — Applications (AI/ML and Physics)` in every notebook and genuinely contains both —
e.g. Landauer's limit, the Boltzmann distribution as maximum entropy, and Gibbs entropy in
physical units alongside the machine-learning problems.

Every notebook, legacy file included, opens with a Google Colab badge.

---

## Notation

The repository-wide register is [`../docs/notation.md`](../docs/notation.md); its
"Information theory" section governs this area.

Three conventions matter here, and **the current notebooks do not yet follow the first two**:

- **Cross-entropy is $H_{\times}(p, q)$, not $H(p, q)$.** The two-argument $H$ is already
  taken: $H(X, Y)$ is the joint entropy of a pair, in Module 02 and Module 05. Module 03
  presently writes cross-entropy as $H(p, q)$, so the same symbol carries two meanings in
  adjacent modules. The register retires that spelling; the decomposition reads
  $H_{\times}(p, q) = H(p) + D_{\mathrm{KL}}(p \parallel q)$.
- **InfoNCE is unnormalized.** The loss is the plain $K$-way softmax cross-entropy with no
  $\tfrac{1}{K}$ inside the denominator, so $\mathcal{L}_{\mathrm{NCE}} \ge 0$, chance level
  is $\log K$, and the bound is $I(X; Y) \ge \log K - \mathcal{L}_{\mathrm{NCE}}$. Module 05
  Proof 3.7 currently defines the loss *with* the $\tfrac{1}{K}$ and then uses the
  unnormalized bound, which puts its headline theorem off by $\log K$.
- **Every numeric answer carries its unit.** Bits for $\log_2$, nats for $\ln$, and no single
  derivation mixes them. Modules 01–03 work in bits, Modules 05–06 in nats. A bare $\log$ is
  allowed only where the base cancels.

KL divergence is always written $D_{\mathrm{KL}}(p \parallel q)$ with `\parallel` — never a
raw pipe, which would break table rendering on GitHub. Differential entropy is lowercase
$h(X)$. Alphabet size is $K$ throughout, including in Fano's inequality.

---

## Suggested order

The six modules form a chain: each one is the prerequisite for the next.

1. **01 — Self-information and entropy.** The axioms, $H(X)$, and its bounds. Start here
   even if you have seen entropy before; the axiomatic derivation is what later modules lean on.
2. **02 — Joint and conditional entropy.** The chain rule and Fano. This module owns the
   canonical statement of Fano's inequality for the whole repository.
3. **03 — Cross-entropy and loss functions.** Where the training loss of a classifier comes
   from, and what its irreducible floor is.
4. **04 — KL divergence and $f$-divergences.** The general machinery. Modules 01 and 02 both
   borrow Gibbs' inequality from here, so a first reading of those two carries one forward
   reference; it costs three lines to close, and a later wave will.
5. **05 — Mutual information.** Everything above, applied to pairs: the data-processing
   inequality, channel capacity, and what MI estimation can and cannot deliver.
6. **06 — Information theory in deep learning.** The synthesis: ELBO, information bottleneck,
   contrastive learning, RLHF, and description length.

For a targeted read, 01 → 03 is enough to understand a cross-entropy loss, and
01 → 02 → 04 → 05 is enough for the data-processing inequality and Fano bounds.

---

## Companion resources

Two legacy files predate the numbered curriculum and sit at the root of this directory.
They are listed in [`../docs/prerequisites.md`](../docs/prerequisites.md) as outside the
dependency graph: no numbered module may depend on either, and neither is maintained against
the module notebooks.

| File | What it actually contains |
| :--- | :--- |
| [`entropy_cross_entropy.md`](entropy_cross_entropy.md) | About one page. Defines $H(p)$ and cross-entropy, states the decomposition into entropy plus KL, notes nonnegativity and asymmetry, and links to a sister repository. No proofs, no exercises. Uses the retired $H(p, q)$ spelling for cross-entropy. Modules 01 and 03 supersede it. |
| [`kl_divergence.ipynb`](kl_divergence.ipynb) | Five cells, two of them code. Defines a `kl` helper and asserts nonnegativity, asymmetry, and the cross-entropy decomposition on one three-point example, then prints one number. It imports `matplotlib` but draws nothing. This is the only executable code in the area. |

---

## References

Benchmark texts for this area, per [`../CLAUDE.md`](../CLAUDE.md), at chapter precision.

**Primary.**

- **Cover, T. M., & Thomas, J. A.** (2006). *Elements of Information Theory*, 2nd ed. Wiley.
  Ch. 2 (entropy, relative entropy, mutual information) → Modules 01–05;
  Ch. 4 (entropy rates of a stochastic process) → Module 02;
  Ch. 5 (data compression, Kraft, Huffman, the wrong-code bound) → Module 03, thinly;
  Ch. 7 (channel capacity) and Ch. 8 (differential entropy) → Modules 01 and 05;
  Ch. 10 (rate–distortion) → Module 06, thinly;
  Ch. 11–12 (information theory and statistics; Sanov, Stein) → Module 04.
- **MacKay, D. J. C.** (2003). *Information Theory, Inference, and Learning Algorithms*.
  Cambridge University Press. Ch. 1–6 (probability, entropy, source coding) → Modules 01, 03;
  Ch. 8–10 (dependent variables, noisy-channel communication) → Modules 02, 05.
- **Shannon, C. E.** (1948). *A Mathematical Theory of Communication*. Bell System Technical
  Journal, 27, 379–423 and 623–656. The founding paper; §6 for the entropy axioms.

**Supporting.**

- **Polyanskiy, Y., & Wu, Y.** (2024). *Information Theory: From Coding to Learning*.
  Cambridge University Press. The modern $f$-divergence toolbox used by Module 04.
- **Csiszár, I., & Körner, J.** (2011). *Information Theory: Coding Theorems for Discrete
  Memoryless Systems*, 2nd ed. Cambridge University Press.
- **Yeung, R. W.** (2008). *Information Theory and Network Coding*. Springer. Ch. 3, the
  I-measure and the limits of information diagrams — the caution behind Module 02, L3.3.
- **Gneiting, T., & Raftery, A. E.** (2007). *Strictly Proper Scoring Rules, Prediction, and
  Estimation*. JASA 102(477), 359–378. The scoring-rule theory behind Module 03.
- **Amari, S.** (2016). *Information Geometry and Its Applications*. Springer. KL as a Bregman
  divergence and the Fisher metric — Module 04, L3.4.
- **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer. §1.6 for the
  information-theoretic reading of the loss functions in Module 03.

**Papers the modules build on directly.**

- **Kullback, S., & Leibler, R. A.** (1951). *On Information and Sufficiency*. Ann. Math.
  Statist. 22(1), 79–86.
- **Fano, R. M.** (1961). *Transmission of Information*. MIT Press. The original inequality,
  canonical here in Module 02, Proof 3.6.
- **Kraskov, A., Stögbauer, H., & Grassberger, P.** (2004). *Estimating Mutual Information*.
  Phys. Rev. E 69, 066138. The KSG estimator of Module 05.
- **Paninski, L.** (2003). *Estimation of Entropy and Mutual Information*. Neural Computation
  15(6), 1191–1253. Plug-in bias, Modules 01 and 05.
- **van den Oord, A., Li, Y., & Vinyals, O.** (2018). *Representation Learning with Contrastive
  Predictive Coding*. arXiv:1807.03748, eq. (4) — the InfoNCE convention fixed above.
- **Poole, B., et al.** (2019). *On Variational Bounds of Mutual Information*. ICML. The
  $\log K$ ceiling of Modules 05 and 06.
- **Tishby, N., Pereira, F. C., & Bialek, W.** (1999). *The Information Bottleneck Method*.
  Allerton. Module 06, Proof 3.4.
- **Kingma, D. P., & Welling, M.** (2014). *Auto-Encoding Variational Bayes*. ICLR,
  Appendix B for the Gaussian KL closed form.
- **Alemi, A. A., et al.** (2018). *Fixing a Broken ELBO*. ICML. The rate–distortion reading
  of the ELBO in Module 06.
