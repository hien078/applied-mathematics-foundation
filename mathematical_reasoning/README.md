# Mathematical Reasoning

Every other area of this repository states theorems, imposes hypotheses, and asks you to
follow a derivation. This area is where you learn to check one.

It develops the six things a reader needs before the first proof in `linear_algebra` or
`calculus` can be read critically: the logic that gives a sentence a definite truth value,
the set-theoretic vocabulary every later object is built from, the standard proof templates,
induction and recursion, finite counting, and asymptotic growth.

The intended reader can compute but has not been trained to argue — someone who can
differentiate a loss but cannot yet say what "gradient descent converges" would have to
mean, which hypotheses it needs, or what single example would refute it.

This area is the root of the repository's dependency graph. Nothing here depends on anything
else; almost everything elsewhere depends on something here.

---

## Prerequisites

None. This area is the entry point to the curriculum.

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
It is the single source of truth for module order, and it places these six modules first.

Areas that depend on this one:

- [`../calculus/`](../calculus/) — quantifier negation for epsilon-delta arguments, and induction for series
- [`../linear_algebra/`](../linear_algebra/) — set proofs by double inclusion, and proof-shape selection
- [`../probability_statistics/`](../probability_statistics/) — counting, inclusion-exclusion, and set algebra
- [`../graph_theory/`](../graph_theory/) — induction, counting, and recurrence solving for algorithm analysis
- [`../numerical_computing/`](../numerical_computing/) — proof technique, and asymptotics for cost models

---

## Module index

| Module | What it covers | Prerequisites | Problems |
|---|---|---|:---:|
| [`01_propositional_and_predicate_logic/`](01_propositional_and_predicate_logic/) | Connectives and truth-table semantics; logical equivalence, tautology, contradiction; De Morgan, contrapositive, implication as disjunction, distributivity; predicates, $\forall$ and $\exists$, quantifier negation, quantifier order; CNF and the SAT connection | none | 20 |
| [`02_sets_relations_and_functions/`](02_sets_relations_and_functions/) | Set algebra and De Morgan for sets; element-chasing proofs; relations, equivalence relations, partitions; functions, injections, surjections, bijections, composition; cardinality and Cantor's theorem by diagonalization | 01 | 20 |
| [`03_proof_techniques/`](03_proof_techniques/) | Direct proof, contrapositive, contradiction, cases, existence and uniqueness, nonconstructive existence, refutation by counterexample; a technique-selection guide; irrationality of $\sqrt{2}$, Euclid's infinitude of primes, the triangle inequality | 01, 02 | 20 |
| [`04_induction_and_recursion/`](04_induction_and_recursion/) | Weak induction, strong induction, well-ordering, and the proof that the three are equivalent; recursive definitions; structural induction on full binary trees; linear homogeneous recurrences by characteristic roots; loop invariants; Binet's formula by generating function | 03 | 20 |
| [`05_combinatorics_and_counting/`](05_combinatorics_and_counting/) | Sum and product rules; permutations, combinations, Pascal's rule; binomial and multinomial theorems; inclusion-exclusion; stars and bars by explicit bijection; derangements; Catalan numbers by reflection; pigeonhole and the birthday bound | 02, 04 | 20 |
| [`06_asymptotics_and_algorithmic_reasoning/`](06_asymptotics_and_algorithmic_reasoning/) | $O$, $\Omega$, $\Theta$, $o$, $\omega$ from witness constants; the growth hierarchy by limit arguments; the Master theorem derived by recursion tree; substitution and the strengthened-hypothesis trap; amortized analysis by aggregate, accounting and potential; the comparison-sorting lower bound; cost of attention, backpropagation and training | 04, 05 | 20 |
| **Total** | 6 modules | | **120** |

Counts come from `python3 tools/curriculum_stats.py --modules`.

### What this area does not cover

Earlier versions of this page listed the following as covered. They are not, and the claims
have been removed rather than softened:

- **An inference-rule calculus and soundness.** Module 01 proves modus ponens in one
  exercise. Modus tollens, the syllogisms, resolution, the quantifier instantiation rules,
  and the distinction between $\vdash$ and $\models$ appear nowhere.
- **Partial orders.** Module 02 defines the term in a single clause. There are no Hasse
  diagrams, no lattices, no maximal-element arguments, and no exercise on the topic.
- **Biconditional and TFAE proofs.** Module 03's template table has six rows and none of
  them is a biconditional; no two-direction or cyclic-implication proof exists in the module.
- **Generating functions as a counting tool.** Module 05 mentions them in one parenthetical.
  The area's only worked generating function is Binet's formula, in module 04.
- **Computability.** No Turing machine, decidability argument, halting-problem proof, or
  statement of P versus NP appears anywhere, although module 01 refers to NP-completeness.
- **Stirling's approximation as a theorem.** It is used in modules 05 and 06 and stated with
  an error term in neither.
- **Pólya's method, dimensional analysis, and Fermi estimation.** These live only in the
  legacy files described under [Companion resources](#companion-resources).

---

## Module architecture

Each `NN_slug/` directory holds exactly three files, per
[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20.

### `README.md`

Eleven sections: title, a 2-4 paragraph overview, a `> [!NOTE]` callout carrying the single
most important result, prerequisites and downstream links as relative paths, learning
outcomes, a Mermaid concept map, a notation table, a core results table, common
misconceptions, an exercise index matching the real tiers and counts, and references at
chapter-level precision.

### `first_principles.ipynb`

Theory in the WHY to INTUITION to DEFINITION to DERIVATION to EXAMPLE order of §5, with:

- executable code cells that verify each major theorem numerically
- two to four figures showing the geometry or dynamics of the central idea
- worked numerical examples with concrete small numbers
- a closing Key Takeaways cell

### `exercises.ipynb`

Twenty fully solved problems in four tiers:

- **L0** — concept checks
- **L1** — foundations
- **L2** — AI/ML and physics applications
- **L3** — challenge proofs

Each problem carries a statement, an intuition note, a full derivation, a `$$\boxed{...}$$`
answer, a key takeaway, and — where the answer is numeric or algorithmic — a code cell that
checks it.

### Current state of this area

> [!NOTE]
> The notebooks in this area do not yet contain executable code. Nothing in
> `mathematical_reasoning` runs. Treat it today as a rigorous text, not a computational one.

Measured against the contract above:

- All twelve module notebooks in this area are still markdown only: no code cells, no figures.
  The upgrade is proceeding area by area — run `python3 tools/check_module.py --all --failing`
  for the current state of the whole repository.
- No `first_principles.ipynb` here ends with a Key Takeaways cell; all six end with the
  literature-mapping section instead.
- Each module `README.md` carries six of the eleven required sections. Missing in all six:
  prerequisites and downstream links, learning outcomes, notation table, core results table,
  and a per-problem exercise index.
- The exercise notebooks do use four tiers of twenty problems, but label the third tier
  "Applications in AI/ML & CS"; §20 names that tier "AI/ML and physics applications".

An upgrade wave is adding the code cells, the figures, the Key Takeaways cells, and the
missing README sections. Until it lands, this section is what the area actually is.

---

## Notation

The register is [`../docs/notation.md`](../docs/notation.md). It is authoritative on
symbols; where a module here contradicts it, the module is what changes.

Conventions this area fixes:

| Symbol | Meaning | Ruling |
|---|---|---|
| $\mathbb{N} = \lbrace 0, 1, 2, \ldots \rbrace$ | natural numbers | includes zero |
| $\lvert A \rvert$ | cardinality | `\lvert ... \rvert`, never `\#A` |
| $\mathcal{P}(A)$ | power set | |
| $(n)_k$, $\binom{n}{k}$ | falling factorial, binomial coefficient | never $P(n, k)$ |
| $D_n$, $C_n$ | derangement count, Catalan number | |
| $\vdash$, $\models$ | derivability, semantic entailment | |
| $T(n) = aT(n/b) + f(n)$ | divide-and-conquer recurrence | |
| $\alpha = \log_b a$ | Master-theorem exponent | local to module 06 |
| $O$, $\Omega$, $\Theta$, $o$, $\omega$ | asymptotics | bare capitals, not `\mathcal{O}` |

Two notes a reader should carry:

Module 05 still writes permutation counts as $P(n, k)$ in seven places in
`first_principles.ipynb` and once in its README. The register rules for $(n)_k$; that
migration is outstanding.

Module 06 is the only place in the repository where $\Omega$ and $\Theta$ are asymptotic
symbols. In `probability_statistics` the same two letters denote a sample space and a
parameter set.

---

## Suggested order

Read the modules in numerical order. The dependencies are real, not decorative.

1. **01** — logic first, because every later definition is a quantified sentence and every
   later proof technique is a propositional equivalence turned into a writing template.
2. **02** — sets next, because relations and functions are defined *as* sets, and because
   Cantor's theorem is the first place the logic pays off in something surprising.
3. **03** — the proof templates, which are 01's equivalences applied to 02's objects.
4. **04** — induction, the technique 03 deliberately defers; it needs the templates first.
5. **05** — counting, which uses bijections from 02 and induction from 04.
6. **06** — asymptotics, which needs 04's recurrences and 05's factorial estimates.

Two shorter paths, for readers who arrive with a specific destination:

- Heading to [`../probability_statistics/`](../probability_statistics/): 01, 02, 05.
- Heading to [`../numerical_computing/`](../numerical_computing/) or
  [`../graph_theory/`](../graph_theory/): 03, 04, 06.

---

## Companion resources

Two legacy files sit at the area root. They predate the numbered modules, are not part of the
§20 contract, and are not maintained against it. They are kept because parts of their content
have no counterpart in any module.

| File | What it actually contains |
|---|---|
| [`first_principles.md`](first_principles.md) | A 643-line single-file theory document in seven sections: propositional logic, predicate logic, proof techniques, set theory basics, mathematical induction, problem-solving strategies, and connection to modeling. Sections 1-5 are superseded by modules 01-04 and are shallower than them. Section 6 (Pólya's four phases, dimensional analysis, Fermi estimation, checking limiting cases) and Section 7 have no counterpart in any numbered module. |
| [`computation.ipynb`](computation.ipynb) | A 42-cell notebook — 22 code cells, 20 markdown cells, 21 code cells carrying stored output — and the only file in this area whose code executes. It imports NumPy, SymPy and `itertools` and covers: SymPy truth tables and equivalence verification, numerical checks of three summation formulas, Cartesian products and relation/function property tests, and worked problem-solving examples. It has no figures, does not use the seeded `rng` preamble of §21, and is referenced by no module. |

Neither file is a substitute for a module, and neither has been checked against the audit
that produced this rewrite.

Sibling areas that consume this one most directly:

- [`../probability_statistics/`](../probability_statistics/) — where counting becomes measure
- [`../graph_theory/`](../graph_theory/) — where induction and asymptotics meet discrete structures
- [`../numerical_methods/`](../numerical_methods/) — where convergence proofs are put to work

---

## References

Benchmark texts for this area, per [`../CLAUDE.md`](../CLAUDE.md), with the chapters each
module is measured against:

**Velleman, D. J.** (2019). *How to Prove It: A Structured Approach*, 3rd ed. Cambridge.

- Ch. 1-2, sentential and quantificational logic — module 01
- Ch. 3, proofs and proof strategy — module 03
- Ch. 4-5, relations and functions — module 02
- Ch. 6, mathematical induction — module 04
- Ch. 7, infinite sets — module 02

**Rosen, K. H.** (2019). *Discrete Mathematics and Its Applications*, 8th ed. McGraw-Hill.

- Ch. 1, logic and proofs; 1.6 rules of inference; 1.7-1.8 proof methods — modules 01 and 03
- Ch. 2, sets and functions; Ch. 9, relations — module 02
- Ch. 3 (3.2-3.3), growth of functions and complexity — module 06
- Ch. 5, induction and recursion — module 04
- Ch. 6, counting; Ch. 8.4-8.5, generating functions and inclusion-exclusion — module 05

**Graham, R. L., Knuth, D. E., & Patashnik, O.** (1994). *Concrete Mathematics*, 2nd ed.
Addison-Wesley.

- Ch. 1, recurrent problems; Ch. 2, sums — module 04
- Ch. 5, binomial coefficients; Ch. 7, generating functions — module 05
- Ch. 9, asymptotics and Stirling's approximation — module 06

Supporting texts the modules cite, at the precision they cite them:

- **Halmos, P. R.** (1960). *Naive Set Theory*. §1-§10 for sets, relations and functions;
  §22-§24 for cardinal numbers — module 02.
- **Hammack, R.** (2018). *Book of Proof*, 3rd ed. Ch. 4-9 for the proof templates;
  Ch. 10 for induction — modules 03 and 04.
- **Enderton, H. B.** (2001). *A Mathematical Introduction to Logic*, 2nd ed. Ch. 1-2, formal
  semantics of propositional and first-order logic — module 01.
- **Cormen, Leiserson, Rivest & Stein** (2022). *Introduction to Algorithms*, 4th ed. Ch. 2,
  loop invariants; Ch. 3-4, asymptotics and recurrences; Ch. 16, amortized analysis; Ch. 34,
  NP-completeness — modules 03, 04 and 06.
- **Stanley, R. P.** (2011). *Enumerative Combinatorics*, Vol. 1, 2nd ed. §1.9, the twelvefold
  way — module 05.
- **Feller, W.** (1968). *An Introduction to Probability Theory*, Vol. 1, 3rd ed. Ch. 2,
  counting and the birthday problem — module 05.
- **Sipser, M.** (2012). *Introduction to the Theory of Computation*, 3rd ed. Ch. 3-5,
  Turing machines, decidability and reducibility. Listed here as the standard for the
  computability material this area does **not** yet contain.
