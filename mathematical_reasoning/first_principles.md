# Theory: Mathematical Reasoning

## Table of Contents

1. [Propositional Logic](#1-propositional-logic)
2. [Predicate Logic](#2-predicate-logic)
3. [Proof Techniques](#3-proof-techniques)
4. [Set Theory Basics](#4-set-theory-basics)
5. [Mathematical Induction](#5-mathematical-induction)
6. [Problem-Solving Strategies](#6-problem-solving-strategies)
7. [Connection to Modeling](#7-connection-to-modeling)

---

## 1. Propositional Logic

### 1.1 Statements (Propositions)

**Definition.** A **proposition** (or **statement**) is a declarative sentence that is either **true** (T) or **false** (F), but not both.

**Examples of propositions:**
- "The population at time $t = 0$ is 100." (True or false — it's a proposition)
- "Every continuous function is differentiable." (False — it's still a proposition)
- "$2 + 3 = 5$" (True)

**Non-examples:**
- "What is the growth rate?" (Question — not a proposition)
- "Solve the equation." (Command — not a proposition)
- "$x > 5$" (Depends on $x$ — this is a predicate, not a proposition)

### 1.2 Logical Connectives

Given propositions $p$ and $q$, we can form compound propositions:

| Connective | Symbol | Name | English |
|-----------|--------|------|---------|
| Negation | $\neg p$ | NOT | "not $p$" |
| Conjunction | $p \wedge q$ | AND | "$p$ and $q$" |
| Disjunction | $p \vee q$ | OR | "$p$ or $q$" (inclusive) |
| Implication | $p \to q$ | IF-THEN | "if $p$ then $q$" |
| Biconditional | $p \leftrightarrow q$ | IFF | "$p$ if and only if $q$" |

### 1.3 Truth Tables

The truth value of compound propositions is determined by the truth values of their components:

**Negation:**

| $p$ | $\neg p$ |
|-----|----------|
| T | F |
| F | T |

**Conjunction and Disjunction:**

| $p$ | $q$ | $p \wedge q$ | $p \vee q$ |
|-----|-----|-------------|------------|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

**Implication** (the most important for mathematics):

| $p$ | $q$ | $p \to q$ |
|-----|-----|-----------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |

**Key insight:** An implication $p \to q$ is false *only* when the hypothesis $p$ is true and the conclusion $q$ is false. When $p$ is false, the implication is **vacuously true** — it makes no claim.

*Modeling example:* "If the growth rate $r > 0$, then the population increases." This says nothing about what happens when $r \leq 0$.

**Biconditional:**

| $p$ | $q$ | $p \leftrightarrow q$ |
|-----|-----|----------------------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

$p \leftrightarrow q$ is true when $p$ and $q$ have the same truth value.

### 1.4 Logical Equivalences

Two propositions are **logically equivalent** ($\equiv$) if they have the same truth value in every possible case.

**Important equivalences:**

| Name | Equivalence |
|------|-------------|
| Double negation | $\neg(\neg p) \equiv p$ |
| De Morgan's laws | $\neg(p \wedge q) \equiv \neg p \vee \neg q$ |
| | $\neg(p \vee q) \equiv \neg p \wedge \neg q$ |
| Contrapositive | $(p \to q) \equiv (\neg q \to \neg p)$ |
| Implication as disjunction | $(p \to q) \equiv (\neg p \vee q)$ |
| Negation of implication | $\neg(p \to q) \equiv p \wedge \neg q$ |
| Distributivity | $p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r)$ |
| | $p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)$ |

**Result:** The contrapositive equivalence is fundamental for proofs:
$$\boxed{(p \to q) \equiv (\neg q \to \neg p)}$$

*Example:* "If $n^2$ is even, then $n$ is even" is equivalent to "If $n$ is odd, then $n^2$ is odd."

### 1.5 Tautologies and Contradictions

**Definition.** A **tautology** is a proposition that is always true (e.g., $p \vee \neg p$).

**Definition.** A **contradiction** is a proposition that is always false (e.g., $p \wedge \neg p$).

**Definition.** A **contingency** is a proposition that is neither a tautology nor a contradiction.

---

## 2. Predicate Logic

### 2.1 Predicates

**Definition.** A **predicate** is a statement involving one or more variables that becomes a proposition when the variables are assigned specific values.

**Examples:**
- $P(x): \; x > 5$ — becomes a proposition for each specific $x$
- $Q(x, y): \; x + y = 10$ — becomes a proposition for each pair $(x, y)$
- $R(t): \; P(t) \geq 0$ — "the population at time $t$ is non-negative"

The set of values the variable can take is called the **domain of discourse** (or **universe**).

### 2.2 Quantifiers

**Universal quantifier:** $\forall x \, P(x)$ means "for all $x$ in the domain, $P(x)$ is true."

**Existential quantifier:** $\exists x \, P(x)$ means "there exists at least one $x$ in the domain such that $P(x)$ is true."

**Examples in modeling:**

$$\forall t \geq 0, \; P(t) \geq 0 \quad \text{(population is always non-negative)}$$

$$\exists t^* > 0 \text{ such that } P'(t^*) = 0 \quad \text{(there is a critical point)}$$

$$\forall \epsilon > 0, \; \exists \delta > 0 \text{ such that } |x - a| < \delta \implies |f(x) - f(a)| < \epsilon \quad \text{(continuity)}$$

### 2.3 Negation of Quantifiers

Negating quantified statements swaps quantifiers:

$$\neg(\forall x \, P(x)) \equiv \exists x \, \neg P(x)$$

$$\neg(\exists x \, P(x)) \equiv \forall x \, \neg P(x)$$

**Result:**
$$\boxed{\neg(\forall x \, P(x)) \equiv \exists x \, \neg P(x)}$$

*Example:* The negation of "every equilibrium is stable" is "there exists an equilibrium that is not stable."

**Nested quantifiers:** Apply the rules from outside in:

$$\neg(\forall \epsilon > 0, \exists \delta > 0, \forall x, |x-a| < \delta \to |f(x) - f(a)| < \epsilon)$$

$$\equiv \exists \epsilon > 0, \forall \delta > 0, \exists x, |x-a| < \delta \wedge |f(x) - f(a)| \geq \epsilon$$

This is exactly the formal statement "$f$ is **not** continuous at $a$."

### 2.4 Order of Quantifiers Matters

$$\forall x \, \exists y \, (x + y = 0) \quad \text{TRUE: for each } x, \text{ take } y = -x$$

$$\exists y \, \forall x \, (x + y = 0) \quad \text{FALSE: no single } y \text{ works for all } x$$

**Rule:** $\forall x \, \exists y \, P(x,y)$ is weaker than $\exists y \, \forall x \, P(x,y)$.

---

## 3. Proof Techniques

### 3.1 Direct Proof

**Strategy:** To prove $p \to q$, assume $p$ is true and deduce that $q$ must be true through a chain of logical steps.

**Template:**

> **Theorem.** If [hypothesis], then [conclusion].
>
> **Proof.** Assume [hypothesis]. Then ... [logical steps] ... Therefore [conclusion]. $\square$

**Example.** *The sum of two even integers is even.*

**Proof.** Let $a$ and $b$ be even integers. Then $a = 2m$ and $b = 2n$ for some integers $m, n$. Therefore:

$$a + b = 2m + 2n = 2(m + n)$$

Since $m + n$ is an integer, $a + b$ is even. $\square$

### 3.2 Proof by Contradiction

**Strategy:** To prove $p$, assume $\neg p$ and derive a contradiction ($q \wedge \neg q$ for some statement $q$).

**Template:**

> **Proof.** Suppose for contradiction that [negation of claim]. Then ... [derive contradiction] ... This is a contradiction. Therefore [claim] must be true. $\square$

**Example.** *$\sqrt{2}$ is irrational.*

**Proof.** Suppose for contradiction that $\sqrt{2}$ is rational. Then $\sqrt{2} = p/q$ where $p, q$ are integers with no common factors ($\gcd(p,q) = 1$). Squaring: $2 = p^2/q^2$, so $p^2 = 2q^2$. Thus $p^2$ is even, so $p$ is even, say $p = 2k$. Then $4k^2 = 2q^2$, giving $q^2 = 2k^2$, so $q$ is also even. But then $\gcd(p,q) \geq 2$, contradicting $\gcd(p,q) = 1$. $\square$

### 3.3 Proof by Contrapositive

**Strategy:** To prove $p \to q$, prove the logically equivalent $\neg q \to \neg p$.

**Template:**

> **Proof.** We prove the contrapositive: if [not conclusion], then [not hypothesis]. Assume [not conclusion]. Then ... Therefore [not hypothesis]. $\square$

**Example.** *If $n^2$ is even, then $n$ is even.*

**Proof.** We prove the contrapositive: if $n$ is odd, then $n^2$ is odd. Assume $n$ is odd, so $n = 2k + 1$. Then:

$$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$

Since $2k^2 + 2k$ is an integer, $n^2$ is odd. $\square$

### 3.4 Proof by Cases (Exhaustion)

**Strategy:** To prove a statement, divide into cases that cover all possibilities and prove each case separately.

**Example.** *For any integer $n$, $n^2 + n$ is even.*

**Proof.** Case 1: $n$ is even. Then $n = 2k$, so $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$ is even.

Case 2: $n$ is odd. Then $n = 2k+1$, so $n^2 + n = (2k+1)^2 + (2k+1) = 4k^2 + 4k + 2 = 2(2k^2 + 2k + 1)$ is even.

In both cases $n^2 + n$ is even. $\square$

### 3.5 Existence and Uniqueness Proofs

**Existence** ($\exists$): Exhibit a specific example, or show existence indirectly.

**Uniqueness** ($\exists!$): Prove existence, then assume two objects satisfy the condition and show they must be equal.

**Example.** *There exists a unique real number $x$ such that $2x + 3 = 7$.*

**Proof.** Existence: $x = 2$ satisfies $2(2) + 3 = 7$. ✓

Uniqueness: Suppose $2a + 3 = 7$ and $2b + 3 = 7$. Then $2a = 2b$, so $a = b$. $\square$

### 3.6 Counterexample

**Strategy:** To disprove $\forall x \, P(x)$, find a single $x_0$ such that $\neg P(x_0)$.

**Example.** *Disprove: "Every continuous function is differentiable."*

**Counterexample:** $f(x) = |x|$ is continuous everywhere but not differentiable at $x = 0$. $\square$

### 3.7 Summary of Proof Techniques

| Technique | When to Use | Form |
|-----------|-------------|------|
| Direct proof | Default; hypothesis gives useful information | Assume $p$, deduce $q$ |
| Contradiction | Negation gives more to work with | Assume $\neg p$, find absurdity |
| Contrapositive | Conclusion's negation is simpler | Prove $\neg q \to \neg p$ |
| Cases | Problem naturally splits | Check all cases |
| Counterexample | Disprove universal claims | One example suffices |
| Induction | Statements about $\mathbb{N}$ | See Section 5 |

---

## 4. Set Theory Basics

### 4.1 Sets

**Definition.** A **set** is an unordered collection of distinct objects, called **elements** or **members**.

**Notation:**
- $x \in A$ means "$x$ is an element of $A$"
- $x \notin A$ means "$x$ is not an element of $A$"
- Roster notation: $A = \{1, 2, 3\}$
- Set-builder notation: $A = \{x \in \mathbb{R} : x > 0\}$

**Important sets:**
- $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$ (natural numbers)
- $\mathbb{Z} = \{\ldots, -2, -1, 0, 1, 2, \ldots\}$ (integers)
- $\mathbb{Q}$ (rationals), $\mathbb{R}$ (reals), $\mathbb{C}$ (complex numbers)
- $\emptyset = \{\}$ (empty set)

### 4.2 Set Operations

| Operation | Notation | Definition |
|-----------|----------|------------|
| Union | $A \cup B$ | $\{x : x \in A \text{ or } x \in B\}$ |
| Intersection | $A \cap B$ | $\{x : x \in A \text{ and } x \in B\}$ |
| Difference | $A \setminus B$ | $\{x : x \in A \text{ and } x \notin B\}$ |
| Complement | $\bar{A}$ or $A^c$ | $\{x \in U : x \notin A\}$ (relative to universe $U$) |
| Symmetric difference | $A \triangle B$ | $(A \setminus B) \cup (B \setminus A)$ |
| Cartesian product | $A \times B$ | $\{(a, b) : a \in A, b \in B\}$ |
| Power set | $\mathcal{P}(A)$ | $\{S : S \subseteq A\}$ |

**Key identities (analogous to logic):**

| Name | Identity |
|------|----------|
| De Morgan's | $(A \cup B)^c = A^c \cap B^c$ |
| | $(A \cap B)^c = A^c \cup B^c$ |
| Distributive | $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$ |
| | $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ |

**Connection to logic:** Set operations mirror logical connectives under the correspondence:

$$x \in A \leftrightarrow p, \quad x \in B \leftrightarrow q, \quad \cup \leftrightarrow \vee, \quad \cap \leftrightarrow \wedge, \quad {}^c \leftrightarrow \neg$$

### 4.3 Subsets and Equality

$A \subseteq B$ (subset): $\forall x, \; x \in A \to x \in B$

$A = B$ (equality): $A \subseteq B$ and $B \subseteq A$

**To prove $A = B$:** Show two inclusions ($A \subseteq B$ and $B \subseteq A$).

**Cardinality:** $|A|$ is the number of elements in a finite set $A$.

$$|A \cup B| = |A| + |B| - |A \cap B| \quad \text{(Inclusion-Exclusion)}$$

**Result:**
$$\boxed{|A \cup B| = |A| + |B| - |A \cap B|}$$

### 4.4 Relations

**Definition.** A **(binary) relation** $R$ from set $A$ to set $B$ is a subset $R \subseteq A \times B$.

We write $a \, R \, b$ or $(a, b) \in R$ to mean "$a$ is related to $b$."

**Properties of relations on a set $A$ (i.e., $R \subseteq A \times A$):**

| Property | Definition |
|----------|------------|
| Reflexive | $\forall a \in A, \; a \, R \, a$ |
| Symmetric | $a \, R \, b \implies b \, R \, a$ |
| Antisymmetric | $a \, R \, b \wedge b \, R \, a \implies a = b$ |
| Transitive | $a \, R \, b \wedge b \, R \, c \implies a \, R \, c$ |

**Equivalence relation:** reflexive + symmetric + transitive. Partitions the set into equivalence classes.

**Partial order:** reflexive + antisymmetric + transitive. (Example: $\leq$ on $\mathbb{R}$)

### 4.5 Functions

**Definition.** A **function** $f: A \to B$ is a relation $f \subseteq A \times B$ such that for each $a \in A$, there is exactly one $b \in B$ with $(a, b) \in f$.

- $A$ is the **domain**, $B$ is the **codomain**
- $f(a) = b$ means $(a, b) \in f$
- **Image/range:** $f(A) = \{f(a) : a \in A\} \subseteq B$

**Types of functions:**

| Type | Definition | Example |
|------|------------|---------|
| **Injective** (one-to-one) | $f(a_1) = f(a_2) \implies a_1 = a_2$ | $f(x) = 2x$ on $\mathbb{R}$ |
| **Surjective** (onto) | $\forall b \in B, \exists a \in A, f(a) = b$ | $f(x) = x^2$ from $\mathbb{R}$ to $[0, \infty)$ |
| **Bijective** | Both injective and surjective | $f(x) = 2x + 1$ on $\mathbb{R}$ |

**Why this matters for modeling:** Models are functions mapping inputs (parameters, initial conditions, time) to outputs (predictions). Understanding injectivity tells us whether different inputs can produce the same output (identifiability).

---

## 5. Mathematical Induction

### 5.1 Weak Induction

**Principle of Mathematical Induction.** Let $P(n)$ be a predicate defined on the natural numbers. If:

1. **Base case:** $P(n_0)$ is true for some starting value $n_0$, and
2. **Inductive step:** For all $k \geq n_0$, $P(k) \to P(k+1)$,

then $P(n)$ is true for all $n \geq n_0$.

**Intuition:** Think of dominoes. If the first one falls (base case) and each falling domino knocks down the next (inductive step), then all dominoes fall.

**Template:**

> **Proof** (by induction on $n$).
>
> **Base case** ($n = n_0$): Verify $P(n_0)$ directly.
>
> **Inductive hypothesis:** Assume $P(k)$ holds for some $k \geq n_0$.
>
> **Inductive step:** Show $P(k+1)$ holds using the inductive hypothesis.
>
> By induction, $P(n)$ holds for all $n \geq n_0$. $\square$

### 5.2 Example: Sum Formula

**Theorem.** For all $n \geq 1$:

$$1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$$

**Proof** (by induction on $n$).

**Base case** ($n = 1$): $\text{LHS} = 1$, $\text{RHS} = \frac{1 \cdot 2}{2} = 1$. ✓

**Inductive hypothesis:** Assume $\sum_{i=1}^{k} i = \frac{k(k+1)}{2}$ for some $k \geq 1$.

**Inductive step:**

$$\sum_{i=1}^{k+1} i = \left(\sum_{i=1}^{k} i\right) + (k+1) = \frac{k(k+1)}{2} + (k+1) = \frac{k(k+1) + 2(k+1)}{2} = \frac{(k+1)(k+2)}{2}$$

This is exactly $\frac{(k+1)((k+1)+1)}{2}$, so $P(k+1)$ holds. $\square$

**Result:**
$$\boxed{\sum_{i=1}^{n} i = \frac{n(n+1)}{2}}$$

### 5.3 Example: Geometric Series

**Theorem.** For $r \neq 1$ and $n \geq 0$:

$$\sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1}$$

**Proof** (by induction on $n$).

**Base case** ($n = 0$): $\text{LHS} = r^0 = 1$, $\text{RHS} = \frac{r - 1}{r - 1} = 1$. ✓

**Inductive hypothesis:** Assume $\sum_{i=0}^{k} r^i = \frac{r^{k+1} - 1}{r - 1}$ for some $k \geq 0$.

**Inductive step:**

$$\sum_{i=0}^{k+1} r^i = \frac{r^{k+1} - 1}{r - 1} + r^{k+1} = \frac{r^{k+1} - 1 + r^{k+1}(r-1)}{r - 1} = \frac{r^{k+2} - 1}{r - 1}$$

So $P(k+1)$ holds. $\square$

**Result:**
$$\boxed{\sum_{i=0}^{n} r^i = \frac{r^{n+1} - 1}{r - 1}, \quad r \neq 1}$$

### 5.4 Strong Induction

**Principle of Strong Induction.** If:

1. **Base case:** $P(n_0)$ is true, and
2. **Strong inductive step:** For all $k \geq n_0$, if $P(n_0), P(n_0+1), \ldots, P(k)$ are all true, then $P(k+1)$ is true,

then $P(n)$ is true for all $n \geq n_0$.

**Difference from weak induction:** The inductive hypothesis assumes $P(j)$ for *all* $j \leq k$, not just $P(k)$.

**Example.** *Every integer $n \geq 2$ has a prime factorization.*

**Proof** (by strong induction on $n$).

**Base case** ($n = 2$): $2$ is prime, so it is its own prime factorization. ✓

**Strong inductive step:** Assume every integer from 2 to $k$ has a prime factorization. Consider $k + 1$:

- If $k+1$ is prime, it is its own prime factorization.
- If $k+1$ is composite, then $k+1 = ab$ where $2 \leq a, b \leq k$. By the inductive hypothesis, both $a$ and $b$ have prime factorizations. Combining them gives a prime factorization of $k+1$.

By strong induction, every integer $\geq 2$ has a prime factorization. $\square$

### 5.5 Common Mistakes in Induction Proofs

| Mistake | Why It's Wrong |
|---------|---------------|
| Forgetting the base case | Without a base case, the induction has no starting point |
| Assuming $P(k+1)$ instead of proving it | Circular reasoning |
| Not using the inductive hypothesis | Then it's just a direct proof, not induction |
| Wrong direction: proving $P(k+1) \to P(k)$ | Induction goes forward, not backward |
| Assuming a specific value of $k$ | Must work for *arbitrary* $k \geq n_0$ |

---

## 6. Problem-Solving Strategies

### 6.1 Polya's Method

George Polya's *How to Solve It* (1945) proposes a four-step method:

1. **Understand the problem**
   - What are the unknowns?
   - What are the data?
   - What are the conditions?
   - Can you draw a picture? State the problem in your own words?

2. **Devise a plan**
   - Have you seen a similar problem?
   - Can you use an analogy?
   - Can you solve a simpler version first?
   - Can you work backwards from the answer?
   - Can you decompose the problem?

3. **Carry out the plan**
   - Execute step by step
   - Check each step
   - Can you see clearly that each step is correct?

4. **Look back**
   - Can you check the result?
   - Can you solve it differently?
   - Can you use the result for other problems?
   - Can you generalize?

### 6.2 Dimensional Analysis

**Principle.** In any physically meaningful equation, every term must have the same dimensions.

**Notation.** $[x]$ denotes the dimension of quantity $x$.

**Base dimensions** (SI system):

| Dimension | Symbol |
|-----------|--------|
| Length | $L$ |
| Mass | $M$ |
| Time | $T$ |
| Temperature | $\Theta$ |

**Example:** In the equation $v = v_0 + at$:

$$[v] = \frac{L}{T}, \quad [v_0] = \frac{L}{T}, \quad [a] \cdot [t] = \frac{L}{T^2} \cdot T = \frac{L}{T} \quad ✓$$

**Application to modeling:** If your model predicts population growth, the growth rate $r$ must have units of $[\text{time}]^{-1}$. If $r$ is given in $\text{year}^{-1}$ but $t$ is in days, the model will give wrong answers.

**Result:**
$$\boxed{\text{Every term in a valid equation must have identical dimensions}}$$

### 6.3 Fermi Estimation

**Idea.** Make reasonable order-of-magnitude estimates using known facts, decomposition, and rough calculations.

**Strategy:**
1. Break the problem into smaller parts
2. Estimate each part independently
3. Combine estimates (multiply, add)
4. Round to the nearest power of 10

**Example:** *How many piano tuners are in Chicago?*

- Chicago population: ~3 million
- People per household: ~2.5 → ~1.2 million households
- Fraction with pianos: ~5% → ~60,000 pianos
- Tunings per year: ~1 → 60,000 tunings/year
- Tunings per tuner per day: ~4
- Working days per year: ~250
- Tunings per tuner per year: ~1,000

Estimate: $60{,}000 / 1{,}000 = 60$ piano tuners.

(Actual number is reportedly around 100 — correct order of magnitude!)

### 6.4 Checking Limiting Cases

**Strategy.** Verify a formula by checking its behavior in extreme or simple cases.

**Example:** The formula for sum of first $n$ integers: $S(n) = \frac{n(n+1)}{2}$.

Check limiting cases:
- $S(1) = \frac{1 \cdot 2}{2} = 1$ ✓ (just the number 1)
- $S(0) = \frac{0 \cdot 1}{2} = 0$ ✓ (empty sum)
- $S(100) = \frac{100 \cdot 101}{2} = 5050$ ✓ (Gauss's famous result)
- For large $n$: $S(n) \approx \frac{n^2}{2}$, which grows quadratically ✓

### 6.5 Working with Counterexamples

When a conjecture seems true but you're unsure, actively try to construct counterexamples:

1. **Try small cases:** Test with $n = 1, 2, 3$
2. **Try boundary cases:** Test with $n = 0$, negative numbers, zero
3. **Try extreme cases:** Very large numbers, degenerate configurations
4. **Try "obvious" counterexamples:** Constant functions, identity matrices, trivial graphs

If you can't find a counterexample, that's evidence (not proof) the conjecture is true.

---

## 7. Connection to Modeling

### 7.1 Logical Structure of Assumptions

Every mathematical model is built on assumptions, which are logical statements:

$$\text{If } \underbrace{A_1 \wedge A_2 \wedge \cdots \wedge A_k}_{\text{assumptions}}, \text{ then } \underbrace{C}_{\text{conclusion (prediction)}}$$

**Understanding the implication:** When the model prediction fails ($\neg C$), the contrapositive tells us:

$$\neg C \implies \neg(A_1 \wedge \cdots \wedge A_k) \equiv \neg A_1 \vee \cdots \vee \neg A_k$$

At least one assumption must be violated. This is how we debug models.

### 7.2 Proof of Correctness in Algorithms

Algorithms used in computational modeling need correctness proofs:

- **Loop invariants** (a form of induction): Prove that a property holds before and after each iteration
- **Termination proofs:** Show the algorithm eventually stops
- **Convergence proofs:** Show that an iterative method approaches the correct answer

### 7.3 Induction in Discrete Models

Difference equations (discrete dynamical systems) are proved correct by induction:

$$P_{n+1} = (1 + r) P_n, \quad P_0 = P_0$$

**Claim:** $P_n = (1+r)^n P_0$.

**Proof by induction:** Base case: $P_0 = (1+r)^0 P_0 = P_0$. ✓

Inductive step: $P_{k+1} = (1+r)P_k = (1+r)(1+r)^k P_0 = (1+r)^{k+1} P_0$. ✓

### 7.4 Sets and Functions in Model Definition

A mathematical model is formally a function:

$$f: \underbrace{\Theta}_{\text{parameters}} \times \underbrace{X_0}_{\text{initial conditions}} \times \underbrace{\mathcal{T}}_{\text{time domain}} \to \underbrace{Y}_{\text{predictions}}$$

Understanding function properties tells us about model behavior:
- **Injectivity:** Can we uniquely recover parameters from observations? (Identifiability)
- **Surjectivity:** Can the model produce any possible observation? (Expressiveness)
- **Continuity:** Do small changes in parameters give small changes in predictions? (Stability)

### 7.5 Dimensional Analysis in Model Verification

After deriving a model equation, check dimensional consistency:

$$\frac{dP}{dt} = rP\left(1 - \frac{P}{K}\right)$$

- $[dP/dt] = \text{individuals} / \text{time}$
- $[r] = 1/\text{time}$
- $[P] = \text{individuals}$
- $[P/K]$ = dimensionless (both individuals)
- $[rP(1 - P/K)] = (1/\text{time}) \cdot \text{individuals} = \text{individuals}/\text{time}$ ✓

If dimensions don't match, there is definitely an error.

---

## Summary of Key Results

| Result | Reference |
|--------|-----------|
| Contrapositive: $(p \to q) \equiv (\neg q \to \neg p)$ | §1.4 |
| Quantifier negation: $\neg(\forall x \, P(x)) \equiv \exists x \, \neg P(x)$ | §2.3 |
| Inclusion-Exclusion: $\|A \cup B\| = \|A\| + \|B\| - \|A \cap B\|$ | §4.3 |
| Sum formula: $\sum_{i=1}^{n} i = n(n+1)/2$ | §5.2 |
| Geometric series: $\sum_{i=0}^{n} r^i = (r^{n+1}-1)/(r-1)$ | §5.3 |
| Dimensional consistency of equations | §6.2 |
