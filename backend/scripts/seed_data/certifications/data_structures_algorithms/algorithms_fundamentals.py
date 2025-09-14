"""Algorithms Fundamentals Certification"""

CERTIFICATION = {
    "name": "Algorithms Fundamentals",
    "description": "Core algorithms including sorting, searching, recursion, and basic algorithmic techniques",
    "slug": "algorithms-fundamentals",
    "level": "Associate",
    "duration": 102,
    "questions_count": 34,
    "category_slug": "data-structures-algorithms",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the average time complexity of Quick Sort?",
        "explanation": "Quick Sort has an average time complexity of O(n log n), though its worst case is O(n²).",
        "reference": "https://en.wikipedia.org/wiki/Quicksort",
        "points": 1,
        "answers": [
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(log n)", "is_correct": False},
        ],
    },
    {
        "text": "Which sorting algorithm is stable and has O(n log n) guaranteed time complexity?",
        "explanation": "Merge Sort is stable (maintains relative order of equal elements) and has guaranteed O(n log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Merge_sort",
        "points": 1,
        "answers": [
            {"text": "Quick Sort", "is_correct": False},
            {"text": "Heap Sort", "is_correct": False},
            {"text": "Merge Sort", "is_correct": True},
            {"text": "Selection Sort", "is_correct": False},
        ],
    },
    {
        "text": "What is the time complexity of binary search on a sorted array?",
        "explanation": "Binary search divides the search space in half with each comparison, resulting in O(log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Binary_search_algorithm",
        "points": 1,
        "answers": [
            {"text": "O(1)", "is_correct": False},
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "What will this TypeScript bubble sort implementation output?\n\n```typescript\nfunction bubbleSort(arr: number[]): number[] {\n    const n = arr.length;\n    const result = [...arr];\n    \n    for (let i = 0; i < n - 1; i++) {\n        for (let j = 0; j < n - i - 1; j++) {\n            if (result[j] > result[j + 1]) {\n                [result[j], result[j + 1]] = [result[j + 1], result[j]];\n            }\n        }\n    }\n    \n    return result;\n}\n\nconst arr = [64, 34, 25, 12, 22, 11, 90];\nconsole.log(bubbleSort(arr));\n```",
        "explanation": "Bubble sort repeatedly swaps adjacent elements if they're in wrong order, eventually sorting the array in ascending order.",
        "reference": "https://en.wikipedia.org/wiki/Bubble_sort",
        "points": 2,
        "answers": [
            {"text": "[11, 12, 22, 25, 34, 64, 90]", "is_correct": True},
            {"text": "[90, 64, 34, 25, 22, 12, 11]", "is_correct": False},
            {"text": "[64, 34, 25, 12, 22, 11, 90]", "is_correct": False},
            {"text": "[12, 11, 22, 25, 34, 64, 90]", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs insertion sort?",
        "explanation": "Insertion sort builds the sorted array one element at a time by inserting each element into its correct position.",
        "reference": "https://en.wikipedia.org/wiki/Insertion_sort",
        "points": 2,
        "answers": [
            {
                "text": "function insertionSort(arr: number[]): number[] {\n    const result = [...arr];\n    \n    for (let i = 1; i < result.length; i++) {\n        const key = result[i];\n        let j = i - 1;\n        \n        while (j >= 0 && result[j] > key) {\n            result[j + 1] = result[j];\n            j--;\n        }\n        \n        result[j + 1] = key;\n    }\n    \n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function insertionSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function insertionSort(arr: number[]): number[] {\n    const result = [...arr];\n    for (let i = 0; i < result.length - 1; i++) {\n        if (result[i] > result[i + 1]) {\n            [result[i], result[i + 1]] = [result[i + 1], result[i]];\n        }\n    }\n    return result;\n}",
                "is_correct": False,
            },
            {
                "text": "function insertionSort(arr: number[]): number[] {\n    return arr.reverse();\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of this TypeScript selection sort implementation?\n\n```typescript\nfunction selectionSort(arr: number[]): number[] {\n    const result = [...arr];\n    const n = result.length;\n    \n    for (let i = 0; i < n - 1; i++) {\n        let minIndex = i;\n        \n        for (let j = i + 1; j < n; j++) {\n            if (result[j] < result[minIndex]) {\n                minIndex = j;\n            }\n        }\n        \n        if (minIndex !== i) {\n            [result[i], result[minIndex]] = [result[minIndex], result[i]];\n        }\n    }\n    \n    return result;\n}\n```",
        "explanation": "Selection sort has O(n²) time complexity in all cases because it always performs nested loops regardless of input.",
        "reference": "https://en.wikipedia.org/wiki/Selection_sort",
        "points": 2,
        "answers": [
            {"text": "O(n²)", "is_correct": True},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": False},
        ],
    },
    {
        "text": "What will this TypeScript recursive factorial implementation output?\n\n```typescript\nfunction factorial(n: number): number {\n    if (n <= 1) {\n        return 1;\n    }\n    return n * factorial(n - 1);\n}\n\nconsole.log(factorial(5));\n```",
        "explanation": "Factorial of 5 is 5! = 5 × 4 × 3 × 2 × 1 = 120.",
        "reference": "https://en.wikipedia.org/wiki/Factorial",
        "points": 1,
        "answers": [
            {"text": "120", "is_correct": True},
            {"text": "25", "is_correct": False},
            {"text": "15", "is_correct": False},
            {"text": "5", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs iterative binary search?",
        "explanation": "Iterative binary search maintains left and right pointers and narrows the search space by half in each iteration.",
        "reference": "https://en.wikipedia.org/wiki/Binary_search_algorithm",
        "points": 2,
        "answers": [
            {
                "text": "function binarySearch(arr: number[], target: number): number {\n    let left = 0;\n    let right = arr.length - 1;\n    \n    while (left <= right) {\n        const mid = Math.floor((left + right) / 2);\n        \n        if (arr[mid] === target) {\n            return mid;\n        } else if (arr[mid] < target) {\n            left = mid + 1;\n        } else {\n            right = mid - 1;\n        }\n    }\n    \n    return -1;\n}",
                "is_correct": True,
            },
            {
                "text": "function binarySearch(arr: number[], target: number): number {\n    for (let i = 0; i < arr.length; i++) {\n        if (arr[i] === target) return i;\n    }\n    return -1;\n}",
                "is_correct": False,
            },
            {
                "text": "function binarySearch(arr: number[], target: number): number {\n    const mid = Math.floor(arr.length / 2);\n    return arr[mid] === target ? mid : -1;\n}",
                "is_correct": False,
            },
            {
                "text": "function binarySearch(arr: number[], target: number): number {\n    return arr.indexOf(target);\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the output of this TypeScript recursive Fibonacci implementation?\n\n```typescript\nfunction fibonacci(n: number): number {\n    if (n <= 1) {\n        return n;\n    }\n    return fibonacci(n - 1) + fibonacci(n - 2);\n}\n\nconsole.log(fibonacci(6));\n```",
        "explanation": "Fibonacci sequence: F(6) = F(5) + F(4) = 5 + 3 = 8. The sequence is 0, 1, 1, 2, 3, 5, 8, ...",
        "reference": "https://en.wikipedia.org/wiki/Fibonacci_number",
        "points": 2,
        "answers": [
            {"text": "8", "is_correct": True},
            {"text": "13", "is_correct": False},
            {"text": "5", "is_correct": False},
            {"text": "6", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs merge sort?",
        "explanation": "Merge sort divides the array into halves, recursively sorts them, and then merges the sorted halves.",
        "reference": "https://en.wikipedia.org/wiki/Merge_sort",
        "points": 3,
        "answers": [
            {
                "text": "function mergeSort(arr: number[]): number[] {\n    if (arr.length <= 1) {\n        return arr;\n    }\n    \n    const mid = Math.floor(arr.length / 2);\n    const left = mergeSort(arr.slice(0, mid));\n    const right = mergeSort(arr.slice(mid));\n    \n    return merge(left, right);\n}\n\nfunction merge(left: number[], right: number[]): number[] {\n    const result: number[] = [];\n    let i = 0, j = 0;\n    \n    while (i < left.length && j < right.length) {\n        if (left[i] <= right[j]) {\n            result.push(left[i]);\n            i++;\n        } else {\n            result.push(right[j]);\n            j++;\n        }\n    }\n    \n    return result.concat(left.slice(i)).concat(right.slice(j));\n}",
                "is_correct": True,
            },
            {
                "text": "function mergeSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function mergeSort(arr: number[]): number[] {\n    const result = [...arr];\n    for (let i = 0; i < result.length - 1; i++) {\n        for (let j = 0; j < result.length - i - 1; j++) {\n            if (result[j] > result[j + 1]) {\n                [result[j], result[j + 1]] = [result[j + 1], result[j]];\n            }\n        }\n    }\n    return result;\n}",
                "is_correct": False,
            },
            {
                "text": "function mergeSort(arr: number[]): number[] {\n    return arr.filter((_, i) => i % 2 === 0).concat(arr.filter((_, i) => i % 2 === 1));\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of this TypeScript recursive binary search?\n\n```typescript\nfunction binarySearchRecursive(arr: number[], target: number, left: number = 0, right: number = arr.length - 1): number {\n    if (left > right) {\n        return -1;\n    }\n    \n    const mid = Math.floor((left + right) / 2);\n    \n    if (arr[mid] === target) {\n        return mid;\n    } else if (arr[mid] < target) {\n        return binarySearchRecursive(arr, target, mid + 1, right);\n    } else {\n        return binarySearchRecursive(arr, target, left, mid - 1);\n    }\n}\n```",
        "explanation": "Recursive binary search uses O(log n) space due to the call stack depth, as it makes log n recursive calls.",
        "reference": "https://en.wikipedia.org/wiki/Binary_search_algorithm",
        "points": 2,
        "answers": [
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(1)", "is_correct": False},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs quick sort with Lomuto partition?",
        "explanation": "Quick sort with Lomuto partition uses the last element as pivot and partitions around it.",
        "reference": "https://en.wikipedia.org/wiki/Quicksort",
        "points": 3,
        "answers": [
            {
                "text": "function quickSort(arr: number[], low: number = 0, high: number = arr.length - 1): number[] {\n    const result = [...arr];\n    \n    if (low < high) {\n        const pi = partition(result, low, high);\n        quickSort(result, low, pi - 1);\n        quickSort(result, pi + 1, high);\n    }\n    \n    return result;\n}\n\nfunction partition(arr: number[], low: number, high: number): number {\n    const pivot = arr[high];\n    let i = low - 1;\n    \n    for (let j = low; j < high; j++) {\n        if (arr[j] <= pivot) {\n            i++;\n            [arr[i], arr[j]] = [arr[j], arr[i]];\n        }\n    }\n    \n    [arr[i + 1], arr[high]] = [arr[high], arr[i + 1]];\n    return i + 1;\n}",
                "is_correct": True,
            },
            {
                "text": "function quickSort(arr: number[]): number[] {\n    if (arr.length <= 1) return arr;\n    return [...quickSort(arr.slice(1)), arr[0]];\n}",
                "is_correct": False,
            },
            {
                "text": "function quickSort(arr: number[]): number[] {\n    return arr.sort();\n}",
                "is_correct": False,
            },
            {
                "text": "function quickSort(arr: number[]): number[] {\n    const result = [...arr];\n    for (let i = 0; i < result.length; i++) {\n        for (let j = i + 1; j < result.length; j++) {\n            if (result[i] > result[j]) {\n                [result[i], result[j]] = [result[j], result[i]];\n            }\n        }\n    }\n    return result;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript linear search implementation output?\n\n```typescript\nfunction linearSearch(arr: number[], target: number): number {\n    for (let i = 0; i < arr.length; i++) {\n        if (arr[i] === target) {\n            return i;\n        }\n    }\n    return -1;\n}\n\nconst arr = [2, 4, 6, 8, 10, 12];\nconsole.log(linearSearch(arr, 8));\n```",
        "explanation": "Linear search finds the target value 8 at index 3 in the array [2, 4, 6, 8, 10, 12].",
        "reference": "https://en.wikipedia.org/wiki/Linear_search",
        "points": 1,
        "answers": [
            {"text": "3", "is_correct": True},
            {"text": "8", "is_correct": False},
            {"text": "4", "is_correct": False},
            {"text": "-1", "is_correct": False},
        ],
    },
    {
        "text": "Which sorting algorithm has the best worst-case time complexity?",
        "explanation": "Merge sort and heap sort both have O(n log n) worst-case time complexity, which is optimal for comparison-based sorting.",
        "reference": "https://en.wikipedia.org/wiki/Sorting_algorithm",
        "points": 2,
        "answers": [
            {"text": "Merge sort", "is_correct": True},
            {"text": "Quick sort", "is_correct": False},
            {"text": "Bubble sort", "is_correct": False},
            {"text": "Insertion sort", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of this TypeScript recursive power function?\n\n```typescript\nfunction power(base: number, exponent: number): number {\n    if (exponent === 0) {\n        return 1;\n    }\n    if (exponent === 1) {\n        return base;\n    }\n    \n    if (exponent % 2 === 0) {\n        const half = power(base, exponent / 2);\n        return half * half;\n    } else {\n        return base * power(base, exponent - 1);\n    }\n}\n\nconsole.log(power(2, 10));\n```",
        "explanation": "Power function calculates 2^10 = 1024 using efficient recursive approach with O(log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Exponentiation_by_squaring",
        "points": 2,
        "answers": [
            {"text": "1024", "is_correct": True},
            {"text": "100", "is_correct": False},
            {"text": "20", "is_correct": False},
            {"text": "512", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs heap sort?",
        "explanation": "Heap sort first builds a max heap, then repeatedly extracts the maximum element to get sorted order.",
        "reference": "https://en.wikipedia.org/wiki/Heapsort",
        "points": 3,
        "answers": [
            {
                "text": "function heapSort(arr: number[]): number[] {\n    const result = [...arr];\n    const n = result.length;\n    \n    // Build max heap\n    for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {\n        heapify(result, n, i);\n    }\n    \n    // Extract elements from heap one by one\n    for (let i = n - 1; i > 0; i--) {\n        [result[0], result[i]] = [result[i], result[0]];\n        heapify(result, i, 0);\n    }\n    \n    return result;\n}\n\nfunction heapify(arr: number[], n: number, i: number): void {\n    let largest = i;\n    const left = 2 * i + 1;\n    const right = 2 * i + 2;\n    \n    if (left < n && arr[left] > arr[largest]) {\n        largest = left;\n    }\n    \n    if (right < n && arr[right] > arr[largest]) {\n        largest = right;\n    }\n    \n    if (largest !== i) {\n        [arr[i], arr[largest]] = [arr[largest], arr[i]];\n        heapify(arr, n, largest);\n    }\n}",
                "is_correct": True,
            },
            {
                "text": "function heapSort(arr: number[]): number[] {\n    return arr.sort((a, b) => b - a);\n}",
                "is_correct": False,
            },
            {
                "text": "function heapSort(arr: number[]): number[] {\n    const heap = [];\n    for (const num of arr) heap.push(num);\n    return heap.sort();\n}",
                "is_correct": False,
            },
            {
                "text": "function heapSort(arr: number[]): number[] {\n    return arr.reverse();\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of finding the maximum element in an unsorted array?",
        "explanation": "Finding the maximum element requires examining each element once, resulting in O(n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Selection_algorithm",
        "points": 1,
        "answers": [
            {"text": "O(n)", "is_correct": True},
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly calculates GCD using Euclidean algorithm?",
        "explanation": "Euclidean algorithm for GCD uses the property that gcd(a, b) = gcd(b, a mod b).",
        "reference": "https://en.wikipedia.org/wiki/Euclidean_algorithm",
        "points": 2,
        "answers": [
            {
                "text": "function gcd(a: number, b: number): number {\n    if (b === 0) {\n        return a;\n    }\n    return gcd(b, a % b);\n}",
                "is_correct": True,
            },
            {
                "text": "function gcd(a: number, b: number): number {\n    return Math.max(a, b) / Math.min(a, b);\n}",
                "is_correct": False,
            },
            {
                "text": "function gcd(a: number, b: number): number {\n    return a + b;\n}",
                "is_correct": False,
            },
            {
                "text": "function gcd(a: number, b: number): number {\n    return a * b;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript implementation of Tower of Hanoi output for n=3?\n\n```typescript\nfunction towerOfHanoi(n: number, source: string, destination: string, auxiliary: string): string[] {\n    const moves: string[] = [];\n    \n    function hanoi(disks: number, src: string, dest: string, aux: string): void {\n        if (disks === 1) {\n            moves.push(`Move disk 1 from ${src} to ${dest}`);\n            return;\n        }\n        \n        hanoi(disks - 1, src, aux, dest);\n        moves.push(`Move disk ${disks} from ${src} to ${dest}`);\n        hanoi(disks - 1, aux, dest, src);\n    }\n    \n    hanoi(n, source, destination, auxiliary);\n    return moves;\n}\n\nconsole.log(towerOfHanoi(3, 'A', 'C', 'B').length);\n```",
        "explanation": "Tower of Hanoi with 3 disks requires 2^3 - 1 = 7 moves to transfer all disks from source to destination.",
        "reference": "https://en.wikipedia.org/wiki/Tower_of_Hanoi",
        "points": 3,
        "answers": [
            {"text": "7", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "8", "is_correct": False},
            {"text": "6", "is_correct": False},
        ],
    },
    {
        "text": "Which algorithm design paradigm does binary search follow?",
        "explanation": "Binary search follows the divide-and-conquer paradigm by dividing the search space in half at each step.",
        "reference": "https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm",
        "points": 2,
        "answers": [
            {"text": "Divide and conquer", "is_correct": True},
            {"text": "Dynamic programming", "is_correct": False},
            {"text": "Greedy", "is_correct": False},
            {"text": "Backtracking", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of this TypeScript prime number checking algorithm?\n\n```typescript\nfunction isPrime(n: number): boolean {\n    if (n <= 1) return False;\n    if (n <= 3) return True;\n    if (n % 2 === 0 || n % 3 === 0) return False;\n    \n    for (let i = 5; i * i <= n; i += 6) {\n        if (n % i === 0 || n % (i + 2) === 0) {\n            return False;\n        }\n    }\n    \n    return True;\n}\n\nconsole.log([17, 18, 19, 20].filter(isPrime));\n```",
        "explanation": "The algorithm checks primality efficiently. From [17, 18, 19, 20], only 17 and 19 are prime numbers.",
        "reference": "https://en.wikipedia.org/wiki/Primality_test",
        "points": 2,
        "answers": [
            {"text": "[17, 19]", "is_correct": True},
            {"text": "[17, 18, 19]", "is_correct": False},
            {"text": "[19, 20]", "is_correct": False},
            {"text": "[18, 20]", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs counting sort?",
        "explanation": "Counting sort works by counting occurrences of each element and then reconstructing the sorted array.",
        "reference": "https://en.wikipedia.org/wiki/Counting_sort",
        "points": 3,
        "answers": [
            {
                "text": "function countingSort(arr: number[]): number[] {\n    const max = Math.max(...arr);\n    const min = Math.min(...arr);\n    const range = max - min + 1;\n    const count = new Array(range).fill(0);\n    const result = new Array(arr.length);\n    \n    // Count occurrences\n    for (const num of arr) {\n        count[num - min]++;\n    }\n    \n    // Calculate cumulative count\n    for (let i = 1; i < count.length; i++) {\n        count[i] += count[i - 1];\n    }\n    \n    // Build result array\n    for (let i = arr.length - 1; i >= 0; i--) {\n        const num = arr[i];\n        result[count[num - min] - 1] = num;\n        count[num - min]--;\n    }\n    \n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function countingSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function countingSort(arr: number[]): number[] {\n    const counts = new Map();\n    for (const num of arr) {\n        counts.set(num, (counts.get(num) || 0) + 1);\n    }\n    return Array.from(counts.keys()).sort();\n}",
                "is_correct": False,
            },
            {
                "text": "function countingSort(arr: number[]): number[] {\n    return [...new Set(arr)].sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of this TypeScript matrix multiplication algorithm?\n\n```typescript\nfunction matrixMultiply(A: number[][], B: number[][]): number[][] {\n    const rows = A.length;\n    const cols = B[0].length;\n    const common = A[0].length;\n    const result = Array(rows).fill(null).map(() => Array(cols).fill(0));\n    \n    for (let i = 0; i < rows; i++) {\n        for (let j = 0; j < cols; j++) {\n            for (let k = 0; k < common; k++) {\n                result[i][j] += A[i][k] * B[k][j];\n            }\n        }\n    }\n    \n    return result;\n}\n```",
        "explanation": "Standard matrix multiplication has three nested loops, resulting in O(n³) time complexity for n×n matrices.",
        "reference": "https://en.wikipedia.org/wiki/Matrix_multiplication",
        "points": 2,
        "answers": [
            {"text": "O(n³)", "is_correct": True},
            {"text": "O(n²)", "is_correct": False},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(n log n)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs radix sort?",
        "explanation": "Radix sort sorts numbers digit by digit, starting from the least significant digit to the most significant digit.",
        "reference": "https://en.wikipedia.org/wiki/Radix_sort",
        "points": 3,
        "answers": [
            {
                "text": "function radixSort(arr: number[]): number[] {\n    const result = [...arr];\n    const max = Math.max(...result);\n    \n    for (let exp = 1; Math.floor(max / exp) > 0; exp *= 10) {\n        countingSortByDigit(result, exp);\n    }\n    \n    return result;\n}\n\nfunction countingSortByDigit(arr: number[], exp: number): void {\n    const count = new Array(10).fill(0);\n    const output = new Array(arr.length);\n    \n    // Count occurrences of each digit\n    for (const num of arr) {\n        const digit = Math.floor(num / exp) % 10;\n        count[digit]++;\n    }\n    \n    // Calculate cumulative count\n    for (let i = 1; i < 10; i++) {\n        count[i] += count[i - 1];\n    }\n    \n    // Build output array\n    for (let i = arr.length - 1; i >= 0; i--) {\n        const digit = Math.floor(arr[i] / exp) % 10;\n        output[count[digit] - 1] = arr[i];\n        count[digit]--;\n    }\n    \n    // Copy output array to original array\n    for (let i = 0; i < arr.length; i++) {\n        arr[i] = output[i];\n    }\n}",
                "is_correct": True,
            },
            {
                "text": "function radixSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function radixSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a.toString().localeCompare(b.toString()));\n}",
                "is_correct": False,
            },
            {
                "text": "function radixSort(arr: number[]): number[] {\n    const result = [];\n    for (let i = 0; i < 10; i++) {\n        result.push(...arr.filter(n => n % 10 === i));\n    }\n    return result;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": 'What will this TypeScript recursive palindrome checker output?\n\n```typescript\nfunction isPalindrome(str: string, start: number = 0, end: number = str.length - 1): boolean {\n    if (start >= end) {\n        return True;\n    }\n    \n    if (str[start] !== str[end]) {\n        return False;\n    }\n    \n    return isPalindrome(str, start + 1, end - 1);\n}\n\nconsole.log(["racecar", "hello", "madam", "world"].filter(isPalindrome));\n```',
        "explanation": "The recursive palindrome checker identifies strings that read the same forwards and backwards: 'racecar' and 'madam'.",
        "reference": "https://en.wikipedia.org/wiki/Palindrome",
        "points": 2,
        "answers": [
            {"text": '["racecar", "madam"]', "is_correct": True},
            {"text": '["hello", "world"]', "is_correct": False},
            {"text": '["racecar"]', "is_correct": False},
            {"text": "[]", "is_correct": False},
        ],
    },
    {
        "text": "Which algorithm has the best average-case time complexity for sorting?",
        "explanation": "Quick sort, merge sort, and heap sort all have O(n log n) average-case time complexity, which is optimal for comparison-based sorting.",
        "reference": "https://en.wikipedia.org/wiki/Sorting_algorithm",
        "points": 2,
        "answers": [
            {"text": "Quick sort", "is_correct": True},
            {"text": "Bubble sort", "is_correct": False},
            {"text": "Insertion sort", "is_correct": False},
            {"text": "Selection sort", "is_correct": False},
        ],
    },
    {
        "text": 'What is the output of this TypeScript recursive string reversal function?\n\n```typescript\nfunction reverseString(str: string): string {\n    if (str.length <= 1) {\n        return str;\n    }\n    \n    return reverseString(str.slice(1)) + str[0];\n}\n\nconsole.log(reverseString("algorithms"));\n```',
        "explanation": "The recursive function reverses 'algorithms' by recursively processing substrings and appending the first character at the end.",
        "reference": "https://en.wikipedia.org/wiki/String_(computer_science)",
        "points": 2,
        "answers": [
            {"text": "smhtirogla", "is_correct": True},
            {"text": "algorithms", "is_correct": False},
            {"text": "mhtiroglas", "is_correct": False},
            {"text": "salgoritm", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs bucket sort?",
        "explanation": "Bucket sort distributes elements into buckets, sorts each bucket individually, then concatenates them.",
        "reference": "https://en.wikipedia.org/wiki/Bucket_sort",
        "points": 3,
        "answers": [
            {
                "text": "function bucketSort(arr: number[], bucketCount: number = 10): number[] {\n    if (arr.length <= 1) return arr;\n    \n    const max = Math.max(...arr);\n    const min = Math.min(...arr);\n    const range = max - min;\n    const bucketSize = range / bucketCount;\n    \n    const buckets: number[][] = Array(bucketCount).fill(null).map(() => []);\n    \n    // Distribute elements into buckets\n    for (const num of arr) {\n        const bucketIndex = Math.min(\n            Math.floor((num - min) / bucketSize),\n            bucketCount - 1\n        );\n        buckets[bucketIndex].push(num);\n    }\n    \n    // Sort each bucket and concatenate\n    const result: number[] = [];\n    for (const bucket of buckets) {\n        if (bucket.length > 0) {\n            bucket.sort((a, b) => a - b);\n            result.push(...bucket);\n        }\n    }\n    \n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function bucketSort(arr: number[]): number[] {\n    const buckets = new Map();\n    for (const num of arr) {\n        buckets.set(num, (buckets.get(num) || 0) + 1);\n    }\n    return Array.from(buckets.keys()).sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function bucketSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function bucketSort(arr: number[]): number[] {\n    const even = arr.filter(n => n % 2 === 0);\n    const odd = arr.filter(n => n % 2 === 1);\n    return [...even.sort(), ...odd.sort()];\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the time complexity of this TypeScript algorithm for checking if a number is a perfect square?\n\n```typescript\nfunction isPerfectSquare(num: number): boolean {\n    if (num < 0) return False;\n    if (num === 0 || num === 1) return True;\n    \n    let left = 1;\n    let right = Math.floor(num / 2);\n    \n    while (left <= right) {\n        const mid = Math.floor((left + right) / 2);\n        const square = mid * mid;\n        \n        if (square === num) {\n            return True;\n        } else if (square < num) {\n            left = mid + 1;\n        } else {\n            right = mid - 1;\n        }\n    }\n    \n    return False;\n}\n```",
        "explanation": "This algorithm uses binary search to find the square root, so it has O(log n) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Perfect_square",
        "points": 2,
        "answers": [
            {"text": "O(log n)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(√n)", "is_correct": False},
            {"text": "O(1)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly finds the intersection of two sorted arrays?",
        "explanation": "Two-pointer technique efficiently finds common elements in sorted arrays by advancing pointers based on comparisons.",
        "reference": "https://en.wikipedia.org/wiki/Two_pointers_technique",
        "points": 2,
        "answers": [
            {
                "text": "function intersection(arr1: number[], arr2: number[]): number[] {\n    const result: number[] = [];\n    let i = 0, j = 0;\n    \n    while (i < arr1.length && j < arr2.length) {\n        if (arr1[i] === arr2[j]) {\n            result.push(arr1[i]);\n            i++;\n            j++;\n        } else if (arr1[i] < arr2[j]) {\n            i++;\n        } else {\n            j++;\n        }\n    }\n    \n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function intersection(arr1: number[], arr2: number[]): number[] {\n    return arr1.filter(x => arr2.includes(x));\n}",
                "is_correct": False,
            },
            {
                "text": "function intersection(arr1: number[], arr2: number[]): number[] {\n    return [...arr1, ...arr2].filter((x, i, arr) => arr.indexOf(x) !== arr.lastIndexOf(x));\n}",
                "is_correct": False,
            },
            {
                "text": "function intersection(arr1: number[], arr2: number[]): number[] {\n    const set1 = new Set(arr1);\n    return arr2.filter(x => set1.has(x));\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript implementation of Sieve of Eratosthenes output?\n\n```typescript\nfunction sieveOfEratosthenes(limit: number): number[] {\n    const isPrime = new Array(limit + 1).fill(True);\n    isPrime[0] = isPrime[1] = False;\n    \n    for (let i = 2; i * i <= limit; i++) {\n        if (isPrime[i]) {\n            for (let j = i * i; j <= limit; j += i) {\n                isPrime[j] = False;\n            }\n        }\n    }\n    \n    const primes: number[] = [];\n    for (let i = 2; i <= limit; i++) {\n        if (isPrime[i]) {\n            primes.push(i);\n        }\n    }\n    \n    return primes;\n}\n\nconsole.log(sieveOfEratosthenes(20));\n```",
        "explanation": "Sieve of Eratosthenes finds all prime numbers up to 20: [2, 3, 5, 7, 11, 13, 17, 19].",
        "reference": "https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes",
        "points": 3,
        "answers": [
            {"text": "[2, 3, 5, 7, 11, 13, 17, 19]", "is_correct": True},
            {"text": "[1, 2, 3, 5, 7, 11, 13, 17, 19]", "is_correct": False},
            {"text": "[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]", "is_correct": False},
            {"text": "[3, 5, 7, 11, 13, 17, 19]", "is_correct": False},
        ],
    },
    {
        "text": "Which algorithm design technique is used in merge sort?",
        "explanation": "Merge sort uses divide-and-conquer by dividing the array into halves, recursively sorting them, and merging the results.",
        "reference": "https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm",
        "points": 2,
        "answers": [
            {"text": "Divide and conquer", "is_correct": True},
            {"text": "Dynamic programming", "is_correct": False},
            {"text": "Greedy", "is_correct": False},
            {"text": "Backtracking", "is_correct": False},
        ],
    },
    {
        "text": 'What is the output of this TypeScript algorithm for finding all permutations of a string?\n\n```typescript\nfunction getAllPermutations(str: string): string[] {\n    if (str.length <= 1) {\n        return [str];\n    }\n    \n    const permutations: string[] = [];\n    \n    for (let i = 0; i < str.length; i++) {\n        const char = str[i];\n        const remaining = str.slice(0, i) + str.slice(i + 1);\n        const subPermutations = getAllPermutations(remaining);\n        \n        for (const perm of subPermutations) {\n            permutations.push(char + perm);\n        }\n    }\n    \n    return permutations;\n}\n\nconsole.log(getAllPermutations("abc").length);\n```',
        "explanation": "The number of permutations of n distinct characters is n!. For 'abc' (3 characters), it's 3! = 6 permutations.",
        "reference": "https://en.wikipedia.org/wiki/Permutation",
        "points": 2,
        "answers": [
            {"text": "6", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "9", "is_correct": False},
            {"text": "8", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly performs shell sort?",
        "explanation": "Shell sort is a variation of insertion sort that allows exchange of far apart elements by using gap sequences.",
        "reference": "https://en.wikipedia.org/wiki/Shellsort",
        "points": 3,
        "answers": [
            {
                "text": "function shellSort(arr: number[]): number[] {\n    const result = [...arr];\n    const n = result.length;\n    \n    // Start with a big gap, then reduce the gap\n    for (let gap = Math.floor(n / 2); gap > 0; gap = Math.floor(gap / 2)) {\n        // Do a gapped insertion sort for this gap size\n        for (let i = gap; i < n; i++) {\n            const temp = result[i];\n            let j = i;\n            \n            // Shift earlier gap-sorted elements up until correct location\n            while (j >= gap && result[j - gap] > temp) {\n                result[j] = result[j - gap];\n                j -= gap;\n            }\n            \n            result[j] = temp;\n        }\n    }\n    \n    return result;\n}",
                "is_correct": True,
            },
            {
                "text": "function shellSort(arr: number[]): number[] {\n    return arr.sort((a, b) => a - b);\n}",
                "is_correct": False,
            },
            {
                "text": "function shellSort(arr: number[]): number[] {\n    const result = [...arr];\n    for (let i = 1; i < result.length; i++) {\n        const key = result[i];\n        let j = i - 1;\n        while (j >= 0 && result[j] > key) {\n            result[j + 1] = result[j];\n            j--;\n        }\n        result[j + 1] = key;\n    }\n    return result;\n}",
                "is_correct": False,
            },
            {
                "text": "function shellSort(arr: number[]): number[] {\n    const shells = [];\n    for (let i = 0; i < arr.length; i += 2) {\n        shells.push(arr[i]);\n    }\n    return shells.sort();\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What is the space complexity of the iterative implementation of factorial?\n\n```typescript\nfunction factorialIterative(n: number): number {\n    let result = 1;\n    for (let i = 2; i <= n; i++) {\n        result *= i;\n    }\n    return result;\n}\n```",
        "explanation": "The iterative factorial implementation uses only a constant amount of extra space regardless of input size.",
        "reference": "https://en.wikipedia.org/wiki/Factorial",
        "points": 2,
        "answers": [
            {"text": "O(1)", "is_correct": True},
            {"text": "O(n)", "is_correct": False},
            {"text": "O(log n)", "is_correct": False},
            {"text": "O(n²)", "is_correct": False},
        ],
    },
    {
        "text": "Which TypeScript implementation correctly finds the median of two sorted arrays?",
        "explanation": "Finding median of two sorted arrays requires binary search approach to achieve O(log(min(m,n))) time complexity.",
        "reference": "https://en.wikipedia.org/wiki/Median",
        "points": 4,
        "answers": [
            {
                "text": "function findMedianSortedArrays(nums1: number[], nums2: number[]): number {\n    const [A, B] = nums1.length <= nums2.length ? [nums1, nums2] : [nums2, nums1];\n    const m = A.length;\n    const n = B.length;\n    const halfLen = Math.floor((m + n + 1) / 2);\n    \n    let left = 0, right = m;\n    \n    while (left <= right) {\n        const i = Math.floor((left + right) / 2);\n        const j = halfLen - i;\n        \n        if (i < m && B[j - 1] > A[i]) {\n            left = i + 1;\n        } else if (i > 0 && A[i - 1] > B[j]) {\n            right = i - 1;\n        } else {\n            let maxOfLeft: number;\n            if (i === 0) maxOfLeft = B[j - 1];\n            else if (j === 0) maxOfLeft = A[i - 1];\n            else maxOfLeft = Math.max(A[i - 1], B[j - 1]);\n            \n            if ((m + n) % 2 === 1) return maxOfLeft;\n            \n            let minOfRight: number;\n            if (i === m) minOfRight = B[j];\n            else if (j === n) minOfRight = A[i];\n            else minOfRight = Math.min(A[i], B[j]);\n            \n            return (maxOfLeft + minOfRight) / 2;\n        }\n    }\n    \n    return 0;\n}",
                "is_correct": True,
            },
            {
                "text": "function findMedianSortedArrays(nums1: number[], nums2: number[]): number {\n    const merged = [...nums1, ...nums2].sort((a, b) => a - b);\n    const n = merged.length;\n    return n % 2 === 0 ? (merged[n/2 - 1] + merged[n/2]) / 2 : merged[Math.floor(n/2)];\n}",
                "is_correct": False,
            },
            {
                "text": "function findMedianSortedArrays(nums1: number[], nums2: number[]): number {\n    return (Math.max(...nums1) + Math.min(...nums2)) / 2;\n}",
                "is_correct": False,
            },
            {
                "text": "function findMedianSortedArrays(nums1: number[], nums2: number[]): number {\n    return (nums1[0] + nums2[0]) / 2;\n}",
                "is_correct": False,
            },
        ],
    },
    {
        "text": "What will this TypeScript implementation of Dutch National Flag algorithm output?\n\n```typescript\nfunction dutchNationalFlag(arr: number[]): number[] {\n    const result = [...arr];\n    let low = 0, mid = 0, high = result.length - 1;\n    \n    while (mid <= high) {\n        if (result[mid] === 0) {\n            [result[low], result[mid]] = [result[mid], result[low]];\n            low++;\n            mid++;\n        } else if (result[mid] === 1) {\n            mid++;\n        } else { // result[mid] === 2\n            [result[mid], result[high]] = [result[high], result[mid]];\n            high--;\n        }\n    }\n    \n    return result;\n}\n\nconst arr = [2, 0, 2, 1, 1, 0];\nconsole.log(dutchNationalFlag(arr));\n```",
        "explanation": "Dutch National Flag algorithm sorts an array of 0s, 1s, and 2s in linear time. Result: [0, 0, 1, 1, 2, 2].",
        "reference": "https://en.wikipedia.org/wiki/Dutch_national_flag_problem",
        "points": 3,
        "answers": [
            {"text": "[0, 0, 1, 1, 2, 2]", "is_correct": True},
            {"text": "[2, 2, 1, 1, 0, 0]", "is_correct": False},
            {"text": "[0, 1, 0, 1, 2, 2]", "is_correct": False},
            {"text": "[2, 0, 2, 1, 1, 0]", "is_correct": False},
        ],
    },
]
