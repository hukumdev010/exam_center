"""Advanced Algorithms Certification"""

CERTIFICATION = {
    "name": "Advanced Algorithms",
    "description": "Advanced algorithmic techniques including dynamic programming, greedy algorithms, and graph algorithms",
    "slug": "advanced-algorithms",
    "level": "Professional",
    "duration": 183,
    "questions_count": 61,
    "category_slug": "data-structures-algorithms",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "Which algorithm is used to find the shortest path in a weighted graph with no negative edges?",
        "explanation": "Dijkstra's algorithm efficiently finds shortest paths in weighted graphs without negative edge weights.",
        "reference": "https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm",
        "points": 1,
        "answers": [
            {"text": "Breadth-First Search", "is_correct": False},
            {"text": "Depth-First Search", "is_correct": False},
            {"text": "Dijkstra's Algorithm", "is_correct": True},
            {"text": "Bellman-Ford Algorithm", "is_correct": False},
        ],
    },
    {
        "text": "What is the key principle behind dynamic programming?",
        "explanation": "Dynamic programming breaks down complex problems into simpler subproblems and stores their solutions to avoid recomputation.",
        "reference": "https://en.wikipedia.org/wiki/Dynamic_programming",
        "points": 1,
        "answers": [
            {"text": "Divide and conquer", "is_correct": False},
            {
                "text": "Optimal substructure and overlapping subproblems",
                "is_correct": True,
            },
            {"text": "Greedy choice property", "is_correct": False},
            {"text": "Backtracking", "is_correct": False},
        ],
    },
    {
        "text": "Implement Dijkstra's algorithm in TypeScript for finding shortest paths:",
        "explanation": "Dijkstra's algorithm uses a priority queue to explore vertices in order of their distance from the source.",
        "reference": "Dijkstra's Algorithm implementation",
        "points": 3,
        "answers": [
            {
                "text": "function dijkstra(graph: number[][], source: number): number[] { const dist = new Array(graph.length).fill(Infinity); const visited = new Array(graph.length).fill(False); dist[source] = 0; const pq = new PriorityQueue<[number, number]>((a, b) => a[0] - b[0]); pq.enqueue([0, source]); while (!pq.isEmpty()) { const [d, u] = pq.dequeue()!; if (visited[u]) continue; visited[u] = True; for (let v = 0; v < graph.length; v++) { if (graph[u][v] > 0 && !visited[v] && dist[u] + graph[u][v] < dist[v]) { dist[v] = dist[u] + graph[u][v]; pq.enqueue([dist[v], v]); } } } return dist; }",
                "is_correct": True,
            },
            {
                "text": "function dijkstra(graph: number[][], source: number): number[] { return graph[source]; }",
                "is_correct": False,
            },
            {
                "text": "function dijkstra(graph: number[][], source: number): number[] { const dist = new Array(graph.length).fill(0); for (let i = 0; i < graph.length; i++) dist[i] = graph[source][i]; return dist; }",
                "is_correct": False,
            },
            {
                "text": "function dijkstra(graph: number[][], source: number): number[] { return new Array(graph.length).fill(1); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the 0/1 Knapsack problem using dynamic programming?",
        "explanation": "0/1 Knapsack uses 2D DP where dp[i][w] represents maximum value using first i items with weight limit w.",
        "reference": "Knapsack Problem DP solution",
        "points": 3,
        "answers": [
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number { const n = weights.length; const dp = Array(n + 1).fill(null).map(() => Array(capacity + 1).fill(0)); for (let i = 1; i <= n; i++) { for (let w = 1; w <= capacity; w++) { if (weights[i-1] <= w) { dp[i][w] = Math.max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w]); } else { dp[i][w] = dp[i-1][w]; } } } return dp[n][capacity]; }",
                "is_correct": True,
            },
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number { return Math.max(...values); }",
                "is_correct": False,
            },
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number { return values.reduce((sum, val) => sum + val, 0); }",
                "is_correct": False,
            },
            {
                "text": "function knapsack(weights: number[], values: number[], capacity: number): number { const ratio = values.map((v, i) => v / weights[i]); return Math.max(...ratio) * capacity; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Bellman-Ford algorithm in TypeScript for detecting negative cycles:",
        "explanation": "Bellman-Ford relaxes all edges V-1 times and checks for negative cycles in the Vth iteration.",
        "reference": "Bellman-Ford Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function bellmanFord(edges: [number, number, number][], V: number, source: number): { distances: number[]; hasNegativeCycle: boolean } { const dist = new Array(V).fill(Infinity); dist[source] = 0; for (let i = 0; i < V - 1; i++) { for (const [u, v, weight] of edges) { if (dist[u] !== Infinity && dist[u] + weight < dist[v]) { dist[v] = dist[u] + weight; } } } for (const [u, v, weight] of edges) { if (dist[u] !== Infinity && dist[u] + weight < dist[v]) { return { distances: dist, hasNegativeCycle: True }; } } return { distances: dist, hasNegativeCycle: False }; }",
                "is_correct": True,
            },
            {
                "text": "function bellmanFord(edges: [number, number, number][], V: number, source: number): number[] { const dist = new Array(V).fill(0); dist[source] = 1; return dist; }",
                "is_correct": False,
            },
            {
                "text": "function bellmanFord(edges: [number, number, number][], V: number, source: number): number[] { return edges.map(([u, v, w]) => w); }",
                "is_correct": False,
            },
            {
                "text": "function bellmanFord(edges: [number, number, number][], V: number, source: number): boolean { return edges.length > 0; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Floyd-Warshall algorithm?",
        "explanation": "Floyd-Warshall uses three nested loops to consider all vertices as intermediate vertices, resulting in O(V³) complexity.",
        "reference": "Floyd-Warshall Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(V²)", "is_correct": False},
            {"text": "O(V³)", "is_correct": True},
            {"text": "O(V log V)", "is_correct": False},
            {"text": "O(E log V)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Longest Common Subsequence (LCS) algorithm in TypeScript:",
        "explanation": "LCS uses 2D DP where dp[i][j] represents LCS length of first i chars of str1 and first j chars of str2.",
        "reference": "Longest Common Subsequence",
        "points": 3,
        "answers": [
            {
                "text": "function lcs(str1: string, str2: string): number { const m = str1.length, n = str2.length; const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0)); for (let i = 1; i <= m; i++) { for (let j = 1; j <= n; j++) { if (str1[i-1] === str2[j-1]) { dp[i][j] = dp[i-1][j-1] + 1; } else { dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]); } } } return dp[m][n]; }",
                "is_correct": True,
            },
            {
                "text": "function lcs(str1: string, str2: string): number { return Math.min(str1.length, str2.length); }",
                "is_correct": False,
            },
            {
                "text": "function lcs(str1: string, str2: string): number { let count = 0; for (let i = 0; i < Math.min(str1.length, str2.length); i++) { if (str1[i] === str2[i]) count++; } return count; }",
                "is_correct": False,
            },
            {
                "text": "function lcs(str1: string, str2: string): number { return str1.length + str2.length; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements Kruskal's algorithm for MST?",
        "explanation": "Kruskal's algorithm sorts edges by weight and uses Union-Find to detect cycles while building MST.",
        "reference": "Kruskal's Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function kruskal(edges: [number, number, number][], V: number): [number, number, number][] { edges.sort((a, b) => a[2] - b[2]); const uf = new UnionFind(V); const mst: [number, number, number][] = []; for (const [u, v, weight] of edges) { if (uf.find(u) !== uf.find(v)) { uf.union(u, v); mst.push([u, v, weight]); if (mst.length === V - 1) break; } } return mst; }",
                "is_correct": True,
            },
            {
                "text": "function kruskal(edges: [number, number, number][], V: number): [number, number, number][] { return edges.slice(0, V - 1); }",
                "is_correct": False,
            },
            {
                "text": "function kruskal(edges: [number, number, number][], V: number): [number, number, number][] { return edges.filter(([u, v, w]) => w > 0); }",
                "is_correct": False,
            },
            {
                "text": "function kruskal(edges: [number, number, number][], V: number): [number, number, number][] { return edges.sort((a, b) => a[2] - b[2]); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement Prim's algorithm for Minimum Spanning Tree in TypeScript:",
        "explanation": "Prim's algorithm grows MST by always adding the minimum weight edge that connects a vertex in MST to a vertex outside MST.",
        "reference": "Prim's Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function prim(graph: number[][], V: number): number { const key = new Array(V).fill(Infinity); const mstSet = new Array(V).fill(False); const parent = new Array(V).fill(-1); key[0] = 0; let mstWeight = 0; for (let count = 0; count < V - 1; count++) { let u = -1; for (let v = 0; v < V; v++) { if (!mstSet[v] && (u === -1 || key[v] < key[u])) u = v; } mstSet[u] = True; mstWeight += key[u]; for (let v = 0; v < V; v++) { if (graph[u][v] > 0 && !mstSet[v] && graph[u][v] < key[v]) { parent[v] = u; key[v] = graph[u][v]; } } } return mstWeight; }",
                "is_correct": True,
            },
            {
                "text": "function prim(graph: number[][], V: number): number { return graph.flat().reduce((sum, val) => sum + val, 0); }",
                "is_correct": False,
            },
            {
                "text": "function prim(graph: number[][], V: number): number { return Math.min(...graph.flat().filter(x => x > 0)); }",
                "is_correct": False,
            },
            {
                "text": "function prim(graph: number[][], V: number): number { return V * V; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Edmonds-Karp algorithm for maximum flow?",
        "explanation": "Edmonds-Karp is Ford-Fulkerson with BFS for finding augmenting paths, giving O(VE²) complexity.",
        "reference": "Edmonds-Karp Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(V²E)", "is_correct": False},
            {"text": "O(VE²)", "is_correct": True},
            {"text": "O(V³)", "is_correct": False},
            {"text": "O(E³)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Longest Increasing Subsequence (LIS) algorithm in TypeScript using binary search:",
        "explanation": "LIS with binary search maintains array of smallest tail elements for each length, achieving O(n log n) complexity.",
        "reference": "Longest Increasing Subsequence optimization",
        "points": 3,
        "answers": [
            {
                "text": "function lisLength(nums: number[]): number { const tails: number[] = []; for (const num of nums) { let left = 0, right = tails.length; while (left < right) { const mid = Math.floor((left + right) / 2); if (tails[mid] < num) left = mid + 1; else right = mid; } if (left === tails.length) tails.push(num); else tails[left] = num; } return tails.length; }",
                "is_correct": True,
            },
            {
                "text": "function lisLength(nums: number[]): number { return nums.length; }",
                "is_correct": False,
            },
            {
                "text": "function lisLength(nums: number[]): number { let count = 0; for (let i = 1; i < nums.length; i++) { if (nums[i] > nums[i-1]) count++; } return count + 1; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the KMP (Knuth-Morris-Pratt) string matching algorithm in TypeScript:",
        "explanation": "KMP uses a failure function to avoid redundant character comparisons during pattern matching.",
        "reference": "KMP Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function kmpSearch(text: string, pattern: string): number[] { const lps = computeLPS(pattern); const matches: number[] = []; let i = 0, j = 0; while (i < text.length) { if (pattern[j] === text[i]) { i++; j++; } if (j === pattern.length) { matches.push(i - j); j = lps[j - 1]; } else if (i < text.length && pattern[j] !== text[i]) { if (j !== 0) j = lps[j - 1]; else i++; } } return matches; } function computeLPS(pattern: string): number[] { const lps = new Array(pattern.length).fill(0); let len = 0, i = 1; while (i < pattern.length) { if (pattern[i] === pattern[len]) { len++; lps[i] = len; i++; } else { if (len !== 0) len = lps[len - 1]; else { lps[i] = 0; i++; } } } return lps; }",
                "is_correct": True,
            },
            {
                "text": "function kmpSearch(text: string, pattern: string): number[] { return text.split(pattern).map((_, i) => i * pattern.length); }",
                "is_correct": False,
            },
            {
                "text": "function kmpSearch(text: string, pattern: string): number[] { const matches = []; for (let i = 0; i <= text.length - pattern.length; i++) { if (text.substring(i, i + pattern.length) === pattern) matches.push(i); } return matches; }",
                "is_correct": False,
            },
            {
                "text": "function kmpSearch(text: string, pattern: string): number[] { return [text.indexOf(pattern)]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Coin Change problem using dynamic programming?",
        "explanation": "Coin change DP uses dp[i] to represent minimum coins needed to make amount i.",
        "reference": "Coin Change DP",
        "points": 3,
        "answers": [
            {
                "text": "function coinChange(coins: number[], amount: number): number { const dp = new Array(amount + 1).fill(Infinity); dp[0] = 0; for (let i = 1; i <= amount; i++) { for (const coin of coins) { if (coin <= i) { dp[i] = Math.min(dp[i], dp[i - coin] + 1); } } } return dp[amount] === Infinity ? -1 : dp[amount]; }",
                "is_correct": True,
            },
            {
                "text": "function coinChange(coins: number[], amount: number): number { return Math.ceil(amount / Math.min(...coins)); }",
                "is_correct": False,
            },
            {
                "text": "function coinChange(coins: number[], amount: number): number { return coins.length; }",
                "is_correct": False,
            },
            {
                "text": "function coinChange(coins: number[], amount: number): number { return amount / coins[0]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Z-algorithm for pattern matching in TypeScript:",
        "explanation": "Z-algorithm computes Z-array where Z[i] is the length of longest substring starting from S[i] which is also prefix of S.",
        "reference": "Z-Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function zAlgorithm(s: string): number[] { const n = s.length; const z = new Array(n).fill(0); let l = 0, r = 0; for (let i = 1; i < n; i++) { if (i <= r) { z[i] = Math.min(r - i + 1, z[i - l]); } while (i + z[i] < n && s[z[i]] === s[i + z[i]]) { z[i]++; } if (i + z[i] - 1 > r) { l = i; r = i + z[i] - 1; } } return z; }",
                "is_correct": True,
            },
            {
                "text": "function zAlgorithm(s: string): number[] { return s.split('').map((_, i) => s.length - i); }",
                "is_correct": False,
            },
            {
                "text": "function zAlgorithm(s: string): number[] { return new Array(s.length).fill(1); }",
                "is_correct": False,
            },
            {
                "text": "function zAlgorithm(s: string): number[] { return s.split('').map((char, i) => char.charCodeAt(0) - i); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Rabin-Karp string matching algorithm in the average case?",
        "explanation": "Rabin-Karp uses rolling hash for O(1) hash computation per position, giving O(n+m) average complexity.",
        "reference": "Rabin-Karp Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(nm)", "is_correct": False},
            {"text": "O(n + m)", "is_correct": True},
            {"text": "O(n log m)", "is_correct": False},
            {"text": "O(m²)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Manacher's algorithm for finding all palindromic substrings in TypeScript:",
        "explanation": "Manacher's algorithm finds all palindromes in linear time using previously computed palindrome information.",
        "reference": "Manacher's Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function manacher(s: string): number[] { const processed = '#' + s.split('').join('#') + '#'; const n = processed.length; const p = new Array(n).fill(0); let center = 0, right = 0; for (let i = 0; i < n; i++) { const mirror = 2 * center - i; if (i < right) { p[i] = Math.min(right - i, p[mirror]); } while (i + p[i] + 1 < n && i - p[i] - 1 >= 0 && processed[i + p[i] + 1] === processed[i - p[i] - 1]) { p[i]++; } if (i + p[i] > right) { center = i; right = i + p[i]; } } return p; }",
                "is_correct": True,
            },
            {
                "text": "function manacher(s: string): number[] { return s.split('').map((_, i) => i); }",
                "is_correct": False,
            },
            {
                "text": "function manacher(s: string): number[] { const result = []; for (let i = 0; i < s.length; i++) { if (s[i] === s[s.length - 1 - i]) result.push(i); } return result; }",
                "is_correct": False,
            },
            {
                "text": "function manacher(s: string): number[] { return new Array(s.length).fill(1); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements the Activity Selection problem using greedy approach?",
        "explanation": "Activity selection greedily selects activities by earliest finish time to maximize number of non-overlapping activities.",
        "reference": "Activity Selection Greedy Algorithm",
        "points": 2,
        "answers": [
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] { const n = start.length; const activities = Array.from({length: n}, (_, i) => ({start: start[i], finish: finish[i], index: i})); activities.sort((a, b) => a.finish - b.finish); const selected = [activities[0].index]; let lastSelected = 0; for (let i = 1; i < n; i++) { if (activities[i].start >= activities[lastSelected].finish) { selected.push(activities[i].index); lastSelected = i; } } return selected; }",
                "is_correct": True,
            },
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] { return start.map((_, i) => i); }",
                "is_correct": False,
            },
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] { return finish.map((_, i) => i).sort(); }",
                "is_correct": False,
            },
            {
                "text": "function activitySelection(start: number[], finish: number[]): number[] { return [0]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Kadane's algorithm for Maximum Subarray Sum in TypeScript:",
        "explanation": "Kadane's algorithm uses dynamic programming to find maximum sum contiguous subarray in linear time.",
        "reference": "Kadane's Algorithm",
        "points": 2,
        "answers": [
            {
                "text": "function maxSubarraySum(nums: number[]): number { let maxSoFar = nums[0]; let maxEndingHere = nums[0]; for (let i = 1; i < nums.length; i++) { maxEndingHere = Math.max(nums[i], maxEndingHere + nums[i]); maxSoFar = Math.max(maxSoFar, maxEndingHere); } return maxSoFar; }",
                "is_correct": True,
            },
            {
                "text": "function maxSubarraySum(nums: number[]): number { return Math.max(...nums); }",
                "is_correct": False,
            },
            {
                "text": "function maxSubarraySum(nums: number[]): number { return nums.reduce((sum, num) => sum + num, 0); }",
                "is_correct": False,
            },
            {
                "text": "function maxSubarraySum(nums: number[]): number { return nums[0] + nums[nums.length - 1]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Ford-Fulkerson algorithm with DFS for finding augmenting paths?",
        "explanation": "Ford-Fulkerson with DFS can take O(Ef) time where E is edges and f is maximum flow value.",
        "reference": "Ford-Fulkerson Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(VE)", "is_correct": False},
            {"text": "O(Ef)", "is_correct": True},
            {"text": "O(V³)", "is_correct": False},
            {"text": "O(E²)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Hungarian algorithm for assignment problem in TypeScript:",
        "explanation": "Hungarian algorithm solves assignment problem in O(n³) time using augmenting paths in bipartite graphs.",
        "reference": "Hungarian Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function hungarian(costMatrix: number[][]): { cost: number; assignment: number[] } { const n = costMatrix.length; const u = new Array(n + 1).fill(0); const v = new Array(n + 1).fill(0); const p = new Array(n + 1).fill(0); const way = new Array(n + 1).fill(0); for (let i = 1; i <= n; i++) { p[0] = i; let j0 = 0; const minv = new Array(n + 1).fill(Infinity); const used = new Array(n + 1).fill(False); do { used[j0] = True; const i0 = p[j0]; let delta = Infinity; let j1 = 0; for (let j = 1; j <= n; j++) { if (!used[j]) { const cur = costMatrix[i0 - 1][j - 1] - u[i0] - v[j]; if (cur < minv[j]) { minv[j] = cur; way[j] = j0; } if (minv[j] < delta) { delta = minv[j]; j1 = j; } } } for (let j = 0; j <= n; j++) { if (used[j]) { u[p[j]] += delta; v[j] -= delta; } else { minv[j] -= delta; } } j0 = j1; } while (p[j0] !== 0); do { const j1 = way[j0]; p[j0] = p[j1]; j0 = j1; } while (j0); } const assignment = new Array(n); for (let j = 1; j <= n; j++) { assignment[p[j] - 1] = j - 1; } return { cost: -v[0], assignment }; }",
                "is_correct": True,
            },
            {
                "text": "function hungarian(costMatrix: number[][]): { cost: number; assignment: number[] } { const assignment = costMatrix.map((_, i) => i); const cost = assignment.reduce((sum, j, i) => sum + costMatrix[i][j], 0); return { cost, assignment }; }",
                "is_correct": False,
            },
            {
                "text": "function hungarian(costMatrix: number[][]): { cost: number; assignment: number[] } { return { cost: 0, assignment: [] }; }",
                "is_correct": False,
            },
            {
                "text": "function hungarian(costMatrix: number[][]): { cost: number; assignment: number[] } { const assignment = new Array(costMatrix.length).fill(0); return { cost: costMatrix.flat().reduce((a, b) => a + b, 0), assignment }; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Boyer-Moore majority vote algorithm in TypeScript:",
        "explanation": "Boyer-Moore algorithm finds majority element (appears > n/2 times) in linear time with constant space.",
        "reference": "Boyer-Moore Majority Vote",
        "points": 2,
        "answers": [
            {
                "text": "function majorityElement(nums: number[]): number { let candidate = nums[0]; let count = 1; for (let i = 1; i < nums.length; i++) { if (count === 0) { candidate = nums[i]; count = 1; } else if (nums[i] === candidate) { count++; } else { count--; } } return candidate; }",
                "is_correct": True,
            },
            {
                "text": "function majorityElement(nums: number[]): number { const map = new Map(); for (const num of nums) { map.set(num, (map.get(num) || 0) + 1); } return [...map.entries()].reduce((a, b) => a[1] > b[1] ? a : b)[0]; }",
                "is_correct": False,
            },
            {
                "text": "function majorityElement(nums: number[]): number { return nums[Math.floor(nums.length / 2)]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the A* search algorithm in TypeScript for pathfinding:",
        "explanation": "A* uses heuristic function h(n) with actual cost g(n) to find optimal path efficiently using f(n) = g(n) + h(n).",
        "reference": "A* Search Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function aStar(graph: number[][], start: number, goal: number, heuristic: (a: number, b: number) => number): number[] { const openSet = new PriorityQueue<{node: number, f: number}>((a, b) => a.f - b.f); const gScore = new Array(graph.length).fill(Infinity); const fScore = new Array(graph.length).fill(Infinity); const cameFrom = new Array(graph.length).fill(-1); gScore[start] = 0; fScore[start] = heuristic(start, goal); openSet.enqueue({node: start, f: fScore[start]}); while (!openSet.isEmpty()) { const current = openSet.dequeue()!.node; if (current === goal) { const path = []; let node = goal; while (node !== -1) { path.unshift(node); node = cameFrom[node]; } return path; } for (let neighbor = 0; neighbor < graph.length; neighbor++) { if (graph[current][neighbor] > 0) { const tentativeG = gScore[current] + graph[current][neighbor]; if (tentativeG < gScore[neighbor]) { cameFrom[neighbor] = current; gScore[neighbor] = tentativeG; fScore[neighbor] = gScore[neighbor] + heuristic(neighbor, goal); openSet.enqueue({node: neighbor, f: fScore[neighbor]}); } } } } return []; }",
                "is_correct": True,
            },
            {
                "text": "function aStar(graph: number[][], start: number, goal: number): number[] { return [start, goal]; }",
                "is_correct": False,
            },
            {
                "text": "function aStar(graph: number[][], start: number, goal: number): number[] { const path = []; for (let i = start; i <= goal; i++) path.push(i); return path; }",
                "is_correct": False,
            },
            {
                "text": "function aStar(graph: number[][], start: number, goal: number): number[] { return graph[start]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Edit Distance (Levenshtein Distance) problem?",
        "explanation": "Edit distance uses 2D DP where dp[i][j] represents minimum operations to transform first i characters of str1 to first j characters of str2.",
        "reference": "Edit Distance DP",
        "points": 3,
        "answers": [
            {
                "text": "function editDistance(str1: string, str2: string): number { const m = str1.length, n = str2.length; const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0)); for (let i = 0; i <= m; i++) dp[i][0] = i; for (let j = 0; j <= n; j++) dp[0][j] = j; for (let i = 1; i <= m; i++) { for (let j = 1; j <= n; j++) { if (str1[i-1] === str2[j-1]) { dp[i][j] = dp[i-1][j-1]; } else { dp[i][j] = 1 + Math.min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]); } } } return dp[m][n]; }",
                "is_correct": True,
            },
            {
                "text": "function editDistance(str1: string, str2: string): number { return Math.abs(str1.length - str2.length); }",
                "is_correct": False,
            },
            {
                "text": "function editDistance(str1: string, str2: string): number { return str1.length + str2.length; }",
                "is_correct": False,
            },
            {
                "text": "function editDistance(str1: string, str2: string): number { let diff = 0; for (let i = 0; i < Math.min(str1.length, str2.length); i++) { if (str1[i] !== str2[i]) diff++; } return diff; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Tarjan's algorithm for finding Strongly Connected Components in TypeScript:",
        "explanation": "Tarjan's algorithm uses DFS with low-link values to identify SCCs in a single pass through the graph.",
        "reference": "Tarjan's SCC Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function tarjanSCC(graph: number[][]): number[][] { const n = graph.length; const ids = new Array(n).fill(-1); const low = new Array(n).fill(0); const onStack = new Array(n).fill(False); const stack: number[] = []; const sccs: number[][] = []; let id = 0; function dfs(at: number): void { stack.push(at); onStack[at] = True; ids[at] = low[at] = id++; for (const to of graph[at]) { if (ids[to] === -1) dfs(to); if (onStack[to]) low[at] = Math.min(low[at], low[to]); } if (ids[at] === low[at]) { const scc: number[] = []; while (True) { const node = stack.pop()!; onStack[node] = False; scc.push(node); if (node === at) break; } sccs.push(scc); } } for (let i = 0; i < n; i++) { if (ids[i] === -1) dfs(i); } return sccs; }",
                "is_correct": True,
            },
            {
                "text": "function tarjanSCC(graph: number[][]): number[][] { return graph.map((_, i) => [i]); }",
                "is_correct": False,
            },
            {
                "text": "function tarjanSCC(graph: number[][]): number[][] { return [graph.map((_, i) => i)]; }",
                "is_correct": False,
            },
            {
                "text": "function tarjanSCC(graph: number[][]): number[][] { return graph.filter(row => row.length > 0).map((_, i) => [i]); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of Kosaraju's algorithm for finding SCCs?",
        "explanation": "Kosaraju's algorithm performs two DFS traversals on the graph and its transpose, resulting in O(V + E) complexity.",
        "reference": "Kosaraju's Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(V²)", "is_correct": False},
            {"text": "O(V + E)", "is_correct": True},
            {"text": "O(VE)", "is_correct": False},
            {"text": "O(E log V)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Topological Sort using Kahn's algorithm in TypeScript:",
        "explanation": "Kahn's algorithm uses BFS approach by repeatedly removing vertices with zero in-degree.",
        "reference": "Kahn's Algorithm",
        "points": 2,
        "answers": [
            {
                "text": "function topologicalSort(graph: number[][], V: number): number[] { const inDegree = new Array(V).fill(0); for (let u = 0; u < V; u++) { for (const v of graph[u]) { inDegree[v]++; } } const queue: number[] = []; for (let i = 0; i < V; i++) { if (inDegree[i] === 0) queue.push(i); } const result: number[] = []; while (queue.length > 0) { const u = queue.shift()!; result.push(u); for (const v of graph[u]) { inDegree[v]--; if (inDegree[v] === 0) queue.push(v); } } return result.length === V ? result : []; }",
                "is_correct": True,
            },
            {
                "text": "function topologicalSort(graph: number[][], V: number): number[] { return Array.from({length: V}, (_, i) => i); }",
                "is_correct": False,
            },
            {
                "text": "function topologicalSort(graph: number[][], V: number): number[] { return graph.flat().sort(); }",
                "is_correct": False,
            },
            {
                "text": "function topologicalSort(graph: number[][], V: number): number[] { return graph.map(row => row[0]).filter(x => x !== undefined); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Articulation Points (Cut Vertices) algorithm using Tarjan's approach in TypeScript:",
        "explanation": "Tarjan's algorithm for articulation points uses DFS with discovery time and low values to identify cut vertices.",
        "reference": "Articulation Points Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function findArticulationPoints(graph: number[][], V: number): number[] { const visited = new Array(V).fill(False); const disc = new Array(V).fill(-1); const low = new Array(V).fill(-1); const parent = new Array(V).fill(-1); const ap = new Array(V).fill(False); let time = 0; function dfs(u: number): void { let children = 0; visited[u] = True; disc[u] = low[u] = ++time; for (const v of graph[u]) { if (!visited[v]) { children++; parent[v] = u; dfs(v); low[u] = Math.min(low[u], low[v]); if (parent[u] === -1 && children > 1) ap[u] = True; if (parent[u] !== -1 && low[v] >= disc[u]) ap[u] = True; } else if (v !== parent[u]) { low[u] = Math.min(low[u], disc[v]); } } } for (let i = 0; i < V; i++) { if (!visited[i]) dfs(i); } return ap.map((isAP, i) => isAP ? i : -1).filter(x => x !== -1); }",
                "is_correct": True,
            },
            {
                "text": "function findArticulationPoints(graph: number[][], V: number): number[] { return graph.map((_, i) => i).filter(i => graph[i].length > 1); }",
                "is_correct": False,
            },
            {
                "text": "function findArticulationPoints(graph: number[][], V: number): number[] { return [0]; }",
                "is_correct": False,
            },
            {
                "text": "function findArticulationPoints(graph: number[][], V: number): number[] { return graph.flat().filter((v, i, arr) => arr.indexOf(v) === i); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements the Convex Hull using Graham's scan?",
        "explanation": "Graham's scan sorts points by polar angle and uses stack to maintain convex hull vertices.",
        "reference": "Graham's Scan Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function convexHull(points: [number, number][]): [number, number][] { function crossProduct(o: [number, number], a: [number, number], b: [number, number]): number { return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]); } function distance(a: [number, number], b: [number, number]): number { return Math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2); } const start = points.reduce((min, p) => p[1] < min[1] || (p[1] === min[1] && p[0] < min[0]) ? p : min); const sorted = points.filter(p => p !== start).sort((a, b) => { const cross = crossProduct(start, a, b); if (cross === 0) return distance(start, a) - distance(start, b); return cross > 0 ? -1 : 1; }); const hull: [number, number][] = [start]; for (const point of sorted) { while (hull.length > 1 && crossProduct(hull[hull.length - 2], hull[hull.length - 1], point) <= 0) { hull.pop(); } hull.push(point); } return hull; }",
                "is_correct": True,
            },
            {
                "text": "function convexHull(points: [number, number][]): [number, number][] { return points.sort((a, b) => a[0] - b[0]); }",
                "is_correct": False,
            },
            {
                "text": "function convexHull(points: [number, number][]): [number, number][] { return [points[0], points[points.length - 1]]; }",
                "is_correct": False,
            },
            {
                "text": "function convexHull(points: [number, number][]): [number, number][] { return points.filter((_, i) => i % 2 === 0); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Aho-Corasick algorithm for multiple pattern matching in TypeScript:",
        "explanation": "Aho-Corasick builds trie with failure links to efficiently find all occurrences of multiple patterns in text.",
        "reference": "Aho-Corasick Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "class AhoCorasick { private root: TrieNode; constructor(patterns: string[]) { this.root = new TrieNode(); this.buildTrie(patterns); this.buildFailureLinks(); } private buildTrie(patterns: string[]): void { for (let i = 0; i < patterns.length; i++) { let node = this.root; for (const char of patterns[i]) { if (!node.children[char]) { node.children[char] = new TrieNode(); } node = node.children[char]; } node.isEnd = True; node.patternIndex = i; } } private buildFailureLinks(): void { const queue: TrieNode[] = []; for (const child of Object.values(this.root.children)) { child.failure = this.root; queue.push(child); } while (queue.length > 0) { const current = queue.shift()!; for (const [char, child] of Object.entries(current.children)) { queue.push(child); let failure = current.failure; while (failure && !failure.children[char]) { failure = failure.failure; } child.failure = failure ? failure.children[char] : this.root; child.output = child.isEnd ? [child] : []; if (child.failure.output) { child.output.push(...child.failure.output); } } } } search(text: string): {pattern: number, position: number}[] { const matches: {pattern: number, position: number}[] = []; let node = this.root; for (let i = 0; i < text.length; i++) { const char = text[i]; while (node && !node.children[char]) { node = node.failure!; } if (node) { node = node.children[char]; for (const match of node.output) { if (match.isEnd) { matches.push({pattern: match.patternIndex!, position: i}); } } } else { node = this.root; } } return matches; } }",
                "is_correct": True,
            },
            {
                "text": "class AhoCorasick { search(text: string, patterns: string[]): number[] { const matches = []; for (let i = 0; i < patterns.length; i++) { if (text.includes(patterns[i])) matches.push(i); } return matches; } }",
                "is_correct": False,
            },
            {
                "text": "class AhoCorasick { search(text: string): string[] { return text.split(' '); } }",
                "is_correct": False,
            },
            {
                "text": "class AhoCorasick { search(text: string, patterns: string[]): boolean { return patterns.some(p => text.includes(p)); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Strassen's matrix multiplication algorithm?",
        "explanation": "Strassen's algorithm reduces matrix multiplication from O(n³) to O(n^log₂7) ≈ O(n^2.807) using divide and conquer.",
        "reference": "Strassen's Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(n³)", "is_correct": False},
            {"text": "O(n^2.807)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Euclidean algorithm for finding GCD in TypeScript:",
        "explanation": "Euclidean algorithm uses the property that gcd(a,b) = gcd(b, a mod b) to find GCD efficiently.",
        "reference": "Euclidean Algorithm",
        "points": 2,
        "answers": [
            {
                "text": "function gcd(a: number, b: number): number { while (b !== 0) { const temp = b; b = a % b; a = temp; } return a; }",
                "is_correct": True,
            },
            {
                "text": "function gcd(a: number, b: number): number { return Math.min(a, b); }",
                "is_correct": False,
            },
            {
                "text": "function gcd(a: number, b: number): number { return a * b; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Extended Euclidean Algorithm in TypeScript for finding modular inverse:",
        "explanation": "Extended Euclidean algorithm finds coefficients x, y such that ax + by = gcd(a,b), useful for modular arithmetic.",
        "reference": "Extended Euclidean Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function extendedGCD(a: number, b: number): {gcd: number, x: number, y: number} { if (b === 0) return {gcd: a, x: 1, y: 0}; const {gcd, x: x1, y: y1} = extendedGCD(b, a % b); const x = y1; const y = x1 - Math.floor(a / b) * y1; return {gcd, x, y}; } function modInverse(a: number, m: number): number { const {gcd, x} = extendedGCD(a, m); if (gcd !== 1) throw new Error('Modular inverse does not exist'); return ((x % m) + m) % m; }",
                "is_correct": True,
            },
            {
                "text": "function extendedGCD(a: number, b: number): {gcd: number, x: number, y: number} { return {gcd: Math.min(a, b), x: 1, y: 1}; }",
                "is_correct": False,
            },
            {
                "text": "function extendedGCD(a: number, b: number): {gcd: number, x: number, y: number} { return {gcd: a + b, x: a, y: b}; }",
                "is_correct": False,
            },
            {
                "text": "function extendedGCD(a: number, b: number): {gcd: number, x: number, y: number} { return {gcd: 1, x: 0, y: 0}; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Travelling Salesman Problem using dynamic programming?",
        "explanation": "TSP DP uses bitmask to represent visited cities and dp[mask][i] for minimum cost ending at city i with visited set mask.",
        "reference": "TSP Dynamic Programming",
        "points": 3,
        "answers": [
            {
                "text": "function tsp(dist: number[][]): number { const n = dist.length; const dp = Array(1 << n).fill(null).map(() => Array(n).fill(Infinity)); dp[1][0] = 0; for (let mask = 1; mask < (1 << n); mask++) { for (let u = 0; u < n; u++) { if (!(mask & (1 << u))) continue; for (let v = 0; v < n; v++) { if (mask & (1 << v)) continue; const newMask = mask | (1 << v); dp[newMask][v] = Math.min(dp[newMask][v], dp[mask][u] + dist[u][v]); } } } let result = Infinity; for (let i = 1; i < n; i++) { result = Math.min(result, dp[(1 << n) - 1][i] + dist[i][0]); } return result; }",
                "is_correct": True,
            },
            {
                "text": "function tsp(dist: number[][]): number { return dist.flat().reduce((sum, val) => sum + val, 0); }",
                "is_correct": False,
            },
            {
                "text": "function tsp(dist: number[][]): number { return Math.min(...dist.flat().filter(x => x > 0)); }",
                "is_correct": False,
            },
            {
                "text": "function tsp(dist: number[][]): number { return dist.length * dist[0].length; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Miller-Rabin primality test in TypeScript:",
        "explanation": "Miller-Rabin is a probabilistic primality test that uses modular exponentiation to test if a number is prime.",
        "reference": "Miller-Rabin Primality Test",
        "points": 3,
        "answers": [
            {
                "text": "function millerRabin(n: number, k: number = 5): boolean { if (n < 2) return False; if (n === 2 || n === 3) return True; if (n % 2 === 0) return False; let r = 0; let d = n - 1; while (d % 2 === 0) { r++; d = Math.floor(d / 2); } function modPow(base: number, exp: number, mod: number): number { let result = 1; base %= mod; while (exp > 0) { if (exp & 1) result = (result * base) % mod; exp >>= 1; base = (base * base) % mod; } return result; } for (let i = 0; i < k; i++) { const a = 2 + Math.floor(Math.random() * (n - 4)); let x = modPow(a, d, n); if (x === 1 || x === n - 1) continue; let composite = True; for (let j = 0; j < r - 1; j++) { x = (x * x) % n; if (x === n - 1) { composite = False; break; } } if (composite) return False; } return True; }",
                "is_correct": True,
            },
            {
                "text": "function millerRabin(n: number): boolean { return n > 1; }",
                "is_correct": False,
            },
            {
                "text": "function millerRabin(n: number): boolean { for (let i = 2; i < n; i++) { if (n % i === 0) return False; } return n > 1; }",
                "is_correct": False,
            },
            {
                "text": "function millerRabin(n: number): boolean { return n % 2 === 1; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Fast Fourier Transform (FFT) algorithm?",
        "explanation": "FFT reduces the complexity of computing Discrete Fourier Transform from O(n²) to O(n log n) using divide and conquer.",
        "reference": "Fast Fourier Transform",
        "points": 2,
        "answers": [
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": True},
            {"text": "O(n³)", "is_correct": False},
            {"text": "O(2^n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Sieve of Eratosthenes algorithm in TypeScript:",
        "explanation": "Sieve of Eratosthenes efficiently finds all prime numbers up to n by iteratively marking multiples of primes.",
        "reference": "Sieve of Eratosthenes",
        "points": 2,
        "answers": [
            {
                "text": "function sieveOfEratosthenes(n: number): number[] { const isPrime = new Array(n + 1).fill(True); isPrime[0] = isPrime[1] = False; for (let i = 2; i * i <= n; i++) { if (isPrime[i]) { for (let j = i * i; j <= n; j += i) { isPrime[j] = False; } } } return isPrime.map((prime, index) => prime ? index : -1).filter(x => x !== -1); }",
                "is_correct": True,
            },
            {
                "text": "function sieveOfEratosthenes(n: number): number[] { const primes = []; for (let i = 2; i <= n; i++) { let isPrime = True; for (let j = 2; j < i; j++) { if (i % j === 0) { isPrime = False; break; } } if (isPrime) primes.push(i); } return primes; }",
                "is_correct": False,
            },
            {
                "text": "function sieveOfEratosthenes(n: number): number[] { return Array.from({length: n}, (_, i) => i + 1).filter(x => x % 2 === 1); }",
                "is_correct": False,
            },
            {
                "text": "function sieveOfEratosthenes(n: number): number[] { return [2, 3, 5, 7]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Johnson's algorithm for all-pairs shortest paths in TypeScript:",
        "explanation": "Johnson's algorithm uses Bellman-Ford to reweight edges, then applies Dijkstra from each vertex for sparse graphs.",
        "reference": "Johnson's Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function johnsonsAlgorithm(graph: [number, number, number][], V: number): number[][] { const extendedEdges = [...graph]; for (let i = 0; i < V; i++) { extendedEdges.push([V, i, 0]); } const bellman = bellmanFord(extendedEdges, V + 1, V); if (bellman.hasNegativeCycle) return []; const h = bellman.distances; const reweightedGraph: number[][] = Array(V).fill(null).map(() => Array(V).fill(Infinity)); for (let i = 0; i < V; i++) reweightedGraph[i][i] = 0; for (const [u, v, w] of graph) { reweightedGraph[u][v] = w + h[u] - h[v]; } const dist: number[][] = Array(V).fill(null).map(() => Array(V).fill(Infinity)); for (let u = 0; u < V; u++) { const dijkstraDist = dijkstra(reweightedGraph, u); for (let v = 0; v < V; v++) { if (dijkstraDist[v] !== Infinity) { dist[u][v] = dijkstraDist[v] - h[u] + h[v]; } } } return dist; }",
                "is_correct": True,
            },
            {
                "text": "function johnsonsAlgorithm(graph: [number, number, number][], V: number): number[][] { return Array(V).fill(null).map(() => Array(V).fill(0)); }",
                "is_correct": False,
            },
            {
                "text": "function johnsonsAlgorithm(graph: [number, number, number][], V: number): number[][] { const dist = Array(V).fill(null).map(() => Array(V).fill(Infinity)); for (const [u, v, w] of graph) { dist[u][v] = w; } return dist; }",
                "is_correct": False,
            },
            {
                "text": "function johnsonsAlgorithm(graph: [number, number, number][], V: number): number[][] { return floydWarshall(graph, V); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements the Reservoir Sampling algorithm?",
        "explanation": "Reservoir Sampling selects k random items from stream of unknown size, ensuring each item has equal probability k/n.",
        "reference": "Reservoir Sampling",
        "points": 2,
        "answers": [
            {
                "text": "function reservoirSample<T>(stream: T[], k: number): T[] { const reservoir: T[] = []; for (let i = 0; i < stream.length; i++) { if (i < k) { reservoir[i] = stream[i]; } else { const j = Math.floor(Math.random() * (i + 1)); if (j < k) { reservoir[j] = stream[i]; } } } return reservoir; }",
                "is_correct": True,
            },
            {
                "text": "function reservoirSample<T>(stream: T[], k: number): T[] { return stream.slice(0, k); }",
                "is_correct": False,
            },
            {
                "text": "function reservoirSample<T>(stream: T[], k: number): T[] { const shuffled = [...stream].sort(() => Math.random() - 0.5); return shuffled.slice(0, k); }",
                "is_correct": False,
            },
            {
                "text": "function reservoirSample<T>(stream: T[], k: number): T[] { return stream.filter((_, i) => i % Math.ceil(stream.length / k) === 0).slice(0, k); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Karatsuba multiplication algorithm in TypeScript:",
        "explanation": "Karatsuba reduces integer multiplication from O(n²) to O(n^1.585) using divide and conquer.",
        "reference": "Karatsuba Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function karatsuba(x: bigint, y: bigint): bigint { if (x < 10n || y < 10n) return x * y; const xStr = x.toString(); const yStr = y.toString(); const n = Math.max(xStr.length, yStr.length); const half = Math.ceil(n / 2); const multiplier = 10n ** BigInt(half); const xHigh = x / multiplier; const xLow = x % multiplier; const yHigh = y / multiplier; const yLow = y % multiplier; const z0 = karatsuba(xLow, yLow); const z1 = karatsuba(xLow + xHigh, yLow + yHigh); const z2 = karatsuba(xHigh, yHigh); return z2 * (10n ** BigInt(2 * half)) + (z1 - z2 - z0) * (10n ** BigInt(half)) + z0; }",
                "is_correct": True,
            },
            {
                "text": "function karatsuba(x: bigint, y: bigint): bigint { return x * y; }",
                "is_correct": False,
            },
            {
                "text": "function karatsuba(x: bigint, y: bigint): bigint { return x + y; }",
                "is_correct": False,
            },
            {
                "text": "function karatsuba(x: bigint, y: bigint): bigint { const str1 = x.toString(); const str2 = y.toString(); return BigInt(str1.length * str2.length); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Pollard's rho algorithm for integer factorization?",
        "explanation": "Pollard's rho algorithm has expected time complexity of O(n^1/4) for factoring integer n.",
        "reference": "Pollard's Rho Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(√n)", "is_correct": False},
            {"text": "O(n^1/4)", "is_correct": True},
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Heap's algorithm for generating all permutations in TypeScript:",
        "explanation": "Heap's algorithm generates all permutations of n objects by minimal changes, using systematic swapping.",
        "reference": "Heap's Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function heapPermutations<T>(arr: T[]): T[][] { const result: T[][] = []; const n = arr.length; function generate(k: number): void { if (k === 1) { result.push([...arr]); return; } generate(k - 1); for (let i = 0; i < k - 1; i++) { if (k % 2 === 0) { [arr[i], arr[k - 1]] = [arr[k - 1], arr[i]]; } else { [arr[0], arr[k - 1]] = [arr[k - 1], arr[0]]; } generate(k - 1); } } generate(n); return result; }",
                "is_correct": True,
            },
            {
                "text": "function heapPermutations<T>(arr: T[]): T[][] { const result: T[][] = []; function backtrack(current: T[]): void { if (current.length === arr.length) { result.push([...current]); return; } for (const item of arr) { if (!current.includes(item)) { current.push(item); backtrack(current); current.pop(); } } } backtrack([]); return result; }",
                "is_correct": False,
            },
            {
                "text": "function heapPermutations<T>(arr: T[]): T[][] { return [arr, [...arr].reverse()]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Monte Carlo algorithm for estimating π in TypeScript:",
        "explanation": "Monte Carlo method estimates π by randomly sampling points in unit square and counting those inside unit circle.",
        "reference": "Monte Carlo Method",
        "points": 2,
        "answers": [
            {
                "text": "function estimatePi(numSamples: number): number { let pointsInCircle = 0; for (let i = 0; i < numSamples; i++) { const x = Math.random() * 2 - 1; const y = Math.random() * 2 - 1; if (x * x + y * y <= 1) { pointsInCircle++; } } return 4 * pointsInCircle / numSamples; }",
                "is_correct": True,
            },
            {
                "text": "function estimatePi(numSamples: number): number { return 3.14159; }",
                "is_correct": False,
            },
            {
                "text": "function estimatePi(numSamples: number): number { return numSamples / 4; }",
                "is_correct": False,
            },
            {
                "text": "function estimatePi(numSamples: number): number { return Math.sqrt(numSamples); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Maximum Bipartite Matching using Ford-Fulkerson?",
        "explanation": "Maximum bipartite matching can be solved using max flow by creating source/sink and unit capacity edges.",
        "reference": "Maximum Bipartite Matching",
        "points": 3,
        "answers": [
            {
                "text": "function maxBipartiteMatching(graph: boolean[][], M: number, N: number): number { const match = new Array(N).fill(-1); let result = 0; function dfs(u: number, visited: boolean[]): boolean { for (let v = 0; v < N; v++) { if (graph[u][v] && !visited[v]) { visited[v] = True; if (match[v] === -1 || dfs(match[v], visited)) { match[v] = u; return True; } } } return False; } for (let u = 0; u < M; u++) { const visited = new Array(N).fill(False); if (dfs(u, visited)) result++; } return result; }",
                "is_correct": True,
            },
            {
                "text": "function maxBipartiteMatching(graph: boolean[][], M: number, N: number): number { return Math.min(M, N); }",
                "is_correct": False,
            },
            {
                "text": "function maxBipartiteMatching(graph: boolean[][], M: number, N: number): number { return graph.flat().filter(x => x).length; }",
                "is_correct": False,
            },
            {
                "text": "function maxBipartiteMatching(graph: boolean[][], M: number, N: number): number { return M + N; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Chinese Remainder Theorem in TypeScript:",
        "explanation": "CRT finds unique solution modulo product of pairwise coprime moduli for system of linear congruences.",
        "reference": "Chinese Remainder Theorem",
        "points": 3,
        "answers": [
            {
                "text": "function chineseRemainderTheorem(remainders: number[], moduli: number[]): number { const n = remainders.length; let result = 0; const product = moduli.reduce((prod, mod) => prod * mod, 1); for (let i = 0; i < n; i++) { const partialProduct = product / moduli[i]; const {x: inverse} = extendedGCD(partialProduct, moduli[i]); result = (result + remainders[i] * partialProduct * inverse) % product; } return ((result % product) + product) % product; }",
                "is_correct": True,
            },
            {
                "text": "function chineseRemainderTheorem(remainders: number[], moduli: number[]): number { return remainders.reduce((sum, rem) => sum + rem, 0) % moduli.reduce((prod, mod) => prod * mod, 1); }",
                "is_correct": False,
            },
            {
                "text": "function chineseRemainderTheorem(remainders: number[], moduli: number[]): number { return Math.max(...remainders); }",
                "is_correct": False,
            },
            {
                "text": "function chineseRemainderTheorem(remainders: number[], moduli: number[]): number { return remainders[0]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Cooley-Tukey FFT algorithm?",
        "explanation": "Cooley-Tukey FFT is the most common FFT algorithm with O(n log n) complexity using radix-2 decomposition.",
        "reference": "Cooley-Tukey FFT",
        "points": 2,
        "answers": [
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": True},
            {"text": "O(n√n)", "is_correct": False},
            {"text": "O(n³)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Simplex algorithm initialization phase in TypeScript:",
        "explanation": "Simplex algorithm Phase I finds initial basic feasible solution by introducing artificial variables.",
        "reference": "Simplex Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function simplexPhaseOne(A: number[][], b: number[], c: number[]): {feasible: boolean, basicSolution?: number[]} { const m = A.length; const n = A[0].length; const tableau: number[][] = []; for (let i = 0; i < m; i++) { tableau[i] = [...A[i], ...new Array(m).fill(0), b[i]]; tableau[i][n + i] = 1; } const objectiveRow = new Array(n + m + 1).fill(0); for (let i = n; i < n + m; i++) { objectiveRow[i] = 1; } tableau.push(objectiveRow); const basis = Array.from({length: m}, (_, i) => n + i); while (True) { const pivotCol = findEnteringVariable(tableau[m]); if (pivotCol === -1) break; const pivotRow = findLeavingVariable(tableau, pivotCol, m); if (pivotRow === -1) return {feasible: False}; pivot(tableau, pivotRow, pivotCol); basis[pivotRow] = pivotCol; } if (Math.abs(tableau[m][tableau[m].length - 1]) > 1e-10) { return {feasible: False}; } const solution = new Array(n).fill(0); for (let i = 0; i < m; i++) { if (basis[i] < n) { solution[basis[i]] = tableau[i][tableau[i].length - 1]; } } return {feasible: True, basicSolution: solution}; }",
                "is_correct": True,
            },
            {
                "text": "function simplexPhaseOne(A: number[][], b: number[], c: number[]): {feasible: boolean} { return {feasible: True}; }",
                "is_correct": False,
            },
            {
                "text": "function simplexPhaseOne(A: number[][], b: number[], c: number[]): {feasible: boolean} { return {feasible: b.every(x => x >= 0)}; }",
                "is_correct": False,
            },
            {
                "text": "function simplexPhaseOne(A: number[][], b: number[], c: number[]): {feasible: boolean} { return {feasible: A.length > 0}; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Viterbi algorithm for Hidden Markov Models in TypeScript:",
        "explanation": "Viterbi algorithm finds most likely sequence of hidden states using dynamic programming on HMM.",
        "reference": "Viterbi Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function viterbi(observations: number[], states: number[], startProb: number[], transProb: number[][], emitProb: number[][]): number[] { const T = observations.length; const N = states.length; const V: number[][] = Array(T).fill(null).map(() => Array(N).fill(0)); const path: number[][] = Array(T).fill(null).map(() => Array(N).fill(0)); for (let s = 0; s < N; s++) { V[0][s] = startProb[s] * emitProb[s][observations[0]]; path[0][s] = s; } for (let t = 1; t < T; t++) { for (let s = 0; s < N; s++) { let maxProb = 0; let maxState = 0; for (let prevS = 0; prevS < N; prevS++) { const prob = V[t-1][prevS] * transProb[prevS][s] * emitProb[s][observations[t]]; if (prob > maxProb) { maxProb = prob; maxState = prevS; } } V[t][s] = maxProb; path[t][s] = maxState; } } let maxProb = 0; let lastState = 0; for (let s = 0; s < N; s++) { if (V[T-1][s] > maxProb) { maxProb = V[T-1][s]; lastState = s; } } const bestPath: number[] = new Array(T); bestPath[T-1] = lastState; for (let t = T-2; t >= 0; t--) { bestPath[t] = path[t+1][bestPath[t+1]]; } return bestPath; }",
                "is_correct": True,
            },
            {
                "text": "function viterbi(observations: number[], states: number[]): number[] { return observations.map(obs => states[obs % states.length]); }",
                "is_correct": False,
            },
            {
                "text": "function viterbi(observations: number[], states: number[]): number[] { return states.slice(0, observations.length); }",
                "is_correct": False,
            },
            {
                "text": "function viterbi(observations: number[], states: number[]): number[] { return new Array(observations.length).fill(0); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements the Needleman-Wunsch algorithm for global sequence alignment?",
        "explanation": "Needleman-Wunsch uses dynamic programming to find optimal global alignment between two sequences.",
        "reference": "Needleman-Wunsch Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function needlemanWunsch(seq1: string, seq2: string, match: number = 2, mismatch: number = -1, gap: number = -1): {score: number, alignment: [string, string]} { const m = seq1.length; const n = seq2.length; const dp = Array(m + 1).fill(null).map(() => Array(n + 1).fill(0)); for (let i = 0; i <= m; i++) dp[i][0] = i * gap; for (let j = 0; j <= n; j++) dp[0][j] = j * gap; for (let i = 1; i <= m; i++) { for (let j = 1; j <= n; j++) { const scoreMatch = dp[i-1][j-1] + (seq1[i-1] === seq2[j-1] ? match : mismatch); const scoreDelete = dp[i-1][j] + gap; const scoreInsert = dp[i][j-1] + gap; dp[i][j] = Math.max(scoreMatch, scoreDelete, scoreInsert); } } let i = m, j = n; let align1 = '', align2 = ''; while (i > 0 || j > 0) { if (i > 0 && j > 0 && dp[i][j] === dp[i-1][j-1] + (seq1[i-1] === seq2[j-1] ? match : mismatch)) { align1 = seq1[i-1] + align1; align2 = seq2[j-1] + align2; i--; j--; } else if (i > 0 && dp[i][j] === dp[i-1][j] + gap) { align1 = seq1[i-1] + align1; align2 = '-' + align2; i--; } else { align1 = '-' + align1; align2 = seq2[j-1] + align2; j--; } } return {score: dp[m][n], alignment: [align1, align2]}; }",
                "is_correct": True,
            },
            {
                "text": "function needlemanWunsch(seq1: string, seq2: string): {score: number, alignment: [string, string]} { return {score: 0, alignment: [seq1, seq2]}; }",
                "is_correct": False,
            },
            {
                "text": "function needlemanWunsch(seq1: string, seq2: string): {score: number, alignment: [string, string]} { const score = seq1.length + seq2.length; return {score, alignment: [seq1, seq2]}; }",
                "is_correct": False,
            },
            {
                "text": "function needlemanWunsch(seq1: string, seq2: string): {score: number, alignment: [string, string]} { let score = 0; for (let i = 0; i < Math.min(seq1.length, seq2.length); i++) { if (seq1[i] === seq2[i]) score++; } return {score, alignment: [seq1, seq2]}; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the RANSAC algorithm for robust parameter estimation in TypeScript:",
        "explanation": "RANSAC iteratively estimates parameters by randomly sampling minimal data points and counting inliers.",
        "reference": "RANSAC Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function ransac(points: [number, number][], iterations: number = 1000, threshold: number = 1.0): {slope: number, intercept: number, inliers: [number, number][]} { let bestModel = {slope: 0, intercept: 0, inliers: [] as [number, number][]}; let maxInliers = 0; function fitLine(p1: [number, number], p2: [number, number]): {slope: number, intercept: number} { const slope = (p2[1] - p1[1]) / (p2[0] - p1[0]); const intercept = p1[1] - slope * p1[0]; return {slope, intercept}; } function distanceToLine(point: [number, number], slope: number, intercept: number): number { const [x, y] = point; return Math.abs(y - slope * x - intercept) / Math.sqrt(slope * slope + 1); } for (let iter = 0; iter < iterations; iter++) { const idx1 = Math.floor(Math.random() * points.length); let idx2 = Math.floor(Math.random() * points.length); while (idx2 === idx1) idx2 = Math.floor(Math.random() * points.length); const {slope, intercept} = fitLine(points[idx1], points[idx2]); const inliers = points.filter(point => distanceToLine(point, slope, intercept) <= threshold); if (inliers.length > maxInliers) { maxInliers = inliers.length; bestModel = {slope, intercept, inliers}; } } return bestModel; }",
                "is_correct": True,
            },
            {
                "text": "function ransac(points: [number, number][]): {slope: number, intercept: number} { const firstPoint = points[0]; const lastPoint = points[points.length - 1]; const slope = (lastPoint[1] - firstPoint[1]) / (lastPoint[0] - firstPoint[0]); return {slope, intercept: firstPoint[1] - slope * firstPoint[0]}; }",
                "is_correct": False,
            },
            {
                "text": "function ransac(points: [number, number][]): {slope: number, intercept: number} { return {slope: 1, intercept: 0}; }",
                "is_correct": False,
            },
            {
                "text": "function ransac(points: [number, number][]): {slope: number, intercept: number} { const avgX = points.reduce((sum, p) => sum + p[0], 0) / points.length; const avgY = points.reduce((sum, p) => sum + p[1], 0) / points.length; return {slope: avgY / avgX, intercept: 0}; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Karger's algorithm for minimum cut in a graph?",
        "explanation": "Karger's algorithm has O(n²) time complexity per iteration and needs O(n² log n) iterations for high success probability.",
        "reference": "Karger's Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n⁴ log n)", "is_correct": True},
            {"text": "O(n³)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Randomized Quickselect algorithm in TypeScript:",
        "explanation": "Randomized Quickselect finds k-th smallest element in expected O(n) time using random pivot selection.",
        "reference": "Randomized Quickselect",
        "points": 2,
        "answers": [
            {
                "text": "function quickselect(arr: number[], k: number, left: number = 0, right: number = arr.length - 1): number { if (left === right) return arr[left]; const pivotIndex = left + Math.floor(Math.random() * (right - left + 1)); const newPivotIndex = partition(arr, left, right, pivotIndex); if (k === newPivotIndex) { return arr[k]; } else if (k < newPivotIndex) { return quickselect(arr, k, left, newPivotIndex - 1); } else { return quickselect(arr, k, newPivotIndex + 1, right); } } function partition(arr: number[], left: number, right: number, pivotIndex: number): number { const pivotValue = arr[pivotIndex]; [arr[pivotIndex], arr[right]] = [arr[right], arr[pivotIndex]]; let storeIndex = left; for (let i = left; i < right; i++) { if (arr[i] < pivotValue) { [arr[storeIndex], arr[i]] = [arr[i], arr[storeIndex]]; storeIndex++; } } [arr[right], arr[storeIndex]] = [arr[storeIndex], arr[right]]; return storeIndex; }",
                "is_correct": True,
            },
            {
                "text": "function quickselect(arr: number[], k: number): number { arr.sort((a, b) => a - b); return arr[k]; }",
                "is_correct": False,
            },
            {
                "text": "function quickselect(arr: number[], k: number): number { return Math.min(...arr); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Simulated Annealing algorithm for optimization in TypeScript:",
        "explanation": "Simulated Annealing accepts worse solutions with decreasing probability to escape local optima.",
        "reference": "Simulated Annealing",
        "points": 3,
        "answers": [
            {
                "text": "function simulatedAnnealing(objective: (x: number[]) => number, initial: number[], maxIterations: number = 10000): number[] { let current = [...initial]; let currentCost = objective(current); let best = [...current]; let bestCost = currentCost; let temperature = 100; const coolingRate = 0.995; for (let iter = 0; iter < maxIterations; iter++) { const neighbor = current.map(x => x + (Math.random() - 0.5) * 2); const neighborCost = objective(neighbor); const deltaE = neighborCost - currentCost; if (deltaE < 0 || Math.random() < Math.exp(-deltaE / temperature)) { current = neighbor; currentCost = neighborCost; if (currentCost < bestCost) { best = [...current]; bestCost = currentCost; } } temperature *= coolingRate; } return best; }",
                "is_correct": True,
            },
            {
                "text": "function simulatedAnnealing(objective: (x: number[]) => number, initial: number[]): number[] { return initial; }",
                "is_correct": False,
            },
            {
                "text": "function simulatedAnnealing(objective: (x: number[]) => number, initial: number[]): number[] { let best = initial; for (let i = 0; i < 100; i++) { const candidate = initial.map(x => x + Math.random()); if (objective(candidate) < objective(best)) best = candidate; } return best; }",
                "is_correct": False,
            },
            {
                "text": "function simulatedAnnealing(objective: (x: number[]) => number, initial: number[]): number[] { return initial.map(x => x * Math.random()); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Stable Marriage Problem using Gale-Shapley algorithm?",
        "explanation": "Gale-Shapley algorithm finds stable matching between two sets by having one side propose and the other accept/reject.",
        "reference": "Gale-Shapley Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function stableMarriage(menPrefs: number[][], womenPrefs: number[][]): number[] { const n = menPrefs.length; const womanPartner = new Array(n).fill(-1); const manPartner = new Array(n).fill(-1); const menNextProposal = new Array(n).fill(0); const freeMen = Array.from({length: n}, (_, i) => i); function womanPrefers(woman: number, man1: number, man2: number): boolean { const prefs = womenPrefs[woman]; return prefs.indexOf(man1) < prefs.indexOf(man2); } while (freeMen.length > 0) { const man = freeMen.shift()!; const woman = menPrefs[man][menNextProposal[man]]; menNextProposal[man]++; if (womanPartner[woman] === -1) { womanPartner[woman] = man; manPartner[man] = woman; } else { const currentPartner = womanPartner[woman]; if (womanPrefers(woman, man, currentPartner)) { womanPartner[woman] = man; manPartner[man] = woman; manPartner[currentPartner] = -1; freeMen.push(currentPartner); } else { freeMen.push(man); } } } return manPartner; }",
                "is_correct": True,
            },
            {
                "text": "function stableMarriage(menPrefs: number[][], womenPrefs: number[][]): number[] { return menPrefs.map((_, i) => i); }",
                "is_correct": False,
            },
            {
                "text": "function stableMarriage(menPrefs: number[][], womenPrefs: number[][]): number[] { return menPrefs.map(prefs => prefs[0]); }",
                "is_correct": False,
            },
            {
                "text": "function stableMarriage(menPrefs: number[][], womenPrefs: number[][]): number[] { return new Array(menPrefs.length).fill(0); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Genetic Algorithm for optimization in TypeScript:",
        "explanation": "Genetic Algorithm evolves population of solutions using selection, crossover, and mutation operations.",
        "reference": "Genetic Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function geneticAlgorithm(fitness: (individual: number[]) => number, populationSize: number, chromosomeLength: number, generations: number): number[] { let population = Array(populationSize).fill(null).map(() => Array(chromosomeLength).fill(null).map(() => Math.random() > 0.5 ? 1 : 0)); function selection(pop: number[][]): number[] { const fitnesses = pop.map(fitness); const totalFitness = fitnesses.reduce((sum, f) => sum + f, 0); let r = Math.random() * totalFitness; for (let i = 0; i < pop.length; i++) { r -= fitnesses[i]; if (r <= 0) return pop[i]; } return pop[pop.length - 1]; } function crossover(parent1: number[], parent2: number[]): [number[], number[]] { const crossoverPoint = Math.floor(Math.random() * chromosomeLength); const child1 = [...parent1.slice(0, crossoverPoint), ...parent2.slice(crossoverPoint)]; const child2 = [...parent2.slice(0, crossoverPoint), ...parent1.slice(crossoverPoint)]; return [child1, child2]; } function mutate(individual: number[], mutationRate: number = 0.01): number[] { return individual.map(gene => Math.random() < mutationRate ? 1 - gene : gene); } for (let gen = 0; gen < generations; gen++) { const newPopulation: number[][] = []; while (newPopulation.length < populationSize) { const parent1 = selection(population); const parent2 = selection(population); const [child1, child2] = crossover(parent1, parent2); newPopulation.push(mutate(child1)); if (newPopulation.length < populationSize) { newPopulation.push(mutate(child2)); } } population = newPopulation; } return population.reduce((best, individual) => fitness(individual) > fitness(best) ? individual : best); }",
                "is_correct": True,
            },
            {
                "text": "function geneticAlgorithm(fitness: (individual: number[]) => number, populationSize: number, chromosomeLength: number): number[] { return new Array(chromosomeLength).fill(1); }",
                "is_correct": False,
            },
            {
                "text": "function geneticAlgorithm(fitness: (individual: number[]) => number, populationSize: number, chromosomeLength: number): number[] { return Array(chromosomeLength).fill(null).map(() => Math.random() > 0.5 ? 1 : 0); }",
                "is_correct": False,
            },
            {
                "text": "function geneticAlgorithm(fitness: (individual: number[]) => number, populationSize: number, chromosomeLength: number): number[] { return Array.from({length: chromosomeLength}, (_, i) => i % 2); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the expected time complexity of Skip List search operation?",
        "explanation": "Skip List maintains multiple levels of linked lists, providing O(log n) expected search time.",
        "reference": "Skip List complexity",
        "points": 2,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(√n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Particle Swarm Optimization algorithm in TypeScript:",
        "explanation": "PSO optimizes by simulating social behavior of particles moving through solution space with velocity updates.",
        "reference": "Particle Swarm Optimization",
        "points": 3,
        "answers": [
            {
                "text": "function particleSwarmOptimization(objective: (x: number[]) => number, dimensions: number, numParticles: number = 30, maxIterations: number = 1000): number[] { const particles = Array(numParticles).fill(null).map(() => ({ position: Array(dimensions).fill(null).map(() => Math.random() * 20 - 10), velocity: Array(dimensions).fill(null).map(() => Math.random() * 2 - 1), bestPosition: Array(dimensions).fill(0), bestFitness: Infinity })); let globalBestPosition = Array(dimensions).fill(0); let globalBestFitness = Infinity; const w = 0.729; const c1 = 1.49445; const c2 = 1.49445; for (const particle of particles) { particle.bestPosition = [...particle.position]; particle.bestFitness = objective(particle.position); if (particle.bestFitness < globalBestFitness) { globalBestFitness = particle.bestFitness; globalBestPosition = [...particle.bestPosition]; } } for (let iter = 0; iter < maxIterations; iter++) { for (const particle of particles) { for (let d = 0; d < dimensions; d++) { const r1 = Math.random(); const r2 = Math.random(); particle.velocity[d] = w * particle.velocity[d] + c1 * r1 * (particle.bestPosition[d] - particle.position[d]) + c2 * r2 * (globalBestPosition[d] - particle.position[d]); particle.position[d] += particle.velocity[d]; } const fitness = objective(particle.position); if (fitness < particle.bestFitness) { particle.bestFitness = fitness; particle.bestPosition = [...particle.position]; if (fitness < globalBestFitness) { globalBestFitness = fitness; globalBestPosition = [...particle.bestPosition]; } } } } return globalBestPosition; }",
                "is_correct": True,
            },
            {
                "text": "function particleSwarmOptimization(objective: (x: number[]) => number, dimensions: number): number[] { return new Array(dimensions).fill(0); }",
                "is_correct": False,
            },
            {
                "text": "function particleSwarmOptimization(objective: (x: number[]) => number, dimensions: number): number[] { return Array(dimensions).fill(null).map(() => Math.random()); }",
                "is_correct": False,
            },
            {
                "text": "function particleSwarmOptimization(objective: (x: number[]) => number, dimensions: number): number[] { let best = Array(dimensions).fill(1); for (let i = 0; i < 100; i++) { const candidate = Array(dimensions).fill(null).map(() => Math.random()); if (objective(candidate) < objective(best)) best = candidate; } return best; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Ant Colony Optimization algorithm for TSP in TypeScript:",
        "explanation": "ACO uses artificial ants that deposit pheromones to find good solutions collaboratively over iterations.",
        "reference": "Ant Colony Optimization",
        "points": 3,
        "answers": [
            {
                "text": "function antColonyOptimization(distances: number[][], numAnts: number = 10, numIterations: number = 100): number[] { const n = distances.length; let pheromones = Array(n).fill(null).map(() => Array(n).fill(1.0)); const alpha = 1; const beta = 2; const evaporation = 0.5; const Q = 100; let bestTour: number[] = []; let bestLength = Infinity; function calculateProbability(from: number, to: number, visited: boolean[]): number { if (visited[to]) return 0; const pheromone = Math.pow(pheromones[from][to], alpha); const heuristic = Math.pow(1.0 / distances[from][to], beta); return pheromone * heuristic; } function selectNextCity(currentCity: number, visited: boolean[]): number { const probabilities: number[] = []; let sum = 0; for (let i = 0; i < n; i++) { const prob = calculateProbability(currentCity, i, visited); probabilities[i] = prob; sum += prob; } if (sum === 0) { for (let i = 0; i < n; i++) { if (!visited[i]) return i; } return -1; } const r = Math.random() * sum; let cumulative = 0; for (let i = 0; i < n; i++) { cumulative += probabilities[i]; if (r <= cumulative) return i; } return n - 1; } for (let iter = 0; iter < numIterations; iter++) { const antTours: number[][] = []; const antLengths: number[] = []; for (let ant = 0; ant < numAnts; ant++) { const visited = new Array(n).fill(False); const tour = [0]; visited[0] = True; let currentCity = 0; while (tour.length < n) { const nextCity = selectNextCity(currentCity, visited); if (nextCity === -1) break; tour.push(nextCity); visited[nextCity] = True; currentCity = nextCity; } let length = 0; for (let i = 0; i < tour.length - 1; i++) { length += distances[tour[i]][tour[i + 1]]; } length += distances[tour[tour.length - 1]][tour[0]]; antTours.push(tour); antLengths.push(length); if (length < bestLength) { bestLength = length; bestTour = [...tour]; } } for (let i = 0; i < n; i++) { for (let j = 0; j < n; j++) { pheromones[i][j] *= (1 - evaporation); } } for (let ant = 0; ant < numAnts; ant++) { const tour = antTours[ant]; const length = antLengths[ant]; const deposit = Q / length; for (let i = 0; i < tour.length - 1; i++) { pheromones[tour[i]][tour[i + 1]] += deposit; pheromones[tour[i + 1]][tour[i]] += deposit; } pheromones[tour[tour.length - 1]][tour[0]] += deposit; pheromones[tour[0]][tour[tour.length - 1]] += deposit; } } return bestTour; }",
                "is_correct": True,
            },
            {
                "text": "function antColonyOptimization(distances: number[][]): number[] { return Array.from({length: distances.length}, (_, i) => i); }",
                "is_correct": False,
            },
            {
                "text": "function antColonyOptimization(distances: number[][]): number[] { return [0, 1, 2, 3]; }",
                "is_correct": False,
            },
            {
                "text": "function antColonyOptimization(distances: number[][]): number[] { const n = distances.length; return Array(n).fill(null).map(() => Math.floor(Math.random() * n)); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly solves the Closest Pair of Points problem using divide and conquer?",
        "explanation": "Closest pair divide and conquer splits points by x-coordinate and efficiently checks points near the dividing line.",
        "reference": "Closest Pair Divide and Conquer",
        "points": 3,
        "answers": [
            {
                "text": "function closestPair(points: [number, number][]): number { function distance(p1: [number, number], p2: [number, number]): number { return Math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2); } function bruteForce(pts: [number, number][]): number { let minDist = Infinity; for (let i = 0; i < pts.length; i++) { for (let j = i + 1; j < pts.length; j++) { minDist = Math.min(minDist, distance(pts[i], pts[j])); } } return minDist; } function closestRec(px: [number, number][], py: [number, number][]): number { const n = px.length; if (n <= 3) return bruteForce(px); const mid = Math.floor(n / 2); const midPoint = px[mid]; const pyl: [number, number][] = []; const pyr: [number, number][] = []; for (const point of py) { if (point[0] <= midPoint[0]) pyl.push(point); else pyr.push(point); } const dl = closestRec(px.slice(0, mid), pyl); const dr = closestRec(px.slice(mid), pyr); const d = Math.min(dl, dr); const strip: [number, number][] = []; for (const point of py) { if (Math.abs(point[0] - midPoint[0]) < d) { strip.push(point); } } let minStrip = d; for (let i = 0; i < strip.length; i++) { for (let j = i + 1; j < strip.length && (strip[j][1] - strip[i][1]) < minStrip; j++) { minStrip = Math.min(minStrip, distance(strip[i], strip[j])); } } return minStrip; } const px = [...points].sort((a, b) => a[0] - b[0]); const py = [...points].sort((a, b) => a[1] - b[1]); return closestRec(px, py); }",
                "is_correct": True,
            },
            {
                "text": "function closestPair(points: [number, number][]): number { let minDist = Infinity; for (let i = 0; i < points.length; i++) { for (let j = i + 1; j < points.length; j++) { const dist = Math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2); minDist = Math.min(minDist, dist); } } return minDist; }",
                "is_correct": False,
            },
            {
                "text": "function closestPair(points: [number, number][]): number { return 1; }",
                "is_correct": False,
            },
            {
                "text": "function closestPair(points: [number, number][]): number { return Math.min(...points.map(p => p[0] + p[1])); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement the Branch and Bound algorithm for 0/1 Knapsack in TypeScript:",
        "explanation": "Branch and Bound explores solution tree systematically, pruning branches that cannot lead to optimal solutions.",
        "reference": "Branch and Bound",
        "points": 3,
        "answers": [
            {
                "text": "function knapsackBranchBound(weights: number[], values: number[], capacity: number): number { interface Node { level: number; profit: number; weight: number; bound: number; } function bound(node: Node): number { if (node.weight >= capacity) return 0; let remainingCapacity = capacity - node.weight; let boundValue = node.profit; let i = node.level + 1; while (i < weights.length && weights[i] <= remainingCapacity) { remainingCapacity -= weights[i]; boundValue += values[i]; i++; } if (i < weights.length) { boundValue += (remainingCapacity / weights[i]) * values[i]; } return boundValue; } const items = Array.from({length: weights.length}, (_, i) => ({weight: weights[i], value: values[i], ratio: values[i] / weights[i], index: i})); items.sort((a, b) => b.ratio - a.ratio); const sortedWeights = items.map(item => item.weight); const sortedValues = items.map(item => item.value); const queue: Node[] = []; let maxProfit = 0; const root: Node = {level: -1, profit: 0, weight: 0, bound: 0}; root.bound = bound(root); queue.push(root); while (queue.length > 0) { const current = queue.shift()!; if (current.bound > maxProfit) { const with: Node = {level: current.level + 1, profit: current.profit + sortedValues[current.level + 1], weight: current.weight + sortedWeights[current.level + 1], bound: 0}; if (with.weight <= capacity && with.profit > maxProfit) { maxProfit = with.profit; } with.bound = bound(with); if (with.bound > maxProfit) { queue.push(with); } const without: Node = {level: current.level + 1, profit: current.profit, weight: current.weight, bound: 0}; without.bound = bound(without); if (without.bound > maxProfit) { queue.push(without); } } } return maxProfit; }",
                "is_correct": True,
            },
            {
                "text": "function knapsackBranchBound(weights: number[], values: number[], capacity: number): number { return Math.max(...values); }",
                "is_correct": False,
            },
            {
                "text": "function knapsackBranchBound(weights: number[], values: number[], capacity: number): number { return values.reduce((sum, val) => sum + val, 0); }",
                "is_correct": False,
            },
            {
                "text": "function knapsackBranchBound(weights: number[], values: number[], capacity: number): number { return capacity; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of the Median of Medians algorithm for selection?",
        "explanation": "Median of Medians guarantees worst-case O(n) time for finding k-th smallest element by ensuring good pivot selection.",
        "reference": "Median of Medians",
        "points": 2,
        "answers": [
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement the Hopcroft-Karp algorithm for maximum bipartite matching in TypeScript:",
        "explanation": "Hopcroft-Karp improves upon Ford-Fulkerson by finding multiple augmenting paths in each iteration using BFS.",
        "reference": "Hopcroft-Karp Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "function hopcroftKarp(graph: number[][], n: number, m: number): number { const pairU = new Array(n + 1).fill(0); const pairV = new Array(m + 1).fill(0); const dist = new Array(n + 1).fill(0); const NIL = 0; function bfs(): boolean { const queue: number[] = []; for (let u = 1; u <= n; u++) { if (pairU[u] === NIL) { dist[u] = 0; queue.push(u); } else { dist[u] = Infinity; } } dist[NIL] = Infinity; while (queue.length > 0) { const u = queue.shift()!; if (dist[u] < dist[NIL]) { for (const v of graph[u - 1]) { if (dist[pairV[v]] === Infinity) { dist[pairV[v]] = dist[u] + 1; queue.push(pairV[v]); } } } } return dist[NIL] !== Infinity; } function dfs(u: number): boolean { if (u !== NIL) { for (const v of graph[u - 1]) { if (dist[pairV[v]] === dist[u] + 1) { if (dfs(pairV[v])) { pairV[v] = u; pairU[u] = v; return True; } } } dist[u] = Infinity; return False; } return True; } let matching = 0; while (bfs()) { for (let u = 1; u <= n; u++) { if (pairU[u] === NIL && dfs(u)) { matching++; } } } return matching; }",
                "is_correct": True,
            },
            {
                "text": "function hopcroftKarp(graph: number[][], n: number, m: number): number { return Math.min(n, m); }",
                "is_correct": False,
            },
            {
                "text": "function hopcroftKarp(graph: number[][], n: number, m: number): number { return graph.flat().length; }",
                "is_correct": False,
            },
            {
                "text": "function hopcroftKarp(graph: number[][], n: number, m: number): number { return n + m; }",
                "is_correct": False,
            },
        ],
    },
]
