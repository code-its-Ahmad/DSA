# Data Structures & Algorithms (DSA) — Complete Preparation Guide

> A production-quality, interview-focused DSA roadmap covering **complexity analysis, data structures, algorithms, problem-solving patterns, pseudocode, edge cases, and interview preparation**.
>
> This README is designed as a complete preparation reference from beginner to advanced level.

---

## Table of Contents

1. [How to Use This Guide](#how-to-use-this-guide)
2. [DSA Fundamentals](#dsa-fundamentals)
3. [Time and Space Complexity](#time-and-space-complexity)
4. [Mathematical Foundations](#mathematical-foundations)
5. [Arrays](#arrays)
6. [Strings](#strings)
7. [Linked Lists](#linked-lists)
8. [Stacks](#stacks)
9. [Queues and Deques](#queues-and-deques)
10. [Hash Tables](#hash-tables)
11. [Sets](#sets)
12. [Recursion](#recursion)
13. [Backtracking](#backtracking)
14. [Searching](#searching)
15. [Sorting](#sorting)
16. [Two Pointers](#two-pointers)
17. [Sliding Window](#sliding-window)
18. [Prefix Sum and Difference Arrays](#prefix-sum-and-difference-arrays)
19. [Fast and Slow Pointers](#fast-and-slow-pointers)
20. [Intervals](#intervals)
21. [Monotonic Stack](#monotonic-stack)
22. [Heap / Priority Queue](#heap--priority-queue)
23. [Binary Trees](#binary-trees)
24. [Binary Search Trees](#binary-search-trees)
25. [Balanced Trees](#balanced-trees)
26. [Tries](#tries)
27. [Graphs](#graphs)
28. [Graph Traversal](#graph-traversal)
29. [Shortest Path Algorithms](#shortest-path-algorithms)
30. [Minimum Spanning Tree](#minimum-spanning-tree)
31. [Disjoint Set Union](#disjoint-set-union)
32. [Topological Sorting](#topological-sorting)
33. [Dynamic Programming](#dynamic-programming)
34. [Greedy Algorithms](#greedy-algorithms)
35. [Bit Manipulation](#bit-manipulation)
36. [Advanced String Algorithms](#advanced-string-algorithms)
37. [Advanced Data Structures](#advanced-data-structures)
38. [Range Query Algorithms](#range-query-algorithms)
39. [Divide and Conquer](#divide-and-conquer)
40. [Amortized Analysis](#amortized-analysis)
41. [Problem-Solving Framework](#problem-solving-framework)
42. [Common DSA Patterns](#common-dsa-patterns)
43. [Important Interview Problems](#important-interview-problems)
44. [Complexity Cheat Sheet](#complexity-cheat-sheet)
45. [Common Mistakes](#common-mistakes)
46. [Interview Checklist](#interview-checklist)
47. [8-Week Preparation Plan](#8-week-preparation-plan)
48. [Final Master Checklist](#final-master-checklist)

---

# How to Use This Guide

Use DSA preparation in four stages:

### Stage 1 — Understand

Learn:

- What the data structure stores.
- Why it exists.
- How it works internally.
- Which operations it supports.
- Time complexity.
- Space complexity.
- Typical use cases.

### Stage 2 — Implement

Implement every important structure from scratch:

- Array-based stack.
- Linked list.
- Queue.
- Hash table.
- Heap.
- Binary tree.
- BST.
- Trie.
- Graph.
- Union-Find.

### Stage 3 — Recognize Patterns

Do not memorize hundreds of solutions. Learn to identify:

- Two pointers.
- Sliding window.
- Binary search.
- Prefix sum.
- Hashing.
- Stack.
- Heap.
- DFS.
- BFS.
- Backtracking.
- Greedy.
- Dynamic programming.
- Graph algorithms.

### Stage 4 — Solve and Explain

For every problem:

1. Clarify the requirements.
2. Identify constraints.
3. State the brute-force approach.
4. Improve it.
5. Explain the invariant.
6. Write the algorithm.
7. Analyze time complexity.
8. Analyze space complexity.
9. Test edge cases.
10. Discuss alternatives.

---

# DSA Fundamentals

## What is a Data Structure?

A data structure is a method of organizing and storing data so operations can be performed efficiently.

Examples:

- Array
- Linked List
- Stack
- Queue
- Hash Table
- Heap
- Tree
- Graph
- Trie

## What is an Algorithm?

An algorithm is a finite sequence of well-defined steps used to solve a problem.

A good algorithm should be:

- Correct.
- Finite.
- Deterministic where appropriate.
- Efficient.
- Understandable.
- Robust against edge cases.

## Correctness

An algorithm is useful only if it produces the correct result.

A common proof structure:

1. Define the invariant.
2. Show it is true before the operation.
3. Show each operation preserves it.
4. Show the invariant implies correctness at termination.

---

# Time and Space Complexity

## Big-O

Big-O describes an asymptotic upper bound on resource growth.

Common complexities:

| Complexity | Name | Typical Example |
|---|---|---|
| `O(1)` | Constant | Array index access |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | Array traversal |
| `O(n log n)` | Linearithmic | Merge sort |
| `O(n²)` | Quadratic | Simple nested loops |
| `O(n³)` | Cubic | Triple nested loops |
| `O(2ⁿ)` | Exponential | Naive subset recursion |
| `O(n!)` | Factorial | Naive permutation generation |

## Big-O Rules

### Sequential operations

```text
O(n) + O(n) = O(n)
```

### Nested operations

```text
O(n) * O(n) = O(n²)
```

### Ignore constants

```text
O(2n) = O(n)
```

### Keep dominant terms

```text
O(n² + n) = O(n²)
```

## Space Complexity

Separate:

- Input space.
- Auxiliary space.
- Recursion stack.
- Data structure storage.

Example:

```text
recursive DFS:
time  = O(V + E)
space = O(V)
```

---

# Mathematical Foundations

Know:

- Prime numbers.
- Factors.
- GCD.
- LCM.
- Modular arithmetic.
- Powers.
- Logarithms.
- Combinations.
- Permutations.
- Bit representation.

## Euclidean GCD

```text
gcd(a, b):
    while b != 0:
        a, b = b, a mod b
    return a
```

Complexity:

```text
O(log(min(a, b)))
```

## LCM

```text
lcm(a, b) = |a / gcd(a, b) * b|
```

Divide before multiply to reduce overflow risk.

## Sieve of Eratosthenes

Find all primes up to `n`.

```text
isPrime[0..n] = true
isPrime[0] = isPrime[1] = false

for p from 2 while p*p <= n:
    if isPrime[p]:
        for multiple from p*p to n step p:
            isPrime[multiple] = false
```

Complexity:

- Time: `O(n log log n)`
- Space: `O(n)`

---

# Arrays

Arrays store elements in contiguous/indexable storage in the common array model.

## Operations

| Operation | Typical Complexity |
|---|---:|
| Access by index | O(1) |
| Search unsorted | O(n) |
| Insert at end | O(1) amortized for dynamic arrays |
| Insert at beginning | O(n) |
| Delete at beginning | O(n) |
| Delete from middle | O(n) |

## Important Array Techniques

- Traversal.
- In-place modification.
- Prefix sums.
- Difference arrays.
- Two pointers.
- Sliding window.
- Binary search.
- Sorting.
- Hashing.

## Array Edge Cases

Always consider:

- Empty array.
- One element.
- All equal values.
- Negative values.
- Already sorted.
- Reverse sorted.
- Duplicate values.
- Integer overflow.
- Very large input.

---

# Strings

Strings are sequences of characters.

Important operations:

- Frequency counting.
- Character mapping.
- Palindrome checking.
- Substring search.
- Anagram checking.
- Prefix/suffix processing.
- Pattern matching.

## Palindrome

Two-pointer approach:

```text
left = 0
right = n - 1

while left < right:
    if s[left] != s[right]:
        return false
    left++
    right--

return true
```

Complexity:

- Time: `O(n)`
- Space: `O(1)` if indexing is constant-space.

---

# Linked Lists

A linked list stores nodes connected by references/pointers.

Node:

```text
Node:
    value
    next
```

Doubly linked list:

```text
Node:
    prev
    value
    next
```

## Complexity

| Operation | Singly Linked List |
|---|---:|
| Access by index | O(n) |
| Search | O(n) |
| Insert at head | O(1) |
| Delete at head | O(1) |
| Insert after known node | O(1) |
| Delete after known predecessor | O(1) |

## Reverse Linked List

Iterative:

```text
prev = null
current = head

while current != null:
    nextNode = current.next
    current.next = prev
    prev = current
    current = nextNode

return prev
```

Complexity:

- Time: `O(n)`
- Space: `O(1)`

## Important Linked List Problems

- Reverse list.
- Detect cycle.
- Find cycle start.
- Find middle.
- Merge sorted lists.
- Remove nth node from end.
- Palindrome linked list.
- Intersection of two lists.
- Reverse in groups.

---

# Stacks

A stack follows:

```text
LIFO = Last In, First Out
```

Operations:

- Push.
- Pop.
- Peek/top.
- Is empty.

Typical complexity:

```text
push = O(1)
pop  = O(1)
peek = O(1)
```

## Applications

- Function calls.
- Expression parsing.
- Parentheses matching.
- DFS.
- Undo/redo.
- Monotonic stack.
- Backtracking.

## Valid Parentheses

Use a stack:

```text
for each character:
    if opening:
        push
    else:
        if stack empty:
            return false
        if top does not match:
            return false
        pop

return stack is empty
```

---

# Queues and Deques

Queue:

```text
FIFO = First In, First Out
```

Operations:

- Enqueue.
- Dequeue.
- Front.

Deque supports both ends.

Applications:

- BFS.
- Scheduling.
- Sliding-window maximum.
- Producer/consumer systems.

Avoid implementing a queue by repeatedly shifting an array because that can make dequeue `O(n)`.

---

# Hash Tables

Hash tables provide average-case constant-time lookup under good hashing and load management.

Typical operations:

```text
insert  -> O(1) average
search  -> O(1) average
delete  -> O(1) average
```

Worst-case behavior depends on implementation and hashing.

## Collision Handling

### Separate chaining

Each bucket contains a collection of entries.

### Open addressing

Store entries directly in the table and probe for another location.

Common probing:

- Linear probing.
- Quadratic probing.
- Double hashing.

## Load Factor

```text
load factor = number of stored entries / table capacity
```

When the load factor becomes too high, resizing/rehashing may be required.

## Hashing Applications

- Frequency counting.
- Duplicate detection.
- Two Sum.
- Group anagrams.
- Caching.
- Memoization.
- Fast membership tests.

---

# Sets

A set stores unique elements.

Typical average complexity for hash-based sets:

```text
insert = O(1)
search = O(1)
delete = O(1)
```

Useful for:

- Duplicate detection.
- Visited nodes.
- Membership queries.
- Unique values.

---

# Recursion

Recursion occurs when a function calls itself.

Every recursive solution needs:

1. Base case.
2. Progress toward the base case.
3. Correct recursive relation.

Example:

```text
factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

## Recursion Stack

If recursion depth is `n`, auxiliary stack space may be `O(n)`.

## Recursion vs Iteration

Prefer iteration when:

- Recursion depth can become unsafe.
- The iterative solution is simpler.
- Stack memory matters.

Use recursion naturally for:

- Trees.
- DFS.
- Backtracking.
- Divide and conquer.

---

# Backtracking

Backtracking explores candidates and removes choices when they cannot lead to a valid solution.

General pattern:

```text
backtrack(state):
    if state is complete:
        record solution
        return

    for candidate in candidates:
        if candidate is invalid:
            continue

        choose(candidate)
        backtrack(updated state)
        undo(candidate)
```

Applications:

- Permutations.
- Combinations.
- Subsets.
- N-Queens.
- Sudoku.
- Word search.

Key optimization:

> Prune impossible branches as early as possible.

---

# Searching

## Linear Search

```text
for i from 0 to n-1:
    if a[i] == target:
        return i
return -1
```

Complexity:

- Time: `O(n)`
- Space: `O(1)`

## Binary Search

Requires a monotonic/searchable condition.

For a sorted array:

```text
left = 0
right = n - 1

while left <= right:
    mid = left + (right - left) // 2

    if a[mid] == target:
        return mid
    else if a[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

Complexity:

- Time: `O(log n)`
- Space: `O(1)` iterative.

## Lower Bound

Find the first index where:

```text
a[i] >= target
```

Template:

```text
left = 0
right = n

while left < right:
    mid = left + (right - left) // 2

    if a[mid] < target:
        left = mid + 1
    else:
        right = mid

return left
```

## Upper Bound

Find the first index where:

```text
a[i] > target
```

---

# Sorting

## Bubble Sort

Repeatedly swaps adjacent out-of-order elements.

- Best: `O(n)` with optimization.
- Average: `O(n²)`.
- Worst: `O(n²)`.
- Space: `O(1)`.

Useful mainly for educational purposes.

## Selection Sort

Repeatedly selects the minimum remaining element.

- Time: `O(n²)`.
- Space: `O(1)`.

## Insertion Sort

Builds a sorted prefix.

- Best: `O(n)`.
- Average: `O(n²)`.
- Worst: `O(n²)`.
- Space: `O(1)`.

Good for small or nearly sorted inputs.

## Merge Sort

Divide the array into halves, sort each half, then merge.

- Time: `O(n log n)`.
- Space: typically `O(n)` for arrays.
- Stable: yes in standard implementations.

## Quick Sort

Choose a pivot and partition.

Average:

```text
O(n log n)
```

Worst:

```text
O(n²)
```

With randomized/appropriate pivot selection, expected performance is generally `O(n log n)`.

## Heap Sort

Build a heap and repeatedly extract.

- Time: `O(n log n)`.
- Auxiliary space: `O(1)` for an in-place implementation.
- Stable: no.

## Counting Sort

Useful when the integer value range is reasonably small.

- Time: `O(n + k)`.
- Space: `O(k)`.

## Radix Sort

Processes digits/characters by position.

Typical complexity:

```text
O(d(n + k))
```

where:

- `d` = number of digits/passes.
- `k` = radix.

## Sorting Selection Guide

| Situation | Good Choice |
|---|---|
| General purpose | Library sort |
| Stable `O(n log n)` | Merge sort |
| Average fast in-place | Quick sort |
| Need heap structure | Heap sort / heap |
| Small integer range | Counting sort |
| Fixed-width integers | Radix sort |
| Nearly sorted small data | Insertion sort |

---

# Two Pointers

Two pointers maintain two positions while scanning a structure.

Common forms:

### Opposite ends

```text
left = 0
right = n - 1
```

Useful for:

- Pair sum in sorted array.
- Palindrome.
- Container problems.
- Partitioning.

### Same direction

Useful for:

- Removing duplicates.
- Merging sequences.
- Fast/slow scanning.

---

# Sliding Window

Sliding window processes contiguous ranges efficiently.

## Fixed Window

For window size `k`:

```text
initialize first window

for right from k to n-1:
    remove element at right-k
    add element at right
    update answer
```

Complexity often becomes:

```text
O(n)
```

## Variable Window

Typical template:

```text
left = 0

for right from 0 to n-1:
    add a[right]

    while window violates condition:
        remove a[left]
        left++

    update answer
```

Use for:

- Longest substring.
- Minimum window.
- At most `k` distinct elements.
- Maximum/minimum constrained subarrays.

---

# Prefix Sum and Difference Arrays

## Prefix Sum

Define:

```text
prefix[i] = sum of elements before/through i
```

Range sum can then be answered in `O(1)` after `O(n)` preprocessing.

For inclusive `[l, r]`:

```text
sum(l, r) = prefix[r + 1] - prefix[l]
```

## Difference Array

For range additions:

```text
diff[l] += value
diff[r + 1] -= value
```

Then recover final values using a prefix sum.

Useful for:

- Range updates.
- Scheduling.
- Interval increments.

---

# Fast and Slow Pointers

Use two pointers moving at different speeds.

Classic linked-list cycle detection:

```text
slow = head
fast = head

while fast != null and fast.next != null:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        cycle exists
```

Complexity:

- Time: `O(n)`
- Space: `O(1)`

Applications:

- Cycle detection.
- Cycle entry.
- Middle element.
- Certain sequence problems.

---

# Intervals

Common steps:

1. Sort intervals by start.
2. Maintain the current merged interval.
3. Merge if overlap exists.
4. Otherwise start a new interval.

Example condition:

```text
if next.start <= current.end:
    current.end = max(current.end, next.end)
else:
    output current
    current = next
```

Complexity:

```text
O(n log n)
```

because of sorting.

Applications:

- Merge intervals.
- Meeting rooms.
- Calendar conflicts.
- Interval insertion.

---

# Monotonic Stack

A monotonic stack maintains elements in increasing or decreasing order.

Used for:

- Next greater element.
- Next smaller element.
- Daily temperatures.
- Largest rectangle in histogram.
- Stock span.

## Next Greater Element

For each element, pop values that are smaller than the current value.

```text
stack = empty

for i from n-1 downto 0:
    while stack not empty and stack.top <= a[i]:
        pop

    answer[i] = stack.top if stack exists else -1
    push a[i]
```

Usually:

```text
Time = O(n)
Space = O(n)
```

Each element is pushed and popped at most once.

---

# Heap / Priority Queue

A heap supports efficient access to the minimum or maximum.

## Min Heap

Parent is no greater than its children.

## Max Heap

Parent is no smaller than its children.

Typical operations:

| Operation | Complexity |
|---|---:|
| Peek | O(1) |
| Insert | O(log n) |
| Extract | O(log n) |
| Build heap | O(n) |

## Applications

- Top K elements.
- Kth largest/smallest.
- Scheduling.
- Dijkstra.
- Merge K sorted lists.
- Median maintenance.

---

# Binary Trees

A binary tree has at most two children per node.

```text
Node:
    value
    left
    right
```

## DFS Traversals

### Preorder

```text
root -> left -> right
```

### Inorder

```text
left -> root -> right
```

### Postorder

```text
left -> right -> root
```

## BFS / Level Order

Use a queue:

```text
queue.push(root)

while queue not empty:
    node = queue.pop_front()
    process(node)

    if node.left:
        queue.push(node.left)

    if node.right:
        queue.push(node.right)
```

Complexity:

```text
Time = O(n)
Space = O(w)
```

where `w` is maximum width.

## Tree Height

For a recursive definition:

```text
height(null) = 0
height(node) = 1 + max(height(left), height(right))
```

---

# Binary Search Trees

BST property:

```text
left subtree < node < right subtree
```

depending on the duplicate policy.

Search:

- Average on balanced tree: `O(log n)`.
- Worst case: `O(n)`.

Insertion/deletion have the same asymptotic behavior.

## BST Deletion

Three cases:

1. Leaf node.
2. One child.
3. Two children.

For two children, replace with:

- Inorder successor, or
- Inorder predecessor.

---

# Balanced Trees

A balanced search tree keeps height near logarithmic.

Examples:

- AVL tree.
- Red-black tree.

Typical operations:

```text
search   O(log n)
insert   O(log n)
delete   O(log n)
```

Balancing is maintained using rotations and/or coloring rules.

---

# Tries

A trie stores strings character by character.

Useful for:

- Prefix search.
- Autocomplete.
- Dictionary matching.
- Word search.
- Routing/string dictionaries.

If `L` is word length:

```text
insert = O(L)
search = O(L)
prefix = O(L)
```

Space depends on the number of nodes and alphabet/representation.

---

# Graphs

A graph consists of:

```text
Vertices (V)
Edges (E)
```

Types:

- Directed.
- Undirected.
- Weighted.
- Unweighted.
- Cyclic.
- Acyclic.
- Connected.
- Disconnected.

## Adjacency List

Typical space:

```text
O(V + E)
```

Best for sparse graphs.

## Adjacency Matrix

Space:

```text
O(V²)
```

Useful when dense connectivity checks are frequent.

---

# Graph Traversal

## BFS

Use a queue.

```text
queue = [source]
visited[source] = true

while queue not empty:
    u = dequeue

    for v in neighbors(u):
        if not visited[v]:
            visited[v] = true
            enqueue(v)
```

Complexity with adjacency lists:

```text
O(V + E)
```

Applications:

- Shortest path in unweighted graph.
- Level traversal.
- Connected components.
- Bipartite checking.

## DFS

Use recursion or an explicit stack.

```text
dfs(u):
    visited[u] = true

    for v in neighbors(u):
        if not visited[v]:
            dfs(v)
```

Complexity:

```text
O(V + E)
```

Applications:

- Components.
- Cycle detection.
- Topological sorting.
- Backtracking.
- Bridges/articulation points.

---

# Shortest Path Algorithms

## BFS Shortest Path

For an unweighted graph:

```text
distance[source] = 0
```

Then BFS assigns the shortest number of edges.

Complexity:

```text
O(V + E)
```

## Dijkstra

For graphs with **non-negative edge weights**.

Core idea:

1. Maintain tentative distances.
2. Extract the vertex with smallest tentative distance.
3. Relax its outgoing edges.
4. Repeat.

With a binary heap:

```text
O((V + E) log V)
```

Do **not** use Dijkstra directly when negative edge weights can exist.

## Bellman-Ford

Supports negative edges and detects reachable negative cycles.

Relax every edge repeatedly:

```text
for i = 1 to V-1:
    for every edge (u, v, w):
        dist[v] = min(dist[v], dist[u] + w)
```

Complexity:

```text
O(VE)
```

## Floyd-Warshall

All-pairs shortest paths.

Recurrence:

```text
dist[i][j] =
    min(dist[i][j],
        dist[i][k] + dist[k][j])
```

Complexity:

```text
O(V³)
```

Space:

```text
O(V²)
```

---

# Minimum Spanning Tree

For a connected, weighted, undirected graph, an MST connects all vertices with minimum total edge weight.

## Kruskal

1. Sort edges by weight.
2. Add an edge if it does not create a cycle.
3. Use DSU to detect connectivity.

Complexity:

```text
O(E log E)
```

## Prim

Grow the MST from a starting vertex.

With a binary heap:

```text
O(E log V)
```

---

# Disjoint Set Union

Also called:

- Union-Find.

Supports:

- `find(x)`
- `union(a, b)`

Optimizations:

- Path compression.
- Union by rank.
- Union by size.

Amortized complexity:

```text
O(alpha(n))
```

per operation, where `alpha` grows extremely slowly.

Applications:

- Kruskal MST.
- Dynamic connectivity.
- Cycle detection in undirected graphs.
- Grouping components.

---

# Topological Sorting

A topological ordering exists for a directed acyclic graph (DAG).

## Kahn's Algorithm

1. Compute indegrees.
2. Add all zero-indegree vertices to a queue.
3. Remove one.
4. Decrease neighbor indegrees.
5. Add newly zero-indegree vertices.

If fewer than `V` vertices are processed, a cycle exists.

Complexity:

```text
O(V + E)
```

Applications:

- Course scheduling.
- Build systems.
- Dependency resolution.
- Task scheduling.

## DFS Topological Sort

Perform DFS and add a vertex after processing all descendants.

Use a three-state visitation scheme to detect cycles:

```text
0 = unvisited
1 = visiting
2 = processed
```

An edge to a `visiting` node indicates a cycle.

---

# Dynamic Programming

Dynamic Programming (DP) solves problems with:

1. Overlapping subproblems.
2. Optimal substructure.

## DP Process

### Step 1 — Define the state

Ask:

> What information uniquely describes a subproblem?

### Step 2 — Define the transition

Ask:

> How is the current state obtained from smaller states?

### Step 3 — Define base cases

Handle the smallest valid inputs.

### Step 4 — Determine evaluation order

Use:

- Top-down memoization.
- Bottom-up tabulation.

### Step 5 — Optimize memory

If a state depends only on the previous few states, reduce memory.

---

## Fibonacci

Naive recursion:

```text
F(n) = F(n-1) + F(n-2)
```

Time:

```text
O(2^n)
```

Memoized:

```text
O(n)
```

Space:

```text
O(n)
```

Bottom-up with two variables:

```text
prev2 = 0
prev1 = 1

for i from 2 to n:
    current = prev1 + prev2
    prev2 = prev1
    prev1 = current
```

Time:

```text
O(n)
```

Space:

```text
O(1)
```

---

# Major DP Patterns

## 1. 1D DP

Examples:

- Climbing stairs.
- House robber.
- Maximum subarray variants.

## 2. 2D/Grid DP

Examples:

- Unique paths.
- Minimum path sum.
- Grid obstacles.

## 3. Knapsack DP

Types:

- 0/1 knapsack.
- Unbounded knapsack.
- Bounded variants.

## 4. Subsequence DP

Examples:

- Longest common subsequence.
- Longest increasing subsequence.
- Edit distance.

## 5. Interval DP

Examples:

- Matrix chain multiplication.
- Burst balloons.
- Palindrome partitioning variants.

## 6. Tree DP

Compute values based on children.

## 7. State Machine DP

Examples:

- Stock buy/sell.
- Cooldown.
- Transaction limits.

## 8. Bitmask DP

Useful when `n` is small and subsets represent state.

---

# Greedy Algorithms

Greedy algorithms make the locally best choice while preserving global optimality.

Greedy is not automatically correct.

You need a proof, commonly through:

- Exchange argument.
- Cut property.
- Staying-ahead argument.
- Structural theorem.

Examples:

- Activity selection.
- Fractional knapsack.
- Huffman coding.
- Kruskal.
- Prim.
- Dijkstra's non-negative-weight relaxation strategy.

---

# Bit Manipulation

Know:

```text
AND  &
OR   |
XOR  ^
NOT  ~
LEFT SHIFT  <<
RIGHT SHIFT >>
```

## Important Properties

```text
x ^ x = 0
x ^ 0 = x
```

XOR is useful for finding a unique element when every other element appears exactly twice.

## Check Odd/Even

```text
n & 1
```

If non-zero, `n` is odd.

## Check Power of Two

For positive `n`:

```text
n & (n - 1) == 0
```

## Remove Lowest Set Bit

```text
n = n & (n - 1)
```

This reduces the number of set bits by one.

## Count Set Bits

Repeatedly apply:

```text
n &= n - 1
```

Complexity:

```text
O(number of set bits)
```

---

# Advanced String Algorithms

## KMP

Knuth-Morris-Pratt finds a pattern in a text using a prefix-function/LPS array.

Complexity:

```text
O(n + m)
```

where:

- `n` = text length.
- `m` = pattern length.

## Z Algorithm

Computes the Z-array:

```text
Z[i] = length of longest substring starting at i
       that matches the prefix
```

Pattern matching can be done in:

```text
O(n + m)
```

## Rolling Hash

Represent strings using polynomial hashing.

Useful for:

- Substring comparison.
- Duplicate substring detection.
- Rabin-Karp style matching.

Use sufficiently strong hashing and collision-aware design.

---

# Advanced Data Structures

## Fenwick Tree / Binary Indexed Tree

Supports:

- Point update.
- Prefix sum query.

Typical complexity:

```text
update = O(log n)
query  = O(log n)
```

Space:

```text
O(n)
```

## Segment Tree

Supports range queries and updates.

Typical:

```text
build  = O(n)
query  = O(log n)
update = O(log n)
```

Depending on the operation and implementation.

With lazy propagation, range updates and range queries can often be supported in:

```text
O(log n)
```

## Sparse Table

Excellent for static idempotent range queries such as:

- Range minimum.
- Range maximum.
- GCD.

Preprocessing:

```text
O(n log n)
```

Query can be:

```text
O(1)
```

for appropriate idempotent operations.

---

# Range Query Algorithms

Choose the structure based on whether the data changes.

| Requirement | Technique |
|---|---|
| Static range sum | Prefix sum |
| Static RMQ | Sparse table |
| Point update + range sum | Fenwick tree |
| Range query + point update | Segment tree |
| Range update | Difference array / lazy segment tree |
| Dynamic connectivity | DSU |

---

# Divide and Conquer

General pattern:

```text
solve(problem):
    if small:
        return direct answer

    divide problem into smaller parts
    solve each part
    combine answers
```

Examples:

- Merge sort.
- Quick sort.
- Binary search.
- Closest pair of points.
- Divide-and-conquer counting.

---

# Amortized Analysis

An operation may be expensive occasionally but cheap on average across a sequence.

Example:

Dynamic array resizing:

- Most appends: `O(1)`.
- Occasional resize: `O(n)`.
- Amortized append: `O(1)`.

Important:

> Amortized complexity is not the same as average-case complexity.

---

# Problem-Solving Framework

Use this framework in interviews and real projects.

## Step 1 — Read Constraints

Constraints often reveal the intended algorithm.

Typical clues:

| Constraint | Possible Direction |
|---|---|
| `n <= 20` | Backtracking / bitmask / exponential may work |
| `n <= 10²` | O(n²) often acceptable |
| `n <= 10³` | O(n²) may be acceptable |
| `n <= 10⁵` | Usually O(n log n) or O(n) |
| `n <= 10⁶` | Prefer O(n), careful constants |
| Huge values | Hashing, logarithmic algorithms, math |

These are guidelines, not universal rules.

## Step 2 — Identify Input Structure

Ask:

- Sorted?
- Nearly sorted?
- Unique?
- Duplicate?
- Positive only?
- Negative allowed?
- Contiguous range?
- Tree?
- Graph?
- Weighted graph?
- Directed graph?

## Step 3 — Start With Brute Force

Know the simplest correct solution first.

Then ask:

> Which repeated work can be removed?

## Step 4 — Choose the Pattern

Look for:

- Hash map.
- Sorting.
- Two pointers.
- Sliding window.
- Prefix sum.
- Binary search.
- Stack.
- Heap.
- DFS/BFS.
- Greedy.
- DP.

## Step 5 — State the Invariant

An invariant is something that remains true during the algorithm.

Examples:

- Sliding window satisfies a constraint.
- Heap maintains priority ordering.
- BFS queue processes nodes by distance.
- Monotonic stack maintains monotonicity.

## Step 6 — Prove Correctness

Explain why:

- Every required case is considered.
- Invalid cases are excluded.
- The chosen answer is optimal if optimization is required.

## Step 7 — Complexity

Always state:

```text
Time: O(...)
Space: O(...)
```

---

# Common DSA Patterns

## Pattern 1 — Frequency Map

Use when:

- Counting occurrences.
- Comparing character frequencies.
- Finding duplicates.
- Matching values.

## Pattern 2 — Hash Set

Use when:

- Membership matters.
- You need uniqueness.
- You need fast duplicate detection.

## Pattern 3 — Sort + Two Pointers

Use when:

- Pair/triple relationships matter.
- Ordering helps eliminate combinations.

## Pattern 4 — Sliding Window

Use when:

- The problem concerns a contiguous subarray/substring.
- The window can be expanded/shrunk.

## Pattern 5 — Prefix Sum

Use when:

- Many range sums are requested.
- Range updates can be transformed into difference updates.

## Pattern 6 — Binary Search on Answer

Instead of searching the input directly, search a numerical answer space.

Template:

```text
low = minimum possible answer
high = maximum possible answer

while low < high:
    mid = low + (high - low) // 2

    if feasible(mid):
        high = mid
    else:
        low = mid + 1

return low
```

The key requirement is a monotonic feasibility condition.

## Pattern 7 — Monotonic Stack

Use for nearest greater/smaller relationships.

## Pattern 8 — Heap

Use when you repeatedly need:

- Minimum.
- Maximum.
- Top K.
- Next best candidate.

## Pattern 9 — BFS

Use for:

- Unweighted shortest path.
- Level-by-level traversal.
- Minimum number of moves.

## Pattern 10 — DFS

Use for:

- Exploring connected structures.
- Components.
- Cycle detection.
- Tree problems.

## Pattern 11 — Backtracking

Use for:

- Enumerating valid possibilities.
- Constraint satisfaction.

## Pattern 12 — DP

Use when:

- The same subproblems repeat.
- An optimal answer can be composed from smaller optimal answers.

## Pattern 13 — Greedy

Use only when a correctness argument exists.

---

# Important Interview Problems

## Arrays

- Two Sum.
- Best Time to Buy and Sell Stock.
- Maximum Subarray.
- Product of Array Except Self.
- Maximum Product Subarray.
- Merge Sorted Arrays.
- Rotate Array.
- Move Zeroes.
- Find Duplicate Number.
- First Missing Positive.
- Longest Consecutive Sequence.

## Strings

- Valid Anagram.
- Valid Palindrome.
- Longest Substring Without Repeating Characters.
- Longest Palindromic Substring.
- Group Anagrams.
- Minimum Window Substring.
- Valid Parentheses.
- String Compression.
- Implement substring search.

## Linked Lists

- Reverse Linked List.
- Merge Two Sorted Lists.
- Linked List Cycle.
- Cycle II.
- Remove Nth Node From End.
- Reorder List.
- Copy List With Random Pointer.
- Merge K Sorted Lists.

## Stack / Queue

- Min Stack.
- Daily Temperatures.
- Next Greater Element.
- Largest Rectangle in Histogram.
- Sliding Window Maximum.
- Evaluate Reverse Polish Notation.

## Trees

- Maximum Depth.
- Same Tree.
- Invert Binary Tree.
- Diameter.
- Balanced Binary Tree.
- Level Order Traversal.
- Lowest Common Ancestor.
- Validate BST.
- Kth Smallest in BST.
- Serialize/Deserialize Binary Tree.

## Graphs

- Number of Islands.
- Clone Graph.
- Course Schedule.
- Pacific Atlantic Water Flow.
- Rotting Oranges.
- Word Ladder.
- Graph Valid Tree.
- Number of Connected Components.
- Shortest Path Problems.
- Network Delay Time.

## DP

- Climbing Stairs.
- House Robber.
- Coin Change.
- Longest Increasing Subsequence.
- Longest Common Subsequence.
- Edit Distance.
- Unique Paths.
- Partition Equal Subset Sum.
- 0/1 Knapsack.
- Word Break.
- Decode Ways.
- Stock DP variants.

---

# Complexity Cheat Sheet

| Structure / Algorithm | Average / Typical Time | Space |
|---|---:|---:|
| Array access | O(1) | O(1) |
| Array search | O(n) | O(1) |
| Hash lookup | O(1) avg | O(n) |
| Linked-list search | O(n) | O(1) |
| Stack push/pop | O(1) | O(n) |
| Queue enqueue/dequeue | O(1) | O(n) |
| Heap insert | O(log n) | O(n) |
| Heap extract | O(log n) | O(n) |
| BST balanced search | O(log n) | O(n) |
| BST worst search | O(n) | O(n) |
| Trie operation | O(L) | O(total chars) |
| BFS | O(V + E) | O(V) |
| DFS | O(V + E) | O(V) |
| Binary search | O(log n) | O(1) |
| Merge sort | O(n log n) | O(n) |
| Quick sort expected | O(n log n) | O(log n) typical recursion |
| Heap sort | O(n log n) | O(1) auxiliary |
| Counting sort | O(n + k) | O(k) |
| Dijkstra + binary heap | O((V + E) log V) | O(V + E) |
| Bellman-Ford | O(VE) | O(V) |
| Floyd-Warshall | O(V³) | O(V²) |
| Kruskal | O(E log E) | O(V + E) |
| Prim + heap | O(E log V) | O(V + E) |
| DSU operation | O(alpha(n)) amortized | O(n) |
| Fenwick update/query | O(log n) | O(n) |
| Segment tree query/update | O(log n) | O(n) |

---

# Common Mistakes

## 1. Off-by-One Errors

Be precise about:

```text
[0, n)
```

versus:

```text
[0, n-1]
```

## 2. Integer Overflow

Use a sufficiently wide integer type when:

```text
a + b
a * b
mid calculations
prefix sums
```

For binary search, prefer:

```text
mid = left + (right - left) / 2
```

## 3. Incorrect Binary Search

Always define:

- Search interval.
- Predicate.
- Meaning of `left`.
- Meaning of `right`.
- Termination condition.

## 4. Forgetting Empty Input

Test:

```text
[]
""
null
```

where applicable.

## 5. Ignoring Duplicates

Explicitly decide whether duplicates are:

- Allowed.
- Ignored.
- Counted.
- Rejected.

## 6. Incorrect Graph Visitation

Mark nodes at the appropriate time to prevent:

- Infinite loops.
- Duplicate processing.
- Incorrect shortest paths.

## 7. Using Dijkstra With Negative Edges

Dijkstra requires non-negative edge weights.

## 8. Assuming Greedy Is Correct

A locally optimal choice needs a proof.

## 9. Excessive Recursion

Deep recursion may overflow the call stack.

## 10. Premature Optimization

First establish:

```text
correctness
```

then optimize:

```text
time
space
constants
```

---

# Interview Checklist

Before submitting a solution:

- [ ] Did I understand the problem?
- [ ] Did I identify constraints?
- [ ] Did I define edge cases?
- [ ] Did I establish a correct baseline?
- [ ] Did I choose an appropriate data structure?
- [ ] Did I consider time complexity?
- [ ] Did I consider space complexity?
- [ ] Did I avoid unnecessary repeated work?
- [ ] Did I handle duplicates?
- [ ] Did I handle empty input?
- [ ] Did I handle one-element input?
- [ ] Did I check integer overflow?
- [ ] Did I test minimum values?
- [ ] Did I test maximum values?
- [ ] Did I explain correctness?
- [ ] Did I explain the invariant?
- [ ] Did I state final complexity?

---

# 8-Week Preparation Plan

## Week 1 — Foundations

### Topics

- Big-O.
- Arrays.
- Strings.
- Basic math.
- Hash maps.
- Hash sets.

### Target

- 20–30 problems.
- Implement basic structures.
- Learn complexity analysis.

---

## Week 2 — Linked Lists and Stack/Queue

### Topics

- Singly linked list.
- Doubly linked list.
- Stack.
- Queue.
- Deque.
- Fast/slow pointers.

### Target

- 20–30 problems.
- Implement each structure from scratch.

---

## Week 3 — Searching and Sorting

### Topics

- Binary search.
- Lower bound.
- Upper bound.
- Merge sort.
- Quick sort.
- Heap basics.
- Two pointers.
- Sliding window.

### Target

- 25–35 problems.

---

## Week 4 — Trees

### Topics

- Binary trees.
- DFS.
- BFS.
- BST.
- Tree recursion.
- LCA.
- Tree serialization.

### Target

- 25–35 problems.

---

## Week 5 — Graphs

### Topics

- Graph representation.
- BFS.
- DFS.
- Cycle detection.
- Components.
- Bipartite graphs.
- Topological sorting.
- DSU.

### Target

- 25–35 problems.

---

## Week 6 — Shortest Paths and MST

### Topics

- Dijkstra.
- Bellman-Ford.
- Floyd-Warshall.
- Kruskal.
- Prim.
- Union-Find.

### Target

- 20–30 problems.
- Implement each major algorithm without copying.

---

## Week 7 — Dynamic Programming and Greedy

### Topics

- 1D DP.
- 2D DP.
- Knapsack.
- Subsequence DP.
- Interval DP.
- Tree DP.
- Greedy proofs.

### Target

- 30–40 problems.

---

## Week 8 — Advanced Topics + Mock Interviews

### Topics

- Trie.
- Fenwick tree.
- Segment tree.
- KMP.
- Bit manipulation.
- Advanced graph problems.
- Mixed problem solving.

### Target

- 5–10 timed mock interviews.
- Re-solve previously failed problems.
- Practice explaining solutions aloud.

---

# Daily DSA Routine

Recommended daily session:

```text
30 min  -> Learn/revise concept
30 min  -> Implement from scratch
60 min  -> Solve 2–4 problems
20 min  -> Review failed solutions
10 min  -> Write complexity + key lesson
```

For difficult topics, reduce the number of problems and increase implementation/proof practice.

---

# How to Review a Failed Problem

Never simply read the solution and move on.

Use this process:

1. Identify why the first approach failed.
2. Write the brute-force solution.
3. Identify the bottleneck.
4. Identify the pattern.
5. Understand the optimized invariant.
6. Close the solution.
7. Re-implement it yourself.
8. Test it.
9. Re-solve the same problem after 24–72 hours.
10. Re-solve again after one or two weeks.

---

# DSA Master Pattern Recognition

When you see...

### "Find pair"

Think:

```text
Hash map
Two pointers
Sorting
```

### "Longest/shortest contiguous subarray"

Think:

```text
Sliding window
Prefix sum
Hash map
Deque
```

### "Next greater/smaller"

Think:

```text
Monotonic stack
```

### "Top K"

Think:

```text
Heap
Quickselect
Counting/frequency
```

### "Shortest path, unweighted"

Think:

```text
BFS
```

### "Shortest path, non-negative weights"

Think:

```text
Dijkstra
```

### "Negative edge weights"

Think:

```text
Bellman-Ford
```

### "All-pairs shortest path"

Think:

```text
Floyd-Warshall
```

### "Connect all vertices with minimum cost"

Think:

```text
MST
Kruskal
Prim
```

### "Dependencies"

Think:

```text
Topological sort
```

### "Repeated subproblems"

Think:

```text
DP
Memoization
Tabulation
```

### "All possible combinations"

Think:

```text
Backtracking
```

### "Prefix matching"

Think:

```text
Trie
```

### "Dynamic connectivity"

Think:

```text
DSU
```

### "Range queries"

Think:

```text
Prefix sum
Fenwick tree
Segment tree
Sparse table
```

---

# Production-Level DSA Principles

A professional solution is not only about passing test cases.

Consider:

## Correctness

The algorithm must satisfy the full specification.

## Complexity

Choose an algorithm appropriate for expected input size.

## Memory

Avoid unnecessary copies and allocations.

## Overflow

Use safe numeric types and safe arithmetic.

## Input Validation

Handle invalid or unexpected input according to the application's contract.

## Determinism

When output ordering matters, make ordering explicit.

## Maintainability

Prefer clear names, well-defined invariants, and simple control flow.

## Testing

Include:

- Normal cases.
- Boundary cases.
- Empty cases.
- Duplicate cases.
- Large cases.
- Adversarial cases.

## Security

For production software, consider:

- Untrusted input.
- Hash-flooding risks where relevant.
- Resource exhaustion.
- Recursion depth.
- Memory limits.
- Integer overflow.

---

# DSA Implementation Requirements

For serious preparation, implement these from scratch:

## Data Structures

- [ ] Dynamic array.
- [ ] Singly linked list.
- [ ] Doubly linked list.
- [ ] Stack.
- [ ] Queue.
- [ ] Deque.
- [ ] Hash table.
- [ ] Min heap.
- [ ] Max heap.
- [ ] Binary tree.
- [ ] BST.
- [ ] Trie.
- [ ] Graph adjacency list.
- [ ] DSU.
- [ ] Fenwick tree.
- [ ] Segment tree.

## Algorithms

- [ ] Linear search.
- [ ] Binary search.
- [ ] Lower bound.
- [ ] Upper bound.
- [ ] Bubble sort.
- [ ] Selection sort.
- [ ] Insertion sort.
- [ ] Merge sort.
- [ ] Quick sort.
- [ ] Heap sort.
- [ ] Counting sort.
- [ ] BFS.
- [ ] DFS.
- [ ] Topological sort.
- [ ] Dijkstra.
- [ ] Bellman-Ford.
- [ ] Floyd-Warshall.
- [ ] Kruskal.
- [ ] Prim.
- [ ] KMP.
- [ ] Z algorithm.
- [ ] Backtracking.
- [ ] Core DP patterns.

---

# Recommended Problem-Solving Order

Follow this progression:

```text
Complexity
    ↓
Arrays
    ↓
Strings
    ↓
Hashing
    ↓
Linked Lists
    ↓
Stack / Queue
    ↓
Two Pointers
    ↓
Sliding Window
    ↓
Binary Search
    ↓
Sorting
    ↓
Heap
    ↓
Trees
    ↓
BST
    ↓
Graphs
    ↓
BFS / DFS
    ↓
Topological Sort
    ↓
DSU
    ↓
Shortest Paths
    ↓
MST
    ↓
Greedy
    ↓
Backtracking
    ↓
Dynamic Programming
    ↓
Trie
    ↓
Fenwick / Segment Tree
    ↓
Advanced Strings
    ↓
Advanced Graphs
```

---

# Final Master Checklist

## Fundamentals

- [ ] Big-O.
- [ ] Big-Theta concept.
- [ ] Big-Omega concept.
- [ ] Time-space tradeoffs.
- [ ] Amortized analysis.
- [ ] Recursion complexity.

## Arrays / Strings

- [ ] Traversal.
- [ ] Two pointers.
- [ ] Sliding window.
- [ ] Prefix sums.
- [ ] Difference arrays.
- [ ] Frequency maps.
- [ ] Binary search.
- [ ] Sorting.

## Linear Data Structures

- [ ] Linked list.
- [ ] Stack.
- [ ] Queue.
- [ ] Deque.
- [ ] Monotonic stack.

## Trees

- [ ] Preorder.
- [ ] Inorder.
- [ ] Postorder.
- [ ] Level order.
- [ ] BST.
- [ ] LCA.
- [ ] Tree DP.
- [ ] Serialization.

## Graphs

- [ ] BFS.
- [ ] DFS.
- [ ] Cycle detection.
- [ ] Components.
- [ ] Bipartite.
- [ ] Topological sort.
- [ ] Dijkstra.
- [ ] Bellman-Ford.
- [ ] Floyd-Warshall.
- [ ] Kruskal.
- [ ] Prim.
- [ ] DSU.

## Advanced

- [ ] Trie.
- [ ] Fenwick tree.
- [ ] Segment tree.
- [ ] Sparse table.
- [ ] KMP.
- [ ] Z algorithm.
- [ ] Bit manipulation.
- [ ] Bitmask DP.

## Interview Skills

- [ ] Clarify requirements.
- [ ] Read constraints.
- [ ] Give brute force.
- [ ] Optimize systematically.
- [ ] Explain invariant.
- [ ] Prove correctness.
- [ ] Analyze complexity.
- [ ] Test edge cases.
- [ ] Communicate clearly.
- [ ] Write clean code.

---

# Final Goal

You are DSA-ready when you can look at a new problem and quickly determine:

```text
1. What is the input structure?
2. What are the constraints?
3. What is the brute-force solution?
4. What repeated work can be eliminated?
5. Which DSA pattern fits?
6. What invariant makes the solution correct?
7. What data structure provides the required operations?
8. What is the time complexity?
9. What is the space complexity?
10. What edge cases can break the solution?
```

The objective is **not to memorize solutions**.

The objective is to build the ability to:

> **Recognize → Model → Choose Data Structure → Design Algorithm → Prove → Implement → Test → Optimize → Explain.**

---

## Completion Standard

A strong DSA preparation cycle should include:

- Fundamental concepts.
- From-scratch implementations.
- Pattern recognition.
- Timed problem solving.
- Complexity analysis.
- Correctness reasoning.
- Edge-case testing.
- Repeated review.
- Mock interviews.
- Re-solving previously failed problems.

Once these skills are consistent, move from isolated topic practice to **mixed unseen problems**, because real interviews rarely tell you which algorithmic pattern to use.
