"""JavaScript Associate Certification"""

CERTIFICATION = {
    "name": "JavaScript Associate",
    "description": "JavaScript Certified Associate Developer",
    "slug": "javascript-associate",
    "level": "Associate",
    "duration": 65,
    "questions_count": 40,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": """## Code Analysis Question

**What is the output of the following code?**

```javascript
class Person {
    constructor(name) {
        this.name = name;
    }
}

let person = new Person("Alice");
console.log(person.name);
```

*Choose the correct output:*""",
        "explanation": """# Object-Oriented Programming - Classes and Objects

> **Key Concept**: Classes are templates for creating objects. The constructor method initializes new instances.

## Code Breakdown:

1. **Class Definition**: `class Person` defines a new class
2. **Constructor Method**: `constructor(name)` is called when creating instances
3. **Instance Property**: `this.name = name` sets an instance property
4. **Object Creation**: `new Person("Alice")` creates a new instance
5. **Property Access**: `person.name` accesses the instance property

## Example Output:
```javascript
class Person {
    constructor(name) {
        this.name = name;
    }
}

let person = new Person("Alice");
console.log(person.name);  // Output: Alice
```

### 📝 **Important Notes:**
- The constructor method initializes instance properties when an object is created
- Instance properties belong to specific object instances
- The `this` keyword refers to the current instance

### 🔗 **Related Concepts:**
- Class vs instance properties
- Object instantiation
- Constructor methods""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes",
        "points": 1,
        "answers": [
            {"text": "**Alice**", "is_correct": True},
            {"text": "**undefined**", "is_correct": False},
            {"text": "**Error**", "is_correct": False},
            {"text": "**Person**", "is_correct": False},
        ],
    },
    {
        "text": "What is a closure in JavaScript?",
        "explanation": """# Closures in JavaScript

A closure is a function that has access to variables in its outer (enclosing) scope even after the outer function has returned.

## Example:
```javascript
function outerFunction(x) {
    return function innerFunction(y) {
        return x + y;  // Access to outer variable 'x'
    };
}

const addFive = outerFunction(5);
console.log(addFive(3)); // 8 - 'x' is still accessible
```

Closures are fundamental for data privacy, callbacks, and functional programming patterns.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures",
        "points": 1,
        "answers": [
            {"text": "A function with access to outer scope variables", "is_correct": True},
            {"text": "A way to close functions", "is_correct": False},
            {"text": "A method to hide code", "is_correct": False},
            {"text": "A type of loop", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between 'let', 'const', and 'var'?",
        "explanation": """# Variable Declarations in JavaScript

Different keywords have different scoping rules and behaviors.

## Example:
```javascript
// var - function scoped, hoisted
var x = 1;
if (true) {
    var x = 2;  // Same variable
}
console.log(x); // 2

// let - block scoped
let y = 1;
if (true) {
    let y = 2;  // Different variable
}
console.log(y); // 1

// const - block scoped, immutable binding
const z = 1;
// z = 2;  // Error: Assignment to constant variable
```

Use `const` by default, `let` when reassignment needed, avoid `var`.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let",
        "points": 1,
        "answers": [
            {"text": "let and const are block scoped, var is function scoped", "is_correct": True},
            {"text": "No difference", "is_correct": False},
            {"text": "var is block scoped", "is_correct": False},
            {"text": "const can be reassigned", "is_correct": False},
        ],
    },
    {
        "text": "What does 'this' keyword refer to in JavaScript?",
        "explanation": """# 'this' Keyword in JavaScript

The value of 'this' depends on how a function is called, not where it's defined.

## Example:
```javascript
const obj = {
    name: "Alice",
    greet: function() {
        console.log("Hello, " + this.name);
    },
    arrowGreet: () => {
        console.log("Hello, " + this.name); // 'this' is undefined/global
    }
};

obj.greet();      // "Hello, Alice"
obj.arrowGreet(); // "Hello, undefined"

// Call method
const standalone = obj.greet;
standalone.call({name: "Bob"}); // "Hello, Bob"
```

Arrow functions don't have their own 'this' - they inherit from enclosing scope.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this",
        "points": 1,
        "answers": [
            {"text": "The context in which a function is called", "is_correct": True},
            {"text": "The current file", "is_correct": False},
            {"text": "The global object always", "is_correct": False},
            {"text": "The function itself", "is_correct": False},
        ],
    },
    {
        "text": "What is event bubbling in JavaScript?",
        "explanation": """# Event Bubbling

Event bubbling is when an event starts from the target element and bubbles up to parent elements.

## Example:
```javascript
// HTML: <div id="parent"><button id="child">Click</button></div>

document.getElementById('parent').addEventListener('click', () => {
    console.log('Parent clicked');
});

document.getElementById('child').addEventListener('click', (e) => {
    console.log('Child clicked');
    // e.stopPropagation(); // Prevents bubbling
});

// Clicking button logs: "Child clicked", then "Parent clicked"
```

Use `stopPropagation()` to prevent bubbling when needed.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_bubbling_and_capture",
        "points": 1,
        "answers": [
            {"text": "Events propagate from target to parent elements", "is_correct": True},
            {"text": "Events only fire on target element", "is_correct": False},
            {"text": "Events fire randomly", "is_correct": False},
            {"text": "Events propagate from parent to child", "is_correct": False},
        ],
    },
    {
        "text": """## Promise Chain Question

**What is the output of the following code?**

```javascript
Promise.resolve(5)
    .then(x => x * 2)
    .then(x => x + 1)
    .then(console.log);
```

*Choose the correct result:*""",
        "explanation": """# Promise Chaining

Promises allow chaining asynchronous operations where each `.then()` receives the result of the previous one.

## Example:
```javascript
Promise.resolve(5)      // Start with value 5
    .then(x => x * 2)   // 5 * 2 = 10
    .then(x => x + 1)   // 10 + 1 = 11
    .then(console.log); // Logs: 11

// Equivalent to:
async function example() {
    let result = 5;
    result = result * 2;  // 10
    result = result + 1;  // 11
    console.log(result);  // 11
}
```

Each `.then()` returns a new Promise with the transformed value.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/then",
        "points": 1,
        "answers": [
            {"text": "11", "is_correct": True},
            {"text": "5", "is_correct": False},
            {"text": "10", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is destructuring in JavaScript?",
        "explanation": """# Destructuring Assignment

Destructuring allows extracting values from arrays or properties from objects into distinct variables.

## Example:
```javascript
// Array destructuring
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first);  // 1
console.log(second); // 2
console.log(rest);   // [3, 4, 5]

// Object destructuring
const {name, age, city = "Unknown"} = {name: "Alice", age: 25};
console.log(name);   // "Alice"
console.log(city);   // "Unknown" (default value)

// Function parameters
function greet({name, age}) {
    console.log(`Hello ${name}, you are ${age}`);
}
```

Great for cleaner code when working with complex data structures.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment",
        "points": 1,
        "answers": [
            {"text": "Extracting values from arrays/objects into variables", "is_correct": True},
            {"text": "Deleting properties from objects", "is_correct": False},
            {"text": "Creating new objects", "is_correct": False},
            {"text": "Combining arrays", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between map() and forEach()?",
        "explanation": """# map() vs forEach()

`map()` transforms each element and returns a new array, `forEach()` executes a function for each element but returns undefined.

## Example:
```javascript
const numbers = [1, 2, 3, 4, 5];

// map() - returns new array
const doubled = numbers.map(x => x * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]
console.log(numbers);  // [1, 2, 3, 4, 5] (unchanged)

// forEach() - returns undefined
const result = numbers.forEach(x => console.log(x * 2));
console.log(result);   // undefined

// Use map() for transformations, forEach() for side effects
```

Choose `map()` when you need a transformed array, `forEach()` for side effects only.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map",
        "points": 1,
        "answers": [
            {"text": "map() returns new array, forEach() returns undefined", "is_correct": True},
            {"text": "No difference", "is_correct": False},
            {"text": "forEach() returns new array", "is_correct": False},
            {"text": "map() is slower than forEach()", "is_correct": False},
        ],
    },
    {
        "text": "What is the spread operator (...) used for?",
        "explanation": """# Spread Operator (...)

The spread operator expands iterables (arrays, strings, objects) into individual elements.

## Example:
```javascript
// Array spreading
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// Object spreading
const obj1 = {a: 1, b: 2};
const obj2 = {c: 3, d: 4};
const merged = {...obj1, ...obj2};    // {a: 1, b: 2, c: 3, d: 4}

// Function arguments
function sum(a, b, c) {
    return a + b + c;
}
const numbers = [1, 2, 3];
console.log(sum(...numbers));  // 6
```

Useful for copying, combining, and passing arrays as function arguments.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax",
        "points": 1,
        "answers": [
            {"text": "Expands iterables into individual elements", "is_correct": True},
            {"text": "Creates new variables", "is_correct": False},
            {"text": "Deletes array elements", "is_correct": False},
            {"text": "Loops through arrays", "is_correct": False},
        ],
    },
    {
        "text": "What is async/await in JavaScript?",
        "explanation": """# Async/Await

Async/await provides a more readable way to work with Promises, making asynchronous code look synchronous.

## Example:
```javascript
// Promise-based approach
function fetchUserData(id) {
    return fetch(`/users/${id}`)
        .then(response => response.json())
        .then(user => {
            return fetch(`/posts/${user.id}`);
        })
        .then(response => response.json());
}

// Async/await approach
async function fetchUserData(id) {
    try {
        const userResponse = await fetch(`/users/${id}`);
        const user = await userResponse.json();
        const postsResponse = await fetch(`/posts/${user.id}`);
        const posts = await postsResponse.json();
        return posts;
    } catch (error) {
        console.error('Error:', error);
    }
}
```

Async functions always return a Promise. Use try/catch for error handling.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function",
        "points": 1,
        "answers": [
            {"text": "Syntactic sugar for working with Promises", "is_correct": True},
            {"text": "A new data type", "is_correct": False},
            {"text": "A way to create functions", "is_correct": False},
            {"text": "A loop construct", "is_correct": False},
        ],
    },
    {
        "text": """## Scope Question

**What is the output of the following code?**

```javascript
let x = 1;
function outer() {
    let x = 2;
    function inner() {
        console.log(x);
    }
    return inner;
}
const fn = outer();
fn();
```

*Choose the correct output:*""",
        "explanation": """# Lexical Scoping and Closures

Functions have access to variables in their lexical scope - where they were defined, not where they're called.

## Example:
```javascript
let x = 1;          // Global scope
function outer() {
    let x = 2;      // outer function scope
    function inner() {
        console.log(x); // Accesses x from outer scope (2)
    }
    return inner;
}
const fn = outer();
fn();               // Output: 2

// Inner function "closes over" the outer function's variable
```

This demonstrates lexical scoping - inner functions have access to outer function variables.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures#lexical_scoping",
        "points": 1,
        "answers": [
            {"text": "2", "is_correct": True},
            {"text": "1", "is_correct": False},
            {"text": "undefined", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between call(), apply(), and bind()?",
        "explanation": """# Function Context Methods

These methods control what 'this' refers to when calling a function.

## Example:
```javascript
const person = {
    name: "Alice",
    greet: function(greeting, punctuation) {
        return greeting + " " + this.name + punctuation;
    }
};

const anotherPerson = {name: "Bob"};

// call() - arguments individually
console.log(person.greet.call(anotherPerson, "Hello", "!"));
// "Hello Bob!"

// apply() - arguments as array
console.log(person.greet.apply(anotherPerson, ["Hi", "."]));
// "Hi Bob."

// bind() - returns new function with bound context
const boundGreet = person.greet.bind(anotherPerson);
console.log(boundGreet("Hey", "?"));
// "Hey Bob?"
```

Use call/apply for immediate invocation, bind for creating reusable functions.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call",
        "points": 1,
        "answers": [
            {"text": "call/apply invoke immediately, bind returns new function", "is_correct": True},
            {"text": "No difference", "is_correct": False},
            {"text": "They work only with objects", "is_correct": False},
            {"text": "bind invokes immediately", "is_correct": False},
        ],
    },
    {
        "text": "What is the prototype chain in JavaScript?",
        "explanation": """# Prototype Chain

JavaScript objects have a prototype property that creates inheritance relationships.

## Example:
```javascript
// Constructor function
function Animal(name) {
    this.name = name;
}

Animal.prototype.speak = function() {
    return `${this.name} makes a sound`;
};

function Dog(name, breed) {
    Animal.call(this, name);  // Call parent constructor
    this.breed = breed;
}

// Set up inheritance
Dog.prototype = Object.create(Animal.prototype);
Dog.prototype.constructor = Dog;

Dog.prototype.bark = function() {
    return `${this.name} barks`;
};

const dog = new Dog("Rex", "Labrador");
console.log(dog.speak()); // "Rex makes a sound" (inherited)
console.log(dog.bark());  // "Rex barks" (own method)
```

Objects inherit properties and methods from their prototype chain.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain",
        "points": 1,
        "answers": [
            {"text": "Mechanism for inheritance in JavaScript", "is_correct": True},
            {"text": "A type of loop", "is_correct": False},
            {"text": "A data structure", "is_correct": False},
            {"text": "A string method", "is_correct": False},
        ],
    },
    {
        "text": "What is event delegation?",
        "explanation": """# Event Delegation

Event delegation uses event bubbling to handle events on parent elements instead of individual child elements.

## Example:
```javascript
// Instead of adding listeners to each button
document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('click', handleClick);  // Multiple listeners
});

// Use delegation on parent container
document.getElementById('container').addEventListener('click', (e) => {
    if (e.target.matches('.button')) {
        handleClick(e);  // Single listener handles all buttons
    }
});

function handleClick(e) {
    console.log('Button clicked:', e.target.textContent);
}

// Benefits: Better performance, works for dynamically added elements
```

Useful for dynamic content and better performance with many elements.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_delegation",
        "points": 1,
        "answers": [
            {"text": "Using parent elements to handle child events", "is_correct": True},
            {"text": "Creating new events", "is_correct": False},
            {"text": "Removing event listeners", "is_correct": False},
            {"text": "Preventing default behavior", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between null and undefined?",
        "explanation": """# null vs undefined

Both represent absence of value but have different meanings and use cases.

## Example:
```javascript
let a;              // undefined (declared but not assigned)
let b = undefined;  // explicitly set to undefined
let c = null;       // explicitly set to null (intentional absence)

console.log(a);     // undefined
console.log(b);     // undefined  
console.log(c);     // null

// Type checking
console.log(typeof a);     // "undefined"
console.log(typeof c);     // "object" (quirk of JavaScript)

// Equality
console.log(a == c);       // true (loose equality)
console.log(a === c);      // false (strict equality)

// Object properties
const obj = {name: "Alice"};
console.log(obj.age);      // undefined (property doesn't exist)
obj.city = null;           // explicitly set to null
```

Use `null` for intentional absence, `undefined` typically means uninitialized.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null",
        "points": 1,
        "answers": [
            {"text": "null is intentional absence, undefined is uninitialized", "is_correct": True},
            {"text": "No difference", "is_correct": False},
            {"text": "undefined is intentional absence", "is_correct": False},
            {"text": "null is uninitialized", "is_correct": False},
        ],
    },
    {
        "text": "What is a higher-order function?",
        "explanation": """# Higher-Order Functions

A higher-order function either takes functions as parameters or returns a function.

## Example:
```javascript
// Function that takes another function as parameter
function processArray(arr, callback) {
    const result = [];
    for (let item of arr) {
        result.push(callback(item));
    }
    return result;
}

const numbers = [1, 2, 3, 4, 5];
const doubled = processArray(numbers, x => x * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]

// Function that returns another function
function createMultiplier(factor) {
    return function(number) {
        return number * factor;
    };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);
console.log(double(5));   // 10
console.log(triple(5));   // 15

// Built-in higher-order functions
[1, 2, 3].map(x => x * 2);      // map takes a function
[1, 2, 3].filter(x => x > 1);   // filter takes a function
```

Common in functional programming for creating reusable, composable code.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Glossary/First-class_Function",
        "points": 1,
        "answers": [
            {"text": "Function that takes or returns other functions", "is_correct": True},
            {"text": "Function with high complexity", "is_correct": False},
            {"text": "Function that runs last", "is_correct": False},
            {"text": "Function with many parameters", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between synchronous and asynchronous code?",
        "explanation": """# Synchronous vs Asynchronous Code

Synchronous code runs line by line, blocking subsequent code. Asynchronous code doesn't block execution.

## Example:
```javascript
// Synchronous code - blocks execution
console.log("Start");
for (let i = 0; i < 1000000000; i++) {
    // Long running operation blocks everything
}
console.log("End");  // Won't run until loop finishes

// Asynchronous code - doesn't block
console.log("Start");
setTimeout(() => {
    console.log("Timeout callback");  // Runs later
}, 1000);
console.log("End");  // Runs immediately

// Output: "Start", "End", then "Timeout callback" after 1 second

// Promises for async operations
fetch('/api/data')
    .then(response => response.json())
    .then(data => console.log(data));  // Non-blocking

// Async/await syntax
async function fetchData() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
```

JavaScript is single-threaded but uses event loop for asynchronous operations.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Asynchronous/Concepts",
        "points": 1,
        "answers": [
            {"text": "Sync blocks execution, async doesn't block", "is_correct": True},
            {"text": "Async blocks execution", "is_correct": False},
            {"text": "No difference", "is_correct": False},
            {"text": "Sync is faster than async", "is_correct": False},
        ],
    },
    {
        "text": "What is object destructuring with default values?",
        "explanation": """# Object Destructuring with Defaults

You can provide default values when destructuring objects in case properties don't exist.

## Example:
```javascript
const user = {
    name: "Alice",
    age: 25
    // no email property
};

// Basic destructuring
const {name, age, email} = user;
console.log(email);  // undefined

// With default values
const {
    name: userName = "Anonymous",
    age: userAge = 0,
    email: userEmail = "no-email@example.com",
    city = "Unknown"
} = user;

console.log(userName);   // "Alice" (from object)
console.log(userAge);    // 25 (from object)
console.log(userEmail);  // "no-email@example.com" (default)
console.log(city);       // "Unknown" (default)

// Function parameters with destructuring defaults
function createProfile({
    name = "Anonymous",
    age = 0,
    role = "user"
} = {}) {
    return {name, age, role};
}

console.log(createProfile());  // Uses all defaults
console.log(createProfile({name: "Bob"}));  // Partial override
```

Useful for handling optional configuration objects and API responses.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#default_values",
        "points": 1,
        "answers": [
            {"text": "Provides fallback values when properties don't exist", "is_correct": True},
            {"text": "Always overwrites existing properties", "is_correct": False},
            {"text": "Only works with arrays", "is_correct": False},
            {"text": "Creates new objects", "is_correct": False},
        ],
    },
    {
        "text": "What is the module system in JavaScript?",
        "explanation": """# JavaScript Modules (ES6+)

Modules allow splitting code into reusable pieces with explicit imports and exports.

## Example:
```javascript
// math.js - Module with exports
export function add(a, b) {
    return a + b;
}

export function multiply(a, b) {
    return a * b;
}

export const PI = 3.14159;

// Default export
export default function subtract(a, b) {
    return a - b;
}

// main.js - Module with imports
import subtract, {add, multiply, PI} from './math.js';

console.log(add(5, 3));        // 8
console.log(multiply(4, 2));   // 8
console.log(PI);               // 3.14159
console.log(subtract(10, 4));  // 6

// Import everything
import * as math from './math.js';
console.log(math.add(2, 3));   // 5

// Dynamic imports
async function loadMath() {
    const math = await import('./math.js');
    return math.add(1, 2);
}
```

Modules provide encapsulation, reusability, and better dependency management.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules",
        "points": 1,
        "answers": [
            {"text": "Way to organize and share code between files", "is_correct": True},
            {"text": "A type of function", "is_correct": False},
            {"text": "A data structure", "is_correct": False},
            {"text": "A loop construct", "is_correct": False},
        ],
    },
]