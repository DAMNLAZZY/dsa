# Predicted Answers for Paper 4 (Part 3)

## Q.5 b) Write a short note on Splay Trees. Explain Zig, Zig-Zig, and Zig-Zag operations. State advantages and applications. (6 Marks)

**Answer:**

**Splay Tree:**
A splay tree is a self-adjusting binary search tree with the additional property that recently accessed elements are quick to access again. It performs basic operations such as insertion, look-up, and removal in O(log n) amortized time. After every operation (search, insert, delete), a special operation called **Splaying** is performed to move the accessed node to the root of the tree.

**Splaying Operations (Rotations):**
When a node `x` is accessed, it is splayed to the root. Let `p` be the parent of `x` and `g` be the grandparent of `x`.

1.  **Zig Step (Single Rotation):**
    *   *Condition:* `p` is the root (no grandparent `g`).
    *   *Action:* If `x` is a left child, perform a right rotation. If `x` is a right child, perform a left rotation. This is identical to a standard AVL single rotation.

2.  **Zig-Zig Step (Double Rotation - Same Direction):**
    *   *Condition:* `p` is NOT the root, and both `x` and `p` are either left children or both are right children.
    *   *Action:* First rotate `p` over `g`, then rotate `x` over `p`.

3.  **Zig-Zag Step (Double Rotation - Opposite Directions):**
    *   *Condition:* `p` is NOT the root, and one is a left child while the other is a right child (e.g., `x` is a right child and `p` is a left child).
    *   *Action:* First rotate `x` over `p`, then rotate `x` (which is now the parent of `p`) over `g`.

**Advantages:**
*   Simpler to implement than AVL or Red-Black trees since no balance factors/colors need to be stored in the nodes.
*   Excellent performance when a small subset of elements is accessed frequently (locality of reference).

**Applications:**
*   Implementing caches (since most recently accessed items move to the top).
*   Garbage collection algorithms.
*   Data compression algorithms (like dynamic Huffman coding).

---

## Q.6 a) Construct OBST for keys (10, 20, 30) with probabilities P = (0.3, 0.5, 0.2). Calculate expected access time for all possible trees. Determine OBST using cost table. (7 Marks)

**Answer:**

Keys: K1=10, K2=20, K3=30
Probabilities: P1=0.3, P2=0.5, P3=0.2

**Method 1: Evaluating all possible trees (Brute Force)**
Since n=3, there are 5 possible binary search trees.
Expected Cost = Σ (Level(Ki) * P(Ki))  *(Assuming root is at level 1)*

*   **Tree 1:** Root=10. Right child=20. Right child of 20=30.
    *   Cost = (1 * 0.3) + (2 * 0.5) + (3 * 0.2) = 0.3 + 1.0 + 0.6 = **1.9**
*   **Tree 2:** Root=10. Right child=30. Left child of 30=20.
    *   Cost = (1 * 0.3) + (2 * 0.2) + (3 * 0.5) = 0.3 + 0.4 + 1.5 = **2.2**
*   **Tree 3:** Root=20. Left child=10. Right child=30.
    *   Cost = (1 * 0.5) + (2 * 0.3) + (2 * 0.2) = 0.5 + 0.6 + 0.4 = **1.5**
*   **Tree 4:** Root=30. Left child=20. Left child of 20=10.
    *   Cost = (1 * 0.2) + (2 * 0.5) + (3 * 0.3) = 0.2 + 1.0 + 0.9 = **2.1**
*   **Tree 5:** Root=30. Left child=10. Right child of 10=20.
    *   Cost = (1 * 0.2) + (2 * 0.3) + (3 * 0.5) = 0.2 + 0.6 + 1.5 = **2.3**

**Minimum Cost is 1.5 (Tree 3).**

**Method 2: Cost Table (Dynamic Programming approach)**
Formula: `C(i, j) = min i<=k<=j { C(i, k-1) + C(k+1, j) } + W(i, j)`
Where `W(i, j) = sum(Pm)` from `m=i` to `j`.

*   **Size 1 (1 node trees):**
    *   C(1,1) = P1 = 0.3 (Root: 10)
    *   C(2,2) = P2 = 0.5 (Root: 20)
    *   C(3,3) = P3 = 0.2 (Root: 30)
*   **Size 2 (2 node trees):**
    *   W(1,2) = 0.3 + 0.5 = 0.8
        *   C(1,2) = min { C(1,0)+C(2,2) , C(1,1)+C(3,2) } + 0.8 = min {0+0.5, 0.3+0} + 0.8 = 0.3 + 0.8 = 1.1 (Root: 20)
    *   W(2,3) = 0.5 + 0.2 = 0.7
        *   C(2,3) = min { C(2,1)+C(3,3) , C(2,2)+C(4,3) } + 0.7 = min {0+0.2, 0.5+0} + 0.7 = 0.2 + 0.7 = 0.9 (Root: 20)
*   **Size 3 (3 node trees):**
    *   W(1,3) = 0.3 + 0.5 + 0.2 = 1.0
    *   C(1,3) = min:
        *   k=1 (root 10): C(1,0) + C(2,3) + 1.0 = 0 + 0.9 + 1.0 = 1.9
        *   k=2 (root 20): C(1,1) + C(3,3) + 1.0 = 0.3 + 0.2 + 1.0 = 1.5  <-- Minimum!
        *   k=3 (root 30): C(1,2) + C(4,3) + 1.0 = 1.1 + 0 + 1.0 = 2.1
    *   **Cost = 1.5, Root is K2 (20).**

**Final OBST Structure:**
```text
      20
     /  \
   10    30
```

---

## Q.8 a) Find Minimum Spanning Tree using Prim's and Kruskal's. (7 Marks)
*Graph Edges: A-B:4, A-C:8, B-C:2, B-D:5, C-D:6, C-E:3, D-E:7, D-F:9, E-F:1*

**Answer:**

**1. Kruskal's Algorithm:**
*   Sort edges by weight: E-F(1), B-C(2), C-E(3), A-B(4), B-D(5), C-D(6), D-E(7), A-C(8), D-F(9)
*   Add edges avoiding cycles:
    1.  Add E-F (1)
    2.  Add B-C (2)
    3.  Add C-E (3)
    4.  Add A-B (4)
    5.  Add B-D (5)
    6.  Edge C-D (6) creates cycle B-C-D. Reject.
    7.  Edge D-E (7) creates cycle B-C-E-D. Reject.
    8.  Edge A-C (8) creates cycle A-B-C. Reject.
    9.  Edge D-F (9) creates cycle D-B-C-E-F. Reject.
*   **Total Weight = 1 + 2 + 3 + 4 + 5 = 15**

**2. Prim's Algorithm:**
*   Start at vertex A. Visited = {A}. Unvisited = {B,C,D,E,F}.
*   Edges from Visited to Unvisited: A-B(4), A-C(8). Pick min: **A-B (4)**. Visited = {A,B}.
*   Edges from {A,B}: A-C(8), B-C(2), B-D(5). Pick min: **B-C (2)**. Visited = {A,B,C}.
*   Edges from {A,B,C}: A-C(8), B-D(5), C-D(6), C-E(3). Pick min: **C-E (3)**. Visited = {A,B,C,E}.
*   Edges from {A,B,C,E}: A-C(8), B-D(5), C-D(6), D-E(7), E-F(1). Pick min: **E-F (1)**. Visited = {A,B,C,E,F}.
*   Edges from {A,B,C,E,F}: A-C(8), B-D(5), C-D(6), D-E(7), D-F(9). Pick min: **B-D (5)**. Visited = {A,B,C,D,E,F}. All visited.
*   **Total Weight = 4 + 2 + 3 + 1 + 5 = 15**

**Comparison:** Both algorithms produce the same MST edges (A-B, B-C, C-E, E-F, B-D) and the same total minimum weight of 15.

---

## Q.8 b) Apply Dijkstra's algorithm to find the shortest path from vertex S. Show execution. (6 Marks)
*Graph: S-A(3), S-B(5), A-B(2), A-C(7), B-C(1), B-D(6), C-D(2), C-E(4), D-E(3)*

**Answer:**

**Initialization:**
Distances: D(S)=0, D(A)=∞, D(B)=∞, D(C)=∞, D(D)=∞, D(E)=∞
Visited set: {}

**Iteration 1:**
*   Current Vertex: **S** (min distance = 0)
*   Update neighbors:
    *   D(A) = min(∞, 0+3) = **3** (Path: S-A)
    *   D(B) = min(∞, 0+5) = **5** (Path: S-B)
*   Visited = {S}

**Iteration 2:**
*   Min unvisited distance is D(A)=3. Current Vertex: **A**
*   Update neighbors:
    *   D(B) = min(5, 3+2) = **5** (Path: S-B or S-A-B, keep existing)
    *   D(C) = min(∞, 3+7) = **10** (Path: S-A-C)
*   Visited = {S, A}

**Iteration 3:**
*   Min unvisited distance is D(B)=5. Current Vertex: **B**
*   Update neighbors:
    *   D(C) = min(10, 5+1) = **6** (Path: S-B-C)
    *   D(D) = min(∞, 5+6) = **11** (Path: S-B-D)
*   Visited = {S, A, B}

**Iteration 4:**
*   Min unvisited distance is D(C)=6. Current Vertex: **C**
*   Update neighbors:
    *   D(D) = min(11, 6+2) = **8** (Path: S-B-C-D)
    *   D(E) = min(∞, 6+4) = **10** (Path: S-B-C-E)
*   Visited = {S, A, B, C}

**Iteration 5:**
*   Min unvisited distance is D(D)=8. Current Vertex: **D**
*   Update neighbors:
    *   D(E) = min(10, 8+3) = **10** (existing path is 10, no change)
*   Visited = {S, A, B, C, D}

**Iteration 6:**
*   Min unvisited distance is D(E)=10. Current Vertex: **E**
*   No unvisited neighbors.
*   Visited = {S, A, B, C, D, E}

**Final Shortest Paths from S:**
*   **S to A:** Distance 3 (Path: S-A)
*   **S to B:** Distance 5 (Path: S-B)
*   **S to C:** Distance 6 (Path: S-B-C)
*   **S to D:** Distance 8 (Path: S-B-C-D)
*   **S to E:** Distance 10 (Path: S-B-C-E)
