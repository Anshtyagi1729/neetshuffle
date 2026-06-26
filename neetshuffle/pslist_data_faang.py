"""Roadmap problem set ("psList").

Each entry is a plain dict so the dataset stays auditable (no executable
content). Fields:
  name        - problem title
  url         - canonical problem URL (the unique key)
  source      - judge it lives on (leetcode, cses, atcoder, ...)
  topic       - top-level roadmap section
  subtopic    - sub-section within the topic
  difficulty  - coarse band (Easy, Easy+, Normal, ... Grandmaster)
  rank        - fine-grained numeric difficulty for sorting/filtering
  importance  - 0..3 priority hint from the roadmap
"""

PSLIST = [
    # === BFS & DFS ===
    # -- BFS
    {"name": 'Breadth First Search', "url": 'https://atcoder.jp/contests/abc007/tasks/abc007_3', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Message Route', "url": 'https://cses.fi/problemset/task/1667/', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Labyrinth', "url": 'https://cses.fi/problemset/task/1193', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Grid Repainting', "url": 'https://atcoder.jp/contests/abc088/tasks/abc088_d', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Knight Moves Grid', "url": 'https://cses.fi/problemset/task/3217/', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Easy+', "rank": 2.5, "importance": 2},
    {"name": 'Building Teams', "url": 'https://cses.fi/problemset/task/1668', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Monsters', "url": 'https://cses.fi/problemset/task/1194', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Darker and Darker', "url": 'https://atcoder.jp/contests/agc033/tasks/agc033_a', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Biridian Forest', "url": 'https://codeforces.com/problemset/problem/329/B', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Two Buttons', "url": 'https://codeforces.com/problemset/problem/520/B', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'BFS', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    # -- Flood Fill
    {"name": 'Counting Rooms', "url": 'https://cses.fi/problemset/task/1192', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Maze', "url": 'https://codeforces.com/problemset/problem/377/A', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Minesweeper', "url": 'https://leetcode.com/problems/minesweeper/description/', "source": 'leetcode', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Normal', "rank": 3.0, "importance": 1},
    {"name": 'Number of Islands', "url": 'https://leetcode.com/problems/number-of-islands/', "source": 'leetcode', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Sensors', "url": 'https://atcoder.jp/contests/abc325/tasks/abc325_c', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Surrounded Regions', "url": 'https://leetcode.com/problems/surrounded-regions/', "source": 'leetcode', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Pacific Atlantic Water Flow', "url": 'https://leetcode.com/problems/pacific-atlantic-water-flow/', "source": 'leetcode', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'The Labyrinth', "url": 'https://codeforces.com/problemset/problem/616/C', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Solve The Maze', "url": 'https://codeforces.com/problemset/problem/1365/D', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'Flood Fill', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    # -- DFS
    {"name": 'Building Roads', "url": 'https://cses.fi/problemset/task/1666', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Tour', "url": 'https://atcoder.jp/contests/abc204/tasks/abc204_c', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Kefa and Park', "url": 'https://codeforces.com/problemset/problem/580/C', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Count Simple Paths', "url": 'https://atcoder.jp/contests/abc284/tasks/abc284_e', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Subordinates', "url": 'https://cses.fi/problemset/task/1674', "source": 'cses', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Mahmoud and Ehab and the bipartiteness', "url": 'https://codeforces.com/problemset/problem/862/B', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Takahashi Tour', "url": 'https://atcoder.jp/contests/abc213/tasks/abc213_d', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Cyclic Components', "url": 'https://codeforces.com/problemset/problem/977/E', "source": 'codeforces', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Normal+', "rank": 4.5, "importance": 3},
    {"name": 'Ki', "url": 'https://atcoder.jp/contests/abc138/tasks/abc138_d', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Make Bipartite 2', "url": 'https://atcoder.jp/contests/abc282/tasks/abc282_d', "source": 'atcoder', "topic": 'BFS & DFS', "subtopic": 'DFS', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    # === Complete Search ===
    # -- Brute Force
    {"name": 'Lucky PIN', "url": 'https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Easy+', "rank": 2.0, "importance": 0},
    {"name": 'March', "url": 'https://atcoder.jp/contests/abc089/tasks/abc089_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Easy+', "rank": 2.0, "importance": 0},
    {"name": 'Pyramid', "url": 'https://atcoder.jp/contests/abc112/tasks/abc112_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": '105', "url": 'https://atcoder.jp/contests/abc106/tasks/abc106_b', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Easy', "rank": 1.5, "importance": 2},
    {"name": 'Half and Half', "url": 'https://atcoder.jp/contests/abc095/tasks/arc096_a', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'HonestOrUnkind2', "url": 'https://atcoder.jp/contests/abc147/tasks/abc147_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Array and Segments (Easy)', "url": 'https://codeforces.com/problemset/problem/1108/E1', "source": 'codeforces', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Shipping Center', "url": 'https://atcoder.jp/contests/abc195/tasks/abc195_d', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Brute Force', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    # -- Permutations & Subsets
    {"name": 'Apple Division', "url": 'https://cses.fi/problemset/task/1623', "source": 'cses', "topic": 'Complete Search', "subtopic": 'Permutations & Subsets', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Buildings are Colorful!', "url": 'https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Permutations & Subsets', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Creating Strings', "url": 'https://cses.fi/problemset/task/1622', "source": 'cses', "topic": 'Complete Search', "subtopic": 'Permutations & Subsets', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": 'Three Logos', "url": 'https://codeforces.com/problemset/problem/581/D', "source": 'codeforces', "topic": 'Complete Search', "subtopic": 'Permutations & Subsets', "difficulty": 'Hard', "rank": 5.5, "importance": 0},
    {"name": 'Make 2-Regular Graph', "url": 'https://atcoder.jp/contests/abc412/tasks/abc412_d', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Permutations & Subsets', "difficulty": 'Hard', "rank": 5.0, "importance": 0},
    {"name": 'Switches', "url": 'https://atcoder.jp/contests/abc128/tasks/abc128_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Permutations & Subsets', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    # -- Additional Practice
    {"name": 'Train Ticket', "url": 'https://atcoder.jp/contests/abc079/tasks/abc079_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Easy+', "rank": 2.5, "importance": 2},
    {"name": 'Cheap Travel', "url": 'https://codeforces.com/problemset/problem/466/A', "source": 'codeforces', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Normal', "rank": 3.0, "importance": 1},
    {"name": 'Skill Up', "url": 'https://atcoder.jp/contests/abc167/tasks/abc167_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Sum of Three Integers', "url": 'https://atcoder.jp/contests/abc051/tasks/abc051_b', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'ORXOR', "url": 'https://atcoder.jp/contests/abc197/tasks/abc197_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": '755', "url": 'https://atcoder.jp/contests/abc114/tasks/abc114_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Many Formulas', "url": 'https://atcoder.jp/contests/abc045/tasks/arc061_a', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Hard', "rank": 5.5, "importance": 3},
    {"name": 'Hanjo', "url": 'https://atcoder.jp/contests/abc196/tasks/abc196_d', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Harder', "rank": 6.5, "importance": 2},
    {"name": 'ABC Puzzle', "url": 'https://atcoder.jp/contests/abc326/tasks/abc326_d', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Harder', "rank": 6.5, "importance": 2},
    {"name": 'All Green', "url": 'https://atcoder.jp/contests/abc104/tasks/abc104_c', "source": 'atcoder', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Insane', "rank": 7.0, "importance": 3},
    {"name": 'Prime Gift', "url": 'https://codeforces.com/problemset/problem/912/E', "source": 'codeforces', "topic": 'Complete Search', "subtopic": 'Additional Practice', "difficulty": 'Master', "rank": 9.0, "importance": 1},
    # === Recursion ===
    # -- Brute Force with Recursion
    {"name": 'Tower of Hanoi', "url": 'https://cses.fi/problemset/task/2165', "source": 'cses', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Normal', "rank": 3.0, "importance": 1},
    {"name": 'Permutations', "url": 'https://leetcode.com/problems/permutations/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Subsets', "url": 'https://leetcode.com/problems/subsets/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Combinations', "url": 'https://leetcode.com/problems/combinations/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Brute-force Attack', "url": 'https://atcoder.jp/contests/abc029/tasks/abc029_c', "source": 'atcoder', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Letter Combinations of a Phone Number', "url": 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Subsets II', "url": 'https://leetcode.com/problems/subsets-ii/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Brute Force with Recursion', "difficulty": 'Normal+', "rank": 4.0, "importance": 1},
    # -- Backtracking & Pruning
    {"name": 'Chessboard and Queens', "url": 'https://cses.fi/problemset/task/1624', "source": 'cses', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Combination Sum', "url": 'https://leetcode.com/problems/combination-sum/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Generate Parentheses', "url": 'https://leetcode.com/problems/generate-parentheses/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Grid Path Description', "url": 'https://cses.fi/problemset/task/1625/', "source": 'cses', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Sudoku Solver', "url": 'https://leetcode.com/problems/sudoku-solver/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Palindrome Partitioning', "url": 'https://leetcode.com/problems/palindrome-partitioning/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'N-Queens', "url": 'https://leetcode.com/problems/n-queens/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Word Search', "url": 'https://leetcode.com/problems/word-search/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Backtracking & Pruning', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    # -- Additional Practice
    {"name": 'Divide and Divide', "url": 'https://atcoder.jp/contests/abc340/tasks/abc340_c', "source": 'atcoder', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Dreamoon and WiFi', "url": 'https://codeforces.com/problemset/problem/476/B', "source": 'codeforces', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Yet Another Recursive Function', "url": 'https://atcoder.jp/contests/abc275/tasks/abc275_d', "source": 'atcoder', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Different Ways to Add Parentheses', "url": 'https://leetcode.com/problems/different-ways-to-add-parentheses/', "source": 'leetcode', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Dance', "url": 'https://atcoder.jp/contests/abc236/tasks/abc236_d', "source": 'atcoder', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Harder', "rank": 6.0, "importance": 3},
    {"name": "Knight's Tour", "url": 'https://cses.fi/problemset/task/1689', "source": 'cses', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'Synthetic Kadomatsu', "url": 'https://atcoder.jp/contests/abc119/tasks/abc119_c', "source": 'atcoder', "topic": 'Recursion', "subtopic": 'Additional Practice', "difficulty": 'Harder', "rank": 6.5, "importance": 2},
    # === Disjoint Union Set (DSU) ===
    # -- DSU
    {"name": 'Redundant Connection', "url": 'https://leetcode.com/problems/redundant-connection/', "source": 'leetcode', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Large Graph', "url": 'https://codeforces.com/contest/1978/problem/F', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Master', "rank": 9.0, "importance": 1},
    {"name": 'Accounts Merge', "url": 'https://leetcode.com/problems/accounts-merge/', "source": 'leetcode', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Satisfiability of Equality Equations', "url": 'https://leetcode.com/problems/satisfiability-of-equality-equations/', "source": 'leetcode', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Road Construction', "url": 'https://cses.fi/problemset/task/1676', "source": 'cses', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'K-th Largest Connected Component', "url": 'https://atcoder.jp/contests/abc372/tasks/abc372_e', "source": 'atcoder', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Decayed Bridges', "url": 'https://atcoder.jp/contests/abc120/tasks/abc120_d', "source": 'atcoder', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Mediator', "url": 'https://atcoder.jp/contests/abc350/tasks/abc350_g', "source": 'atcoder', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Expert', "rank": 8.0, "importance": 2},
    {"name": 'Learning Languages', "url": 'https://codeforces.com/contest/277/problem/A', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Secret Passwords', "url": 'https://codeforces.com/contest/1263/problem/D', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'DSU', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    # -- MST
    {"name": 'Road Reparation', "url": 'https://cses.fi/problemset/task/1675', "source": 'cses', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'MST', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Min Cost to Connect All Points', "url": 'https://leetcode.com/problems/min-cost-to-connect-all-points/description/', "source": 'leetcode', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'MST', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Shichikuji and Power Grid', "url": 'https://codeforces.com/problemset/problem/1245/D', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'MST', "difficulty": 'Harder', "rank": 6.5, "importance": 2},
    {"name": 'GCD and MST', "url": 'https://codeforces.com/problemset/problem/1513/D', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'MST', "difficulty": 'Insane', "rank": 7.0, "importance": 2},
    {"name": 'Minimum spanning tree for each edge', "url": 'https://codeforces.com/contest/609/problem/E', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'MST', "difficulty": 'Insane', "rank": 7.5, "importance": 2},
    {"name": 'Road Reform', "url": 'https://codeforces.com/contest/1468/problem/J', "source": 'codeforces', "topic": 'Disjoint Union Set (DSU)', "subtopic": 'MST', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    # === Prefix Sums ===
    # -- Prefix Sums
    {"name": 'GeT AC', "url": 'https://atcoder.jp/contests/abc122/tasks/abc122_c', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Tsundoku', "url": 'https://atcoder.jp/contests/abc172/tasks/abc172_c', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Wandering', "url": 'https://atcoder.jp/contests/abc182/tasks/abc182_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Subarray Sum Equals K', "url": 'https://leetcode.com/problems/subarray-sum-equals-k/', "source": 'leetcode', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Static Range Sum Queries', "url": 'https://cses.fi/problemset/task/1646', "source": 'cses', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Easy', "rank": 1.5, "importance": 3},
    {"name": 'Ilya and Queries', "url": 'https://codeforces.com/problemset/problem/313/B', "source": 'codeforces', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Subarray Divisible by N', "url": 'https://cses.fi/problemset/task/1662', "source": 'cses', "topic": 'Prefix Sums', "subtopic": 'Prefix Sums', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    # -- Difference Arrays
    {"name": 'Water Heater', "url": 'https://atcoder.jp/contests/abc183/tasks/abc183_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Difference Arrays', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Snuke Prime', "url": 'https://atcoder.jp/contests/abc188/tasks/abc188_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Difference Arrays', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Little Girl and Maximum Sum', "url": 'https://codeforces.com/problemset/problem/276/C', "source": 'codeforces', "topic": 'Prefix Sums', "subtopic": 'Difference Arrays', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Corporate Flight Bookings', "url": 'https://leetcode.com/problems/corporate-flight-bookings/', "source": 'leetcode', "topic": 'Prefix Sums', "subtopic": 'Difference Arrays', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Online games', "url": 'https://atcoder.jp/contests/abc221/tasks/abc221_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Difference Arrays', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Othello', "url": 'https://atcoder.jp/contests/abc035/tasks/abc035_c', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Difference Arrays', "difficulty": 'Hard', "rank": 5.0, "importance": 1},
    # -- 2D Prefix Sums
    {"name": 'Forest Queries', "url": 'https://cses.fi/problemset/task/1652', "source": 'cses', "topic": 'Prefix Sums', "subtopic": '2D Prefix Sums', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Range Sum Query 2D - Immutable', "url": 'https://leetcode.com/problems/range-sum-query-2d-immutable/', "source": 'leetcode', "topic": 'Prefix Sums', "subtopic": '2D Prefix Sums', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'AtCoder Express 2', "url": 'https://atcoder.jp/contests/abc106/tasks/abc106_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": '2D Prefix Sums', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Pond', "url": 'https://atcoder.jp/contests/abc203/tasks/abc203_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": '2D Prefix Sums', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Matrix Block Sum', "url": 'https://leetcode.com/problems/matrix-block-sum/', "source": 'leetcode', "topic": 'Prefix Sums', "subtopic": '2D Prefix Sums', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Counting Rectangles', "url": 'https://codeforces.com/problemset/problem/1722/E', "source": 'codeforces', "topic": 'Prefix Sums', "subtopic": '2D Prefix Sums', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # -- Additional Practice
    {"name": 'Number of Ways', "url": 'https://codeforces.com/problemset/problem/466/C', "source": 'codeforces', "topic": 'Prefix Sums', "subtopic": 'Additional Practice', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Lamp', "url": 'https://atcoder.jp/contests/abc129/tasks/abc129_d', "source": 'atcoder', "topic": 'Prefix Sums', "subtopic": 'Additional Practice', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    # === Stacks & Queues ===
    # -- Monotonic Stack
    {"name": 'Daily Temperatures', "url": 'https://leetcode.com/problems/daily-temperatures/', "source": 'leetcode', "topic": 'Stacks & Queues', "subtopic": 'Monotonic Stack', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Next Greater Element II', "url": 'https://leetcode.com/problems/next-greater-element-ii/', "source": 'leetcode', "topic": 'Stacks & Queues', "subtopic": 'Monotonic Stack', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Nearest Smaller Values', "url": 'https://cses.fi/problemset/task/1645', "source": 'cses', "topic": 'Stacks & Queues', "subtopic": 'Monotonic Stack', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Largest Rectangle in Histogram', "url": 'https://leetcode.com/problems/largest-rectangle-in-histogram/', "source": 'leetcode', "topic": 'Stacks & Queues', "subtopic": 'Monotonic Stack', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Sum of Subarray Minimums', "url": 'https://leetcode.com/problems/sum-of-subarray-minimums/', "source": 'leetcode', "topic": 'Stacks & Queues', "subtopic": 'Monotonic Stack', "difficulty": 'Normal+', "rank": 4.5, "importance": 3},
    # -- Monotonic Queue
    {"name": 'Sliding Window Maximum', "url": 'https://leetcode.com/problems/sliding-window-maximum/', "source": 'leetcode', "topic": 'Stacks & Queues', "subtopic": 'Monotonic Queue', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    # -- Additional Practice
    {"name": 'Decode String', "url": 'https://leetcode.com/problems/decode-string/description/', "source": 'leetcode', "topic": 'Stacks & Queues', "subtopic": 'Additional Practice', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    # === More Graph Algorithms ===
    # -- Dijkstras
    {"name": 'Our clients, please wait a moment', "url": 'https://atcoder.jp/contests/abc325/tasks/abc325_e', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Shortest Routes I', "url": 'https://cses.fi/problemset/task/1671', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Super Takahashi Bros.', "url": 'https://atcoder.jp/contests/abc340/tasks/abc340_d', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Routing', "url": 'https://atcoder.jp/contests/arc177/tasks/arc177_c', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Flight Discount', "url": 'https://cses.fi/problemset/task/1195', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Rendez-vous de Marian et Robin', "url": 'https://codeforces.com/contest/2014/problem/E', "source": 'codeforces', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Harder', "rank": 6.0, "importance": 1},
    {"name": 'Investigation', "url": 'https://cses.fi/problemset/task/1202', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Edge Deletion', "url": 'https://codeforces.com/contest/1076/problem/D', "source": 'codeforces', "topic": 'More Graph Algorithms', "subtopic": 'Dijkstras', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    # -- Topological Sort
    {"name": 'Course Schedule', "url": 'https://cses.fi/problemset/task/1679', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Topological Sort', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Fox And Names', "url": 'https://codeforces.com/contest/510/problem/C', "source": 'codeforces', "topic": 'More Graph Algorithms', "subtopic": 'Topological Sort', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Restricted Permutation', "url": 'https://atcoder.jp/contests/abc223/tasks/abc223_d', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Topological Sort', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Course Schedule II', "url": 'https://leetcode.com/problems/course-schedule-ii/', "source": 'leetcode', "topic": 'More Graph Algorithms', "subtopic": 'Topological Sort', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Parallel Courses', "url": 'https://leetcode.com/problems/parallel-courses/', "source": 'leetcode', "topic": 'More Graph Algorithms', "subtopic": 'Topological Sort', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Substring', "url": 'https://codeforces.com/problemset/problem/919/D', "source": 'codeforces', "topic": 'More Graph Algorithms', "subtopic": 'Topological Sort', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    # -- Floyd Warshall
    {"name": 'Souvenir', "url": 'https://atcoder.jp/contests/abc286/tasks/abc286_e', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Floyd Warshall', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    # -- Cycle Detection
    {"name": 'Cycle', "url": 'https://atcoder.jp/contests/abc376/tasks/abc376_d', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Cycle Detection', "difficulty": 'Normal+', "rank": 4.0, "importance": 1},
    {"name": 'Round Trip II', "url": 'https://cses.fi/problemset/task/1678', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Cycle Detection', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Round Trip', "url": 'https://cses.fi/problemset/task/1669', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Cycle Detection', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Round Trip', "url": 'https://atcoder.jp/contests/abc276/tasks/abc276_e', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Cycle Detection', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Change Usernames', "url": 'https://atcoder.jp/contests/abc285/tasks/abc285_d', "source": 'atcoder', "topic": 'More Graph Algorithms', "subtopic": 'Cycle Detection', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Graph Girth', "url": 'https://cses.fi/problemset/task/1707', "source": 'cses', "topic": 'More Graph Algorithms', "subtopic": 'Cycle Detection', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # === LCA & Tree Queries ===
    # -- Centroid Decomposition
    {"name": 'Close Vertices', "url": 'https://codeforces.com/problemset/problem/293/E', "source": 'codeforces', "topic": 'LCA & Tree Queries', "subtopic": 'Centroid Decomposition', "difficulty": 'Grandmaster', "rank": 10.0, "importance": 2},
    # === Getting Started ===
    # -- I/O & Basic Syntax
    {"name": 'Multiplication 2', "url": 'https://atcoder.jp/contests/abc169/tasks/abc169_b', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 0},
    {"name": 'ABC400 Party', "url": 'https://atcoder.jp/contests/abc400/tasks/abc400_a', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 0},
    {"name": 'Grid Walk', "url": 'https://atcoder.jp/contests/abc364/tasks/abc364_b', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 0},
    {"name": 'Present from Lena', "url": 'https://codeforces.com/problemset/problem/118/B', "source": 'codeforces', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 0},
    {"name": 'Full House 2', "url": 'https://atcoder.jp/contests/abc386/tasks/abc386_a', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Heavy Snake', "url": 'https://atcoder.jp/contests/abc388/tasks/abc388_b', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Weird Algorithm', "url": 'https://cses.fi/problemset/task/1068', "source": 'cses', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Word', "url": 'https://codeforces.com/problemset/problem/59/A', "source": 'codeforces', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Geometric Sequence', "url": 'https://atcoder.jp/contests/abc390/tasks/abc390_b', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": '1122 String', "url": 'https://atcoder.jp/contests/abc381/tasks/abc381_b', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'I/O & Basic Syntax', "difficulty": 'Easy', "rank": 1.5, "importance": 2},
    # -- Simulation
    {"name": 'Josephus Problem I', "url": 'https://cses.fi/problemset/task/2162/', "source": 'cses', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": 'Spiral Rotation', "url": 'https://atcoder.jp/contests/abc375/tasks/abc375_c', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Hard', "rank": 5.0, "importance": 0},
    {"name": 'Fall Down', "url": 'https://codeforces.com/problemset/problem/1669/G', "source": 'codeforces', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": 'Ancestor', "url": 'https://atcoder.jp/contests/abc263/tasks/abc263_b', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Consecutive', "url": 'https://atcoder.jp/contests/abc328/tasks/abc328_c', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'Digital Counter', "url": 'https://codeforces.com/problemset/problem/495/A', "source": 'codeforces', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Easy+', "rank": 2.5, "importance": 2},
    {"name": 'Takahashi Gets Lost', "url": 'https://atcoder.jp/contests/abc341/tasks/abc341_c', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'Simulation', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    # -- Time & Space Complexity
    {"name": 'Missing Number', "url": 'https://cses.fi/problemset/task/1083', "source": 'cses', "topic": 'Getting Started', "subtopic": 'Time & Space Complexity', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Otoshidama', "url": 'https://atcoder.jp/contests/abc085/tasks/abc085_c', "source": 'atcoder', "topic": 'Getting Started', "subtopic": 'Time & Space Complexity', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'Distinct Numbers', "url": 'https://cses.fi/problemset/task/1621', "source": 'cses', "topic": 'Getting Started', "subtopic": 'Time & Space Complexity', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    # === Maps & Sets ===
    {"name": 'Two Sum', "url": 'https://cses.fi/problemset/task/1640', "source": 'cses', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Easy', "rank": 1.5, "importance": 0},
    {"name": 'Diversity of Scores', "url": 'https://atcoder.jp/contests/abc343/tasks/abc343_d', "source": 'atcoder', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 0},
    {"name": 'Playlist', "url": 'https://cses.fi/problemset/task/1141', "source": 'cses', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 0},
    {"name": 'Pedometer', "url": 'https://atcoder.jp/contests/abc367/tasks/abc367_d', "source": 'atcoder', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": 'Subarray Sums II', "url": 'https://cses.fi/problemset/task/1661/', "source": 'cses', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": 'Subarray Divisibility', "url": 'https://cses.fi/problemset/task/1662/', "source": 'cses', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Concert Tickets', "url": 'https://cses.fi/problemset/task/1091', "source": 'cses', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 0},
    {"name": 'Traffic Lights', "url": 'https://cses.fi/problemset/task/1163', "source": 'cses', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 0},
    {"name": 'Isolation', "url": 'https://atcoder.jp/contests/abc302/tasks/abc302_e', "source": 'atcoder', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Normal', "rank": 3.5, "importance": 1},
    {"name": 'Wrapping Chocolate', "url": 'https://atcoder.jp/contests/abc245/tasks/abc245_e', "source": 'atcoder', "topic": 'Maps & Sets', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # === Two Pointers ===
    {"name": 'Valid Palindrome', "url": 'https://leetcode.com/problems/valid-palindrome/', "source": 'leetcode', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Two Sum II - Input Array Is Sorted', "url": 'https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/', "source": 'leetcode', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Container With Most Water', "url": 'https://leetcode.com/problems/container-with-most-water/', "source": 'leetcode', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Sum of Three Values', "url": 'https://cses.fi/problemset/task/1641', "source": 'cses', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Sum of Four Values', "url": 'https://cses.fi/problemset/task/1642', "source": 'cses', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Trapping Rain Water', "url": 'https://leetcode.com/problems/trapping-rain-water/', "source": 'leetcode', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Sum of Two Values', "url": 'https://cses.fi/problemset/task/1640', "source": 'cses', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Three Parts of the Array', "url": 'https://codeforces.com/problemset/problem/1006/C', "source": 'codeforces', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Number of Pairs', "url": 'https://codeforces.com/problemset/problem/1538/C', "source": 'codeforces', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Cellular Network', "url": 'https://codeforces.com/problemset/problem/702/C', "source": 'codeforces', "topic": 'Two Pointers', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 3},
    # === Sliding Window ===
    {"name": 'Sliding Window Sum', "url": 'https://cses.fi/problemset/task/3220', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Longest Substring Without Repeating Characters', "url": 'https://leetcode.com/problems/longest-substring-without-repeating-characters/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Minimum Size Subarray Sum', "url": 'https://leetcode.com/problems/minimum-size-subarray-sum/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Subarray Sums I', "url": 'https://cses.fi/problemset/task/1660/', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Books', "url": 'https://codeforces.com/problemset/problem/279/B', "source": 'codeforces', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Permutation in String', "url": 'https://leetcode.com/problems/permutation-in-string/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Subarray Product Less Than K', "url": 'https://leetcode.com/problems/subarray-product-less-than-k/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Sliding Window Distinct Values', "url": 'https://cses.fi/problemset/task/3222', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Longest Repeating Character Replacement', "url": 'https://leetcode.com/problems/longest-repeating-character-replacement/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Count Subarrays Where Max Element Appears at Least K Times', "url": 'https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Sliding Window Minimum', "url": 'https://cses.fi/problemset/task/3221', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Sliding Window Xor', "url": 'https://cses.fi/problemset/task/3426', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 1},
    {"name": 'Sliding Window Or', "url": 'https://cses.fi/problemset/task/3405', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 1},
    {"name": 'Approximating a Constant Range', "url": 'https://codeforces.com/contest/602/problem/B', "source": 'codeforces', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Sliding Median', "url": 'https://cses.fi/problemset/task/1076', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Sliding Cost', "url": 'https://cses.fi/problemset/task/1077', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'Sliding Window Mode', "url": 'https://cses.fi/problemset/task/3224', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 1},
    {"name": 'Sliding Window Mex', "url": 'https://cses.fi/problemset/task/3219', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 1},
    {"name": 'Minimum Window Substring', "url": 'https://leetcode.com/problems/minimum-window-substring/', "source": 'leetcode', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Sliding Window Inversions', "url": 'https://cses.fi/problemset/task/3223', "source": 'cses', "topic": 'Sliding Window', "subtopic": '', "difficulty": 'Hard', "rank": 5.5, "importance": 3},
    # === Heaps & Priority Queues ===
    {"name": 'Last Stone Weight', "url": 'https://leetcode.com/problems/last-stone-weight/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Easy', "rank": 1.5, "importance": 2},
    {"name": 'Kth Largest Element in an Array', "url": 'https://leetcode.com/problems/kth-largest-element-in-an-array/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Top K Frequent Elements', "url": 'https://leetcode.com/problems/top-k-frequent-elements/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Kth Largest Element in a Stream', "url": 'https://leetcode.com/problems/kth-largest-element-in-a-stream/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'Room Allocation', "url": 'https://cses.fi/problemset/task/1164', "source": 'cses', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Merge K Sorted Lists', "url": 'https://leetcode.com/problems/merge-k-sorted-lists/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Find Median from Data Stream', "url": 'https://leetcode.com/problems/find-median-from-data-stream/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 3},
    {"name": 'Task Scheduler', "url": 'https://leetcode.com/problems/task-scheduler/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'IPO', "url": 'https://leetcode.com/problems/ipo/description/', "source": 'leetcode', "topic": 'Heaps & Priority Queues', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # === Fenwick Tree (BIT) ===
    # -- Coordinate Compression
    {"name": 'Count of Smaller Numbers After Self', "url": 'https://leetcode.com/problems/count-of-smaller-numbers-after-self/', "source": 'leetcode', "topic": 'Fenwick Tree (BIT)', "subtopic": 'Coordinate Compression', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Sliding Window Inversions', "url": 'https://cses.fi/problemset/task/3223', "source": 'cses', "topic": 'Fenwick Tree (BIT)', "subtopic": 'Coordinate Compression', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Salary Queries', "url": 'https://cses.fi/problemset/task/1144', "source": 'cses', "topic": 'Fenwick Tree (BIT)', "subtopic": 'Coordinate Compression', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    # === Binary Search ===
    # -- Binary Search on Sorted Array
    {"name": 'Binary Search', "url": 'https://leetcode.com/problems/binary-search/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Search Insert Position', "url": 'https://leetcode.com/problems/search-insert-position/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Easy', "rank": 1.5, "importance": 3},
    {"name": 'Longest Increasing Subsequence', "url": 'https://leetcode.com/problems/longest-increasing-subsequence/description/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Towers', "url": 'https://cses.fi/problemset/task/1073', "source": 'cses', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Snuke Festival', "url": 'https://atcoder.jp/contests/abc077/tasks/arc084_a', "source": 'atcoder', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Queries about less or equal elements', "url": 'https://codeforces.com/problemset/problem/600/B', "source": 'codeforces', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Triangles', "url": 'https://atcoder.jp/contests/abc143/tasks/abc143_d', "source": 'atcoder', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Range Count Query', "url": 'https://atcoder.jp/contests/abc248/tasks/abc248_d', "source": 'atcoder', "topic": 'Binary Search', "subtopic": 'Binary Search on Sorted Array', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    # -- Binary Search on Answer
    {"name": 'Koko Eating Bananas', "url": 'https://leetcode.com/problems/koko-eating-bananas/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Capacity To Ship Packages Within D Days', "url": 'https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Factory Machines', "url": 'https://cses.fi/problemset/task/1620', "source": 'cses', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Array Division', "url": 'https://cses.fi/problemset/task/1085', "source": 'cses', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'How to Win the Election', "url": 'https://atcoder.jp/contests/abc373/tasks/abc373_e', "source": 'atcoder', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'The Meeting Place Cannot Be Changed', "url": 'https://codeforces.com/problemset/problem/780/B', "source": 'codeforces', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Minimum Number of Days to Make m Bouquets', "url": 'https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Magnetic Force Between Two Balls', "url": 'https://leetcode.com/problems/magnetic-force-between-two-balls/', "source": 'leetcode', "topic": 'Binary Search', "subtopic": 'Binary Search on Answer', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    # === Trees & Binary Trees ===
    # -- Basic Tree Algorithms
    {"name": 'Maximum Depth of Binary Tree', "url": 'https://leetcode.com/problems/maximum-depth-of-binary-tree/', "source": 'leetcode', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Easy', "rank": 1.5, "importance": 3},
    {"name": 'Invert Binary Tree', "url": 'https://leetcode.com/problems/invert-binary-tree/', "source": 'leetcode', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Easy', "rank": 1.5, "importance": 3},
    {"name": 'Binary Tree Level Order Traversal', "url": 'https://leetcode.com/problems/binary-tree-level-order-traversal/', "source": 'leetcode', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Timofey and a tree', "url": 'https://codeforces.com/contest/763/problem/A', "source": 'codeforces', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Subordinates', "url": 'https://cses.fi/problemset/task/1674', "source": 'cses', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Even Relation', "url": 'https://atcoder.jp/contests/abc126/tasks/abc126_d', "source": 'atcoder', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Tree Diameter', "url": 'https://cses.fi/problemset/task/1131', "source": 'cses', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Tree Distances I', "url": 'https://cses.fi/problemset/task/1132', "source": 'cses', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Diameter of Binary Tree', "url": 'https://leetcode.com/problems/diameter-of-binary-tree/', "source": 'leetcode', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Validate Binary Search Tree', "url": 'https://leetcode.com/problems/validate-binary-search-tree/', "source": 'leetcode', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Lowest Common Ancestor of a Binary Tree', "url": 'https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/', "source": 'leetcode', "topic": 'Trees & Binary Trees', "subtopic": 'Basic Tree Algorithms', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    # === Tries ===
    {"name": 'Implement Trie (Prefix Tree)', "url": 'https://leetcode.com/problems/implement-trie-prefix-tree/', "source": 'leetcode', "topic": 'Tries', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Maximum XOR of Two Numbers in an Array', "url": 'https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/', "source": 'leetcode', "topic": 'Tries', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Delete Duplicate Folders in System', "url": 'https://leetcode.com/problems/delete-duplicate-folders-in-system/description/', "source": 'leetcode', "topic": 'Tries', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Forbidden Prefix', "url": 'https://atcoder.jp/contests/abc403/tasks/abc403_e', "source": 'atcoder', "topic": 'Tries', "subtopic": '', "difficulty": 'Hard', "rank": 5.5, "importance": 3},
    {"name": 'Good Substrings', "url": 'https://codeforces.com/contest/271/problem/D', "source": 'codeforces', "topic": 'Tries', "subtopic": '', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": "Vasiliy's Multiset", "url": 'https://codeforces.com/contest/706/problem/D', "source": 'codeforces', "topic": 'Tries', "subtopic": '', "difficulty": 'Harder', "rank": 6.0, "importance": 3},
    {"name": 'A Lot of Games', "url": 'https://codeforces.com/contest/455/problem/B', "source": 'codeforces', "topic": 'Tries', "subtopic": '', "difficulty": 'Harder', "rank": 6.5, "importance": 2},
    {"name": 'Design Add and Search Words Data Structure', "url": 'https://leetcode.com/problems/design-add-and-search-words-data-structure/', "source": 'leetcode', "topic": 'Tries', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Word Combinations', "url": 'https://cses.fi/problemset/task/1731', "source": 'cses', "topic": 'Tries', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Karuta', "url": 'https://atcoder.jp/contests/abc287/tasks/abc287_e', "source": 'atcoder', "topic": 'Tries', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Word Search II', "url": 'https://leetcode.com/problems/word-search-ii/', "source": 'leetcode', "topic": 'Tries', "subtopic": '', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    # === Segment Trees ===
    # -- Arbitrary Monoids
    {"name": 'Subarray Sum Queries', "url": 'https://cses.fi/problemset/task/1190', "source": 'cses', "topic": 'Segment Trees', "subtopic": 'Arbitrary Monoids', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Xenia and Bit Operations', "url": 'https://codeforces.com/problemset/problem/339/D', "source": 'codeforces', "topic": 'Segment Trees', "subtopic": 'Arbitrary Monoids', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    # -- Persistent Segment Tree
    {"name": 'Range Queries and Copies', "url": 'https://cses.fi/problemset/task/1737', "source": 'cses', "topic": 'Segment Trees', "subtopic": 'Persistent Segment Tree', "difficulty": 'Harder', "rank": 6.0, "importance": 3},
    # === Sorting ===
    {"name": 'AtCoder Market', "url": 'https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b', "source": 'atcoder', "topic": 'Sorting', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 0},
    {"name": 'The Smallest String Concatenation', "url": 'https://codeforces.com/problemset/problem/632/C', "source": 'codeforces', "topic": 'Sorting', "subtopic": '', "difficulty": 'Hard', "rank": 5.5, "importance": 0},
    {"name": 'Global and Local Inversions', "url": 'https://leetcode.com/problems/global-and-local-inversions/', "source": 'leetcode', "topic": 'Sorting', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Merge Intervals', "url": 'https://leetcode.com/problems/merge-intervals/', "source": 'leetcode', "topic": 'Sorting', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'K-th Not Divisible by n', "url": 'https://codeforces.com/problemset/problem/1352/C', "source": 'codeforces', "topic": 'Sorting', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Guidebook', "url": 'https://atcoder.jp/contests/abc128/tasks/abc128_b', "source": 'atcoder', "topic": 'Sorting', "subtopic": '', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Nested Ranges Check', "url": 'https://cses.fi/problemset/task/2168', "source": 'cses', "topic": 'Sorting', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Restaurant Customers', "url": 'https://cses.fi/problemset/task/1619', "source": 'cses', "topic": 'Sorting', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'Phoenix and Distribution', "url": 'https://codeforces.com/problemset/problem/1348/C', "source": 'codeforces', "topic": 'Sorting', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # === Greedy ===
    {"name": 'Apartments', "url": 'https://cses.fi/problemset/task/1084/', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Ferris Wheel', "url": 'https://cses.fi/problemset/task/1090/', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Movie Festival', "url": 'https://cses.fi/problemset/task/1629', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Missing Coin Sum', "url": 'https://cses.fi/problemset/task/2183/', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Reading Books', "url": 'https://cses.fi/problemset/task/1631/', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 2},
    {"name": 'Tasks and Deadlines', "url": 'https://cses.fi/problemset/task/1630/', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 2},
    {"name": 'Circle of Monsters', "url": 'https://codeforces.com/problemset/problem/1334/C', "source": 'codeforces', "topic": 'Greedy', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Photoshoot', "url": 'https://usaco.org/index.php?page=viewproblem2&cpid=1227', "source": 'usaco', "topic": 'Greedy', "subtopic": '', "difficulty": 'Normal', "rank": 3.0, "importance": 1},
    {"name": 'Race', "url": 'https://usaco.org/index.php?page=viewproblem2&cpid=989', "source": 'usaco', "topic": 'Greedy', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 1},
    {"name": 'Movie Festival II', "url": 'https://cses.fi/problemset/task/1632/', "source": 'cses', "topic": 'Greedy', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    # === DP Level 2 ===
    # -- Range DP
    {"name": 'Removal Game', "url": 'https://cses.fi/problemset/task/1097/', "source": 'cses', "topic": 'DP Level 2', "subtopic": 'Range DP', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    # -- Probability & Expectation DP
    {"name": 'Coins', "url": 'https://atcoder.jp/contests/dp/tasks/dp_i', "source": 'atcoder', "topic": 'DP Level 2', "subtopic": 'Probability & Expectation DP', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    # -- Bitmask DP
    {"name": 'Traveling Salesman among Aerial Cities', "url": 'https://atcoder.jp/contests/abc180/tasks/abc180_e', "source": 'atcoder', "topic": 'DP Level 2', "subtopic": 'Bitmask DP', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    # === DP Level 4 ===
    # -- Knuth's Optimization
    {"name": 'Knuth Division', "url": 'https://cses.fi/problemset/task/2088', "source": 'cses', "topic": 'DP Level 4', "subtopic": "Knuth's Optimization", "difficulty": 'Insane', "rank": 7.0, "importance": 3},
    # === DP Level 1 ===
    # -- DP Fundamentals
    {"name": 'Frog 1', "url": 'https://atcoder.jp/contests/dp/tasks/dp_a', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Removing Digits', "url": 'https://cses.fi/problemset/task/1637/', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'Frog 2', "url": 'https://atcoder.jp/contests/dp/tasks/dp_b', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Hoof Paper Scissors', "url": 'https://usaco.org/index.php?page=viewproblem2&cpid=694', "source": 'usaco', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Mortal Kombat Tower', "url": 'https://codeforces.com/problemset/problem/1418/C', "source": 'codeforces', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Teamwork', "url": 'https://usaco.org/index.php?page=viewproblem2&cpid=863', "source": 'usaco', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Dice Combinations', "url": 'https://cses.fi/problemset/task/1633', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Boredom', "url": 'https://codeforces.com/problemset/problem/455/A', "source": 'codeforces', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Vacation', "url": 'https://atcoder.jp/contests/dp/tasks/dp_c', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Basketball Exercise', "url": 'https://codeforces.com/problemset/problem/1195/C', "source": 'codeforces', "topic": 'DP Level 1', "subtopic": 'DP Fundamentals', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    # -- DP on Grids
    {"name": 'Grid 1', "url": 'https://atcoder.jp/contests/dp/tasks/dp_h', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Edit Distance', "url": 'https://cses.fi/problemset/task/1639', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Longest Common Subsequence', "url": 'https://cses.fi/problemset/task/3403/', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'LCS', "url": 'https://atcoder.jp/contests/dp/tasks/dp_f', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Minimum Path Sum', "url": 'https://leetcode.com/problems/minimum-path-sum/', "source": 'leetcode', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Easy+', "rank": 2.5, "importance": 2},
    {"name": 'Grid Paths', "url": 'https://cses.fi/problemset/task/1638', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Triangle', "url": 'https://leetcode.com/problems/triangle/', "source": 'leetcode', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Minimum Falling Path Sum', "url": 'https://leetcode.com/problems/minimum-falling-path-sum/', "source": 'leetcode', "topic": 'DP Level 1', "subtopic": 'DP on Grids', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # -- DP on DAG
    {"name": 'Longest Path', "url": 'https://atcoder.jp/contests/dp/tasks/dp_g', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'DP on DAG', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Game Routes', "url": 'https://cses.fi/problemset/task/1681', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP on DAG', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Longest Flight Route', "url": 'https://cses.fi/problemset/task/1680', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'DP on DAG', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    # -- Additional Practice
    {"name": 'Rectangle Cutting', "url": 'https://cses.fi/problemset/task/1744', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Additional Practice', "difficulty": 'Normal', "rank": 3.0, "importance": 1},
    {"name": 'Flowers', "url": 'https://codeforces.com/contest/474/problem/D', "source": 'codeforces', "topic": 'DP Level 1', "subtopic": 'Additional Practice', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Beautiful Array', "url": 'https://codeforces.com/problemset/problem/1155/D', "source": 'codeforces', "topic": 'DP Level 1', "subtopic": 'Additional Practice', "difficulty": 'Harder', "rank": 6.5, "importance": 2},
    {"name": 'Counting Towers', "url": 'https://cses.fi/problemset/task/2413', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Additional Practice', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    # -- Knapsack DP
    {"name": 'Coin Combination I', "url": 'https://cses.fi/problemset/task/1635', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Coin Combinations II', "url": 'https://cses.fi/problemset/task/1636', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Knapsack 1', "url": 'https://atcoder.jp/contests/dp/tasks/dp_d', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Knapsack 2', "url": 'https://atcoder.jp/contests/dp/tasks/dp_e', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Candies', "url": 'https://atcoder.jp/contests/dp/tasks/dp_m', "source": 'atcoder', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Book Shop', "url": 'https://cses.fi/problemset/task/1158', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Money Sums', "url": 'https://cses.fi/problemset/task/1745', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Book Shop II', "url": 'https://cses.fi/problemset/task/1159', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Minimizing Coins', "url": 'https://cses.fi/problemset/task/1634', "source": 'cses', "topic": 'DP Level 1', "subtopic": 'Knapsack DP', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    # === Bitwise Operations ===
    {"name": 'Single Number', "url": 'https://leetcode.com/problems/single-number/', "source": 'leetcode', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Number of 1 Bits', "url": 'https://leetcode.com/problems/number-of-1-bits/', "source": 'leetcode', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Easy', "rank": 1.0, "importance": 3},
    {"name": 'Counting Bits', "url": 'https://leetcode.com/problems/counting-bits/', "source": 'leetcode', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Vitamins', "url": 'https://codeforces.com/problemset/problem/1042/B', "source": 'codeforces', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Range Xor Queries', "url": 'https://cses.fi/problemset/task/1650', "source": 'cses', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Bitwise AND of Numbers Range', "url": 'https://leetcode.com/problems/bitwise-and-of-numbers-range/', "source": 'leetcode', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Normal', "rank": 3.5, "importance": 3},
    {"name": 'Single Number II', "url": 'https://leetcode.com/problems/single-number-ii/', "source": 'leetcode', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Popcount and XOR', "url": 'https://atcoder.jp/contests/abc347/tasks/abc347_d', "source": 'atcoder', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 3},
    {"name": 'Little Girl and Maximum XOR', "url": 'https://codeforces.com/problemset/problem/276/D', "source": 'codeforces', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Hard', "rank": 5.5, "importance": 3},
    {"name": 'The Brand New Function', "url": 'https://codeforces.com/contest/243/problem/A', "source": 'codeforces', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 3},
    {"name": 'Bits', "url": 'https://codeforces.com/contest/484/problem/A', "source": 'codeforces', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Xor Sigma Problem', "url": 'https://atcoder.jp/contests/abc365/tasks/abc365_e', "source": 'atcoder', "topic": 'Bitwise Operations', "subtopic": '', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    # === Basic Strings ===
    # -- Hashing
    {"name": 'Repeating Substring', "url": 'https://cses.fi/problemset/task/2106', "source": 'cses', "topic": 'Basic Strings', "subtopic": 'Hashing', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'Watto and Mechanism', "url": 'https://codeforces.com/problemset/problem/514/C', "source": 'codeforces', "topic": 'Basic Strings', "subtopic": 'Hashing', "difficulty": 'Insane', "rank": 7.0, "importance": 2},
    {"name": 'ABCBAC', "url": 'https://atcoder.jp/contests/abc284/tasks/abc284_f', "source": 'atcoder', "topic": 'Basic Strings', "subtopic": 'Hashing', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'Who Says a Pun?', "url": 'https://atcoder.jp/contests/abc141/tasks/abc141_e', "source": 'atcoder', "topic": 'Basic Strings', "subtopic": 'Hashing', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # -- KMP Algorithm
    {"name": 'String Matching', "url": 'https://cses.fi/problemset/task/1753', "source": 'cses', "topic": 'Basic Strings', "subtopic": 'KMP Algorithm', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    # === Math Level 1 ===
    # -- Primes & Sieve
    {"name": 'Count Primes', "url": 'https://leetcode.com/problems/count-primes/', "source": 'leetcode', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Almost Prime', "url": 'https://codeforces.com/problemset/problem/26/A', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'T-primes', "url": 'https://codeforces.com/problemset/problem/230/B', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Counting Divisors', "url": 'https://cses.fi/problemset/task/1713', "source": 'cses', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Sherlock and his girlfriend', "url": 'https://codeforces.com/problemset/problem/776/B', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    {"name": 'Happy New Year 2023', "url": 'https://atcoder.jp/contests/abc284/tasks/abc284_d', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Div Game', "url": 'https://atcoder.jp/contests/abc169/tasks/abc169_d', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Digits in Multiplication', "url": 'https://atcoder.jp/contests/abc057/tasks/abc057_c', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Primes & Sieve', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    # -- Modular Arithmetic
    {"name": 'Exponentiation', "url": 'https://cses.fi/problemset/task/1095', "source": 'cses', "topic": 'Math Level 1', "subtopic": 'Modular Arithmetic', "difficulty": 'Easy+', "rank": 2.0, "importance": 3},
    {"name": 'Exponentiation II', "url": 'https://cses.fi/problemset/task/1712', "source": 'cses', "topic": 'Math Level 1', "subtopic": 'Modular Arithmetic', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    # -- GCD & LCM
    {"name": 'Monster Battle Royale', "url": 'https://atcoder.jp/contests/abc118/tasks/abc118_c', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Easy', "rank": 1.5, "importance": 3},
    {"name": 'Multiple Clocks', "url": 'https://atcoder.jp/contests/abc070/tasks/abc070_c', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'Common Divisors', "url": 'https://cses.fi/problemset/task/1081', "source": 'cses', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Easy+', "rank": 2.5, "importance": 3},
    {"name": 'Skip', "url": 'https://atcoder.jp/contests/abc109/tasks/abc109_c', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Common Divisors', "url": 'https://codeforces.com/problemset/problem/1203/C', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Fadi and LCM', "url": 'https://codeforces.com/problemset/problem/1285/C', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Diluc and Kaeya', "url": 'https://codeforces.com/problemset/problem/1536/C', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'GCD & LCM', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    # -- Pigeonhole Principle
    {"name": 'CopyCopyCopyCopyCopy', "url": 'https://codeforces.com/problemset/problem/1325/B', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Easy', "rank": 1.0, "importance": 2},
    {"name": 'Subarray Sums Divisible by K', "url": 'https://leetcode.com/problems/subarray-sums-divisible-by-k/', "source": 'leetcode', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Find the Duplicate Number', "url": 'https://leetcode.com/problems/find-the-duplicate-number/', "source": 'leetcode', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Kuroni and Impossible Calculation', "url": 'https://codeforces.com/problemset/problem/1305/C', "source": 'codeforces', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Hard', "rank": 5.0, "importance": 3},
    {"name": 'Maximum Gap', "url": 'https://leetcode.com/problems/maximum-gap/', "source": 'leetcode', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Happy Birthday! 2', "url": 'https://atcoder.jp/contests/abc200/tasks/abc200_d', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Harder', "rank": 6.0, "importance": 3},
    {"name": 'Multiple of 2019', "url": 'https://atcoder.jp/contests/abc164/tasks/abc164_d', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'Sequence Sum', "url": 'https://atcoder.jp/contests/abc179/tasks/abc179_e', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Pigeonhole Principle', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    # -- Additional Practice
    {"name": 'Div Game', "url": 'https://atcoder.jp/contests/abc169/tasks/abc169_d', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Additional Practice', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Flatten', "url": 'https://atcoder.jp/contests/abc152/tasks/abc152_e', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Additional Practice', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Dice and Coin', "url": 'https://atcoder.jp/contests/abc126/tasks/abc126_c', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Additional Practice', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    {"name": 'abc285_brutmhyhiizp', "url": 'https://atcoder.jp/contests/abc285/tasks/abc285_c', "source": 'atcoder', "topic": 'Math Level 1', "subtopic": 'Additional Practice', "difficulty": 'Easy+', "rank": 2.0, "importance": 2},
    # === Math Level 2 ===
    # -- Combinatorics
    {"name": 'Binomial Coefficients', "url": 'https://cses.fi/problemset/task/1079', "source": 'cses', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Distributing Apples', "url": 'https://cses.fi/problemset/task/1716', "source": 'cses', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Normal', "rank": 3.0, "importance": 3},
    {"name": 'Bracket Sequences I', "url": 'https://cses.fi/problemset/task/2064', "source": 'cses', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    {"name": 'Creating Strings II', "url": 'https://cses.fi/problemset/task/1715', "source": 'cses', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Normal+', "rank": 4.0, "importance": 3},
    {"name": 'Count the Arrays', "url": 'https://codeforces.com/problemset/problem/1312/D', "source": 'codeforces', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Hard', "rank": 5.5, "importance": 2},
    {"name": 'Colorful Blocks', "url": 'https://atcoder.jp/contests/abc167/tasks/abc167_e', "source": 'atcoder', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Beautiful Numbers', "url": 'https://codeforces.com/problemset/problem/300/C', "source": 'codeforces', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'One Time Swap', "url": 'https://atcoder.jp/contests/abc345/tasks/abc345_c', "source": 'atcoder', "topic": 'Math Level 2', "subtopic": 'Combinatorics', "difficulty": 'Normal', "rank": 3.0, "importance": 2},
    # -- Additional Practice
    {"name": 'Steps to One', "url": 'https://codeforces.com/problemset/problem/1139/D', "source": 'codeforces', "topic": 'Math Level 2', "subtopic": 'Additional Practice', "difficulty": 'Expert', "rank": 8.5, "importance": 2},
    {"name": 'Jzzhu and Numbers', "url": 'https://codeforces.com/problemset/problem/449/D', "source": 'codeforces', "topic": 'Math Level 2', "subtopic": 'Additional Practice', "difficulty": 'Master', "rank": 9.0, "importance": 2},
    # === Ad-hoc ===
    {"name": 'Dominated Subarray', "url": 'https://codeforces.com/problemset/problem/1257/C', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Normal', "rank": 3.5, "importance": 2},
    {"name": 'Interesting Story', "url": 'https://codeforces.com/problemset/problem/1551/C', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Normal+', "rank": 4.0, "importance": 2},
    {"name": 'Prefix Flip (Easy Version)', "url": 'https://codeforces.com/problemset/problem/1381/A1', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Prefix Flip (Hard Version)', "url": 'https://codeforces.com/problemset/problem/1381/A2', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Insane', "rank": 7.0, "importance": 2},
    {"name": 'Dual (Easy Version)', "url": 'https://codeforces.com/problemset/problem/1854/A1', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
    {"name": 'Dual (Hard Version)', "url": 'https://codeforces.com/problemset/problem/1854/A2', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'Balance the Bits', "url": 'https://codeforces.com/problemset/problem/1503/A', "source": 'codeforces', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Harder', "rank": 6.0, "importance": 2},
    {"name": 'FEB', "url": 'http://www.usaco.org/index.php?page=viewproblem2&cpid=1323', "source": 'usaco', "topic": 'Ad-hoc', "subtopic": '', "difficulty": 'Normal+', "rank": 4.5, "importance": 2},
    # === Constructive Algorithms ===
    {"name": 'Matching Numbers', "url": 'https://codeforces.com/problemset/problem/1788/C', "source": 'codeforces', "topic": 'Constructive Algorithms', "subtopic": '', "difficulty": 'Hard', "rank": 5.0, "importance": 2},
]
