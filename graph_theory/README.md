# Foundations of Graph Theory — Graph & Network Mastery Curriculum

Welcome to the **Graph Theory Mastery Curriculum** under `foundations/graph_theory/`.

Graph theory is the mathematical language of relationships between discrete objects — social networks, transportation systems, molecular structures, and neural architectures all reduce to vertices and edges. This module provides a comprehensive, first-principles learning system spanning graph fundamentals and matrix representations, traversal and connectivity, trees and minimum spanning trees, shortest-path algorithms, network flows and matchings, the graph Laplacian and its spectrum, and modern spectral clustering and Graph Neural Network applications. Designed specifically for **Mathematical Modeling**, **AI Research**, and **Advanced Physics/Applied Mathematics**.

**Prerequisites:** [Linear Algebra](../linear_algebra/), [Calculus](../calculus/), basic set theory

---

## 🗺️ Master Index of 7 Graph Theory Modules

| Module # | Topic Name | Folder Link | Core Mathematical Focus | Exercise Count |
|---|---|---|---|:---:|
| **Topic 01** | Graph Fundamentals & Representations | [`01_graph_fundamentals_and_representations/`](01_graph_fundamentals_and_representations/) | $G = (V, E)$, order and size, handshaking lemma, adjacency/incidence matrices, adjacency lists, degree sequences, isomorphism, special graph families | 20 |
| **Topic 02** | Traversal & Connectivity | [`02_traversal_and_connectivity/`](02_traversal_and_connectivity/) | BFS and DFS trees, walks/trails/paths, connected and strongly connected components, Tarjan and Kosaraju, cut vertices, bridges, topological sort | 20 |
| **Topic 03** | Trees & Minimum Spanning Trees | [`03_trees_and_minimum_spanning_trees/`](03_trees_and_minimum_spanning_trees/) | Tree characterizations $m = n - 1$, Cayley's formula, cut and cycle properties, Kruskal and Prim correctness, union-find, Matrix-Tree theorem | 20 |
| **Topic 04** | Shortest Paths Algorithms | [`04_shortest_paths_algorithms/`](04_shortest_paths_algorithms/) | Optimal substructure, edge relaxation, Dijkstra with priority queues, Bellman-Ford and negative cycles, Floyd-Warshall, A\* admissible heuristics | 20 |
| **Topic 05** | Flows, Matchings & Bipartite Graphs | [`05_flows_matchings_and_bipartite_graphs/`](05_flows_matchings_and_bipartite_graphs/) | Residual networks, augmenting paths, max-flow min-cut theorem, Ford-Fulkerson and Edmonds-Karp, König's theorem, Hall's marriage theorem, Hungarian algorithm | 20 |
| **Topic 06** | Graph Laplacian & Spectral Theory | [`06_graph_laplacian_and_spectral_theory/`](06_graph_laplacian_and_spectral_theory/) | $L = D - A$, quadratic form and PSD-ness, algebraic connectivity $\lambda_2$, Fiedler vector, normalized Laplacians, Cheeger inequality, random walks | 20 |
| **Topic 07** | Spectral Clustering & GNN Applications | [`07_spectral_clustering_and_gnn_applications/`](07_spectral_clustering_and_gnn_applications/) | Ratio/normalized cut relaxations, Shi-Malik and Ng-Jordan-Weiss algorithms, graph convolution, message passing, over-smoothing, PageRank | 20 |
| **TOTAL** | **7 Graph Theory Modules** | — | **Complete First-Principles Curriculum** | **140 Problems** |

---

## 📚 Standard Module Architecture

Every module folder (`01_...` through `07_...`) strictly follows the 3-file standardized architecture:

1. **`README.md`**: Master Overview, First-Principles Framework, Mermaid Concept Map, Common Misconceptions Table, Directory Inventory, Canonical Literature References.
2. **`first_principles.ipynb`**: Markdown-only theory notebook — First-Principles Intuition, Rigorous Definitions and Theorem Statements, Step-by-Step Proofs and Derivations (e.g., the handshaking lemma, Kruskal's cut-property correctness, max-flow min-cut duality, the Cheeger inequality), Computational and Algorithmic Insights with complexity analysis, Real-World Physics and AI/ML Applications, Canonical Literature Mapping.
3. **`exercises.ipynb`**: **20 Fully Solved 4-Level Problems** (L0 Concept Check $\to$ L1 Foundation $\to$ L2 Applications in AI/ML & Physics $\to$ L3 Challenge) featuring intuition notes, complete step-by-step derivations, boxed final answers `$$\boxed{...}$$`, and key takeaways.

Every notebook opens with a Google Colab badge for one-click cloud reading.

---

## 🎯 Learning Objectives

After working through this curriculum you should be able to:

1. **Define and classify graphs** — directed/undirected, weighted/unweighted, simple/multi.
2. **Represent graphs mathematically** — adjacency matrices, adjacency lists, incidence matrices, and the Laplacian.
3. **Analyse graph properties** — degree sequences, connectivity, paths, cycles, cuts, and components.
4. **Understand trees** — tree characterizations, spanning trees, and minimum-spanning-tree algorithms.
5. **Apply graph algorithms** — BFS, DFS, Dijkstra, Bellman-Ford, Floyd-Warshall, max-flow, and bipartite matching.
6. **Read graph spectra** — interpret $\lambda_2$, the Fiedler vector, and normalized cuts.
7. **Connect to modeling and AI** — recognise graph structure in real problems and build spectral clustering and GNN pipelines.

---

## 🔗 Companion Resources

The original single-file foundation documents remain available and are fully compatible with the numbered curriculum:

| Resource | Description |
|---|---|
| [`first_principles.md`](first_principles.md) | Legacy master theory file: definitions, representations, properties, theorems and key results — the seed document the 7 modules expand upon |
| [`computation.ipynb`](computation.ipynb) | Executable companion notebook: interactive `networkx` examples, graph visualization, and algorithm implementations |
| [`../linear_algebra/10_matrix_calculus_graph_and_ai_applications/`](../linear_algebra/10_matrix_calculus_graph_and_ai_applications/) | Sibling module tying matrix calculus to graph and AI applications — the linear-algebraic backbone of the Laplacian spectrum |
| [`../numerical_methods/`](../numerical_methods/) | Sibling module supplying eigenvalue solvers and sparse linear algebra used by spectral methods |
| [`../optimization/`](../optimization/) | Sibling module formalising the LP/duality view behind max-flow min-cut and matching |

### Connection to Modeling

Graph theory is the essential prerequisite for:

- **Network flow models** — transportation, supply chains, max-flow/min-cut
- **Social network analysis** — centrality, clustering, community detection
- **Epidemiological models on networks** — SIR on graphs, contact tracing
- **Graph Neural Networks (GNNs)** — message passing, node classification, link prediction
- **Optimization on graphs** — shortest paths, traveling salesman, graph coloring

> **Usage:** Read each module's `first_principles.ipynb` for theory and proofs, work through `exercises.ipynb`, then run the legacy `computation.ipynb` to see the algorithms executing on real `networkx` graphs.

---

## 🏛️ Benchmark Literature References

The curriculum explicitly maps and cites top canonical literature:

- **Diestel, R.** — *Graph Theory*, 5th Edition (Springer)
- **West, D. B.** — *Introduction to Graph Theory*, 2nd Edition (Pearson)
- **Bollobás, B.** — *Modern Graph Theory* (Springer)
- **Chung, F. R. K.** — *Spectral Graph Theory* (AMS, CBMS Regional Conference Series)
- **Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C.** — *Introduction to Algorithms*, 4th Edition (MIT Press)
- **Ahuja, R. K., Magnanti, T. L., & Orlin, J. B.** — *Network Flows: Theory, Algorithms, and Applications* (Prentice Hall)
- **Hamilton, W. L.** — *Graph Representation Learning* (Morgan & Claypool)
- **Newman, M.** — *Networks: An Introduction* (Oxford University Press)
- **Bondy, J. A., & Murty, U. S. R.** — *Graph Theory* (Springer)
- **von Luxburg, U.** — *A Tutorial on Spectral Clustering* (Statistics and Computing, 2007)
- **Kipf, T. N., & Welling, M.** — *Semi-Supervised Classification with Graph Convolutional Networks* (ICLR, 2017)
