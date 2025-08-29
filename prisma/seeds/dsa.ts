import { PrismaClient } from '../../src/generated/prisma'

export async function seedDSA(prisma: PrismaClient, categoryId: number) {
  const dsa = await prisma.certification.upsert({
    where: { slug: 'dsa-fundamentals' },
    update: {},
    create: {
      name: 'Data Structures and Algorithms',
      description: 'Core data structures and algorithmic concepts for technical interviews and problem solving',
      slug: 'dsa-fundamentals',
      level: 'Intermediate',
      duration: 120,
      questionsCount: 40,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the time complexity of accessing an element in an array by index?',
            explanation: 'Array access by index is O(1) because arrays store elements in contiguous memory locations, allowing direct calculation of memory address.',
            points: 1,
            answers: {
              create: [
                { text: 'O(1)', isCorrect: true },
                { text: 'O(n)', isCorrect: false },
                { text: 'O(log n)', isCorrect: false },
                { text: 'O(n²)', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which data structure follows the LIFO (Last In, First Out) principle?',
            explanation: 'A stack follows LIFO principle where the last element added is the first one to be removed, like a stack of plates.',
            points: 1,
            answers: {
              create: [
                { text: 'Stack', isCorrect: true },
                { text: 'Queue', isCorrect: false },
                { text: 'Array', isCorrect: false },
                { text: 'Linked List', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the average time complexity of searching in a balanced binary search tree?',
            explanation: 'In a balanced BST, search operations have O(log n) time complexity because we can eliminate half of the remaining nodes at each step.',
            points: 1,
            answers: {
              create: [
                { text: 'O(log n)', isCorrect: true },
                { text: 'O(1)', isCorrect: false },
                { text: 'O(n)', isCorrect: false },
                { text: 'O(n log n)', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which sorting algorithm has the best average-case time complexity?',
            explanation: 'Merge Sort and Heap Sort both have O(n log n) average-case time complexity, which is optimal for comparison-based sorting algorithms.',
            points: 1,
            answers: {
              create: [
                { text: 'Merge Sort', isCorrect: true },
                { text: 'Bubble Sort', isCorrect: false },
                { text: 'Selection Sort', isCorrect: false },
                { text: 'Insertion Sort', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a hash collision?',
            explanation: 'A hash collision occurs when two different keys produce the same hash value, which can be resolved using techniques like chaining or open addressing.',
            points: 1,
            answers: {
              create: [
                { text: 'When two different keys produce the same hash value', isCorrect: true },
                { text: 'When a hash table runs out of space', isCorrect: false },
                { text: 'When a hash function fails', isCorrect: false },
                { text: 'When hash table performance degrades', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the space complexity of merge sort?',
            explanation: 'Merge sort requires O(n) additional space for the temporary arrays used during the merge process.',
            points: 1,
            answers: {
              create: [
                { text: 'O(n)', isCorrect: true },
                { text: 'O(1)', isCorrect: false },
                { text: 'O(log n)', isCorrect: false },
                { text: 'O(n²)', isCorrect: false },
              ],
            },
          },
          {
            text: 'Which data structure is best for implementing a priority queue?',
            explanation: 'A heap is the most efficient data structure for implementing a priority queue, providing O(log n) insertion and extraction of the highest priority element.',
            points: 1,
            answers: {
              create: [
                { text: 'Heap', isCorrect: true },
                { text: 'Array', isCorrect: false },
                { text: 'Linked List', isCorrect: false },
                { text: 'Stack', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the time complexity of DFS (Depth-First Search) in a graph?',
            explanation: 'DFS visits each vertex once and explores all edges, resulting in O(V + E) time complexity where V is vertices and E is edges.',
            points: 1,
            answers: {
              create: [
                { text: 'O(V + E)', isCorrect: true },
                { text: 'O(V²)', isCorrect: false },
                { text: 'O(E²)', isCorrect: false },
                { text: 'O(V × E)', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is dynamic programming?',
            explanation: 'Dynamic programming is an algorithmic technique that solves complex problems by breaking them down into simpler subproblems and storing their solutions to avoid redundant calculations.',
            points: 1,
            answers: {
              create: [
                { text: 'A technique that stores solutions to subproblems to avoid redundant calculations', isCorrect: true },
                { text: 'A way to allocate memory dynamically', isCorrect: false },
                { text: 'A programming paradigm like OOP', isCorrect: false },
                { text: 'A database optimization technique', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between BFS and DFS?',
            explanation: 'BFS explores nodes level by level using a queue, while DFS goes as deep as possible using a stack. BFS finds shortest path in unweighted graphs.',
            points: 1,
            answers: {
              create: [
                { text: 'BFS explores level by level, DFS goes as deep as possible', isCorrect: true },
                { text: 'BFS is faster than DFS', isCorrect: false },
                { text: 'DFS uses more memory than BFS', isCorrect: false },
                { text: 'They are the same algorithm', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a trie data structure used for?',
            explanation: 'A trie (prefix tree) is used for efficient storage and retrieval of strings, commonly used for autocomplete, spell checkers, and IP routing.',
            points: 1,
            answers: {
              create: [
                { text: 'Efficient storage and retrieval of strings', isCorrect: true },
                { text: 'Storing numerical data', isCorrect: false },
                { text: 'Graph traversal', isCorrect: false },
                { text: 'Sorting algorithms', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of the two-pointer technique?',
            explanation: 'The two-pointer technique uses two pointers moving through data structure to solve problems efficiently, often reducing time complexity from O(n²) to O(n).',
            points: 1,
            answers: {
              create: [
                { text: 'To solve problems efficiently by using two pointers moving through data', isCorrect: true },
                { text: 'To allocate memory for two variables', isCorrect: false },
                { text: 'To compare two arrays', isCorrect: false },
                { text: 'To create doubly linked lists', isCorrect: false },
              ],
            },
          },
        ],
      },
    },
  })

  return dsa
}
