"""NeetCode 150 problem dataset.

Each entry: (name, slug, topic)
The LeetCode URL is derived from the slug: https://leetcode.com/problems/<slug>/
Keeping this as plain data (no executable content) keeps the dataset auditable.
"""

# (name, slug, topic)
NEETCODE_150 = [
    # Arrays & Hashing
    ("Contains Duplicate", "contains-duplicate", "Arrays & Hashing"),
    ("Valid Anagram", "valid-anagram", "Arrays & Hashing"),
    ("Two Sum", "two-sum", "Arrays & Hashing"),
    ("Group Anagrams", "group-anagrams", "Arrays & Hashing"),
    ("Top K Frequent Elements", "top-k-frequent-elements", "Arrays & Hashing"),
    ("Product of Array Except Self", "product-of-array-except-self", "Arrays & Hashing"),
    ("Valid Sudoku", "valid-sudoku", "Arrays & Hashing"),
    ("Encode and Decode Strings", "encode-and-decode-strings", "Arrays & Hashing"),
    ("Longest Consecutive Sequence", "longest-consecutive-sequence", "Arrays & Hashing"),

    # Two Pointers
    ("Valid Palindrome", "valid-palindrome", "Two Pointers"),
    ("Two Sum II", "two-sum-ii-input-array-is-sorted", "Two Pointers"),
    ("3Sum", "3sum", "Two Pointers"),
    ("Container With Most Water", "container-with-most-water", "Two Pointers"),
    ("Trapping Rain Water", "trapping-rain-water", "Two Pointers"),

    # Sliding Window
    ("Best Time to Buy and Sell Stock", "best-time-to-buy-and-sell-stock", "Sliding Window"),
    ("Longest Substring Without Repeating Characters", "longest-substring-without-repeating-characters", "Sliding Window"),
    ("Longest Repeating Character Replacement", "longest-repeating-character-replacement", "Sliding Window"),
    ("Permutation in String", "permutation-in-string", "Sliding Window"),
    ("Minimum Window Substring", "minimum-window-substring", "Sliding Window"),
    ("Sliding Window Maximum", "sliding-window-maximum", "Sliding Window"),

    # Stack
    ("Valid Parentheses", "valid-parentheses", "Stack"),
    ("Min Stack", "min-stack", "Stack"),
    ("Evaluate Reverse Polish Notation", "evaluate-reverse-polish-notation", "Stack"),
    ("Generate Parentheses", "generate-parentheses", "Stack"),
    ("Daily Temperatures", "daily-temperatures", "Stack"),
    ("Car Fleet", "car-fleet", "Stack"),
    ("Largest Rectangle in Histogram", "largest-rectangle-in-histogram", "Stack"),

    # Binary Search
    ("Binary Search", "binary-search", "Binary Search"),
    ("Search a 2D Matrix", "search-a-2d-matrix", "Binary Search"),
    ("Koko Eating Bananas", "koko-eating-bananas", "Binary Search"),
    ("Find Minimum in Rotated Sorted Array", "find-minimum-in-rotated-sorted-array", "Binary Search"),
    ("Search in Rotated Sorted Array", "search-in-rotated-sorted-array", "Binary Search"),
    ("Time Based Key-Value Store", "time-based-key-value-store", "Binary Search"),
    ("Median of Two Sorted Arrays", "median-of-two-sorted-arrays", "Binary Search"),

    # Linked List
    ("Reverse Linked List", "reverse-linked-list", "Linked List"),
    ("Merge Two Sorted Lists", "merge-two-sorted-lists", "Linked List"),
    ("Reorder List", "reorder-list", "Linked List"),
    ("Remove Nth Node From End of List", "remove-nth-node-from-end-of-list", "Linked List"),
    ("Copy List with Random Pointer", "copy-list-with-random-pointer", "Linked List"),
    ("Add Two Numbers", "add-two-numbers", "Linked List"),
    ("Linked List Cycle", "linked-list-cycle", "Linked List"),
    ("Find the Duplicate Number", "find-the-duplicate-number", "Linked List"),
    ("LRU Cache", "lru-cache", "Linked List"),
    ("Merge k Sorted Lists", "merge-k-sorted-lists", "Linked List"),
    ("Reverse Nodes in k-Group", "reverse-nodes-in-k-group", "Linked List"),

    # Trees
    ("Invert Binary Tree", "invert-binary-tree", "Trees"),
    ("Maximum Depth of Binary Tree", "maximum-depth-of-binary-tree", "Trees"),
    ("Diameter of Binary Tree", "diameter-of-binary-tree", "Trees"),
    ("Balanced Binary Tree", "balanced-binary-tree", "Trees"),
    ("Same Tree", "same-tree", "Trees"),
    ("Subtree of Another Tree", "subtree-of-another-tree", "Trees"),
    ("Lowest Common Ancestor of a Binary Search Tree", "lowest-common-ancestor-of-a-binary-search-tree", "Trees"),
    ("Binary Tree Level Order Traversal", "binary-tree-level-order-traversal", "Trees"),
    ("Binary Tree Right Side View", "binary-tree-right-side-view", "Trees"),
    ("Count Good Nodes in Binary Tree", "count-good-nodes-in-binary-tree", "Trees"),
    ("Validate Binary Search Tree", "validate-binary-search-tree", "Trees"),
    ("Kth Smallest Element in a BST", "kth-smallest-element-in-a-bst", "Trees"),
    ("Construct Binary Tree from Preorder and Inorder Traversal", "construct-binary-tree-from-preorder-and-inorder-traversal", "Trees"),
    ("Binary Tree Maximum Path Sum", "binary-tree-maximum-path-sum", "Trees"),
    ("Serialize and Deserialize Binary Tree", "serialize-and-deserialize-binary-tree", "Trees"),

    # Tries
    ("Implement Trie (Prefix Tree)", "implement-trie-prefix-tree", "Tries"),
    ("Design Add and Search Words Data Structure", "design-add-and-search-words-data-structure", "Tries"),
    ("Word Search II", "word-search-ii", "Tries"),

    # Heap / Priority Queue
    ("Kth Largest Element in a Stream", "kth-largest-element-in-a-stream", "Heap / Priority Queue"),
    ("Last Stone Weight", "last-stone-weight", "Heap / Priority Queue"),
    ("K Closest Points to Origin", "k-closest-points-to-origin", "Heap / Priority Queue"),
    ("Kth Largest Element in an Array", "kth-largest-element-in-an-array", "Heap / Priority Queue"),
    ("Task Scheduler", "task-scheduler", "Heap / Priority Queue"),
    ("Design Twitter", "design-twitter", "Heap / Priority Queue"),
    ("Find Median from Data Stream", "find-median-from-data-stream", "Heap / Priority Queue"),

    # Backtracking
    ("Subsets", "subsets", "Backtracking"),
    ("Combination Sum", "combination-sum", "Backtracking"),
    ("Permutations", "permutations", "Backtracking"),
    ("Subsets II", "subsets-ii", "Backtracking"),
    ("Combination Sum II", "combination-sum-ii", "Backtracking"),
    ("Word Search", "word-search", "Backtracking"),
    ("Palindrome Partitioning", "palindrome-partitioning", "Backtracking"),
    ("Letter Combinations of a Phone Number", "letter-combinations-of-a-phone-number", "Backtracking"),
    ("N-Queens", "n-queens", "Backtracking"),

    # Graphs
    ("Number of Islands", "number-of-islands", "Graphs"),
    ("Clone Graph", "clone-graph", "Graphs"),
    ("Max Area of Island", "max-area-of-island", "Graphs"),
    ("Pacific Atlantic Water Flow", "pacific-atlantic-water-flow", "Graphs"),
    ("Surrounded Regions", "surrounded-regions", "Graphs"),
    ("Rotting Oranges", "rotting-oranges", "Graphs"),
    ("Walls and Gates", "walls-and-gates", "Graphs"),
    ("Course Schedule", "course-schedule", "Graphs"),
    ("Course Schedule II", "course-schedule-ii", "Graphs"),
    ("Redundant Connection", "redundant-connection", "Graphs"),
    ("Number of Connected Components in an Undirected Graph", "number-of-connected-components-in-an-undirected-graph", "Graphs"),
    ("Graph Valid Tree", "graph-valid-tree", "Graphs"),
    ("Word Ladder", "word-ladder", "Graphs"),

    # Advanced Graphs
    ("Reconstruct Itinerary", "reconstruct-itinerary", "Advanced Graphs"),
    ("Min Cost to Connect All Points", "min-cost-to-connect-all-points", "Advanced Graphs"),
    ("Network Delay Time", "network-delay-time", "Advanced Graphs"),
    ("Swim in Rising Water", "swim-in-rising-water", "Advanced Graphs"),
    ("Alien Dictionary", "alien-dictionary", "Advanced Graphs"),
    ("Cheapest Flights Within K Stops", "cheapest-flights-within-k-stops", "Advanced Graphs"),

    # 1-D Dynamic Programming
    ("Climbing Stairs", "climbing-stairs", "1-D Dynamic Programming"),
    ("Min Cost Climbing Stairs", "min-cost-climbing-stairs", "1-D Dynamic Programming"),
    ("House Robber", "house-robber", "1-D Dynamic Programming"),
    ("House Robber II", "house-robber-ii", "1-D Dynamic Programming"),
    ("Longest Palindromic Substring", "longest-palindromic-substring", "1-D Dynamic Programming"),
    ("Palindromic Substrings", "palindromic-substrings", "1-D Dynamic Programming"),
    ("Decode Ways", "decode-ways", "1-D Dynamic Programming"),
    ("Coin Change", "coin-change", "1-D Dynamic Programming"),
    ("Maximum Product Subarray", "maximum-product-subarray", "1-D Dynamic Programming"),
    ("Word Break", "word-break", "1-D Dynamic Programming"),
    ("Longest Increasing Subsequence", "longest-increasing-subsequence", "1-D Dynamic Programming"),
    ("Partition Equal Subset Sum", "partition-equal-subset-sum", "1-D Dynamic Programming"),

    # 2-D Dynamic Programming
    ("Unique Paths", "unique-paths", "2-D Dynamic Programming"),
    ("Longest Common Subsequence", "longest-common-subsequence", "2-D Dynamic Programming"),
    ("Best Time to Buy and Sell Stock with Cooldown", "best-time-to-buy-and-sell-stock-with-cooldown", "2-D Dynamic Programming"),
    ("Coin Change II", "coin-change-ii", "2-D Dynamic Programming"),
    ("Target Sum", "target-sum", "2-D Dynamic Programming"),
    ("Interleaving String", "interleaving-string", "2-D Dynamic Programming"),
    ("Longest Increasing Path in a Matrix", "longest-increasing-path-in-a-matrix", "2-D Dynamic Programming"),
    ("Distinct Subsequences", "distinct-subsequences", "2-D Dynamic Programming"),
    ("Edit Distance", "edit-distance", "2-D Dynamic Programming"),
    ("Burst Balloons", "burst-balloons", "2-D Dynamic Programming"),
    ("Regular Expression Matching", "regular-expression-matching", "2-D Dynamic Programming"),

    # Greedy
    ("Maximum Subarray", "maximum-subarray", "Greedy"),
    ("Jump Game", "jump-game", "Greedy"),
    ("Jump Game II", "jump-game-ii", "Greedy"),
    ("Gas Station", "gas-station", "Greedy"),
    ("Hand of Straights", "hand-of-straights", "Greedy"),
    ("Merge Triplets to Form Target Triplet", "merge-triplets-to-form-target-triplet", "Greedy"),
    ("Partition Labels", "partition-labels", "Greedy"),
    ("Valid Parenthesis String", "valid-parenthesis-string", "Greedy"),

    # Intervals
    ("Insert Interval", "insert-interval", "Intervals"),
    ("Merge Intervals", "merge-intervals", "Intervals"),
    ("Non-overlapping Intervals", "non-overlapping-intervals", "Intervals"),
    ("Meeting Rooms", "meeting-rooms", "Intervals"),
    ("Meeting Rooms II", "meeting-rooms-ii", "Intervals"),
    ("Minimum Interval to Include Each Query", "minimum-interval-to-include-each-query", "Intervals"),

    # Math & Geometry
    ("Rotate Image", "rotate-image", "Math & Geometry"),
    ("Spiral Matrix", "spiral-matrix", "Math & Geometry"),
    ("Set Matrix Zeroes", "set-matrix-zeroes", "Math & Geometry"),
    ("Happy Number", "happy-number", "Math & Geometry"),
    ("Plus One", "plus-one", "Math & Geometry"),
    ("Pow(x, n)", "powx-n", "Math & Geometry"),
    ("Multiply Strings", "multiply-strings", "Math & Geometry"),
    ("Detect Squares", "detect-squares", "Math & Geometry"),

    # Bit Manipulation
    ("Single Number", "single-number", "Bit Manipulation"),
    ("Number of 1 Bits", "number-of-1-bits", "Bit Manipulation"),
    ("Counting Bits", "counting-bits", "Bit Manipulation"),
    ("Reverse Bits", "reverse-bits", "Bit Manipulation"),
    ("Missing Number", "missing-number", "Bit Manipulation"),
    ("Sum of Two Integers", "sum-of-two-integers", "Bit Manipulation"),
    ("Reverse Integer", "reverse-integer", "Bit Manipulation"),
]


def url_for(slug):
    """Build the canonical LeetCode URL for a problem slug."""
    return "https://leetcode.com/problems/{}/".format(slug)


# slug -> one-line optimal-approach gist (technique + complexity). Shown only
# AFTER you mark a problem done, as a post-solve learning beat.
GISTS = {
    # Arrays & Hashing
    "contains-duplicate": "Hash set; return true on the first repeat. O(n) / O(n).",
    "valid-anagram": "Compare character counts (count array / Counter). O(n) / O(1).",
    "two-sum": "Hash map value->index; look up the complement. O(n) / O(n).",
    "group-anagrams": "Bucket words by sorted chars (or 26-count tuple) in a map. O(n*k) / O(n*k).",
    "top-k-frequent-elements": "Count freqs, then bucket-sort by frequency. O(n) / O(n).",
    "product-of-array-except-self": "Prefix products from the left, suffix products from the right. O(n) / O(1) extra.",
    "valid-sudoku": "One pass with row/col/box hash sets of seen digits. O(1) / O(1) (fixed 9x9).",
    "encode-and-decode-strings": "Length-prefix each string ('len#str') so decode is unambiguous. O(n) / O(n).",
    "longest-consecutive-sequence": "Put all in a set; count runs only from sequence heads (n-1 absent). O(n) / O(n).",

    # Two Pointers
    "valid-palindrome": "Two pointers from the ends, skip non-alphanumerics, compare lowercased. O(n) / O(1).",
    "two-sum-ii-input-array-is-sorted": "Two pointers on the sorted array; move based on sum vs target. O(n) / O(1).",
    "3sum": "Sort; fix one element and two-pointer the rest, skipping duplicates. O(n^2) / O(1).",
    "container-with-most-water": "Two pointers from the ends; move the shorter wall inward. O(n) / O(1).",
    "trapping-rain-water": "Two pointers tracking left/right max; water = maxSoFar - height. O(n) / O(1).",

    # Sliding Window
    "best-time-to-buy-and-sell-stock": "Track the min price so far; profit = price - min. O(n) / O(1).",
    "longest-substring-without-repeating-characters": "Sliding window with a last-seen map; shrink on a repeat. O(n) / O(min(n,charset)).",
    "longest-repeating-character-replacement": "Window valid while (len - maxFreq) <= k; expand/shrink. O(n) / O(1).",
    "permutation-in-string": "Fixed-size sliding window comparing 26-char count arrays. O(n) / O(1).",
    "minimum-window-substring": "Expand to satisfy need-counts, then contract to minimize. O(n) / O(charset).",
    "sliding-window-maximum": "Monotonic decreasing deque of indices. O(n) / O(k).",

    # Stack
    "valid-parentheses": "Push opens, match closes against the stack top. O(n) / O(n).",
    "min-stack": "Auxiliary stack (or pairs) tracking the current min. O(1) ops / O(n).",
    "evaluate-reverse-polish-notation": "Stack; on an operator pop two operands and push the result. O(n) / O(n).",
    "generate-parentheses": "Backtrack: add '(' if open<n, ')' if close<open. O(4^n/sqrt(n)) / O(n).",
    "daily-temperatures": "Monotonic decreasing stack of indices; pop when a warmer day appears. O(n) / O(n).",
    "car-fleet": "Sort by position desc; track time-to-target, new fleet when a car can't catch up. O(n log n) / O(n).",
    "largest-rectangle-in-histogram": "Monotonic increasing stack; compute area when popping. O(n) / O(n).",

    # Binary Search
    "binary-search": "Classic lo/hi midpoint halving. O(log n) / O(1).",
    "search-a-2d-matrix": "Treat as a flattened sorted array; binary search the index. O(log m*n) / O(1).",
    "koko-eating-bananas": "Binary search the eating speed; feasibility check by total hours. O(n log max) / O(1).",
    "find-minimum-in-rotated-sorted-array": "Binary search comparing mid to the right end to find the pivot. O(log n) / O(1).",
    "search-in-rotated-sorted-array": "Binary search; figure out which half is sorted and narrow. O(log n) / O(1).",
    "time-based-key-value-store": "Per-key list of (time,val); binary search for <= timestamp. O(log n) get / O(n).",
    "median-of-two-sorted-arrays": "Binary search the partition on the smaller array. O(log min(m,n)) / O(1).",

    # Linked List
    "reverse-linked-list": "Iteratively rewire next pointers (prev/cur). O(n) / O(1).",
    "merge-two-sorted-lists": "Splice nodes with a dummy head. O(n) / O(1).",
    "reorder-list": "Find middle, reverse the second half, merge alternately. O(n) / O(1).",
    "remove-nth-node-from-end-of-list": "Two pointers n apart; remove when the lead hits the end. O(n) / O(1).",
    "copy-list-with-random-pointer": "Interleave clones inline (or old->new hash map). O(n) / O(1) interleave.",
    "add-two-numbers": "Walk both lists with a carry, building the result. O(n) / O(1).",
    "linked-list-cycle": "Floyd's fast/slow pointers meet inside a cycle. O(n) / O(1).",
    "find-the-duplicate-number": "Floyd's cycle detection treating values as next-indices. O(n) / O(1).",
    "lru-cache": "Hash map + doubly linked list for O(1) get/put. O(1) / O(capacity).",
    "merge-k-sorted-lists": "Min-heap of list heads, or pairwise merging. O(n log k) / O(k).",
    "reverse-nodes-in-k-group": "Reverse each k-block iteratively and reconnect. O(n) / O(1).",

    # Trees
    "invert-binary-tree": "Recursively swap left/right subtrees. O(n) / O(h).",
    "maximum-depth-of-binary-tree": "DFS: 1 + max(left, right). O(n) / O(h).",
    "diameter-of-binary-tree": "DFS returning height while tracking max(left+right). O(n) / O(h).",
    "balanced-binary-tree": "DFS returning height; use -1 to signal imbalance. O(n) / O(h).",
    "same-tree": "Simultaneous recursion comparing nodes. O(n) / O(h).",
    "subtree-of-another-tree": "At each node check sameTree against the target. O(n*m) / O(h).",
    "lowest-common-ancestor-of-a-binary-search-tree": "Walk down; the split point where values straddle is the LCA. O(h) / O(1).",
    "binary-tree-level-order-traversal": "BFS with a queue, one level at a time. O(n) / O(n).",
    "binary-tree-right-side-view": "BFS taking the last node per level (or right-first DFS). O(n) / O(n).",
    "count-good-nodes-in-binary-tree": "DFS carrying the max value seen on the path. O(n) / O(h).",
    "validate-binary-search-tree": "DFS passing down (low, high) value bounds. O(n) / O(h).",
    "kth-smallest-element-in-a-bst": "In-order traversal, stop at the kth node. O(h+k) / O(h).",
    "construct-binary-tree-from-preorder-and-inorder-traversal": "Preorder gives the root; split inorder by its index (index map). O(n) / O(n).",
    "binary-tree-maximum-path-sum": "DFS returning best downward path; track a global with both children. O(n) / O(h).",
    "serialize-and-deserialize-binary-tree": "Preorder with explicit null markers. O(n) / O(n).",

    # Tries
    "implement-trie-prefix-tree": "Nodes with a children map and an end flag. O(L) per op / O(total chars).",
    "design-add-and-search-words-data-structure": "Trie with DFS for the '.' wildcard. O(L) add / O(26^dots * L) search.",
    "word-search-ii": "Build a trie of the words; DFS the board pruning by the trie. O(cells*4^L) / O(total chars).",

    # Heap / Priority Queue
    "kth-largest-element-in-a-stream": "Min-heap of size k; its top is the kth largest. O(log k) add / O(k).",
    "last-stone-weight": "Max-heap; repeatedly smash the two heaviest. O(n log n) / O(n).",
    "k-closest-points-to-origin": "Size-k max-heap by distance (or quickselect). O(n log k) / O(k).",
    "kth-largest-element-in-an-array": "Quickselect (avg) or a size-k min-heap. O(n) avg / O(1).",
    "task-scheduler": "Greedy by most-frequent task; closed-form, or max-heap with cooldown. O(n) / O(1).",
    "design-twitter": "Per-user tweet lists; merge the most recent via a heap for the feed. O(feed log) / O(n).",
    "find-median-from-data-stream": "Two balanced heaps: max-heap low half, min-heap high half. O(log n) add / O(n).",

    # Backtracking
    "subsets": "Backtrack include/exclude each element. O(n*2^n) / O(n).",
    "combination-sum": "Backtrack with reuse allowed; prune when over target. O(2^t) / O(t).",
    "permutations": "Backtrack with swapping or a used array. O(n*n!) / O(n).",
    "subsets-ii": "Sort; skip duplicate siblings while backtracking. O(n*2^n) / O(n).",
    "combination-sum-ii": "Sort; use each number once; skip duplicate siblings. O(2^n) / O(n).",
    "word-search": "DFS from each cell, marking visited along the path. O(cells*4^L) / O(L).",
    "palindrome-partitioning": "Backtrack cut points, checking palindrome substrings. O(n*2^n) / O(n).",
    "letter-combinations-of-a-phone-number": "Backtrack over the digit->letters mapping. O(4^n * n) / O(n).",
    "n-queens": "Backtrack column by column; track used cols and both diagonals. O(n!) / O(n).",

    # Graphs
    "number-of-islands": "DFS/BFS flood-fill each unvisited land cell. O(m*n) / O(m*n).",
    "clone-graph": "DFS/BFS with an old->new node map. O(V+E) / O(V).",
    "max-area-of-island": "Flood-fill returning area; track the max. O(m*n) / O(m*n).",
    "pacific-atlantic-water-flow": "BFS/DFS inward from each ocean's borders; intersect the reachable sets. O(m*n) / O(m*n).",
    "surrounded-regions": "Mark border-connected 'O's safe, then flip the rest. O(m*n) / O(m*n).",
    "rotting-oranges": "Multi-source BFS counting minutes. O(m*n) / O(m*n).",
    "walls-and-gates": "Multi-source BFS from all gates at once. O(m*n) / O(m*n).",
    "course-schedule": "Detect a cycle via topological sort (Kahn or DFS colors). O(V+E) / O(V+E).",
    "course-schedule-ii": "Kahn's topological order if there's no cycle. O(V+E) / O(V+E).",
    "redundant-connection": "Union-Find; the edge joining already-connected nodes is the answer. O(n a(n)) / O(n).",
    "number-of-connected-components-in-an-undirected-graph": "Union-Find (or DFS) counting components. O(V+E a) / O(V).",
    "graph-valid-tree": "Fully connected and edges == n-1 (Union-Find / DFS). O(V+E) / O(V).",
    "word-ladder": "BFS over words using wildcard ('*') patterns as edges. O(N*L^2) / O(N*L).",

    # Advanced Graphs
    "reconstruct-itinerary": "Hierholzer's Eulerian path, taking lexicographically smallest. O(E log E) / O(E).",
    "min-cost-to-connect-all-points": "Prim's MST on the dense graph. O(n^2) / O(n).",
    "network-delay-time": "Dijkstra from the source; answer is the max shortest-distance. O(E log V) / O(V).",
    "swim-in-rising-water": "Dijkstra/min-heap minimizing the max elevation along a path. O(n^2 log n) / O(n^2).",
    "alien-dictionary": "Build a precedence graph from adjacent words, then topological sort. O(C) / O(1).",
    "cheapest-flights-within-k-stops": "Bellman-Ford limited to k+1 relaxation rounds. O(k*E) / O(V).",

    # 1-D Dynamic Programming
    "climbing-stairs": "Fibonacci: dp[i] = dp[i-1] + dp[i-2]. O(n) / O(1).",
    "min-cost-climbing-stairs": "dp[i] = cost[i] + min(dp[i-1], dp[i-2]). O(n) / O(1).",
    "house-robber": "dp = max(skip, rob + prev2). O(n) / O(1).",
    "house-robber-ii": "Run the linear robber twice (exclude first, or exclude last). O(n) / O(1).",
    "longest-palindromic-substring": "Expand around each center. O(n^2) / O(1).",
    "palindromic-substrings": "Expand around each center and count. O(n^2) / O(1).",
    "decode-ways": "dp over valid 1- and 2-digit decodings. O(n) / O(1).",
    "coin-change": "Unbounded knapsack: dp[a] = min over coins. O(amount*coins) / O(amount).",
    "maximum-product-subarray": "Track running max and min (signs flip on negatives). O(n) / O(1).",
    "word-break": "dp[i] true if some j has dp[j] and word[j:i] in the dict. O(n^2) / O(n).",
    "longest-increasing-subsequence": "Patience sorting: binary search into a tails array. O(n log n) / O(n).",
    "partition-equal-subset-sum": "Subset-sum to total/2 via boolean DP. O(n*sum) / O(sum).",

    # 2-D Dynamic Programming
    "unique-paths": "dp grid summing top+left (or combinatorics C(m+n-2, m-1)). O(m*n) / O(n).",
    "longest-common-subsequence": "2-D dp incrementing on matches. O(m*n) / O(n).",
    "best-time-to-buy-and-sell-stock-with-cooldown": "State-machine dp over hold/sold/rest. O(n) / O(1).",
    "coin-change-ii": "Count combinations: dp over coins, then amounts. O(amount*coins) / O(amount).",
    "target-sum": "Transform to a subset-sum count via DP. O(n*sum) / O(sum).",
    "interleaving-string": "2-D dp matching s1 and s2 into s3. O(m*n) / O(n).",
    "longest-increasing-path-in-a-matrix": "DFS with memoization. O(m*n) / O(m*n).",
    "distinct-subsequences": "2-D dp counting subsequence matches. O(m*n) / O(n).",
    "edit-distance": "2-D dp over insert/delete/replace. O(m*n) / O(n).",
    "burst-balloons": "Interval dp on the last balloon burst in a range. O(n^3) / O(n^2).",
    "regular-expression-matching": "2-D dp handling '*' and '.'. O(m*n) / O(m*n).",

    # Greedy
    "maximum-subarray": "Kadane's: drop the running sum when it goes negative. O(n) / O(1).",
    "jump-game": "Track the farthest reachable index. O(n) / O(1).",
    "jump-game-ii": "BFS-like greedy over the current jump range. O(n) / O(1).",
    "gas-station": "If total gas >= cost, start where the tank last went negative. O(n) / O(1).",
    "hand-of-straights": "Count cards; greedily build consecutive runs from the smallest. O(n log n) / O(n).",
    "merge-triplets-to-form-target-triplet": "Keep triplets with no value above target; OR-combine them. O(n) / O(1).",
    "partition-labels": "Record each char's last index; cut when the window end is reached. O(n) / O(1).",
    "valid-parenthesis-string": "Track the range [low, high] of possible open counts. O(n) / O(1).",

    # Intervals
    "insert-interval": "Add non-overlapping parts before/after, merging the overlap. O(n) / O(n).",
    "merge-intervals": "Sort by start, then merge overlapping intervals. O(n log n) / O(n).",
    "non-overlapping-intervals": "Sort by end; greedily keep the earliest-finishing. O(n log n) / O(1).",
    "meeting-rooms": "Sort by start and check for any overlap. O(n log n) / O(1).",
    "meeting-rooms-ii": "Min-heap of end times (or sweep line) for concurrent rooms. O(n log n) / O(n).",
    "minimum-interval-to-include-each-query": "Sort queries and intervals; min-heap by interval size. O(n log n) / O(n).",

    # Math & Geometry
    "rotate-image": "Transpose, then reverse each row, in place. O(n^2) / O(1).",
    "spiral-matrix": "Peel boundaries with four shrinking bounds. O(m*n) / O(1).",
    "set-matrix-zeroes": "Use the first row/column as zero markers. O(m*n) / O(1).",
    "happy-number": "Floyd cycle detection on digit-square sums. O(log n) / O(1).",
    "plus-one": "Add the carry from the least significant digit. O(n) / O(1).",
    "powx-n": "Fast exponentiation by squaring. O(log n) / O(1).",
    "multiply-strings": "Schoolbook digit multiplication into index buckets. O(m*n) / O(m+n).",
    "detect-squares": "Hash point counts; for a query, find diagonal corners. O(n) per query / O(n).",

    # Bit Manipulation
    "single-number": "XOR everything; pairs cancel out. O(n) / O(1).",
    "number-of-1-bits": "n &= n-1 clears the lowest set bit each step. O(set bits) / O(1).",
    "counting-bits": "dp[i] = dp[i >> 1] + (i & 1). O(n) / O(n).",
    "reverse-bits": "Shift bits one at a time into the reversed position. O(1) / O(1).",
    "missing-number": "XOR all indices and values (or use the sum formula). O(n) / O(1).",
    "sum-of-two-integers": "Loop: XOR is the sum, (AND << 1) is the carry. O(1) / O(1).",
    "reverse-integer": "Pop/push digits while checking 32-bit overflow. O(log n) / O(1).",
}


def gist_for(slug):
    """One-line optimal-approach hint for a problem, or '' if unknown."""
    return GISTS.get(slug, "")
