import { PrismaClient } from '../../src/generated/prisma'

export async function seedTypeScript(prisma: PrismaClient, categoryId: number) {
  const typescript = await prisma.certification.upsert({
    where: { slug: 'typescript' },
    update: {},
    create: {
      name: 'TypeScript Advanced',
      description: 'Advanced TypeScript features and type system',
      slug: 'typescript',
      level: 'Advanced',
      duration: 90,
      questionsCount: 35,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the purpose of TypeScript interfaces?',
            explanation: 'Interfaces in TypeScript define the structure of objects and provide type checking at compile time.',
            points: 1,
            answers: {
              create: [
                { text: 'To define object structure and enable type checking', isCorrect: true },
                { text: 'To create classes', isCorrect: false },
                { text: 'To handle runtime errors', isCorrect: false },
                { text: 'To manage memory allocation', isCorrect: false },
              ],
            },
          },
          {
            text: 'What are TypeScript generics?',
            explanation: 'Generics allow you to create reusable components that work with multiple types while maintaining type safety.',
            points: 1,
            answers: {
              create: [
                { text: 'Reusable components that work with multiple types', isCorrect: true },
                { text: 'A way to handle errors', isCorrect: false },
                { text: 'A compilation target', isCorrect: false },
                { text: 'A module system', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between type and interface in TypeScript?',
            explanation: 'Interfaces can be extended and merged, while types are more flexible and can represent unions, primitives, and computed types.',
            points: 1,
            answers: {
              create: [
                { text: 'Interfaces can be extended and merged, types are more flexible', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: 'Types are only for primitives', isCorrect: false },
                { text: 'Interfaces are only for classes', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a union type in TypeScript?',
            explanation: 'A union type allows a value to be one of several types, indicated by the | (pipe) symbol.',
            points: 1,
            answers: {
              create: [
                { text: 'A type that can be one of several types using |', isCorrect: true },
                { text: 'A way to combine multiple objects', isCorrect: false },
                { text: 'A type for database unions', isCorrect: false },
                { text: 'A mathematical operation type', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of the "never" type in TypeScript?',
            explanation: 'The "never" type represents values that never occur, such as functions that always throw errors or infinite loops.',
            points: 1,
            answers: {
              create: [
                { text: 'Represents values that never occur', isCorrect: true },
                { text: 'Represents undefined values', isCorrect: false },
                { text: 'Is used for optional properties', isCorrect: false },
                { text: 'Represents null values', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return typescript
}
