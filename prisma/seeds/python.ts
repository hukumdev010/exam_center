import { PrismaClient } from '../../src/generated/prisma'

export async function seedPython(prisma: PrismaClient, categoryId: number) {
  const python = await prisma.certification.upsert({
    where: { slug: 'python' },
    update: {},
    create: {
      name: 'Python Programming',
      description: 'Python fundamentals and advanced concepts',
      slug: 'python',
      level: 'Fundamentals',
      duration: 90,
      questionsCount: 40,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the difference between a list and a tuple in Python?',
            explanation: 'Lists are mutable (can be changed) while tuples are immutable (cannot be changed after creation).',
            points: 1,
            answers: {
              create: [
                { text: 'Lists are mutable, tuples are immutable', isCorrect: true },
                { text: 'Lists are faster than tuples', isCorrect: false },
                { text: 'Tuples can only store numbers', isCorrect: false },
                { text: 'There is no difference', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a Python decorator?',
            explanation: 'A decorator is a function that modifies or extends the behavior of another function without permanently modifying it.',
            points: 1,
            answers: {
              create: [
                { text: 'A function that modifies another function\'s behavior', isCorrect: true },
                { text: 'A way to add comments to code', isCorrect: false },
                { text: 'A type of variable', isCorrect: false },
                { text: 'A debugging tool', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of __init__.py files?',
            explanation: '__init__.py files make Python treat directories as packages and can contain initialization code for the package.',
            points: 1,
            answers: {
              create: [
                { text: 'Makes directories into Python packages', isCorrect: true },
                { text: 'Contains the main program logic', isCorrect: false },
                { text: 'Stores configuration settings', isCorrect: false },
                { text: 'Is used for error handling', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between append() and extend() methods in Python lists?',
            explanation: 'append() adds a single element to the end of a list, while extend() adds all elements from an iterable.',
            points: 1,
            answers: {
              create: [
                { text: 'append() adds one element, extend() adds all elements from iterable', isCorrect: true },
                { text: 'They do the same thing', isCorrect: false },
                { text: 'extend() is faster', isCorrect: false },
                { text: 'append() only works with strings', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a lambda function in Python?',
            explanation: 'A lambda function is an anonymous function that can have any number of arguments but can only have one expression.',
            points: 1,
            answers: {
              create: [
                { text: 'An anonymous function with one expression', isCorrect: true },
                { text: 'A way to import modules', isCorrect: false },
                { text: 'A type of loop', isCorrect: false },
                { text: 'A debugging statement', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return python
}
