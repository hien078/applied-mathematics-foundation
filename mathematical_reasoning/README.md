# Foundations of Mathematical Reasoning — Proof & Discrete Mathematics Mastery Curriculum

Welcome to the **Mathematical Reasoning Mastery Curriculum** under `foundations/mathematical_reasoning/`.

Mathematical reasoning is the meta-foundation supporting every other area of this repository: it supplies the logical toolkit for constructing valid arguments, verifying model correctness, and systematically solving problems. This module provides a comprehensive, first-principles learning system spanning propositional and predicate logic, sets/relations/functions, the full arsenal of proof techniques, induction and recursion, combinatorics and counting, and the asymptotic reasoning used to analyse algorithms. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** none — this is the entry point to the rest of the curriculum, including [Calculus](../calculus/) and [Linear Algebra](../linear_algebra/)

---

## 🗺️ Master Index of 6 Mathematical Reasoning Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Propositional & Predicate Logic | [`01_propositional_and_predicate_logic/`](01_propositional_and_predicate_logic/) | Connectives and truth tables, tautologies, logical equivalence, De Morgan's laws, quantifiers $\forall$ and $\exists$, quantifier negation and order, inference rules, soundness | 20 |
| **Topic 02** | Sets, Relations & Functions | [`02_sets_relations_and_functions/`](02_sets_relations_and_functions/) | Set algebra, power sets, Cartesian products, equivalence relations and partitions, partial orders, injections/surjections/bijections, cardinality and Cantor's theorem | 20 |
| **Topic 03** | Proof Techniques | [`03_proof_techniques/`](03_proof_techniques/) | Direct proof, contrapositive, contradiction, proof by cases, constructive vs non-constructive existence, counterexamples, biconditional and uniqueness proofs | 20 |
| **Topic 04** | Induction & Recursion | [`04_induction_and_recursion/`](04_induction_and_recursion/) | Weak and strong induction, well-ordering equivalence, structural induction, recursive definitions, recurrence relations, loop invariants and program correctness | 20 |
| **Topic 05** | Combinatorics & Counting | [`05_combinatorics_and_counting/`](05_combinatorics_and_counting/) | Product and sum rules, permutations and combinations $\binom{n}{k}$, binomial theorem, inclusion-exclusion, pigeonhole principle, stars and bars, generating functions | 20 |
| **Topic 06** | Asymptotics & Algorithmic Reasoning | [`06_asymptotics_and_algorithmic_reasoning/`](06_asymptotics_and_algorithmic_reasoning/) | Big-$O$, $\Omega$, $\Theta$ and little-$o$, limit tests, growth hierarchies, Master theorem, amortized analysis, Stirling's approximation, complexity of ML primitives | 20 |
| **TOTAL** | **6 Mathematical Reasoning Modules** | — | **Complete First-Principles Curriculum** | **120 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `06_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., De Morgan's laws, Cantor's diagonal argument, the equivalence of induction and well-ordering, the Master theorem), Computational and Algorithmic Insights, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## 🎯 Why This Is a Meta-Foundation

Every mathematical modeling topic in this repository relies on reasoning skills:

| Activity | Reasoning Skill |
|---|---|
| Stating model assumptions | Propositional logic, precise language |
| Deriving model equations | Proof techniques, algebraic manipulation |
| Proving stability or convergence | Proof by contradiction, induction |
| Checking dimensional consistency | Dimensional analysis |
| Verifying limiting cases | Logical equivalences, substitution |
| Validating correctness | Direct proof, counterexamples |
| Estimating parameters | Fermi estimation, order-of-magnitude reasoning |
| Analysing algorithm cost | Asymptotics, recurrence relations |

---

## 🔗 Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`first_principles.md`](first_principles.md) | Legacy master theory file: logic, proof techniques, set theory, induction and problem-solving strategy — the seed document the 6 modules expand upon |
| [`computation.ipynb`](computation.ipynb) | Executable companion notebook: SymPy logic manipulation, numerical induction checks, set operations, and worked examples |
| [`../probability_statistics/`](../probability_statistics/) | Sibling module where counting arguments become probability measures |
| [`../graph_theory/`](../graph_theory/) | Sibling module applying induction, counting and asymptotics to discrete structures and algorithms |
| [`../numerical_methods/`](../numerical_methods/) | Sibling module where convergence proofs and error bounds are put to work |

### Used By

**All topics in this repository** depend on this foundation — every derivation, convergence proof, and correctness argument elsewhere in the curriculum is written in the language established here.

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy `computation.ipynb` to verify logical identities and recurrences symbolically.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Velleman, D. J.** — *How to Prove It: A Structured Approach*, 3rd Edition (Cambridge University Press)
- **Rosen, K. H.** — *Discrete Mathematics and Its Applications*, 8th Edition (McGraw-Hill)
- **Graham, R. L., Knuth, D. E., & Patashnik, O.** — *Concrete Mathematics*, 2nd Edition (Addison-Wesley)
- **Halmos, P. R.** — *Naive Set Theory* (Springer)
- **Pólya, G.** — *How to Solve It* (Princeton University Press)
- **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** — *Introduction to Algorithms*, 4th Edition (MIT Press)
- **Hammack, R.** — *Book of Proof*, 3rd Edition (free online)
- **Enderton, H. B.** — *A Mathematical Introduction to Logic* (Academic Press)
- **Stanley, R. P.** — *Enumerative Combinatorics*, Volume 1 (Cambridge University Press)
