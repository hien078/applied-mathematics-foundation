# Graph Theory

A graph is the smallest honest model of a relational system: a set of objects and a set of pairs.
This area builds that object from the definition upward and follows it as far as the spectral
machinery that modern machine learning runs on.

The order is deliberate. Counting arguments come first, then traversal, then the two great
combinatorial dualities — the cut/cycle exchange behind minimum spanning trees, and max-flow
min-cut. Only then does the Laplacian appear, which converts the earlier combinatorial questions
into questions about eigenvalues. Spectral clustering and graph neural networks are the last stop,
not the first.

It is written for readers who want the proofs. Every theorem carries its hypotheses, and every
exercise is solved in full, so the area doubles as a worked-problem book.

Read it directly on GitHub, or open any module notebook in Google Colab from the badge in its
first cell.

---

## Prerequisites

The repository-wide dependency graph is [`../docs/prerequisites.md`](../docs/prerequisites.md).
It is the source of truth, and the prerequisite column in the index below is taken from it.

Two areas feed this one, and no others:

- [`../mathematical_reasoning/`](../mathematical_reasoning/) — proof technique, counting, and the
  asymptotic notation every complexity bound here is written in.
- [`../linear_algebra/`](../linear_algebra/) — matrices as linear maps, determinants, the spectral
  theorem, and iterative eigensolvers.

---

## Module index

Prerequisite labels: a bare number is a module of this area; `reasoning/NN` and `algebra/NN` point
into `mathematical_reasoning` and `linear_algebra`.

| Module | What it covers | Prerequisites | Problems |
|---|---|---|:---:|
| [01 Graph Fundamentals and Representations](01_graph_fundamentals_and_representations/) | $G = (V,E)$, degree and neighbourhoods, isomorphism and invariants, the three representations (adjacency matrix, adjacency list, incidence matrix), canonical families, the handshaking lemma and its parity corollary, the walk-counting theorem for $(A^k)_{ij}$, and $L = BB^\top$ | [reasoning/03](../mathematical_reasoning/03_proof_techniques/), [algebra/02](../linear_algebra/02_linear_maps_and_matrix_transformations/) | 20 |
| [02 Traversal and Connectivity](02_traversal_and_connectivity/) | BFS and DFS, walks, trails and paths, components as a partition, the graph metric, topological order exists iff the digraph is acyclic, Euler's theorem, back-edge cycle detection, BFS two-colouring as a bipartiteness test | [reasoning/06](../mathematical_reasoning/06_asymptotics_and_algorithmic_reasoning/), [01](01_graph_fundamentals_and_representations/) | 20 |
| [03 Trees and Minimum Spanning Trees](03_trees_and_minimum_spanning_trees/) | The leaf lemma, tree characterisations and $m = n - 1$, the cut and cycle properties, Kruskal's correctness, Cayley's formula via the Prüfer bijection, the Matrix-Tree theorem stated | [reasoning/05](../mathematical_reasoning/05_combinatorics_and_counting/), [algebra/05](../linear_algebra/05_determinants_trace_and_matrix_polynomials/), [02](02_traversal_and_connectivity/) | 20 |
| [04 Shortest Paths Algorithms](04_shortest_paths_algorithms/) | Optimal substructure and the Bellman equation, edge relaxation, Dijkstra by induction on extraction order, Bellman–Ford with negative-cycle detection, Floyd–Warshall, the DAG sweep, and $A^{\ast}$ as Dijkstra on reduced costs | [02](02_traversal_and_connectivity/) | 20 |
| [05 Flows, Matchings and Bipartite Graphs](05_flows_matchings_and_bipartite_graphs/) | Residual networks and augmenting paths, the flow-value lemma, max-flow min-cut, integrality, the Edmonds–Karp $O(nm^2)$ bound, Berge, König via minimum cuts, Hall, Birkhoff–von Neumann, and the Hungarian primal–dual | [04](04_shortest_paths_algorithms/) | 20 |
| [06 Graph Laplacian and Spectral Theory](06_graph_laplacian_and_spectral_theory/) | $L = D - A$, the energy identity, the kernel counts components, the variational $\lambda_2$ and the Fiedler vector, the normalized spectrum in $[0,2]$, Cheeger, Matrix-Tree via Cauchy–Binet, effective resistance, and $L_{\mathrm{rw}} = I - P$ | [algebra/06](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/), [03](03_trees_and_minimum_spanning_trees/) | 20 |
| [07 Spectral Clustering and GNN Applications](07_spectral_clustering_and_gnn_applications/) | RatioCut and NCut relaxations, the trace form and Ky Fan's theorem, NCut as an escape probability, Shi–Malik and Ng–Jordan–Weiss, Chebyshev filters to the GCN propagation rule, and the over-smoothing theorem | [algebra/09](../linear_algebra/09_numerical_spectrum_algorithms/), [06](06_graph_laplacian_and_spectral_theory/) | 20 |
| **Total** | **7 modules** | — | **140** |

Counts come from `python3 tools/curriculum_stats.py --modules`.

### Known gaps

This list exists so no reader looks for material that is not here.

- **Strong-component algorithms.** Module 02 names Tarjan and Kosaraju in a complexity table and a
  citation table. Neither algorithm is written out and neither is proved. The condensation is
  proved to be a DAG in exercise L3.3 of that module.

- **Connectivity theory.** Cut vertices, bridges, blocks, vertex connectivity $\kappa$ and edge
  connectivity $\kappa'$ are defined nowhere in the area. The two symbols appear only inside a
  single bound in module 06. Menger's theorem is proved once, in exercise L3.1 of module 05, not in
  any theory notebook.

- **Minimum spanning trees.** Module 03 proves Kruskal in full. Prim's correctness is a
  one-sentence appeal to the cut property, Borůvka is a row in the comparison table, and the
  union–find $O(m\,\alpha(n))$ bound is quoted rather than derived. The Matrix-Tree theorem is
  stated in module 03 and proved in module 06.

- **Cheeger's inequality.** Module 06 proves the easy direction in full and sketches the hard
  direction, which is the direction the guarantees in module 07 rest on.

- **PageRank.** Not covered. A personalized-PageRank operator is used once without derivation, in
  exercise L2.6 of module 07.

- **Whole benchmark chapters with no home here.** Colouring, planarity, Hamiltonicity, extremal
  theory (Turán, Ramsey), random-graph models (Erdős–Rényi, the configuration model, preferential
  attachment), and the centrality family (degree, closeness, betweenness, eigenvector, Katz).

---

## Module architecture

[`../STYLE_GUIDE.md`](../STYLE_GUIDE.md) §20 is the contract, and it overrides any older convention
found in this repository. Each `NN_slug/` directory holds exactly three files.

`README.md` — the module overview, a `> [!NOTE]` callout carrying the single most important result,
prerequisites and downstream links, learning outcomes, a Mermaid concept map, a notation table, a
core-results table, common misconceptions, an exercise index matching the notebook, and references
at chapter precision.

`first_principles.ipynb` — the theory, following the WHY → INTUITION → WHAT → DEFINITION →
DERIVATION → INTERPRETATION → EXAMPLE → CONNECTION → KEY TAKEAWAYS progression of §5.

`exercises.ipynb` — fully solved problems in four tiers.

| Tier | Name | Problems per module |
|---|---|:---:|
| L0 | concept checks | 4 |
| L1 | foundations | 6 |
| L2 | AI/ML and physics applications | 6 |
| L3 | challenge proofs | 4 |

§20 requires every problem to carry a statement, an intuition block, a full derivation, a
`$$\boxed{...}$$` answer, and a key takeaway. In this area the boxed answers and key takeaways are
present in all 140 problems; the intuition blocks are not — see below.

### What is not built yet

§20 further requires each `first_principles.ipynb` to carry **executable code cells** that verify
its major theorems numerically, two to four figures showing the geometry of the central idea, and a
closing **Key Takeaways** cell; and each `exercises.ipynb` to carry a code cell wherever an answer
is numeric or algorithmic.

None of that exists in this area yet.

The fourteen module notebooks in this area are still markdown-only: no theorem here is verified
numerically, no notebook ends with a Key Takeaways cell, and no solution opens with the required
intuition block.

The upgrade is proceeding area by area. Run `python3 tools/check_module.py --all --failing` for the modules that still fall short, and `python3 tools/curriculum_stats.py` for the live code-cell and figure counts.

Until this area is reached, read the "Verification strategy" sections inside modules 02 through 07
as specifications of checks that have not yet been run.

---

## Notation

The repository-wide register is [`../docs/notation.md`](../docs/notation.md). Its graph-theory
section fixes the symbols below.

| Symbol | Meaning |
|---|---|
| $G = (V, E)$ | graph, with $n = \lvert V \rvert$ and $m = \lvert E \rvert$ |
| $A$ | adjacency matrix — inside this area $A$ is never a generic matrix |
| $D$ | degree matrix $\operatorname{diag}(d_1, \ldots, d_n)$ |
| $B$ | incidence matrix, with $L = BB^\top$ |
| $L = D - A$ | combinatorial Laplacian |
| $L_{\mathrm{sym}} = D^{-1/2} L D^{-1/2}$ | symmetric normalized Laplacian, spectrum in $[0,2]$ |
| $L_{\mathrm{rw}} = D^{-1} L = I - P$ | random-walk Laplacian |
| $P = D^{-1} A$ | random-walk operator |
| $h(G)$ | Cheeger constant or conductance |
| $\kappa(G)$, $\kappa'(G)$ | vertex and edge connectivity |
| $\tau(G)$, $\nu(G)$ | spanning-tree count, maximum matching size |
| $\delta(s, v)$ | shortest-path distance |

Three conventions are specific to this area and worth stating twice.

**Laplacian eigenvalues run ascending and are indexed from one**, so
$0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n$. This is a declared exception to the
repository's descending default; it matches Chung and von Luxburg. Under it $\lambda_2$ is the
algebraic connectivity and the Matrix-Tree theorem reads
$\tau(G) = \tfrac{1}{n}\lambda_2 \lambda_3 \cdots \lambda_n$.

**$P$ is row-stochastic**, forced by $L_{\mathrm{rw}} = I - P$. Stationarity is therefore written
$\pi^\top P = \pi^\top$, not $P\pi = \pi$.

**A Cheeger constant is meaningless without its normalization.** Name it in the same sentence as
the bound: the conductance form pairs with $\lambda_2(L_{\mathrm{sym}})$, and the
cut-size-over-vertex-count form pairs with $\lambda_2(L)$. Mixing them inside one inequality gives
a false statement.

---

## Suggested order

Modules 01 and 02 come first; everything downstream assumes both.

After that the area splits into two tracks that rejoin nowhere:

1. **Algorithmic track** — 03, then 04, then 05. Module 04 needs only 02, so it may be read before
   03 if the goal is shortest paths. Module 05 continues directly from 04.
2. **Spectral track** — 03, then 06, then 07. Module 06 needs the spanning-tree counting of 03 and
   the spectral theorem from [`../linear_algebra/06`](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/);
   module 07 needs 06 and the iterative eigensolvers of
   [`../linear_algebra/09`](../linear_algebra/09_numerical_spectrum_algorithms/).

Straight through, 01 to 07 in order satisfies both tracks.

---

## Companion resources

### Legacy files at the area root

Two files predate the numbered modules and were never removed.
[`../docs/prerequisites.md`](../docs/prerequisites.md) excludes both from the dependency graph: no
numbered module may depend on either.

[`first_principles.md`](first_principles.md) — a 544-line single-file theory document, superseded
by modules 01 through 03. It covers graphs and representations, degree, paths, connectivity,
diameter, trees and spanning trees, BFS/DFS/Dijkstra, and short sections on planar, Eulerian and
Hamiltonian graphs. Its proofs are sketches rather than the derivations the modules carry, and it
uses the zero-indexed spectrum $0 = \lambda_0 \le \cdots \le \lambda_{n-1}$, which contradicts the
notation register above. It has not been migrated.

[`computation.ipynb`](computation.ipynb) — 15 markdown cells and 22 code cells, with stored
outputs, importing `networkx`, `numpy` and `matplotlib`. It builds undirected, directed and
weighted graphs, checks the handshaking lemma numerically, draws adjacency matrices, implements
BFS, DFS, Dijkstra and a union–find MST against the `networkx` results, analyses Zachary's karate
club, and plots a gallery of standard graphs. It is the only executable file in the area.

Read it as a demonstration, not as verification. It checks none of the theorems the modules prove,
it is the sole place in the area where centrality appears — as `networkx` calls, with the notion
never defined — and no module README links to it.

### Sibling modules

| Module | Why it is relevant here |
|---|---|
| [`../linear_algebra/06`](../linear_algebra/06_eigenvalues_eigenvectors_spectral_theory/) | The spectral theorem and Rayleigh quotients that module 06 rests on |
| [`../linear_algebra/09`](../linear_algebra/09_numerical_spectrum_algorithms/) | Power, QR and Lanczos iteration — how the eigenvectors of module 07 are actually computed |
| [`../linear_algebra/10`](../linear_algebra/10_matrix_calculus_graph_and_ai_applications/) | Matrix calculus with a graph and AI slant; shares the Laplacian and spectral-clustering material |
| [`../optimization/06`](../optimization/06_kkt_conditions_and_duality/) | LP duality in general form — the abstract version of the max-flow min-cut and assignment dualities of module 05 |
| [`../optimization/07`](../optimization/07_linear_quadratic_conic_programs/) | Linear programs as objects, behind the flow and matching relaxations |

---

## References

The benchmarks for this area, named in [`../CLAUDE.md`](../CLAUDE.md), are Bollobás, Chung and
Newman. The modules are measured against them.

**Bollobás, B.** (1998). *Modern Graph Theory*. Springer GTM 184.
Ch. I fundamentals and the complement; Ch. II electrical networks; Ch. III flows, connectivity and
matching — the home of the connectivity theory this area lacks; Ch. IV–VII extremal problems,
colouring, Ramsey theory and random graphs; §VIII.5 the Matrix-Tree theorem.

**Chung, F. R. K.** (1997). *Spectral Graph Theory*. AMS CBMS Regional Conference Series 92.
Ch. 1 the normalized Laplacian and eigenvalue basics; Ch. 2 isoperimetric problems and Cheeger's
inequality; Ch. 6 expanders and eigenvalue bounds.

**Newman, M.** (2018). *Networks* (2nd ed.). Oxford University Press.
Ch. 6 the mathematics of networks, including cocitation and bipartite projections; Ch. 7 measures
and metrics — degree, closeness, betweenness, eigenvector and Katz centrality; Ch. 8 large-scale
network structure. The random-graph model chapters have no counterpart in this area.

### Supporting texts, cited by the modules at chapter level

- **Diestel, R.** (2017). *Graph Theory* (5th ed.). Springer GTM 173. — Ch. 1 basics, trees,
  connectivity and Euler tours; Ch. 2 matching, covering and packing; §6.2 flows; §8.5 expansion
  and eigenvalues.
- **West, D. B.** (2001). *Introduction to Graph Theory* (2nd ed.). Pearson. — Ch. 1 fundamental
  concepts; Ch. 2 trees and distance; Ch. 3 matchings and factors; §4.3 network flow.
- **Cormen, Leiserson, Rivest & Stein** (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
  — Ch. 19 disjoint sets; Ch. 20 elementary graph algorithms; Ch. 21 minimum spanning trees;
  Ch. 22–23 shortest paths; Ch. 24 maximum flow.
- **Ahuja, Magnanti & Orlin** (1993). *Network Flows*. Prentice Hall. — Ch. 4–5 label-setting and
  label-correcting shortest paths; Ch. 6–9 maximum flow; Ch. 12 the assignment problem.
- **Schrijver, A.** (2003). *Combinatorial Optimization: Polyhedra and Efficiency*. Springer. —
  Ch. 7 shortest paths and LP duality; Ch. 10 max-flow min-cut; Ch. 16–18 matchings, König and
  Hall.
- **Godsil, C., & Royle, G.** (2001). *Algebraic Graph Theory*. Springer GTM 207. — Ch. 8
  Laplacians and incidence matrices; Ch. 13 the Matrix-Tree theorem.
- **Brouwer, A. E., & Haemers, W. H.** (2012). *Spectra of Graphs*. Springer Universitext. —
  Ch. 1 and 3, reference spectra for standard families and interlacing.
- **von Luxburg, U.** (2007). A tutorial on spectral clustering. *Statistics and Computing* 17(4),
  395–416. — §3 the three Laplacians; §4 the algorithms; §5 the two relaxations.
- **Hamilton, W. L.** (2020). *Graph Representation Learning*. Morgan & Claypool. — Ch. 1
  traditional approaches; Ch. 5 message passing; Ch. 7 expressivity and the Weisfeiler–Leman
  ceiling.
- **Kipf, T. N., & Welling, M.** (2017). Semi-supervised classification with graph convolutional
  networks. *ICLR*.
