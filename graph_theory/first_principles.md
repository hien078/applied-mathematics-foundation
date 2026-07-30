# Theory: Graph Theory

## Table of Contents

1. [What is a Graph?](#1-what-is-a-graph)
2. [Graph Representations](#2-graph-representations)
3. [Graph Properties](#3-graph-properties)
4. [Trees and Spanning Trees](#4-trees-and-spanning-trees)
5. [Graph Algorithms](#5-graph-algorithms)
6. [Special Graphs](#6-special-graphs)
7. [Connection to Modeling](#7-connection-to-modeling)

---

## 1. What is a Graph?

### 1.1 Informal Motivation

Many systems consist of objects and relationships between them:
- Cities connected by roads
- People connected by friendships
- Neurons connected by synapses
- Web pages connected by hyperlinks

A **graph** captures this structure by abstracting away everything except the objects (vertices) and their pairwise connections (edges).

### 1.2 Formal Definition

**Definition (Graph).** A **graph** is an ordered pair $G = (V, E)$ where:
- $V$ is a finite, nonempty set of **vertices** (also called **nodes**),
- $E$ is a set of **edges**, each connecting a pair of vertices.

For an **undirected graph**, each edge is an unordered pair $\{u, v\}$ with $u, v \in V$.

For a **directed graph** (digraph), each edge is an ordered pair $(u, v)$, representing a directed connection from $u$ to $v$.

**Notation:**
- $|V| = n$ is the **order** of the graph (number of vertices).
- $|E| = m$ is the **size** of the graph (number of edges).

### 1.3 Types of Graphs

| Type | Definition |
|------|-----------|
| **Simple graph** | No self-loops, no multiple edges between the same pair |
| **Multigraph** | Multiple edges between the same pair allowed |
| **Directed graph (digraph)** | Edges have direction: $(u,v) \neq (v,u)$ |
| **Weighted graph** | Each edge $e$ has an associated weight $w(e) \in \mathbb{R}$ |
| **Labeled graph** | Vertices and/or edges carry labels or attributes |

### 1.4 Undirected vs Directed

In an **undirected graph**, edge $\{u, v\}$ means $u$ and $v$ are mutually connected. The edge set satisfies:

$$\{u, v\} \in E \iff \{v, u\} \in E$$

In a **directed graph**, edge $(u, v)$ means there is a connection *from* $u$ *to* $v$, but not necessarily from $v$ to $u$:

$$(u, v) \in E \;\not\!\!\!\implies (v, u) \in E$$

### 1.5 Weighted Graphs

A **weighted graph** is a triple $G = (V, E, w)$ where $w: E \to \mathbb{R}$ assigns a real number to each edge.

**Examples of weights:**
- Distance between cities (km)
- Capacity of a pipe (liters/second)
- Strength of a friendship (interaction frequency)
- Cost of a connection (dollars)

### 1.6 Subgraphs

**Definition (Subgraph).** A graph $H = (V_H, E_H)$ is a **subgraph** of $G = (V, E)$ if $V_H \subseteq V$ and $E_H \subseteq E$.

**Definition (Induced subgraph).** Given $S \subseteq V$, the **induced subgraph** $G[S]$ has vertex set $S$ and edge set $\{e \in E : \text{both endpoints of } e \text{ are in } S\}$.

---

## 2. Graph Representations

To work with graphs computationally, we need concrete data structures. Each representation has different trade-offs in space and time complexity.

### 2.1 Adjacency Matrix

**Definition.** For a graph $G = (V, E)$ with $n = |V|$ vertices labeled $1, 2, \ldots, n$, the **adjacency matrix** $A \in \{0, 1\}^{n \times n}$ is defined by:

$$A_{ij} = \begin{cases} 1 & \text{if } \{i, j\} \in E \\ 0 & \text{otherwise} \end{cases}$$

**Properties of the adjacency matrix:**

1. **Symmetry (undirected graphs):** $A = A^\top$
2. **Diagonal (simple graphs):** $A_{ii} = 0$ (no self-loops)
3. **Weighted graphs:** Replace 1 with $w(i,j)$ and 0 with $\infty$ or 0 depending on convention.
4. **Space complexity:** $O(n^2)$

**Key result:** The entry $(A^k)_{ij}$ counts the number of walks of length $k$ from vertex $i$ to vertex $j$.

**Result:**
$$\text{Number of walks of length } k \text{ from } i \text{ to } j = (A^k)_{ij}$$

**Proof sketch.** By induction on $k$:
- **Base case** ($k=1$): $(A^1)_{ij} = A_{ij}$, which is 1 if there is an edge (walk of length 1) from $i$ to $j$.
- **Inductive step:** $(A^{k+1})_{ij} = \sum_{\ell=1}^{n} (A^k)_{i\ell} \cdot A_{\ell j}$. Each term counts walks of length $k$ from $i$ to $\ell$ followed by a single edge from $\ell$ to $j$. $\square$

### 2.2 Adjacency List

**Definition.** For each vertex $v \in V$, store a list $\text{Adj}(v)$ of its neighbors:

$$\text{Adj}(v) = \{u \in V : \{v, u\} \in E\}$$

**Properties:**
- **Space complexity:** $O(n + m)$ — much better than adjacency matrix for sparse graphs
- **Edge lookup:** $O(\deg(v))$ to check if $\{u, v\} \in E$
- **Neighbor iteration:** $O(\deg(v))$ — very efficient

**When to use which:**

| Operation | Adjacency Matrix | Adjacency List |
|-----------|-----------------|----------------|
| Check if edge exists | $O(1)$ | $O(\deg(v))$ |
| List all neighbors | $O(n)$ | $O(\deg(v))$ |
| Space | $O(n^2)$ | $O(n + m)$ |
| Add edge | $O(1)$ | $O(1)$ |
| Matrix algebra (spectral) | Natural | Requires conversion |

### 2.3 Incidence Matrix

**Definition.** The **incidence matrix** $B \in \{0, 1\}^{n \times m}$ has rows indexed by vertices and columns indexed by edges:

$$B_{ve} = \begin{cases} 1 & \text{if vertex } v \text{ is an endpoint of edge } e \\ 0 & \text{otherwise} \end{cases}$$

For a directed graph, the signed incidence matrix uses:

$$B_{ve} = \begin{cases} +1 & \text{if } v \text{ is the tail of } e \\ -1 & \text{if } v \text{ is the head of } e \\ 0 & \text{otherwise} \end{cases}$$

**Connection to the Laplacian:**

The **graph Laplacian** can be expressed as:

$$L = B B^\top = D - A$$

where $D = \text{diag}(\deg(v_1), \ldots, \deg(v_n))$ is the degree matrix.

**Result:**
$$\boxed{L = D - A = B B^\top}$$

The Laplacian is fundamental in spectral graph theory, graph signal processing, and GNNs.

---

## 3. Graph Properties

### 3.1 Degree

**Definition (Degree).** The **degree** of a vertex $v$ in an undirected graph is the number of edges incident to $v$:

$$\deg(v) = |\{e \in E : v \in e\}|$$

For directed graphs:
- **In-degree:** $\deg^{-}(v) = |\{(u, v) \in E\}|$ — number of edges pointing *into* $v$
- **Out-degree:** $\deg^{+}(v) = |\{(v, u) \in E\}|$ — number of edges pointing *out of* $v$

**Theorem (Handshaking Lemma).** For any undirected graph $G = (V, E)$:

$$\sum_{v \in V} \deg(v) = 2|E|$$

**Proof.** Each edge $\{u, v\}$ contributes exactly 1 to $\deg(u)$ and 1 to $\deg(v)$, hence contributes 2 to the total sum. $\square$

**Result:**
$$\boxed{\sum_{v \in V} \deg(v) = 2|E|}$$

**Corollary.** Every graph has an even number of vertices with odd degree.

**Proof.** Let $V_{\text{odd}} = \{v : \deg(v) \text{ is odd}\}$ and $V_{\text{even}} = \{v : \deg(v) \text{ is even}\}$. Then:

$$\sum_{v \in V_{\text{odd}}} \deg(v) = 2|E| - \sum_{v \in V_{\text{even}}} \deg(v)$$

The right side is even (difference of two even numbers), so the left side is even. Since each term on the left is odd, there must be an even number of terms. $\square$

### 3.2 Paths and Walks

**Definition (Walk).** A **walk** in $G$ is a sequence of vertices $v_0, v_1, \ldots, v_k$ such that $\{v_{i-1}, v_i\} \in E$ for all $i = 1, \ldots, k$. The **length** of the walk is $k$ (number of edges).

**Definition (Path).** A **path** is a walk with no repeated vertices.

**Definition (Cycle).** A **cycle** is a walk $v_0, v_1, \ldots, v_k$ where $v_0 = v_k$ and all other vertices are distinct, with $k \geq 3$.

**Definition (Distance).** The **distance** $d(u, v)$ between vertices $u$ and $v$ is the length of the shortest path from $u$ to $v$. If no path exists, $d(u, v) = \infty$.

**Properties of distance (metric):**
1. $d(u, v) \geq 0$ with equality iff $u = v$
2. $d(u, v) = d(v, u)$ (symmetry, for undirected graphs)
3. $d(u, w) \leq d(u, v) + d(v, w)$ (triangle inequality)

### 3.3 Connectivity

**Definition (Connected).** An undirected graph $G$ is **connected** if there exists a path between every pair of vertices.

**Definition (Connected component).** A **connected component** of $G$ is a maximal connected subgraph.

**Definition (Strongly connected).** A directed graph is **strongly connected** if there is a directed path from $u$ to $v$ *and* from $v$ to $u$ for every pair $u, v$.

**Theorem.** A graph $G$ with $n$ vertices is connected if and only if $A + A^2 + \cdots + A^{n-1}$ has no zero entries (excluding the diagonal), where $A$ is the adjacency matrix.

*Intuition:* $(A^k)_{ij} > 0$ means there is a walk of length exactly $k$ from $i$ to $j$. If some power works, there is a path (of length at most $n-1$).

### 3.4 Graph Diameter and Eccentricity

**Definition (Eccentricity).** The **eccentricity** of a vertex $v$ is:

$$\text{ecc}(v) = \max_{u \in V} d(v, u)$$

**Definition (Diameter).** The **diameter** of a connected graph $G$ is:

$$\text{diam}(G) = \max_{v \in V} \text{ecc}(v) = \max_{u, v \in V} d(u, v)$$

**Definition (Radius).** The **radius** of $G$ is:

$$\text{rad}(G) = \min_{v \in V} \text{ecc}(v)$$

---

## 4. Trees and Spanning Trees

### 4.1 Definition and Characterization

**Definition (Tree).** A **tree** is a connected graph with no cycles.

**Theorem (Equivalent characterizations).** For a graph $G$ with $n$ vertices, the following are equivalent:
1. $G$ is a tree (connected and acyclic)
2. $G$ is connected and has exactly $n - 1$ edges
3. $G$ is acyclic and has exactly $n - 1$ edges
4. There is exactly one path between every pair of vertices
5. $G$ is connected, but removing any edge disconnects it
6. $G$ is acyclic, but adding any edge creates exactly one cycle

**Result:**
$$\boxed{\text{A tree on } n \text{ vertices has exactly } n - 1 \text{ edges}}$$

**Proof (1 → has $n-1$ edges).** By induction on $n$:
- **Base case:** $n = 1$: 0 edges = $1 - 1$. ✓
- **Inductive step:** A tree $T$ with $n \geq 2$ vertices has at least one leaf $v$ (vertex of degree 1). Removing $v$ gives a tree on $n-1$ vertices with $n-2$ edges (induction hypothesis). Adding $v$ back adds one edge, giving $n-1$ edges. $\square$

### 4.2 Spanning Trees

**Definition (Spanning tree).** A **spanning tree** of a connected graph $G = (V, E)$ is a subgraph $T = (V, E_T)$ that is a tree and includes all vertices of $G$.

**Theorem (Cayley's formula).** The number of labeled spanning trees of the complete graph $K_n$ is:

$$\boxed{\tau(K_n) = n^{n-2}}$$

*Example:* $K_4$ has $4^2 = 16$ spanning trees.

**Kirchhoff's Matrix Tree Theorem.** The number of spanning trees of any graph $G$ equals any cofactor of its Laplacian matrix $L = D - A$:

$$\tau(G) = \frac{1}{n} \lambda_1 \lambda_2 \cdots \lambda_{n-1}$$

where $0 = \lambda_0 \leq \lambda_1 \leq \cdots \leq \lambda_{n-1}$ are the eigenvalues of $L$.

### 4.3 Minimum Spanning Tree (MST)

**Problem.** Given a connected, weighted graph $G = (V, E, w)$, find a spanning tree $T$ that minimizes the total weight:

$$w(T) = \sum_{e \in T} w(e)$$

**Cut Property.** For any cut $(S, V \setminus S)$ of $G$, the minimum-weight edge crossing the cut must be in every MST (assuming unique edge weights).

**Two classical algorithms:**

**Kruskal's Algorithm:**
1. Sort all edges by weight
2. Process edges in order: add edge to $T$ if it doesn't create a cycle
3. Stop when $T$ has $n - 1$ edges

Time complexity: $O(m \log m)$

**Prim's Algorithm:**
1. Start from any vertex $s$
2. Maintain a set $S$ of "reached" vertices (initially $S = \{s\}$)
3. Repeatedly add the minimum-weight edge connecting $S$ to $V \setminus S$
4. Stop when $S = V$

Time complexity: $O(m \log n)$ with a priority queue

**Result:**
$$\boxed{T^* = \arg\min_{T \text{ spanning tree}} \sum_{e \in T} w(e)}$$

---

## 5. Graph Algorithms

### 5.1 Breadth-First Search (BFS)

**Purpose:** Explore all vertices reachable from a source $s$, visiting vertices in order of increasing distance.

**Algorithm:**

```
BFS(G, s):
    for each v ∈ V: dist[v] ← ∞, parent[v] ← nil
    dist[s] ← 0
    Q ← empty queue
    Q.enqueue(s)
    while Q is not empty:
        u ← Q.dequeue()
        for each v ∈ Adj(u):
            if dist[v] = ∞:
                dist[v] ← dist[u] + 1
                parent[v] ← u
                Q.enqueue(v)
```

**Properties:**
- Time complexity: $O(n + m)$
- BFS produces a **shortest-path tree** from $s$ (for unweighted graphs)
- `dist[v]` = exact shortest distance from $s$ to $v$ in unweighted graphs
- Visits vertices layer by layer (distance 0, then 1, then 2, ...)

**Result:**
$$\boxed{d_{\text{BFS}}(s, v) = d(s, v) \text{ for unweighted graphs}}$$

### 5.2 Depth-First Search (DFS)

**Purpose:** Explore as far as possible along each branch before backtracking.

**Algorithm:**

```
DFS(G):
    for each v ∈ V: color[v] ← WHITE, parent[v] ← nil
    time ← 0
    for each v ∈ V:
        if color[v] = WHITE:
            DFS-Visit(v)

DFS-Visit(u):
    time ← time + 1
    discover[u] ← time
    color[u] ← GRAY
    for each v ∈ Adj(u):
        if color[v] = WHITE:
            parent[v] ← u
            DFS-Visit(v)
    color[u] ← BLACK
    time ← time + 1
    finish[u] ← time
```

**Properties:**
- Time complexity: $O(n + m)$
- Produces a **DFS forest** with timestamps
- **Edge classification:** tree edges, back edges, forward edges, cross edges
- A directed graph has a cycle if and only if DFS finds a **back edge**

**Applications:**
- Topological sorting (DAGs)
- Finding connected components
- Finding strongly connected components (Tarjan's algorithm)
- Cycle detection

### 5.3 Dijkstra's Shortest Path Algorithm

**Purpose:** Find shortest paths from source $s$ to all other vertices in a weighted graph with **non-negative** edge weights.

**Assumption:** $w(e) \geq 0$ for all $e \in E$.

**Algorithm:**

```
Dijkstra(G, w, s):
    for each v ∈ V: dist[v] ← ∞, parent[v] ← nil
    dist[s] ← 0
    Q ← priority queue of all vertices, keyed by dist
    while Q is not empty:
        u ← Q.extract_min()
        for each v ∈ Adj(u):
            if dist[u] + w(u,v) < dist[v]:
                dist[v] ← dist[u] + w(u,v)
                parent[v] ← u
                Q.decrease_key(v, dist[v])
```

**Correctness intuition:** At each step, the vertex $u$ with minimum tentative distance is finalized — no other path to $u$ can be shorter because all remaining edges are non-negative.

**Time complexity:**
- With binary heap: $O((n + m) \log n)$
- With Fibonacci heap: $O(m + n \log n)$

**Result:** For a weighted graph with non-negative weights,
$$\boxed{d_{\text{Dijkstra}}(s, v) = \min_{\text{paths } P: s \to v} \sum_{e \in P} w(e)}$$

### 5.4 Algorithm Comparison

| Algorithm | Graph Type | Edge Weights | Finds | Time |
|-----------|-----------|-------------|-------|------|
| BFS | Any | Unweighted | Shortest paths from $s$ | $O(n+m)$ |
| DFS | Any | Unweighted | Reachability, components, cycles | $O(n+m)$ |
| Dijkstra | Any | Non-negative | Shortest paths from $s$ | $O((n+m)\log n)$ |
| Bellman-Ford | Directed | Any | Shortest paths, negative cycles | $O(nm)$ |

---

## 6. Special Graphs

### 6.1 Complete Graph $K_n$

**Definition.** The **complete graph** $K_n$ has $n$ vertices and every possible edge:

$$|E(K_n)| = \binom{n}{2} = \frac{n(n-1)}{2}$$

Every vertex has degree $n - 1$.

### 6.2 Bipartite Graphs

**Definition.** A graph $G = (V, E)$ is **bipartite** if $V$ can be partitioned into two disjoint sets $V_1, V_2$ such that every edge connects a vertex in $V_1$ to a vertex in $V_2$.

**Theorem.** A graph is bipartite if and only if it contains no odd-length cycle.

**Complete bipartite graph** $K_{p,q}$: every vertex in $V_1$ (size $p$) is connected to every vertex in $V_2$ (size $q$). It has $pq$ edges.

**Applications:** Matching problems, recommendation systems, two-mode networks.

### 6.3 Planar Graphs

**Definition.** A graph is **planar** if it can be drawn in the plane with no edge crossings.

**Euler's Formula.** For a connected planar graph with $n$ vertices, $m$ edges, and $f$ faces:

$$\boxed{n - m + f = 2}$$

**Corollary.** For a simple planar graph with $n \geq 3$:

$$m \leq 3n - 6$$

This immediately shows $K_5$ is not planar: $\binom{5}{2} = 10 > 3(5) - 6 = 9$.

**Kuratowski's Theorem.** A graph is planar if and only if it does not contain a subdivision of $K_5$ or $K_{3,3}$.

### 6.4 Eulerian Graphs

**Definition.** An **Eulerian circuit** is a closed walk that visits every edge exactly once.

**Theorem (Euler, 1736).** A connected graph has an Eulerian circuit if and only if every vertex has even degree.

This is historically the first theorem of graph theory, arising from the **Königsberg bridge problem**.

### 6.5 Hamiltonian Graphs

**Definition.** A **Hamiltonian cycle** is a cycle that visits every vertex exactly once.

**Key difference from Eulerian:** Determining whether a graph is Hamiltonian is NP-complete — no efficient necessary-and-sufficient condition is known.

**Dirac's Theorem (sufficient condition).** If $G$ has $n \geq 3$ vertices and every vertex satisfies $\deg(v) \geq n/2$, then $G$ has a Hamiltonian cycle.

### 6.6 Summary of Special Graphs

| Graph Class | Key Property | Key Result |
|------------|-------------|------------|
| $K_n$ | All pairs connected | $\binom{n}{2}$ edges, $n^{n-2}$ spanning trees |
| Bipartite | Two-part structure | No odd cycles |
| Planar | No crossings | $n - m + f = 2$ |
| Eulerian | Traverse all edges | All degrees even |
| Hamiltonian | Visit all vertices | NP-complete to decide |

---

## 7. Connection to Modeling

### 7.1 Network Flow Models

Many optimization problems have graph structure:
- **Max-flow / min-cut:** Find maximum flow through a capacitated network (Ford-Fulkerson algorithm)
- **Shortest path:** Route planning (Dijkstra, Bellman-Ford, A*)
- **Minimum cost flow:** Transportation and assignment problems

The governing principle is **conservation of flow** at each node:

$$\sum_{\text{in-flow}} f_{in} = \sum_{\text{out-flow}} f_{out} \quad \text{(Kirchhoff's current law)}$$

### 7.2 Social Networks

Graphs model social relationships with vertices as people and edges as connections:
- **Degree centrality:** How many connections does a person have?
- **Betweenness centrality:** How often does a person lie on shortest paths between others?
- **Clustering coefficient:** How many of a person's friends are also friends with each other?
- **Community detection:** Are there densely connected subgroups?

### 7.3 Transportation Networks

Road networks, airline routes, and logistics networks are naturally modeled as weighted graphs:
- Vertices = locations
- Edges = routes
- Weights = distance, time, or cost
- Optimization = shortest path, minimum spanning tree, network design

### 7.4 Biological Networks

- **Protein interaction networks:** Vertices = proteins, edges = interactions
- **Metabolic networks:** Vertices = metabolites, edges = reactions
- **Neural networks (biological):** Vertices = neurons, edges = synapses
- **Phylogenetic trees:** Tree structure representing evolutionary relationships

### 7.5 Graph Neural Networks (GNNs)

The mathematical connection from graph theory to deep learning:

**Message passing** on a graph implements the update rule:

$$h_v^{(k+1)} = \phi\left(h_v^{(k)}, \bigoplus_{u \in \mathcal{N}(v)} \psi(h_v^{(k)}, h_u^{(k)}, e_{uv})\right)$$

where:
- $h_v^{(k)}$ is the feature vector of node $v$ at layer $k$
- $\mathcal{N}(v) = \text{Adj}(v)$ is the neighborhood from graph theory
- $\bigoplus$ is a permutation-invariant aggregation (sum, mean, max)
- $\phi, \psi$ are learned functions

The simplest form (GCN) uses the adjacency and degree matrices directly:

$$H^{(k+1)} = \sigma\left(\tilde{D}^{-1/2} \tilde{A} \tilde{D}^{-1/2} H^{(k)} W^{(k)}\right)$$

where $\tilde{A} = A + I$ (self-loops added), $\tilde{D}$ is the corresponding degree matrix, and $W^{(k)}$ is a learnable weight matrix.

This directly builds on:
- **Adjacency matrix** $A$ (Section 2.1)
- **Degree matrix** $D$ (Section 3.1)
- **Laplacian** $L = D - A$ (Section 2.3)
- **Neighborhood** $\mathcal{N}(v)$ (Section 2.2)

---

## Summary of Key Results

| Result | Formula |
|--------|---------|
| Handshaking Lemma | $\sum_{v} \deg(v) = 2|E|$ |
| Walks via adjacency matrix | $(A^k)_{ij}$ = number of walks of length $k$ |
| Graph Laplacian | $L = D - A = BB^\top$ |
| Tree edge count | $n$ vertices $\implies$ $n-1$ edges |
| Cayley's formula | $\tau(K_n) = n^{n-2}$ |
| Euler's formula (planar) | $n - m + f = 2$ |
| Planar edge bound | $m \leq 3n - 6$ |
| Eulerian circuit condition | All vertices have even degree |
| BFS correctness | $d_{\text{BFS}}(s,v) = d(s,v)$ for unweighted |
| Dijkstra correctness | Finds shortest paths with $w \geq 0$ |
