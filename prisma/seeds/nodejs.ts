import { PrismaClient } from '../../src/generated/prisma'

export async function seedNodeJS(prisma: PrismaClient, categoryId: number) {
  const nodejs = await prisma.certification.upsert({
    where: { slug: 'nodejs' },
    update: {},
    create: {
      name: 'Node.js Backend Development',
      description: 'Server-side JavaScript development with Node.js',
      slug: 'nodejs',
      level: 'Intermediate',
      duration: 75,
      questionsCount: 30,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the Node.js event loop?',
            explanation: 'The event loop is what allows Node.js to perform non-blocking I/O operations by offloading operations to the system kernel whenever possible.',
            points: 1,
            answers: {
              create: [
                { text: 'A mechanism for handling asynchronous operations', isCorrect: true },
                { text: 'A debugging tool', isCorrect: false },
                { text: 'A package manager', isCorrect: false },
                { text: 'A testing framework', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is npm?',
            explanation: 'npm (Node Package Manager) is the default package manager for Node.js, used to install and manage JavaScript packages.',
            points: 1,
            answers: {
              create: [
                { text: 'Node Package Manager for JavaScript packages', isCorrect: true },
                { text: 'A JavaScript framework', isCorrect: false },
                { text: 'A database system', isCorrect: false },
                { text: 'A web server', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between require() and import in Node.js?',
            explanation: 'require() is CommonJS syntax for synchronous module loading, while import is ES6 syntax for asynchronous module loading.',
            points: 1,
            answers: {
              create: [
                { text: 'require() is CommonJS, import is ES6 modules', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: 'require() is for client-side only', isCorrect: false },
                { text: 'import is deprecated', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is middleware in Express.js?',
            explanation: 'Middleware functions are functions that have access to the request object, response object, and the next function in the application\'s request-response cycle.',
            points: 1,
            answers: {
              create: [
                { text: 'Functions that execute during request-response cycle', isCorrect: true },
                { text: 'A type of database connection', isCorrect: false },
                { text: 'A caching mechanism', isCorrect: false },
                { text: 'A security protocol', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of process.nextTick() in Node.js?',
            explanation: 'process.nextTick() schedules a callback to be invoked in the next iteration of the event loop, before any other I/O events.',
            points: 1,
            answers: {
              create: [
                { text: 'Schedules callback for next event loop iteration', isCorrect: true },
                { text: 'Restarts the Node.js process', isCorrect: false },
                { text: 'Handles process termination', isCorrect: false },
                { text: 'Manages memory cleanup', isCorrect: false },
              ],
            },
          }
        ],
      },
    },
  })

  return nodejs
}
