"""Advanced Data Structures Certification"""

CERTIFICATION = {
    "name": "Advanced Data Structures",
    "description": "Advanced data structures including heaps, tries, balanced trees, and graph representations",
    "slug": "advanced-data-structures",
    "level": "Professional",
    "duration": 213,
    "questions_count": 71,
    "category_slug": "data-structures-algorithms",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the time complexity of inserting into a min-heap?",
        "explanation": "Inserting into a heap requires adding the element at the end and bubbling up, which takes O(log n) time.",
        "reference": "https://en.wikipedia.org/wiki/Binary_heap",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "Which data structure is most efficient for prefix matching in strings?",
        "explanation": "A Trie (prefix tree) is specifically designed for efficient prefix matching and string operations.",
        "reference": "https://en.wikipedia.org/wiki/Trie",
        "points": 1,
        "answers": [
            {"text": "Hash Table", "is_correct": False},
            {"text": "Binary Search Tree", "is_correct": False},
            {"text": "Trie", "is_correct": True},
            {"text": "Array", "is_correct": False},
        ],
    },
    {
        "text": "Implement a basic Trie node structure in TypeScript:",
        "explanation": "A Trie node contains children map and an end-of-word flag. This structure allows efficient prefix operations.",
        "reference": "TypeScript Trie implementation",
        "points": 2,
        "answers": [
            {
                "text": "class TrieNode { children: {[key: string]: TrieNode} = {}; isEndOfWord: boolean = False; }",
                "is_correct": True,
            },
            {
                "text": "class TrieNode { children: TrieNode[] = []; isEndOfWord: boolean = False; }",
                "is_correct": False,
            },
            {
                "text": "class TrieNode { left: TrieNode; right: TrieNode; value: string; }",
                "is_correct": False,
            },
            {
                "text": "class TrieNode { data: string; next: TrieNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the correct TypeScript implementation for inserting into a max heap?",
        "explanation": "Max heap insertion involves adding at the end and bubbling up while parent is smaller.",
        "reference": "Binary Heap operations",
        "points": 3,
        "answers": [
            {
                "text": "insert(val: number) { this.heap.push(val); this.bubbleUp(this.heap.length - 1); }",
                "is_correct": True,
            },
            {
                "text": "insert(val: number) { this.heap.unshift(val); this.bubbleDown(0); }",
                "is_correct": False,
            },
            {
                "text": "insert(val: number) { this.heap.splice(0, 0, val); }",
                "is_correct": False,
            },
            {
                "text": "insert(val: number) { this.heap[0] = val; this.heapify(); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Red-Black tree node?",
        "explanation": "Red-Black tree nodes need color property, value, and left/right children with null handling.",
        "reference": "Red-Black Tree implementation",
        "points": 2,
        "answers": [
            {
                "text": "class RBNode { color: 'red' | 'black'; value: number; left: RBNode | null; right: RBNode | null; }",
                "is_correct": True,
            },
            {
                "text": "class RBNode { isRed: boolean; value: number; children: RBNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class RBNode { balance: number; value: number; left: RBNode; right: RBNode; }",
                "is_correct": False,
            },
            {
                "text": "class RBNode { color: string; data: any; next: RBNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of searching in a B-tree with height h?",
        "explanation": "B-tree search involves traversing from root to leaf, taking O(log n) time due to its balanced nature.",
        "reference": "B-tree operations",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(h)", "is_correct": False},
        ],
    },
    {
        "text": "Implement a TypeScript method to check if a binary tree is a valid BST:",
        "explanation": "BST validation requires checking that all nodes satisfy the BST property within their valid range.",
        "reference": "Binary Search Tree validation",
        "points": 3,
        "answers": [
            {
                "text": "isValidBST(node: TreeNode | null, min = -Infinity, max = Infinity): boolean { if (!node) return True; return node.val > min && node.val < max && this.isValidBST(node.left, min, node.val) && this.isValidBST(node.right, node.val, max); }",
                "is_correct": True,
            },
            {
                "text": "isValidBST(node: TreeNode): boolean { return node.left.val < node.val && node.val < node.right.val; }",
                "is_correct": False,
            },
            {
                "text": "isValidBST(node: TreeNode): boolean { return this.inorderTraversal(node).every((val, i, arr) => i === 0 || arr[i-1] < val); }",
                "is_correct": False,
            },
            {
                "text": "isValidBST(node: TreeNode): boolean { return node.val > 0; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly represents a Disjoint Set (Union-Find)?",
        "explanation": "Union-Find needs parent array and rank/size for optimization, with path compression in find operation.",
        "reference": "Disjoint Set data structure",
        "points": 2,
        "answers": [
            {
                "text": "class UnionFind { parent: number[]; rank: number[]; find(x: number): number { if (this.parent[x] !== x) this.parent[x] = this.find(this.parent[x]); return this.parent[x]; } }",
                "is_correct": True,
            },
            {
                "text": "class UnionFind { nodes: Set<number>; find(x: number): number { return x; } }",
                "is_correct": False,
            },
            {
                "text": "class UnionFind { graph: number[][]; find(x: number): number { return this.graph[x][0]; } }",
                "is_correct": False,
            },
            {
                "text": "class UnionFind { parent: Map<number, number>; find(x: number): number { return this.parent.get(x) || x; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of an adjacency matrix for a graph with V vertices?",
        "explanation": "Adjacency matrix requires V×V space regardless of the number of edges in the graph.",
        "reference": "Graph representations",
        "points": 1,
        "answers": [
            {"text": "O(V)", "is_correct": False},
            {"text": "O(E)", "is_correct": False},
            {"text": "O(V²)", "is_correct": True},
            {"text": "O(V + E)", "is_correct": False},
        ],
    },
    {
        "text": "Implement a TypeScript class for a Segment Tree node:",
        "explanation": "Segment Tree nodes store range information and values for efficient range queries and updates.",
        "reference": "Segment Tree implementation",
        "points": 2,
        "answers": [
            {
                "text": "class SegmentTreeNode { start: number; end: number; sum: number; left: SegmentTreeNode | null; right: SegmentTreeNode | null; }",
                "is_correct": True,
            },
            {
                "text": "class SegmentTreeNode { value: number; children: SegmentTreeNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class SegmentTreeNode { data: number[]; index: number; }",
                "is_correct": False,
            },
            {
                "text": "class SegmentTreeNode { min: number; max: number; parent: SegmentTreeNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a circular buffer (ring buffer)?",
        "explanation": "Circular buffer uses modulo arithmetic to wrap around when reaching buffer capacity.",
        "reference": "Circular Buffer implementation",
        "points": 2,
        "answers": [
            {
                "text": "class CircularBuffer<T> { private buffer: T[]; private head = 0; private tail = 0; private size = 0; enqueue(item: T) { this.buffer[this.tail] = item; this.tail = (this.tail + 1) % this.buffer.length; if (this.size < this.buffer.length) this.size++; else this.head = (this.head + 1) % this.buffer.length; } }",
                "is_correct": True,
            },
            {
                "text": "class CircularBuffer<T> { private buffer: T[]; push(item: T) { this.buffer.push(item); if (this.buffer.length > 10) this.buffer.shift(); } }",
                "is_correct": False,
            },
            {
                "text": "class CircularBuffer<T> { private buffer: T[] = []; add(item: T) { this.buffer[this.buffer.length] = item; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the optimal TypeScript implementation for a Binary Indexed Tree (Fenwick Tree)?",
        "explanation": "BIT uses 1-based indexing and bit manipulation for efficient prefix sum queries and updates.",
        "reference": "Binary Indexed Tree",
        "points": 3,
        "answers": [
            {
                "text": "class BIT { private tree: number[]; update(i: number, delta: number) { for (i++; i < this.tree.length; i += i & -i) this.tree[i] += delta; } query(i: number): number { let sum = 0; for (i++; i > 0; i -= i & -i) sum += this.tree[i]; return sum; } }",
                "is_correct": True,
            },
            {
                "text": "class BIT { private tree: number[]; update(i: number, val: number) { this.tree[i] = val; } query(i: number): number { return this.tree.slice(0, i+1).reduce((a, b) => a + b, 0); } }",
                "is_correct": False,
            },
            {
                "text": "class BIT { private tree: number[]; update(i: number, val: number) { this.tree[i] += val; } query(i: number): number { return this.tree[i]; } }",
                "is_correct": False,
            },
            {
                "text": "class BIT { private tree: Map<number, number>; update(i: number, val: number) { this.tree.set(i, val); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements AVL tree rotation?",
        "explanation": "AVL tree right rotation involves updating parent-child relationships and recalculating heights.",
        "reference": "AVL Tree rotations",
        "points": 3,
        "answers": [
            {
                "text": "rightRotate(y: AVLNode): AVLNode { const x = y.left!; y.left = x.right; x.right = y; y.height = Math.max(this.getHeight(y.left), this.getHeight(y.right)) + 1; x.height = Math.max(this.getHeight(x.left), this.getHeight(x.right)) + 1; return x; }",
                "is_correct": True,
            },
            {
                "text": "rightRotate(node: AVLNode): AVLNode { const temp = node.right; node.right = temp.left; temp.left = node; return temp; }",
                "is_correct": False,
            },
            {
                "text": "rightRotate(node: AVLNode): AVLNode { [node.left, node.right] = [node.right, node.left]; return node; }",
                "is_correct": False,
            },
            {
                "text": "rightRotate(node: AVLNode): AVLNode { node.balance++; return node; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of building a suffix array using the naive approach?",
        "explanation": "Naive suffix array construction involves sorting all suffixes, which takes O(n² log n) time.",
        "reference": "Suffix Array algorithms",
        "points": 2,
        "answers": [
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n² log n)", "is_correct": True},
            {"text": "O(n³)", "is_correct": False},
        ],
    },
    {
        "text": "Implement a TypeScript class for a Bloom Filter:",
        "explanation": "Bloom Filter uses multiple hash functions and a bit array for probabilistic membership testing.",
        "reference": "Bloom Filter data structure",
        "points": 3,
        "answers": [
            {
                "text": "class BloomFilter { private bitArray: boolean[]; private hashFunctions: ((x: string) => number)[]; add(item: string) { this.hashFunctions.forEach(hash => { this.bitArray[hash(item) % this.bitArray.length] = True; }); } contains(item: string): boolean { return this.hashFunctions.every(hash => this.bitArray[hash(item) % this.bitArray.length]); } }",
                "is_correct": True,
            },
            {
                "text": "class BloomFilter { private set: Set<string>; add(item: string) { this.set.add(item); } contains(item: string): boolean { return this.set.has(item); } }",
                "is_correct": False,
            },
            {
                "text": "class BloomFilter { private array: string[]; add(item: string) { this.array.push(item); } }",
                "is_correct": False,
            },
            {
                "text": "class BloomFilter { private map: Map<string, boolean>; add(item: string) { this.map.set(item, True); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the optimal data structure for implementing an LRU Cache in TypeScript?",
        "explanation": "LRU Cache requires O(1) access, insertion, and deletion, achievable with HashMap + Doubly Linked List.",
        "reference": "LRU Cache implementation",
        "points": 2,
        "answers": [
            {"text": "HashMap + Doubly Linked List", "is_correct": True},
            {"text": "Array + HashMap", "is_correct": False},
            {"text": "Binary Search Tree", "is_correct": False},
            {"text": "Priority Queue", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Skip List node:",
        "explanation": "Skip List nodes contain value and multiple forward pointers for different levels.",
        "reference": "Skip List data structure",
        "points": 2,
        "answers": [
            {
                "text": "class SkipListNode { value: number; forward: (SkipListNode | null)[]; constructor(value: number, level: number) { this.value = value; this.forward = new Array(level + 1).fill(null); } }",
                "is_correct": True,
            },
            {
                "text": "class SkipListNode { value: number; next: SkipListNode | null; prev: SkipListNode | null; }",
                "is_correct": False,
            },
            {
                "text": "class SkipListNode { value: number; children: SkipListNode[]; parent: SkipListNode; }",
                "is_correct": False,
            },
            {
                "text": "class SkipListNode { data: number; level: number; link: SkipListNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles collision resolution in a Hash Table using chaining?",
        "explanation": "Chaining uses arrays or linked lists at each bucket to store multiple elements that hash to the same index.",
        "reference": "Hash Table collision resolution",
        "points": 2,
        "answers": [
            {
                "text": "class HashTable<T> { private buckets: T[][] = []; put(key: string, value: T) { const index = this.hash(key); if (!this.buckets[index]) this.buckets[index] = []; this.buckets[index].push(value); } }",
                "is_correct": True,
            },
            {
                "text": "class HashTable<T> { private buckets: T[] = []; put(key: string, value: T) { let index = this.hash(key); while (this.buckets[index]) index++; this.buckets[index] = value; } }",
                "is_correct": False,
            },
            {
                "text": "class HashTable<T> { private map: Map<string, T> = new Map(); put(key: string, value: T) { this.map.set(key, value); } }",
                "is_correct": False,
            },
            {
                "text": "class HashTable<T> { private array: T[] = []; put(key: string, value: T) { this.array.push(value); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of a complete binary tree with n nodes when represented as an array?",
        "explanation": "Array representation of a complete binary tree requires exactly n spaces for n nodes.",
        "reference": "Binary Tree representations",
        "points": 1,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(2^n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement a TypeScript method for in-order traversal of a threaded binary tree:",
        "explanation": "Threaded binary tree uses null pointers to store inorder predecessors/successors for efficient traversal.",
        "reference": "Threaded Binary Tree",
        "points": 3,
        "answers": [
            {
                "text": "inorderTraversal(root: ThreadedNode): number[] { const result: number[] = []; let current = this.leftmost(root); while (current) { result.push(current.val); if (current.rightThreaded) current = current.right; else current = this.leftmost(current.right); } return result; }",
                "is_correct": True,
            },
            {
                "text": "inorderTraversal(root: ThreadedNode): number[] { if (!root) return []; return [...this.inorderTraversal(root.left), root.val, ...this.inorderTraversal(root.right)]; }",
                "is_correct": False,
            },
            {
                "text": "inorderTraversal(root: ThreadedNode): number[] { const stack = [root]; const result = []; while (stack.length) { const node = stack.pop()!; result.push(node.val); } return result; }",
                "is_correct": False,
            },
            {
                "text": "inorderTraversal(root: ThreadedNode): number[] { return [root.val]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Cartesian Tree construction?",
        "explanation": "Cartesian Tree maintains heap property based on priorities and BST property based on array indices.",
        "reference": "Cartesian Tree construction",
        "points": 3,
        "answers": [
            {
                "text": "buildCartesianTree(arr: number[]): TreeNode | null { if (!arr.length) return null; const maxIdx = arr.indexOf(Math.max(...arr)); const root = new TreeNode(arr[maxIdx]); root.left = this.buildCartesianTree(arr.slice(0, maxIdx)); root.right = this.buildCartesianTree(arr.slice(maxIdx + 1)); return root; }",
                "is_correct": True,
            },
            {
                "text": "buildCartesianTree(arr: number[]): TreeNode | null { const root = new TreeNode(arr[0]); for (let i = 1; i < arr.length; i++) { this.insert(root, arr[i]); } return root; }",
                "is_correct": False,
            },
            {
                "text": "buildCartesianTree(arr: number[]): TreeNode | null { return new TreeNode(arr.length > 0 ? arr[0] : 0); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the optimal TypeScript implementation for a persistent data structure using structural sharing?",
        "explanation": "Persistent data structures share unchanged parts between versions, requiring immutable operations.",
        "reference": "Persistent Data Structures",
        "points": 3,
        "answers": [
            {
                "text": "class PersistentList<T> { constructor(private head: Node<T> | null = null) {} add(value: T): PersistentList<T> { return new PersistentList(new Node(value, this.head)); } }",
                "is_correct": True,
            },
            {
                "text": "class PersistentList<T> { private items: T[] = []; add(value: T): PersistentList<T> { this.items.push(value); return this; } }",
                "is_correct": False,
            },
            {
                "text": "class PersistentList<T> { private items: T[] = []; add(value: T): PersistentList<T> { const newList = new PersistentList<T>(); newList.items = [...this.items, value]; return newList; } }",
                "is_correct": False,
            },
            {
                "text": "class PersistentList<T> { add(value: T): void { console.log('Added:', value); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement a TypeScript class for a Van Emde Boas Tree node:",
        "explanation": "vEB tree recursively subdivides universe size and maintains cluster and summary structures.",
        "reference": "Van Emde Boas Tree",
        "points": 3,
        "answers": [
            {
                "text": "class VEBNode { universeSize: number; min: number | null; max: number | null; summary: VEBNode | null; clusters: VEBNode[]; constructor(size: number) { this.universeSize = size; this.min = this.max = null; if (size > 2) { const clusterSize = Math.ceil(Math.sqrt(size)); this.summary = new VEBNode(clusterSize); this.clusters = Array(clusterSize).fill(null).map(() => new VEBNode(clusterSize)); } } }",
                "is_correct": True,
            },
            {
                "text": "class VEBNode { value: number; left: VEBNode; right: VEBNode; }",
                "is_correct": False,
            },
            {
                "text": "class VEBNode { data: number[]; size: number; }",
                "is_correct": False,
            },
            {
                "text": "class VEBNode { min: number; max: number; children: VEBNode[]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Splay Tree splay operation?",
        "explanation": "Splay operation moves accessed node to root through rotations (zig, zig-zig, zig-zag cases).",
        "reference": "Splay Tree operations",
        "points": 3,
        "answers": [
            {
                "text": "splay(node: SplayNode): SplayNode { while (node.parent) { if (!node.parent.parent) { if (node === node.parent.left) this.rightRotate(node.parent); else this.leftRotate(node.parent); } else if (node === node.parent.left && node.parent === node.parent.parent.left) { this.rightRotate(node.parent.parent); this.rightRotate(node.parent); } else if (node === node.parent.right && node.parent === node.parent.parent.right) { this.leftRotate(node.parent.parent); this.leftRotate(node.parent); } else { if (node === node.parent.left) this.rightRotate(node.parent); else this.leftRotate(node.parent); if (node === node.parent.right) this.leftRotate(node.parent); else this.rightRotate(node.parent); } } return node; }",
                "is_correct": True,
            },
            {
                "text": "splay(node: SplayNode): SplayNode { while (node.parent) { this.rightRotate(node.parent); } return node; }",
                "is_correct": False,
            },
            {
                "text": "splay(node: SplayNode): SplayNode { node.isRoot = True; return node; }",
                "is_correct": False,
            },
            {
                "text": "splay(node: SplayNode): SplayNode { return this.balance(node); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of range minimum query in a Sparse Table after O(n log n) preprocessing?",
        "explanation": "Sparse Table allows O(1) RMQ queries after preprocessing by precomputing minimum for all power-of-2 ranges.",
        "reference": "Sparse Table data structure",
        "points": 2,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(1)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Link-Cut Tree node:",
        "explanation": "Link-Cut Tree maintains dynamic trees with path queries, requiring auxiliary trees and path operations.",
        "reference": "Link-Cut Tree",
        "points": 3,
        "answers": [
            {
                "text": "class LCTNode { value: number; left: LCTNode | null; right: LCTNode | null; parent: LCTNode | null; pathParent: LCTNode | null; reversed: boolean; constructor(value: number) { this.value = value; this.left = this.right = this.parent = this.pathParent = null; this.reversed = False; } }",
                "is_correct": True,
            },
            {
                "text": "class LCTNode { value: number; children: LCTNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class LCTNode { data: number; next: LCTNode; prev: LCTNode; }",
                "is_correct": False,
            },
            {
                "text": "class LCTNode { value: number; parent: LCTNode; depth: number; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Treap (randomized BST) insertion?",
        "explanation": "Treap maintains BST property by key and heap property by random priority through rotations.",
        "reference": "Treap data structure",
        "points": 3,
        "answers": [
            {
                "text": "insert(root: TreapNode | null, key: number): TreapNode { if (!root) return new TreapNode(key, Math.random()); if (key < root.key) { root.left = this.insert(root.left, key); if (root.left && root.left.priority > root.priority) root = this.rightRotate(root); } else { root.right = this.insert(root.right, key); if (root.right && root.right.priority > root.priority) root = this.leftRotate(root); } return root; }",
                "is_correct": True,
            },
            {
                "text": "insert(root: TreapNode, key: number): TreapNode { root.children.push(new TreapNode(key, Math.random())); return root; }",
                "is_correct": False,
            },
            {
                "text": "insert(root: TreapNode, key: number): TreapNode { if (key < root.key) root.left = new TreapNode(key, 1); else root.right = new TreapNode(key, 1); return root; }",
                "is_correct": False,
            },
            {
                "text": "insert(root: TreapNode, key: number): void { root.values.add(key); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the expected height of a randomized BST (Treap) with n nodes?",
        "explanation": "Due to random priorities, Treap maintains expected O(log n) height like a balanced tree.",
        "reference": "Treap analysis",
        "points": 2,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(√n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Implement a TypeScript class for a Fibonacci Heap node:",
        "explanation": "Fibonacci Heap nodes maintain degree, parent, child, mark status and circular doubly-linked siblings.",
        "reference": "Fibonacci Heap",
        "points": 3,
        "answers": [
            {
                "text": "class FibHeapNode { key: number; degree: number; parent: FibHeapNode | null; child: FibHeapNode | null; left: FibHeapNode; right: FibHeapNode; mark: boolean; constructor(key: number) { this.key = key; this.degree = 0; this.parent = this.child = null; this.left = this.right = this; this.mark = False; } }",
                "is_correct": True,
            },
            {
                "text": "class FibHeapNode { value: number; children: FibHeapNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class FibHeapNode { data: number; next: FibHeapNode; priority: number; }",
                "is_correct": False,
            },
            {
                "text": "class FibHeapNode { key: number; left: FibHeapNode; right: FibHeapNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs range sum query in a 2D Segment Tree?",
        "explanation": "2D Segment Tree requires nested tree structure for efficient 2D range operations.",
        "reference": "2D Segment Tree",
        "points": 3,
        "answers": [
            {
                "text": "class SegTree2D { private tree: SegTree1D[]; query(x1: number, y1: number, x2: number, y2: number, vx = 1, lx = 0, rx = this.n): number { if (x1 > x2) return 0; if (lx === rx) return this.tree[vx].query(y1, y2); const m = Math.floor((lx + rx) / 2); return this.query(x1, y1, Math.min(x2, m), y2, 2*vx, lx, m) + this.query(Math.max(x1, m+1), y1, x2, y2, 2*vx+1, m+1, rx); } }",
                "is_correct": True,
            },
            {
                "text": "class SegTree2D { query(x1: number, y1: number, x2: number, y2: number): number { return this.matrix[x1][y1] + this.matrix[x2][y2]; } }",
                "is_correct": False,
            },
            {
                "text": "class SegTree2D { query(x1: number, y1: number, x2: number, y2: number): number { let sum = 0; for (let i = x1; i <= x2; i++) for (let j = y1; j <= y2; j++) sum += this.matrix[i][j]; return sum; } }",
                "is_correct": False,
            },
            {
                "text": "class SegTree2D { query(): number { return 0; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the amortized time complexity of union operation in Union-Find with path compression and union by rank?",
        "explanation": "With both optimizations, union operations achieve nearly constant amortized time O(α(n)) where α is inverse Ackermann.",
        "reference": "Union-Find analysis",
        "points": 2,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(α(n))", "is_correct": True},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Rope data structure node:",
        "explanation": "Rope efficiently handles string operations by representing strings as binary trees of smaller strings.",
        "reference": "Rope data structure",
        "points": 3,
        "answers": [
            {
                "text": "class RopeNode { str: string; weight: number; left: RopeNode | null; right: RopeNode | null; constructor(str: string = '') { this.str = str; this.weight = str.length; this.left = this.right = null; } }",
                "is_correct": True,
            },
            {
                "text": "class RopeNode { data: string; next: RopeNode; length: number; }",
                "is_correct": False,
            },
            {
                "text": "class RopeNode { chars: string[]; children: RopeNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class RopeNode { value: string; parent: RopeNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles Heavy-Light Decomposition preprocessing?",
        "explanation": "HLD decomposes tree into heavy and light edges, creating paths for efficient tree queries.",
        "reference": "Heavy-Light Decomposition",
        "points": 3,
        "answers": [
            {
                "text": "class HLD { private parent: number[]; private depth: number[]; private heavy: number[]; private head: number[]; private pos: number[]; dfs1(v: number, p: number, d: number) { this.parent[v] = p; this.depth[v] = d; let maxChild = -1, maxSize = 0; for (const u of this.adj[v]) { if (u !== p) { this.dfs1(u, v, d + 1); if (this.subtreeSize[u] > maxSize) { maxSize = this.subtreeSize[u]; maxChild = u; } } } this.heavy[v] = maxChild; } }",
                "is_correct": True,
            },
            {
                "text": "class HLD { decompose(root: number) { this.paths.push([root]); } }",
                "is_correct": False,
            },
            {
                "text": "class HLD { private tree: number[][]; process() { return this.tree.flat(); } }",
                "is_correct": False,
            },
            {
                "text": "class HLD { preprocess(n: number) { for (let i = 0; i < n; i++) this.parent[i] = i; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of a suffix tree for a string of length n?",
        "explanation": "Suffix tree can have O(n) nodes and edges in the worst case with careful implementation.",
        "reference": "Suffix Tree analysis",
        "points": 2,
        "answers": [
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Implement a TypeScript class for a Palindromic Tree (Eertree) node:",
        "explanation": "Palindromic Tree maintains all palindromic substrings with failure links and suffix links.",
        "reference": "Palindromic Tree",
        "points": 3,
        "answers": [
            {
                "text": "class EertreeNode { len: number; link: EertreeNode | null; go: Map<string, EertreeNode>; constructor(len: number) { this.len = len; this.link = null; this.go = new Map(); } }",
                "is_correct": True,
            },
            {
                "text": "class EertreeNode { palindrome: string; children: EertreeNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class EertreeNode { data: string; next: EertreeNode; prev: EertreeNode; }",
                "is_correct": False,
            },
            {
                "text": "class EertreeNode { value: string; parent: EertreeNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Wavelet Tree for rank queries?",
        "explanation": "Wavelet Tree recursively partitions alphabet and maintains bit vectors for efficient rank/select queries.",
        "reference": "Wavelet Tree",
        "points": 3,
        "answers": [
            {
                "text": "class WaveletTree { private left: WaveletTree | null; private right: WaveletTree | null; private bits: boolean[]; private prefixSum: number[]; rank(c: number, pos: number): number { if (this.left === null) return pos + 1; const bit = (c >> this.level) & 1; if (bit === 0) return this.left.rank(c, this.prefixSum[pos] - 1); else return this.right.rank(c, pos - this.prefixSum[pos] - 1); } }",
                "is_correct": True,
            },
            {
                "text": "class WaveletTree { private array: number[]; rank(c: number, pos: number): number { return this.array.slice(0, pos + 1).filter(x => x === c).length; } }",
                "is_correct": False,
            },
            {
                "text": "class WaveletTree { private map: Map<number, number[]>; rank(c: number, pos: number): number { return this.map.get(c)?.length || 0; } }",
                "is_correct": False,
            },
            {
                "text": "class WaveletTree { rank(c: number, pos: number): number { return c + pos; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of finding LCA using binary lifting preprocessing?",
        "explanation": "Binary lifting preprocesses O(n log n) ancestors, allowing O(log n) LCA queries.",
        "reference": "LCA Binary Lifting",
        "points": 2,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Centroid Decomposition:",
        "explanation": "Centroid decomposition recursively decomposes tree using centroids for efficient tree algorithms.",
        "reference": "Centroid Decomposition",
        "points": 3,
        "answers": [
            {
                "text": "class CentroidDecomp { private removed: boolean[]; private subtreeSize: number[]; findCentroid(v: number, p: number, treeSize: number): number { for (const u of this.adj[v]) { if (u !== p && !this.removed[u] && this.subtreeSize[u] > treeSize / 2) return this.findCentroid(u, v, treeSize); } return v; } decompose(v: number): void { const size = this.calcSize(v, -1); const centroid = this.findCentroid(v, -1, size); this.removed[centroid] = True; for (const u of this.adj[centroid]) { if (!this.removed[u]) this.decompose(u); } } }",
                "is_correct": True,
            },
            {
                "text": "class CentroidDecomp { decompose(root: number): number[] { return [root]; } }",
                "is_correct": False,
            },
            {
                "text": "class CentroidDecomp { private tree: number[][]; process(): void { this.tree.forEach(row => row.sort()); } }",
                "is_correct": False,
            },
            {
                "text": "class CentroidDecomp { decompose(): void { console.log('Decomposed'); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a K-D Tree range search?",
        "explanation": "K-D Tree range search recursively checks if current node and subtrees intersect with query range.",
        "reference": "K-D Tree operations",
        "points": 3,
        "answers": [
            {
                "text": "rangeSearch(node: KDNode | null, range: Range, depth = 0): Point[] { if (!node) return []; const result: Point[] = []; const axis = depth % this.k; if (this.inRange(node.point, range)) result.push(node.point); if (range.min[axis] <= node.point[axis]) result.push(...this.rangeSearch(node.left, range, depth + 1)); if (range.max[axis] >= node.point[axis]) result.push(...this.rangeSearch(node.right, range, depth + 1)); return result; }",
                "is_correct": True,
            },
            {
                "text": "rangeSearch(node: KDNode, range: Range): Point[] { return node.children.filter(child => this.inRange(child.point, range)).map(child => child.point); }",
                "is_correct": False,
            },
            {
                "text": "rangeSearch(node: KDNode, range: Range): Point[] { return [node.point]; }",
                "is_correct": False,
            },
            {
                "text": "rangeSearch(node: KDNode, range: Range): Point[] { return this.allPoints.filter(p => this.inRange(p, range)); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the expected time complexity of insertion in a Randomized Binary Search Tree?",
        "explanation": "Randomized BST maintains expected O(log n) height through random choices during insertion.",
        "reference": "Randomized BST",
        "points": 2,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(1)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a persistent segment tree update:",
        "explanation": "Persistent segment tree creates new nodes only for changed path, sharing unchanged subtrees.",
        "reference": "Persistent Segment Tree",
        "points": 3,
        "answers": [
            {
                "text": "update(node: SegNode | null, tl: number, tr: number, pos: number, val: number): SegNode { const newNode = new SegNode(node?.sum || 0); if (tl === tr) { newNode.sum = val; } else { const tm = Math.floor((tl + tr) / 2); newNode.left = pos <= tm ? this.update(node?.left || null, tl, tm, pos, val) : node?.left || null; newNode.right = pos > tm ? this.update(node?.right || null, tm + 1, tr, pos, val) : node?.right || null; newNode.sum = (newNode.left?.sum || 0) + (newNode.right?.sum || 0); } return newNode; }",
                "is_correct": True,
            },
            {
                "text": "update(node: SegNode, pos: number, val: number): SegNode { node.sum = val; return node; }",
                "is_correct": False,
            },
            {
                "text": "update(node: SegNode, pos: number, val: number): SegNode { const newNode = JSON.parse(JSON.stringify(node)); newNode.sum = val; return newNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Scapegoat Tree rebalancing?",
        "explanation": "Scapegoat Tree maintains balance by rebuilding subtrees when they become too unbalanced.",
        "reference": "Scapegoat Tree",
        "points": 3,
        "answers": [
            {
                "text": "rebalance(node: ScapegoatNode): ScapegoatNode { const nodes: ScapegoatNode[] = []; this.inorderTraversal(node, nodes); return this.buildBalanced(nodes, 0, nodes.length - 1); } buildBalanced(nodes: ScapegoatNode[], start: number, end: number): ScapegoatNode | null { if (start > end) return null; const mid = Math.floor((start + end) / 2); const root = nodes[mid]; root.left = this.buildBalanced(nodes, start, mid - 1); root.right = this.buildBalanced(nodes, mid + 1, end); return root; }",
                "is_correct": True,
            },
            {
                "text": "rebalance(node: ScapegoatNode): ScapegoatNode { node.balance = 0; return node; }",
                "is_correct": False,
            },
            {
                "text": "rebalance(node: ScapegoatNode): ScapegoatNode { return this.rotateLeft(node); }",
                "is_correct": False,
            },
            {
                "text": "rebalance(node: ScapegoatNode): void { node.children.sort((a, b) => a.value - b.value); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of Mo's algorithm for offline range queries?",
        "explanation": "Mo's algorithm achieves O((N + Q) * √N) complexity by sorting queries and using sliding window technique.",
        "reference": "Mo's Algorithm",
        "points": 2,
        "answers": [
            {"text": "O(N log N)", "is_correct": False},
            {"text": "O((N + Q) * √N)", "is_correct": True},
            {"text": "O(N²)", "is_correct": False},
            {"text": "O(Q log Q)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Count-Min Sketch data structure:",
        "explanation": "Count-Min Sketch uses multiple hash functions and counters for approximate frequency counting.",
        "reference": "Count-Min Sketch",
        "points": 3,
        "answers": [
            {
                "text": "class CountMinSketch { private table: number[][]; private hashFunctions: ((x: string) => number)[]; increment(item: string): void { this.hashFunctions.forEach((hash, i) => { const j = hash(item) % this.table[i].length; this.table[i][j]++; }); } estimate(item: string): number { return Math.min(...this.hashFunctions.map((hash, i) => { const j = hash(item) % this.table[i].length; return this.table[i][j]; })); } }",
                "is_correct": True,
            },
            {
                "text": "class CountMinSketch { private map: Map<string, number>; increment(item: string): void { this.map.set(item, (this.map.get(item) || 0) + 1); } }",
                "is_correct": False,
            },
            {
                "text": "class CountMinSketch { private counter: number = 0; increment(): void { this.counter++; } }",
                "is_correct": False,
            },
            {
                "text": "class CountMinSketch { private array: number[]; increment(index: number): void { this.array[index]++; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Suffix Automaton construction?",
        "explanation": "Suffix Automaton incrementally builds states and transitions for all suffixes of the string.",
        "reference": "Suffix Automaton",
        "points": 3,
        "answers": [
            {
                "text": "class SuffixAutomaton { private states: SAState[] = []; private last: number = 0; extend(c: string): void { const cur = this.states.length; this.states.push(new SAState()); this.states[cur].len = this.states[this.last].len + 1; let p = this.last; while (p !== -1 && !this.states[p].go.has(c)) { this.states[p].go.set(c, cur); p = this.states[p].link; } if (p === -1) { this.states[cur].link = 0; } else { const q = this.states[p].go.get(c)!; if (this.states[p].len + 1 === this.states[q].len) { this.states[cur].link = q; } else { const clone = this.states.length; this.states.push(new SAState()); this.states[clone] = Object.assign({}, this.states[q]); this.states[clone].len = this.states[p].len + 1; while (p !== -1 && this.states[p].go.get(c) === q) { this.states[p].go.set(c, clone); p = this.states[p].link; } this.states[q].link = this.states[cur].link = clone; } } this.last = cur; } }",
                "is_correct": True,
            },
            {
                "text": "class SuffixAutomaton { private suffixes: string[] = []; extend(c: string): void { this.suffixes.push(c); } }",
                "is_correct": False,
            },
            {
                "text": "class SuffixAutomaton { private trie: TrieNode; extend(c: string): void { this.trie.children[c] = new TrieNode(); } }",
                "is_correct": False,
            },
            {
                "text": "class SuffixAutomaton { extend(c: string): void { console.log('Extended with:', c); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of a Fenwick Tree for an array of size n?",
        "explanation": "Fenwick Tree (Binary Indexed Tree) requires exactly n+1 space for efficient prefix operations.",
        "reference": "Fenwick Tree analysis",
        "points": 1,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(n²)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Top Tree node:",
        "explanation": "Top Tree maintains tree decomposition with clusters and provides efficient tree operations.",
        "reference": "Top Tree data structure",
        "points": 3,
        "answers": [
            {
                "text": "class TopTreeNode { type: 'compress' | 'rake'; left: TopTreeNode | null; right: TopTreeNode | null; boundary: Set<number>; pathInfo: any; constructor(type: 'compress' | 'rake') { this.type = type; this.left = this.right = null; this.boundary = new Set(); this.pathInfo = null; } }",
                "is_correct": True,
            },
            {
                "text": "class TopTreeNode { value: number; parent: TopTreeNode; children: TopTreeNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class TopTreeNode { data: number; next: TopTreeNode; prev: TopTreeNode; }",
                "is_correct": False,
            },
            {
                "text": "class TopTreeNode { cluster: number[]; level: number; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Dynamic Connectivity query?",
        "explanation": "Dynamic Connectivity maintains connectivity information as edges are added/removed over time.",
        "reference": "Dynamic Connectivity",
        "points": 3,
        "answers": [
            {
                "text": "class DynamicConnectivity { private uf: UnionFind[]; private maxLevel: number; addEdge(u: number, v: number, time: number): void { for (let level = 0; level <= this.maxLevel; level++) { if (this.shouldAddAtLevel(time, level)) { this.uf[level].union(u, v); } } } connected(u: number, v: number, time: number): boolean { const level = this.getQueryLevel(time); return this.uf[level].find(u) === this.uf[level].find(v); } }",
                "is_correct": True,
            },
            {
                "text": "class DynamicConnectivity { private graph: Map<number, Set<number>>; connected(u: number, v: number): boolean { return this.graph.get(u)?.has(v) || False; } }",
                "is_correct": False,
            },
            {
                "text": "class DynamicConnectivity { private edges: [number, number][] = []; connected(u: number, v: number): boolean { return this.edges.some(([a, b]) => (a === u && b === v) || (a === v && b === u)); } }",
                "is_correct": False,
            },
            {
                "text": "class DynamicConnectivity { connected(): boolean { return True; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of range update in a Lazy Propagation Segment Tree?",
        "explanation": "Lazy propagation allows O(log n) range updates by deferring updates until needed.",
        "reference": "Lazy Propagation",
        "points": 2,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(1)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Y-fast Trie node:",
        "explanation": "Y-fast Trie combines X-fast Trie with balanced BSTs for efficient predecessor/successor queries.",
        "reference": "Y-fast Trie",
        "points": 3,
        "answers": [
            {
                "text": "class YFastTrieNode { isLeaf: boolean; left: YFastTrieNode | null; right: YFastTrieNode | null; bst: BalancedBST | null; representative: number | null; constructor(isLeaf: boolean = False) { this.isLeaf = isLeaf; this.left = this.right = null; this.bst = isLeaf ? new BalancedBST() : null; this.representative = null; } }",
                "is_correct": True,
            },
            {
                "text": "class YFastTrieNode { value: number; children: YFastTrieNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class YFastTrieNode { bit: boolean; next: YFastTrieNode; }",
                "is_correct": False,
            },
            {
                "text": "class YFastTrieNode { data: number; parent: YFastTrieNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Fractional Cascading preprocessing?",
        "explanation": "Fractional Cascading speeds up multiple binary searches by maintaining bridge pointers between sorted lists.",
        "reference": "Fractional Cascading",
        "points": 3,
        "answers": [
            {
                "text": "class FractionalCascading { private lists: (number | Bridge)[][][]; private bridges: Map<number, [number, number]>; preprocess(): void { for (let i = this.lists.length - 2; i >= 0; i--) { const current = this.lists[i]; const next = this.lists[i + 1]; let j = 0, k = 0; while (j < current.length && k < next.length) { if (current[j] <= next[k]) { this.bridges.set(this.getId(i, j), [i + 1, k]); j++; } else { k++; } } } } }",
                "is_correct": True,
            },
            {
                "text": "class FractionalCascading { preprocess(): void { this.lists.forEach(list => list.sort()); } }",
                "is_correct": False,
            },
            {
                "text": "class FractionalCascading { preprocess(): void { console.log('Preprocessed'); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement TypeScript code for a Succinct Data Structure bit vector:",
        "explanation": "Succinct bit vector provides rank/select operations in o(n) extra space beyond the n bits.",
        "reference": "Succinct Data Structures",
        "points": 3,
        "answers": [
            {
                "text": "class SuccinctBitVector { private bits: boolean[]; private rankTable: number[]; private selectTable: number[]; rank(pos: number): number { if (pos < 0) return 0; let count = this.rankTable[Math.floor(pos / this.blockSize)]; for (let i = Math.floor(pos / this.blockSize) * this.blockSize; i <= pos; i++) { if (this.bits[i]) count++; } return count; } select(k: number): number { const block = this.selectTable[Math.floor(k / this.selectBlockSize)]; for (let i = block, count = 0; i < this.bits.length; i++) { if (this.bits[i] && ++count === k) return i; } return -1; } }",
                "is_correct": True,
            },
            {
                "text": "class SuccinctBitVector { private bits: boolean[]; rank(pos: number): number { return this.bits.slice(0, pos + 1).filter(b => b).length; } }",
                "is_correct": False,
            },
            {
                "text": "class SuccinctBitVector { private array: number[]; rank(pos: number): number { return this.array[pos]; } }",
                "is_correct": False,
            },
            {
                "text": "class SuccinctBitVector { rank(): number { return 0; } select(): number { return -1; } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of LCA query using Euler Tour + Sparse Table?",
        "explanation": "Euler tour converts LCA to RMQ, which is answered in O(1) time with sparse table preprocessing.",
        "reference": "LCA using RMQ",
        "points": 2,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(1)", "is_correct": True},
            {"text": "O(√n)", "is_correct": False},
            {"text": "O(n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Leftist Heap merge operation:",
        "explanation": "Leftist heap merge maintains the leftist property where null path length of left child ≥ right child.",
        "reference": "Leftist Heap",
        "points": 3,
        "answers": [
            {
                "text": "merge(h1: LeftistNode | null, h2: LeftistNode | null): LeftistNode | null { if (!h1) return h2; if (!h2) return h1; if (h1.key > h2.key) [h1, h2] = [h2, h1]; h1.right = this.merge(h1.right, h2); if (!h1.left || (h1.right && h1.left.npl < h1.right.npl)) { [h1.left, h1.right] = [h1.right, h1.left]; } h1.npl = (h1.right?.npl || 0) + 1; return h1; }",
                "is_correct": True,
            },
            {
                "text": "merge(h1: LeftistNode, h2: LeftistNode): LeftistNode { h1.children.push(...h2.children); return h1; }",
                "is_correct": False,
            },
            {
                "text": "merge(h1: LeftistNode, h2: LeftistNode): LeftistNode { return h1.key < h2.key ? h1 : h2; }",
                "is_correct": False,
            },
            {
                "text": "merge(h1: LeftistNode, h2: LeftistNode): LeftistNode { const result = new LeftistNode(Math.min(h1.key, h2.key)); return result; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Pairing Heap decrease key operation?",
        "explanation": "Pairing heap decrease key cuts the node from its parent and merges it with the root.",
        "reference": "Pairing Heap operations",
        "points": 3,
        "answers": [
            {
                "text": "decreaseKey(node: PairingNode, newKey: number): void { if (newKey >= node.key) return; node.key = newKey; if (node.parent) { this.cut(node); this.root = this.merge(this.root, node); } } cut(node: PairingNode): void { if (node.parent) { if (node.parent.child === node) { node.parent.child = node.next; } if (node.prev) node.prev.next = node.next; if (node.next) node.next.prev = node.prev; node.parent = node.prev = node.next = null; } }",
                "is_correct": True,
            },
            {
                "text": "decreaseKey(node: PairingNode, newKey: number): void { node.key = newKey; this.heapifyUp(node); }",
                "is_correct": False,
            },
            {
                "text": "decreaseKey(node: PairingNode, newKey: number): void { node.key = newKey; }",
                "is_correct": False,
            },
            {
                "text": "decreaseKey(node: PairingNode, newKey: number): void { if (newKey < node.key) { node.key = newKey; this.bubbleUp(node); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of a Cartesian Tree for an array of n elements?",
        "explanation": "Cartesian Tree stores exactly n nodes for n array elements, requiring O(n) space.",
        "reference": "Cartesian Tree analysis",
        "points": 1,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(n²)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Merkle Tree node:",
        "explanation": "Merkle Tree nodes store hash values, with leaves containing data hashes and internal nodes containing combined hashes.",
        "reference": "Merkle Tree",
        "points": 2,
        "answers": [
            {
                "text": "class MerkleNode { hash: string; left: MerkleNode | null; right: MerkleNode | null; data: any; constructor(data?: any, left?: MerkleNode, right?: MerkleNode) { this.data = data; this.left = left || null; this.right = right || null; this.hash = this.calculateHash(); } private calculateHash(): string { if (this.data) return this.sha256(JSON.stringify(this.data)); return this.sha256((this.left?.hash || '') + (this.right?.hash || '')); } }",
                "is_correct": True,
            },
            {
                "text": "class MerkleNode { value: string; children: MerkleNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class MerkleNode { data: any; next: MerkleNode; }",
                "is_correct": False,
            },
            {
                "text": "class MerkleNode { hash: number; parent: MerkleNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a B+ Tree leaf node?",
        "explanation": "B+ Tree leaf nodes store actual data and maintain pointers to next leaf for range queries.",
        "reference": "B+ Tree structure",
        "points": 2,
        "answers": [
            {
                "text": "class BPlusLeafNode { keys: number[]; values: any[]; next: BPlusLeafNode | null; parent: BPlusInternalNode | null; constructor(order: number) { this.keys = []; this.values = []; this.next = null; this.parent = null; } isLeaf(): boolean { return True; } }",
                "is_correct": True,
            },
            {
                "text": "class BPlusLeafNode { data: Map<number, any>; children: BPlusLeafNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class BPlusLeafNode { value: any; left: BPlusLeafNode; right: BPlusLeafNode; }",
                "is_correct": False,
            },
            {
                "text": "class BPlusLeafNode { entries: [number, any][]; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of insertion in a Ternary Search Tree?",
        "explanation": "TST insertion follows path based on character comparisons, taking O(log n) average time for balanced tree.",
        "reference": "Ternary Search Tree",
        "points": 2,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Cuckoo Hashing table:",
        "explanation": "Cuckoo Hashing uses two hash functions and handles collisions by displacing existing elements.",
        "reference": "Cuckoo Hashing",
        "points": 3,
        "answers": [
            {
                "text": "class CuckooHashTable<T> { private table1: (T | null)[]; private table2: (T | null)[]; private hash1: (key: T) => number; private hash2: (key: T) => number; insert(key: T): boolean { if (this.contains(key)) return True; let current = key; for (let i = 0; i < this.maxCycles; i++) { const pos1 = this.hash1(current) % this.table1.length; if (!this.table1[pos1]) { this.table1[pos1] = current; return True; } [current, this.table1[pos1]] = [this.table1[pos1]!, current]; const pos2 = this.hash2(current) % this.table2.length; if (!this.table2[pos2]) { this.table2[pos2] = current; return True; } [current, this.table2[pos2]] = [this.table2[pos2]!, current]; } return this.rehash(); } }",
                "is_correct": True,
            },
            {
                "text": "class CuckooHashTable<T> { private table: T[] = []; insert(key: T): void { this.table.push(key); } }",
                "is_correct": False,
            },
            {
                "text": "class CuckooHashTable<T> { private map: Map<T, boolean> = new Map(); insert(key: T): void { this.map.set(key, True); } }",
                "is_correct": False,
            },
            {
                "text": "class CuckooHashTable<T> { insert(key: T): void { console.log('Inserted:', key); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Range Tree 2D query?",
        "explanation": "Range Tree performs 2D range queries by first filtering on x-coordinate, then querying y-coordinates in associated structures.",
        "reference": "Range Tree",
        "points": 3,
        "answers": [
            {
                "text": "query2D(xmin: number, xmax: number, ymin: number, ymax: number, node: RangeTreeNode = this.root, xl = -Infinity, xr = Infinity): Point[] { if (!node || xmax < xl || xmin > xr) return []; if (xmin <= xl && xr <= xmax) { return node.yTree.rangeQuery(ymin, ymax); } const xm = (xl + xr) / 2; const leftResult = this.query2D(xmin, xmax, ymin, ymax, node.left, xl, xm); const rightResult = this.query2D(xmin, xmax, ymin, ymax, node.right, xm, xr); return [...leftResult, ...rightResult]; }",
                "is_correct": True,
            },
            {
                "text": "query2D(xmin: number, xmax: number, ymin: number, ymax: number): Point[] { return this.allPoints.filter(p => p.x >= xmin && p.x <= xmax && p.y >= ymin && p.y <= ymax); }",
                "is_correct": False,
            },
            {
                "text": "query2D(xmin: number, xmax: number, ymin: number, ymax: number): Point[] { return []; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Implement TypeScript code for a Radix Tree (Patricia Trie) node:",
        "explanation": "Radix Tree compresses paths by storing strings in nodes instead of single characters.",
        "reference": "Radix Tree",
        "points": 2,
        "answers": [
            {
                "text": "class RadixNode { key: string; children: Map<string, RadixNode>; isEndOfWord: boolean; value?: any; constructor(key: string = '') { this.key = key; this.children = new Map(); this.isEndOfWord = False; } }",
                "is_correct": True,
            },
            {
                "text": "class RadixNode { char: string; children: RadixNode[]; isLeaf: boolean; }",
                "is_correct": False,
            },
            {
                "text": "class RadixNode { data: string; next: RadixNode; prev: RadixNode; }",
                "is_correct": False,
            },
            {
                "text": "class RadixNode { value: string; parent: RadixNode; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the worst-case time complexity of searching in a Quadtree?",
        "explanation": "Quadtree search in worst case (unbalanced) can degrade to O(n) when all points cluster in one region.",
        "reference": "Quadtree analysis",
        "points": 2,
        "answers": [
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(√n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Dancing Links (DLX) node:",
        "explanation": "Dancing Links uses doubly-linked lists in both directions with cover/uncover operations for exact cover problems.",
        "reference": "Dancing Links",
        "points": 3,
        "answers": [
            {
                "text": "class DLXNode { left: DLXNode; right: DLXNode; up: DLXNode; down: DLXNode; column: DLXNode; rowId: number; constructor() { this.left = this.right = this.up = this.down = this; this.column = this; this.rowId = -1; } cover(): void { this.right.left = this.left; this.left.right = this.right; for (let row = this.down; row !== this; row = row.down) { for (let node = row.right; node !== row; node = node.right) { node.down.up = node.up; node.up.down = node.down; (node.column as any).size--; } } } }",
                "is_correct": True,
            },
            {
                "text": "class DLXNode { value: number; links: DLXNode[]; }",
                "is_correct": False,
            },
            {
                "text": "class DLXNode { data: any; next: DLXNode; }",
                "is_correct": False,
            },
            {
                "text": "class DLXNode { id: number; connected: Set<DLXNode>; }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Randomized Skip List search?",
        "explanation": "Skip List search starts from highest level and moves right/down based on key comparisons.",
        "reference": "Skip List search",
        "points": 2,
        "answers": [
            {
                "text": "search(key: number): SkipListNode | null { let current = this.head; for (let level = this.maxLevel; level >= 0; level--) { while (current.forward[level] && current.forward[level]!.value < key) { current = current.forward[level]!; } } current = current.forward[0]; return current && current.value === key ? current : null; }",
                "is_correct": True,
            },
            {
                "text": "search(key: number): SkipListNode | null { let current = this.head; while (current && current.value !== key) { current = current.next; } return current; }",
                "is_correct": False,
            },
            {
                "text": "search(key: number): SkipListNode | null { return this.nodes.find(node => node.value === key) || null; }",
                "is_correct": False,
            },
            {
                "text": "search(key: number): SkipListNode | null { return new SkipListNode(key, 0); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the expected time complexity of insertion in a Randomized Treap?",
        "explanation": "Randomized Treap maintains expected O(log n) height due to random priorities, making insertion O(log n) expected.",
        "reference": "Treap complexity analysis",
        "points": 2,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(1)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Binomial Heap merge operation:",
        "explanation": "Binomial Heap merge combines two heaps by merging binomial trees of the same order.",
        "reference": "Binomial Heap",
        "points": 3,
        "answers": [
            {
                "text": "merge(h1: BinomialHeap, h2: BinomialHeap): BinomialHeap { const result = new BinomialHeap(); let p1 = h1.head, p2 = h2.head; let carry: BinomialNode | null = null; while (p1 || p2 || carry) { let min1 = p1?.degree ?? Infinity; let min2 = p2?.degree ?? Infinity; let minCarry = carry?.degree ?? Infinity; let minDegree = Math.min(min1, min2, minCarry); let trees: BinomialNode[] = []; if (p1?.degree === minDegree) { trees.push(p1); p1 = p1.sibling; } if (p2?.degree === minDegree) { trees.push(p2); p2 = p2.sibling; } if (carry?.degree === minDegree) { trees.push(carry); carry = null; } if (trees.length === 1) { result.addTree(trees[0]); } else if (trees.length === 2) { carry = this.linkTrees(trees[0], trees[1]); } else { result.addTree(trees[0]); carry = this.linkTrees(trees[1], trees[2]); } } return result; }",
                "is_correct": True,
            },
            {
                "text": "merge(h1: BinomialHeap, h2: BinomialHeap): BinomialHeap { const result = new BinomialHeap(); result.trees = [...h1.trees, ...h2.trees]; return result; }",
                "is_correct": False,
            },
            {
                "text": "merge(h1: BinomialHeap, h2: BinomialHeap): BinomialHeap { return h1.size > h2.size ? h1 : h2; }",
                "is_correct": False,
            },
            {
                "text": "merge(h1: BinomialHeap, h2: BinomialHeap): BinomialHeap { return new BinomialHeap(); }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript code correctly implements a Suffix Tree construction using Ukkonen's algorithm?",
        "explanation": "Ukkonen's algorithm builds suffix tree online in linear time using active point and suffix links.",
        "reference": "Ukkonen's Algorithm",
        "points": 3,
        "answers": [
            {
                "text": "class UkkonenSuffixTree { private activeNode: SuffixNode; private activeEdge: number; private activeLength: number; private remainingSuffixCount: number; buildSuffixTree(text: string): void { for (let i = 0; i < text.length; i++) { this.extendSuffixTree(text, i); } } private extendSuffixTree(text: string, pos: number): void { this.remainingSuffixCount++; let lastNewNode: SuffixNode | null = null; while (this.remainingSuffixCount > 0) { if (this.activeLength === 0) { this.activeEdge = pos; } if (!this.activeNode.children.has(text[this.activeEdge])) { this.activeNode.children.set(text[this.activeEdge], new SuffixNode(pos)); if (lastNewNode) { lastNewNode.suffixLink = this.activeNode; lastNewNode = null; } } else { const next = this.activeNode.children.get(text[this.activeEdge])!; if (this.walkDown(next, text, pos)) continue; if (text[next.start + this.activeLength] === text[pos]) { if (lastNewNode && this.activeNode !== this.root) { lastNewNode.suffixLink = this.activeNode; } this.activeLength++; break; } const splitEnd = next.start + this.activeLength - 1; const split = new SuffixNode(next.start, splitEnd); this.activeNode.children.set(text[this.activeEdge], split); split.children.set(text[pos], new SuffixNode(pos)); next.start += this.activeLength; split.children.set(text[next.start], next); if (lastNewNode) { lastNewNode.suffixLink = split; } lastNewNode = split; } this.remainingSuffixCount--; if (this.activeNode === this.root && this.activeLength > 0) { this.activeLength--; this.activeEdge = pos - this.remainingSuffixCount + 1; } else if (this.activeNode !== this.root) { this.activeNode = this.activeNode.suffixLink || this.root; } } } }",
                "is_correct": True,
            },
            {
                "text": "class UkkonenSuffixTree { buildSuffixTree(text: string): void { for (let i = 0; i < text.length; i++) { this.addSuffix(text.substring(i)); } } }",
                "is_correct": False,
            },
            {
                "text": "class UkkonenSuffixTree { buildSuffixTree(text: string): void { this.suffixes = this.getAllSuffixes(text); this.root = this.buildTrie(this.suffixes); } }",
                "is_correct": False,
            },
            {
                "text": "class UkkonenSuffixTree { buildSuffixTree(text: string): void { console.log('Building suffix tree for:', text); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of a perfect k-ary heap with n elements?",
        "explanation": "Perfect k-ary heap with n elements requires exactly n space when stored in an array.",
        "reference": "k-ary Heap",
        "points": 1,
        "answers": [
            {"text": "O(k)", "is_correct": False},
            {"text": "O(n)", "is_correct": True},
            {"text": "O(n log k)", "is_correct": False},
            {"text": "O(kn)", "is_correct": False},
        ],
    },
    {
        "text": "Implement TypeScript code for a Persistent Stack using path copying:",
        "explanation": "Persistent Stack creates new versions without modifying previous versions, sharing unchanged parts.",
        "reference": "Persistent Data Structures",
        "points": 2,
        "answers": [
            {
                "text": "class PersistentStack<T> { constructor(private head: StackNode<T> | null = null, private _size: number = 0) {} push(value: T): PersistentStack<T> { return new PersistentStack(new StackNode(value, this.head), this._size + 1); } pop(): { value: T | undefined; stack: PersistentStack<T> } { if (!this.head) return { value: undefined, stack: this }; return { value: this.head.value, stack: new PersistentStack(this.head.next, this._size - 1) }; } peek(): T | undefined { return this.head?.value; } size(): number { return this._size; } }",
                "is_correct": True,
            },
            {
                "text": "class PersistentStack<T> { private items: T[] = []; push(value: T): PersistentStack<T> { this.items.push(value); return this; } }",
                "is_correct": False,
            },
            {
                "text": "class PersistentStack<T> { private stack: T[] = []; push(value: T): PersistentStack<T> { const newStack = new PersistentStack<T>(); newStack.stack = [...this.stack, value]; return newStack; } }",
                "is_correct": False,
            },
            {
                "text": "class PersistentStack<T> { push(value: T): void { console.log('Pushed:', value); } }",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "Which TypeScript implementation correctly handles a Finger Tree split operation?",
        "explanation": "Finger Tree split divides the tree at a given position while maintaining the finger tree structure and annotations.",
        "reference": "Finger Tree",
        "points": 3,
        "answers": [
            {
                "text": "split<A>(predicate: (v: V) => boolean, tree: FingerTree<V, A>): { left: FingerTree<V, A>; middle: A; right: FingerTree<V, A> } { if (tree instanceof Empty) throw new Error('Cannot split empty tree'); if (tree instanceof Single) return { left: new Empty(), middle: tree.value, right: new Empty() }; const vl = tree.left.measure(); if (predicate(vl)) { const { left, middle, right } = this.splitDigit(predicate, tree.left, this.monoid.empty()); return { left: this.digitToTree(left), middle, right: this.deepLeft(right, tree.middle, tree.right) }; } const vm = this.monoid.combine(vl, tree.middle.measure()); if (predicate(vm)) { const { left: ml, middle: xs, right: mr } = this.splitTree(predicate, vl, tree.middle); const { left, middle, right } = this.splitNode(predicate, this.monoid.combine(vl, ml.measure()), xs); return { left: this.deepRight(tree.left, ml, left), middle, right: this.deepLeft(right, mr, tree.right) }; } const { left, middle, right } = this.splitDigit(predicate, tree.right, vm); return { left: this.deepRight(tree.left, tree.middle, left), middle, right: this.digitToTree(right) }; }",
                "is_correct": True,
            },
            {
                "text": "split<A>(position: number, tree: FingerTree<V, A>): { left: A[]; right: A[] } { const array = this.toArray(tree); return { left: array.slice(0, position), right: array.slice(position) }; }",
                "is_correct": False,
            },
            {
                "text": "split<A>(tree: FingerTree<V, A>): { left: FingerTree<V, A>; right: FingerTree<V, A> } { return { left: tree, right: new Empty() }; }",
                "is_correct": False,
            },
            {
                "text": "split<A>(): void { console.log('Split operation'); }",
                "is_correct": False,
            },
        ],
    },
]
