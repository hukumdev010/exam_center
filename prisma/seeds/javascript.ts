import { PrismaClient } from '../../src/generated/prisma'

export async function seedJavaScript(prisma: PrismaClient, categoryId: number) {
  const javascript = await prisma.certification.create({
    data: {
      name: 'JavaScript Fundamentals',
      description: 'Core JavaScript concepts and modern ES6+ features',
      slug: 'javascript',
      level: 'Fundamentals',
      duration: 60,
      questionsCount: 25,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the difference between let, const, and var?',
            explanation: 'let and const are block-scoped, while var is function-scoped. const creates immutable bindings, let allows reassignment.',
            points: 1,
            answers: {
              create: [
                { text: 'let and const are block-scoped, var is function-scoped', isCorrect: true },
                { text: 'They are all the same', isCorrect: false },
                { text: 'Only var can be reassigned', isCorrect: false },
                { text: 'const is function-scoped', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is a closure in JavaScript?',
            explanation: 'A closure is a function that has access to variables in its outer (enclosing) scope even after the outer function has returned.',
            points: 1,
            answers: {
              create: [
                { text: 'A function with access to outer scope variables', isCorrect: true },
                { text: 'A way to close browser windows', isCorrect: false },
                { text: 'A type of loop', isCorrect: false },
                { text: 'A database connection', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between == and === in JavaScript?',
            explanation: '== performs type coercion before comparison, while === checks both value and type without coercion (strict equality).',
            points: 1,
            answers: {
              create: [
                { text: '=== checks both value and type, == performs type coercion', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: '== is faster than ===', isCorrect: false },
                { text: '=== only works with numbers', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is hoisting in JavaScript?',
            explanation: 'Hoisting is JavaScript\'s behavior of moving variable and function declarations to the top of their scope during compilation.',
            points: 1,
            answers: {
              create: [
                { text: 'Moving declarations to the top of their scope', isCorrect: true },
                { text: 'A way to optimize code performance', isCorrect: false },
                { text: 'A method to handle errors', isCorrect: false },
                { text: 'A technique for data binding', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of the "this" keyword in JavaScript?',
            explanation: 'The "this" keyword refers to the object that is currently executing the code. Its value depends on how a function is called.',
            points: 1,
            answers: {
              create: [
                { text: 'Refers to the object currently executing the code', isCorrect: true },
                { text: 'Always refers to the global object', isCorrect: false },
                { text: 'Is used to declare variables', isCorrect: false },
                { text: 'Is a reserved keyword with no function', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return javascript
}
