# Answers for Units 1, 2, and 3 (Linear Data Structures)

## Q.1 a) Differentiate between Primitive and Non-Primitive data structures. Explain the concept of Time Complexity using the step-counting method for Linear Search. (7 Marks)

**Answer:**

**1. Difference between Primitive and Non-Primitive Data Structures:**

| Aspect | Primitive Data Structure | Non-Primitive Data Structure |
| :--- | :--- | :--- |
| **Definition** | Basic, built-in types that hold a single value. Directly operated upon by machine instructions. | User-defined structures that can hold multiple values, derived from primitive types. |
| **Examples** | `int`, `char`, `float`, `boolean` | Arrays, Linked Lists, Stacks, Trees, Graphs |
| **Operations** | Supports basic arithmetic and logical operations (+, -, ==). | Supports higher-level operations like insertion, deletion, sorting, traversal. |
| **Memory** | Single contiguous memory block for a specific value. | Contiguous or scattered memory blocks to store collections of values. |
| **Complexity** | Simple and direct. | More complex implementation and usage. |

**2. Time Complexity using Step-Counting for Linear Search:**
Time complexity describes how the number of operations in an algorithm grows as the input size (N) increases.

*Linear Search Algorithm:*
```cpp
int linearSearch(int arr[], int N, int target) {
    for (int i = 0; i < N; i++) {       // Step 1: Loop N times
        if (arr[i] == target)           // Step 2: Comparison inside loop
            return i;                   // Step 3: Return if found
    }
    return -1;                          // Step 4: Return if not found
}
```

*Step-Counting Method Analysis (Average Case):*
*   **Initialization:** `int i = 0` (1 step)
*   **Condition Check:** `i < N` runs (N+1) times. (N+1 steps)
*   **Increment:** `i++` runs N times. (N steps)
*   **Comparison:** `arr[i] == target` runs N times in the worst case. (N steps)
*   On average, the target is found at the middle of the array (`N/2` comparisons).
*   Total average steps ≈ `1 + (N/2 + 1) + (N/2) + (N/2)` ≈ `1.5 * N + 2`.
*   Dropping constants and lower-order terms, the dominant term is `N`.
*   **Average Time Complexity = O(N)**

---

## Q.2 a) Write an algorithm for Polynomial Addition using Arrays. (7 Marks)

**Answer:**

**Algorithm for Polynomial Addition (using Arrays):**
*Assumption:* Polynomials are represented using two arrays where the index represents the exponent and the value at that index represents the coefficient. For example, `3x^2 + 5` is `arr[2]=3, arr[0]=5`.

```text
Algorithm: AddPolynomials(A, B, result, maxDegree)
Input: 
  A: Array representing the first polynomial
  B: Array representing the second polynomial
  maxDegree: The highest exponent degree in both polynomials
Output:
  result: Array containing the sum of A and B

Steps:
1. Initialize a loop counter 'i' from 0 to maxDegree.
2. For i = 0 to maxDegree DO:
3.     // Add the coefficients of the same degree
       result[i] = A[i] + B[i]
4. End For
5. Print "Polynomial Addition Complete."
6. Return result array.
```
*(Note: If polynomials are stored as arrays of structures `[Coefficient, Exponent]`, a two-pointer merge approach similar to merge sort is used, comparing exponents and adding coefficients if exponents match).*

---

## Q.1 b) Write pseudocode for Push and Pop operations in a Stack. Evaluate an infix expression to a postfix expression (provide your own example). (7 Marks)

**Answer:**

**1. Pseudocode for Stack Operations (Array Implementation):**
```cpp
Initialize: top = -1, max_size = N, stack[N]

Procedure Push(x):
    If top == max_size - 1 Then
        Print "Stack Overflow"
        Return
    top = top + 1
    stack[top] = x
    Return

Function Pop():
    If top == -1 Then
        Print "Stack Underflow"
        Return NULL
    element = stack[top]
    top = top - 1
    Return element
```

**2. Infix to Postfix Evaluation:**
*Example Infix Expression:* `A * (B + C) - D`

| Step | Symbol Scanned | Stack | Postfix Expression (Result) | Action |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `A` | Empty | `A` | Operand goes to output |
| 2 | `*` | `*` | `A` | Push operator |
| 3 | `(` | `* (` | `A` | Push `(` |
| 4 | `B` | `* (` | `A B` | Operand goes to output |
| 5 | `+` | `* ( +` | `A B` | Push operator |
| 6 | `C` | `* ( +` | `A B C` | Operand goes to output |
| 7 | `)` | `*` | `A B C +` | Pop until `(`. Append `+` to output |
| 8 | `-` | `-` | `A B C + *` | `-` has lower precedence than `*`, so pop `*` and push `-` |
| 9 | `D` | `-` | `A B C + * D` | Operand goes to output |
| 10 | End | Empty | `A B C + * D -` | Pop remaining operators |

**Final Postfix:** `A B C + * D -`

---

## Q.2 b) Perform Enqueue and Dequeue operations on a Circular Queue for the sequence: 10, 20, 30, 40. Show the intermediate queue states and Front/Rear pointers. (7 Marks)

**Answer:**

*Assumptions:* Queue size `N = 4`. Initial state: `Front = -1, Rear = -1`.
Formula for Circular Queue: `Rear = (Rear + 1) % N`, `Front = (Front + 1) % N`.

**1. Enqueue 10:**
*   Queue is empty (`Front == -1`).
*   `Front = 0, Rear = 0`
*   Queue State: `[10, -, -, -]`

**2. Enqueue 20:**
*   `Rear = (0 + 1) % 4 = 1`
*   Queue State: `[10, 20, -, -]`
*   Pointers: `Front = 0, Rear = 1`

**3. Enqueue 30:**
*   `Rear = (1 + 1) % 4 = 2`
*   Queue State: `[10, 20, 30, -]`
*   Pointers: `Front = 0, Rear = 2`

**4. Enqueue 40:**
*   `Rear = (2 + 1) % 4 = 3`
*   Queue State: `[10, 20, 30, 40]`
*   Pointers: `Front = 0, Rear = 3` (Queue is Full)

**5. Dequeue:**
*   Remove element at `Front` (10).
*   `Front = (0 + 1) % 4 = 1`
*   Queue State: `[-, 20, 30, 40]`
*   Pointers: `Front = 1, Rear = 3`

**6. Dequeue:**
*   Remove element at `Front` (20).
*   `Front = (1 + 1) % 4 = 2`
*   Queue State: `[-, -, 30, 40]`
*   Pointers: `Front = 2, Rear = 3`

---

## Q.1 c) Write an algorithm to insert and delete a node at the beginning of a Doubly Linked List (DLL). (6 Marks)

**Answer:**

**Node Structure:** `[prev | data | next]`

**1. Algorithm: Insert at Beginning**
```text
Algorithm InsertFront(head, newValue)
1. Allocate memory for newNode.
2. newNode->data = newValue.
3. newNode->prev = NULL.
4. If head == NULL Then (List is empty)
5.     newNode->next = NULL
6.     head = newNode
7. Else (List is not empty)
8.     newNode->next = head
9.     head->prev = newNode
10.    head = newNode
11. End If
```

**2. Algorithm: Delete from Beginning**
```text
Algorithm DeleteFront(head)
1. If head == NULL Then
2.     Print "List is empty, cannot delete."
3.     Return NULL
4. End If
5. temp = head
6. If head->next == NULL Then (Only one node in list)
7.     head = NULL
8. Else (Multiple nodes)
9.     head = head->next
10.    head->prev = NULL
11. End If
12. Free memory allocated to temp.
```

---

## Q.2 c) Explain Generalized Linked List (GLL) and demonstrate how it can be used to represent a polynomial. (6 Marks)

**Answer:**

**Generalized Linked List (GLL):**
A Generalized Linked List (GLL) is a linked list wherein the data part of a node can either contain an atomic value (like a standard integer or character) OR it can hold a pointer to another Generalized Linked List (a sublist). 
This allows GLLs to represent complex, non-linear, hierarchical structures like trees or multi-variable polynomials easily.

Node Structure of GLL:
`[Flag | Data/DownPointer | NextPointer]`
*   **Flag:** 0 if the node contains an atomic value, 1 if it contains a pointer to a sublist.

**Representing a Polynomial using GLL:**
GLLs are incredibly useful for representing multi-variable polynomials. 
Consider the polynomial: `P(x, y, z) = 3x^2y + 5xyz^3`

Since there are multiple variables, a standard linked list struggles. In a GLL, we can group sub-expressions by their variables.
We can factor it out: `x(3xy + 5yz^3)`.
*   The main list represents the variable `x`.
*   The nodes in the main list point down to sublists that represent the expressions in terms of `y`.
*   Those sublists might point down to sublists representing `z`.

*Node layout for Polynomial GLL:*
`[Flag | Coefficient | Exponent | DownPointer/Variable | NextPointer]`

By recursively following the down-pointers, the algorithm can easily evaluate or add complex polynomials with multiple variables without needing a rigid multi-dimensional array structure.
