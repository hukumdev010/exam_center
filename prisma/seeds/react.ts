import { PrismaClient } from '../../src/generated/prisma'

export async function seedReact(prisma: PrismaClient, categoryId: number) {
  const react = await prisma.certification.upsert({
    where: { slug: 'react-fundamentals' },
    update: {},
    create: {
      name: 'React Fundamentals',
      description: 'Core React concepts, hooks, and modern development patterns',
      slug: 'react-fundamentals',
      level: 'Fundamentals',
      duration: 75,
      questionsCount: 30,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is a React component?',
            explanation: 'A React component is a reusable piece of UI that can accept props and return JSX elements to describe what should appear on the screen.',
            points: 1,
            answers: {
              create: [
                { text: 'A reusable piece of UI that returns JSX', isCorrect: true },
                { text: 'A CSS class', isCorrect: false },
                { text: 'A JavaScript function only', isCorrect: false },
                { text: 'A database model', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of the useState hook?',
            explanation: 'useState is a React hook that allows you to add state to functional components. It returns an array with the current state value and a function to update it.',
            points: 1,
            answers: {
              create: [
                { text: 'Add state to functional components', isCorrect: true },
                { text: 'Handle side effects', isCorrect: false },
                { text: 'Create context', isCorrect: false },
                { text: 'Manage component lifecycle', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is JSX?',
            explanation: 'JSX is a syntax extension for JavaScript that allows you to write HTML-like code in JavaScript. It gets compiled to React.createElement() calls.',
            points: 1,
            answers: {
              create: [
                { text: 'A syntax extension for JavaScript that looks like HTML', isCorrect: true },
                { text: 'A new programming language', isCorrect: false },
                { text: 'A CSS framework', isCorrect: false },
                { text: 'A database query language', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the purpose of props in React?',
            explanation: 'Props (properties) are used to pass data from parent components to child components. They are read-only and help make components reusable.',
            points: 1,
            answers: {
              create: [
                { text: 'Pass data from parent to child components', isCorrect: true },
                { text: 'Store component state', isCorrect: false },
                { text: 'Handle user events', isCorrect: false },
                { text: 'Connect to databases', isCorrect: false },
              ],
            },
          },
          {
            text: 'When should you use useEffect hook?',
            explanation: 'useEffect is used for side effects like data fetching, subscriptions, timers, or manually changing the DOM. It runs after render.',
            points: 1,
            answers: {
              create: [
                { text: 'For side effects like data fetching and subscriptions', isCorrect: true },
                { text: 'Only for state management', isCorrect: false },
                { text: 'For component rendering', isCorrect: false },
                { text: 'For handling user input', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the Virtual DOM?',
            explanation: 'The Virtual DOM is a JavaScript representation of the real DOM. React uses it to optimize rendering by comparing changes and updating only what has changed.',
            points: 1,
            answers: {
              create: [
                { text: 'A JavaScript representation of the real DOM for optimization', isCorrect: true },
                { text: 'A new web browser', isCorrect: false },
                { text: 'A CSS property', isCorrect: false },
                { text: 'A database technology', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the difference between controlled and uncontrolled components?',
            explanation: 'Controlled components have their form data handled by React state, while uncontrolled components store form data in the DOM itself.',
            points: 1,
            answers: {
              create: [
                { text: 'Controlled components use React state, uncontrolled use DOM', isCorrect: true },
                { text: 'There is no difference', isCorrect: false },
                { text: 'Controlled components are faster', isCorrect: false },
                { text: 'Uncontrolled components use props', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is React Context?',
            explanation: 'React Context provides a way to pass data through the component tree without having to pass props down manually at every level.',
            points: 1,
            answers: {
              create: [
                { text: 'A way to share data across the component tree without prop drilling', isCorrect: true },
                { text: 'A state management library', isCorrect: false },
                { text: 'A routing solution', isCorrect: false },
                { text: 'A testing framework', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is the key prop used for in React lists?',
            explanation: 'The key prop helps React identify which items have changed, are added, or removed. It should be a stable, unique identifier.',
            points: 1,
            answers: {
              create: [
                { text: 'To help React identify changes in lists efficiently', isCorrect: true },
                { text: 'To style list items', isCorrect: false },
                { text: 'To sort list items', isCorrect: false },
                { text: 'To filter list items', isCorrect: false },
              ],
            },
          },
          {
            text: 'What is React.Fragment used for?',
            explanation: 'React.Fragment allows you to group multiple elements without adding an extra DOM node. It can be written as <></> for short.',
            points: 1,
            answers: {
              create: [
                { text: 'Group multiple elements without adding extra DOM nodes', isCorrect: true },
                { text: 'Create reusable components', isCorrect: false },
                { text: 'Handle form submissions', isCorrect: false },
                { text: 'Manage component state', isCorrect: false },
              ],
            },
          },
        ],
      },
    },
  })

  return react
}
