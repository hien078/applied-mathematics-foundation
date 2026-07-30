# Theory: Numerical Methods

This document covers the core numerical methods needed for mathematical modeling.
The focus is on understanding **why** each algorithm works, **when** it is appropriate,
and **how** errors propagate.

---

## 1. Floating Point Arithmetic

### 1.1 Why This Matters

Computers represent real numbers using a finite number of bits. This means:
- Not every real number can be represented exactly.
- Arithmetic operations introduce rounding errors.
- These errors can accumulate and, in worst cases, destroy the accuracy of a computation.

Understanding floating-point representation is essential for writing reliable numerical code.

### 1.2 IEEE 754 Representation

A floating-point number has the form:

$$x = \pm (1.d_1 d_2 \cdots d_p)_2 \times 2^e$$

where:
- $p$ is the number of **significand** (mantissa) bits
- $e$ is the **exponent**

| Format | Total bits | Significand bits ($p$) | Exponent bits | Decimal digits |
|--------|-----------|----------------------|---------------|----------------|
| Single (float32) | 32 | 23 | 8 | ~7 |
| Double (float64) | 64 | 52 | 11 | ~16 |

### 1.3 Machine Epsilon

The **machine epsilon** $\varepsilon_{\text{mach}}$ is the smallest number such that:

$$\text{fl}(1 + \varepsilon_{\text{mach}}) > 1$$

For double precision:

$$\boxed{\varepsilon_{\text{mach}} = 2^{-52} \approx 2.22 \times 10^{-16}}$$

This means double-precision arithmetic is accurate to about 16 significant decimal digits.

### 1.4 Rounding Errors and Catastrophic Cancellation

**Rounding error** in a single operation satisfies:

$$\text{fl}(a \mathop{\text{op}} b) = (a \mathop{\text{op}} b)(1 + \delta), \qquad |\delta| \le \varepsilon_{\text{mach}}$$

**Catastrophic cancellation** occurs when subtracting two nearly equal numbers:

$$\text{fl}(a - b) \quad \text{loses many significant digits when } a \approx b$$

**Example:** Computing $\sqrt{x^2 + 1} - x$ for large $x$ loses precision. Better:

$$\sqrt{x^2 + 1} - x = \frac{1}{\sqrt{x^2 + 1} + x}$$

The rearranged form avoids subtracting nearly equal numbers.

### 1.5 Condition Number

A problem is **well-conditioned** if small input changes produce small output changes.
The **condition number** measures this sensitivity:

$$\kappa = \left|\frac{x f'(x)}{f(x)}\right|$$

For a linear system $A\mathbf{x} = \mathbf{b}$:

$$\kappa(A) = \|A\| \cdot \|A^{-1}\|$$

**Result:** A problem with condition number $\kappa$ loses about $\log_{10} \kappa$ digits of accuracy.

$$\boxed{\text{Accurate digits} \approx 16 - \log_{10} \kappa \quad \text{(double precision)}}$$

---

## 2. Root Finding

### 2.1 Problem Statement

Given a continuous function $f: \mathbb{R} \to \mathbb{R}$, find $x^*$ such that:

$$f(x^*) = 0$$

### 2.2 Bisection Method

**Idea:** If $f(a) f(b) < 0$ (sign change), then by the Intermediate Value Theorem,
there exists a root in $[a, b]$. Halve the interval repeatedly.

**Algorithm:**
1. Set $c = \frac{a + b}{2}$
2. If $f(a) f(c) < 0$, set $b = c$; else set $a = c$
3. Repeat until $|b - a| < \varepsilon$

**Convergence:** Linear. After $n$ iterations:

$$|x_n - x^*| \le \frac{b - a}{2^n}$$

To achieve tolerance $\varepsilon$:

$$\boxed{n \ge \frac{\log(b - a) - \log \varepsilon}{\log 2}}$$

**Pros:** Always converges (guaranteed). **Cons:** Slow (gains one bit per step).

### 2.3 Newton's Method

**Idea:** Approximate $f$ by its tangent line and find where the tangent crosses zero.

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

**Convergence:** Quadratic (near a simple root):

$$|x_{n+1} - x^*| \le C |x_n - x^*|^2$$

The number of correct digits roughly doubles each iteration.

**Pros:** Very fast near the root. **Cons:** Requires $f'$; may diverge for bad initial guesses; fails if $f'(x_n) = 0$.

**Result:**

$$\boxed{x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \qquad \text{(Newton's method)}}$$

### 2.4 Secant Method

**Idea:** Replace $f'(x_n)$ in Newton's method with a finite-difference approximation:

$$x_{n+1} = x_n - f(x_n) \frac{x_n - x_{n-1}}{f(x_n) - f(x_{n-1})}$$

**Convergence:** Superlinear with order $\phi = \frac{1 + \sqrt{5}}{2} \approx 1.618$ (the golden ratio).

**Pros:** No derivative needed. **Cons:** Requires two starting points; not as fast as Newton.

### 2.5 Convergence Comparison

| Method | Order | Derivative needed? | Guaranteed? |
|--------|-------|--------------------|-------------|
| Bisection | 1 (linear) | No | Yes |
| Newton | 2 (quadratic) | Yes | No |
| Secant | 1.618 (superlinear) | No | No |

---

## 3. Interpolation

### 3.1 Problem Statement

Given data points $(x_0, y_0), (x_1, y_1), \ldots, (x_n, y_n)$, find a function $p(x)$
that passes through all the points:

$$p(x_i) = y_i, \qquad i = 0, 1, \ldots, n$$

### 3.2 Lagrange Interpolation

The unique polynomial of degree $\le n$ through $n+1$ points is:

$$p(x) = \sum_{i=0}^n y_i L_i(x)$$

where the **Lagrange basis polynomials** are:

$$L_i(x) = \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}$$

**Key property:** $L_i(x_j) = \delta_{ij}$ (equals 1 if $i = j$, 0 otherwise).

**Result:**

$$\boxed{p(x) = \sum_{i=0}^n y_i \prod_{\substack{j=0 \\ j \ne i}}^n \frac{x - x_j}{x_i - x_j}}$$

### 3.3 Newton's Divided Differences

An alternative form using **divided differences**:

$$p(x) = f[x_0] + f[x_0, x_1](x - x_0) + f[x_0, x_1, x_2](x - x_0)(x - x_1) + \cdots$$

Divided differences are defined recursively:

$$f[x_i] = y_i$$

$$f[x_i, x_{i+1}, \ldots, x_{i+k}] = \frac{f[x_{i+1}, \ldots, x_{i+k}] - f[x_i, \ldots, x_{i+k-1}]}{x_{i+k} - x_i}$$

**Advantage over Lagrange:** Adding a new data point requires only computing one new divided difference, not rebuilding the entire polynomial.

### 3.4 Interpolation Error

If $f$ is $(n+1)$ times differentiable, the error of degree-$n$ interpolation is:

$$f(x) - p(x) = \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{i=0}^n (x - x_i)$$

for some $\xi$ in the interval spanned by $x_0, \ldots, x_n, x$.

**Warning (Runge's Phenomenon):** High-degree polynomial interpolation on equally
spaced nodes can produce large oscillations near the boundaries. This motivates
Chebyshev nodes and spline interpolation.

### 3.5 Spline Interpolation

A **cubic spline** $S(x)$ satisfies:
1. $S(x)$ is a piecewise cubic polynomial on each subinterval $[x_i, x_{i+1}]$
2. $S(x_i) = y_i$ for all $i$ (interpolation)
3. $S, S', S''$ are continuous (smoothness)

Splines avoid the oscillation problems of high-degree polynomials and are the standard
choice for smooth interpolation in practice.

**Natural spline** boundary conditions: $S''(x_0) = S''(x_n) = 0$.

---

## 4. Numerical Integration (Quadrature)

### 4.1 Problem Statement

Approximate the definite integral:

$$I = \int_a^b f(x)\, dx$$

### 4.2 Trapezoidal Rule

Approximate $f$ by a piecewise linear function on $n$ subintervals of width $h = (b-a)/n$:

$$\int_a^b f(x)\, dx \approx \frac{h}{2}\bigl[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\bigr]$$

**Error:** $O(h^2)$. More precisely:

$$E_T = -\frac{(b-a)}{12} h^2 f''(\xi)$$

### 4.3 Simpson's Rule

Approximate $f$ by piecewise quadratics on pairs of subintervals ($n$ must be even):

$$\int_a^b f(x)\, dx \approx \frac{h}{3}\bigl[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 4f(x_{n-1}) + f(x_n)\bigr]$$

**Error:** $O(h^4)$ — two orders better than the trapezoidal rule!

$$E_S = -\frac{(b-a)}{180} h^4 f^{(4)}(\xi)$$

**Result:**

$$\boxed{\text{Simpson's rule: } \frac{h}{3}\bigl[f(x_0) + 4f(x_1) + 2f(x_2) + \cdots + 4f(x_{n-1}) + f(x_n)\bigr]}$$

### 4.4 Gaussian Quadrature

**Key idea:** Instead of using equally spaced nodes, choose **both the nodes and weights**
to maximize accuracy.

An $n$-point Gaussian quadrature rule:

$$\int_{-1}^1 f(x)\, dx \approx \sum_{i=1}^n w_i f(x_i)$$

is exact for all polynomials of degree $\le 2n - 1$.

The nodes $x_i$ are the roots of the Legendre polynomial $P_n(x)$, and the weights $w_i$
are determined by the integration condition.

| Points $n$ | Polynomial exactness | Nodes (on $[-1,1]$) |
|---|---|---|
| 1 | Degree 1 | $x_1 = 0$ |
| 2 | Degree 3 | $x_{1,2} = \pm 1/\sqrt{3}$ |
| 3 | Degree 5 | $0, \pm\sqrt{3/5}$ |

For integration over $[a, b]$, use the change of variables $x = \frac{b-a}{2}t + \frac{a+b}{2}$.

### 4.5 Comparison

| Method | Error order | Function evaluations ($n$ subintervals) |
|--------|-------------|-----------------------------------------|
| Trapezoidal | $O(h^2)$ | $n + 1$ |
| Simpson | $O(h^4)$ | $n + 1$ ($n$ even) |
| Gauss ($m$ pts) | $O(h^{2m})$ | $m$ per subinterval |

---

## 5. Least Squares

### 5.1 Problem Statement

Given $m$ data points $(x_i, y_i)$ and a model $y = \phi(x; \mathbf{c})$ with parameters
$\mathbf{c} = (c_0, c_1, \ldots, c_n)^T$ where $n < m$ (overdetermined), find $\mathbf{c}$
to minimize:

$$\min_{\mathbf{c}} \sum_{i=1}^m \bigl(y_i - \phi(x_i; \mathbf{c})\bigr)^2$$

### 5.2 Linear Least Squares

When $\phi$ is linear in $\mathbf{c}$ (e.g., $\phi = c_0 + c_1 x + c_2 x^2$), the
problem becomes:

$$\min_{\mathbf{c}} \|A\mathbf{c} - \mathbf{y}\|_2^2$$

where $A$ is the $m \times (n+1)$ **design matrix** (or Vandermonde matrix for polynomial fitting).

### 5.3 Normal Equations

Setting the gradient to zero:

$$A^T A \mathbf{c} = A^T \mathbf{y}$$

If $A$ has full column rank, the solution is:

**Result:**

$$\boxed{\mathbf{c} = (A^T A)^{-1} A^T \mathbf{y}}$$

**Warning:** Computing $(A^T A)^{-1}$ directly can be numerically unstable because
$\kappa(A^T A) = \kappa(A)^2$.

### 5.4 QR Factorization Approach

Factor $A = QR$ where $Q$ is $m \times (n+1)$ with orthonormal columns and $R$ is
$(n+1) \times (n+1)$ upper triangular.

Then $A^T A \mathbf{c} = A^T \mathbf{y}$ becomes $R\mathbf{c} = Q^T \mathbf{y}$, solved
by back-substitution.

**Advantages:**
- Numerically stable: $\kappa(R) = \kappa(A)$ (not squared)
- No need to form $A^T A$
- This is what `numpy.linalg.lstsq` uses internally

### 5.5 Geometric Interpretation

The least-squares solution $\hat{\mathbf{y}} = A\mathbf{c}$ is the **orthogonal projection**
of $\mathbf{y}$ onto the column space of $A$.

The residual $\mathbf{r} = \mathbf{y} - A\mathbf{c}$ is orthogonal to every column of $A$:

$$A^T \mathbf{r} = A^T(\mathbf{y} - A\mathbf{c}) = \mathbf{0}$$

This is exactly the normal equations — the algebraic and geometric views are the same.

---

## 6. Connection to Modeling

### 6.1 Root Finding in Models

Many modeling questions reduce to root finding:
- Finding **equilibria**: Solve $f(x^*) = 0$ for a dynamical system $x' = f(x)$
- Finding **break-even points**: Where does profit equal cost?
- **Implicit equations**: $F(x, y) = 0$ requires root finding for given $y$

### 6.2 Interpolation in Models

- **Tabulated data:** When a model produces values at discrete points, interpolation
  provides estimates between them
- **Basis functions:** Spline interpolation is the foundation of finite element methods
- **Surrogate models:** Interpolate expensive simulations for fast approximate evaluation

### 6.3 Quadrature in Models

- **Expected values:** $\mathbb{E}[f(X)] = \int f(x) p(x)\, dx$ requires numerical integration
- **Integral constraints:** Conservation laws often involve integrals
- **Bayesian inference:** Posterior normalization requires $\int p(y|\theta) p(\theta)\, d\theta$

### 6.4 Least Squares in Models

- **Parameter estimation:** Fit model parameters to data (curve fitting, regression)
- **System identification:** Determine parameters of a differential equation from observations
- **Machine learning:** Linear regression, polynomial regression, basis function regression

---

## Summary of Key Results

| Topic | Key Formula |
|-------|-------------|
| Machine epsilon (float64) | $\varepsilon_{\text{mach}} \approx 2.22 \times 10^{-16}$ |
| Newton's method | $x_{n+1} = x_n - f(x_n)/f'(x_n)$ |
| Bisection iterations | $n \ge (\log(b-a) - \log\varepsilon)/\log 2$ |
| Lagrange interpolation | $p(x) = \sum_i y_i \prod_{j \ne i} \frac{x - x_j}{x_i - x_j}$ |
| Simpson's rule error | $O(h^4)$ |
| Normal equations | $\mathbf{c} = (A^T A)^{-1} A^T \mathbf{y}$ |
