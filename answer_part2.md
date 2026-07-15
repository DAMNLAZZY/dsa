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
