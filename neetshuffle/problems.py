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
