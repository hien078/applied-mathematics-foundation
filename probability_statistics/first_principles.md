# Theory: Probability & Statistics for Mathematical Modeling and AI

This document provides a comprehensive, first-principles foundation of probability theory, mathematical statistics, stochastic processes, and information theory. The emphasis is on **understanding randomness as a modeling tool** — how probabilistic frameworks model uncertainty, enable statistical inference, drive data-driven parameter estimation, and power modern Machine Learning and Artificial Intelligence architectures.

---

## 1. Probability Axioms

### 1.1 Sample Space and Events

**Definition (Sample Space).** The **sample space** $\Omega$ is the set of all possible outcomes of a random experiment.

**Definition (Event).** An **event** $A$ is a subset of $\Omega$ ($A \subseteq \Omega$), belonging to a $\sigma$-algebra $\mathcal{F}$ of subsets of $\Omega$.

**Examples:**

| Experiment | Sample Space $\Omega$ | Example Event $A$ |
|---|---|---|
| Coin flip | $\{H, T\}$ | $A = \{H\}$ ("heads") |
| Die roll | $\{1, 2, 3, 4, 5, 6\}$ | $A = \{2, 4, 6\}$ ("even outcome") |
| Lifetime of a component | $[0, \infty)$ | $A = [100, \infty)$ ("lasts over 100 hours") |
| Sensor noise trajectory | $\mathbb{R}^d$ | $A = \{\mathbf{x} \in \mathbb{R}^d \mid \|\mathbf{x}\|_2 \le \epsilon\}$ ("bounded error") |

### 1.2 Kolmogorov Axioms

**Definition (Probability Measure).** A function $P: \mathcal{F} \to [0, 1]$ is a **probability measure** if it satisfies the three Kolmogorov Axioms:

1. **Non-negativity:** $P(A) \ge 0$ for all events $A \in \mathcal{F}$.
2. **Normalization:** $P(\Omega) = 1$.
3. **Countable Additivity:** If $A_1, A_2, \ldots$ are pairwise disjoint events ($A_i \cap A_j = \emptyset$ for $i \ne j$), then:

$$P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i).$$

### 1.3 Fundamental Consequences of the Axioms

| Property | Mathematical Statement | Derivation Sketch |
|---|---|---|
| Complement | $P(A^c) = 1 - P(A)$ | $\Omega = A \cup A^c$ (disjoint); apply Axioms 2 and 3 |
| Empty Set | $P(\emptyset) = 0$ | $\emptyset = \Omega^c \implies P(\emptyset) = 1 - P(\Omega) = 0$ |
| Monotonicity | $A \subseteq B \implies P(A) \le P(B)$ | Write $B = A \cup (B \setminus A)$ as disjoint union |
| Inclusion-Exclusion | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ | $A \cup B = A \cup (B \setminus (A \cap B))$ disjoint union |
| Union Bound (Boole's Inequality) | $P\left(\bigcup_i A_i\right) \le \sum_i P(A_i)$ | Follows directly from Inclusion-Exclusion and monotonicity |

---

## 2. Conditional Probability, Independence, and Bayes' Theorem

### 2.1 Conditional Probability

**Definition.** The **conditional probability** of an event $A$ given that event $B$ has occurred ($P(B) > 0$) is defined as:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}.$$

**Geometric & Intuitive Interpretation:** Conditioning on $B$ restricts the effective sample space from $\Omega$ down to $B$. $P(A|B)$ measures the proportion of event $B$'s probability mass that falls inside event $A$.

### 2.2 Statistical Independence

**Definition.** Events $A$ and $B$ are **statistically independent** ($A \perp\!\!\!\perp B$) if and only if:

$$P(A \cap B) = P(A) \cdot P(B).$$

Equivalently, if $P(B) > 0$, independence implies $P(A|B) = P(A)$ — learning that $B$ occurred provides zero information about $A$.

### 2.3 Law of Total Probability

**Theorem.** Let $B_1, B_2, \ldots, B_n$ be a partition of $\Omega$ (i.e., mutually exclusive $B_i \cap B_j = \emptyset$ for $i \ne j$, and collectively exhaustive $\bigcup_{i=1}^n B_i = \Omega$), with $P(B_i) > 0$ for all $i$. Then for any event $A$:

$$P(A) = \sum_{i=1}^{n} P(A|B_i) P(B_i).$$

### 2.4 Bayes' Theorem

**Theorem (Bayes' Rule).** Under the same partition conditions as above, for any specific scenario $B_j$ given that $A$ has occurred ($P(A) > 0$):

$$P(B_j|A) = \frac{P(A|B_j) P(B_j)}{\sum_{i=1}^{n} P(A|B_i) P(B_i)}.$$

**Bayesian Terminology:**
- $P(B_j)$: **Prior Probability** — initial belief about hypothesis $B_j$ before observing data $A$.
- $P(A|B_j)$: **Likelihood** — probability of observing data $A$ under hypothesis $B_j$.
- $P(B_j|A)$: **Posterior Probability** — updated belief about $B_j$ after observing data $A$.
- $P(A) = \sum_i P(A|B_i) P(B_i)$: **Marginal Likelihood (Evidence)** — total probability of observing data $A$ across all hypotheses.

**Result:**

$$\boxed{\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}} \implies P(\theta \mid D) = \frac{P(D \mid \theta) P(\theta)}{P(D)}}$$

### 2.5 Real-World Example: Disease Screening & Base Rate Fallacy

Suppose a rare disease affects $1\%$ of the population ($P(D) = 0.01$). A diagnostic test exhibits:
- **Sensitivity (True Positive Rate):** $P(\text{Pos}|D) = 0.95$.
- **Specificity (True Negative Rate):** $P(\text{Neg}|D^c) = 0.90 \implies P(\text{Pos}|D^c) = 0.10$ (False Positive Rate).

If a randomly selected individual tests positive, what is the probability they actually have the disease?

By Bayes' Theorem:

$$P(D|\text{Pos}) = \frac{P(\text{Pos}|D) P(D)}{P(\text{Pos}|D) P(D) + P(\text{Pos}|D^c) P(D^c)} = \frac{0.95 \times 0.01}{(0.95 \times 0.01) + (0.10 \times 0.99)} = \frac{0.0095}{0.0095 + 0.0990} = \frac{0.0095}{0.1085} \approx 0.0876 \; (8.76\%).$$

**Insight:** Despite a high sensitivity of $95\%$, a positive test result means only an $8.76\%$ chance of actual disease. This phenomenon is known as the **base rate fallacy** — when the prior $P(D)$ is extremely small, false positives from the large healthy population outnumber true positives from the small diseased population.

---

## 3. Random Variables: Univariate and Multivariate

### 3.1 Definition of a Random Variable

**Definition.** A **random variable** $X$ is a measurable function $X: \Omega \to \mathbb{R}$ assigning a real value to every outcome $\omega \in \Omega$.

### 3.2 Discrete Random Variables

A random variable $X$ is **discrete** if it takes values in a countable set $\{x_1, x_2, \ldots\}$.

- **Probability Mass Function (PMF):** $p_X(x) = P(X = x)$, where $p_X(x) \ge 0$ and $\sum_x p_X(x) = 1$.
- **Cumulative Distribution Function (CDF):** $F_X(x) = P(X \le x) = \sum_{x_i \le x} p_X(x_i)$.

### 3.3 Continuous Random Variables

A random variable $X$ is **continuous** if there exists a non-negative integrable function $f_X: \mathbb{R} \to [0, \infty)$ such that the CDF can be expressed as:

$$F_X(x) = P(X \le x) = \int_{-\infty}^{x} f_X(t)\,dt.$$

- **Probability Density Function (PDF):** $f_X(x) = \frac{d}{dx} F_X(x)$, satisfying $\int_{-\infty}^{\infty} f_X(x)\,dx = 1$.
- **Point Probabilities:** For a continuous random variable, the probability of any exact point value is zero: $P(X = x) = 0$. Probabilities are defined over intervals:

$$\boxed{P(a \le X \le b) = \int_{a}^{b} f_X(x)\,dx = F_X(b) - F_X(a)}$$

### 3.4 Joint Distributions & Multivariate Random Variables

When modeling real-world systems or multi-dimensional data vectors $\mathbf{X} = (X_1, X_2, \ldots, X_d)^T \in \mathbb{R}^d$, we require multivariate distributions.

#### Joint PDF / PMF
For two continuous random variables $X$ and $Y$, the **joint PDF** $f_{X,Y}(x,y)$ satisfies:

$$P((X,Y) \in A) = \iint_A f_{X,Y}(x,y)\,dx\,dy, \quad \text{with } \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx\,dy = 1.$$

#### Marginal Distributions
The individual behavior of $X$ isolated from $Y$ is obtained by integrating out (marginalizing) $Y$:

$$f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dy, \quad f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x,y)\,dx.$$

#### Conditional Distributions
The density of $Y$ given that $X = x$ is defined as:

$$f_{Y|X}(y|x) = \frac{f_{X,Y}(x,y)}{f_X(x)} \quad (\text{for } f_X(x) > 0).$$

#### Independence of Random Variables
Random variables $X$ and $Y$ are independent ($X \perp\!\!\!\perp Y$) if and only if their joint density factorizes as the product of their marginals:

$$f_{X,Y}(x,y) = f_X(x) \cdot f_Y(y) \quad \forall x, y.$$

### 3.5 Covariance, Correlation, and Covariance Matrix

#### Covariance
**Definition.** The **covariance** between random variables $X$ and $Y$ measures their joint linear variability:

$$\text{Cov}(X,Y) = E[(X - E[X])(Y - E[Y])] = E[XY] - E[X]E[Y].$$

#### Correlation Coefficient
**Definition.** The normalized, dimensionless measure of linear dependence is Pearson's correlation coefficient $\rho_{X,Y} \in [-1, 1]$:

$$\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}.$$

#### Variance of a Linear Combination
For random variables $X$ and $Y$ and constants $a, b$:

$$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab\,\text{Cov}(X,Y).$$

If $X \perp\!\!\!\perp Y$, then $\text{Cov}(X,Y) = 0$, and $\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y)$.

#### Covariance Matrix
For a random vector $\mathbf{X} = (X_1, X_2, \ldots, X_d)^T$ with mean vector $\boldsymbol{\mu} = E[\mathbf{X}]$, the **Covariance Matrix** $\mathbf{\Sigma} \in \mathbb{R}^{d \times d}$ is defined as:

$$\mathbf{\Sigma} = E[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^T] = \begin{pmatrix} \text{Var}(X_1) & \text{Cov}(X_1, X_2) & \cdots & \text{Cov}(X_1, X_d) \\ \text{Cov}(X_2, X_1) & \text{Var}(X_2) & \cdots & \text{Cov}(X_2, X_d) \\ \vdots & \vdots & \ddots & \vdots \\ \text{Cov}(X_d, X_1) & \text{Cov}(X_d, X_2) & \cdots & \text{Var}(X_d) \end{pmatrix}.$$

**Properties of $\mathbf{\Sigma}$:**
1. Symmetric: $\mathbf{\Sigma}^T = \mathbf{\Sigma}$ since $\text{Cov}(X_i, X_j) = \text{Cov}(X_j, X_i)$.
2. Symmetric Positive Semi-Definite (SPSD): $\mathbf{v}^T \mathbf{\Sigma} \mathbf{v} = \text{Var}(\mathbf{v}^T \mathbf{X}) \ge 0$ for any vector $\mathbf{v} \in \mathbb{R}^d$.

---

## 4. Common Probability Distributions Family

### 4.1 Discrete Distributions

#### Bernoulli Distribution
$X \sim \text{Bernoulli}(p)$: Modeling a single binary trial (success/failure) with success probability $p \in [0,1]$.
- **PMF:** $P(X=1) = p, \; P(X=0) = 1-p \implies p_X(x) = p^x (1-p)^{1-x}$ for $x \in \{0, 1\}$.
- **Expectation & Variance:** $E[X] = p$, $\text{Var}(X) = p(1-p)$.

#### Binomial Distribution
$X \sim \text{Binomial}(n, p)$: Total number of successes in $n$ independent and identically distributed (i.i.d.) Bernoulli($p$) trials.
- **PMF:** $P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$ for $k \in \{0, 1, \ldots, n\}$.
- **Expectation & Variance:** $E[X] = np$, $\text{Var}(X) = np(1-p)$.

#### Poisson Distribution
$X \sim \text{Poisson}(\lambda)$: Number of rare events occurring in a fixed interval when events arrive independently at a constant average rate $\lambda > 0$.
- **PMF:** $P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}$ for $k \in \{0, 1, 2, \ldots\}$.
- **Expectation & Variance:** $E[X] = \lambda$, $\text{Var}(X) = \lambda$.
- **Binomial Limit Connection:** As $n \to \infty$ and $p \to 0$ such that $np = \lambda$, $\text{Binomial}(n,p) \to \text{Poisson}(\lambda)$.

#### Categorical & Multinomial Distributions
- $\text{Categorical}(p_1, \ldots, p_K)$: Single trial with $K$ discrete categories where $\sum_{k=1}^K p_k = 1$. (Standard output representation of Softmax in ML classification).
- $\text{Multinomial}(n, \mathbf{p})$: Generalization of Binomial for $n$ trials across $K$ categories.

---

### 4.2 Continuous Distributions

#### Uniform Distribution
$X \sim \text{Uniform}(a, b)$: Equal likelihood density across interval $[a,b]$.
- **PDF:** $f_X(x) = \frac{1}{b-a}$ for $x \in [a, b]$.
- **Expectation & Variance:** $E[X] = \frac{a+b}{2}$, $\text{Var}(X) = \frac{(b-a)^2}{12}$.

#### Normal (Gaussian) Distribution
$X \sim \mathcal{N}(\mu, \sigma^2)$: Ubiquitous distribution for continuous physical measurements and measurement errors.
- **PDF:** $f_X(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$.
- **Expectation & Variance:** $E[X] = \mu$, $\text{Var}(X) = \sigma^2$.

#### Exponential Distribution
$X \sim \text{Exponential}(\lambda)$: Continuous waiting time between Poisson process events with rate $\lambda > 0$.
- **PDF & CDF:** $f_X(x) = \lambda e^{-\lambda x}$, $F_X(x) = 1 - e^{-\lambda x}$ for $x \ge 0$.
- **Expectation & Variance:** $E[X] = \frac{1}{\lambda}$, $\text{Var}(X) = \frac{1}{\lambda^2}$.
- **Memoryless Property:** $P(X > s + t \mid X > s) = P(X > t)$.

#### Gamma & Beta Distributions
- $\text{Gamma}(\alpha, \beta)$: Generalization of Exponential distribution for waiting times until $\alpha$ events occur.
- $\text{Beta}(\alpha, \beta)$: Continuous distribution bounded on $[0,1]$, widely used as a conjugate prior for Bernoulli/Binomial probabilities in Bayesian statistics.

#### Student's t & Chi-Squared ($\chi^2$) Distributions
- **Chi-Squared $\chi^2(k)$:** Sum of squares of $k$ independent standard normal variables $Z_1^2 + \cdots + Z_k^2$. Used in variance testing and goodness-of-fit.
- **Student's t-distribution $t(\nu)$:** Ratio of a standard normal variable to the square root of an independent $\chi^2$ variable. Crucial for hypothesis testing with small sample sizes.

---

### 4.3 Multivariate Normal (Gaussian) Distribution

$\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \mathbf{\Sigma})$ for $\mathbf{X} \in \mathbb{R}^d$:
- **PDF:**

$$f_{\mathbf{X}}(\mathbf{x}) = \frac{1}{(2\pi)^{d/2} \det(\mathbf{\Sigma})^{1/2}} \exp\left(-\frac{1}{2} (\mathbf{x} - \boldsymbol{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right).$$

- **Mahalanobis Distance:** The exponent features $D_M(\mathbf{x}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^T \mathbf{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})}$, measuring scale-invariant distance from mean $\boldsymbol{\mu}$.
- **Geometry:** Contours of equal probability density form ellipsoids in $\mathbb{R}^d$ aligned with the eigenvectors of $\mathbf{\Sigma}$.

---

### 4.4 Comprehensive Distribution Summary Table

| Distribution | Symbol | Type | Support | PMF / PDF $f(x)$ | Mean $E[X]$ | Variance $\text{Var}(X)$ |
|---|---|---|---|---|---|---|
| Bernoulli | $\text{Bern}(p)$ | Discrete | $\{0, 1\}$ | $p^x (1-p)^{1-x}$ | $p$ | $p(1-p)$ |
| Binomial | $\text{Bin}(n,p)$ | Discrete | $\{0,\ldots,n\}$ | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| Poisson | $\text{Pois}(\lambda)$ | Discrete | $\{0,1,2,\ldots\}$ | $\frac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ |
| Uniform | $\text{Unif}(a,b)$ | Continuous | $[a,b]$ | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ |
| Normal | $\mathcal{N}(\mu,\sigma^2)$ | Continuous | $\mathbb{R}$ | $\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ |
| Exponential | $\text{Exp}(\lambda)$ | Continuous | $[0,\infty)$ | $\lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ |
| Beta | $\text{Beta}(\alpha,\beta)$ | Continuous | $[0,1]$ | $\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ |
| Multivariate Normal | $\mathcal{N}(\boldsymbol{\mu},\mathbf{\Sigma})$ | Continuous Vector | $\mathbb{R}^d$ | $\frac{e^{-\frac{1}{2}(\mathbf{x}-\boldsymbol{\mu})^T\mathbf{\Sigma}^{-1}(\mathbf{x}-\boldsymbol{\mu})}}{(2\pi)^{d/2}\det(\mathbf{\Sigma})^{1/2}}$ | $\boldsymbol{\mu}$ | $\mathbf{\Sigma}$ (Covariance matrix) |

---

## 5. Expectation, Variance, Moments, and Limit Theorems

### 5.1 Mathematical Expectation

**Definition (Discrete):** $E[X] = \sum_x x \cdot p_X(x)$.

**Definition (Continuous):** $E[X] = \int_{-\infty}^{\infty} x \cdot f_X(x)\,dx$.

#### Linearity of Expectation
For any random variables $X_1, X_2, \ldots, X_n$ (regardless of independence!) and constants $a_1, \ldots, a_n, b$:

$$\boxed{E\left[\sum_{i=1}^n a_i X_i + b\right] = \sum_{i=1}^n a_i E[X_i] + b}$$

### 5.2 Variance and Standard Deviation

**Definition.** $\text{Var}(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$.

**Algebraic Derivation:** Letting $\mu = E[X]$:

$$\text{Var}(X) = E[(X - \mu)^2] = E[X^2 - 2\mu X + \mu^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2] - \mu^2.$$

**Standard Deviation:** $\sigma_X = \sqrt{\text{Var}(X)}$, expressed in the same physical units as $X$.

### 5.3 Moment Generating Functions (MGF)

**Definition.** The **Moment Generating Function (MGF)** $M_X(t)$ of a random variable $X$ is defined as:

$$M_X(t) = E[e^{tX}] = \begin{cases} \sum_x e^{tx} p_X(x) & \text{(discrete)} \\ \int_{-\infty}^{\infty} e^{tx} f_X(x)\,dx & \text{(continuous)} \end{cases}$$

#### Moment Extraction Property
By expanding $e^{tX} = 1 + tX + \frac{t^2 X^2}{2!} + \frac{t^3 X^3}{3!} + \cdots$, taking expectations term-by-term yields:

$$M_X(t) = 1 + t E[X] + \frac{t^2}{2!} E[X^2] + \frac{t^3}{3!} E[X^3] + \cdots$$

Differentiating $k$ times with respect to $t$ and evaluating at $t = 0$ isolates the $k$-th raw moment:

$$\boxed{E[X^k] = M_X^{(k)}(0) = \left. \frac{d^k M_X(t)}{dt^k} \right|_{t=0}}$$

#### Independence and Sums
If $X \perp\!\!\!\perp Y$, then $M_{X+Y}(t) = E[e^{t(X+Y)}] = E[e^{tX}] E[e^{tY}] = M_X(t) M_Y(t)$. The MGF of a sum of independent random variables is the product of their individual MGFs.

---

### 5.4 Law of Large Numbers (LLN)

Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with finite mean $E[X_i] = \mu$ and variance $\text{Var}(X_i) = \sigma^2 < \infty$. Define the sample mean $\bar{X}_n = \frac{1}{n} \sum_{i=1}^n X_i$.

**Weak Law of Large Numbers (WLLN):** The sample mean converges in probability to the population mean:

$$\lim_{n \to \infty} P(|\bar{X}_n - \mu| > \epsilon) = 0 \quad \forall \epsilon > 0.$$

**Modeling Significance:** Justifies **Monte Carlo Simulation** — expectations of complex integrals or system states can be approximated numerically to arbitrary precision by generating $n$ random samples and computing their sample mean.

### 5.5 Central Limit Theorem (CLT)

**Theorem (CLT).** Let $X_1, X_2, \ldots, X_n$ be i.i.d. random variables with $E[X_i] = \mu$ and $\text{Var}(X_i) = \sigma^2 < \infty$. As $n \to \infty$, the normalized sample mean converges in distribution to a Standard Normal distribution $\mathcal{N}(0,1)$:

$$\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1).$$

Equivalently, for large $n$:

$$\boxed{\bar{X}_n \approx \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)}$$

**Why the CLT is Profound:** It guarantees that the average of a large number of independent random factors will behave like a Normal distribution, **regardless of the underlying distribution of individual factors**. This explains the universal emergence of Gaussian noise in physical sensors, measurement errors, and financial markets.

---

## 6. Mathematical Statistics and Parameter Estimation

Statistical inference reverses the probability direction: given observed sample data $\mathcal{D} = \{x_1, x_2, \ldots, x_n\}$, how do we estimate unknown underlying parameters $\theta$ of a parametric probabilistic model $f(x; \theta)$?

### 6.1 Maximum Likelihood Estimation (MLE)

#### Likelihood Function
The **Likelihood function** $L(\theta; \mathcal{D})$ measures the joint probability/density of observing the dataset $\mathcal{D}$ under parameter $\theta$:

$$L(\theta; \mathcal{D}) = \prod_{i=1}^{n} f(x_i; \theta).$$

#### Log-Likelihood Function
To simplify calculus and avoid underflow, we take the natural logarithm:

$$\ell(\theta; \mathcal{D}) = \ln L(\theta; \mathcal{D}) = \sum_{i=1}^{n} \ln f(x_i; \theta).$$

#### MLE Principle
The **Maximum Likelihood Estimator** $\hat{\theta}_{\text{MLE}}$ chooses parameter values that maximize the probability of generating the observed data:

$$\boxed{\hat{\theta}_{\text{MLE}} = \arg\max_{\theta} \ell(\theta; \mathcal{D})}$$

#### Concrete Example: MLE for Gaussian Mean and Variance
Given $x_1, \ldots, x_n \sim \text{i.i.d. } \mathcal{N}(\mu, \sigma^2)$:

$$\ell(\mu, \sigma^2) = -\frac{n}{2} \ln(2\pi) - \frac{n}{2} \ln(\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu)^2.$$

1. Setting $\frac{\partial \ell}{\partial \mu} = 0 \implies \frac{1}{\sigma^2} \sum_{i=1}^n (x_i - \mu) = 0 \implies \hat{\mu}_{\text{MLE}} = \frac{1}{n}\sum_{i=1}^n x_i = \bar{x}$.
2. Setting $\frac{\partial \ell}{\partial \sigma^2} = 0 \implies \hat{\sigma}^2_{\text{MLE}} = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2$.

---

### 6.2 Maximum A Posteriori Estimation (MAP)

When prior knowledge about parameter $\theta$ is available via a prior distribution $p(\theta)$, Bayes' Theorem gives:

$$p(\theta \mid \mathcal{D}) \propto p(\mathcal{D} \mid \theta) p(\theta).$$

Taking the logarithm yields the **MAP Objective**:

$$\boxed{\hat{\theta}_{\text{MAP}} = \arg\max_{\theta} \left[ \sum_{i=1}^n \ln f(x_i \mid \theta) + \ln p(\theta) \right]}$$

#### Direct Connection to Machine Learning Regularization
- **Gaussian Prior $p(\theta) = \mathcal{N}(0, \sigma_0^2)$:** $\ln p(\theta) = -\frac{\|\theta\|_2^2}{2\sigma_0^2} + \text{const} \implies$ **Ridge Regression (L2 Regularization / Weight Decay)**.
- **Laplace Prior $p(\theta) \propto \exp(-\lambda \|\theta\|_1)$:** $\ln p(\theta) = -\lambda \|\theta\|_1 + \text{const} \implies$ **Lasso Regression (L1 Regularization / Sparsity)**.

---

### 6.3 Properties of Estimators & Bias-Variance Decomposition

#### Bias
The **Bias** of an estimator $\hat{\theta}$ is $B(\hat{\theta}) = E[\hat{\theta}] - \theta$. An estimator is **unbiased** if $E[\hat{\theta}] = \theta$.

#### Mean Squared Error (MSE)
$\text{MSE}(\hat{\theta}) = E[(\hat{\theta} - \theta)^2]$.

**Bias-Variance Decomposition Theorem:**

$$\boxed{\text{MSE}(\hat{\theta}) = \text{Bias}(\hat{\theta})^2 + \text{Var}(\hat{\theta})}$$

*Proof:* Add and subtract $E[\hat{\theta}]$ inside the expectation:

$$E[(\hat{\theta} - \theta)^2] = E[\{(\hat{\theta} - E[\hat{\theta}]) + (E[\hat{\theta}] - \theta)\}^2] = \text{Var}(\hat{\theta}) + (E[\hat{\theta}] - \theta)^2 + 0 = \text{Var}(\hat{\theta}) + \text{Bias}(\hat{\theta})^2.$$

#### Cramér-Rao Lower Bound (CRLB) & Efficiency
For any unbiased estimator $\hat{\theta}$ of parameter $\theta$ from $n$ i.i.d. observations with log-density $\ln f(x; \theta)$ (under standard regularity conditions):

$$\boxed{\text{Var}(\hat{\theta}) \ge \frac{1}{I_n(\theta)} = \frac{1}{n I(\theta)}}$$

where $I(\theta) = E\left[ \left( \frac{\partial \ln f(X; \theta)}{\partial \theta} \right)^2 \right] = -E\left[ \frac{\partial^2 \ln f(X; \theta)}{\partial \theta^2} \right]$ is the **Fisher Information**. An unbiased estimator that achieves the CRLB is termed **efficient** (Uniformly Minimum Variance Unbiased Estimator / UMVUE) (Lehmann & Casella, 1998).

---

### 6.4 Confidence Intervals & Hypothesis Testing Basics

#### Confidence Interval (CI)
A $(1-\alpha)100\%$ **Confidence Interval** for parameter $\theta$ is a random interval $[L, U]$ derived from sample statistics such that $P(L \le \theta \le U) = 1 - \alpha$.
For example, a $95\%$ CI for the mean $\mu$ of a Normal distribution with known variance $\sigma^2$ is:

$$\bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}} = \left[ \bar{X} - 1.96 \frac{\sigma}{\sqrt{n}}, \, \bar{X} + 1.96 \frac{\sigma}{\sqrt{n}} \right].$$

#### Hypothesis Testing
- **Null Hypothesis ($H_0$):** Baseline assertion of no effect / no difference (e.g., $\mu = \mu_0$).
- **Alternative Hypothesis ($H_1$):** Claim being tested against $H_0$.
- **$p$-value:** Probability under $H_0$ of observing a test statistic as extreme as or more extreme than the one computed from sample data. Reject $H_0$ if $p\text{-value} < \alpha$.

---

## 7. Information Theory Foundations for AI

Information theory quantifies uncertainty, information content, and distance between probability distributions.

### 7.1 Self-Information and Shannon Entropy

#### Self-Information
The information content of observing an outcome $x$ with probability $P(x)$ is:

$$I(x) = -\log_2 P(x) \quad (\text{measured in bits}).$$

Unlikely events convey high information content; certainty conveys zero information.

#### Shannon Entropy
**Definition.** The **Entropy** $H(P)$ measures the average uncertainty or surprise in a probability distribution $P$:

$$\boxed{H(P) = -\sum_{x} P(x) \log P(x) \quad \text{or} \quad H(P) = -\int f(x) \ln f(x)\,dx}$$

Maximal entropy occurs under uniform distributions (maximum uncertainty); minimal entropy ($H=0$) occurs when outcomes are deterministic.

---

### 7.2 Cross-Entropy

**Definition.** Given true target distribution $P$ and predicted model distribution $Q$, the **Cross-Entropy** $H(P, Q)$ measures the average code length required to encode events drawn from $P$ using code optimized for $Q$:

$$\boxed{H(P, Q) = -\sum_{x} P(x) \log Q(x)}$$

#### Application in Machine Learning Classification
In $K$-class classification, for a sample with one-hot ground truth $\mathbf{y} = (y_1, \ldots, y_K)^T$ and predicted softmax probabilities $\hat{\mathbf{y}} = (\hat{y}_1, \ldots, \hat{y}_K)^T$:

$$\mathcal{L}_{\text{CE}} = H(\mathbf{y}, \hat{\mathbf{y}}) = -\sum_{k=1}^K y_k \ln \hat{y}_k = -\ln \hat{y}_{\text{true}}.$$

Cross-entropy loss in machine learning is mathematically identical to the Negative Log-Likelihood (NLL) under a Categorical distribution!

---

### 7.3 Kullback-Leibler (KL) Divergence

**Definition.** The **KL Divergence** (also called relative entropy) measures the asymmetric information discrepancy between true distribution $P$ and approximating distribution $Q$:

$$\boxed{D_{\text{KL}}(P \parallel Q) = \sum_{x} P(x) \log \left(\frac{P(x)}{Q(x)}\right) = H(P, Q) - H(P)}$$

For continuous distributions:

$$D_{\text{KL}}(P \parallel Q) = \int_{-\infty}^{\infty} p(x) \ln \left(\frac{p(x)}{q(x)}\right)\,dx.$$

#### Key Properties of KL Divergence
1. **Non-negativity (Gibbs' Inequality):** $D_{\text{KL}}(P \parallel Q) \ge 0$, with equality $D_{\text{KL}}(P \parallel Q) = 0$ if and only if $P = Q$ almost everywhere.
2. **Asymmetry:** $D_{\text{KL}}(P \parallel Q) \ne D_{\text{KL}}(Q \parallel P)$ in general (it is not a metric).

#### Closed-Form KL Divergence Between Two Gaussians
For $P = \mathcal{N}(\mu_1, \sigma_1^2)$ and $Q = \mathcal{N}(\mu_2, \sigma_2^2)$:

$$D_{\text{KL}}(P \parallel Q) = \ln\left(\frac{\sigma_2}{\sigma_1}\right) + \frac{\sigma_1^2 + (\mu_1 - \mu_2)^2}{2\sigma_2^2} - \frac{1}{2}.$$

*(This exact closed-form equation forms the regularizer term in Variational Autoencoders (VAEs)!)*

---

## 8. Stochastic Processes and Stochastic Differential Equations (SDEs)

A **stochastic process** is a collection of random variables $\{X(t) \mid t \in T\}$ indexed by time $t \in T$.

### 8.1 Discrete-Time Markov Chains (DTMC)

#### Markov Property
A discrete-time process $\{X_0, X_1, X_2, \ldots\}$ on discrete state space $S = \{1, 2, \ldots, M\}$ possesses the **Markov Property** if the future state depends solely on the current state:

$$P(X_{n+1} = j \mid X_n = i, X_{n-1} = i_{n-1}, \ldots, X_0 = i_0) = P(X_{n+1} = j \mid X_n = i) = p_{ij}.$$

#### Transition Matrix
The $M \times M$ **Transition Matrix** $\mathbf{P}$ contains non-negative probabilities $p_{ij} \ge 0$, with row sums $\sum_{j=1}^M p_{ij} = 1$ (right stochastic matrix).

#### Multi-Step State Evolution
Starting with initial probability state vector $\boldsymbol{\pi}^{(0)}$, the state probability distribution at step $k$ is given by matrix multiplication:

$$\boldsymbol{\pi}^{(k)} = \boldsymbol{\pi}^{(0)} \mathbf{P}^k.$$

#### Stationary Distribution
A distribution vector $\boldsymbol{\pi}$ is **stationary** if it satisfies the eigenvector equation:

$$\boxed{\boldsymbol{\pi} = \boldsymbol{\pi}\mathbf{P}, \quad \text{subject to } \sum_{i=1}^M \pi_i = 1, \; \pi_i \ge 0}$$

---

### 8.2 Continuous-Time Poisson Process

A counting process $\{N(t), t \ge 0\}$ representing total event occurrences up to time $t$ is a **Poisson Process** with rate $\lambda > 0$ if:
1. $N(0) = 0$.
2. Independent Increments: number of events in non-overlapping intervals are independent.
3. For any $t > 0$ and $h > 0$, $N(t+h) - N(t) \sim \text{Poisson}(\lambda h)$.

The inter-arrival times $T_1, T_2, \ldots$ between successive events are i.i.d. $\text{Exponential}(\lambda)$ variables.

---

### 8.3 Brownian Motion (Wiener Process)

A continuous-time stochastic process $\{W(t), t \ge 0\}$ is a standard **Brownian Motion** (or Wiener process) if:
1. $W(0) = 0$ almost surely.
2. Continuous trajectories: $t \mapsto W(t)$ is continuous.
3. Independent stationary increments: For $s < t$, $W(t) - W(s) \sim \mathcal{N}(0, t-s)$ independent of past trajectory $\{W(\tau), \tau \le s\}$.

---

### 8.4 Stochastic Differential Equations (SDEs)

In continuous physical systems and generative AI modeling, deterministic ODEs are extended to include stochastic noise driven by a Wiener process $W(t)$:

$$\boxed{dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t}$$

- $\mu(X_t, t)$: **Drift coefficient** (deterministic trend direction).
- $\sigma(X_t, t)$: **Diffusion coefficient** (stochastic magnitude scale).
- $dW_t \sim \mathcal{N}(0, dt)$: Gaussian increment of Brownian motion.

**Key Connection to Modern AI:** Continuous-time Score-based Diffusion Models (e.g., DDPM, SDE-based image generation) use forward SDEs to gradually convert data into Gaussian noise, and learn neural networks to reverse the SDE to generate high-fidelity samples!

---

## 9. Direct Bridge to Mathematical Modeling and AI/ML

The table below establishes explicit mappings between core probability/statistics theory and modern AI / ML algorithms:

| Probability & Statistics Concept | Mathematical Formulation | Machine Learning / AI Architecture Application |
|---|---|---|
| **Bayes' Theorem** | $P(\theta \mid D) \propto P(D \mid \theta) P(\theta)$ | Naive Bayes Classifier, Bayesian Neural Networks, Prompt conditioning in LLMs |
| **Maximum Likelihood (MLE)** | $\hat{\theta} = \arg\max \sum \ln f(x_i \mid \theta)$ | Supervised Loss functions: Cross-Entropy Loss, NLL, MSE Loss |
| **Maximum A Posteriori (MAP)** | $\hat{\theta} = \arg\max [\ln L + \ln p(\theta)]$ | Regularization techniques: L2 Weight Decay (Gaussian prior), L1 Lasso (Laplace prior) |
| **Covariance Matrix $\mathbf{\Sigma}$** | $\mathbf{\Sigma} = E[(\mathbf{X}-\boldsymbol{\mu})(\mathbf{X}-\boldsymbol{\mu})^T]$ | Principal Component Analysis (PCA), Mahalanobis Distance, Gaussian Process Regression |
| **KL Divergence** | $D_{\text{KL}}(P \parallel Q) = \int p \ln(p/q)$ | Variational Autoencoders (ELBO Loss), PPO Policy Optimization in RL, Model Distillation |
| **Markov Property** | $P(X_{n+1} \mid X_n, \ldots) = P(X_{n+1} \mid X_n)$ | Markov Chain Monte Carlo (MCMC), Hidden Markov Models (HMM), Reinforcement Learning (MDP) |
| **Categorical / Softmax** | $p_k = \frac{e^{z_k}}{\sum_j e^{z_j}}$ | Multi-class Classification head, Token probability prediction in Transformers (LLMs) |
| **Stochastic Differential Equations (SDEs)** | $dX_t = \mu dt + \sigma dW_t$ | Score-based Generative Diffusion Models (DDPM, SDEdit, Stable Diffusion) |

---

## References

- Ross, S. *A First Course in Probability*, 10th Edition. Pearson, 2018.
- Blitzstein, J. K., & Hwang, J. *Introduction to Probability*, 2nd Edition. CRC Press, 2019.
- Billingsley, P. *Probability and Measure*, 3rd Edition. Wiley, 1995.
- Feller, W. *An Introduction to Probability Theory and Its Applications*, Volumes 1 & 2. Wiley, 1968/1971.
- Bertsekas, D. & Tsitsiklis, J. *Introduction to Probability*, 2nd Edition. Athena Scientific, 2008.
- Wasserman, L. *All of Statistics: A Concise Course in Statistical Inference*. Springer, 2004.
- Casella, G., & Berger, R. L. *Statistical Inference*, 2nd Edition. Cengage Learning, 2002.
- Lehmann, E. L., & Casella, G. *Theory of Point Estimation*, 2nd Edition. Springer, 1998.
- Bishop, C. M. *Pattern Recognition and Machine Learning*. Springer, 2006.
- Goodfellow, I., Bengio, Y., & Courville, A. *Deep Learning*. MIT Press, 2016.
- Cover, T. M., & Thomas, J. A. *Elements of Information Theory*, 2nd Edition. Wiley-Interscience, 2006.
- Oksendal, B. *Stochastic Differential Equations: An Introduction with Applications*, 6th Edition. Springer, 2003.
