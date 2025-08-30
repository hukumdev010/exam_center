import { PrismaClient } from '../../src/generated/prisma'

// Helper function to randomize answer order
function shuffleAnswers(answers: { text: string; isCorrect: boolean }[]) {
  const shuffled = [...answers];
  for (let i = shuffled.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
  }
  return shuffled;
}

export async function seedJavaScript(prisma: PrismaClient, categoryId: number) {
  const javascript = await prisma.certification.create({
    data: {
      name: 'JavaScript Fundamentals',
      description: 'Core JavaScript concepts and modern ES6+ features',
      slug: 'javascript',
      level: 'Fundamentals',
      duration: 60,
      questionsCount: 85,
      categoryId,
      questions: {
        create: [
          {
            text: 'What is the difference between let, const, and var?',
            explanation: 'let and const are block-scoped, while var is function-scoped. const creates immutable bindings, let allows reassignment.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'let and const are block-scoped, var is function-scoped', isCorrect: true },
                { text: 'They are all the same', isCorrect: false },
                { text: 'Only var can be reassigned', isCorrect: false },
                { text: 'const is function-scoped', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is a closure in JavaScript?',
            explanation: 'A closure is a function that has access to variables in its outer (enclosing) scope even after the outer function has returned.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'A function with access to outer scope variables', isCorrect: true },
                { text: 'A way to close browser windows', isCorrect: false },
                { text: 'A type of loop', isCorrect: false },
                { text: 'A database connection', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the difference between == and === in JavaScript?',
            explanation: '== performs type coercion before comparison, while === checks both value and type without coercion (strict equality).',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: '=== checks both value and type, == performs type coercion', isCorrect: true },
                { text: 'They are exactly the same', isCorrect: false },
                { text: '== is faster than ===', isCorrect: false },
                { text: '=== only works with numbers', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is hoisting in JavaScript?',
            explanation: 'Hoisting is JavaScript\'s behavior of moving variable and function declarations to the top of their scope during compilation.',
            reference: 'https://developer.mozilla.org/en-US/docs/Glossary/Hoisting',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'Moving declarations to the top of their scope', isCorrect: true },
                { text: 'A way to optimize code performance', isCorrect: false },
                { text: 'A method to handle errors', isCorrect: false },
                { text: 'A technique for data binding', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the purpose of the "this" keyword in JavaScript?',
            explanation: 'The "this" keyword refers to the object that is currently executing the code. Its value depends on how a function is called.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'Refers to the object currently executing the code', isCorrect: true },
                { text: 'Always refers to the global object', isCorrect: false },
                { text: 'Is used to declare variables', isCorrect: false },
                { text: 'Is a reserved keyword with no function', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the Event Loop in JavaScript?',
            explanation: 'The Event Loop is a mechanism that handles asynchronous operations in JavaScript. It continuously checks the call stack and task queue, moving tasks from the queue to the stack when the stack is empty. This enables non-blocking execution.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'A mechanism that handles asynchronous operations by managing call stack and task queue', isCorrect: true },
                { text: 'A way to create infinite loops', isCorrect: false },
                { text: 'A method to handle DOM events only', isCorrect: false },
                { text: 'A debugging tool in browser DevTools', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the difference between null and undefined?',
            explanation: 'undefined means a variable has been declared but not assigned a value, or a property doesn\'t exist. null is an intentional absence of value, explicitly set by the programmer. undefined == null is true, but undefined === null is false.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'undefined means not assigned, null is intentionally empty', isCorrect: true },
                { text: 'They are exactly the same thing', isCorrect: false },
                { text: 'null means not assigned, undefined is intentionally empty', isCorrect: false },
                { text: 'Both always evaluate to false', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What are Promises in JavaScript?',
            explanation: 'Promises represent the eventual completion or failure of an asynchronous operation. They have three states: pending, fulfilled (resolved), or rejected. Promises can be chained using .then(), .catch(), and .finally().',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Objects representing eventual completion/failure of async operations', isCorrect: true },
                { text: 'A way to make synchronous code', isCorrect: false },
                { text: 'Built-in error handling mechanism', isCorrect: false },
                { text: 'A method to declare variables', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the difference between arrow functions and regular functions?',
            explanation: 'Arrow functions have lexical "this" binding (inherit from enclosing scope), cannot be used as constructors, don\'t have their own arguments object, and are always anonymous. Regular functions have dynamic "this" binding, can be constructors, have arguments object, and can be named.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Arrow functions have lexical this binding, regular functions have dynamic this', isCorrect: true },
                { text: 'Arrow functions are faster to execute', isCorrect: false },
                { text: 'Regular functions cannot use parameters', isCorrect: false },
                { text: 'They are functionally identical', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is prototypal inheritance in JavaScript?',
            explanation: 'JavaScript uses prototypal inheritance where objects can inherit properties and methods from other objects via the prototype chain. Every object has a __proto__ property that points to its prototype. This enables code reuse and object extension.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Objects inherit from other objects via prototype chain', isCorrect: true },
                { text: 'A way to create private variables', isCorrect: false },
                { text: 'A method to handle async operations', isCorrect: false },
                { text: 'A technique for memory management', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is destructuring in JavaScript?',
            explanation: 'Destructuring is a syntax that allows extracting values from arrays or properties from objects into distinct variables. It provides a concise way to unpack values. Example: const [a, b] = array; const {x, y} = object.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'Syntax to extract values from arrays/objects into variables', isCorrect: true },
                { text: 'A way to delete object properties', isCorrect: false },
                { text: 'A method to combine multiple arrays', isCorrect: false },
                { text: 'A technique to compress code', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What are template literals in JavaScript?',
            explanation: 'Template literals are string literals allowing embedded expressions, multi-line strings, and string interpolation using backticks (`). They support expression interpolation with ${expression} syntax and tagged templates for advanced string processing.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'String literals with backticks allowing embedded expressions', isCorrect: true },
                { text: 'A way to create HTML templates', isCorrect: false },
                { text: 'Pre-built string functions', isCorrect: false },
                { text: 'A method to escape special characters', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is async/await in JavaScript?',
            explanation: 'async/await is syntactic sugar over Promises that makes asynchronous code look and behave more like synchronous code. async functions always return a Promise, and await pauses execution until the Promise resolves. This improves readability and error handling.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Syntactic sugar over Promises for cleaner async code', isCorrect: true },
                { text: 'A way to make code run faster', isCorrect: false },
                { text: 'Built-in error handling for sync functions', isCorrect: false },
                { text: 'A method to create parallel execution', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the difference between map(), filter(), and reduce()?',
            explanation: 'map() transforms each element and returns a new array of same length. filter() returns a new array with elements passing a test condition. reduce() accumulates array elements into a single value using an accumulator function. All are pure functions that don\'t mutate the original array.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'map transforms, filter selects, reduce accumulates to single value', isCorrect: true },
                { text: 'They all do the same thing with different syntax', isCorrect: false },
                { text: 'Only map() returns a new array', isCorrect: false },
                { text: 'reduce() is the fastest for all operations', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What are JavaScript modules (ES6)?',
            explanation: 'ES6 modules allow code organization into separate files with explicit imports/exports. They have their own scope, are statically analyzable, and support both named exports (export const x) and default exports (export default). Modules are automatically in strict mode.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'A way to organize code into separate files with imports/exports', isCorrect: true },
                { text: 'Functions that return objects', isCorrect: false },
                { text: 'Built-in Node.js libraries', isCorrect: false },
                { text: 'A method to create global variables', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the Temporal Dead Zone (TDZ)?',
            explanation: 'The Temporal Dead Zone is the time between entering a scope and the declaration being initialized for let/const variables. During TDZ, accessing the variable throws a ReferenceError. This prevents using variables before declaration, unlike var which gets hoisted with undefined.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Time between scope entry and let/const initialization', isCorrect: true },
                { text: 'A debugging mode in JavaScript engines', isCorrect: false },
                { text: 'Memory area for temporary variables', isCorrect: false },
                { text: 'Time limit for async operations', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What are WeakMap and WeakSet in JavaScript?',
            explanation: 'WeakMap and WeakSet are collections that hold weak references to their keys/values. Keys in WeakMap must be objects, and entries are garbage collected when keys become unreachable. They\'re not enumerable and don\'t prevent memory leaks. Useful for private data and metadata.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Collections with weak references that allow garbage collection', isCorrect: true },
                { text: 'Smaller versions of Map and Set with limited capacity', isCorrect: false },
                { text: 'Maps and Sets with automatic data compression', isCorrect: false },
                { text: 'Thread-safe versions of Map and Set', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is currying in JavaScript?',
            explanation: 'Currying is a functional programming technique that transforms a function with multiple parameters into a sequence of functions, each taking a single parameter. It enables partial application and function composition. Example: f(a,b,c) becomes f(a)(b)(c).',
            reference: 'https://javascript.info/currying-partials',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Transforming multi-parameter function into sequence of single-parameter functions', isCorrect: true },
                { text: 'A way to optimize function performance', isCorrect: false },
                { text: 'Method to handle function errors', isCorrect: false },
                { text: 'Technique to create recursive functions', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the difference between call(), apply(), and bind()?',
            explanation: 'call() invokes function immediately with specified this and arguments list. apply() invokes immediately with specified this and arguments array. bind() returns a new function with specified this and optionally pre-set arguments, without immediate invocation. All three methods control function context.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'call uses arg list, apply uses array, bind returns new function', isCorrect: true },
                { text: 'They are exactly the same with different names', isCorrect: false },
                { text: 'Only bind() can change the this context', isCorrect: false },
                { text: 'call() and apply() return new functions', isCorrect: false },
              ]),
            },
          },
          {
            text: 'What is the difference between synchronous and asynchronous JavaScript?',
            explanation: 'Synchronous code executes line by line, blocking further execution until current operation completes. Asynchronous code allows operations to run in background while other code continues executing, using callbacks, promises, or async/await. This prevents UI freezing and improves performance.',
            reference: 'https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Sync blocks execution, async allows background operations', isCorrect: true },
                { text: 'Sync is faster than async operations', isCorrect: false },
                { text: 'Async code always runs first', isCorrect: false },
                { text: 'They perform exactly the same way', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript generators?',
            explanation: 'Generators are functions that can be paused and resumed, yielding values one at a time. They use function* syntax and yield keyword. They return an iterator object with next() method. Useful for lazy evaluation, infinite sequences, and async iteration.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Functions that can be paused/resumed using yield keyword', isCorrect: true },
                { text: 'Functions that create random numbers', isCorrect: false },
                { text: 'Built-in array creation methods', isCorrect: false },
                { text: 'Functions that automatically call themselves', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Symbol primitive type in JavaScript?',
            explanation: 'Symbol is a primitive type that creates unique identifiers. Each Symbol() call returns a unique symbol, even with same description. Symbols are often used as object property keys to avoid naming collisions. Symbol.for() creates global symbols.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Primitive type that creates unique identifiers', isCorrect: true },
                { text: 'A way to create mathematical symbols', isCorrect: false },
                { text: 'Built-in emoji support in JavaScript', isCorrect: false },
                { text: 'A method to create string templates', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between shallow copy and deep copy?',
            explanation: 'Shallow copy copies only the first level properties. Nested objects/arrays are still referenced. Deep copy creates completely independent copy of all levels. Methods: Object.assign() (shallow), JSON.parse/stringify (deep but limited), structuredClone() (modern deep copy).',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Shallow copies first level only, deep copies all nested levels', isCorrect: true },
                { text: 'Shallow is faster but deep is more secure', isCorrect: false },
                { text: 'Deep copy only works with primitive types', isCorrect: false },
                { text: 'They produce identical results always', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript Proxies?',
            explanation: 'Proxies allow you to intercept and customize operations on objects (property access, assignment, enumeration, function calls). They use handlers (traps) to define custom behavior. Useful for validation, property access logging, virtual objects, and API wrappers.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Objects that intercept and customize operations on other objects', isCorrect: true },
                { text: 'Network intermediaries for API calls', isCorrect: false },
                { text: 'Built-in security mechanisms', isCorrect: false },
                { text: 'A way to create private variables', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is memoization in JavaScript?',
            explanation: 'Memoization is an optimization technique that stores function results based on input parameters. When the same inputs occur again, the cached result is returned instead of recalculating. Improves performance for expensive, pure functions with repeated calls.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/API/Performance',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Caching function results based on input parameters', isCorrect: true },
                { text: 'A way to remember variable names', isCorrect: false },
                { text: 'Built-in memory management system', isCorrect: false },
                { text: 'Method to store data in localStorage', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between forEach() and map()?',
            explanation: 'forEach() executes a function for each array element but returns undefined. Used for side effects like logging or DOM manipulation. map() creates and returns a new array with transformed elements. Use forEach for side effects, map for transformations.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'forEach returns undefined, map returns new array', isCorrect: true },
                { text: 'forEach is faster than map', isCorrect: false },
                { text: 'map can only work with numbers', isCorrect: false },
                { text: 'They are functionally identical', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript classes and how do they work?',
            explanation: 'ES6 classes are syntactic sugar over prototypal inheritance. They provide cleaner syntax for constructor functions and prototype methods. Support inheritance with extends, super() for parent constructor, static methods, and private fields (#field). Still prototype-based under the hood.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Syntactic sugar over prototypal inheritance with cleaner syntax', isCorrect: true },
                { text: 'True classical inheritance like Java/C#', isCorrect: false },
                { text: 'A way to create global variables', isCorrect: false },
                { text: 'Functions that return HTML elements', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is debouncing and throttling?',
            explanation: 'Debouncing delays function execution until after a quiet period (no more calls for X ms). Throttling limits function execution to once per time interval. Debouncing is good for search input, throttling for scroll/resize events. Both optimize performance by reducing function calls.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/API/Performance/',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Debouncing delays execution, throttling limits frequency', isCorrect: true },
                { text: 'Both prevent any function execution', isCorrect: false },
                { text: 'They only work with async functions', isCorrect: false },
                { text: 'Throttling delays, debouncing limits frequency', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between Object.freeze(), Object.seal(), and Object.preventExtensions()?',
            explanation: 'Object.freeze() prevents all modifications (add, delete, modify). Object.seal() allows modification of existing properties but prevents add/delete. Object.preventExtensions() only prevents adding new properties. Each has corresponding check methods (isFrozen, isSealed, isExtensible).',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'freeze prevents all changes, seal allows modifications, preventExtensions blocks additions', isCorrect: true },
                { text: 'They all do exactly the same thing', isCorrect: false },
                { text: 'Only freeze() actually works', isCorrect: false },
                { text: 'seal is the strongest protection', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript iterators and iterables?',
            explanation: 'Iterables are objects that implement Symbol.iterator method, returning an iterator. Iterators have next() method returning {value, done} objects. Arrays, strings, maps, sets are built-in iterables. for...of loops work with iterables. Custom iterables enable clean data traversal patterns.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Iterables implement Symbol.iterator, iterators have next() method', isCorrect: true },
                { text: 'Built-in loop optimization techniques', isCorrect: false },
                { text: 'Methods to create infinite arrays', isCorrect: false },
                { text: 'Functions that repeat automatically', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the rest parameter and spread operator?',
            explanation: 'Rest parameter (...args) collects multiple elements into an array, used in function parameters. Spread operator (...) expands arrays/objects into individual elements, used in function calls, array/object literals. Same syntax, different contexts and purposes.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'Rest collects elements into array, spread expands elements', isCorrect: true },
                { text: 'They are two names for the same feature', isCorrect: false },
                { text: 'Rest is for objects, spread is for arrays', isCorrect: false },
                { text: 'Spread creates arrays, rest creates objects', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is a JavaScript module bundler?',
            explanation: 'Module bundlers (webpack, Vite, Rollup) combine multiple JavaScript modules into optimized bundles for browsers. They resolve dependencies, transform code (transpiling, minification), handle assets, and enable code splitting. Essential for modern web development workflow.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Tools that combine multiple modules into optimized bundles', isCorrect: true },
                { text: 'Built-in browser feature for loading modules', isCorrect: false },
                { text: 'A way to compress JavaScript files', isCorrect: false },
                { text: 'Server-side module management system', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between function declaration and function expression?',
            explanation: 'Function declarations are hoisted completely and can be called before definition. Function expressions are not hoisted and create functions as values assigned to variables. Arrow functions are always expressions. Declarations create function-scoped names, expressions can be anonymous.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'Declarations are hoisted completely, expressions are not', isCorrect: true },
                { text: 'Expressions are faster to execute', isCorrect: false },
                { text: 'Declarations cannot have parameters', isCorrect: false },
                { text: 'They compile to identical bytecode', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript getters and setters?',
            explanation: 'Getters and setters are special methods that allow defining object properties that behave like normal properties but execute functions when accessed/modified. Use get/set keywords or Object.defineProperty(). Enable validation, computed properties, and encapsulation.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/getter',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Special methods that define property access/modification behavior', isCorrect: true },
                { text: 'Built-in functions to retrieve/store data', isCorrect: false },
                { text: 'Methods only available in classes', isCorrect: false },
                { text: 'A way to create private variables', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Observer Pattern in JavaScript?',
            explanation: 'Observer pattern defines one-to-many dependency between objects. When subject changes state, all observers are notified automatically. Common implementations include EventEmitter in Node.js, custom event systems, and reactive programming libraries. Promotes loose coupling.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Pattern where subjects notify multiple observers of state changes', isCorrect: true },
                { text: 'Built-in browser API for watching DOM changes', isCorrect: false },
                { text: 'A debugging technique for monitoring variables', isCorrect: false },
                { text: 'Method to create singleton objects', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is JSON and how do you work with it in JavaScript?',
            explanation: 'JSON (JavaScript Object Notation) is a text-based data interchange format. JavaScript provides JSON.parse() to convert JSON strings to objects and JSON.stringify() to convert objects to JSON strings. Supports strings, numbers, booleans, arrays, objects, and null. No functions, undefined, or symbols.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: 'Text format for data exchange, use JSON.parse() and JSON.stringify()', isCorrect: true },
                { text: 'Built-in JavaScript database system', isCorrect: false },
                { text: 'A way to create object constructors', isCorrect: false },
                { text: 'Network protocol for API communication', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript regular expressions?',
            explanation: 'Regular expressions (RegExp) are patterns used to match character combinations in strings. Created with /pattern/flags or new RegExp(). Common methods: test(), exec(), match(), replace(), search(). Flags include g (global), i (case-insensitive), m (multiline). Essential for string validation and parsing.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Patterns for matching character combinations in strings', isCorrect: true },
                { text: 'Built-in functions for mathematical calculations', isCorrect: false },
                { text: 'A way to create reusable code blocks', isCorrect: false },
                { text: 'Methods for handling asynchronous operations', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between localStorage, sessionStorage, and cookies?',
            explanation: 'localStorage persists until explicitly cleared, has ~5-10MB limit, client-side only. sessionStorage lasts for session/tab, same size limit. Cookies are smaller (~4KB), sent with HTTP requests, have expiration dates, can be server or client-side. Each serves different storage needs.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'localStorage persists, sessionStorage per session, cookies sent with requests', isCorrect: true },
                { text: 'They all store data exactly the same way', isCorrect: false },
                { text: 'Cookies are the largest and most secure', isCorrect: false },
                { text: 'localStorage is sent with every HTTP request', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is functional programming in JavaScript?',
            explanation: 'Functional programming treats computation as evaluation of mathematical functions, avoiding state mutation and side effects. Key concepts: pure functions, immutability, higher-order functions, function composition, currying. JavaScript supports FP with map/filter/reduce, closures, and first-class functions.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Programming paradigm using pure functions and avoiding mutations', isCorrect: true },
                { text: 'Writing functions that only return other functions', isCorrect: false },
                { text: 'A way to optimize JavaScript performance', isCorrect: false },
                { text: 'Programming style that only uses built-in methods', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript Web APIs?',
            explanation: 'Web APIs are browser-provided interfaces for interacting with browser features and services. Examples: DOM API, Fetch API, Geolocation API, Web Storage API, Canvas API, Web Workers. They extend JavaScript capabilities beyond the core language specification.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Browser-provided interfaces for accessing browser features', isCorrect: true },
                { text: 'Server-side JavaScript frameworks', isCorrect: false },
                { text: 'Built-in JavaScript optimization tools', isCorrect: false },
                { text: 'Methods for creating responsive designs', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between == (loose equality) and === (strict equality)?',
            explanation: 'Loose equality (==) performs type coercion before comparison, converting operands to same type. Strict equality (===) compares both value and type without coercion. Examples: "5" == 5 is true, "5" === 5 is false. Always prefer === for predictable comparisons.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array',
            points: 1,
            answers: {
              create: shuffleAnswers([
                { text: '== performs type coercion, === compares value and type', isCorrect: true },
                { text: '=== is slower than == operator', isCorrect: false },
                { text: 'They produce identical results always', isCorrect: false },
                { text: '== only works with numbers', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript promises chaining and error handling?',
            explanation: 'Promise chaining allows sequential async operations using .then(). Each .then() returns a new promise. Errors propagate down the chain until caught by .catch(). .finally() runs regardless of resolution. async/await provides cleaner syntax for the same concepts.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Sequential async operations with .then(), errors caught by .catch()', isCorrect: true },
                { text: 'A way to create infinite loops with promises', isCorrect: false },
                { text: 'Method to run promises in parallel only', isCorrect: false },
                { text: 'Built-in error logging mechanism', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is event bubbling and capturing in JavaScript?',
            explanation: 'Event bubbling: events trigger from target element up to root. Event capturing: events trigger from root down to target. Event propagation has 3 phases: capturing, target, bubbling. stopPropagation() stops further propagation. addEventListener() third parameter controls capture phase.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Event',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Bubbling goes up from target, capturing goes down to target', isCorrect: true },
                { text: 'Both terms describe the same event behavior', isCorrect: false },
                { text: 'Bubbling prevents events, capturing enables them', isCorrect: false },
                { text: 'They only apply to mouse events', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Module Pattern in JavaScript?',
            explanation: 'Module Pattern uses closures to create private scope and expose public API. Classic implementation uses IIFE (Immediately Invoked Function Expression) returning object with public methods. Provides encapsulation and namespace management. Modern ES6 modules replaced this pattern.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Pattern using closures to create private scope with public API', isCorrect: true },
                { text: 'Built-in JavaScript feature for importing files', isCorrect: false },
                { text: 'A way to create reusable HTML templates', isCorrect: false },
                { text: 'Method for optimizing code performance', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript typed arrays?',
            explanation: 'Typed arrays provide a way to work with binary data in JavaScript. Types include Int8Array, Uint8Array, Float32Array, etc. They offer better performance for numerical computations and are used with WebGL, Canvas, File API. Based on ArrayBuffer for raw binary data.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/API/Performance',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Arrays for working with binary data with specific numeric types', isCorrect: true },
                { text: 'Arrays that can only store one data type', isCorrect: false },
                { text: 'Built-in array validation mechanisms', isCorrect: false },
                { text: 'A way to create strongly-typed JavaScript', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between synchronous and asynchronous iteration?',
            explanation: 'Synchronous iteration uses for...of with regular iterables, blocking until each value is available. Asynchronous iteration uses for await...of with async iterables, allowing await within iteration. Async iterables implement Symbol.asyncIterator. Useful for streams and async data sources.',
            reference: 'https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Sync blocks until values ready, async allows await within iteration', isCorrect: true },
                { text: 'Async iteration is always faster', isCorrect: false },
                { text: 'They can be used interchangeably', isCorrect: false },
                { text: 'Only sync iteration works with arrays', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript BigInt and when would you use it?',
            explanation: 'BigInt represents integers larger than Number.MAX_SAFE_INTEGER (2^53 - 1). Created with BigInt() function or n suffix (123n). Cannot mix with regular numbers in operations. Useful for cryptography, precise calculations, working with large datasets or IDs.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Type for integers larger than MAX_SAFE_INTEGER', isCorrect: true },
                { text: 'Built-in big data processing library', isCorrect: false },
                { text: 'A way to create very long strings', isCorrect: false },
                { text: 'Method for handling floating-point precision', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Singleton Pattern in JavaScript?',
            explanation: 'Singleton Pattern ensures a class has only one instance and provides global access point. Implementation can use closures, modules, or classes with static instance property. Common uses: database connections, logging, configuration objects. Can make testing difficult due to global state.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Pattern ensuring only one instance of a class exists', isCorrect: true },
                { text: 'A way to create arrays with one element', isCorrect: false },
                { text: 'Method for handling single-threaded operations', isCorrect: false },
                { text: 'Built-in JavaScript optimization technique', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is tail call optimization in JavaScript?',
            explanation: 'Tail call optimization (TCO) is when the last operation in a function is a call to another function. The current stack frame can be replaced instead of adding new one, preventing stack overflow in recursive functions. ES6 spec includes TCO but browser support is limited.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Optimization replacing stack frames for recursive tail calls', isCorrect: true },
                { text: 'Built-in function performance monitoring', isCorrect: false },
                { text: 'A way to automatically minimize function calls', isCorrect: false },
                { text: 'Method for handling function parameters', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript decorators?',
            explanation: 'Decorators are a stage 3 proposal for extending classes and class members with additional functionality. They use @ syntax and are functions that modify classes, methods, or properties. Popular in frameworks like Angular. Similar to annotations in other languages.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Proposed feature for extending classes with @ syntax', isCorrect: true },
                { text: 'Built-in functions for code beautification', isCorrect: false },
                { text: 'A way to add comments to functions', isCorrect: false },
                { text: 'Methods for creating design patterns', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between microtasks and macrotasks?',
            explanation: 'Microtasks (Promise callbacks, queueMicrotask) have higher priority and execute before macrotasks (setTimeout, setInterval, I/O). Event loop processes all microtasks before moving to next macrotask. This ensures Promise resolution happens before timers. Understanding this is crucial for async behavior.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Microtasks have higher priority and execute before macrotasks', isCorrect: true },
                { text: 'Macrotasks always execute first', isCorrect: false },
                { text: 'They are processed simultaneously', isCorrect: false },
                { text: 'The difference only matters in Node.js', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript template tagged functions?',
            explanation: 'Tagged templates allow you to parse template literals with a function. The tag function receives an array of string pieces and values as arguments. Enables custom processing like escaping, internationalization, or DSLs. Example: styled`color: ${color};` in styled-components.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Functions that process template literals with custom logic', isCorrect: true },
                { text: 'Built-in functions for HTML template creation', isCorrect: false },
                { text: 'A way to create reusable string patterns', isCorrect: false },
                { text: 'Methods for template performance optimization', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Revealing Module Pattern?',
            explanation: 'Revealing Module Pattern is a variation of Module Pattern where all methods are defined privately and selectively exposed in return statement. Provides cleaner syntax and makes it clear what\'s public vs private. Uses IIFE and returns object literal mapping public names to private functions.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Module pattern variation that clearly reveals public interface', isCorrect: true },
                { text: 'A debugging technique for module inspection', isCorrect: false },
                { text: 'Built-in JavaScript feature for code organization', isCorrect: false },
                { text: 'Method for exposing private variables globally', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript ArrayBuffer and DataView?',
            explanation: 'ArrayBuffer represents raw binary data buffer. DataView provides a low-level interface for reading/writing multiple number types in ArrayBuffer at specified byte offsets. Useful for binary protocols, file formats, and WebAssembly interfacing. TypedArrays are higher-level views of ArrayBuffers.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/ArrayBuffer',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'ArrayBuffer is raw binary data, DataView provides read/write interface', isCorrect: true },
                { text: 'Built-in database storage mechanisms', isCorrect: false },
                { text: 'Methods for optimizing array performance', isCorrect: false },
                { text: 'A way to create multidimensional arrays', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Factory Pattern in JavaScript?',
            explanation: 'Factory Pattern creates objects without specifying exact classes. A factory function returns new objects based on parameters. Provides abstraction over object creation, enabling polymorphism and reducing coupling. Common in JavaScript due to its flexible object creation mechanisms.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Pattern for creating objects without specifying exact classes', isCorrect: true },
                { text: 'Built-in JavaScript object creation optimization', isCorrect: false },
                { text: 'A way to create manufacturing simulation software', isCorrect: false },
                { text: 'Method for mass-producing identical functions', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript service workers?',
            explanation: 'Service Workers are scripts that run in background, separate from web pages, enabling features like push notifications, background sync, and offline functionality. They act as proxy between app and network, can intercept requests, cache resources. Essential for Progressive Web Apps (PWAs).',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Background scripts enabling offline functionality and PWA features', isCorrect: true },
                { text: 'Server-side JavaScript execution environment', isCorrect: false },
                { text: 'Built-in browser optimization workers', isCorrect: false },
                { text: 'A way to create multi-threaded JavaScript', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the difference between imperative and declarative programming?',
            explanation: 'Imperative programming describes HOW to do something step-by-step (for loops, if statements). Declarative programming describes WHAT you want (map, filter, SQL). JavaScript supports both paradigms. Functional programming tends to be declarative, while procedural is imperative.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Imperative describes HOW, declarative describes WHAT', isCorrect: true },
                { text: 'Imperative is always faster than declarative', isCorrect: false },
                { text: 'JavaScript only supports imperative style', isCorrect: false },
                { text: 'They produce different results for same logic', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript web workers?',
            explanation: 'Web Workers run JavaScript in background threads, separate from main UI thread. They enable parallel processing without blocking user interface. Cannot directly access DOM but can communicate via message passing. Types include dedicated workers, shared workers, and service workers.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/API/Worker',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Background threads for JavaScript parallel processing', isCorrect: true },
                { text: 'Built-in browser debugging tools', isCorrect: false },
                { text: 'Server-side JavaScript execution environment', isCorrect: false },
                { text: 'A way to optimize DOM manipulation', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Command Pattern in JavaScript?',
            explanation: 'Command Pattern encapsulates requests as objects, allowing parameterization of clients with different requests, queuing operations, and supporting undo functionality. Commands have execute() and optional undo() methods. Useful for implementing macro recording, undo/redo systems, and queuing systems.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function',
            points: 3,
            answers: {
              create: shuffleAnswers([
                { text: 'Pattern encapsulating requests as objects with execute/undo methods', isCorrect: true },
                { text: 'Built-in JavaScript command line interface', isCorrect: false },
                { text: 'A way to create terminal applications', isCorrect: false },
                { text: 'Method for handling user input events', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript mixins?',
            explanation: 'Mixins are a way to achieve multiple inheritance by copying properties from one object to another. JavaScript doesn\'t have built-in multiple inheritance, so mixins provide a composition-based approach. Can be implemented with Object.assign() or custom mixing functions. Promotes code reuse.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Way to achieve multiple inheritance through property copying', isCorrect: true },
                { text: 'Built-in JavaScript inheritance mechanism', isCorrect: false },
                { text: 'A method for combining array elements', isCorrect: false },
                { text: 'Functions that mix different data types', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What is the Adapter Pattern in JavaScript?',
            explanation: 'Adapter Pattern allows incompatible interfaces to work together by wrapping existing interface with a new one. Acts as bridge between different APIs or data formats. Common when integrating third-party libraries or legacy code. Example: adapting different API response formats to unified interface.',
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy',
            points: 2,
            answers: {
              create: shuffleAnswers([
                { text: 'Pattern making incompatible interfaces work together', isCorrect: true },
                { text: 'Built-in JavaScript type conversion system', isCorrect: false },
                { text: 'A way to optimize code performance', isCorrect: false },
                { text: 'Method for creating responsive web designs', isCorrect: false },
                            ]),
            },
          },
          {
            text: 'What are JavaScript private fields and methods?',
            explanation: 'Private fields (#field) and methods (#method) are ES2022 features providing true encapsulation in classes. Only accessible within the class where defined. Unlike naming conventions (_private), these are enforced by the language. Enable proper information hiding and prevent accidental access. Reference: MDN Web Docs - Private class features',
            points: 2,
            reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_class_fields',
            answers: {
              create: shuffleAnswers([
                { text: 'ES2022 features using # syntax for true encapsulation in classes', isCorrect: true },
                { text: 'Old JavaScript convention using underscore prefix', isCorrect: false },
                { text: 'A way to hide functions from global scope', isCorrect: false },
                { text: 'Built-in security mechanism for all objects', isCorrect: false },
              ]),
            },
          }
        ],
      },
    },
  })

  return javascript
}
