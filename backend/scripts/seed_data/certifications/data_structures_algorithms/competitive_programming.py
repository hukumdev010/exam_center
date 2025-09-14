"""Competitive Programming Certification"""

CERTIFICATION = {
    "name": "Competitive Programming",
    "description": "Problem-solving skills for coding competitions and technical interviews",
    "slug": "competitive-programming",
    "level": "Expert",
    "duration": 81,
    "questions_count": 27,
    "category_slug": "data-structures-algorithms",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the time complexity of finding the Longest Common Subsequence using dynamic programming?",
        "explanation": "The LCS problem using DP has a time complexity of O(m*n) where m and n are the lengths of the two sequences.",
        "reference": "https://en.wikipedia.org/wiki/Longest_common_subsequence_problem",
        "points": 1,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(m * n)", "is_correct": True},
            {"text": "O(2^n)", "is_correct": False},
        ],
    },
    {
        "text": "Which technique is most effective for solving problems with optimal substructure?",
        "explanation": "Dynamic programming is ideal for problems that exhibit optimal substructure and overlapping subproblems.",
        "reference": "https://en.wikipedia.org/wiki/Optimal_substructure",
        "points": 1,
        "answers": [
            {"text": "Greedy algorithms", "is_correct": False},
            {"text": "Dynamic programming", "is_correct": True},
            {"text": "Backtracking", "is_correct": False},
            {"text": "Branch and bound", "is_correct": False},
        ],
    },
    {
        "text": "What will this TypeScript implementation of Kadane's algorithm output for the given array?\n\n```typescript\nfunction maxSubArray(nums: number[]): number {\n    let maxSoFar = nums[0];\n    let maxEndingHere = nums[0];\n    \n    for (let i = 1; i < nums.length; i++) {\n        maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]);\n        maxSoFar = Math.max(maxSoFar, maxEndingHere);\n    }\n    \n    return maxSoFar;\n}\n\nconst arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4];\nconsole.log(maxSubArray(arr));\n```",
        "explanation": "Kadane's algorithm finds the maximum sum subarray. For [-2, 1, -3, 4, -1, 2, 1, -5, 4], the maximum subarray is [4, -1, 2, 1] with sum 6.",
        "reference": "https://en.wikipedia.org/wiki/Maximum_subarray_problem",
        "points": 2,
        "answers": [
            {"text": "6", "is_correct": True},
            {"text": "4", "is_correct": False},
            {"text": "7", "is_correct": False},
            {"text": "1", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the coin change problem using dynamic programming?",
        "explanation": "The coin change DP solution builds up the minimum coins needed for each amount from 1 to the target amount.",
        "reference": "https://en.wikipedia.org/wiki/Change-making_problem",
        "points": 3,
        "answers": [
            {
                "text": "function coinChange(coins: number[], amount: number): number {\n    const dp = new Array(amount + 1).fill(Infinity);\n    dp[0] = 0;\n    \n    for (let i = 1; i <= amount; i++) {\n        for (const coin of coins) {\n            if (coin <= i) {\n                dp[i] = Math.min(dp[i], dp[i - coin] + 1);\n            }\n        }\n    }\n    \n    return dp[amount] === Infinity ? -1 : dp[amount];\n}",
                "is_correct": True,
            },
            {
                "text": "function coinChange(coins: number[], amount: number): number {\n    return coins.filter(coin => coin <= amount).length;\n}",
                "is_correct": False,
            },
            {
                "text": "function coinChange(coins: number[], amount: number): number {\n    return Math.floor(amount / Math.min(...coins));\n}",
                "is_correct": False,
            },
            {
                "text": "function coinChange(coins: number[], amount: number): number {\n    let count = 0;\n    for (const coin of coins.sort((a, b) => b - a)) {\n        count += Math.floor(amount / coin);\n        amount %= coin;\n    }\n    return amount === 0 ? count : -1;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the output of this TypeScript backtracking solution for N-Queens problem?\n\n```typescript\nfunction solveNQueens(n: number): string[][] {\n    const result: string[][] = [];\n    const board: string[][] = Array(n).fill(null).map(() => Array(n).fill('.'));\n    \n    const isValid = (row: number, col: number): boolean => {\n        // Check column\n        for (let i = 0; i < row; i++) {\n            if (board[i][col] === 'Q') return False;\n        }\n        \n        // Check diagonal\n        for (let i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {\n            if (board[i][j] === 'Q') return False;\n        }\n        \n        // Check anti-diagonal\n        for (let i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {\n            if (board[i][j] === 'Q') return False;\n        }\n        \n        return True;\n    };\n    \n    const backtrack = (row: number): void => {\n        if (row === n) {\n            result.push(board.map(r => r.join('')));\n            return;\n        }\n        \n        for (let col = 0; col < n; col++) {\n            if (isValid(row, col)) {\n                board[row][col] = 'Q';\n                backtrack(row + 1);\n                board[row][col] = '.';\n            }\n        }\n    };\n    \n    backtrack(0);\n    return result;\n}\n\nconsole.log(solveNQueens(4).length);\n```",
        "explanation": "For a 4x4 board, there are exactly 2 valid solutions to place 4 queens such that none attack each other.",
        "reference": "https://en.wikipedia.org/wiki/Eight_queens_puzzle",
        "points": 3,
        "answers": [
            {"text": "2", "is_correct": True},
            {"text": "1", "is_correct": False},
            {"text": "4", "is_correct": False},
            {"text": "0", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly finds the Longest Increasing Subsequence (LIS)?",
        "explanation": "The optimal LIS solution uses binary search with a patience-sorting approach to achieve O(n log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Longest_increasing_subsequence",
        "points": 3,
        "answers": [
            {
                "text": "function lengthOfLIS(nums: number[]): number {\n    const tails: number[] = [];\n    \n    for (const num of nums) {\n        let left = 0, right = tails.length;\n        \n        while (left < right) {\n            const mid = Math.floor((left + right) / 2);\n            if (tails[mid] < num) {\n                left = mid + 1;\n            } else {\n                right = mid;\n            }\n        }\n        \n        if (left === tails.length) {\n            tails.push(num);\n        } else {\n            tails[left] = num;\n        }\n    }\n    \n    return tails.length;\n}",
                "is_correct": True,
            },
            {
                "text": "function lengthOfLIS(nums: number[]): number {\n    return nums.filter((num, i) => i === 0 || num > nums[i-1]).length;\n}",
                "is_correct": False,
            },
            {
                "text": "function lengthOfLIS(nums: number[]): number {\n    const dp = new Array(nums.length).fill(1);\n    for (let i = 1; i < nums.length; i++) {\n        if (nums[i] > nums[i-1]) dp[i] = dp[i-1] + 1;\n    }\n    return Math.max(...dp);\n}",
                "is_correct": False,
            },
            {
                "text": "function lengthOfLIS(nums: number[]): number {\n    return new Set(nums.sort((a, b) => a - b)).size;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript Dijkstra's algorithm implementation output?\n\n```typescript\nclass PriorityQueue {\n    private heap: [number, number][] = [];\n    \n    enqueue(priority: number, value: number): void {\n        this.heap.push([priority, value]);\n        this.heapifyUp(this.heap.length - 1);\n    }\n    \n    dequeue(): [number, number] | undefined {\n        if (this.heap.length === 0) return undefined;\n        if (this.heap.length === 1) return this.heap.pop();\n        \n        const result = this.heap[0];\n        this.heap[0] = this.heap.pop()!;\n        this.heapifyDown(0);\n        return result;\n    }\n    \n    private heapifyUp(index: number): void {\n        const parent = Math.floor((index - 1) / 2);\n        if (parent >= 0 && this.heap[parent][0] > this.heap[index][0]) {\n            [this.heap[parent], this.heap[index]] = [this.heap[index], this.heap[parent]];\n            this.heapifyUp(parent);\n        }\n    }\n    \n    private heapifyDown(index: number): void {\n        const left = 2 * index + 1;\n        const right = 2 * index + 2;\n        let smallest = index;\n        \n        if (left < this.heap.length && this.heap[left][0] < this.heap[smallest][0]) {\n            smallest = left;\n        }\n        if (right < this.heap.length && this.heap[right][0] < this.heap[smallest][0]) {\n            smallest = right;\n        }\n        \n        if (smallest !== index) {\n            [this.heap[index], this.heap[smallest]] = [this.heap[smallest], this.heap[index]];\n            this.heapifyDown(smallest);\n        }\n    }\n    \n    isEmpty(): boolean {\n        return this.heap.length === 0;\n    }\n}\n\nfunction dijkstra(graph: number[][], start: number): number[] {\n    const n = graph.length;\n    const dist = new Array(n).fill(Infinity);\n    const pq = new PriorityQueue();\n    \n    dist[start] = 0;\n    pq.enqueue(0, start);\n    \n    while (!pq.isEmpty()) {\n        const [d, u] = pq.dequeue()!;\n        \n        if (d > dist[u]) continue;\n        \n        for (let v = 0; v < n; v++) {\n            if (graph[u][v] > 0) {\n                const newDist = dist[u] + graph[u][v];\n                if (newDist < dist[v]) {\n                    dist[v] = newDist;\n                    pq.enqueue(newDist, v);\n                }\n            }\n        }\n    }\n    \n    return dist;\n}\n\nconst graph = [\n    [0, 4, 0, 0, 0, 0, 0, 8, 0],\n    [4, 0, 8, 0, 0, 0, 0, 11, 0],\n    [0, 8, 0, 7, 0, 4, 0, 0, 2],\n    [0, 0, 7, 0, 9, 14, 0, 0, 0],\n    [0, 0, 0, 9, 0, 10, 0, 0, 0],\n    [0, 0, 4, 14, 10, 0, 2, 0, 0],\n    [0, 0, 0, 0, 0, 2, 0, 1, 6],\n    [8, 11, 0, 0, 0, 0, 1, 0, 7],\n    [0, 0, 2, 0, 0, 0, 6, 7, 0]\n];\n\nconsole.log(dijkstra(graph, 0)[4]);\n```",
        "explanation": "Dijkstra's algorithm finds shortest path from node 0 to node 4. The shortest distance is 21 (0→7→6→5→4).",
        "reference": "https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm",
        "points": 4,
        "answers": [
            {"text": "21", "is_correct": True},
            {"text": "20", "is_correct": False},
            {"text": "19", "is_correct": False},
            {"text": "22", "is_correct": False},
        ],
    },
    {
        "text": "What is the time complexity of this TypeScript Union-Find implementation?\n\n```typescript\nclass UnionFind {\n    private parent: number[];\n    private rank: number[];\n    \n    constructor(n: number) {\n        this.parent = Array.from({length: n}, (_, i) => i);\n        this.rank = new Array(n).fill(0);\n    }\n    \n    find(x: number): number {\n        if (this.parent[x] !== x) {\n            this.parent[x] = this.find(this.parent[x]); // Path compression\n        }\n        return this.parent[x];\n    }\n    \n    union(x: number, y: number): boolean {\n        const rootX = this.find(x);\n        const rootY = this.find(y);\n        \n        if (rootX === rootY) return False;\n        \n        // Union by rank\n        if (this.rank[rootX] < this.rank[rootY]) {\n            this.parent[rootX] = rootY;\n        } else if (this.rank[rootX] > this.rank[rootY]) {\n            this.parent[rootY] = rootX;\n        } else {\n            this.parent[rootY] = rootX;\n            this.rank[rootX]++;\n        }\n        \n        return True;\n    }\n}\n```",
        "explanation": "Union-Find with path compression and union by rank has nearly constant amortized time complexity O(α(n)) where α is the inverse Ackermann function.",
        "reference": "https://en.wikipedia.org/wiki/Disjoint-set_data_structure",
        "points": 2,
        "answers": [
            {"text": "O(α(n)) amortized", "is_correct": True},
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the 0/1 Knapsack problem?",
        "explanation": "The 0/1 Knapsack problem requires dynamic programming where each item can either be included or excluded.",
        "reference": "https://en.wikipedia.org/wiki/Knapsack_problem",
        "points": 3,
        "answers": [
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number {\n    const n = weights.length;\n    const dp = Array(n + 1).fill(null).map(() => Array(capacity + 1).fill(0));\n    \n    for (let i = 1; i <= n; i++) {\n        for (let w = 1; w <= capacity; w++) {\n            if (weights[i - 1] <= w) {\n                dp[i][w] = Math.max(\n                    dp[i - 1][w],\n                    dp[i - 1][w - weights[i - 1]] + values[i - 1]\n                );\n            } else {\n                dp[i][w] = dp[i - 1][w];\n            }\n        }\n    }\n    \n    return dp[n][capacity];\n}",
                "is_correct": True,
            },
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number {\n    return values.reduce((sum, val) => sum + val, 0);\n}",
                "is_correct": False,
            },
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number {\n    const items = weights.map((w, i) => ({w, v: values[i], ratio: values[i]/w}));\n    items.sort((a, b) => b.ratio - a.ratio);\n    \n    let totalValue = 0, totalWeight = 0;\n    for (const item of items) {\n        if (totalWeight + item.w <= capacity) {\n            totalValue += item.v;\n            totalWeight += item.w;\n        }\n    }\n    return totalValue;\n}",
                "is_correct": False,
            },
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number {\n    return Math.max(...values);\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript segment tree implementation output?\n\n```typescript\nclass SegmentTree {\n    private tree: number[];\n    private n: number;\n    \n    constructor(arr: number[]) {\n        this.n = arr.length;\n        this.tree = new Array(4 * this.n);\n        this.build(arr, 0, 0, this.n - 1);\n    }\n    \n    private build(arr: number[], node: number, start: number, end: number): void {\n        if (start === end) {\n            this.tree[node] = arr[start];\n        } else {\n            const mid = Math.floor((start + end) / 2);\n            this.build(arr, 2 * node + 1, start, mid);\n            this.build(arr, 2 * node + 2, mid + 1, end);\n            this.tree[node] = this.tree[2 * node + 1] + this.tree[2 * node + 2];\n        }\n    }\n    \n    query(l: number, r: number): number {\n        return this.queryUtil(0, 0, this.n - 1, l, r);\n    }\n    \n    private queryUtil(node: number, start: number, end: number, l: number, r: number): number {\n        if (r < start || end < l) return 0;\n        if (l <= start && end <= r) return this.tree[node];\n        \n        const mid = Math.floor((start + end) / 2);\n        return this.queryUtil(2 * node + 1, start, mid, l, r) +\n               this.queryUtil(2 * node + 2, mid + 1, end, l, r);\n    }\n}\n\nconst arr = [1, 3, 5, 7, 9, 11];\nconst segTree = new SegmentTree(arr);\nconsole.log(segTree.query(1, 3));\n```",
        "explanation": "Segment tree range sum query from index 1 to 3: arr[1] + arr[2] + arr[3] = 3 + 5 + 7 = 15.",
        "reference": "https://en.wikipedia.org/wiki/Segment_tree",
        "points": 3,
        "answers": [
            {"text": "15", "is_correct": True},
            {"text": "16", "is_correct": False},
            {"text": "12", "is_correct": False},
            {"text": "18", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly finds all permutations of a string?",
        "explanation": "Generating permutations requires backtracking to try all possible arrangements of characters.",
        "reference": "https://en.wikipedia.org/wiki/Permutation",
        "points": 3,
        "answers": [
            {
                "text": "function permute(s: string): string[] {\n    const result: string[] = [];\n    const chars = s.split('');\n    \n    const backtrack = (current: string[], remaining: string[]): void => {\n        if (remaining.length === 0) {\n            result.push(current.join(''));\n            return;\n        }\n        \n        for (let i = 0; i < remaining.length; i++) {\n            const char = remaining[i];\n            current.push(char);\n            const newRemaining = [...remaining.slice(0, i), ...remaining.slice(i + 1)];\n            backtrack(current, newRemaining);\n            current.pop();\n        }\n    };\n    \n    backtrack([], chars);\n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function permute(s: string): string[] {\n    return s.split('').sort().join('').split('');\n}",
                "is_correct": False,
            },
            {
                "text": "function permute(s: string): string[] {\n    const result = [];\n    for (let i = 0; i < s.length; i++) {\n        result.push(s.slice(i) + s.slice(0, i));\n    }\n    return result;\n}",
                "is_correct": False,
            },
            {
                "text": "function permute(s: string): string[] {\n    return [s, s.split('').reverse().join('')];\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the output of this TypeScript implementation for finding edit distance (Levenshtein distance)?\n\n```typescript\nfunction editDistance(str1: string, str2: string): number {\n    const m = str1.length;\n    const n = str2.length;\n    const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));\n    \n    // Initialize base cases\n    for (let i = 0; i <= m; i++) dp[i][0] = i;\n    for (let j = 0; j <= n; j++) dp[0][j] = j;\n    \n    for (let i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n            if (str1[i - 1] === str2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1];\n            } else {\n                dp[i][j] = 1 + Math.min(\n                    dp[i - 1][j],    // deletion\n                    dp[i][j - 1],    // insertion\n                    dp[i - 1][j - 1] // substitution\n                );\n            }\n        }\n    }\n    \n    return dp[m][n];\n}\n\nconsole.log(editDistance('kitten', 'sitting'));\n```",
        "explanation": "Edit distance between 'kitten' and 'sitting' is 3: substitute k→s, substitute e→i, insert g.",
        "reference": "https://en.wikipedia.org/wiki/Edit_distance",
        "points": 3,
        "answers": [
            {"text": "3", "is_correct": True},
            {"text": "2", "is_correct": False},
            {"text": "4", "is_correct": False},
            {"text": "5", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Traveling Salesman Problem using dynamic programming with bitmask?",
        "explanation": "TSP with DP uses bitmask to represent visited cities and memoization to avoid recomputing subproblems.",
        "reference": "https://en.wikipedia.org/wiki/Travelling_salesman_problem",
        "points": 4,
        "answers": [
            {
                "text": "function tsp(dist: number[][]): number {\n    const n = dist.length;\n    const dp = Array(1 << n).fill(null).map(() => Array(n).fill(Infinity));\n    dp[1][0] = 0; // Start from city 0\n    \n    for (let mask = 0; mask < (1 << n); mask++) {\n        for (let u = 0; u < n; u++) {\n            if (!(mask & (1 << u))) continue;\n            \n            for (let v = 0; v < n; v++) {\n                if (mask & (1 << v)) continue;\n                \n                const newMask = mask | (1 << v);\n                dp[newMask][v] = Math.min(dp[newMask][v], dp[mask][u] + dist[u][v]);\n            }\n        }\n    }\n    \n    let result = Infinity;\n    for (let i = 1; i < n; i++) {\n        result = Math.min(result, dp[(1 << n) - 1][i] + dist[i][0]);\n    }\n    \n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function tsp(dist: number[][]): number {\n    const n = dist.length;\n    let minCost = Infinity;\n    \n    function permute(cities: number[], index: number): void {\n        if (index === cities.length) {\n            let cost = 0;\n            for (let i = 0; i < n - 1; i++) {\n                cost += dist[cities[i]][cities[i + 1]];\n            }\n            cost += dist[cities[n - 1]][cities[0]];\n            minCost = Math.min(minCost, cost);\n            return;\n        }\n        \n        for (let i = index; i < cities.length; i++) {\n            [cities[index], cities[i]] = [cities[i], cities[index]];\n            permute(cities, index + 1);\n            [cities[index], cities[i]] = [cities[i], cities[index]];\n        }\n    }\n    \n    permute(Array.from({length: n}, (_, i) => i), 0);\n    return minCost;\n}",
                "is_correct": False,
            },
            {
                "text": "function tsp(dist: number[][]): number {\n    return dist.flat().reduce((sum, val) => sum + val, 0);\n}",
                "is_correct": False,
            },
            {
                "text": "function tsp(dist: number[][]): number {\n    const n = dist.length;\n    let totalCost = 0;\n    let currentCity = 0;\n    const visited = new Set([0]);\n    \n    while (visited.size < n) {\n        let minDist = Infinity;\n        let nextCity = -1;\n        \n        for (let i = 0; i < n; i++) {\n            if (!visited.has(i) && dist[currentCity][i] < minDist) {\n                minDist = dist[currentCity][i];\n                nextCity = i;\n            }\n        }\n        \n        totalCost += minDist;\n        visited.add(nextCity);\n        currentCity = nextCity;\n    }\n    \n    return totalCost + dist[currentCity][0];\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript KMP (Knuth-Morris-Pratt) string matching algorithm output?\n\n```typescript\nfunction kmpSearch(text: string, pattern: string): number[] {\n    const positions: number[] = [];\n    const lps = computeLPS(pattern);\n    \n    let i = 0; // index for text\n    let j = 0; // index for pattern\n    \n    while (i < text.length) {\n        if (pattern[j] === text[i]) {\n            i++;\n            j++;\n        }\n        \n        if (j === pattern.length) {\n            positions.push(i - j);\n            j = lps[j - 1];\n        } else if (i < text.length && pattern[j] !== text[i]) {\n            if (j !== 0) {\n                j = lps[j - 1];\n            } else {\n                i++;\n            }\n        }\n    }\n    \n    return positions;\n}\n\nfunction computeLPS(pattern: string): number[] {\n    const lps = new Array(pattern.length).fill(0);\n    let len = 0;\n    let i = 1;\n    \n    while (i < pattern.length) {\n        if (pattern[i] === pattern[len]) {\n            len++;\n            lps[i] = len;\n            i++;\n        } else {\n            if (len !== 0) {\n                len = lps[len - 1];\n            } else {\n                lps[i] = 0;\n                i++;\n            }\n        }\n    }\n    \n    return lps;\n}\n\nconst text = 'ABABDABACDABABCABCABCABCABC';\nconst pattern = 'ABABCABCAB';\nconsole.log(kmpSearch(text, pattern));\n```",
        "explanation": "KMP finds pattern 'ABABCABCAB' in text. The pattern appears starting at index 15 in the given text.",
        "reference": "https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm",
        "points": 4,
        "answers": [
            {"text": "[15]", "is_correct": True},
            {"text": "[10]", "is_correct": False},
            {"text": "[12]", "is_correct": False},
            {"text": "[]", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Maximum Flow problem using Ford-Fulkerson algorithm?",
        "explanation": "Ford-Fulkerson algorithm finds maximum flow by repeatedly finding augmenting paths and updating residual capacities.",
        "reference": "https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm",
        "points": 4,
        "answers": [
            {
                "text": "function maxFlow(capacity: number[][], source: number, sink: number): number {\n    const n = capacity.length;\n    const residual = capacity.map(row => [...row]);\n    let maxFlowValue = 0;\n    \n    const bfs = (): number[] | null => {\n        const visited = new Array(n).fill(False);\n        const parent = new Array(n).fill(-1);\n        const queue = [source];\n        visited[source] = True;\n        \n        while (queue.length > 0) {\n            const u = queue.shift()!;\n            \n            for (let v = 0; v < n; v++) {\n                if (!visited[v] && residual[u][v] > 0) {\n                    visited[v] = True;\n                    parent[v] = u;\n                    queue.push(v);\n                    \n                    if (v === sink) {\n                        return parent;\n                    }\n                }\n            }\n        }\n        \n        return null;\n    };\n    \n    let parent = bfs();\n    while (parent !== null) {\n        let pathFlow = Infinity;\n        \n        // Find minimum capacity along the path\n        for (let v = sink; v !== source; v = parent[v]) {\n            const u = parent[v];\n            pathFlow = Math.min(pathFlow, residual[u][v]);\n        }\n        \n        // Update residual capacities\n        for (let v = sink; v !== source; v = parent[v]) {\n            const u = parent[v];\n            residual[u][v] -= pathFlow;\n            residual[v][u] += pathFlow;\n        }\n        \n        maxFlowValue += pathFlow;\n        parent = bfs();\n    }\n    \n    return maxFlowValue;\n}",
                "is_correct": True,
            },
            {
                "text": "function maxFlow(capacity: number[][], source: number, sink: number): number {\n    return capacity[source][sink];\n}",
                "is_correct": False,
            },
            {
                "text": "function maxFlow(capacity: number[][], source: number, sink: number): number {\n    let flow = 0;\n    for (let i = 0; i < capacity.length; i++) {\n        flow += capacity[source][i];\n    }\n    return flow;\n}",
                "is_correct": False,
            },
            {
                "text": "function maxFlow(capacity: number[][], source: number, sink: number): number {\n    return Math.min(...capacity[source].filter(c => c > 0));\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of this TypeScript Z-algorithm implementation for string matching?\n\n```typescript\nfunction zAlgorithm(s: string): number[] {\n    const n = s.length;\n    const z = new Array(n).fill(0);\n    let l = 0, r = 0;\n    \n    for (let i = 1; i < n; i++) {\n        if (i <= r) {\n            z[i] = Math.min(r - i + 1, z[i - l]);\n        }\n        \n        while (i + z[i] < n && s[z[i]] === s[i + z[i]]) {\n            z[i]++;\n        }\n        \n        if (i + z[i] - 1 > r) {\n            l = i;\n            r = i + z[i] - 1;\n        }\n    }\n    \n    return z;\n}\n```",
        "explanation": "The Z-algorithm has linear time complexity O(n) because each character is compared at most twice due to the sliding window approach.",
        "reference": "https://en.wikipedia.org/wiki/Z_algorithm",
        "points": 3,
        "answers": [
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(n³)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Longest Common Subsequence problem?",
        "explanation": "LCS uses dynamic programming to build a table where dp[i][j] represents the LCS length for first i characters of string1 and first j characters of string2.",
        "reference": "https://en.wikipedia.org/wiki/Longest_common_subsequence_problem",
        "points": 3,
        "answers": [
            {
                "text": "function lcs(str1: string, str2: string): number {\n    const m = str1.length;\n    const n = str2.length;\n    const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0));\n    \n    for (let i = 1; i <= m; i++) {\n        for (let j = 1; j <= n; j++) {\n            if (str1[i - 1] === str2[j - 1]) {\n                dp[i][j] = dp[i - 1][j - 1] + 1;\n            } else {\n                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    \n    return dp[m][n];\n}",
                "is_correct": True,
            },
            {
                "text": "function lcs(str1: string, str2: string): number {\n    return Math.min(str1.length, str2.length);\n}",
                "is_correct": False,
            },
            {
                "text": "function lcs(str1: string, str2: string): number {\n    const set1 = new Set(str1);\n    const set2 = new Set(str2);\n    return new Set([...set1, ...set2]).size;\n}",
                "is_correct": False,
            },
            {
                "text": "function lcs(str1: string, str2: string): number {\n    let count = 0;\n    for (let i = 0; i < Math.min(str1.length, str2.length); i++) {\n        if (str1[i] === str2[i]) count++;\n    }\n    return count;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript implementation of Manacher's algorithm output for finding longest palindromic substring?\n\n```typescript\nfunction manacher(s: string): string {\n    // Transform string to handle even length palindromes\n    const transformed = '#' + s.split('').join('#') + '#';\n    const n = transformed.length;\n    const P = new Array(n).fill(0);\n    let center = 0, right = 0;\n    let maxLen = 0, centerIndex = 0;\n    \n    for (let i = 0; i < n; i++) {\n        const mirror = 2 * center - i;\n        \n        if (i < right) {\n            P[i] = Math.min(right - i, P[mirror]);\n        }\n        \n        // Try to expand palindrome centered at i\n        while (i + P[i] + 1 < n && i - P[i] - 1 >= 0 && \n               transformed[i + P[i] + 1] === transformed[i - P[i] - 1]) {\n            P[i]++;\n        }\n        \n        // If palindrome centered at i extends past right, adjust center and right\n        if (i + P[i] > right) {\n            center = i;\n            right = i + P[i];\n        }\n        \n        // Update maximum length palindrome\n        if (P[i] > maxLen) {\n            maxLen = P[i];\n            centerIndex = i;\n        }\n    }\n    \n    const start = (centerIndex - maxLen) / 2;\n    return s.substring(start, start + maxLen);\n}\n\nconsole.log(manacher('babad'));\n```",
        "explanation": "Manacher's algorithm efficiently finds the longest palindromic substring. For 'babad', it finds 'bab' (or 'aba') as the longest palindrome.",
        "reference": "https://en.wikipedia.org/wiki/Longest_palindromic_substring",
        "points": 4,
        "answers": [
            {"text": "bab", "is_correct": True},
            {"text": "aba", "is_correct": False},
            {"text": "babad", "is_correct": False},
            {"text": "b", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Matrix Chain Multiplication problem?",
        "explanation": "Matrix chain multiplication uses dynamic programming to find the optimal parenthesization that minimizes scalar multiplications.",
        "reference": "https://en.wikipedia.org/wiki/Matrix_chain_multiplication",
        "points": 4,
        "answers": [
            {
                "text": "function matrixChainOrder(dimensions: number[]): number {\n    const n = dimensions.length - 1;\n    const dp = Array(n).fill(null).map(() => Array(n).fill(0));\n    \n    for (let len = 2; len <= n; len++) {\n        for (let i = 0; i <= n - len; i++) {\n            const j = i + len - 1;\n            dp[i][j] = Infinity;\n            \n            for (let k = i; k < j; k++) {\n                const cost = dp[i][k] + dp[k + 1][j] + \n                           dimensions[i] * dimensions[k + 1] * dimensions[j + 1];\n                dp[i][j] = Math.min(dp[i][j], cost);\n            }\n        }\n    }\n    \n    return dp[0][n - 1];\n}",
                "is_correct": True,
            },
            {
                "text": "function matrixChainOrder(dimensions: number[]): number {\n    return dimensions.reduce((product, dim) => product * dim, 1);\n}",
                "is_correct": False,
            },
            {
                "text": "function matrixChainOrder(dimensions: number[]): number {\n    let cost = 0;\n    for (let i = 0; i < dimensions.length - 2; i++) {\n        cost += dimensions[i] * dimensions[i + 1] * dimensions[i + 2];\n    }\n    return cost;\n}",
                "is_correct": False,
            },
            {
                "text": "function matrixChainOrder(dimensions: number[]): number {\n    return (dimensions.length - 1) * Math.max(...dimensions);\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the output of this TypeScript implementation for finding strongly connected components using Kosaraju's algorithm?\n\n```typescript\nfunction kosaraju(graph: number[][]): number {\n    const n = graph.length;\n    const visited = new Array(n).fill(False);\n    const stack: number[] = [];\n    \n    // Step 1: Fill stack with vertices in order of finishing times\n    const dfs1 = (v: number): void => {\n        visited[v] = True;\n        for (const u of graph[v]) {\n            if (!visited[u]) {\n                dfs1(u);\n            }\n        }\n        stack.push(v);\n    };\n    \n    for (let i = 0; i < n; i++) {\n        if (!visited[i]) {\n            dfs1(i);\n        }\n    }\n    \n    // Step 2: Create transpose graph\n    const transpose: number[][] = Array(n).fill(null).map(() => []);\n    for (let i = 0; i < n; i++) {\n        for (const j of graph[i]) {\n            transpose[j].push(i);\n        }\n    }\n    \n    // Step 3: DFS on transpose in reverse order\n    visited.fill(False);\n    let sccCount = 0;\n    \n    const dfs2 = (v: number): void => {\n        visited[v] = True;\n        for (const u of transpose[v]) {\n            if (!visited[u]) {\n                dfs2(u);\n            }\n        }\n    };\n    \n    while (stack.length > 0) {\n        const v = stack.pop()!;\n        if (!visited[v]) {\n            dfs2(v);\n            sccCount++;\n        }\n    }\n    \n    return sccCount;\n}\n\nconst graph = [\n    [1],\n    [2],\n    [0, 3],\n    [4],\n    [5],\n    [3]\n];\nconsole.log(kosaraju(graph));\n```",
        "explanation": "Kosaraju's algorithm finds strongly connected components. The given graph has 3 SCCs: {0,1,2}, {3,5}, {4}.",
        "reference": "https://en.wikipedia.org/wiki/Kosaraju%27s_algorithm",
        "points": 4,
        "answers": [
            {"text": "3", "is_correct": True},
            {"text": "2", "is_correct": False},
            {"text": "4", "is_correct": False},
            {"text": "6", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Activity Selection problem using greedy approach?",
        "explanation": "Activity selection greedy algorithm selects activities by earliest finish time to maximize the number of non-overlapping activities.",
        "reference": "https://en.wikipedia.org/wiki/Activity_selection_problem",
        "points": 3,
        "answers": [
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] {\n    const n = start.length;\n    const activities = Array.from({length: n}, (_, i) => ({index: i, start: start[i], finish: finish[i]}));\n    \n    // Sort by finish time\n    activities.sort((a, b) => a.finish - b.finish);\n    \n    const selected: number[] = [];\n    let lastFinish = 0;\n    \n    for (const activity of activities) {\n        if (activity.start >= lastFinish) {\n            selected.push(activity.index);\n            lastFinish = activity.finish;\n        }\n    }\n    \n    return selected;\n}",
                "is_correct": True,
            },
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] {\n    return start.map((_, i) => i).filter(i => start[i] < finish[i]);\n}",
                "is_correct": False,
            },
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] {\n    const activities = start.map((s, i) => ({index: i, duration: finish[i] - s}));\n    activities.sort((a, b) => a.duration - b.duration);\n    return activities.map(a => a.index);\n}",
                "is_correct": False,
            },
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] {\n    return Array.from({length: start.length}, (_, i) => i);\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript implementation of Rabin-Karp string matching algorithm output?\n\n```typescript\nfunction rabinKarp(text: string, pattern: string): number[] {\n    const positions: number[] = [];\n    const patternLength = pattern.length;\n    const textLength = text.length;\n    const prime = 101;\n    const base = 256;\n    \n    let patternHash = 0;\n    let textHash = 0;\n    let h = 1;\n    \n    // Calculate h = base^(patternLength-1) % prime\n    for (let i = 0; i < patternLength - 1; i++) {\n        h = (h * base) % prime;\n    }\n    \n    // Calculate hash for pattern and first window of text\n    for (let i = 0; i < patternLength; i++) {\n        patternHash = (base * patternHash + pattern.charCodeAt(i)) % prime;\n        textHash = (base * textHash + text.charCodeAt(i)) % prime;\n    }\n    \n    for (let i = 0; i <= textLength - patternLength; i++) {\n        // Check if hash values match\n        if (patternHash === textHash) {\n            // Verify character by character\n            let match = True;\n            for (let j = 0; j < patternLength; j++) {\n                if (text[i + j] !== pattern[j]) {\n                    match = False;\n                    break;\n                }\n            }\n            if (match) {\n                positions.push(i);\n            }\n        }\n        \n        // Calculate hash for next window\n        if (i < textLength - patternLength) {\n            textHash = (base * (textHash - text.charCodeAt(i) * h) + \n                       text.charCodeAt(i + patternLength)) % prime;\n            \n            // Handle negative hash\n            if (textHash < 0) {\n                textHash += prime;\n            }\n        }\n    }\n    \n    return positions;\n}\n\nconst text = 'GEEKS FOR GEEKS';\nconst pattern = 'GEEKS';\nconsole.log(rabinKarp(text, pattern));\n```",
        "explanation": "Rabin-Karp finds pattern 'GEEKS' in text 'GEEKS FOR GEEKS' at positions 0 and 10.",
        "reference": "https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm",
        "points": 3,
        "answers": [
            {"text": "[0, 10]", "is_correct": True},
            {"text": "[0]", "is_correct": False},
            {"text": "[10]", "is_correct": False},
            {"text": "[]", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Subset Sum problem using dynamic programming?",
        "explanation": "Subset sum problem uses DP to determine if there's a subset with the given sum by building a boolean table.",
        "reference": "https://en.wikipedia.org/wiki/Subset_sum_problem",
        "points": 3,
        "answers": [
            {
                "text": "function subsetSum(nums: number[], target: number): boolean {\n    const dp = Array(target + 1).fill(False);\n    dp[0] = True;\n    \n    for (const num of nums) {\n        for (let j = target; j >= num; j--) {\n            dp[j] = dp[j] || dp[j - num];\n        }\n    }\n    \n    return dp[target];\n}",
                "is_correct": True,
            },
            {
                "text": "function subsetSum(nums: number[], target: number): boolean {\n    return nums.reduce((sum, num) => sum + num, 0) === target;\n}",
                "is_correct": False,
            },
            {
                "text": "function subsetSum(nums: number[], target: number): boolean {\n    return nums.includes(target);\n}",
                "is_correct": False,
            },
            {
                "text": "function subsetSum(nums: number[], target: number): boolean {\n    const sum = nums.reduce((s, n) => s + n, 0);\n    return sum >= target;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of this TypeScript implementation for finding the nth Fibonacci number using matrix exponentiation?\n\n```typescript\nfunction matrixMultiply(A: number[][], B: number[][]): number[][] {\n    return [\n        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],\n        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]\n    ];\n}\n\nfunction matrixPower(matrix: number[][], n: number): number[][] {\n    if (n === 1) return matrix;\n    if (n % 2 === 0) {\n        const half = matrixPower(matrix, n / 2);\n        return matrixMultiply(half, half);\n    } else {\n        return matrixMultiply(matrix, matrixPower(matrix, n - 1));\n    }\n}\n\nfunction fibonacci(n: number): number {\n    if (n <= 1) return n;\n    \n    const baseMatrix = [[1, 1], [1, 0]];\n    const result = matrixPower(baseMatrix, n - 1);\n    return result[0][0];\n}\n```",
        "explanation": "Matrix exponentiation for Fibonacci uses O(log n) space due to recursion depth, with each call using constant space for 2x2 matrices.",
        "reference": "https://en.wikipedia.org/wiki/Fibonacci_number",
        "points": 3,
        "answers": [
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
            {"text": "O(n²)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Longest Palindromic Subsequence problem?",
        "explanation": "LPS uses dynamic programming where dp[i][j] represents the length of LPS in substring from index i to j.",
        "reference": "https://en.wikipedia.org/wiki/Longest_palindromic_subsequence",
        "points": 3,
        "answers": [
            {
                "text": "function longestPalindromicSubsequence(s: string): number {\n    const n = s.length;\n    const dp = Array(n).fill(null).map(() => Array(n).fill(0));\n    \n    // Every single character is a palindrome of length 1\n    for (let i = 0; i < n; i++) {\n        dp[i][i] = 1;\n    }\n    \n    // Fill for lengths 2 to n\n    for (let len = 2; len <= n; len++) {\n        for (let i = 0; i <= n - len; i++) {\n            const j = i + len - 1;\n            if (s[i] === s[j]) {\n                dp[i][j] = dp[i + 1][j - 1] + 2;\n            } else {\n                dp[i][j] = Math.max(dp[i + 1][j], dp[i][j - 1]);\n            }\n        }\n    }\n    \n    return dp[0][n - 1];\n}",
                "is_correct": True,
            },
            {
                "text": "function longestPalindromicSubsequence(s: string): number {\n    return s.length;\n}",
                "is_correct": False,
            },
            {
                "text": "function longestPalindromicSubsequence(s: string): number {\n    const reversed = s.split('').reverse().join('');\n    return lcs(s, reversed);\n}",
                "is_correct": False,
            },
            {
                "text": "function longestPalindromicSubsequence(s: string): number {\n    let maxLen = 1;\n    for (let i = 0; i < s.length; i++) {\n        for (let j = i + 1; j < s.length; j++) {\n            if (s[i] === s[j]) {\n                maxLen = Math.max(maxLen, j - i + 1);\n            }\n        }\n    }\n    return maxLen;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript implementation of Bellman-Ford algorithm output for detecting negative cycles?\n\n```typescript\nfunction bellmanFord(graph: Array<[number, number, number]>, vertices: number, source: number): { distances: number[], hasNegativeCycle: boolean } {\n    const distances = new Array(vertices).fill(Infinity);\n    distances[source] = 0;\n    \n    // Relax all edges V-1 times\n    for (let i = 0; i < vertices - 1; i++) {\n        for (const [u, v, weight] of graph) {\n            if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {\n                distances[v] = distances[u] + weight;\n            }\n        }\n    }\n    \n    // Check for negative cycles\n    let hasNegativeCycle = False;\n    for (const [u, v, weight] of graph) {\n        if (distances[u] !== Infinity && distances[u] + weight < distances[v]) {\n            hasNegativeCycle = True;\n            break;\n        }\n    }\n    \n    return { distances, hasNegativeCycle };\n}\n\nconst edges: Array<[number, number, number]> = [\n    [0, 1, -1],\n    [0, 2, 4],\n    [1, 2, 3],\n    [1, 3, 2],\n    [1, 4, 2],\n    [3, 2, 5],\n    [3, 1, 1],\n    [4, 3, -3]\n];\n\nconst result = bellmanFord(edges, 5, 0);\nconsole.log(result.hasNegativeCycle);\n```",
        "explanation": "Bellman-Ford detects negative cycles by checking if any edge can still be relaxed after V-1 iterations. This graph has a negative cycle: 1→4→3→1.",
        "reference": "https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm",
        "points": 4,
        "answers": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False},
            {"text": "undefined", "is_correct": False},
            {"text": "null", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Palindrome Partitioning problem to find minimum cuts?",
        "explanation": "Palindrome partitioning uses DP to precompute palindromes and then find minimum cuts needed to partition string into palindromes.",
        "reference": "https://en.wikipedia.org/wiki/Palindrome_partitioning",
        "points": 4,
        "answers": [
            {
                "text": "function minCut(s: string): number {\n    const n = s.length;\n    const isPalin = Array(n).fill(null).map(() => Array(n).fill(False));\n    const cuts = new Array(n).fill(0);\n    \n    // Build palindrome table\n    for (let i = 0; i < n; i++) {\n        isPalin[i][i] = True;\n    }\n    \n    for (let len = 2; len <= n; len++) {\n        for (let i = 0; i <= n - len; i++) {\n            const j = i + len - 1;\n            if (s[i] === s[j]) {\n                isPalin[i][j] = (len === 2) || isPalin[i + 1][j - 1];\n            }\n        }\n    }\n    \n    // Calculate minimum cuts\n    for (let i = 0; i < n; i++) {\n        if (isPalin[0][i]) {\n            cuts[i] = 0;\n        } else {\n            cuts[i] = i; // worst case: i cuts\n            for (let j = 0; j < i; j++) {\n                if (isPalin[j + 1][i]) {\n                    cuts[i] = Math.min(cuts[i], cuts[j] + 1);\n                }\n            }\n        }\n    }\n    \n    return cuts[n - 1];\n}",
                "is_correct": True,
            },
            {
                "text": "function minCut(s: string): number {\n    return s.length - 1;\n}",
                "is_correct": False,
            },
            {
                "text": "function minCut(s: string): number {\n    let cuts = 0;\n    for (let i = 0; i < s.length - 1; i++) {\n        if (s[i] !== s[i + 1]) cuts++;\n    }\n    return cuts;\n}",
                "is_correct": False,
            },
            {
                "text": "function minCut(s: string): number {\n    const palindromes = [];\n    for (let i = 0; i < s.length; i++) {\n        if (s[i] === s[s.length - 1 - i]) {\n            palindromes.push(i);\n        }\n    }\n    return palindromes.length - 1;\n}",
                "is_correct": False,
            },
        ],
    },
]
