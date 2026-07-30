# Theory: Differential Equations

This document covers the core theory of ordinary differential equations (ODEs) needed
for mathematical modeling. We progress from definitions and classification through
solution techniques to qualitative analysis and numerical methods.

---

## 1. What Is a Differential Equation?

### 1.1 Definition

A **differential equation** is an equation that relates a function to its derivatives.

> If $y = y(t)$ is an unknown function of the independent variable $t$, then a
> differential equation is any equation involving $y$, $t$, and derivatives
> $y', y'', \ldots, y^{(n)}$.

**Example:** The equation

$$\frac{dy}{dt} = ky$$

says that the rate of change of $y$ is proportional to $y$ itself.

### 1.2 Order

The **order** of a differential equation is the highest derivative that appears.

| Equation | Order |
|----------|-------|
| $y' = ky$ | 1 |
| $y'' + \omega^2 y = 0$ | 2 |
| $y''' - y' + y = e^t$ | 3 |

### 1.3 ODE vs PDE

- **Ordinary Differential Equation (ODE):** The unknown function depends on a single
  independent variable. Example: $y'(t) = -\lambda y(t)$.
- **Partial Differential Equation (PDE):** The unknown function depends on multiple
  independent variables. Example: $\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}$.

This foundation focuses on ODEs. PDEs appear in topics like diffusion and spatial modeling.

### 1.4 Linear vs Nonlinear

An ODE is **linear** if the unknown function and all its derivatives appear to the
first power and are not multiplied together:

$$a_n(t) y^{(n)} + a_{n-1}(t) y^{(n-1)} + \cdots + a_1(t) y' + a_0(t) y = g(t)$$

Any ODE not in this form is **nonlinear**.

| Equation | Linear? | Why? |
|----------|---------|------|
| $y' + 3y = \sin t$ | Yes | $y$ and $y'$ appear linearly |
| $y'' + y = 0$ | Yes | Standard harmonic oscillator |
| $y' = y^2$ | No | $y$ appears squared |
| $y' = y(1 - y/K)$ | No | Contains $y^2/K$ term |

**Why it matters:** Linear ODEs have a complete solution theory based on superposition.
Nonlinear ODEs generally require qualitative or numerical methods.

### 1.5 Autonomous vs Non-Autonomous

An ODE is **autonomous** if $t$ does not appear explicitly on the right-hand side:

$$\frac{dy}{dt} = f(y) \qquad \text{(autonomous)}$$

$$\frac{dy}{dt} = f(t, y) \qquad \text{(non-autonomous)}$$

Autonomous equations are particularly important in modeling because their behavior
is determined entirely by the state, not by when you start observing.

### 1.6 Initial Value Problems

A differential equation together with an **initial condition** forms an
**initial value problem (IVP):**

$$\frac{dy}{dt} = f(t, y), \qquad y(t_0) = y_0$$

**Existence and Uniqueness (Picard–Lindelöf Theorem):** If $f(t, y)$ is continuous in
$t$ and Lipschitz continuous in $y$ in some rectangle around $(t_0, y_0)$, then the IVP
has a unique local solution.

This theorem tells us *when* we can trust that a model has exactly one prediction for
the future, given the present state.

---

## 2. First-Order ODEs

### 2.1 Separable Equations

A first-order ODE is **separable** if it can be written as:

$$\frac{dy}{dt} = g(t) \cdot h(y)$$

**Solution method:** Separate variables and integrate:

$$\int \frac{1}{h(y)}\, dy = \int g(t)\, dt + C$$

**Example:** Solve $\dfrac{dy}{dt} = ky$ with $y(0) = y_0$.

Separate: $\dfrac{dy}{y} = k\, dt$.

Integrate: $\ln|y| = kt + C$.

Apply initial condition: $C = \ln|y_0|$.

**Result:**

$$\boxed{y(t) = y_0 e^{kt}}$$

This is the **exponential growth/decay model** — the simplest and most fundamental
continuous-time model.

**Example:** Solve the logistic equation $\dfrac{dy}{dt} = ry\left(1 - \dfrac{y}{K}\right)$.

This is separable with $h(y) = ry(1 - y/K)$. Using partial fractions:

$$\int \frac{dy}{y(1 - y/K)} = \int \frac{dy}{y} + \int \frac{1/K}{1 - y/K}\, dy = \ln|y| - \ln|1 - y/K|$$

Setting equal to $rt + C$ and solving with $y(0) = y_0$:

**Result:**

$$\boxed{y(t) = \frac{K}{1 + \left(\frac{K - y_0}{y_0}\right) e^{-rt}}}$$

### 2.2 Linear First-Order ODEs

A **linear first-order ODE** has the standard form:

$$\frac{dy}{dt} + p(t) y = q(t)$$

**Solution by Integrating Factor:**

1. Compute the integrating factor: $\mu(t) = e^{\int p(t)\, dt}$
2. Multiply both sides by $\mu(t)$:
   $$\frac{d}{dt}\bigl[\mu(t) y\bigr] = \mu(t) q(t)$$
3. Integrate both sides:
   $$y(t) = \frac{1}{\mu(t)} \left[\int \mu(t) q(t)\, dt + C\right]$$

**Why this works:** Multiplying by $\mu(t)$ makes the left side an exact derivative,
which is the key insight of the integrating factor method.

**Example:** Solve $y' + 2y = e^{-t}$, $y(0) = 1$.

Here $p(t) = 2$, so $\mu(t) = e^{2t}$.

$$\frac{d}{dt}[e^{2t} y] = e^{2t} \cdot e^{-t} = e^t$$

$$e^{2t} y = e^t + C$$

$$y(t) = e^{-t} + C e^{-2t}$$

Apply $y(0) = 1$: $1 = 1 + C$, so $C = 0$.

**Result:**

$$\boxed{y(t) = e^{-t}}$$

### 2.3 Exact Equations (Brief Note)

An ODE $M(x,y)\, dx + N(x,y)\, dy = 0$ is **exact** if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$.

In that case, there exists a function $F(x,y)$ such that $dF = M\, dx + N\, dy$, and
the solution is $F(x,y) = C$.

This connects to the idea of conservative vector fields from multivariable calculus.

---

## 3. Second-Order Linear ODEs

### 3.1 General Form

$$a y'' + b y' + c y = g(t)$$

where $a, b, c$ are constants and $g(t)$ is a known forcing function.

- **Homogeneous** if $g(t) = 0$.
- **Non-homogeneous** if $g(t) \neq 0$.

### 3.2 Homogeneous Case: Characteristic Equation

For $ay'' + by' + cy = 0$, try $y = e^{\lambda t}$. Substituting:

$$a\lambda^2 + b\lambda + c = 0$$

This is the **characteristic equation**. Its roots determine the solution:

| Discriminant $\Delta = b^2 - 4ac$ | Roots | General Solution |
|---|---|---|
| $\Delta > 0$ | Real distinct $\lambda_1, \lambda_2$ | $y = c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$ |
| $\Delta = 0$ | Repeated $\lambda$ | $y = (c_1 + c_2 t) e^{\lambda t}$ |
| $\Delta < 0$ | Complex $\alpha \pm i\beta$ | $y = e^{\alpha t}(c_1 \cos\beta t + c_2 \sin\beta t)$ |

**Example: Simple Harmonic Oscillator.** $y'' + \omega^2 y = 0$.

Characteristic equation: $\lambda^2 + \omega^2 = 0 \implies \lambda = \pm i\omega$.

Here $\alpha = 0$, $\beta = \omega$.

**Result:**

$$\boxed{y(t) = c_1 \cos(\omega t) + c_2 \sin(\omega t)}$$

This describes undamped oscillation — the mathematical model of an ideal spring-mass
system.

**Example: Damped Oscillator.** $y'' + 2\gamma y' + \omega^2 y = 0$.

Characteristic equation: $\lambda^2 + 2\gamma\lambda + \omega^2 = 0$.

$$\lambda = -\gamma \pm \sqrt{\gamma^2 - \omega^2}$$

Three regimes:

| Condition | Behavior | Physical Meaning |
|-----------|----------|-----------------|
| $\gamma < \omega$ | Underdamped oscillation | Oscillates with decaying amplitude |
| $\gamma = \omega$ | Critically damped | Fastest non-oscillatory return |
| $\gamma > \omega$ | Overdamped | Exponential decay, no oscillation |

### 3.3 Non-Homogeneous Case: Particular Solutions

The **general solution** of $ay'' + by' + cy = g(t)$ is:

$$y = y_h + y_p$$

where $y_h$ is the general solution of the homogeneous equation and $y_p$ is any
particular solution.

**Method of Undetermined Coefficients** works when $g(t)$ is a polynomial, exponential,
sine, cosine, or combination thereof. Guess a form for $y_p$ with unknown coefficients
and substitute.

| $g(t)$ | Guess for $y_p$ |
|--------|-----------------|
| $e^{\alpha t}$ | $A e^{\alpha t}$ |
| $\sin(\beta t)$ or $\cos(\beta t)$ | $A\cos(\beta t) + B\sin(\beta t)$ |
| Polynomial of degree $n$ | Polynomial of degree $n$ |

If the guess is already part of $y_h$, multiply by $t$ (or $t^2$) until it is no longer
a solution of the homogeneous equation.

### 3.4 Superposition Principle

For linear ODEs, if $y_1$ solves $Ly = g_1$ and $y_2$ solves $Ly = g_2$, then
$c_1 y_1 + c_2 y_2$ solves $Ly = c_1 g_1 + c_2 g_2$.

This is the foundation of linear system analysis and does **not** hold for nonlinear equations.

---

## 4. Systems of ODEs

### 4.1 Motivation

Many models involve multiple interacting quantities. For example, in a predator-prey
system, we track both the prey population $x(t)$ and the predator population $y(t)$:

$$\frac{dx}{dt} = \alpha x - \beta xy, \qquad \frac{dy}{dt} = \delta xy - \gamma y$$

More generally, a **system of first-order ODEs** is:

$$\frac{d\mathbf{x}}{dt} = \mathbf{f}(t, \mathbf{x})$$

where $\mathbf{x} = (x_1, x_2, \ldots, x_n)^T \in \mathbb{R}^n$.

### 4.2 Reduction to First-Order Systems

Any higher-order ODE can be rewritten as a first-order system. For example,
$y'' + by' + cy = 0$ becomes:

$$\begin{cases} x_1 = y \\ x_2 = y' \end{cases} \implies \begin{pmatrix} x_1' \\ x_2' \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -c & -b \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$$

This is why first-order systems are the fundamental object of study.

### 4.3 Linear Systems: $\mathbf{x}' = A\mathbf{x}$

For a **constant-coefficient linear system**:

$$\frac{d\mathbf{x}}{dt} = A\mathbf{x}, \qquad \mathbf{x}(0) = \mathbf{x}_0$$

where $A$ is an $n \times n$ constant matrix.

**Solution via Eigenvalues:**

1. Find eigenvalues $\lambda_1, \ldots, \lambda_n$ and eigenvectors $\mathbf{v}_1, \ldots, \mathbf{v}_n$ of $A$.
2. If $A$ has $n$ linearly independent eigenvectors, the general solution is:

$$\mathbf{x}(t) = c_1 e^{\lambda_1 t} \mathbf{v}_1 + c_2 e^{\lambda_2 t} \mathbf{v}_2 + \cdots + c_n e^{\lambda_n t} \mathbf{v}_n$$

3. Find $c_1, \ldots, c_n$ from the initial condition.

**Result:**

$$\boxed{\mathbf{x}(t) = e^{At}\mathbf{x}_0 \quad \text{where} \quad e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!}}$$

### 4.4 Two-Dimensional Linear Systems Classification

For $\mathbf{x}' = A\mathbf{x}$ with $A \in \mathbb{R}^{2\times 2}$, the behavior is
completely determined by the eigenvalues of $A$:

| Eigenvalues | Type | Stability |
|---|---|---|
| $\lambda_1 < \lambda_2 < 0$ | Stable node | Asymptotically stable |
| $0 < \lambda_1 < \lambda_2$ | Unstable node | Unstable |
| $\lambda_1 < 0 < \lambda_2$ | Saddle point | Unstable |
| $\alpha \pm i\beta$, $\alpha < 0$ | Stable spiral | Asymptotically stable |
| $\alpha \pm i\beta$, $\alpha > 0$ | Unstable spiral | Unstable |
| $\pm i\beta$ (pure imaginary) | Center | Stable (not asymptotically) |
| $\lambda_1 = \lambda_2 < 0$ | Stable star/degenerate node | Asymptotically stable |

This classification is fundamental for understanding dynamical systems models.

---

## 5. Qualitative Analysis

When we cannot solve an ODE analytically, we can still extract important information
about the behavior of solutions.

### 5.1 Equilibrium Points

An **equilibrium** (or **fixed point**, **steady state**) of $\mathbf{x}' = \mathbf{f}(\mathbf{x})$ is a point $\mathbf{x}^*$ where:

$$\mathbf{f}(\mathbf{x}^*) = \mathbf{0}$$

At an equilibrium, the system does not change. The key question is: **is it stable?**

### 5.2 Stability Definitions

- **Stable (Lyapunov):** Solutions starting near $\mathbf{x}^*$ remain near $\mathbf{x}^*$.
- **Asymptotically stable:** Solutions starting near $\mathbf{x}^*$ converge to $\mathbf{x}^*$ as $t \to \infty$.
- **Unstable:** Not stable — some nearby solutions move away.

### 5.3 Linearization

For a nonlinear system $\mathbf{x}' = \mathbf{f}(\mathbf{x})$ near an equilibrium
$\mathbf{x}^*$, let $\mathbf{u} = \mathbf{x} - \mathbf{x}^*$ (small perturbation). Taylor expansion gives:

$$\mathbf{u}' \approx J \mathbf{u}$$

where $J = D\mathbf{f}(\mathbf{x}^*)$ is the **Jacobian matrix** evaluated at the equilibrium:

$$J_{ij} = \frac{\partial f_i}{\partial x_j}\bigg|_{\mathbf{x} = \mathbf{x}^*}$$

**Hartman–Grobman Theorem:** If all eigenvalues of $J$ have nonzero real part
(the equilibrium is **hyperbolic**), then the nonlinear system behaves qualitatively
like the linearized system near $\mathbf{x}^*$.

**Result:** The stability of $\mathbf{x}^*$ is determined by the eigenvalues of $J$:

$$\boxed{\text{Asymptotically stable} \iff \text{Re}(\lambda_i) < 0 \;\;\forall\, i}$$

### 5.4 Phase Portraits

A **phase portrait** is a diagram showing trajectories of a system in state space
(the $(x_1, x_2)$-plane for 2D systems).

Key elements:

- **Trajectories:** Curves showing how the state evolves over time
- **Equilibria:** Fixed points where trajectories converge, diverge, or orbit
- **Nullclines:** Curves where $x_1' = 0$ or $x_2' = 0$ (trajectories cross nullclines
  horizontally or vertically)
- **Separatrices:** Special trajectories that divide the phase plane into regions with
  qualitatively different behavior

Phase portraits are the primary tool for visualizing and understanding 2D dynamical systems.

### 5.5 Example: Damped Pendulum

The nonlinear pendulum with damping:

$$\ddot{\theta} + b\dot{\theta} + \sin\theta = 0$$

As a system: $x_1 = \theta$, $x_2 = \dot{\theta}$:

$$x_1' = x_2, \qquad x_2' = -\sin x_1 - bx_2$$

**Equilibria:** $x_2 = 0$ and $\sin x_1 = 0$, so $x_1 = n\pi$ for integer $n$.

- At $(0, 0)$ (hanging down): $J = \begin{pmatrix} 0 & 1 \\ -1 & -b \end{pmatrix}$.
  Eigenvalues have negative real parts for $b > 0$. → **Stable spiral** (underdamped) or **stable node** (overdamped).

- At $(\pi, 0)$ (inverted): $J = \begin{pmatrix} 0 & 1 \\ 1 & -b \end{pmatrix}$.
  Has a positive eigenvalue. → **Saddle point** (unstable).

---

## 6. Numerical Methods for ODEs

When analytical solutions are unavailable, we approximate solutions computationally.
This section provides a brief introduction; detailed treatment is in
[`foundations/numerical_methods/`](../numerical_methods/).

### 6.1 The Basic Idea

Given $y' = f(t, y)$, $y(t_0) = y_0$, and a step size $h$:

Compute a sequence of approximations $y_n \approx y(t_n)$ where $t_n = t_0 + nh$.

### 6.2 Euler's Method (Forward Euler)

The simplest approach: use the tangent line to step forward.

$$y_{n+1} = y_n + h f(t_n, y_n)$$

- **Order:** 1 (local error $O(h^2)$, global error $O(h)$)
- **Pro:** Simple to understand and implement
- **Con:** Requires very small $h$ for accuracy; can be unstable

### 6.3 Improved Euler (Heun's Method)

Predict with Euler, then correct using the average slope:

$$\tilde{y}_{n+1} = y_n + h f(t_n, y_n)$$
$$y_{n+1} = y_n + \frac{h}{2}\bigl[f(t_n, y_n) + f(t_{n+1}, \tilde{y}_{n+1})\bigr]$$

- **Order:** 2 (global error $O(h^2)$)

### 6.4 Classical Runge–Kutta (RK4)

The workhorse of ODE numerical methods:

$$k_1 = f(t_n, y_n)$$
$$k_2 = f\!\left(t_n + \frac{h}{2},\; y_n + \frac{h}{2} k_1\right)$$
$$k_3 = f\!\left(t_n + \frac{h}{2},\; y_n + \frac{h}{2} k_2\right)$$
$$k_4 = f(t_n + h,\; y_n + h k_3)$$
$$y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

- **Order:** 4 (global error $O(h^4)$)
- **Pro:** Excellent accuracy-to-cost ratio
- **Con:** Fixed step size in basic form

**Result:**

$$\boxed{y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)}$$

### 6.5 Adaptive Methods

Modern solvers (like `scipy.integrate.solve_ivp`) use **adaptive step-size control**:
they estimate the local error and adjust $h$ automatically to maintain a target accuracy.

Common adaptive methods:
- **RK45** (Dormand–Prince): embedded Runge–Kutta pair of orders 4 and 5
- **RK23**: embedded pair of orders 2 and 3
- **BDF**: implicit method for stiff problems

### 6.6 Stiffness

A problem is **stiff** when the solution has components evolving on very different time
scales. Explicit methods (Euler, RK4) require extremely small $h$ for stability on stiff
problems, even though the solution itself is smooth.

**Implicit methods** (backward Euler, BDF) are designed for stiff problems but require
solving an equation at each step.

---

## 7. Connection to Modeling

Differential equations are the mathematical language of continuous-time modeling.
Here is how the theory connects to major modeling topics:

### 7.1 Population Dynamics

| Model | ODE | Type |
|-------|-----|------|
| Exponential growth | $P' = rP$ | Separable, linear |
| Logistic growth | $P' = rP(1 - P/K)$ | Separable, nonlinear |
| Predator-prey (Lotka-Volterra) | $x' = \alpha x - \beta xy$, $y' = \delta xy - \gamma y$ | Nonlinear system |

### 7.2 Compartmental Models

The SIR epidemic model:

$$S' = -\beta SI, \qquad I' = \beta SI - \gamma I, \qquad R' = \gamma I$$

This is a nonlinear system with a conservation law: $S + I + R = N$.

### 7.3 Mechanical Systems

Newton's second law $F = ma$ gives second-order ODEs:

$$m\ddot{x} + c\dot{x} + kx = F(t)$$

This models damped, forced oscillators (springs, circuits, bridges).

### 7.4 Chemical Kinetics

Reaction rate equations are systems of ODEs. For a first-order reaction $A \to B$:

$$\frac{d[A]}{dt} = -k[A], \qquad \frac{d[B]}{dt} = k[A]$$

### 7.5 From ODEs to AI

The connection between ODEs and modern AI is deep:

- **Recurrent Neural Networks:** Discrete update $h_{t+1} = f(h_t, x_t)$ is a discrete
  dynamical system; the continuous limit leads to **Neural ODEs**.
- **Residual Networks:** $x_{l+1} = x_l + f(x_l)$ resembles an Euler step for $x' = f(x)$.
- **Gradient Flow:** Gradient descent $\theta_{k+1} = \theta_k - \eta \nabla L(\theta_k)$
  is a discretization of the gradient flow ODE $\dot{\theta} = -\nabla L(\theta)$.

---

## Summary of Key Results

| Topic | Key Result |
|-------|------------|
| Exponential growth | $y(t) = y_0 e^{kt}$ |
| Integrating factor | $\mu(t) = e^{\int p(t)\, dt}$ |
| Characteristic equation | $a\lambda^2 + b\lambda + c = 0$ |
| Linear system solution | $\mathbf{x}(t) = e^{At}\mathbf{x}_0$ |
| Stability criterion | $\text{Re}(\lambda_i) < 0$ for all eigenvalues of $J$ |
| Euler method | $y_{n+1} = y_n + hf(t_n, y_n)$ |
| RK4 | $y_{n+1} = y_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$ |
