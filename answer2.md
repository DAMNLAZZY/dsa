# Predicted Answers for Paper 4 (Continued)

## Q.3 a) Perform a dry run of the Merge Sort algorithm on the array: [35, 18, 42, 7, 29, 63, 14, 51]. Show the step-by-step process of dividing the array and then merging the sub-arrays in sorted order. (7 Marks)

**Answer:**

**Initial Array:** `[35, 18, 42, 7, 29, 63, 14, 51]`

**Phase 1: Divide (Splitting into halves until single elements)**
*   **Step 1:** Split into two halves
    *   Left: `[35, 18, 42, 7]`
    *   Right: `[29, 63, 14, 51]`
*   **Step 2:** Split left and right halves again
    *   LL: `[35, 18]`, LR: `[42, 7]`
    *   RL: `[29, 63]`, RR: `[14, 51]`
*   **Step 3:** Split into single elements
    *   `[35]`, `[18]`, `[42]`, `[7]`, `[29]`, `[63]`, `[14]`, `[51]`

**Phase 2: Conquer (Merging sorted sub-arrays)**
*   **Merge Step 1 (pairs):**
    *   Merge `[35]` and `[18]` -> `[18, 35]`
    *   Merge `[42]` and `[7]` -> `[7, 42]`
    *   Merge `[29]` and `[63]` -> `[29, 63]`
    *   Merge `[14]` and `[51]` -> `[14, 51]`
*   **Merge Step 2 (fours):**
    *   Merge `[18, 35]` and `[7, 42]` -> `[7, 18, 35, 42]`
    *   Merge `[29, 63]` and `[14, 51]` -> `[14, 29, 51, 63]`
*   **Merge Step 3 (final array):**
    *   Merge `[7, 18, 35, 42]` and `[14, 29, 51, 63]` -> `[7, 14, 18, 29, 35, 42, 51, 63]`

**Final Sorted Array:** `[7, 14, 18, 29, 35, 42, 51, 63]`

---

## Q.5 a) Construct an AVL Tree by inserting the following elements in the given order: 50, 25, 75, 10, 30, 60, 80, 5, 35, 55. Show the balance factor of each node after every insertion. Clearly name the type of rotation used. (7 Marks)

**Answer:**
*(Note: Balance Factor = Height of Left Subtree - Height of Right Subtree. Valid BFs are -1, 0, 1)*

1.  **Insert 50:**
    ```text
    50(0)
    ```

2.  **Insert 25:**
    ```text
        50(1)
       /
    25(0)
    ```

3.  **Insert 75:**
    ```text
        50(0)
       /    \
    25(0)  75(0)
    ```

4.  **Insert 10:**
    ```text
           50(1)
          /    \
       25(1)  75(0)
      /
    10(0)
    ```

5.  **Insert 30:**
    ```text
           50(1)
          /    \
       25(0)  75(0)
      /    \
    10(0)  30(0)
    ```

6.  **Insert 60:**
    ```text
           50(1)
          /    \
       25(0)  75(1)
      /    \  /
    10    30 60(0)
    ```

7.  **Insert 80:**
    ```text
           50(0)
          /    \
       25(0)  75(0)
      /   \   /   \
    10   30  60   80(0)
    ```

8.  **Insert 5:**
    ```text
           50(1)
          /    \
       25(1)  75(0)
      /   \   /   \
    10(1) 30 60   80
    /
   5(0)
    ```

9.  **Insert 35:**
    ```text
           50(1)
          /    \
       25(1)  75(0)
      /   \   /   \
    10(1) 30(-1) 60 80
    /       \
   5(0)     35(0)
    ```

10. **Insert 55:**
    ```text
           50(1)
          /    \
       25(1)  75(2)  <-- Unbalanced at 75! Left-Left heavy (LL case)
      /   \   /   \
    10   30  60(1) 80
    /     \  /
   5      35 55(0)
    ```
    **Rebalancing:** We inserted 55 into the left subtree of the left child of 75. This is an **LL Rotation** around 75.
    *   60 moves up to replace 75.
    *   75 becomes the right child of 60.
    *   The right child of 60 (if any) becomes the left child of 75.

    **Final AVL Tree (After LL Rotation):**
    ```text
           50(0)
          /    \
       25(1)  60(0)
      /   \   /   \
    10(1) 30 55(0) 75(0)
    /     \         \
   5(0)   35(0)     80(0)
    ```

---

## Q.7 b) Apply the Floyd-Warshall algorithm to find the transitive closure of the following directed graph. Show the intermediate matrices after each iteration (k=1,2,3,4). (6 Marks)
*Vertices: 1, 2, 3, 4 | Edges: 1->2, 2->3, 3->4, 4->1, 2->4*

**Answer:**

**Initial Matrix (Direct Edges), T(0):**
```
   1  2  3  4
1 [0  1  0  0]
2 [0  0  1  1]
3 [0  0  0  1]
4 [1  0  0  0]
```

**Iteration 1 (k=1): Paths via vertex 1**
`T[4][1]=1` and `T[1][2]=1` => new path `T[4][2] = 1`.
```
   1  2  3  4
1 [0  1  0  0]
2 [0  0  1  1]
3 [0  0  0  1]
4 [1  1  0  0]  <-- T[4][2] updated
```

**Iteration 2 (k=2): Paths via vertex 2**
`T[1][2]=1` and `T[2][3]=1` => `T[1][3] = 1`
`T[1][2]=1` and `T[2][4]=1` => `T[1][4] = 1`
`T[4][2]=1` and `T[2][3]=1` => `T[4][3] = 1`
`T[4][2]=1` and `T[2][4]=1` => `T[4][4] = 1`
```
   1  2  3  4
1 [0  1  1  1]  <-- T[1][3], T[1][4] updated
2 [0  0  1  1]
3 [0  0  0  1]
4 [1  1  1  1]  <-- T[4][3], T[4][4] updated
```

**Iteration 3 (k=3): Paths via vertex 3**
No new paths discovered.
```
   1  2  3  4
1 [0  1  1  1]
2 [0  0  1  1]
3 [0  0  0  1]
4 [1  1  1  1]
```

**Iteration 4 (k=4): Paths via vertex 4**
This completes the cycle, making every vertex reachable. All 0s become 1s.
```
   1  2  3  4
1 [1  1  1  1]
2 [1  1  1  1]
3 [1  1  1  1]
4 [1  1  1  1]
```
**Final Transitive Closure Matrix:** All elements are 1, meaning it's a Strongly Connected Graph.
