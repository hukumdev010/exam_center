"""JavaScript ES6+ Modern Features Certification"""

CERTIFICATION = {
    "name": "JavaScript ES6+ Modern Features",
    "description": "Modern JavaScript ES6+ features and advanced concepts",
    "slug": "javascript-es6-modern",
    "level": "Intermediate",
    "duration": 60,
    "questions_count": 30,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the difference between '==' and '===' operators in JavaScript?",
        "explanation": """# Equality Operators in JavaScript

The '==' (loose equality) performs type coercion before comparison, while '===' (strict equality) compares both value and type without coercion.

## Examples:
```javascript
// Loose equality (==) with type coercion
console.log(5 == "5");     // true (string converted to number)
console.log(true == 1);    // true (true converted to 1)
console.log(false == 0);   // true (false converted to 0)
console.log("" == 0);      // true (empty string converted to 0)

// Strict equality (===) without coercion
console.log(5 === "5");    // false (different types)
console.log(true === 1);   // false (different types)
console.log(false === 0);  // false (different types)
console.log("" === 0);     // false (different types)
```

Always prefer '===' for predictable comparisons.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "'===' is stricter and doesn't perform type coercion", "is_correct": True},
            {"text": "'==' is stricter", "is_correct": False},
            {"text": "They work only with numbers", "is_correct": False},
        ],
    },
    {
        "text": "What are template literals in ES6?",
        "explanation": """# Template Literals (ES6)

Template literals use backticks (`) and allow embedded expressions with ${}.

## Features:
- String interpolation
- Multi-line strings
- Tagged templates

## Examples:
```javascript
// Basic template literal
const name = "Alice";
const age = 25;
const message = `Hello, my name is ${name} and I am ${age} years old.`;

// Multi-line strings
const html = `
    <div>
        <h1>${name}</h1>
        <p>Age: ${age}</p>
    </div>
`;

// Expressions in templates
const price = 19.99;
const tax = 0.08;
const total = `Total: $${(price * (1 + tax)).toFixed(2)}`;

// Tagged templates
function highlight(strings, ...values) {
    return strings.map((str, i) => 
        str + (values[i] ? `<mark>${values[i]}</mark>` : '')
    ).join('');
}

const result = highlight`Name: ${name}, Age: ${age}`;
```

Much more powerful than traditional string concatenation.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals",
        "points": 1,
        "answers": [
            {"text": "Strings using backticks with embedded expressions", "is_correct": True},
            {"text": "Regular string literals", "is_correct": False},
            {"text": "Array literals", "is_correct": False},
            {"text": "Object literals", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the rest parameter (...args)?",
        "explanation": """# Rest Parameters (ES6)

Rest parameters allow a function to accept indefinite number of arguments as an array.

## Syntax: `...paramName`

## Examples:
```javascript
// Basic rest parameters
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}

console.log(sum(1, 2, 3, 4, 5)); // 15
console.log(sum(10, 20));        // 30

// Rest with other parameters
function greet(greeting, ...names) {
    return `${greeting} ${names.join(', ')}!`;
}

console.log(greet("Hello", "Alice", "Bob", "Charlie"));
// "Hello Alice, Bob, Charlie!"

// Array destructuring with rest
const [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first);  // 1
console.log(second); // 2
console.log(rest);   // [3, 4, 5]

// Object destructuring with rest
const {name, age, ...otherInfo} = {
    name: "Alice",
    age: 25,
    city: "NYC",
    country: "USA"
};
console.log(otherInfo); // {city: "NYC", country: "USA"}
```

Replaces the need for the `arguments` object.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters",
        "points": 1,
        "answers": [
            {"text": "Collects remaining arguments into an array", "is_correct": True},
            {"text": "Spreads array elements", "is_correct": False},
            {"text": "Creates default parameters", "is_correct": False},
            {"text": "Defines optional parameters", "is_correct": False},
        ],
    },
    {
        "text": "What is array destructuring in ES6?",
        "explanation": """# Array Destructuring (ES6)

Array destructuring allows unpacking values from arrays into distinct variables.

## Examples:
```javascript
// Basic array destructuring
const colors = ["red", "green", "blue"];
const [primary, secondary, tertiary] = colors;
console.log(primary);   // "red"
console.log(secondary); // "green"
console.log(tertiary);  // "blue"

// Skipping elements
const numbers = [1, 2, 3, 4, 5];
const [first, , third, , fifth] = numbers;
console.log(first, third, fifth); // 1, 3, 5

// Default values
const [a, b, c = 0] = [1, 2];
console.log(a, b, c); // 1, 2, 0

// Rest in destructuring
const [head, ...tail] = [1, 2, 3, 4, 5];
console.log(head); // 1
console.log(tail); // [2, 3, 4, 5]

// Swapping variables
let x = 1, y = 2;
[x, y] = [y, x];
console.log(x, y); // 2, 1

// Function return values
function getCoordinates() {
    return [10, 20];
}
const [x2, y2] = getCoordinates();

// Nested arrays
const nested = [[1, 2], [3, 4]];
const [[a1, b1], [a2, b2]] = nested;
```

Makes working with arrays much more convenient.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#array_destructuring",
        "points": 1,
        "answers": [
            {"text": "Unpacking array values into variables", "is_correct": True},
            {"text": "Creating new arrays", "is_correct": False},
            {"text": "Sorting array elements", "is_correct": False},
            {"text": "Filtering array elements", "is_correct": False},
        ],
    },
    {
        "text": "What are default parameters in ES6?",
        "explanation": """# Default Parameters (ES6)

Default parameters allow function parameters to have default values if no value or undefined is passed.

## Examples:
```javascript
// Basic default parameters
function greet(name = "World", punctuation = "!") {
    return `Hello, ${name}${punctuation}`;
}

console.log(greet());           // "Hello, World!"
console.log(greet("Alice"));    // "Hello, Alice!"
console.log(greet("Bob", "?"));  // "Hello, Bob?"

// Default parameters can reference other parameters
function createUser(name, role = "user", active = true) {
    return {name, role, active};
}

// Default parameters with destructuring
function processOrder({
    item = "Unknown",
    quantity = 1,
    price = 0,
    discount = 0
} = {}) {
    const total = quantity * price * (1 - discount);
    return {item, quantity, price, discount, total};
}

console.log(processOrder());  // Uses all defaults
console.log(processOrder({item: "Book", price: 20}));

// Default parameters are evaluated at call time
function getValue() {
    console.log("Getting default value");
    return 42;
}

function test(value = getValue()) {
    return value;
}

test(10);  // getValue() not called
test();    // getValue() is called

// Default parameters with arrow functions
const multiply = (a = 1, b = 1) => a * b;
```

Much cleaner than checking for undefined values manually.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters",
        "points": 1,
        "answers": [
            {"text": "Allows function parameters to have default values", "is_correct": True},
            {"text": "Makes all parameters optional", "is_correct": False},
            {"text": "Sets global default values", "is_correct": False},
            {"text": "Creates constant parameters", "is_correct": False},
        ],
    },
]
