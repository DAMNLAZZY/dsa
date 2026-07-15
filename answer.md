# Predicted Answers for Paper 4

## Q.1 a) What is a Hash Function? Explain different collision resolution techniques: Separate Chaining, Linear Probing, Quadratic Probing, and Double Hashing with examples. (6 Marks)

**Answer:**

**Hash Function:**
A hash function is a mathematical algorithm that maps a given key (which can be of any size) to a fixed-size value, usually an index in a hash table. The goal is to distribute the keys evenly across the hash table to minimize collisions.
*Formula:* `Index = HashFunction(Key)`
*Example:* `h(k) = k mod M` (where M is table size)

**Collision:** Occurs when a hash function maps two different keys to the same index.

**Collision Resolution Techniques:**

1.  **Separate Chaining (Open Hashing):**
    *   **Concept:** Each slot of the hash table contains a linked list (chain). When a collision occurs, the new element is simply appended to the linked list at that index.
    *   **Example:** Insert 12, 22 into table size 10 using `k mod 10`.
        *   `12 mod 10 = 2`
        *   `22 mod 10 = 2` (Collision!)
        *   Index 2 will point to a linked list: `12 -> 22 -> NULL`.

2.  **Linear Probing (Closed Hashing / Open Addressing):**
    *   **Concept:** When a collision occurs, search sequentially for the next available slot in the table.
    *   **Formula:** `h'(k, i) = (h(k) + i) mod M` (where i = 0, 1, 2,...)
    *   **Example:** Insert 12, 22 into table size 10 using `k mod 10`.
        *   `12 mod 10 = 2` (Placed at index 2)
        *   `22 mod 10 = 2` (Collision)
        *   Probe next: `(2+1)%10 = 3` (Placed at index 3).

3.  **Quadratic Probing (Closed Hashing):**
    *   **Concept:** To avoid primary clustering seen in linear probing, search using a quadratic function.
    *   **Formula:** `h'(k, i) = (h(k) + i^2) mod M` (where i = 0, 1, 2,...)
    *   **Example:** If collision at index 2:
        *   Probe 1: `(2 + 1^2) % 10 = 3`
        *   Probe 2: `(2 + 2^2) % 10 = 6`
        *   Probe 3: `(2 + 3^2) % 10 = 1`

4.  **Double Hashing (Closed Hashing):**
    *   **Concept:** Uses a second hash function `h2(k)` to determine the probe step size when a collision occurs.
    *   **Formula:** `h'(k, i) = (h1(k) + i * h2(k)) mod M`
    *   **Example:** `h1(k) = k mod 10`, `h2(k) = 7 - (k mod 7)`. If collision, step by `h2(k)`.

---

## Q.1 b) Given the following traversals, build a binary tree from them: In-order: D, B, H, E, I, A, F, C, G / Pre-order: A, B, D, E, H, I, C, F, G. Also write the Post-order traversal. (7 Marks)

**Answer:**

**Step-by-step Construction:**
1.  **Root:** The first element in Pre-order is always the root.
    *   Root = **A**
2.  **Split In-order:** Find 'A' in the In-order traversal. Elements to the left form the Left Subtree (LST), elements to the right form the Right Subtree (RST).
    *   LST nodes: `D, B, H, E, I`
    *   RST nodes: `F, C, G`
3.  **Process LST (Pre-order: B, D, E, H, I | In-order: D, B, H, E, I):**
    *   Root of LST is **B** (next in pre-order).
    *   In-order split by B: Left = `D`, Right = `H, E, I`.
    *   Left child of B is **D**.
    *   Process right of B (Pre-order: E, H, I | In-order: H, E, I):
        *   Root is **E**.
        *   In-order split by E: Left = `H`, Right = `I`.
        *   Left child of E is **H**, right child is **I**.
4.  **Process RST (Pre-order: C, F, G | In-order: F, C, G):**
    *   Root of RST is **C**.
    *   In-order split by C: Left = `F`, Right = `G`.
    *   Left child of C is **F**, right child is **G**.

**Constructed Tree:**
```text
        A
      /   \
     B     C
    / \   / \
   D   E F   G
      / \
     H   I
```

**Post-order Traversal (Left, Right, Root):**
`D, H, I, E, B, F, G, C, A`

---

## Q.1 c) Write pseudocode to create a Doubly Linked List (DLL). Implement insert at beginning, insert at end, delete a node, and display operations. (7 Marks)

**Answer:**

```cpp
// Node Structure
Struct Node {
    Data data
    Node prev
    Node next
}

// Global Head Pointer
Node head = NULL

// 1. Insert at Beginning
Function InsertAtBeginning(val):
    newNode = allocate Node
    newNode.data = val
    newNode.prev = NULL
    newNode.next = head
    
    If head != NULL:
        head.prev = newNode
        
    head = newNode

// 2. Insert at End
Function InsertAtEnd(val):
    newNode = allocate Node
    newNode.data = val
    newNode.next = NULL
    
    If head == NULL:
        newNode.prev = NULL
        head = newNode
        Return
        
    temp = head
    While temp.next != NULL:
        temp = temp.next
        
    temp.next = newNode
    newNode.prev = temp

// 3. Delete a Specific Node (by value)
Function DeleteNode(val):
    If head == NULL:
        Print "List is empty"
        Return
        
    temp = head
    
    // Find the node
    While temp != NULL AND temp.data != val:
        temp = temp.next
        
    If temp == NULL:
        Print "Node not found"
        Return
        
    // If node to be deleted is head
    If head == temp:
        head = temp.next
        
    // Change next only if node to be deleted is NOT the last node
    If temp.next != NULL:
        temp.next.prev = temp.prev
        
    // Change prev only if node to be deleted is NOT the first node
    If temp.prev != NULL:
        temp.prev.next = temp.next
        
    Free temp

// 4. Display
Function Display():
    temp = head
    If temp == NULL:
        Print "List is Empty"
        Return
        
    Print "NULL <-> "
    While temp != NULL:
        Print temp.data + " <-> "
        temp = temp.next
    Print "NULL"
```

---

## Q.2 a) Create a Hash table of size 10 using h(key) = key mod 10. Insert: 25, 42, 96, 32, 65, 52, 85, 72, 105, 15 using Linear Probing with and without replacement. (6 Marks)

**Answer:**

**Given:**
Size (M) = 10 (Indices 0 to 9)
Hash Function: `h(k) = k % 10`
Keys: `25, 42, 96, 32, 65, 52, 85, 72, 105, 15`

### 1. Linear Probing WITHOUT Replacement

*Rule: If collision, find the next empty slot `(i+1)%10` and place the new key there.*

*   25 % 10 = 5 → Empty. Place at 5.
*   42 % 10 = 2 → Empty. Place at 2.
*   96 % 10 = 6 → Empty. Place at 6.
*   32 % 10 = 2 → Collision with 42. Next empty is 3. Place at 3.
*   65 % 10 = 5 → Collision with 25. Next empty is 7 (since 6 is full). Place at 7.
*   52 % 10 = 2 → Collision. Slots 2,3 full. Next empty is 4. Place at 4.
*   85 % 10 = 5 → Collision. Slots 5,6,7 full. Next empty is 8. Place at 8.
*   72 % 10 = 2 → Collision. Slots 2-8 full. Next empty is 9. Place at 9.
*   105 % 10 = 5 → Collision. Slots 5-9 full. Next empty is 0. Place at 0.
*   15 % 10 = 5 → Collision. Slots 5-0 full. Next empty is 1. Place at 1.

**Final Table (Without Replacement):**
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Key** | 105 | 15 | 42 | 32 | 52 | 25 | 96 | 65 | 85 | 72 |

### 2. Linear Probing WITH Replacement

*Rule: If collision occurs and the existing element is NOT at its home index, replace it with the new key (which IS at its home index), and re-insert the displaced element in the next empty slot.*

*   25 % 10 = 5 → Place at 5.
*   42 % 10 = 2 → Place at 2.
*   96 % 10 = 6 → Place at 6.
*   32 % 10 = 2 → Collision with 42 (home). Place at 3.
*   65 % 10 = 5 → Collision with 25 (home). Place at 7.
*   52 % 10 = 2 → Collision with 42 (home). Place at 4.
*   85 % 10 = 5 → Collision with 25 (home). Place at 8.
*   72 % 10 = 2 → Collision with 42 (home). Place at 9.
*   105 % 10 = 5 → Collision with 25 (home). Place at 0.
*   15 % 10 = 5 → Collision with 25 (home). Place at 1.

*(Note: In this specific dataset, because elements at collision points were always at their home addresses initially, the table remains the same as without replacement. A replacement only happens if a key hashes to an index occupied by a shifted key.)*

**Final Table (With Replacement):** (Same as above for this sequence)
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Key** | 105 | 15 | 42 | 32 | 52 | 25 | 96 | 65 | 85 | 72 |

---

## Q.2 c) Explain the drawbacks of implementing a Queue using an array. Write pseudocode to implement a Queue using a Singly Linked List with Enqueue and Dequeue operations. (7 Marks)

**Answer:**

**Drawbacks of Array-Based Queue:**
1.  **Static Size:** The size of the array must be declared in advance. If the queue becomes full, no new elements can be added (Queue Overflow), even if memory is available in the system.
2.  **Memory Wastage (Linear Queue):** In a simple linear queue, when elements are dequeued, the spaces at the front become empty. However, the `rear` pointer continues to increment, eventually reaching the end of the array, leading to a false "Queue Full" condition while spaces exist at the front. (Circular queues solve this, but still have static size).
3.  **Costly Shifting:** If shifting is used to solve the empty space problem, moving all elements to the front takes O(n) time.

**Pseudocode: Queue using Singly Linked List**

```cpp
// Node Structure
Struct Node {
    Data data
    Node next
}

// Global Pointers
Node front = NULL
Node rear = NULL

// 1. Enqueue (Insert at Rear)
Function Enqueue(val):
    newNode = allocate Node
    newNode.data = val
    newNode.next = NULL
    
    // If queue is empty
    If front == NULL and rear == NULL:
        front = rear = newNode
        Return
        
    // Add to rear and update rear pointer
    rear.next = newNode
    rear = newNode

// 2. Dequeue (Delete from Front)
Function Dequeue():
    // If queue is empty
    If front == NULL:
        Print "Queue Underflow"
        Return -1
        
    temp = front
    val = temp.data
    
    // If only one element was in queue
    If front == rear:
        front = rear = NULL
    Else:
        front = front.next
        
    Free temp
    Return val
```
#   P r e d i c t e d   A n s w e r s   f o r   P a p e r   4   ( C o n t i n u e d )  
  
 # #   Q . 3   a )   P e r f o r m   a   d r y   r u n   o f   t h e   M e r g e   S o r t   a l g o r i t h m   o n   t h e   a r r a y :   [ 3 5 ,   1 8 ,   4 2 ,   7 ,   2 9 ,   6 3 ,   1 4 ,   5 1 ] .   S h o w   t h e   s t e p - b y - s t e p   p r o c e s s   o f   d i v i d i n g   t h e   a r r a y   a n d   t h e n   m e r g i n g   t h e   s u b - a r r a y s   i n   s o r t e d   o r d e r .   ( 7   M a r k s )  
  
 * * A n s w e r : * *  
  
 * * I n i t i a l   A r r a y : * *   ` [ 3 5 ,   1 8 ,   4 2 ,   7 ,   2 9 ,   6 3 ,   1 4 ,   5 1 ] `  
  
 * * P h a s e   1 :   D i v i d e   ( S p l i t t i n g   i n t o   h a l v e s   u n t i l   s i n g l e   e l e m e n t s ) * *  
 *       * * S t e p   1 : * *   S p l i t   i n t o   t w o   h a l v e s  
         *       L e f t :   ` [ 3 5 ,   1 8 ,   4 2 ,   7 ] `  
         *       R i g h t :   ` [ 2 9 ,   6 3 ,   1 4 ,   5 1 ] `  
 *       * * S t e p   2 : * *   S p l i t   l e f t   a n d   r i g h t   h a l v e s   a g a i n  
         *       L L :   ` [ 3 5 ,   1 8 ] ` ,   L R :   ` [ 4 2 ,   7 ] `  
         *       R L :   ` [ 2 9 ,   6 3 ] ` ,   R R :   ` [ 1 4 ,   5 1 ] `  
 *       * * S t e p   3 : * *   S p l i t   i n t o   s i n g l e   e l e m e n t s  
         *       ` [ 3 5 ] ` ,   ` [ 1 8 ] ` ,   ` [ 4 2 ] ` ,   ` [ 7 ] ` ,   ` [ 2 9 ] ` ,   ` [ 6 3 ] ` ,   ` [ 1 4 ] ` ,   ` [ 5 1 ] `  
  
 * * P h a s e   2 :   C o n q u e r   ( M e r g i n g   s o r t e d   s u b - a r r a y s ) * *  
 *       * * M e r g e   S t e p   1   ( p a i r s ) : * *  
         *       M e r g e   ` [ 3 5 ] `   a n d   ` [ 1 8 ] `   - >   ` [ 1 8 ,   3 5 ] `  
         *       M e r g e   ` [ 4 2 ] `   a n d   ` [ 7 ] `   - >   ` [ 7 ,   4 2 ] `  
         *       M e r g e   ` [ 2 9 ] `   a n d   ` [ 6 3 ] `   - >   ` [ 2 9 ,   6 3 ] `  
         *       M e r g e   ` [ 1 4 ] `   a n d   ` [ 5 1 ] `   - >   ` [ 1 4 ,   5 1 ] `  
 *       * * M e r g e   S t e p   2   ( f o u r s ) : * *  
         *       M e r g e   ` [ 1 8 ,   3 5 ] `   a n d   ` [ 7 ,   4 2 ] `   - >   ` [ 7 ,   1 8 ,   3 5 ,   4 2 ] `  
         *       M e r g e   ` [ 2 9 ,   6 3 ] `   a n d   ` [ 1 4 ,   5 1 ] `   - >   ` [ 1 4 ,   2 9 ,   5 1 ,   6 3 ] `  
 *       * * M e r g e   S t e p   3   ( f i n a l   a r r a y ) : * *  
         *       M e r g e   ` [ 7 ,   1 8 ,   3 5 ,   4 2 ] `   a n d   ` [ 1 4 ,   2 9 ,   5 1 ,   6 3 ] `   - >   ` [ 7 ,   1 4 ,   1 8 ,   2 9 ,   3 5 ,   4 2 ,   5 1 ,   6 3 ] `  
  
 * * F i n a l   S o r t e d   A r r a y : * *   ` [ 7 ,   1 4 ,   1 8 ,   2 9 ,   3 5 ,   4 2 ,   5 1 ,   6 3 ] `  
  
 - - -  
  
 # #   Q . 5   a )   C o n s t r u c t   a n   A V L   T r e e   b y   i n s e r t i n g   t h e   f o l l o w i n g   e l e m e n t s   i n   t h e   g i v e n   o r d e r :   5 0 ,   2 5 ,   7 5 ,   1 0 ,   3 0 ,   6 0 ,   8 0 ,   5 ,   3 5 ,   5 5 .   S h o w   t h e   b a l a n c e   f a c t o r   o f   e a c h   n o d e   a f t e r   e v e r y   i n s e r t i o n .   C l e a r l y   n a m e   t h e   t y p e   o f   r o t a t i o n   u s e d .   ( 7   M a r k s )  
  
 * * A n s w e r : * *  
 * ( N o t e :   B a l a n c e   F a c t o r   =   H e i g h t   o f   L e f t   S u b t r e e   -   H e i g h t   o f   R i g h t   S u b t r e e .   V a l i d   B F s   a r e   - 1 ,   0 ,   1 ) *  
  
 1 .     * * I n s e r t   5 0 : * *  
         ` ` ` t e x t  
         5 0 ( 0 )  
         ` ` `  
  
 2 .     * * I n s e r t   2 5 : * *  
         ` ` ` t e x t  
                 5 0 ( 1 )  
               /  
         2 5 ( 0 )  
         ` ` `  
  
 3 .     * * I n s e r t   7 5 : * *  
         ` ` ` t e x t  
                 5 0 ( 0 )  
               /         \  
         2 5 ( 0 )     7 5 ( 0 )  
         ` ` `  
  
 4 .     * * I n s e r t   1 0 : * *  
         ` ` ` t e x t  
                       5 0 ( 1 )  
                     /         \  
               2 5 ( 1 )     7 5 ( 0 )  
             /  
         1 0 ( 0 )  
         ` ` `  
  
 5 .     * * I n s e r t   3 0 : * *  
         ` ` ` t e x t  
                       5 0 ( 1 )  
                     /         \  
               2 5 ( 0 )     7 5 ( 0 )  
             /         \  
         1 0 ( 0 )     3 0 ( 0 )  
         ` ` `  
  
 6 .     * * I n s e r t   6 0 : * *  
         ` ` ` t e x t  
                       5 0 ( 1 )  
                     /         \  
               2 5 ( 0 )     7 5 ( 1 )  
             /         \     /  
         1 0         3 0   6 0 ( 0 )  
         ` ` `  
  
 7 .     * * I n s e r t   8 0 : * *  
         ` ` ` t e x t  
                       5 0 ( 0 )  
                     /         \  
               2 5 ( 0 )     7 5 ( 0 )  
             /       \       /       \  
         1 0       3 0     6 0       8 0 ( 0 )  
         ` ` `  
  
 8 .     * * I n s e r t   5 : * *  
         ` ` ` t e x t  
                       5 0 ( 1 )  
                     /         \  
               2 5 ( 1 )     7 5 ( 0 )  
             /       \       /       \  
         1 0 ( 1 )   3 0   6 0       8 0  
         /  
       5 ( 0 )  
         ` ` `  
  
 9 .     * * I n s e r t   3 5 : * *  
         ` ` ` t e x t  
                       5 0 ( 1 )  
                     /         \  
               2 5 ( 1 )     7 5 ( 0 )  
             /       \       /       \  
         1 0 ( 1 )   3 0 ( - 1 )   6 0   8 0  
         /               \  
       5 ( 0 )           3 5 ( 0 )  
         ` ` `  
  
 1 0 .   * * I n s e r t   5 5 : * *  
         ` ` ` t e x t  
                       5 0 ( 1 )  
                     /         \  
               2 5 ( 1 )     7 5 ( 2 )     < - -   U n b a l a n c e d   a t   7 5 !   L e f t - L e f t   h e a v y   ( L L   c a s e )  
             /       \       /       \  
         1 0       3 0     6 0 ( 1 )   8 0  
         /           \     /  
       5             3 5   5 5 ( 0 )  
         ` ` `  
         * * R e b a l a n c i n g : * *   W e   i n s e r t e d   5 5   i n t o   t h e   l e f t   s u b t r e e   o f   t h e   l e f t   c h i l d   o f   7 5 .   T h i s   i s   a n   * * L L   R o t a t i o n * *   a r o u n d   7 5 .  
         *       6 0   m o v e s   u p   t o   r e p l a c e   7 5 .  
         *       7 5   b e c o m e s   t h e   r i g h t   c h i l d   o f   6 0 .  
         *       T h e   r i g h t   c h i l d   o f   6 0   ( i f   a n y )   b e c o m e s   t h e   l e f t   c h i l d   o f   7 5 .  
  
         * * F i n a l   A V L   T r e e   ( A f t e r   L L   R o t a t i o n ) : * *  
         ` ` ` t e x t  
                       5 0 ( 0 )  
                     /         \  
               2 5 ( 1 )     6 0 ( 0 )  
             /       \       /       \  
         1 0 ( 1 )   3 0   5 5 ( 0 )   7 5 ( 0 )  
         /           \                   \  
       5 ( 0 )       3 5 ( 0 )           8 0 ( 0 )  
         ` ` `  
  
 - - -  
  
 # #   Q . 7   b )   A p p l y   t h e   F l o y d - W a r s h a l l   a l g o r i t h m   t o   f i n d   t h e   t r a n s i t i v e   c l o s u r e   o f   t h e   f o l l o w i n g   d i r e c t e d   g r a p h .   S h o w   t h e   i n t e r m e d i a t e   m a t r i c e s   a f t e r   e a c h   i t e r a t i o n   ( k = 1 , 2 , 3 , 4 ) .   ( 6   M a r k s )  
 * V e r t i c e s :   1 ,   2 ,   3 ,   4   |   E d g e s :   1 - > 2 ,   2 - > 3 ,   3 - > 4 ,   4 - > 1 ,   2 - > 4 *  
  
 * * A n s w e r : * *  
  
 * * I n i t i a l   M a t r i x   ( D i r e c t   E d g e s ) ,   T ( 0 ) : * *  
 ` ` `  
       1     2     3     4  
 1   [ 0     1     0     0 ]  
 2   [ 0     0     1     1 ]  
 3   [ 0     0     0     1 ]  
 4   [ 1     0     0     0 ]  
 ` ` `  
  
 * * I t e r a t i o n   1   ( k = 1 ) :   P a t h s   v i a   v e r t e x   1 * *  
 ` T [ 4 ] [ 1 ] = 1 `   a n d   ` T [ 1 ] [ 2 ] = 1 `   = >   n e w   p a t h   ` T [ 4 ] [ 2 ]   =   1 ` .  
 ` ` `  
       1     2     3     4  
 1   [ 0     1     0     0 ]  
 2   [ 0     0     1     1 ]  
 3   [ 0     0     0     1 ]  
 4   [ 1     1     0     0 ]     < - -   T [ 4 ] [ 2 ]   u p d a t e d  
 ` ` `  
  
 * * I t e r a t i o n   2   ( k = 2 ) :   P a t h s   v i a   v e r t e x   2 * *  
 ` T [ 1 ] [ 2 ] = 1 `   a n d   ` T [ 2 ] [ 3 ] = 1 `   = >   ` T [ 1 ] [ 3 ]   =   1 `  
 ` T [ 1 ] [ 2 ] = 1 `   a n d   ` T [ 2 ] [ 4 ] = 1 `   = >   ` T [ 1 ] [ 4 ]   =   1 `  
 ` T [ 4 ] [ 2 ] = 1 `   a n d   ` T [ 2 ] [ 3 ] = 1 `   = >   ` T [ 4 ] [ 3 ]   =   1 `  
 ` T [ 4 ] [ 2 ] = 1 `   a n d   ` T [ 2 ] [ 4 ] = 1 `   = >   ` T [ 4 ] [ 4 ]   =   1 `  
 ` ` `  
       1     2     3     4  
 1   [ 0     1     1     1 ]     < - -   T [ 1 ] [ 3 ] ,   T [ 1 ] [ 4 ]   u p d a t e d  
 2   [ 0     0     1     1 ]  
 3   [ 0     0     0     1 ]  
 4   [ 1     1     1     1 ]     < - -   T [ 4 ] [ 3 ] ,   T [ 4 ] [ 4 ]   u p d a t e d  
 ` ` `  
  
 * * I t e r a t i o n   3   ( k = 3 ) :   P a t h s   v i a   v e r t e x   3 * *  
 N o   n e w   p a t h s   d i s c o v e r e d .  
 ` ` `  
       1     2     3     4  
 1   [ 0     1     1     1 ]  
 2   [ 0     0     1     1 ]  
 3   [ 0     0     0     1 ]  
 4   [ 1     1     1     1 ]  
 ` ` `  
  
 * * I t e r a t i o n   4   ( k = 4 ) :   P a t h s   v i a   v e r t e x   4 * *  
 T h i s   c o m p l e t e s   t h e   c y c l e ,   m a k i n g   e v e r y   v e r t e x   r e a c h a b l e .   A l l   0 s   b e c o m e   1 s .  
 ` ` `  
       1     2     3     4  
 1   [ 1     1     1     1 ]  
 2   [ 1     1     1     1 ]  
 3   [ 1     1     1     1 ]  
 4   [ 1     1     1     1 ]  
 ` ` `  
 * * F i n a l   T r a n s i t i v e   C l o s u r e   M a t r i x : * *   A l l   e l e m e n t s   a r e   1 ,   m e a n i n g   i t ' s   a   S t r o n g l y   C o n n e c t e d   G r a p h .  
 

# Predicted Answers for Paper 4 (Part 2)

## Q.2 b) Construct a Huffman Tree for the characters and their frequencies: A:5, B:9, C:12, D:13, E:16, F:45. Find the Huffman code for each character. (7 Marks)

**Answer:**

**Step 1: Sort by frequency (Ascending)**
Nodes: `A(5), B(9), C(12), D(13), E(16), F(45)`

**Step 2: Build the Huffman Tree**
*Iteration 1:* Take two lowest frequencies A(5) and B(9). Combine them to create a parent node with frequency 14.
List: `C(12), D(13), AB(14), E(16), F(45)`
```text
   14
  /  \
A(5) B(9)
```

*Iteration 2:* Take lowest two: C(12) and D(13). Combine them.
List: `AB(14), E(16), CD(25), F(45)`
```text
    25
   /  \
C(12) D(13)
```

*Iteration 3:* Take lowest two: AB(14) and E(16). Combine them.
List: `CD(25), ABE(30), F(45)`
```text
      30
     /  \
   14    E(16)
  /  \
A(5) B(9)
```

*Iteration 4:* Take lowest two: CD(25) and ABE(30). Combine them.
List: `F(45), CDABE(55)`
```text
         55
       /    \
     25      30
    / \     /  \
  C(12)D(13)14  E(16)
           / \
         A(5) B(9)
```

*Iteration 5:* Combine the last two: F(45) and CDABE(55). Root frequency = 100.
```text
             100
           /     \
       F(45)       55
                 /    \
               25      30
              / \     /  \
            C(12)D(13)14  E(16)
                     / \
                   A(5) B(9)
```

**Step 3: Assign Codes (0 for left branch, 1 for right branch)**
```text
             100
          0/     \1
       F(45)       55
                 0/    \1
               25      30
             0/ \1    0/  \1
            C(12)D(13)14  E(16)
                    0/ \1
                   A(5) B(9)
```

**Final Huffman Codes:**
*   **F:** 0
*   **C:** 100
*   **D:** 101
*   **A:** 1100
*   **B:** 1101
*   **E:** 111

*(Total bits calculation: (45*1) + (12*3) + (13*3) + (5*4) + (9*4) + (16*3) = 45 + 36 + 39 + 20 + 36 + 48 = 224 bits)*

---

## Q.3 b) Perform a complete Heap Sort on the array [20, 35, 15, 7, 45, 30, 10, 25]. Show BUILD-MAX-HEAP and extractions. (7 Marks)

**Answer:**

**Step 1: BUILD-MAX-HEAP**
Initial Array: `[20, 35, 15, 7, 45, 30, 10, 25]`
Represented as a complete binary tree:
```text
        20
      /    \
    35      15
   /  \    /  \
  7   45  30   10
 /
25
```
Start heapifying from the last non-leaf node (index `n/2 - 1` = `8/2 - 1` = 3, which is 7).
*   **Heapify(7):** Left child 25 is greater. Swap 7 and 25.
    *   Array: `[20, 35, 15, 25, 45, 30, 10, 7]`
*   **Heapify(15):** Left child 30 is greater. Swap 15 and 30.
    *   Array: `[20, 35, 30, 25, 45, 15, 10, 7]`
*   **Heapify(35):** Right child 45 is greater. Swap 35 and 45.
    *   Array: `[20, 45, 30, 25, 35, 15, 10, 7]`
*   **Heapify(20):** Left child 45 is greater. Swap 20 and 45. Then heapify 20 again (its children are 25 and 35, swap with 35).
    *   Array: `[45, 35, 30, 25, 20, 15, 10, 7]`
**Initial Max-Heap is built:** `[45, 35, 30, 25, 20, 15, 10, 7]`

**Step 2: Extraction & Sorting Phase**
Swap the root (maximum element) with the last element, reduce heap size, and heapify the new root.
*   **Extract 45:** Swap 45 and 7. Array: `[7, 35, 30, 25, 20, 15, 10 | 45]`
    *   Heapify(7): Swap with 35, then 25. Result: `[35, 25, 30, 7, 20, 15, 10]`
*   **Extract 35:** Swap 35 and 10. Array: `[10, 25, 30, 7, 20, 15 | 35, 45]`
    *   Heapify(10): Swap with 30, then 15. Result: `[30, 25, 15, 7, 20, 10]`
*   **Extract 30:** Swap 30 and 10. Array: `[10, 25, 15, 7, 20 | 30, 35, 45]`
    *   Heapify(10): Swap with 25, then 20. Result: `[25, 20, 15, 7, 10]`
*   **Extract 25:** Swap 25 and 10. Array: `[10, 20, 15, 7 | 25, 30, 35, 45]`
    *   Heapify(10): Swap with 20. Result: `[20, 10, 15, 7]`
*   **Extract 20:** Swap 20 and 7. Array: `[7, 10, 15 | 20, 25, 30, 35, 45]`
    *   Heapify(7): Swap with 15. Result: `[15, 10, 7]`
*   **Extract 15:** Swap 15 and 7. Array: `[7, 10 | 15, 20, 25, 30, 35, 45]`
    *   Heapify(7): Swap with 10. Result: `[10, 7]`
*   **Extract 10:** Swap 10 and 7. Array: `[7 | 10, 15, 20, 25, 30, 35, 45]`

**Final Sorted Array:** `[7, 10, 15, 20, 25, 30, 35, 45]`

---

## Q.4 a) Sort using Bubble Sort: [52, 17, 63, 28, 41, 9, 34]. Show the status after each complete pass. (7 Marks)

**Answer:**

**Initial Array:** `[52, 17, 63, 28, 41, 9, 34]`

*   **Pass 1:**
    *   (52, 17) -> swap -> [17, 52, 63, 28, 41, 9, 34]
    *   (52, 63) -> no swap -> [17, 52, 63, 28, 41, 9, 34]
    *   (63, 28) -> swap -> [17, 52, 28, 63, 41, 9, 34]
    *   (63, 41) -> swap -> [17, 52, 28, 41, 63, 9, 34]
    *   (63, 9)  -> swap -> [17, 52, 28, 41, 9, 63, 34]
    *   (63, 34) -> swap -> [17, 52, 28, 41, 9, 34, **63**] (Largest element bubbled to the end)

*   **Pass 2:**
    *   Compare up to 2nd last element.
    *   Result: `[17, 28, 41, 9, 34, **52, 63**]`

*   **Pass 3:**
    *   Result: `[17, 28, 9, 34, **41, 52, 63**]`

*   **Pass 4:**
    *   Result: `[17, 9, 28, **34, 41, 52, 63**]`

*   **Pass 5:**
    *   Result: `[9, 17, **28, 34, 41, 52, 63**]`

*   **Pass 6:** (No swaps occur, array is sorted, algorithm can terminate early if optimized)
    *   Final Result: `[9, 17, 28, 34, 41, 52, 63]`

---

## Q.4 b) Write pseudocode for Quick Sort algorithm. Trace its execution on [30, 15, 42, 8, 25, 50, 12]. Analyze time complexity. (7 Marks)

**Answer:**

**Pseudocode:**
```cpp
Function QuickSort(arr, low, high):
    If low < high:
        // Find pivot index
        pi = Partition(arr, low, high)
        // Recursively sort elements before and after partition
        QuickSort(arr, low, pi - 1)
        QuickSort(arr, pi + 1, high)

Function Partition(arr, low, high):
    pivot = arr[high]  // Choose last element as pivot
    i = (low - 1)      // Index of smaller element

    For j = low to high - 1:
        If arr[j] <= pivot:
            i = i + 1
            Swap arr[i] and arr[j]
            
    Swap arr[i + 1] and arr[high]
    Return (i + 1)
```

**Trace on `[30, 15, 42, 8, 25, 50, 12]`:**
1.  **Initial Call:** QuickSort(arr, 0, 6)
    *   Pivot = 12 (last element)
    *   Compare elements with 12. Only 8 is smaller.
    *   Swap 30 and 8 -> `[8, 15, 42, 30, 25, 50, 12]`
    *   Swap pivot (12) with element at `i+1` (15).
    *   Array: `[8, 12, 42, 30, 25, 50, 15]`
    *   Pivot 12 is at index 1.
2.  **Left Recursive Call:** QuickSort(arr, 0, 0)
    *   Subarray `[8]`. Already sorted. (low not < high).
3.  **Right Recursive Call:** QuickSort(arr, 2, 6)
    *   Subarray: `[42, 30, 25, 50, 15]`
    *   Pivot = 15. No elements are smaller.
    *   Swap pivot (15) with 42.
    *   Array: `[15, 30, 25, 50, 42]`
    *   Pivot 15 is at index 2.
4.  **Right Recursive Call 2:** QuickSort(arr, 3, 6)
    *   Subarray: `[30, 25, 50, 42]`
    *   Pivot = 42. Smaller elements: 30, 25.
    *   Array becomes `[30, 25, 42, 50]` after partitioning around 42.
5.  **Further calls** will sort `[30, 25]` into `[25, 30]`.
*   **Final Sorted Array:** `[8, 12, 15, 25, 30, 42, 50]`

**Time Complexity Analysis:**
*   **Best Case: O(n log n)**. Occurs when the partition process always picks the middle element as pivot (balanced split).
*   **Average Case: O(n log n)**.
*   **Worst Case: O(n²)**. Occurs when the array is already sorted (ascending or descending) and we always pick the greatest or smallest element as pivot, resulting in highly unbalanced partitions (size 0 and size n-1).


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
