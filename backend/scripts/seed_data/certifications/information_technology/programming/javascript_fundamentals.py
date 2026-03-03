"""JavaScript Fundamentals Certification"""

CERTIFICATION = {
    "name": "JavaScript Fundamentals",
    "description": "JavaScript Certified Entry-level Developer",
    "slug": "javascript-fundamentals",
    "level": "Entry",
    "duration": 20,
    "questions_count": 120,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is JavaScript?",
        "explanation": """# JavaScript Programming Language

**JavaScript** is a high-level, interpreted programming language that was originally created to make web pages interactive.

## Key Features:
- **Interpreted**: Runs directly in browsers or Node.js
- **Dynamic**: Variables can change types at runtime
- **Object-oriented**: Supports objects and classes
- **Functional**: Supports functional programming concepts

## Examples:

### 1. Simple Program
```javascript
console.log("Hello, World!");
// Output: Hello, World!
```

### 2. Variables and Data Types
```javascript
let name = "Alice";         // String
let age = 25;              // Number
let height = 5.6;          // Number (no separate float type)
let isStudent = true;      // Boolean

console.log(`Name: ${name}, Age: ${age}`);
// Output: Name: Alice, Age: 25
```

### 3. Basic Operations
```javascript
// Arithmetic
let x = 10 + 5;    // 15
let y = 20 - 8;    // 12
let z = 4 * 3;     // 12

// String operations
let greeting = "Hello" + " " + "World";
console.log(greeting);  // Hello World
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction",
        "points": 1,
        "answers": [
            {"text": "A programming language for web development", "is_correct": True},
            {"text": "A database management system", "is_correct": False},
            {"text": "An operating system", "is_correct": False},
            {"text": "A web browser", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log(Boolean(0))?",
        "explanation": """# Boolean Values in JavaScript

**Boolean(0)** returns false because 0 is considered a **falsy** value in JavaScript.

## Falsy Values:
- `false`, `0`, `-0`, `0n`
- Empty strings: `""`, `''`
- `null`, `undefined`, `NaN`

## Truthy Values:
- `true`, any non-zero number
- Non-empty strings: `"hello"`, `"false"`
- Objects, arrays (even empty ones)

## Examples:

### 1. Boolean Conversion
```javascript
console.log(Boolean(0));        // false
console.log(Boolean(1));        // true
console.log(Boolean(-5));       // true
console.log(Boolean(""));       // false
console.log(Boolean("hello"));  // true
```

### 2. Implicit Conversion
```javascript
if (0) {
    console.log("This won't run");
} else {
    console.log("0 is falsy");
}

if ("hello") {
    console.log("Strings are truthy");
}
```

### 3. Practical Usage
```javascript
let numbers = [1, 2, 3, 4, 5];

if (numbers.length) {  // Checks if array has items
    console.log("Array has items");
} else {
    console.log("Array is empty");
}
// Output: Array has items
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Glossary/Truthy",
        "points": 1,
        "answers": [
            {"text": "true", "is_correct": False},
            {"text": "false", "is_correct": True},
            {"text": "0", "is_correct": False},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which method adds an element to the end of an array?",
        "explanation": """# Array Methods in JavaScript

**push()** method adds one or more elements to the end of an array and returns the new length.

## Common Array Methods:
- `push()` - Add elements to end
- `pop()` - Remove last element
- `unshift()` - Add elements to beginning
- `shift()` - Remove first element

## Examples:

### 1. Using push()
```javascript
let fruits = ["apple", "banana"];
fruits.push("orange");
console.log(fruits);  // ["apple", "banana", "orange"]

// Push multiple elements
let numbers = [1, 2, 3];
numbers.push(4, 5, 6);
console.log(numbers);  // [1, 2, 3, 4, 5, 6]

// Returns new length
let length = fruits.push("grape");
console.log(length);  // 4
```

### 2. Other Array Methods
```javascript
let colors = ["red", "blue"];

// Add to beginning
colors.unshift("green");
console.log(colors);  // ["green", "red", "blue"]

// Remove from end
let lastColor = colors.pop();
console.log(lastColor);  // "blue"
console.log(colors);     // ["green", "red"]

// Remove from beginning
let firstColor = colors.shift();
console.log(firstColor); // "green"
```

### 3. Method Chaining
```javascript
let result = [1, 2, 3]
    .push(4)           // Add 4
    .map(x => x * 2);  // Double each number
// Note: push() returns length, not array, so this won't work
// Better approach:
let arr = [1, 2, 3];
arr.push(4);
result = arr.map(x => x * 2);  // [2, 4, 6, 8]
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push",
        "points": 1,
        "answers": [
            {"text": "add()", "is_correct": False},
            {"text": "push()", "is_correct": True},
            {"text": "append()", "is_correct": False},
            {"text": "insert()", "is_correct": False},
        ],
    },
    {
        "text": "What does the length property return?",
        "explanation": """# Length Property in JavaScript

The **length** property returns the number of elements in an array or characters in a string.

## Works with:
- Arrays, strings, and other array-like objects
- Returns a number representing the count

## Examples:

### 1. String Length
```javascript
let text = "Hello World";
console.log(text.length);  // 11 (includes space)

let name = "JavaScript";
console.log(name.length);  // 10
```

### 2. Array Length
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(numbers.length);  // 5

let emptyArray = [];
console.log(emptyArray.length);  // 0
```

### 3. Modifying Array Length
```javascript
let arr = [1, 2, 3, 4, 5];
console.log(arr.length);  // 5

// Truncate array
arr.length = 3;
console.log(arr);  // [1, 2, 3]

// Extend array (fills with undefined)
arr.length = 5;
console.log(arr);  // [1, 2, 3, undefined, undefined]
```

### 4. Practical Usage
```javascript
// Check if array is empty
let items = [];
if (items.length === 0) {
    console.log("No items found");
}

// Loop through array
let words = ["hello", "world", "javascript"];
for (let i = 0; i < words.length; i++) {
    console.log(`${i}: ${words[i]}`);
}

// Get last element
let lastItem = words[words.length - 1];
console.log(lastItem);  // "javascript"
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/length",
        "points": 1,
        "answers": [
            {"text": "The length of an array or string", "is_correct": True},
            {"text": "The type of an object", "is_correct": False},
            {"text": "The value of an object", "is_correct": False},
            {"text": "The memory address", "is_correct": False},
        ],
    },
    {
        "text": "What is the correct way to create a comment in JavaScript?",
        "explanation": """# Comments in JavaScript

**Comments** in JavaScript can be single-line (`//`) or multi-line (`/* */`).

## Types of Comments:

### 1. Single-line Comments
```javascript
// This is a single-line comment
console.log("Hello World");  // This is also a comment

// You can have multiple single-line comments
// Each line needs its own // symbols
let x = 5;  // Variable declaration
```

### 2. Multi-line Comments
```javascript
/*
This is a multi-line comment
that spans multiple lines
*/

let y = 10; /* This can also be inline */

/*
Multi-line comments are useful for:
- Longer explanations
- Temporarily disabling code blocks
- Documentation headers
*/
```

### 3. JSDoc Comments (Documentation)
```javascript
/**
 * Calculates the area of a rectangle
 * @param {number} width - The width of the rectangle
 * @param {number} height - The height of the rectangle
 * @returns {number} The area of the rectangle
 */
function calculateArea(width, height) {
    return width * height;
}
```

### 4. Commenting Best Practices
```javascript
// Good: Explain WHY, not WHAT
let totalPrice = price * taxRate;  // Apply local tax rate

// Bad: Just repeating what code does
x = x + 1;  // Add 1 to x

// Good: Explain complex logic
// Calculate compound interest using A = P(1+r/n)^(nt)
let amount = principal * Math.pow(1 + rate/frequency, frequency * time);

// Temporary disable code
/*
if (debugMode) {
    console.log("Debug info");
}
*/
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types#comments",
        "points": 1,
        "answers": [
            {"text": "<!-- This is a comment -->", "is_correct": False},
            {"text": "# This is a comment", "is_correct": False},
            {"text": "// This is a comment", "is_correct": True},
            {"text": "' This is a comment", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following is a valid JavaScript variable name?",
        "explanation": """# JavaScript Variable Naming Rules

**Valid variable names** in JavaScript must follow specific rules and conventions.

## Rules (Required):
- Must start with letter (a-z, A-Z), underscore (_), or dollar sign ($)
- Can contain letters, numbers, underscores, and dollar signs
- Case-sensitive
- Cannot be JavaScript keywords

## Examples:

### 1. Valid Names
```javascript
let name = "Alice";           // lowercase
let firstName = "Bob";        // camelCase (preferred)
let first_name = "Charlie";   // snake_case (less common)
let _private = "secret";      // starts with underscore
let $element = document;      // starts with dollar sign
let age2 = 25;               // contains numbers
const MAX_SIZE = 100;        // constants (all uppercase)
```

### 2. Invalid Names
```javascript
// These will cause SyntaxError:
// let 2name = "invalid";        // starts with number
// let first-name = "invalid";   // contains hyphen
// let class = "invalid";        // JavaScript keyword
// let first name = "invalid";   // contains space
```

### 3. JavaScript Keywords (Reserved)
```javascript
// Reserved words that cannot be used as variable names:
// break, case, catch, class, const, continue, debugger, default,
// delete, do, else, export, extends, finally, for, function,
// if, import, in, instanceof, let, new, return, super, switch,
// this, throw, try, typeof, var, void, while, with, yield
```

### 4. Naming Conventions
```javascript
// Variables and functions: camelCase
let userAge = 25;
function calculateTotal() {
    return 100;
}

// Constants: ALL_CAPS
const PI = 3.14159;
const MAX_RETRIES = 5;

// Classes: PascalCase
class StudentRecord {
    constructor(name) {
        this.name = name;
    }
}

// Private-like variables: underscore prefix
let _internalValue = 42;
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_Types#variables",
        "points": 1,
        "answers": [
            {"text": "2name", "is_correct": False},
            {"text": "first-name", "is_correct": False},
            {"text": "firstName", "is_correct": True},
            {"text": "class", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log(typeof 3.14)?",
        "explanation": """# Data Types in JavaScript

**typeof** operator returns the data type of a value. `3.14` is a **number** in JavaScript.

## Basic Data Types:

### 1. Primitive Types
```javascript
console.log(typeof 42);        // "number"
console.log(typeof 3.14);      // "number"
console.log(typeof "Hello");   // "string"
console.log(typeof true);      // "boolean"
console.log(typeof undefined); // "undefined"
console.log(typeof null);      // "object" (this is a known quirk!)
console.log(typeof Symbol());  // "symbol"
console.log(typeof BigInt(123)); // "bigint"
```

### 2. Non-Primitive Types
```javascript
console.log(typeof {});        // "object"
console.log(typeof []);        // "object" (arrays are objects)
console.log(typeof function(){}); // "function"
console.log(typeof new Date()); // "object"
console.log(typeof /regex/);   // "object"
```

### 3. Number Type Details
```javascript
// JavaScript has only one number type
console.log(typeof 42);     // "number"
console.log(typeof 3.14);   // "number"
console.log(typeof -17);    // "number"
console.log(typeof Infinity); // "number"
console.log(typeof NaN);    // "number" (Not a Number is still type number!)
```

### 4. Type Checking
```javascript
let x = 3.14;
console.log(typeof x === "number");  // true

// More specific checks
console.log(Number.isInteger(42));   // true
console.log(Number.isInteger(3.14)); // false
console.log(Number.isNaN(NaN));      // true
console.log(Number.isFinite(42));    // true
```

### 5. Type Conversion
```javascript
console.log(typeof String(123));    // "string" - "123"
console.log(typeof Number("456"));  // "number" - 456
console.log(typeof Boolean(1));     // "boolean" - true
console.log(typeof parseInt("78")); // "number" - 78
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof",
        "points": 1,
        "answers": [
            {"text": "\"float\"", "is_correct": False},
            {"text": "\"number\"", "is_correct": True},
            {"text": "\"decimal\"", "is_correct": False},
            {"text": "\"double\"", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for string concatenation in JavaScript?",
        "explanation": """# String Concatenation in JavaScript

**+ operator** is used to concatenate (join) strings in JavaScript, along with template literals.

## String Operations:

### 1. Basic Concatenation with +
```javascript
let firstName = "John";
let lastName = "Doe";
let fullName = firstName + " " + lastName;
console.log(fullName);  // John Doe

let greeting = "Hello" + " " + "World";
console.log(greeting);  // Hello World
```

### 2. Template Literals (ES6+)
```javascript
let name = "Alice";
let age = 25;
let message = `My name is ${name} and I am ${age} years old`;
console.log(message);  // My name is Alice and I am 25 years old

// Multi-line strings
let multiline = `
    This is a
    multi-line
    string
`;
```

### 3. Multiple Concatenations
```javascript
let result = "JavaScript" + " " + "is" + " " + "awesome";
console.log(result);  // JavaScript is awesome

// With variables
let language = "JavaScript";
let adjective = "powerful";
let sentence = language + " is " + adjective + "!";
console.log(sentence);  // JavaScript is powerful!
```

### 4. Alternative Methods
```javascript
// Using Array.join()
let words = ["JavaScript", "is", "great"];
let sentence = words.join(" ");  // JavaScript is great

// Using concat() method
let str1 = "Hello";
let str2 = " World";
let result = str1.concat(str2);  // Hello World
```

### 5. Type Coercion with +
```javascript
// Automatic string conversion
let result = "Age: " + 25;
console.log(result);  // "Age: 25"

let mixed = "5" + 3;
console.log(mixed);   // "53" (string concatenation, not addition)

// To force addition:
let sum = Number("5") + 3;  // 8
// or
let sum2 = +"5" + 3;        // 8 (unary + converts to number)
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#string_concatenation",
        "points": 1,
        "answers": [
            {"text": "&", "is_correct": False},
            {"text": "+", "is_correct": True},
            {"text": "*", "is_correct": False},
            {"text": ".", "is_correct": False},
        ],
    },
    {
        "text": "What will be the output of console.log(Math.floor(5.7))?",
        "explanation": """# Math.floor() Method in JavaScript

**Math.floor()** returns the largest integer less than or equal to a given number (rounds down).

## Math Methods:

### 1. Math.floor() - Round Down
```javascript
console.log(Math.floor(5.7));    // 5
console.log(Math.floor(5.1));    // 5
console.log(Math.floor(5.9));    // 5
console.log(Math.floor(-5.1));   // -6 (rounds down toward negative infinity)
```

### 2. Related Math Methods
```javascript
// Math.ceil() - Round Up
console.log(Math.ceil(5.1));     // 6
console.log(Math.ceil(5.9));     // 6
console.log(Math.ceil(-5.1));    // -5

// Math.round() - Round to Nearest
console.log(Math.round(5.4));    // 5
console.log(Math.round(5.5));    // 6
console.log(Math.round(5.6));    // 6

// Math.trunc() - Remove Decimal Part
console.log(Math.trunc(5.9));    // 5
console.log(Math.trunc(-5.9));   // -5
```

### 3. Practical Examples
```javascript
// Calculate pages needed for pagination
let totalItems = 23;
let itemsPerPage = 5;
let pages = Math.ceil(totalItems / itemsPerPage);
console.log(`Need ${pages} pages`);  // Need 5 pages

// Round down to nearest 10
let price = 47.99;
let roundedDown = Math.floor(price / 10) * 10;
console.log(roundedDown);  // 40

// Generate random integer between 1 and 6 (dice)
let dice = Math.floor(Math.random() * 6) + 1;
console.log(dice);  // Random number: 1, 2, 3, 4, 5, or 6
```

### 4. Working with Time
```javascript
// Convert milliseconds to seconds (round down)
let milliseconds = 5750;
let seconds = Math.floor(milliseconds / 1000);
console.log(seconds);  // 5

// Age calculation (round down)
let birthYear = 1995;
let currentYear = 2023;
let age = Math.floor((currentYear - birthYear));
console.log(age);  // 28
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor",
        "points": 1,
        "answers": [
            {"text": "5.7", "is_correct": False},
            {"text": "5", "is_correct": True},
            {"text": "6", "is_correct": False},
            {"text": "6.0", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword is used to define a function in JavaScript?",
        "explanation": """# Function Definition in JavaScript

**function** keyword is used to define functions in JavaScript, along with arrow functions and function expressions.

## Function Declaration Syntax:
```javascript
function functionName(parameters) {
    // Function body
    return value;  // Optional
}
```

## Examples:

### 1. Simple Function
```javascript
function greet() {
    console.log("Hello, World!");
}

greet();  // Call the function
// Output: Hello, World!
```

### 2. Function with Parameters
```javascript
function greetPerson(name) {
    console.log(`Hello, ${name}!`);
}

greetPerson("Alice");  // Hello, Alice!
greetPerson("Bob");    // Hello, Bob!
```

### 3. Function with Return Value
```javascript
function addNumbers(a, b) {
    let result = a + b;
    return result;
}

let sum = addNumbers(5, 3);
console.log(sum);  // 8
```

### 4. Function Expression
```javascript
const multiply = function(a, b) {
    return a * b;
};

console.log(multiply(4, 5));  // 20
```

### 5. Arrow Functions (ES6+)
```javascript
// Arrow function syntax
const divide = (a, b) => {
    return a / b;
};

// Shorter arrow function for simple expressions
const square = x => x * x;
const add = (a, b) => a + b;

console.log(square(5));    // 25
console.log(add(3, 4));    // 7
```

### 6. Function with Default Parameters
```javascript
function introduce(name, age = 25) {
    return `My name is ${name} and I am ${age} years old`;
}

console.log(introduce("Alice"));         // Uses default age
console.log(introduce("Bob", 30));       // Uses provided age
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions",
        "points": 1,
        "answers": [
            {"text": "def", "is_correct": False},
            {"text": "function", "is_correct": True},
            {"text": "func", "is_correct": False},
            {"text": "define", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log([1, 2, 3])?",
        "explanation": """# Array Output in JavaScript

**Arrays** are displayed as comma-separated values in square brackets when logged to the console.

## Array Display:

### 1. Basic Array Logging
```javascript
console.log([1, 2, 3]);        // [1, 2, 3]
console.log(["a", "b", "c"]);  // ['a', 'b', 'c']
console.log([]);               // []
```

### 2. Mixed Data Types
```javascript
let mixedArray = [1, "hello", true, null];
console.log(mixedArray);  // [1, 'hello', true, null]

let nestedArray = [1, [2, 3], 4];
console.log(nestedArray);  // [1, [2, 3], 4]
```

### 3. Array Properties and Methods
```javascript
let numbers = [1, 2, 3];
console.log(numbers.length);     // 3
console.log(numbers[0]);         // 1 (first element)
console.log(numbers[numbers.length - 1]); // 3 (last element)

// Array methods
console.log(numbers.join(", "));  // "1, 2, 3"
console.log(numbers.toString());  // "1,2,3"
```

### 4. Array vs String Representation
```javascript
let arr = [1, 2, 3];
console.log(arr);              // [1, 2, 3] (array)
console.log(String(arr));      // "1,2,3" (string)
console.log(JSON.stringify(arr)); // "[1,2,3]" (JSON string)
```

### 5. Console Methods for Arrays
```javascript
let data = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30}
];

console.log(data);          // Standard array display
console.table(data);        // Table format in console
console.dir(data);          // Directory-style listing
```

### 6. Array Iteration
```javascript
let fruits = ["apple", "banana", "orange"];

// For loop
for (let i = 0; i < fruits.length; i++) {
    console.log(i, fruits[i]);
}

// For...of loop
for (let fruit of fruits) {
    console.log(fruit);
}

// forEach method
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array",
        "points": 1,
        "answers": [
            {"text": "[1, 2, 3]", "is_correct": True},
            {"text": "(1, 2, 3)", "is_correct": False},
            {"text": "1 2 3", "is_correct": False},
            {"text": "Array(3)", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to exit from a loop in JavaScript?",
        "explanation": """# Loop Control Statements in JavaScript

**break** statement is used to exit/terminate a loop immediately.

## Loop Control Keywords:
- `break` - Exit loop completely
- `continue` - Skip current iteration, continue with next
- `return` - Exit function (and any loops within)

## Examples:

### 1. Using break
```javascript
// Exit loop when condition met
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}
// Output: 0, 1, 2, 3, 4

// Search and exit
let numbers = [1, 3, 7, 2, 9, 5];
let target = 7;
for (let num of numbers) {
    if (num === target) {
        console.log(`Found ${target}!`);
        break;
    }
}
```

### 2. Using continue
```javascript
// Skip even numbers
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {
        continue;  // Skip rest of loop body
    }
    console.log(i);
}
// Output: 1, 3, 5, 7, 9

// Process only valid data
let data = [1, -2, 3, 0, 5, -1];
for (let value of data) {
    if (value <= 0) {
        continue;  // Skip negative/zero values
    }
    console.log(`Processing: ${value}`);
}
```

### 3. Nested Loops with break
```javascript
// Break only exits innermost loop
for (let i = 0; i < 3; i++) {
    console.log(`Outer loop: ${i}`);
    for (let j = 0; j < 3; j++) {
        if (j === 1) {
            break;  // Only breaks inner loop
        }
        console.log(`  Inner loop: ${j}`);
    }
}

// To break outer loop, use labeled break
outerLoop: for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        if (i === 1 && j === 1) {
            break outerLoop;  // Breaks outer loop
        }
        console.log(`${i}, ${j}`);
    }
}
```

### 4. While Loop with break
```javascript
let count = 0;
while (true) {  // Infinite loop
    count++;
    console.log(count);
    if (count >= 5) {
        break;  // Exit the loop
    }
}
// Output: 1, 2, 3, 4, 5
```

### 5. Switch Statement break
```javascript
let day = "Monday";
switch (day) {
    case "Monday":
        console.log("Start of work week");
        break;  // Prevents fall-through
    case "Friday":
        console.log("End of work week");
        break;
    default:
        console.log("Regular day");
}
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break",
        "points": 1,
        "answers": [
            {"text": "exit", "is_correct": False},
            {"text": "break", "is_correct": True},
            {"text": "stop", "is_correct": False},
            {"text": "end", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of console.log('JavaScript'[0])?",
        "explanation": """# String Indexing in JavaScript

**String indexing** uses square brackets to access individual characters. JavaScript uses **zero-based indexing**.

## String Indexing:

### 1. Positive Indexing
```javascript
let text = "JavaScript";
console.log(text[0]);    // 'J' - First character
console.log(text[1]);    // 'a' - Second character
console.log(text[2]);    // 'v' - Third character
console.log(text[9]);    // 't' - Last character
```

### 2. Accessing Characters
```javascript
let text = "JavaScript";
console.log(text[0]);               // 'J'
console.log(text.charAt(0));        // 'J' (alternative method)
console.log(text.charAt(100));      // '' (empty string for out of bounds)
console.log(text[100]);             // undefined (for out of bounds)
```

### 3. String Slicing
```javascript
let text = "JavaScript";
console.log(text.slice(0, 4));      // 'Java' - Characters 0-3
console.log(text.slice(4));         // 'Script' - From index 4 to end
console.log(text.slice(-6));        // 'Script' - Last 6 characters
console.log(text.slice(-6, -2));    // 'Scri' - From -6 to -2
```

### 4. String Substring Methods
```javascript
let text = "JavaScript";
console.log(text.substring(0, 4));  // 'Java'
console.log(text.substr(4, 6));     // 'Script' (deprecated)
console.log(text.slice(4, 10));     // 'Script'
```

### 5. Practical Examples
```javascript
let email = "user@example.com";
let atIndex = email.indexOf('@');
let username = email.slice(0, atIndex);     // 'user'
let domain = email.slice(atIndex + 1);      // 'example.com'

// Check file extension
let filename = "document.pdf";
let extension = filename.slice(-4);         // '.pdf'

// Get first and last characters
let word = "Hello";
let firstLast = word[0] + word[word.length - 1];  // 'Ho'

// Check if string starts with specific character
let text2 = "JavaScript";
if (text2[0] === 'J') {
    console.log("Starts with J");
}
```

### 6. String Immutability
```javascript
let text = "Hello";
text[0] = "h";  // This doesn't work - strings are immutable
console.log(text);  // Still "Hello"

// Create new string instead
let newText = "h" + text.slice(1);  // "hello"
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String#character_access",
        "points": 1,
        "answers": [
            {"text": "'J'", "is_correct": True},
            {"text": "'a'", "is_correct": False},
            {"text": "'JavaScript'", "is_correct": False},
            {"text": "0", "is_correct": False},
        ],
    },
    {
        "text": "Which data structure is mutable in JavaScript?",
        "explanation": """# Mutable vs Immutable Data Structures in JavaScript

**Arrays** are mutable in JavaScript, meaning their contents can be changed after creation.

## Mutable Types (Can be changed):
- **Arrays** `[]`
- **Objects** `{}`
- **Functions** (properties can be added)

## Immutable Types (Cannot be changed):
- **Strings** `""`
- **Numbers**
- **Booleans**
- **null**, **undefined**

## Examples:

### 1. Arrays are Mutable
```javascript
// Arrays can be modified
let fruits = ["apple", "banana"];
fruits.push("orange");              // Add element
fruits[0] = "grape";                // Change element
fruits.pop();                       // Remove last element
console.log(fruits);  // ['grape', 'banana']

// Array methods that modify the original
fruits.splice(1, 0, "kiwi");        // Insert at index 1
fruits.sort();                      // Sort in place
fruits.reverse();                   // Reverse in place
```

### 2. Strings are Immutable
```javascript
// Strings cannot be modified
let text = "Hello";
text[0] = "h";  // This doesn't work
console.log(text);  // Still "Hello"

// Create new string instead
let newText = "h" + text.slice(1);  // "hello"
let upperText = text.toUpperCase(); // "HELLO" (creates new string)
```

### 3. Objects are Mutable
```javascript
let student = {name: "Alice", age: 20};
student.grade = "A";                // Add new property
student.age = 21;                   // Modify existing property
delete student.name;                // Remove property
console.log(student);  // {age: 21, grade: "A"}

// Nested objects
let person = {
    name: "Bob",
    address: {city: "New York", zip: "10001"}
};
person.address.city = "Boston";     // Modifies nested object
```

### 4. Reference vs Value
```javascript
// Arrays and objects are passed by reference
let arr1 = [1, 2, 3];
let arr2 = arr1;  // Both point to same array
arr2.push(4);
console.log(arr1);  // [1, 2, 3, 4] - Original array changed!

// Primitives are passed by value
let str1 = "hello";
let str2 = str1;  // Copy of the value
str2 = "world";   // Creates new string
console.log(str1);  // "hello" - Original unchanged
```

### 5. Avoiding Mutation
```javascript
// Create copies to avoid mutation
let original = [1, 2, 3];

// Shallow copy methods
let copy1 = [...original];          // Spread operator
let copy2 = Array.from(original);   // Array.from()
let copy3 = original.slice();       // slice() method

copy1.push(4);
console.log(original);  // [1, 2, 3] - Unchanged

// For objects
let originalObj = {name: "Alice", age: 25};
let copyObj = {...originalObj};     // Spread operator
let copyObj2 = Object.assign({}, originalObj);
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array",
        "points": 1,
        "answers": [
            {"text": "String", "is_correct": False},
            {"text": "Array", "is_correct": True},
            {"text": "Number", "is_correct": False},
            {"text": "Boolean", "is_correct": False},
        ],
    },
    {
        "text": "What keyword is used to check if a value exists in an array?",
        "explanation": """# Checking Array Membership in JavaScript

**includes()** method is commonly used to check if a value exists in an array, along with **indexOf()**.

## Array Membership Methods:

### 1. includes() Method (ES2016+)
```javascript
let numbers = [1, 2, 3, 4, 5];
console.log(numbers.includes(3));      // true
console.log(numbers.includes(6));      // false

let colors = ["red", "blue", "green"];
console.log(colors.includes("blue"));  // true
console.log(colors.includes("yellow")); // false
```

### 2. indexOf() Method
```javascript
let fruits = ["apple", "banana", "orange"];
console.log(fruits.indexOf("banana"));     // 1 (index position)
console.log(fruits.indexOf("grape"));      // -1 (not found)

// Check existence
if (fruits.indexOf("apple") !== -1) {
    console.log("Apple found!");
}
```

### 3. find() and findIndex() Methods
```javascript
let users = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30},
    {name: "Charlie", age: 35}
];

// Find object
let user = users.find(u => u.name === "Bob");
console.log(user);  // {name: "Bob", age: 30}

// Find index of object
let index = users.findIndex(u => u.age > 30);
console.log(index);  // 2 (Charlie's index)
```

### 4. some() Method
```javascript
let numbers = [1, 2, 3, 4, 5];

// Check if any element meets condition
let hasEven = numbers.some(num => num % 2 === 0);
console.log(hasEven);  // true

let hasLarge = numbers.some(num => num > 10);
console.log(hasLarge); // false
```

### 5. Practical Examples
```javascript
// Validate user input
let validChoices = ["yes", "no", "maybe"];
let userInput = "yes";
if (validChoices.includes(userInput)) {
    console.log("Valid choice");
}

// Check file extensions
let allowedExtensions = [".jpg", ".png", ".gif"];
let filename = "image.png";
let isAllowed = allowedExtensions.some(ext => filename.endsWith(ext));
console.log(isAllowed);  // true

// Filter arrays
let emails = ["user1@gmail.com", "user2@yahoo.com", "user3@gmail.com"];
let gmailUsers = emails.filter(email => email.includes("@gmail.com"));
console.log(gmailUsers);  // ['user1@gmail.com', 'user3@gmail.com']
```

### 6. String Contains Check
```javascript
let text = "JavaScript programming";
console.log(text.includes("Script"));     // true
console.log(text.includes("Python"));     // false

// Case sensitive
console.log(text.includes("javascript")); // false
console.log(text.toLowerCase().includes("javascript")); // true
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes",
        "points": 1,
        "answers": [
            {"text": "contains", "is_correct": False},
            {"text": "includes", "is_correct": True},
            {"text": "in", "is_correct": False},
            {"text": "has", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between '==' and '===' operators in JavaScript?",
        "explanation": """# Equality Operators in JavaScript

**==** performs type coercion and compares values, while **===** compares both value and type without coercion.

## Comparison Operators:

### 1. Loose Equality (==)
```javascript
console.log(5 == "5");        // true (string "5" converted to number)
console.log(true == 1);       // true (true converted to 1)
console.log(false == 0);      // true (false converted to 0)
console.log(null == undefined); // true (special case)
console.log(0 == "");         // true (empty string converted to 0)
```

### 2. Strict Equality (===)
```javascript
console.log(5 === "5");       // false (different types)
console.log(true === 1);      // false (different types)
console.log(false === 0);     // false (different types)
console.log(null === undefined); // false (different types)
console.log(0 === "");        // false (different types)
console.log(5 === 5);         // true (same type and value)
```

### 3. Type Coercion Examples
```javascript
// Loose equality with type coercion
console.log("5" == 5);        // true
console.log([1] == 1);        // true (array converted to primitive)
console.log([1,2] == "1,2");  // true (array.toString())
console.log({} == "[object Object]"); // true

// Strict equality without coercion
console.log("5" === 5);       // false
console.log([1] === 1);       // false
console.log([1,2] === "1,2"); // false
```

### 4. Best Practices
```javascript
// Recommended: Use strict equality
let userAge = "25";
if (userAge === "25") {       // Check for exact string match
    console.log("User age is string 25");
}

if (Number(userAge) === 25) { // Convert then compare
    console.log("User age is number 25");
}

// Avoid loose equality for clarity
// if (userAge == 25) { }     // Unclear intent
```

### 5. Inequality Operators
```javascript
// Loose inequality
console.log(5 != "5");        // false (values are equal after coercion)
console.log(5 != 3);          // true

// Strict inequality
console.log(5 !== "5");       // true (different types)
console.log(5 !== 5);         // false (same type and value)
```

### 6. Common Gotchas
```javascript
// Surprising results with ==
console.log(0 == false);      // true
console.log("" == false);     // true
console.log([] == false);     // true
console.log([] == "");        // true
console.log("0" == false);    // true

// But:
console.log(false == "false"); // false!
console.log(0 == null);       // false!

// Always use === for predictable results
console.log(0 === false);     // false
console.log("" === false);    // false
console.log([] === false);    // false
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "=== is stricter and doesn't perform type coercion", "is_correct": True},
            {"text": "== is stricter", "is_correct": False},
            {"text": "They work only with numbers", "is_correct": False},
        ],
    },
    {
        "text": "What is the correct way to create an object in JavaScript?",
        "explanation": """# Creating Objects in JavaScript

**Objects** in JavaScript can be created using object literals, constructors, or classes.

## Object Creation Methods:

### 1. Object Literal (Most Common)
```javascript
let person = {
    name: "Alice",
    age: 25,
    city: "New York"
};

console.log(person.name);  // Alice
console.log(person["age"]); // 25
```

### 2. Object Constructor
```javascript
let car = new Object();
car.brand = "Toyota";
car.model = "Camry";
car.year = 2023;

console.log(car);  // {brand: "Toyota", model: "Camry", year: 2023}
```

### 3. Constructor Function
```javascript
function Student(name, grade) {
    this.name = name;
    this.grade = grade;
}

let student1 = new Student("Bob", "A");
console.log(student1.name);  // Bob
```

### 4. ES6 Class Syntax
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Hello, I'm ${this.name}`;
    }
}

let person = new Person("Charlie", 30);
console.log(person.greet());  // Hello, I'm Charlie
```

### 5. Object Methods
```javascript
let calculator = {
    add: function(a, b) {
        return a + b;
    },
    // ES6 shorthand
    subtract(a, b) {
        return a - b;
    }
};

console.log(calculator.add(5, 3));       // 8
console.log(calculator.subtract(10, 4)); // 6
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects",
        "points": 1,
        "answers": [
            {"text": "let obj = ()", "is_correct": False},
            {"text": "let obj = []", "is_correct": False},
            {"text": "let obj = {}", "is_correct": True},
            {"text": "let obj = <>", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'this' keyword refer to in JavaScript?",
        "explanation": """# The 'this' Keyword in JavaScript

**this** refers to the context in which a function is called, typically the object that owns the method.

## Context-Dependent Behavior:

### 1. In Object Methods
```javascript
let person = {
    name: "Alice",
    greet: function() {
        return `Hello, I'm ${this.name}`;
    }
};

console.log(person.greet());  // Hello, I'm Alice
```

### 2. In Global Context
```javascript
console.log(this);  // Window object in browser, global in Node.js

function showThis() {
    console.log(this);
}
showThis();  // Window (non-strict) or undefined (strict mode)
```

### 3. In Arrow Functions
```javascript
let person = {
    name: "Bob",
    greet: () => {
        return `Hello, I'm ${this.name}`;  // 'this' from outer scope
    }
};

// Arrow functions don't have their own 'this'
console.log(person.greet());  // Hello, I'm undefined
```

### 4. Constructor Functions
```javascript
function Car(brand) {
    this.brand = brand;
}

let myCar = new Car("Toyota");
console.log(myCar.brand);  // Toyota
```

### 5. Explicit Binding
```javascript
let person1 = {name: "Alice"};
let person2 = {name: "Bob"};

function introduce() {
    return `I'm ${this.name}`;
}

console.log(introduce.call(person1));   // I'm Alice
console.log(introduce.apply(person2));  // I'm Bob

let boundFunc = introduce.bind(person1);
console.log(boundFunc());  // I'm Alice
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this",
        "points": 1,
        "answers": [
            {"text": "The current object", "is_correct": True},
            {"text": "The window object only", "is_correct": False},
            {"text": "The parent function", "is_correct": False},
            {"text": "Always undefined", "is_correct": False},
        ],
    },
    {
        "text": "What is a closure in JavaScript?",
        "explanation": """# Closures in JavaScript

A **closure** is a function that has access to variables from its outer (enclosing) scope, even after the outer function has finished executing.

## How Closures Work:

### 1. Basic Closure
```javascript
function outer() {
    let count = 0;
    
    function inner() {
        count++;
        return count;
    }
    
    return inner;
}

let counter = outer();
console.log(counter());  // 1
console.log(counter());  // 2
console.log(counter());  // 3
```

### 2. Private Variables
```javascript
function createBankAccount(initialBalance) {
    let balance = initialBalance;  // Private variable
    
    return {
        deposit: function(amount) {
            balance += amount;
            return balance;
        },
        withdraw: function(amount) {
            if (amount <= balance) {
                balance -= amount;
                return balance;
            }
            return "Insufficient funds";
        },
        getBalance: function() {
            return balance;
        }
    };
}

let account = createBankAccount(100);
console.log(account.deposit(50));     // 150
console.log(account.withdraw(30));    // 120
console.log(account.getBalance());    // 120
// console.log(account.balance);      // undefined (private)
```

### 3. Loop Closure Problem
```javascript
// Problem: All functions share same 'i'
for (var i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 3, 3, 3
    }, 1000);
}

// Solution 1: Use let (block scoped)
for (let i = 0; i < 3; i++) {
    setTimeout(function() {
        console.log(i);  // 0, 1, 2
    }, 1000);
}

// Solution 2: IIFE (Immediately Invoked Function Expression)
for (var i = 0; i < 3; i++) {
    (function(j) {
        setTimeout(function() {
            console.log(j);  // 0, 1, 2
        }, 1000);
    })(i);
}
```

### 4. Function Factory
```javascript
function createMultiplier(multiplier) {
    return function(num) {
        return num * multiplier;
    };
}

let double = createMultiplier(2);
let triple = createMultiplier(3);

console.log(double(5));  // 10
console.log(triple(5));  // 15
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures",
        "points": 1,
        "answers": [
            {"text": "A function with access to outer scope variables", "is_correct": True},
            {"text": "A way to close a file", "is_correct": False},
            {"text": "A method to end a loop", "is_correct": False},
            {"text": "A type of object", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the 'map()' method in JavaScript?",
        "explanation": """# Array map() Method in JavaScript

**map()** creates a new array by applying a function to each element of the original array.

## map() Characteristics:
- Returns a new array
- Doesn't modify original array
- Transforms each element

## Examples:

### 1. Basic Transformation
```javascript
let numbers = [1, 2, 3, 4, 5];
let doubled = numbers.map(num => num * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]
console.log(numbers);  // [1, 2, 3, 4, 5] (unchanged)
```

### 2. Transform Objects
```javascript
let users = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30}
];

let names = users.map(user => user.name);
console.log(names);  // ["Alice", "Bob"]

let agesInMonths = users.map(user => ({
    name: user.name,
    ageInMonths: user.age * 12
}));
console.log(agesInMonths);
// [{name: "Alice", ageInMonths: 300}, {name: "Bob", ageInMonths: 360}]
```

### 3. With Index
```javascript
let fruits = ["apple", "banana", "orange"];
let indexed = fruits.map((fruit, index) => `${index + 1}. ${fruit}`);
console.log(indexed);  // ["1. apple", "2. banana", "3. orange"]
```

### 4. String Operations
```javascript
let words = ["hello", "world", "javascript"];
let uppercase = words.map(word => word.toUpperCase());
console.log(uppercase);  // ["HELLO", "WORLD", "JAVASCRIPT"]

let lengths = words.map(word => word.length);
console.log(lengths);  // [5, 5, 10]
```

### 5. Chaining Methods
```javascript
let numbers = [1, 2, 3, 4, 5];
let result = numbers
    .filter(num => num > 2)     // [3, 4, 5]
    .map(num => num * 2)        // [6, 8, 10]
    .reduce((sum, num) => sum + num, 0);  // 24

console.log(result);  // 24
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map",
        "points": 1,
        "answers": [
            {"text": "To create a new transformed array", "is_correct": True},
            {"text": "To find a specific element", "is_correct": False},
            {"text": "To sort an array", "is_correct": False},
            {"text": "To remove elements", "is_correct": False},
        ],
    },
    {
        "text": "What does 'NaN' stand for in JavaScript?",
        "explanation": """# NaN (Not-a-Number) in JavaScript

**NaN** represents a value that is not a valid number, resulting from invalid mathematical operations.

## NaN Characteristics:
- Type is "number"
- Not equal to itself
- Indicates failed numeric operation

## Examples:

### 1. Operations Producing NaN
```javascript
console.log(0 / 0);              // NaN
console.log(parseInt("hello"));  // NaN
console.log(Math.sqrt(-1));      // NaN
console.log("text" - 5);         // NaN
console.log(undefined + 5);      // NaN
```

### 2. Type of NaN
```javascript
console.log(typeof NaN);         // "number"
console.log(NaN === NaN);        // false (unique property!)
console.log(NaN == NaN);         // false
```

### 3. Checking for NaN
```javascript
let result = 0 / 0;

// Wrong way
console.log(result === NaN);     // false (doesn't work!)

// Correct ways
console.log(Number.isNaN(result));     // true (recommended)
console.log(isNaN(result));            // true

// Difference between isNaN and Number.isNaN
console.log(isNaN("hello"));           // true (coerces to number first)
console.log(Number.isNaN("hello"));    // false (strict check)
```

### 4. NaN Propagation
```javascript
let x = NaN;
console.log(x + 5);    // NaN
console.log(x * 2);    // NaN
console.log(x / 10);   // NaN

// NaN spreads through calculations
let a = parseInt("abc");
let b = a + 10;
let c = b * 2;
console.log(c);  // NaN
```

### 5. Handling NaN
```javascript
function safeDivide(a, b) {
    let result = a / b;
    return Number.isNaN(result) ? 0 : result;
}

console.log(safeDivide(10, 2));   // 5
console.log(safeDivide(0, 0));    // 0 (instead of NaN)

// Parse with fallback
let userInput = "abc";
let age = parseInt(userInput) || 0;
console.log(age);  // 0
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN",
        "points": 1,
        "answers": [
            {"text": "Not a Number", "is_correct": True},
            {"text": "Negative and Null", "is_correct": False},
            {"text": "Null and None", "is_correct": False},
            {"text": "New Array Number", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between 'let', 'const', and 'var'?",
        "explanation": """# Variable Declaration Keywords in JavaScript

**var** is function-scoped and hoisted, **let** is block-scoped and can be reassigned, **const** is block-scoped and cannot be reassigned.

## Key Differences:

### 1. Scope Differences
```javascript
// var: function scoped
function testVar() {
    if (true) {
        var x = 10;
    }
    console.log(x);  // 10 (accessible outside block)
}

// let: block scoped
function testLet() {
    if (true) {
        let y = 10;
    }
    // console.log(y);  // ReferenceError: y is not defined
}

// const: block scoped
function testConst() {
    if (true) {
        const z = 10;
    }
    // console.log(z);  // ReferenceError: z is not defined
}
```

### 2. Reassignment
```javascript
// var and let can be reassigned
var a = 1;
a = 2;  // OK

let b = 1;
b = 2;  // OK

// const cannot be reassigned
const c = 1;
// c = 2;  // TypeError: Assignment to constant variable

// But const objects/arrays can be mutated
const arr = [1, 2, 3];
arr.push(4);  // OK - modifying content
console.log(arr);  // [1, 2, 3, 4]

const obj = {name: "Alice"};
obj.age = 25;  // OK - adding property
console.log(obj);  // {name: "Alice", age: 25}
```

### 3. Hoisting
```javascript
// var is hoisted with undefined
console.log(x);  // undefined (hoisted)
var x = 5;

// let and const are hoisted but not initialized (TDZ)
// console.log(y);  // ReferenceError: Cannot access before initialization
let y = 10;

// console.log(z);  // ReferenceError
const z = 15;
```

### 4. Loop Behavior
```javascript
// var problem in loops
for (var i = 0; i < 3; i++) {
    setTimeout(() => console.log(i), 100);
}
// Output: 3, 3, 3 (all functions share same 'i')

// let solution
for (let j = 0; j < 3; j++) {
    setTimeout(() => console.log(j), 100);
}
// Output: 0, 1, 2 (each iteration has own 'j')
```

### 5. Best Practices
```javascript
// Use const by default
const API_URL = "https://api.example.com";
const MAX_RETRIES = 3;

// Use let when you need to reassign
let counter = 0;
counter++;

// Avoid var in modern JavaScript
// var oldStyle = "avoid";  // Don't use

// const for objects and arrays you'll mutate
const users = [];
users.push({name: "Alice"});

const config = {theme: "dark"};
config.language = "en";
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "var is function-scoped, let and const are block-scoped", "is_correct": True},
            {"text": "Only syntax difference", "is_correct": False},
            {"text": "var is faster", "is_correct": False},
        ],
    },
    {
        "text": "What is an arrow function in JavaScript?",
        "explanation": """# Arrow Functions in JavaScript

**Arrow functions** are a shorter syntax for writing functions, introduced in ES6, with lexical 'this' binding.

## Arrow Function Syntax:

### 1. Basic Syntax
```javascript
// Traditional function
function add(a, b) {
    return a + b;
}

// Arrow function
const add = (a, b) => {
    return a + b;
};

// Concise arrow function (implicit return)
const add = (a, b) => a + b;

console.log(add(3, 4));  // 7
```

### 2. Different Syntaxes
```javascript
// No parameters
const greet = () => "Hello!";

// One parameter (parentheses optional)
const square = x => x * x;
const double = (x) => x * 2;

// Multiple parameters
const multiply = (a, b) => a * b;

// Multiple statements (need explicit return)
const calculate = (a, b) => {
    let sum = a + b;
    let product = a * b;
    return {sum, product};
};
```

### 3. Lexical 'this'
```javascript
// Traditional function has its own 'this'
let person = {
    name: "Alice",
    hobbies: ["reading", "coding"],
    showHobbies: function() {
        this.hobbies.forEach(function(hobby) {
            // 'this' is undefined in strict mode
            // console.log(this.name + " likes " + hobby);
        });
    }
};

// Arrow function inherits 'this' from parent scope
let person2 = {
    name: "Bob",
    hobbies: ["gaming", "music"],
    showHobbies: function() {
        this.hobbies.forEach(hobby => {
            console.log(`${this.name} likes ${hobby}`);
        });
    }
};

person2.showHobbies();
// Bob likes gaming
// Bob likes music
```

### 4. Returning Objects
```javascript
// Need parentheses to return object literal
const createPerson = (name, age) => ({name, age});

console.log(createPerson("Charlie", 30));
// {name: "Charlie", age: 30}

// Without parentheses - error!
// const bad = (name, age) => {name, age};  // Syntax error
```

### 5. Array Methods with Arrow Functions
```javascript
let numbers = [1, 2, 3, 4, 5];

// map
let doubled = numbers.map(n => n * 2);
console.log(doubled);  // [2, 4, 6, 8, 10]

// filter
let evens = numbers.filter(n => n % 2 === 0);
console.log(evens);  // [2, 4]

// reduce
let sum = numbers.reduce((acc, n) => acc + n, 0);
console.log(sum);  // 15
```

### 6. Limitations
```javascript
// Cannot be used as constructors
const Person = (name) => {
    this.name = name;
};
// new Person("Alice");  // TypeError: Person is not a constructor

// No arguments object
const showArgs = () => {
    // console.log(arguments);  // ReferenceError
};

// Use rest parameters instead
const showArgs2 = (...args) => {
    console.log(args);
};
showArgs2(1, 2, 3);  // [1, 2, 3]
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions",
        "points": 1,
        "answers": [
            {"text": "A shorter syntax for functions with lexical 'this'", "is_correct": True},
            {"text": "A function that draws arrows", "is_correct": False},
            {"text": "A pointer function", "is_correct": False},
            {"text": "An async function", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'filter()' method do in JavaScript?",
        "explanation": """# Array filter() Method in JavaScript

**filter()** creates a new array with elements that pass a test function, returning true/false for each element.

## filter() Characteristics:
- Returns new array
- Doesn't modify original
- Includes elements where callback returns true

## Examples:

### 1. Basic Filtering
```javascript
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// Get even numbers
let evens = numbers.filter(num => num % 2 === 0);
console.log(evens);  // [2, 4, 6, 8, 10]

// Get numbers greater than 5
let large = numbers.filter(num => num > 5);
console.log(large);  // [6, 7, 8, 9, 10]
```

### 2. Filter Objects
```javascript
let users = [
    {name: "Alice", age: 25, active: true},
    {name: "Bob", age: 30, active: false},
    {name: "Charlie", age: 35, active: true},
    {name: "Dave", age: 28, active: true}
];

// Get active users
let activeUsers = users.filter(user => user.active);
console.log(activeUsers);
// [{name: "Alice", ...}, {name: "Charlie", ...}, {name: "Dave", ...}]

// Get users over 30
let over30 = users.filter(user => user.age > 30);
console.log(over30);  // [{name: "Charlie", age: 35, active: true}]
```

### 3. Remove Falsy Values
```javascript
let mixed = [0, 1, false, 2, "", 3, null, undefined, 4, NaN, 5];

// Remove all falsy values
let truthy = mixed.filter(Boolean);
console.log(truthy);  // [1, 2, 3, 4, 5]

// Or explicit function
let truthy2 = mixed.filter(item => item);
console.log(truthy2);  // [1, 2, 3, 4, 5]
```

### 4. String Filtering
```javascript
let words = ["apple", "banana", "apricot", "cherry", "avocado"];

// Words starting with 'a'
let aWords = words.filter(word => word.startsWith('a'));
console.log(aWords);  // ["apple", "apricot", "avocado"]

// Words longer than 6 characters
let longWords = words.filter(word => word.length > 6);
console.log(longWords);  // ["apricot", "avocado"]
```

### 5. Remove Duplicates
```javascript
let numbers = [1, 2, 3, 2, 4, 3, 5, 1];

// Keep only first occurrence
let unique = numbers.filter((num, index, arr) => {
    return arr.indexOf(num) === index;
});
console.log(unique);  // [1, 2, 3, 4, 5]

// Or use Set
let unique2 = [...new Set(numbers)];
console.log(unique2);  // [1, 2, 3, 4, 5]
```

### 6. Complex Conditions
```javascript
let products = [
    {name: "Laptop", price: 1000, inStock: true},
    {name: "Phone", price: 500, inStock: false},
    {name: "Tablet", price: 300, inStock: true},
    {name: "Monitor", price: 200, inStock: true}
];

// Available products under $400
let affordable = products.filter(p => p.price < 400 && p.inStock);
console.log(affordable);
// [{name: "Tablet", ...}, {name: "Monitor", ...}]
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter",
        "points": 1,
        "answers": [
            {"text": "Creates a new array with elements that pass a test", "is_correct": True},
            {"text": "Sorts the array", "is_correct": False},
            {"text": "Removes all elements", "is_correct": False},
            {"text": "Merges two arrays", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of 'async/await' in JavaScript?",
        "explanation": """# Async/Await in JavaScript

**async/await** provides a cleaner syntax for handling asynchronous operations, making async code look synchronous.

## Async/Await Basics:

### 1. Basic Syntax
```javascript
// Traditional Promise
function fetchData() {
    return fetch('https://api.example.com/data')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error(error));
}

// With async/await
async function fetchData() {
    try {
        let response = await fetch('https://api.example.com/data');
        let data = await response.json();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}
```

### 2. Async Functions Always Return Promise
```javascript
async function getName() {
    return "Alice";  // Wrapped in Promise.resolve()
}

getName().then(name => console.log(name));  // Alice

// Equivalent to:
function getName2() {
    return Promise.resolve("Alice");
}
```

### 3. Await Pauses Execution
```javascript
async function example() {
    console.log("Start");
    
    // Wait for promise to resolve
    let result = await new Promise(resolve => {
        setTimeout(() => resolve("Done"), 2000);
    });
    
    console.log(result);  // After 2 seconds
    console.log("End");
}

example();
// Output:
// Start
// (2 second pause)
// Done
// End
```

### 4. Error Handling
```javascript
async function riskyOperation() {
    try {
        let data = await fetchFromAPI();
        let processed = await processData(data);
        return processed;
    } catch (error) {
        console.error("Error:", error.message);
        return null;
    }
}

// Alternative: catch at call site
riskyOperation()
    .then(result => console.log(result))
    .catch(error => console.error(error));
```

### 5. Parallel Execution
```javascript
// Sequential (slow)
async function sequential() {
    let user = await fetchUser();        // 1 second
    let posts = await fetchPosts();      // 1 second
    let comments = await fetchComments(); // 1 second
    return {user, posts, comments};      // Total: 3 seconds
}

// Parallel (fast)
async function parallel() {
    let [user, posts, comments] = await Promise.all([
        fetchUser(),
        fetchPosts(),
        fetchComments()
    ]);
    return {user, posts, comments};  // Total: 1 second
}
```

### 6. Real-World Example
```javascript
async function getUserData(userId) {
    try {
        // Fetch user
        let userResponse = await fetch(`/api/users/${userId}`);
        if (!userResponse.ok) {
            throw new Error("User not found");
        }
        let user = await userResponse.json();
        
        // Fetch user's posts
        let postsResponse = await fetch(`/api/users/${userId}/posts`);
        let posts = await postsResponse.json();
        
        return {
            user: user,
            posts: posts,
            postCount: posts.length
        };
    } catch (error) {
        console.error("Failed to fetch user data:", error);
        return null;
    }
}

// Usage
let data = await getUserData(123);
console.log(data);
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function",
        "points": 1,
        "answers": [
            {"text": "To handle asynchronous operations with cleaner syntax", "is_correct": True},
            {"text": "To make code run faster", "is_correct": False},
            {"text": "To create loops", "is_correct": False},
            {"text": "To define variables", "is_correct": False},
        ],
    },
    {
        "text": "What is the spread operator (...) used for in JavaScript?",
        "explanation": """# Spread Operator in JavaScript

The **spread operator (...)** expands iterables (arrays, objects, strings) into individual elements.

## Spread Operator Uses:

### 1. Array Spreading
```javascript
// Copy array
let original = [1, 2, 3];
let copy = [...original];
console.log(copy);  // [1, 2, 3]

// Combine arrays
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
let combined = [...arr1, ...arr2];
console.log(combined);  // [1, 2, 3, 4, 5, 6]

// Insert in middle
let middle = [...arr1, 10, ...arr2];
console.log(middle);  // [1, 2, 3, 10, 4, 5, 6]
```

### 2. Object Spreading
```javascript
// Copy object
let person = {name: "Alice", age: 25};
let personCopy = {...person};
console.log(personCopy);  // {name: "Alice", age: 25}

// Merge objects
let defaults = {theme: "light", language: "en"};
let userSettings = {language: "es", fontSize: 14};
let settings = {...defaults, ...userSettings};
console.log(settings);
// {theme: "light", language: "es", fontSize: 14}

// Override properties
let updated = {...person, age: 26, city: "NYC"};
console.log(updated);
// {name: "Alice", age: 26, city: "NYC"}
```

### 3. Function Arguments
```javascript
// Pass array elements as arguments
function sum(a, b, c) {
    return a + b + c;
}

let numbers = [1, 2, 3];
console.log(sum(...numbers));  // 6

// Math functions
let scores = [85, 92, 78, 95, 88];
console.log(Math.max(...scores));  // 95
console.log(Math.min(...scores));  // 78
```

### 4. String to Array
```javascript
let text = "Hello";
let chars = [...text];
console.log(chars);  // ['H', 'e', 'l', 'l', 'o']

// Remove duplicates
let str = "Mississippi";
let unique = [...new Set(str)];
console.log(unique.join(''));  // "Misp"
```

### 5. Rest Parameters (Similar Syntax)
```javascript
// Collect remaining parameters
function multiply(multiplier, ...numbers) {
    return numbers.map(n => n * multiplier);
}

console.log(multiply(2, 1, 2, 3));  // [2, 4, 6]

// Destructuring with rest
let [first, second, ...rest] = [1, 2, 3, 4, 5];
console.log(first);   // 1
console.log(second);  // 2
console.log(rest);    // [3, 4, 5]

let {name, ...others} = {name: "Bob", age: 30, city: "LA"};
console.log(name);    // "Bob"
console.log(others);  // {age: 30, city: "LA"}
```

### 6. Practical Examples
```javascript
// Add item to array immutably
let items = [1, 2, 3];
let newItems = [...items, 4];  // Don't modify original

// Remove item immutably
let filtered = items.filter(item => item !== 2);
let withSpread = [...items.slice(0, 1), ...items.slice(2)];

// Clone nested structures (shallow)
let nested = {
    user: {name: "Alice"},
    scores: [1, 2, 3]
};
let shallowCopy = {...nested};
// Note: nested.scores is still referenced, not copied deep
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax",
        "points": 1,
        "answers": [
            {"text": "To expand iterables into individual elements", "is_correct": True},
            {"text": "To perform division", "is_correct": False},
            {"text": "To create comments", "is_correct": False},
            {"text": "To declare variables", "is_correct": False},
        ],
    },
    {
        "text": "What is destructuring in JavaScript?",
        "explanation": """# Destructuring in JavaScript

**Destructuring** is a syntax for extracting values from arrays or properties from objects into distinct variables.

## Destructuring Syntax:

### 1. Array Destructuring
```javascript
// Basic array destructuring
let [a, b, c] = [1, 2, 3];
console.log(a);  // 1
console.log(b);  // 2
console.log(c);  // 3

// Skip elements
let [first, , third] = [1, 2, 3];
console.log(first);  // 1
console.log(third);  // 3

// Rest operator
let [head, ...tail] = [1, 2, 3, 4, 5];
console.log(head);  // 1
console.log(tail);  // [2, 3, 4, 5]
```

### 2. Object Destructuring
```javascript
// Basic object destructuring
let person = {name: "Alice", age: 25, city: "NYC"};
let {name, age, city} = person;
console.log(name);  // Alice
console.log(age);   // 25

// Rename variables
let {name: fullName, age: years} = person;
console.log(fullName);  // Alice
console.log(years);     // 25

// Default values
let {name, country = "USA"} = person;
console.log(country);  // USA
```

### 3. Nested Destructuring
```javascript
let user = {
    id: 1,
    name: "Bob",
    address: {
        city: "Boston",
        zip: "02101"
    }
};

// Nested destructuring
let {
    name,
    address: {city, zip}
} = user;

console.log(name);  // Bob
console.log(city);  // Boston
console.log(zip);   // 02101
```

### 4. Function Parameters
```javascript
// Destructure in function params
function greet({name, age}) {
    console.log(`${name} is ${age} years old`);
}

greet({name: "Charlie", age: 30});
// Charlie is 30 years old

// With defaults
function createUser({name, role = "user", active = true}) {
    return {name, role, active};
}

console.log(createUser({name: "Dave"}));
// {name: "Dave", role: "user", active: true}
```

### 5. Array Return Values
```javascript
function getCoordinates() {
    return [40.7128, -74.0060];
}

let [latitude, longitude] = getCoordinates();
console.log(latitude);   // 40.7128
console.log(longitude);  // -74.0060

// Object return values
function getUserInfo() {
    return {
        name: "Eve",
        email: "eve@example.com"
    };
}

let {name, email} = getUserInfo();
console.log(name);   // Eve
console.log(email);  // eve@example.com
```

### 6. Swapping Variables
```javascript
// Swap without temp variable
let x = 1;
let y = 2;
[x, y] = [y, x];
console.log(x);  // 2
console.log(y);  // 1

// Multiple swaps
let [a, b, c] = [1, 2, 3];
[a, b, c] = [c, a, b];
console.log(a, b, c);  // 3, 1, 2
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment",
        "points": 1,
        "answers": [
            {"text": "Extracting values from arrays/objects into variables", "is_correct": True},
            {"text": "Deleting properties from objects", "is_correct": False},
            {"text": "Breaking loops", "is_correct": False},
            {"text": "Removing array elements", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the 'reduce()' method in JavaScript?",
        "explanation": """# Array reduce() Method in JavaScript

**reduce()** executes a reducer function on each array element, returning a single accumulated value.

## reduce() Syntax:
```javascript
array.reduce((accumulator, currentValue, index, array) => {
    // return updated accumulator
}, initialValue);
```

## Examples:

### 1. Sum Array Elements
```javascript
let numbers = [1, 2, 3, 4, 5];

let sum = numbers.reduce((acc, num) => acc + num, 0);
console.log(sum);  // 15

// Step by step:
// acc=0, num=1 => 0+1=1
// acc=1, num=2 => 1+2=3
// acc=3, num=3 => 3+3=6
// acc=6, num=4 => 6+4=10
// acc=10, num=5 => 10+5=15
```

### 2. Find Maximum/Minimum
```javascript
let numbers = [5, 2, 9, 1, 7];

let max = numbers.reduce((acc, num) => Math.max(acc, num));
console.log(max);  // 9

let min = numbers.reduce((acc, num) => Math.min(acc, num));
console.log(min);  // 1

// Or simpler:
let max2 = Math.max(...numbers);  // 9
```

### 3. Count Occurrences
```javascript
let fruits = ["apple", "banana", "apple", "orange", "banana", "apple"];

let count = fruits.reduce((acc, fruit) => {
    acc[fruit] = (acc[fruit] || 0) + 1;
    return acc;
}, {});

console.log(count);
// {apple: 3, banana: 2, orange: 1}
```

### 4. Group By Property
```javascript
let people = [
    {name: "Alice", age: 25},
    {name: "Bob", age: 30},
    {name: "Charlie", age: 25},
    {name: "Dave", age: 30}
];

let grouped = people.reduce((acc, person) => {
    let age = person.age;
    if (!acc[age]) {
        acc[age] = [];
    }
    acc[age].push(person);
    return acc;
}, {});

console.log(grouped);
// {
//   25: [{name: "Alice", age: 25}, {name: "Charlie", age: 25}],
//   30: [{name: "Bob", age: 30}, {name: "Dave", age: 30}]
// }
```

### 5. Flatten Array
```javascript
let nested = [[1, 2], [3, 4], [5, 6]];

let flattened = nested.reduce((acc, arr) => acc.concat(arr), []);
console.log(flattened);  // [1, 2, 3, 4, 5, 6]

// Or use flat()
let flattened2 = nested.flat();  // [1, 2, 3, 4, 5, 6]
```

### 6. Create Object from Array
```javascript
let users = [
    {id: 1, name: "Alice"},
    {id: 2, name: "Bob"},
    {id: 3, name: "Charlie"}
];

let userMap = users.reduce((acc, user) => {
    acc[user.id] = user.name;
    return acc;
}, {});

console.log(userMap);
// {1: "Alice", 2: "Bob", 3: "Charlie"}
```

### 7. Pipeline/Compose Functions
```javascript
let numbers = [1, 2, 3, 4, 5];

// Apply multiple transformations
let result = numbers
    .filter(n => n > 2)
    .reduce((acc, n) => acc + (n * 2), 0);

console.log(result);  // (3*2) + (4*2) + (5*2) = 24
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce",
        "points": 1,
        "answers": [
            {"text": "To reduce array to a single accumulated value", "is_correct": True},
            {"text": "To remove elements from array", "is_correct": False},
            {"text": "To sort the array", "is_correct": False},
            {"text": "To make the array smaller", "is_correct": False},
        ],
    },
    {
        "text": "What is event delegation in JavaScript?",
        "explanation": """# Event Delegation in JavaScript

**Event delegation** is a technique where you attach a single event listener to a parent element to handle events for multiple child elements.

## How Event Delegation Works:

### 1. Without Event Delegation (Inefficient)
```javascript
// Add listener to each button
document.querySelectorAll('.button').forEach(button => {
    button.addEventListener('click', function() {
        console.log('Button clicked:', this.textContent);
    });
});

// Problem: Many event listeners, must update when DOM changes
```

### 2. With Event Delegation (Efficient)
```javascript
// Add single listener to parent
document.getElementById('button-container').addEventListener('click', function(e) {
    if (e.target.classList.contains('button')) {
        console.log('Button clicked:', e.target.textContent);
    }
});

// Benefits: One listener, works with dynamically added buttons
```

### 3. Event Bubbling
```javascript
// Events bubble up from child to parent
<div id="parent">
    <div id="child">
        <button id="button">Click me</button>
    </div>
</div>

document.getElementById('parent').addEventListener('click', function(e) {
    console.log('Clicked element:', e.target.id);
    console.log('Event attached to:', e.currentTarget.id);
});

// Clicking button logs:
// Clicked element: button (e.target)
// Event attached to: parent (e.currentTarget)
```

### 4. Practical Example - Todo List
```javascript
// HTML
<ul id="todo-list">
    <li><button class="delete">Delete</button> Task 1</li>
    <li><button class="delete">Delete</button> Task 2</li>
</ul>

// Event delegation
document.getElementById('todo-list').addEventListener('click', function(e) {
    if (e.target.classList.contains('delete')) {
        let listItem = e.target.parentElement;
        listItem.remove();
    }
});

// Add new todo dynamically (delegation still works!)
function addTodo(text) {
    let li = document.createElement('li');
    li.innerHTML = `<button class="delete">Delete</button> ${text}`;
    document.getElementById('todo-list').appendChild(li);
}

addTodo('Task 3');  // Delete button will work automatically
```

### 5. Table Row Example
```javascript
// HTML
<table id="data-table">
    <tr><td>Row 1</td><td><button class="edit">Edit</button></td></tr>
    <tr><td>Row 2</td><td><button class="edit">Edit</button></td></tr>
</table>

// Delegate to table
document.getElementById('data-table').addEventListener('click', function(e) {
    if (e.target.classList.contains('edit')) {
        let row = e.target.closest('tr');
        let rowData = row.cells[0].textContent;
        console.log('Editing:', rowData);
    }
});
```

### 6. Multiple Event Types
```javascript
let container = document.getElementById('container');

// Handle different elements
container.addEventListener('click', function(e) {
    // Handle buttons
    if (e.target.matches('.btn-save')) {
        console.log('Save clicked');
    }
    
    // Handle links
    if (e.target.matches('a.nav-link')) {
        e.preventDefault();
        console.log('Navigation:', e.target.href);
    }
    
    // Handle checkboxes
    if (e.target.matches('input[type="checkbox"]')) {
        console.log('Checkbox:', e.target.checked);
    }
});
```

### 7. Benefits
```javascript
// ✓ Better performance (fewer listeners)
// ✓ Works with dynamically added elements
// ✓ Less memory usage
// ✓ Simpler code maintenance

// When to use:
// - Many similar elements
// - Dynamic content
// - Repeated patterns

// When not to use:
// - Events that don't bubble (focus, blur)
// - Unique event handlers per element
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Events#event_delegation",
        "points": 1,
        "answers": [
            {"text": "Attaching a listener to parent to handle child events", "is_correct": True},
            {"text": "Delegating tasks to other functions", "is_correct": False},
            {"text": "Removing event listeners", "is_correct": False},
            {"text": "Creating custom events", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between 'null' and 'undefined' in JavaScript?",
        "explanation": """# null vs undefined in JavaScript

**undefined** means a variable has been declared but not assigned a value, while **null** is an intentional absence of value.

## Key Differences:

### 1. Basic Definitions
```javascript
// undefined: variable declared but not assigned
let x;
console.log(x);  // undefined
console.log(typeof x);  // "undefined"

// null: intentional absence of value
let y = null;
console.log(y);  // null
console.log(typeof y);  // "object" (known JavaScript quirk!)
```

### 2. Default Values
```javascript
// Function parameters default to undefined
function greet(name) {
    console.log(name);
}
greet();  // undefined

// Object properties that don't exist
let person = {name: "Alice"};
console.log(person.age);  // undefined

// Array elements not yet assigned
let arr = new Array(3);
console.log(arr[0]);  // undefined
```

### 3. Intentional Assignment
```javascript
// undefined - variable exists but no value
let notAssigned;
console.log(notAssigned);  // undefined

// null - explicitly set to no value
let intentionallyEmpty = null;
console.log(intentionallyEmpty);  // null

// Use case: reset a value
let user = {name: "Bob"};
user = null;  // Clear the reference
```

### 4. Type Checking
```javascript
let a;
let b = null;

console.log(typeof a);  // "undefined"
console.log(typeof b);  // "object" (quirk!)

// Proper null check
console.log(b === null);  // true

// Check for both
console.log(a == null);   // true (loose equality)
console.log(b == null);   // true
console.log(a === null);  // false (strict equality)
console.log(b === undefined);  // false
```

### 5. Comparisons
```javascript
console.log(null == undefined);   // true (loose equality)
console.log(null === undefined);  // false (strict equality)

console.log(null == 0);   // false
console.log(null == "");  // false
console.log(null == false);  // false

console.log(undefined == 0);   // false
console.log(undefined == "");  // false
console.log(undefined == false);  // false
```

### 6. Practical Usage
```javascript
// Function returns undefined if nothing returned
function doNothing() {
    // no return statement
}
console.log(doNothing());  // undefined

// Use null to reset object references
let config = {theme: "dark"};
config = null;  // Clear config

// Check if variable was assigned
function process(value) {
    if (value === undefined) {
        console.log("No value provided");
    }
}

// Optional chaining with undefined
let user = {name: "Alice"};
console.log(user.address?.city);  // undefined (address doesn't exist)
```

### 7. Best Practices
```javascript
// Use undefined for default/missing values
function greet(name = "Guest") {  // name is undefined if not provided
    console.log(`Hello, ${name}`);
}

// Use null for intentional absence
let selectedItem = null;  // Nothing selected yet

function findUser(id) {
    // Return null if not found
    return users.find(u => u.id === id) || null;
}

// Check both with nullish coalescing
let value = potentiallyNullOrUndefined ?? "default";

// Use optional chaining
let cityName = user?.address?.city ?? "Unknown";
```""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null",
        "points": 1,
        "answers": [
            {"text": "undefined is unassigned, null is intentional absence", "is_correct": True},
            {"text": "They are the same", "is_correct": False},
            {"text": "null is for numbers only", "is_correct": False},
            {"text": "undefined is for objects only", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword declares a block-scoped variable that can be reassigned?",
        "explanation": """**let** is block-scoped and allows reassignment, unlike **const**, which cannot be reassigned.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let",
        "points": 1,
        "answers": [
            {"text": "var", "is_correct": False},
            {"text": "let", "is_correct": True},
            {"text": "const", "is_correct": False},
            {"text": "define", "is_correct": False},
        ],
    },
    {
        "text": "What will console.log('5' + 2) output?",
        "explanation": """With **+**, JavaScript performs string concatenation when one operand is a string.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition",
        "points": 1,
        "answers": [
            {"text": "7", "is_correct": False},
            {"text": "52", "is_correct": True},
            {"text": "5 2", "is_correct": False},
            {"text": "NaN", "is_correct": False},
        ],
    },
    {
        "text": "Which array method creates a new array with items that pass a test?",
        "explanation": """**filter()** returns a new array containing only elements that satisfy the callback test.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter",
        "points": 1,
        "answers": [
            {"text": "map()", "is_correct": False},
            {"text": "filter()", "is_correct": True},
            {"text": "reduce()", "is_correct": False},
            {"text": "forEach()", "is_correct": False},
        ],
    },
    {
        "text": "How do you declare a constant in JavaScript?",
        "explanation": """Use **const** to declare a block-scoped constant that cannot be reassigned.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const",
        "points": 1,
        "answers": [
            {"text": "let PI = 3.14;", "is_correct": False},
            {"text": "const PI = 3.14;", "is_correct": True},
            {"text": "var PI == 3.14;", "is_correct": False},
            {"text": "constant PI = 3.14;", "is_correct": False},
        ],
    },
    {
        "text": "What is the correct syntax for a template literal?",
        "explanation": """Template literals use backticks and `${}` for interpolation.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals",
        "points": 1,
        "answers": [
            {"text": "'Hello ${name}'", "is_correct": False},
            {"text": "`Hello ${name}`", "is_correct": True},
            {"text": "\"Hello ${name}\"", "is_correct": False},
            {"text": "Hello ${name}", "is_correct": False},
        ],
    },
    {
        "text": "Which method converts a JSON string to a JavaScript object?",
        "explanation": """**JSON.parse()** parses a JSON string into a JavaScript value or object.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/parse",
        "points": 1,
        "answers": [
            {"text": "JSON.stringify()", "is_correct": False},
            {"text": "JSON.parse()", "is_correct": True},
            {"text": "JSON.toObject()", "is_correct": False},
            {"text": "JSON.convert()", "is_correct": False},
        ],
    },
    {
        "text": "What does Array.isArray([]) return?",
        "explanation": """**Array.isArray()** checks whether a value is an array.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/isArray",
        "points": 1,
        "answers": [
            {"text": "true", "is_correct": True},
            {"text": "false", "is_correct": False},
            {"text": "undefined", "is_correct": False},
            {"text": "null", "is_correct": False},
        ],
    },
    {
        "text": "Which statement skips to the next iteration of a loop?",
        "explanation": """**continue** skips the rest of the current loop body and moves to the next iteration.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue",
        "points": 1,
        "answers": [
            {"text": "break", "is_correct": False},
            {"text": "return", "is_correct": False},
            {"text": "continue", "is_correct": True},
            {"text": "exit", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of typeof null?",
        "explanation": """Due to a historical quirk, **typeof null** returns **\"object\"**.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof",
        "points": 1,
        "answers": [
            {"text": "\"null\"", "is_correct": False},
            {"text": "\"undefined\"", "is_correct": False},
            {"text": "\"object\"", "is_correct": True},
            {"text": "\"number\"", "is_correct": False},
        ],
    },
    {
        "text": "Which method removes the last element of an array?",
        "explanation": """**pop()** removes the last element and returns it.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop",
        "points": 1,
        "answers": [
            {"text": "shift()", "is_correct": False},
            {"text": "pop()", "is_correct": True},
            {"text": "push()", "is_correct": False},
            {"text": "unshift()", "is_correct": False},
        ],
    },
    {
        "text": "What does console.log(Boolean('')) output?",
        "explanation": """An empty string is falsy, so **Boolean('')** returns **false**.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Glossary/Falsy",
        "points": 1,
        "answers": [
            {"text": "true", "is_correct": False},
            {"text": "false", "is_correct": True},
            {"text": "undefined", "is_correct": False},
            {"text": "null", "is_correct": False},
        ],
    },
    {
        "text": "Which method joins array elements into a string?",
        "explanation": """**join()** concatenates array elements into a single string.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join",
        "points": 1,
        "answers": [
            {"text": "concat()", "is_correct": False},
            {"text": "join()", "is_correct": True},
            {"text": "split()", "is_correct": False},
            {"text": "slice()", "is_correct": False},
        ],
    },
    {
        "text": "Which statement creates a block-scoped constant?",
        "explanation": """**const** creates a block-scoped binding that cannot be reassigned.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const",
        "points": 1,
        "answers": [
            {"text": "const x = 10;", "is_correct": True},
            {"text": "var x = 10;", "is_correct": False},
            {"text": "let x == 10;", "is_correct": False},
            {"text": "constant x = 10;", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for strict equality comparison?",
        "explanation": """**===** compares both value and type without coercion.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Strict_equality",
        "points": 1,
        "answers": [
            {"text": "==", "is_correct": False},
            {"text": "===", "is_correct": True},
            {"text": "=", "is_correct": False},
            {"text": "!=", "is_correct": False},
        ],
    },
    {
        "text": "What will console.log(2 ** 3) output?",
        "explanation": """** is the exponentiation operator; $2^3$ equals 8.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation",
        "points": 1,
        "answers": [
            {"text": "6", "is_correct": False},
            {"text": "8", "is_correct": True},
            {"text": "9", "is_correct": False},
            {"text": "23", "is_correct": False},
        ],
    },
    {
        "text": "Which method removes the first element of an array?",
        "explanation": """**shift()** removes the first element and returns it.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/shift",
        "points": 1,
        "answers": [
            {"text": "pop()", "is_correct": False},
            {"text": "shift()", "is_correct": True},
            {"text": "unshift()", "is_correct": False},
            {"text": "splice()", "is_correct": False},
        ],
    },
    {
        "text": "Which method adds one or more elements to the beginning of an array?",
        "explanation": """**unshift()** adds elements to the start and returns the new length.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/unshift",
        "points": 1,
        "answers": [
            {"text": "push()", "is_correct": False},
            {"text": "unshift()", "is_correct": True},
            {"text": "shift()", "is_correct": False},
            {"text": "concat()", "is_correct": False},
        ],
    },
    {
        "text": "What does Number('10') return?",
        "explanation": """**Number('10')** converts the string to the number 10.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number",
        "points": 1,
        "answers": [
            {"text": "\"10\"", "is_correct": False},
            {"text": "10", "is_correct": True},
            {"text": "NaN", "is_correct": False},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns the index of the first matching element in an array?",
        "explanation": """**indexOf()** returns the index of the first occurrence or -1 if not found.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf",
        "points": 1,
        "answers": [
            {"text": "find()", "is_correct": False},
            {"text": "indexOf()", "is_correct": True},
            {"text": "includes()", "is_correct": False},
            {"text": "lastIndexOf()", "is_correct": False},
        ],
    },
    {
        "text": "Which method creates a shallow copy of part of an array?",
        "explanation": """**slice()** returns a shallow copy of a portion of an array.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice",
        "points": 1,
        "answers": [
            {"text": "splice()", "is_correct": False},
            {"text": "slice()", "is_correct": True},
            {"text": "copyWithin()", "is_correct": False},
            {"text": "fill()", "is_correct": False},
        ],
    },
    {
        "text": "Which method removes or replaces elements in an array in place?",
        "explanation": """**splice()** changes the array by removing and/or adding elements.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice",
        "points": 1,
        "answers": [
            {"text": "slice()", "is_correct": False},
            {"text": "splice()", "is_correct": True},
            {"text": "map()", "is_correct": False},
            {"text": "filter()", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword declares a function-scoped variable?",
        "explanation": """**var** is function-scoped (unlike block-scoped **let** and **const**).""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var",
        "points": 1,
        "answers": [
            {"text": "var", "is_correct": True},
            {"text": "let", "is_correct": False},
            {"text": "const", "is_correct": False},
            {"text": "def", "is_correct": False},
        ],
    },
    {
        "text": "Which method checks if every array element passes a test?",
        "explanation": """**every()** returns true only if all elements satisfy the predicate.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/every",
        "points": 1,
        "answers": [
            {"text": "some()", "is_correct": False},
            {"text": "every()", "is_correct": True},
            {"text": "map()", "is_correct": False},
            {"text": "find()", "is_correct": False},
        ],
    },
    {
        "text": "Which method checks if at least one array element passes a test?",
        "explanation": """**some()** returns true if any element satisfies the predicate.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/some",
        "points": 1,
        "answers": [
            {"text": "some()", "is_correct": True},
            {"text": "every()", "is_correct": False},
            {"text": "filter()", "is_correct": False},
            {"text": "reduce()", "is_correct": False},
        ],
    },
    {
        "text": "Which method finds the first element that matches a condition?",
        "explanation": """**find()** returns the first element that satisfies the predicate.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find",
        "points": 1,
        "answers": [
            {"text": "find()", "is_correct": True},
            {"text": "filter()", "is_correct": False},
            {"text": "indexOf()", "is_correct": False},
            {"text": "includes()", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns a string with leading and trailing whitespace removed?",
        "explanation": """**trim()** removes whitespace from both ends of a string.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/trim",
        "points": 1,
        "answers": [
            {"text": "slice()", "is_correct": False},
            {"text": "trim()", "is_correct": True},
            {"text": "replace()", "is_correct": False},
            {"text": "split()", "is_correct": False},
        ],
    },
    {
        "text": "Which string method converts all characters to uppercase?",
        "explanation": """**toUpperCase()** returns a new string with uppercase letters.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toUpperCase",
        "points": 1,
        "answers": [
            {"text": "toUpperCase()", "is_correct": True},
            {"text": "toLowerCase()", "is_correct": False},
            {"text": "uppercase()", "is_correct": False},
            {"text": "capitalize()", "is_correct": False},
        ],
    },
    {
        "text": "Which global function can be used to parse an integer from a string?",
        "explanation": """**parseInt()** converts a string to an integer (if possible).""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt",
        "points": 1,
        "answers": [
            {"text": "parseInt()", "is_correct": True},
            {"text": "parseFloat()", "is_correct": False},
            {"text": "Number()", "is_correct": False},
            {"text": "toInteger()", "is_correct": False},
        ],
    },
    {
        "text": "What does JSON.stringify({a: 1}) return?",
        "explanation": """**JSON.stringify()** converts a JavaScript value to a JSON string.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON/stringify",
        "points": 1,
        "answers": [
            {"text": "{a: 1}", "is_correct": False},
            {"text": "\"{\\\"a\\\":1}\"", "is_correct": True},
            {"text": "[\"a\",1]", "is_correct": False},
            {"text": "\"a:1\"", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used to provide a default value for null or undefined?",
        "explanation": """The **nullish coalescing operator (??)** returns the right-hand value only for null or undefined.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing",
        "points": 1,
        "answers": [
            {"text": "||", "is_correct": False},
            {"text": "??", "is_correct": True},
            {"text": "&&", "is_correct": False},
            {"text": "?:", "is_correct": False},
        ],
    },
    {
        "text": "What does String(123) return?",
        "explanation": """**String(123)** converts the number 123 to the string \"123\".""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String",
        "points": 1,
        "answers": [
            {"text": "123", "is_correct": False},
            {"text": "\"123\"", "is_correct": True},
            {"text": "NaN", "is_correct": False},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for logical AND operation?",
        "explanation": """The **&&** operator returns true only if both operands are truthy.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND",
        "points": 1,
        "answers": [
            {"text": "||", "is_correct": False},
            {"text": "&&", "is_correct": True},
            {"text": "&", "is_correct": False},
            {"text": "and", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for logical OR operation?",
        "explanation": """The **||** operator returns true if at least one operand is truthy.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR",
        "points": 1,
        "answers": [
            {"text": "||", "is_correct": True},
            {"text": "&&", "is_correct": False},
            {"text": "|", "is_correct": False},
            {"text": "or", "is_correct": False},
        ],
    },
    {
        "text": "Which method converts a string to lowercase?",
        "explanation": """**toLowerCase()** returns a new string with all lowercase letters.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase",
        "points": 1,
        "answers": [
            {"text": "toLowerCase()", "is_correct": True},
            {"text": "toUpperCase()", "is_correct": False},
            {"text": "toLower()", "is_correct": False},
            {"text": "lowercase()", "is_correct": False},
        ],
    },
    {
        "text": "Which method checks if a string starts with a specific substring?",
        "explanation": """**startsWith()** returns true if the string begins with the specified substring.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/startsWith",
        "points": 1,
        "answers": [
            {"text": "startsWith()", "is_correct": True},
            {"text": "beginsWith()", "is_correct": False},
            {"text": "includes()", "is_correct": False},
            {"text": "indexOf()", "is_correct": False},
        ],
    },
    {
        "text": "Which method checks if a string ends with a specific substring?",
        "explanation": """**endsWith()** returns true if the string ends with the specified substring.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/endsWith",
        "points": 1,
        "answers": [
            {"text": "endsWith()", "is_correct": True},
            {"text": "finishes()", "is_correct": False},
            {"text": "includes()", "is_correct": False},
            {"text": "lastIndexOf()", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns the character at a specified index in a string?",
        "explanation": """**charAt()** returns the character at the specified index.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/charAt",
        "points": 1,
        "answers": [
            {"text": "charAt()", "is_correct": True},
            {"text": "getChar()", "is_correct": False},
            {"text": "characterAt()", "is_correct": False},
            {"text": "char()", "is_correct": False},
        ],
    },
    {
        "text": "Which method extracts a section of a string and returns a new string?",
        "explanation": """**substring()** or **slice()** extracts characters between two indices.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/substring",
        "points": 1,
        "answers": [
            {"text": "substring()", "is_correct": True},
            {"text": "extract()", "is_correct": False},
            {"text": "get()", "is_correct": False},
            {"text": "section()", "is_correct": False},
        ],
    },
    {
        "text": "Which method divides a string into an array based on a separator?",
        "explanation": """**split()** divides a string into an array of substrings.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split",
        "points": 1,
        "answers": [
            {"text": "split()", "is_correct": True},
            {"text": "divide()", "is_correct": False},
            {"text": "separate()", "is_correct": False},
            {"text": "toArray()", "is_correct": False},
        ],
    },
    {
        "text": "Which method replaces the first occurrence of a substring in a string?",
        "explanation": """**replace()** replaces the first match of a pattern in a string.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace",
        "points": 1,
        "answers": [
            {"text": "replace()", "is_correct": True},
            {"text": "replaceAll()", "is_correct": False},
            {"text": "substitute()", "is_correct": False},
            {"text": "swap()", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns the number of characters in a string?",
        "explanation": """The **length property** returns the number of characters in a string.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/length",
        "points": 1,
        "answers": [
            {"text": "length", "is_correct": True},
            {"text": "size", "is_correct": False},
            {"text": "count()", "is_correct": False},
            {"text": "getLength()", "is_correct": False},
        ],
    },
    {
        "text": "What will console.log(Math.max(5, 10, 3)) output?",
        "explanation": """**Math.max()** returns the largest number among the arguments.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max",
        "points": 1,
        "answers": [
            {"text": "5", "is_correct": False},
            {"text": "10", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "18", "is_correct": False},
        ],
    },
    {
        "text": "What will console.log(Math.min(5, 10, 3)) output?",
        "explanation": """**Math.min()** returns the smallest number among the arguments.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/min",
        "points": 1,
        "answers": [
            {"text": "5", "is_correct": False},
            {"text": "10", "is_correct": False},
            {"text": "3", "is_correct": True},
            {"text": "18", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns a random number between 0 (inclusive) and 1 (exclusive)?",
        "explanation": """**Math.random()** returns a random decimal between 0 and 1.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random",
        "points": 1,
        "answers": [
            {"text": "Math.random()", "is_correct": True},
            {"text": "Math.rand()", "is_correct": False},
            {"text": "random()", "is_correct": False},
            {"text": "Math.getRandom()", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns the absolute value of a number?",
        "explanation": """**Math.abs()** returns the absolute (positive) value of a number.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/abs",
        "points": 1,
        "answers": [
            {"text": "Math.abs()", "is_correct": True},
            {"text": "Math.absolute()", "is_correct": False},
            {"text": "absolute()", "is_correct": False},
            {"text": "Math.positive()", "is_correct": False},
        ],
    },
    {
        "text": "Which method rounds a number to the nearest integer?",
        "explanation": """**Math.round()** rounds to the nearest whole number.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/round",
        "points": 1,
        "answers": [
            {"text": "Math.round()", "is_correct": True},
            {"text": "Math.floor()", "is_correct": False},
            {"text": "Math.ceil()", "is_correct": False},
            {"text": "Math.trunc()", "is_correct": False},
        ],
    },
    {
        "text": "Which method rounds down to the nearest integer?",
        "explanation": """**Math.ceil()** rounds up, while **Math.floor()** rounds down.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/floor",
        "points": 1,
        "answers": [
            {"text": "Math.round()", "is_correct": False},
            {"text": "Math.floor()", "is_correct": True},
            {"text": "Math.ceil()", "is_correct": False},
            {"text": "Math.down()", "is_correct": False},
        ],
    },
    {
        "text": "Which method rounds up to the nearest integer?",
        "explanation": """**Math.ceil()** rounds up to the nearest whole number.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/ceil",
        "points": 1,
        "answers": [
            {"text": "Math.round()", "is_correct": False},
            {"text": "Math.floor()", "is_correct": False},
            {"text": "Math.ceil()", "is_correct": True},
            {"text": "Math.up()", "is_correct": False},
        ],
    },
    {
        "text": "What does the ternary operator ? : do?",
        "explanation": """The **ternary operator** is shorthand for if-else: `condition ? valueIfTrue : valueIfFalse`.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_operator",
        "points": 1,
        "answers": [
            {"text": "Creates a loop", "is_correct": False},
            {"text": "Provides conditional value selection", "is_correct": True},
            {"text": "Performs division", "is_correct": False},
            {"text": "Compares equality", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword is used to exit a function early?",
        "explanation": """**return** exits a function and optionally returns a value.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/return",
        "points": 1,
        "answers": [
            {"text": "exit", "is_correct": False},
            {"text": "return", "is_correct": True},
            {"text": "break", "is_correct": False},
            {"text": "stop", "is_correct": False},
        ],
    },
    {
        "text": "What does console.log(1 + '2') output?",
        "explanation": """With **+**, if one operand is a string, both are concatenated as strings: \"1\" + \"2\" = \"12\".""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Addition",
        "points": 1,
        "answers": [
            {"text": "3", "is_correct": False},
            {"text": "\"12\"", "is_correct": True},
            {"text": "\"3\"", "is_correct": False},
            {"text": "NaN", "is_correct": False},
        ],
    },
    {
        "text": "What does console.log('5' - 2) output?",
        "explanation": """The **-** operator forces type coercion to numbers: 5 - 2 = 3.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Subtraction",
        "points": 1,
        "answers": [
            {"text": "\"52\"", "is_correct": False},
            {"text": "3", "is_correct": True},
            {"text": "\"3\"", "is_correct": False},
            {"text": "NaN", "is_correct": False},
        ],
    },
    {
        "text": "Which method iterates over array elements without returning a new array?",
        "explanation": """**forEach()** executes a function for each array element but returns undefined.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach",
        "points": 1,
        "answers": [
            {"text": "forEach()", "is_correct": True},
            {"text": "map()", "is_correct": False},
            {"text": "filter()", "is_correct": False},
            {"text": "reduce()", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to execute code a certain number of times?",
        "explanation": """**for** loop repeats code a specified number of times.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for",
        "points": 1,
        "answers": [
            {"text": "if", "is_correct": False},
            {"text": "for", "is_correct": True},
            {"text": "switch", "is_correct": False},
            {"text": "while", "is_correct": False},
        ],
    },
    {
        "text": "Which statement repeats code as long as a condition is true?",
        "explanation": """**while** loop repeats code while a condition remains true.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while",
        "points": 1,
        "answers": [
            {"text": "for", "is_correct": False},
            {"text": "if", "is_correct": False},
            {"text": "while", "is_correct": True},
            {"text": "switch", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to make decisions based on conditions?",
        "explanation": """**if** statement executes code based on a boolean condition.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else",
        "points": 1,
        "answers": [
            {"text": "switch", "is_correct": False},
            {"text": "if", "is_correct": True},
            {"text": "for", "is_correct": False},
            {"text": "while", "is_correct": False},
        ],
    },
    {
        "text": "Which statement compares a value against multiple cases?",
        "explanation": """**switch** statement compares a value and executes code for matching cases.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch",
        "points": 1,
        "answers": [
            {"text": "if", "is_correct": False},
            {"text": "switch", "is_correct": True},
            {"text": "for", "is_correct": False},
            {"text": "while", "is_correct": False},
        ],
    },
    {
        "text": "Which method checks if a string contains a substring?",
        "explanation": """**includes()** checks if a string contains the specified substring.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/includes",
        "points": 1,
        "answers": [
            {"text": "contains()", "is_correct": False},
            {"text": "includes()", "is_correct": True},
            {"text": "indexOf()", "is_correct": False},
            {"text": "has()", "is_correct": False},
        ],
    },
    {
        "text": "What does console.log(!true) output?",
        "explanation": """The **logical NOT operator (!)** reverses the boolean: !true = false.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_NOT",
        "points": 1,
        "answers": [
            {"text": "true", "is_correct": False},
            {"text": "false", "is_correct": True},
            {"text": "undefined", "is_correct": False},
            {"text": "null", "is_correct": False},
        ],
    },
    {
        "text": "Which method repeats a string a specified number of times?",
        "explanation": """**repeat()** returns a new string with the original string repeated n times.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/repeat",
        "points": 1,
        "answers": [
            {"text": "repeat()", "is_correct": True},
            {"text": "duplicate()", "is_correct": False},
            {"text": "multiply()", "is_correct": False},
            {"text": "times()", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between Object.assign() and the spread operator?",
        "explanation": """Both perform shallow copies, but **Object.assign()** modifies the target object, while the spread operator creates a new object.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign",
        "points": 1,
        "answers": [
            {"text": "They do the same thing", "is_correct": False},
            {"text": "Object.assign() modifies target, spread creates new", "is_correct": True},
            {"text": "Spread operator modifies target", "is_correct": False},
            {"text": "Object.assign() creates new object", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns all keys of an object?",
        "explanation": """**Object.keys()** returns an array of the object's own property names.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys",
        "points": 1,
        "answers": [
            {"text": "Object.keys()", "is_correct": True},
            {"text": "Object.getKeys()", "is_correct": False},
            {"text": "Object.properties()", "is_correct": False},
            {"text": "Object.entries()", "is_correct": False},
        ],
    },
    {
        "text": "Which method returns all values of an object?",
        "explanation": """**Object.values()** returns an array of the object's own property values.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/values",
        "points": 1,
        "answers": [
            {"text": "Object.values()", "is_correct": True},
            {"text": "Object.getValues()", "is_correct": False},
            {"text": "Object.data()", "is_correct": False},
            {"text": "Object.entries()", "is_correct": False},
        ],
    },
    {
        "text": "What does Promise.resolve() return?",
        "explanation": """**Promise.resolve()** returns a Promise resolved with the given value.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/resolve",
        "points": 1,
        "answers": [
            {"text": "A pending promise", "is_correct": False},
            {"text": "A resolved promise", "is_correct": True},
            {"text": "A rejected promise", "is_correct": False},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "What does Promise.reject() return?",
        "explanation": """**Promise.reject()** returns a Promise rejected with the given reason.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/reject",
        "points": 1,
        "answers": [
            {"text": "A resolved promise", "is_correct": False},
            {"text": "A pending promise", "is_correct": False},
            {"text": "A rejected promise", "is_correct": True},
            {"text": "undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which method waits for multiple promises to resolve?",
        "explanation": """**Promise.all()** waits for all promises and rejects if any fails.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/all",
        "points": 1,
        "answers": [
            {"text": "Promise.all()", "is_correct": True},
            {"text": "Promise.race()", "is_correct": False},
            {"text": "Promise.any()", "is_correct": False},
            {"text": "Promise.allSettled()", "is_correct": False},
        ],
    },
    {
        "text": "Which method creates an iterable of Set values?",
        "explanation": """**Set** is a collection of unique values. Use **for...of** to iterate.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set",
        "points": 1,
        "answers": [
            {"text": "Set", "is_correct": True},
            {"text": "Array", "is_correct": False},
            {"text": "Map", "is_correct": False},
            {"text": "Object", "is_correct": False},
        ],
    },
    {
        "text": "Which data structure stores key-value pairs similar to objects?",
        "explanation": """**Map** is like an object but keys can be any type, not just strings.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map",
        "points": 1,
        "answers": [
            {"text": "Set", "is_correct": False},
            {"text": "Map", "is_correct": True},
            {"text": "Array", "is_correct": False},
            {"text": "Object", "is_correct": False},
        ],
    },
    {
        "text": "What will console.log(typeof {}) output?",
        "explanation": """Objects, arrays, functions all return **\"object\"** as their type.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof",
        "points": 1,
        "answers": [
            {"text": "\"object\"", "is_correct": True},
            {"text": "\"Object\"", "is_correct": False},
            {"text": "\"dict\"", "is_correct": False},
            {"text": "\"map\"", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword checks the prototype chain?",
        "explanation": """**instanceof** checks if an object is an instance of a constructor function.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof",
        "points": 1,
        "answers": [
            {"text": "typeof", "is_correct": False},
            {"text": "instanceof", "is_correct": True},
            {"text": "isInstance", "is_correct": False},
            {"text": "typeOf", "is_correct": False},
        ],
    },
    {
        "text": "What happens when you use 'new' with a constructor function?",
        "explanation": """**new** creates a new object, sets its prototype, calls the constructor, and returns the object.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new",
        "points": 1,
        "answers": [
            {"text": "Creates and returns a new object", "is_correct": True},
            {"text": "Creates a copy of the function", "is_correct": False},
            {"text": "Creates a class", "is_correct": False},
            {"text": "Throws an error", "is_correct": False},
        ],
    },
    {
        "text": "Which method can be used to call a function with a specific 'this' context?",
        "explanation": """**call()**, **apply()**, and **bind()** allow you to set the 'this' context.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call",
        "points": 1,
        "answers": [
            {"text": "call()", "is_correct": True},
            {"text": "invoke()", "is_correct": False},
            {"text": "execute()", "is_correct": False},
            {"text": "run()", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Object.freeze()?",
        "explanation": """**Object.freeze()** prevents modifications to an object's properties.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze",
        "points": 1,
        "answers": [
            {"text": "Freezes object properties from modification", "is_correct": True},
            {"text": "Creates a copy of the object", "is_correct": False},
            {"text": "Clears object properties", "is_correct": False},
            {"text": "Merges objects", "is_correct": False},
        ],
    },
    {
        "text": "Which array method combines an array of arrays into a single array?",
        "explanation": """**flat()** flattens nested arrays. **flatMap()** combines flat and map.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/flat",
        "points": 1,
        "answers": [
            {"text": "flat()", "is_correct": True},
            {"text": "flatten()", "is_correct": False},
            {"text": "merge()", "is_correct": False},
            {"text": "combine()", "is_correct": False},
        ],
    },
    {
        "text": "What is hoisting in JavaScript?",
        "explanation": """**Hoisting** moves variable and function declarations to the top of their scope.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Glossary/Hoisting",
        "points": 1,
        "answers": [
            {"text": "Moving declarations to top of scope", "is_correct": True},
            {"text": "Lifting objects up", "is_correct": False},
            {"text": "Creating new variables", "is_correct": False},
            {"text": "Calling functions early", "is_correct": False},
        ],
    },
    {
        "text": "What is the Temporal Dead Zone (TDZ)?",
        "explanation": """The **TDZ** is the period from block start until a variable is declared; accessing it throws ReferenceError.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone",
        "points": 1,
        "answers": [
            {"text": "Period where variable is inaccessible before declaration", "is_correct": True},
            {"text": "Time zone for dates", "is_correct": False},
            {"text": "Period after hoisting", "is_correct": False},
            {"text": "Temporary variable storage", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to create a named export in modules?",
        "explanation": """**export** keyword exports variables, functions, or classes for use in other modules.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/export",
        "points": 1,
        "answers": [
            {"text": "export", "is_correct": True},
            {"text": "expose", "is_correct": False},
            {"text": "share", "is_correct": False},
            {"text": "publish", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to import modules?",
        "explanation": """**import** statement loads variables, functions, or classes from other modules.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import",
        "points": 1,
        "answers": [
            {"text": "import", "is_correct": True},
            {"text": "require", "is_correct": False},
            {"text": "include", "is_correct": False},
            {"text": "use", "is_correct": False},
        ],
    },
    {
        "text": "What is a default parameter in JavaScript?",
        "explanation": """A **default parameter** provides a default value when no argument is passed.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Default_parameters",
        "points": 1,
        "answers": [
            {"text": "Parameter with default value", "is_correct": True},
            {"text": "Unnamed parameter", "is_correct": False},
            {"text": "Parameter without value", "is_correct": False},
            {"text": "Global parameter", "is_correct": False},
        ],
    },
    {
        "text": "What are rest parameters used for?",
        "explanation": """**Rest parameters** (using ...) allow functions to accept variable number of arguments as an array.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/rest_parameters",
        "points": 1,
        "answers": [
            {"text": "Accept multiple arguments as array", "is_correct": True},
            {"text": "Take a break in loops", "is_correct": False},
            {"text": "Rest the code", "is_correct": False},
            {"text": "Return remaining values", "is_correct": False},
        ],
    },
    {
        "text": "Which method creates a string with tag function processing?",
        "explanation": """**Tagged template literals** call a function with template string parts and expressions.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals#tagged_templates",
        "points": 1,
        "answers": [
            {"text": "Tagged templates", "is_correct": True},
            {"text": "String templates", "is_correct": False},
            {"text": "Label templates", "is_correct": False},
            {"text": "Named templates", "is_correct": False},
        ],
    },
    {
        "text": "What does Object.entries() return?",
        "explanation": """**Object.entries()** returns an array of [key, value] pairs.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries",
        "points": 1,
        "answers": [
            {"text": "Array of [key, value] pairs", "is_correct": True},
            {"text": "Array of keys only", "is_correct": False},
            {"text": "Array of values only", "is_correct": False},
            {"text": "Single object", "is_correct": False},
        ],
    },
    {
        "text": "Which statement throws an error that can be caught?",
        "explanation": """**throw** statement throws a user-defined error or re-throws caught errors.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw",
        "points": 1,
        "answers": [
            {"text": "throw", "is_correct": True},
            {"text": "catch", "is_correct": False},
            {"text": "error", "is_correct": False},
            {"text": "fail", "is_correct": False},
        ],
    },
    {
        "text": "What does finally block do in try-catch-finally?",
        "explanation": """**finally** block always executes after try or catch, regardless of success or failure.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch",
        "points": 1,
        "answers": [
            {"text": "Always executes after try/catch", "is_correct": True},
            {"text": "Only executes on error", "is_correct": False},
            {"text": "Only executes on success", "is_correct": False},
            {"text": "Ends the program", "is_correct": False},
        ],
    },
    {
        "text": "Which method creates a proxy object?",
        "explanation": """**new Proxy()** creates a proxy that intercepts operations on an object.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy",
        "points": 1,
        "answers": [
            {"text": "Proxy", "is_correct": True},
            {"text": "Wrapper", "is_correct": False},
            {"text": "Handler", "is_correct": False},
            {"text": "Interceptor", "is_correct": False},
        ],
    },
    {
        "text": "Which function is called repeatedly after a specified delay?",
        "explanation": """**setInterval()** calls a function repeatedly at specified intervals.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/setInterval",
        "points": 1,
        "answers": [
            {"text": "setTimeout()", "is_correct": False},
            {"text": "setInterval()", "is_correct": True},
            {"text": "setTimer()", "is_correct": False},
            {"text": "repeatAfter()", "is_correct": False},
        ],
    },
    {
        "text": "Which function executes after a specified delay only once?",
        "explanation": """**setTimeout()** calls a function after a specified delay, only one time.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/setTimeout",
        "points": 1,
        "answers": [
            {"text": "setTimeout()", "is_correct": True},
            {"text": "setInterval()", "is_correct": False},
            {"text": "setDelay()", "is_correct": False},
            {"text": "waitFor()", "is_correct": False},
        ],
    },
    {
        "text": "What does the optional chaining operator (?.) do?",
        "explanation": """**?.** safely accesses nested properties and returns undefined if property doesn't exist.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining",
        "points": 1,
        "answers": [
            {"text": "Safely accesses properties", "is_correct": True},
            {"text": "Throws error on missing property", "is_correct": False},
            {"text": "Creates new property", "is_correct": False},
            {"text": "Deletes property", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Symbol in JavaScript?",
        "explanation": """**Symbol** creates unique identifiers that cannot collide with other property keys.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol",
        "points": 1,
        "answers": [
            {"text": "Create unique identifiers", "is_correct": True},
            {"text": "Create string values", "is_correct": False},
            {"text": "Create numbers", "is_correct": False},
            {"text": "Create arrays", "is_correct": False},
        ],
    },
    {
        "text": "Which method adds or updates elements in place in an array?",
        "explanation": """**fill()** fills array elements with a static value.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill",
        "points": 1,
        "answers": [
            {"text": "fill()", "is_correct": True},
            {"text": "replace()", "is_correct": False},
            {"text": "update()", "is_correct": False},
            {"text": "set()", "is_correct": False},
        ],
    },
]