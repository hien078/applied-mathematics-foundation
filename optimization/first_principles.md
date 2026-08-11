# Theory: Optimization

This document covers the essential and advanced optimization theory needed for mathematical modeling and machine learning.
We progress from problem formulation and classification through unconstrained optimization (gradient, Newton, Quasi-Newton, momentum, adaptive methods), convexity and the convex hierarchy (LP, QP, SOCP, SDP), constrained optimization and general Lagrangian duality (KKT, Slater's condition), non-smooth composite optimization (subgradients, proximal operators), to discrete, non-convex, and global search strategies.

---

## 1. Optimization Problem Formulation

### 1.1 General Form

An optimization problem has the standard form:

$$\min_{\mathbf{x} \in \mathcal{D}} f(\mathbf{x})$$
$$\text{subject to } \quad g_i(\mathbf{x}) \le 0, \quad i = 1, \ldots, m$$
$$\phantom{\text{subject to }} \quad h_j(\mathbf{x}) = 0, \quad j = 1, \ldots, p$$

where:
- $f: \mathbb{R}^n \to \mathbb{R}$ is the **objective function** (what we minimize or maximize)
- $g_i: \mathbb{R}^n \to \mathbb{R}$ are **inequality constraints** ($m$ constraints)
- $h_j: \mathbb{R}^n \to \mathbb{R}$ are **equality constraints** ($p$ constraints)
- $\mathbf{x} \in \mathbb{R}^n$ is the **decision variable** (or state/parameter vector)
- $\mathcal{D} \subseteq \mathbb{R}^n$ is the domain of definition where $f, g_i, h_j$ are defined.

### 1.2 Key Terminology

- **Feasible set:** $\mathcal{F} = \{\mathbf{x} \in \mathcal{D} : g_i(\mathbf{x}) \le 0 \;(i=1\dots m),\; h_j(\mathbf{x}) = 0 \;(j=1\dots p)\}$
- **Feasible point:** Any point $\mathbf{x} \in \mathcal{F}$
- **Optimal value:** $p^* = f^* = \inf \{f(\mathbf{x}) : \mathbf{x} \in \mathcal{F}\}$ (if infeasible, $p^* = +\infty$; if unbounded below, $p^* = -\infty$)
- **Optimal point (minimizer):** Any $\mathbf{x}^* \in \mathcal{F}$ such that $f(\mathbf{x}^*) = p^*$

### 1.3 Local vs Global Optima

- **Local minimum:** $\mathbf{x}^* \in \mathcal{F}$ is a local minimum if there exists an $\epsilon > 0$ such that $f(\mathbf{x}^*) \le f(\mathbf{x})$ for all feasible $\mathbf{x}$ satisfying $\|\mathbf{x} - \mathbf{x}^*\| < \epsilon$.
- **Global minimum:** $\mathbf{x}^* \in \mathcal{F}$ is a global minimum if $f(\mathbf{x}^*) \le f(\mathbf{x})$ for all $\mathbf{x} \in \mathcal{F}$.

Finding a global minimum for general non-convex functions is NP-hard. Convexity (Section 3) guarantees that every local minimum is a global minimum.

### 1.4 Maximization

Maximizing $f(\mathbf{x})$ is mathematically equivalent to minimizing $-f(\mathbf{x})$:

$$\max_{\mathbf{x} \in \mathcal{F}} f(\mathbf{x}) \iff -\min_{\mathbf{x} \in \mathcal{F}} (-f(\mathbf{x}))$$

### 1.5 Taxonomy of Optimization Problems

Optimization problems are categorized along several key dimensions:
- **Continuous vs Discrete:** Continuous decision variables ($\mathbf{x} \in \mathbb{R}^n$) vs Discrete/Integer variables ($\mathbf{x} \in \mathbb{Z}^n$).
- **Convex vs Non-Convex:** Convex objectives and feasible sets guarantee global optimality; non-convex problems can have multiple local minima, saddle points, and flat regions.
- **Unconstrained vs Constrained:** Presence or absence of constraint functions $g_i, h_j$.
- **Smooth vs Non-Smooth:** Smooth functions have continuous gradients ($\mathcal{C}^1$ or $\mathcal{C}^2$); non-smooth functions have kinks, sharp bends, or point discontinuities (e.g., $L_1$-norm).

---

## 2. Unconstrained Optimization

Consider minimizing a smooth function $f: \mathbb{R}^n \to \mathbb{R}$ without constraints.

### 2.1 Necessary Conditions

If $f$ is continuously differentiable ($\mathcal{C}^1$) and $\mathbf{x}^*$ is a local minimum:

**First-order necessary condition (FONC):**

$$\nabla f(\mathbf{x}^*) = \mathbf{0}$$

A point satisfying $\nabla f(\mathbf{x}^*) = \mathbf{0}$ is a **stationary point** (or **critical point**).

If $f$ is twice continuously differentiable ($\mathcal{C}^2$) and $\mathbf{x}^*$ is a local minimum:

**Second-order necessary condition (SONC):**

$$\nabla f(\mathbf{x}^*) = \mathbf{0} \quad \text{and} \quad \nabla^2 f(\mathbf{x}^*) \succeq 0 \quad (\text{Hessian is positive semidefinite})$$

### 2.2 Sufficient Conditions

**Second-order sufficient condition (SOSC):**

If $\nabla f(\mathbf{x}^*) = \mathbf{0}$ and the Hessian $H(\mathbf{x}^*) = \nabla^2 f(\mathbf{x}^*)$ is **positive definite** ($H(\mathbf{x}^*) \succ 0$), then $\mathbf{x}^*$ is a **strict local minimum**.

$$\boxed{\nabla f(\mathbf{x}^*) = \mathbf{0} \;\text{ and }\; \nabla^2 f(\mathbf{x}^*) \succ 0 \;\implies\; \mathbf{x}^* \text{ is a strict local min}}$$

*Recall:* A real symmetric $n \times n$ matrix $H$ is positive definite ($H \succ 0$) if and only if all its eigenvalues are strictly positive ($\lambda_i > 0$), or equivalently $\mathbf{v}^T H \mathbf{v} > 0$ for all $\mathbf{v} \neq \mathbf{0}$.

### 2.3 Classification of Stationary Points

At any stationary point where $\nabla f(\mathbf{x}^*) = \mathbf{0}$:

| Hessian $\nabla^2 f(\mathbf{x}^*)$ | Eigenvalue Signature | Classification |
|---|---|---|
| Positive definite ($H \succ 0$) | All $\lambda_i > 0$ | Strict Local Minimum |
| Negative definite ($H \prec 0$) | All $\lambda_i < 0$ | Strict Local Maximum |
| Indefinite ($H$ has $+,\,-$) | $\lambda_{\min} < 0 < \lambda_{\max}$ | Saddle Point |
| Positive semidefinite ($H \succeq 0, \det H = 0$) | $\lambda_i \ge 0$, at least one $\lambda_i = 0$ | Inconclusive (higher-order test needed) |

### 2.4 First-Order Algorithms

#### 2.4.1 Standard Gradient Descent
Move in the direction of steepest descent $-\nabla f(\mathbf{x}_k)$:

$$\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha_k \nabla f(\mathbf{x}_k)$$

*Derivation of Direction:* The first-order Taylor expansion gives $f(\mathbf{x} + \alpha \mathbf{d}) \approx f(\mathbf{x}) + \alpha \nabla f(\mathbf{x})^T \mathbf{d}$. For a fixed unit step length $\|\mathbf{d}\|_2 = 1$, the inner product $\nabla f(\mathbf{x})^T \mathbf{d}$ is minimized when $\mathbf{d} = -\frac{\nabla f(\mathbf{x})}{\|\nabla f(\mathbf{x})\|_2}$.

*Convergence Rate:* If $f$ is $L$-smooth ($\|\nabla f(\mathbf{x}) - \nabla f(\mathbf{y})\| \le L \|\mathbf{x} - \mathbf{y}\|$) and $\mu$-strongly convex ($\nabla^2 f \succeq \mu I$), setting $\alpha = 1/L$ yields geometric (linear) convergence:

$$f(\mathbf{x}_k) - f^* \le \left(1 - \frac{\mu}{L}\right)^k (f(\mathbf{x}_0) - f^*)$$

The ratio $\kappa = \frac{L}{\mu} \ge 1$ is the **condition number**. High $\kappa$ causes severe "zig-zagging" along narrow valleys.

$$\boxed{\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha_k \nabla f(\mathbf{x}_k) \qquad \text{(Gradient Descent)}}$$

#### 2.4.2 Momentum and Accelerated Gradient Methods
To overcome ill-conditioning and oscillation:

- **Polyak Heavy-ball Momentum:** Adds physical momentum from previous velocity:
  $$\mathbf{v}_{k+1} = \beta \mathbf{v}_k + \alpha \nabla f(\mathbf{x}_k)$$
  $$\mathbf{x}_{k+1} = \mathbf{x}_k - \mathbf{v}_{k+1}$$

- **Nesterov Accelerated Gradient (NAG):** Computes gradient at the "look-ahead" point:
  $$\mathbf{v}_{k+1} = \beta \mathbf{v}_k + \alpha \nabla f(\mathbf{x}_k - \beta \mathbf{v}_k)$$
  $$\mathbf{x}_{k+1} = \mathbf{x}_k - \mathbf{v}_{k+1}$$
  NAG improves convergence rate on convex functions from $O(1/k)$ to $O(1/k^2)$.

#### 2.4.3 Stochastic Gradient Descent (SGD) and Adaptive Methods
For finite-sum objectives $f(\mathbf{x}) = \frac{1}{N}\sum_{i=1}^N f_i(\mathbf{x})$:
- **Stochastic Gradient Descent (SGD):** Uses an unbiased mini-batch estimator $g_k(\mathbf{x}_k) \approx \nabla f(\mathbf{x}_k)$ with $\mathbb{E}[g_k] = \nabla f$.
- **Adam (Adaptive Moment Estimation):** Maintains running estimates of first moment ($m_k$, mean gradient) and second moment ($v_k$, uncentered variance):
  $$m_k = \beta_1 m_{k-1} + (1-\beta_1) g_k, \quad v_k = \beta_2 v_{k-1} + (1-\beta_2) g_k^2$$
  $$\hat{m}_k = \frac{m_k}{1-\beta_1^k}, \quad \hat{v}_k = \frac{v_k}{1-\beta_2^k}, \quad \mathbf{x}_{k+1} = \mathbf{x}_k - \frac{\alpha}{\sqrt{\hat{v}_k} + \epsilon} \hat{m}_k$$

### 2.5 Step Size Selection

| Strategy | Selection Rule | Strengths & Drawbacks |
|---|---|---|
| Fixed Step Size | $\alpha_k = \alpha$ | Simple; requires $\alpha < 2/L$ to prevent divergence |
| Exact Line Search | $\alpha_k = \arg\min_{\alpha > 0} f(\mathbf{x}_k - \alpha \nabla f(\mathbf{x}_k))$ | Maximum per-step decrease; computationally expensive |
| Armijo Backtracking | Find smallest $m \ge 0$ s.t. $f(\mathbf{x}_k - \beta^m \alpha_0 \mathbf{d}_k) \le f(\mathbf{x}_k) + c_1 \beta^m \alpha_0 \nabla f(\mathbf{x}_k)^T \mathbf{d}_k$ | Highly practical, guarantees sufficient decrease ($c_1 \in (0,1), \beta \in (0,1)$) |

### 2.6 Newton's Method

Newton's method uses a local quadratic Taylor approximation of $f$ around $\mathbf{x}_k$:

$$f(\mathbf{x}_k + \mathbf{p}) \approx f(\mathbf{x}_k) + \nabla f(\mathbf{x}_k)^T \mathbf{p} + \frac{1}{2} \mathbf{p}^T \nabla^2 f(\mathbf{x}_k) \mathbf{p}$$

Minimizing this quadratic with respect to $\mathbf{p}$ yields the **Newton step** $\mathbf{p}_k = -[\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$:

$$\mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$$

- **Convergence:** Quadratic ($O(\|\mathbf{x}_k - \mathbf{x}^*\|^2)$) near the solution.
- **Drawbacks:** Computing $\nabla^2 f(\mathbf{x})$ requires $O(n^2)$ space/derivatives and solving the linear system costs $O(n^3)$ operations per iteration.

### 2.7 Quasi-Newton Methods (BFGS and L-BFGS)

Quasi-Newton methods replace the exact Hessian with an approximation $B_k \approx \nabla^2 f(\mathbf{x}_k)$ (or $H_k \approx [\nabla^2 f(\mathbf{x}_k)]^{-1}$) updated iteratively using gradient information.

Let $\mathbf{s}_k = \mathbf{x}_{k+1} - \mathbf{x}_k$ and $\mathbf{y}_k = \nabla f(\mathbf{x}_{k+1}) - \nabla f(\mathbf{x}_k)$.

**Secant Equation:** Any valid Hessian approximation must satisfy:

$$B_{k+1} \mathbf{s}_k = \mathbf{y}_k \quad \text{or equivalently} \quad H_{k+1} \mathbf{y}_k = \mathbf{s}_k$$

**BFGS Update Formula (Direct Inverse Hessian $H_k$):**

$$H_{k+1} = (I - \rho_k \mathbf{s}_k \mathbf{y}_k^T) H_k (I - \rho_k \mathbf{y}_k \mathbf{s}_k^T) + \rho_k \mathbf{s}_k \mathbf{s}_k^T, \quad \text{where } \rho_k = \frac{1}{\mathbf{y}_k^T \mathbf{s}_k}$$

- **BFGS:** Superlinear convergence; requires $O(n^2)$ memory to store $H_k$.
- **L-BFGS (Limited-memory BFGS):** Stores only the $m$ most recent vector pairs $\{(\mathbf{s}_i, \mathbf{y}_i)\}_{i=k-m}^{k-1}$ (typically $m \in [5, 20]$). Solves $H_k \nabla f(\mathbf{x}_k)$ using a two-loop recursion in $O(m n)$ time and $O(m n)$ memory. It is the workhorse solver for large-scale continuous optimization.

---

## 3. Convexity and Convex Problem Classes

Convexity ensures that any local optimum is guaranteed to be a global optimum.

### 3.1 Convex Sets

A set $C \subseteq \mathbb{R}^n$ is **convex** if for all $\mathbf{x}, \mathbf{y} \in C$ and all $\theta \in [0, 1]$:

$$\theta \mathbf{x} + (1 - \theta) \mathbf{y} \in C$$

**Examples of Convex Sets:**
- Hyperplanes: $\{\mathbf{x} : \mathbf{a}^T \mathbf{x} = b\}$
- Half-spaces: $\{\mathbf{x} : \mathbf{a}^T \mathbf{x} \le b\}$
- Norm balls: $\{\mathbf{x} : \|\mathbf{x} - \mathbf{c}\| \le r\}$
- Polyhedra: $\{\mathbf{x} : A\mathbf{x} \le \mathbf{b}\}$
- Positive Semidefinite Cone: $\mathbb{S}^n_+ = \{X \in \mathbb{R}^{n \times n} : X = X^T,\; X \succeq 0\}$

### 3.2 Convex Functions

A function $f: C \to \mathbb{R}$ on a convex set $C$ is **convex** if for all $\mathbf{x}, \mathbf{y} \in C$ and $\theta \in [0, 1]$:

$$f(\theta \mathbf{x} + (1 - \theta) \mathbf{y}) \le \theta f(\mathbf{x}) + (1 - \theta) f(\mathbf{y})$$

If strict inequality holds for all $\mathbf{x} \neq \mathbf{y}$ and $\theta \in (0, 1)$, $f$ is **strictly convex**.

### 3.3 Characterizations of Convexity

For differentiable functions:

1. **First-Order Condition:** $f$ is convex if and only if $\text{dom } f$ is convex and for all $\mathbf{x}, \mathbf{y} \in \text{dom } f$:
   $$f(\mathbf{y}) \ge f(\mathbf{x}) + \nabla f(\mathbf{x})^T (\mathbf{y} - \mathbf{x})$$
   *(Geometric meaning: the linear first-order Taylor approximation forms a global lower bound on $f$.)*

2. **Second-Order Condition:** For a $\mathcal{C}^2$ function $f$:
   $$\boxed{f \text{ is convex} \iff \nabla^2 f(\mathbf{x}) \succeq 0 \quad \forall\, \mathbf{x} \in \text{dom } f}$$

### 3.4 The Fundamental Theorem of Convex Optimization

**For any convex optimization problem (convex objective function $f$ over a convex feasible set $\mathcal{F}$):**

1. **Every local minimum is a global minimum.**
2. **If $f$ is strictly convex, the global minimizer $\mathbf{x}^*$ is unique.**

$$\boxed{f \text{ convex over convex set } \mathcal{F} \implies \text{local min} = \text{global min}}$$

### 3.5 Operations Preserving Convexity

- **Non-negative weighted sum:** $\alpha f_1 + \beta f_2$ ($\alpha, \beta \ge 0$)
- **Pointwise supremum / maximum:** $f(\mathbf{x}) = \max_{i} f_i(\mathbf{x})$
- **Affine composition:** $g(\mathbf{x}) = f(A\mathbf{x} + \mathbf{b})$ is convex if $f$ is convex.
- **Vector composition:** $f(g(\mathbf{x}))$ under appropriate monotonicity conditions.

### 3.6 Hierarchy of Convex Optimization Problems

Convex optimization problems are organized in a strict hierarchy based on expressiveness and solvability:

```text
Linear Programming (LP) ⊂ Quadratic Programming (QP) ⊂ Second-Order Cone Programming (SOCP) ⊂ Semidefinite Programming (SDP)
```

| Class | Objective $f(\mathbf{x})$ | Constraint Types | Standard Form |
|---|---|---|---|
| **LP** | Linear: $\mathbf{c}^T \mathbf{x}$ | Linear inequalities/equalities | $\min \mathbf{c}^T \mathbf{x} \;\text{s.t.}\; A\mathbf{x} \le \mathbf{b}$ |
| **QP** | Quadratic: $\frac{1}{2}\mathbf{x}^T Q \mathbf{x} + \mathbf{c}^T \mathbf{x}$ ($Q \succeq 0$) | Linear inequalities/equalities | $\min \frac{1}{2}\mathbf{x}^T Q \mathbf{x} + \mathbf{c}^T \mathbf{x} \;\text{s.t.}\; A\mathbf{x} \le \mathbf{b}$ |
| **SOCP** | Linear: $\mathbf{f}^T \mathbf{x}$ | Second-order cone constraints | $\min \mathbf{f}^T \mathbf{x} \;\text{s.t.}\; \Vert A_i \mathbf{x} + \mathbf{b}_i\Vert_2 \le \mathbf{c}_i^T \mathbf{x} + d_i$ |
| **SDP** | Linear matrix trace: $\text{tr}(C X)$ | Linear matrix inequalities (LMI) | $\min \text{tr}(C X) \;\text{s.t.}\; \text{tr}(A_i X) = b_i,\; X \succeq 0$ |

---

## 4. Constrained Optimization and Duality

Consider the general constrained problem:

$$\min_{\mathbf{x} \in \mathbb{R}^n} f(\mathbf{x}) \quad \text{s.t.} \quad g_i(\mathbf{x}) \le 0 \; (i=1\dots m), \quad h_j(\mathbf{x}) = 0 \; (j=1\dots p)$$

### 4.1 Equality Constraints and Lagrange Multipliers

For equality constraints $h_j(\mathbf{x}) = 0$:

At a constrained minimum, $\nabla f(\mathbf{x}^*)$ must lie in the span of the constraint gradients $\{\nabla h_j(\mathbf{x}^*)\}$.

Define the **Lagrangian**:

$$\mathcal{L}(\mathbf{x}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{j=1}^p \lambda_j h_j(\mathbf{x}) = f(\mathbf{x}) + \boldsymbol{\lambda}^T \mathbf{h}(\mathbf{x})$$

Stationarity condition:

$$\nabla_{\mathbf{x}} \mathcal{L} = \mathbf{0} \implies \nabla f(\mathbf{x}^*) + \sum_{j=1}^p \lambda_j \nabla h_j(\mathbf{x}^*) = \mathbf{0}$$

**Sensitivity Interpretation:** The multiplier $\lambda_j^*$ measures the marginal change in optimal cost with respect to perturbations in constraint level $h_j(\mathbf{x}) = b_j$:

$$\frac{\partial f^*}{\partial b_j} = -\lambda_j^*$$

### 4.2 KKT Conditions (Inequality & Equality Constraints)

For both inequality ($g_i \le 0$) and equality ($h_j = 0$) constraints, the **Karush–Kuhn–Tucker (KKT) conditions** state that if $\mathbf{x}^*$ is a local minimizer satisfying constraint qualifications (e.g., LICQ - Linear Independence Constraint Qualification), there exist multipliers $\boldsymbol{\mu}^* \in \mathbb{R}^m$ and $\boldsymbol{\lambda}^* \in \mathbb{R}^p$ such that:

1. **Stationarity:**
   $$\nabla f(\mathbf{x}^*) + \sum_{i=1}^m \mu_i^* \nabla g_i(\mathbf{x}^*) + \sum_{j=1}^p \lambda_j^* \nabla h_j(\mathbf{x}^*) = \mathbf{0}$$
2. **Primal Feasibility:**
   $$g_i(\mathbf{x}^*) \le 0 \quad (i=1\dots m), \qquad h_j(\mathbf{x}^*) = 0 \quad (j=1\dots p)$$
3. **Dual Feasibility:**
   $$\mu_i^* \ge 0 \quad (i=1\dots m)$$
4. **Complementary Slackness:**
   $$\mu_i^* g_i(\mathbf{x}^*) = 0 \quad (i=1\dots m)$$

$$\boxed{\text{KKT: Stationarity + Primal Feasibility + Dual Feasibility } (\boldsymbol{\mu} \ge \mathbf{0}) + \text{Complementary Slackness } (\mu_i g_i = 0)}$$

*Complementary slackness logic:* If an inequality constraint is inactive ($g_i(\mathbf{x}^*) < 0$), its multiplier must be zero ($\mu_i^* = 0$). If $\mu_i^* > 0$, the constraint must be active ($g_i(\mathbf{x}^*) = 0$).

### 4.3 General Lagrangian Duality

Define the full Lagrangian:

$$\mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda}) = f(\mathbf{x}) + \sum_{i=1}^m \mu_i g_i(\mathbf{x}) + \sum_{j=1}^p \lambda_j h_j(\mathbf{x})$$

#### 4.3.1 The Dual Function
The **Lagrange Dual Function** $g(\boldsymbol{\mu}, \boldsymbol{\lambda})$ is the infimum of the Lagrangian over $\mathbf{x}$:

$$g(\boldsymbol{\mu}, \boldsymbol{\lambda}) = \inf_{\mathbf{x} \in \mathcal{D}} \mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda})$$

*Key Property:* $g(\boldsymbol{\mu}, \boldsymbol{\lambda})$ is **concave** in $(\boldsymbol{\mu}, \boldsymbol{\lambda})$ even if the original problem $f, g_i, h_j$ is non-convex, because it is the pointwise infimum of affine functions.

#### 4.3.2 Weak Duality
For any $\boldsymbol{\mu} \ge \mathbf{0}$ and any $\boldsymbol{\lambda}$, the dual function provides a global lower bound on the primal optimal value $p^*$:

$$g(\boldsymbol{\mu}, \boldsymbol{\lambda}) \le p^*$$

The **Lagrange Dual Problem** maximizes this lower bound:

$$d^* = \max_{\boldsymbol{\mu} \ge \mathbf{0}, \boldsymbol{\lambda}} g(\boldsymbol{\mu}, \boldsymbol{\lambda})$$

**Weak Duality Theorem:**

$$d^* \le p^* \quad \implies \quad \text{Duality Gap } \Delta = p^* - d^* \ge 0$$

#### 4.3.3 Strong Duality and Slater's Condition
If $d^* = p^*$ (zero duality gap), **Strong Duality** holds.

**Slater's Condition (Sufficient Condition for Strong Duality):**
For a convex optimization problem ($\min f(\mathbf{x})$ s.t. $g_i(\mathbf{x}) \le 0$ convex, $h_j(\mathbf{x}) = A\mathbf{x} - \mathbf{b} = 0$ affine), if there exists a **strictly feasible point** $\mathbf{x}_0 \in \text{relint}(\mathcal{D})$ such that:

$$g_i(\mathbf{x}_0) < 0 \quad (i=1\dots m) \quad \text{and} \quad A\mathbf{x}_0 = \mathbf{b}$$

then strong duality holds ($d^* = p^*$) and a dual optimal solution $(\boldsymbol{\mu}^*, \boldsymbol{\lambda}^*)$ exists.

Under strong duality, KKT conditions are both **necessary and sufficient** for global optimality.

---

## 5. Linear Programming (LP)

### 5.1 Standard Form

A Linear Program in standard form:

$$\min_{\mathbf{x}} \mathbf{c}^T \mathbf{x} \quad \text{s.t.} \quad A\mathbf{x} = \mathbf{b}, \quad \mathbf{x} \ge \mathbf{0}$$

where $\mathbf{c} \in \mathbb{R}^n$, $A \in \mathbb{R}^{m \times n}$ ($m < n$), and $\mathbf{b} \in \mathbb{R}^m$.

### 5.2 Feasible Geometry and Fundamental Theorem of LP

The feasible set $\mathcal{F} = \{\mathbf{x} : A\mathbf{x} = \mathbf{b}, \mathbf{x} \ge \mathbf{0}\}$ is a convex **polyhedron**.

**Fundamental Theorem of Linear Programming:**
If a linear program has an optimal solution, then at least one extreme point (vertex) of the feasible polyhedron is optimal.

### 5.3 Simplex Method & Interior-Point Methods

- **Simplex Method (Dantzig):** Traverses connected vertices along edges of the feasible polyhedron in directions that decrease $\mathbf{c}^T \mathbf{x}$. Extremely efficient in practice ($O(n)$ average iterations), though worst-case exponential.
- **Interior-Point Methods (Karmarkar, Barrier Methods):** Move through the interior of the feasible set along the "central path" using logarithmic barrier functions. Guarantees worst-case polynomial time $O(n^{3.5} L)$.

### 5.4 LP Duality

| Primal Problem | Dual Problem |
|---|---|
| $\min_{\mathbf{x}} \mathbf{c}^T \mathbf{x}$ | $\max_{\mathbf{y}} \mathbf{b}^T \mathbf{y}$ |
| s.t. $A\mathbf{x} \ge \mathbf{b}$ | s.t. $A^T \mathbf{y} \le \mathbf{c}$ |
| $\mathbf{x} \ge \mathbf{0}$ | $\mathbf{y} \ge \mathbf{0}$ |

**Strong Duality for LP:** If either the primal or dual has a finite optimal solution, then both have optimal solutions and $\mathbf{c}^T \mathbf{x}^* = \mathbf{b}^T \mathbf{y}^*$.

---

## 6. Non-smooth and Composite Optimization

Many real-world and machine learning applications involve objective functions that are non-differentiable (e.g., $L_1$-norm regularization, LASSO, Support Vector Machine Hinge loss).

### 6.1 Subgradients and Subdifferentials

Let $f: \mathbb{R}^n \to \mathbb{R}$ be a convex function (not necessarily differentiable).

A vector $\mathbf{g} \in \mathbb{R}^n$ is a **subgradient** of $f$ at $\mathbf{x}$ if for all $\mathbf{y} \in \text{dom } f$:

$$f(\mathbf{y}) \ge f(\mathbf{x}) + \mathbf{g}^T (\mathbf{y} - \mathbf{x})$$

The **subdifferential** $\partial f(\mathbf{x})$ is the set of all subgradients of $f$ at $\mathbf{x}$:

$$\partial f(\mathbf{x}) = \{\mathbf{g} \in \mathbb{R}^n : f(\mathbf{y}) \ge f(\mathbf{x}) + \mathbf{g}^T (\mathbf{y} - \mathbf{x}) \quad \forall \mathbf{y}\}$$

- If $f$ is differentiable at $\mathbf{x}$, then $\partial f(\mathbf{x}) = \{\nabla f(\mathbf{x})\}$.
- **Optimality Condition for Non-smooth Convex Problems:**
  $$\mathbf{x}^* \text{ is a global minimizer of } f \iff \mathbf{0} \in \partial f(\mathbf{x}^*)$$

*Example ($f(x) = |x|$):*
$$\partial |x| = \begin{cases} \{1\} & x > 0 \\ \{-1\} & x < 0 \\ [-1, 1] & x = 0 \end{cases}$$
At $x^* = 0$, $0 \in [-1, 1]$, confirming $x=0$ is the global minimizer.

### 6.2 Subgradient Method
Updates take steps along an arbitrary subgradient $\mathbf{g}_k \in \partial f(\mathbf{x}_k)$:

$$\mathbf{x}_{k+1} = \mathbf{x}_k - \alpha_k \mathbf{g}_k$$

Unlike Gradient Descent, $-\mathbf{g}_k$ is not necessarily a descent direction. We track the best iterate $f_{\text{best}}^{(k)} = \min_{i \le k} f(\mathbf{x}_i)$. Convergence rate is slower: $O(1/\epsilon^2)$ iterations.

### 6.3 Proximal Operators and Proximal Gradient Descent

For composite optimization problems:

$$\min_{\mathbf{x}} f(\mathbf{x}) + g(\mathbf{x})$$

where $f$ is convex and $L$-smooth, and $g$ is convex but non-smooth (e.g., $g(\mathbf{x}) = \lambda \|\mathbf{x}\|_1$).

#### 6.3.1 Proximal Operator
The **proximal operator** of a convex function $g$ with step parameter $\gamma > 0$ is defined as:

$$\text{prox}_{\gamma g}(\mathbf{v}) = \arg\min_{\mathbf{x}} \left( g(\mathbf{x}) + \frac{1}{2\gamma} \|\mathbf{x} - \mathbf{v}\|_2^2 \right)$$

*Soft-Thresholding Operator (Proximal for $g(\mathbf{x}) = \lambda \|\mathbf{x}\|_1$):*
$$[\text{prox}_{\gamma \lambda \|\cdot\|_1}(\mathbf{v})]_i = \text{sign}(v_i) \max(|v_i| - \gamma \lambda, 0)$$

#### 6.3.2 Proximal Gradient Algorithm (ISTA / FISTA)
Combines a forward gradient step on $f$ with a backward proximal step on $g$:

$$\mathbf{x}_{k+1} = \text{prox}_{\alpha_k g}\left( \mathbf{x}_k - \alpha_k \nabla f(\mathbf{x}_k) \right)$$

- **ISTA (Iterative Soft-Thresholding Algorithm):** Convergence rate $O(1/k)$.
- **FISTA (Fast ISTA):** Incorporates Nesterov momentum to achieve optimal rate $O(1/k^2)$.

---

## 7. Discrete, Non-convex, and Global Optimization

### 7.1 Mixed-Integer Programming (MILP / MINLP)

When some or all variables are restricted to integers ($\mathbf{x} \in \mathbb{Z}^n$):

$$\min_{\mathbf{x} \in \mathbb{Z}^k \times \mathbb{R}^{n-k}} \mathbf{c}^T \mathbf{x} \quad \text{s.t.} \quad A\mathbf{x} \le \mathbf{b}$$

- **Convex Relaxation:** Dropping the integer constraint ($\mathbf{x} \in \mathbb{R}^n$) yields an LP relaxation whose optimal value $p_{\text{LP}}^*$ provides a lower bound ($p_{\text{LP}}^* \le p_{\text{IP}}^*$).
- **Branch and Bound:** Systematically partitions the search space into subproblems (branching) and prunes branches whose relaxed lower bounds exceed the best known integer solution (bounding).

### 7.2 Non-convex Optimization & Loss Landscapes

In non-convex problems (e.g., deep neural networks, phase retrieval):
- **Saddle Points:** Points where $\nabla f = \mathbf{0}$ but the Hessian has both positive and negative eigenvalues. In high dimensions, saddle points are far more prevalent than spurious local minima.
- **Escape Strategies:** Stochastic noise in SGD and perturbed gradient methods help escape strict saddle points ($\lambda_{\min}(\nabla^2 f) < 0$).

### 7.3 Derivative-Free and Global Search (Metaheuristics)

When gradient evaluation is impossible or $f$ is a noisy black-box function:

1. **Simulated Annealing (SA):** Probabilistically accepts worse solutions with probability $P(\Delta E) = \exp(-\Delta E / T)$, lowering "temperature" $T$ over time to escape local minima.
2. **Genetic Algorithms (GA):** Evolves a population of candidate solutions using selection, crossover, and mutation operators.
3. **Bayesian Optimization:** Fits a Gaussian Process (GP) surrogate model to $f(\mathbf{x})$ and uses an acquisition function (e.g., Expected Improvement - EI, Upper Confidence Bound - UCB) to balance exploration and exploitation. Ideal for hyperparameter tuning.

---

## 8. Connection to Modeling and Machine Learning

### 8.1 Parameter Estimation & Inverse Problems

Estimating parameters $\boldsymbol{\theta}$ from noisy data $y_i = h(x_i; \boldsymbol{\theta}) + \epsilon_i$:

- **Least Squares:** $\min_{\boldsymbol{\theta}} \sum_{i=1}^N (y_i - h(x_i; \boldsymbol{\theta}))^2$
- **Regularized Least Squares (Ridge / LASSO):**
  $$\min_{\boldsymbol{\theta}} \|Y - X\boldsymbol{\theta}\|_2^2 + \lambda \|\boldsymbol{\theta}\|_p^2 \quad (p=2 \text{ Ridge}, p=1 \text{ LASSO})$$
- **Maximum Likelihood Estimation (MLE):** $\max_{\boldsymbol{\theta}} \sum_{i=1}^N \log p(y_i \mid x_i; \boldsymbol{\theta})$

### 8.2 Operations Research & Resource Allocation

- **Production Planning:** Formulated as LP or MILP.
- **Portfolio Optimization (Markowitz):** Formulated as QP ($\min \mathbf{x}^T \Sigma \mathbf{x}$ s.t. $\boldsymbol{\mu}^T \mathbf{x} \ge R, \mathbf{1}^T \mathbf{x} = 1$).
- **Network Flow / Transportation:** Solved via specialized LP / Graph algorithms.

### 8.3 Machine Learning & AI Training

| Machine Learning Task | Optimization Formulation | Solver / Algorithm |
|---|---|---|
| Linear Regression | $\min_{\mathbf{w}} \frac{1}{2}\Vert X\mathbf{w} - \mathbf{y}\Vert_2^2$ | Normal Equations $(X^TX)^{-1}X^T\mathbf{y}$ or Gradient Descent |
| Logistic Regression | $\min_{\mathbf{w}} \sum_i \log(1 + e^{-y_i \mathbf{w}^T \mathbf{x}_i})$ | L-BFGS, Newton-Raphson (IRLS) |
| Support Vector Machine (SVM) | $\min_{\mathbf{w}, b} \frac{1}{2}\Vert\mathbf{w}\Vert_2^2 + C \sum_i \max(0, 1 - y_i(\mathbf{w}^T \mathbf{x}_i + b))$ | Convex QP / Sequential Minimal Optimization (SMO) |
| Deep Learning Training | $\min_{\boldsymbol{\theta}} \frac{1}{N}\sum_i \mathcal{L}(f_{\boldsymbol{\theta}}(\mathbf{x}_i), y_i)$ | SGD with Momentum, Adam, AdamW |
| Sparse Feature Selection | $\min_{\mathbf{w}} \frac{1}{2}\Vert X\mathbf{w} - \mathbf{y}\Vert_2^2 + \lambda \Vert\mathbf{w}\Vert_1$ | Proximal Gradient Descent (FISTA) |

---

## 9. Summary of Key Theoretical Results

| Topic | Primary Formulation / Result | Condition / Context |
|---|---|---|
| **FONC (Unconstrained)** | $\nabla f(\mathbf{x}^*) = \mathbf{0}$ | Necessary for smooth local min |
| **SOSC (Unconstrained)** | $\nabla f(\mathbf{x}^*) = \mathbf{0} \;\text{and}\; \nabla^2 f(\mathbf{x}^*) \succ 0$ | Sufficient for strict local min |
| **GD Convergence Rate** | $f(\mathbf{x}_k) - f^* \le \left(1 - \frac{\mu}{L}\right)^k (f(\mathbf{x}_0) - f^*)$ | $L$-smooth, $\mu$-strongly convex |
| **Newton Step** | $\mathbf{x}_{k+1} = \mathbf{x}_k - [\nabla^2 f(\mathbf{x}_k)]^{-1} \nabla f(\mathbf{x}_k)$ | Quadratic local convergence |
| **BFGS Secant Condition** | $B_{k+1} \mathbf{s}_k = \mathbf{y}_k$ | Hessian approximation update |
| **Convexity Criterion** | $\nabla^2 f(\mathbf{x}) \succeq 0 \quad \forall \mathbf{x}$ | Necessary & sufficient for $\mathcal{C}^2$ functions |
| **Convex Optimality** | Every local minimum is a global minimum | Convex objective over convex set |
| **KKT Conditions** | Stationarity + Primal Feas. + Dual Feas. + Comp. Slackness | Necessary for constrained local min |
| **Lagrange Dual Function** | $g(\boldsymbol{\mu}, \boldsymbol{\lambda}) = \inf_{\mathbf{x}} \mathcal{L}(\mathbf{x}, \boldsymbol{\mu}, \boldsymbol{\lambda})$ | Always concave in $(\boldsymbol{\mu}, \boldsymbol{\lambda})$ |
| **Strong Duality** | $d^* = p^*$ (zero duality gap) | Guaranteed by Slater's Condition |
| **Subgradient Optimality** | $\mathbf{0} \in \partial f(\mathbf{x}^*)$ | Global min for non-smooth convex $f$ |
| **Proximal Gradient Update** | $\mathbf{x}_{k+1} = \text{prox}_{\alpha g}(\mathbf{x}_k - \alpha \nabla f(\mathbf{x}_k))$ | Composite $\min f(\mathbf{x}) + g(\mathbf{x})$ |
