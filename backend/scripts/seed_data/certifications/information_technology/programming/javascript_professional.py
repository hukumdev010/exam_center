"""JavaScript Professional Certification"""

CERTIFICATION = {
    "name": "JavaScript Professional",
    "description": "JavaScript Certified Professional Developer",
    "slug": "javascript-professional",
    "level": "Professional",
    "duration": 90,
    "questions_count": 50,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is the Event Loop in JavaScript?",
        "explanation": """# Event Loop in JavaScript

The Event Loop is what allows JavaScript to perform non-blocking operations by handling asynchronous callbacks.

## How it works:
1. **Call Stack**: Executes synchronous code
2. **Web APIs**: Handle async operations (setTimeout, DOM events, HTTP requests)
3. **Task Queue**: Holds completed async callbacks
4. **Event Loop**: Moves tasks from queue to call stack when stack is empty

## Example:
```javascript
console.log('Start');

setTimeout(() => {
    console.log('Timeout');
}, 0);

Promise.resolve().then(() => {
    console.log('Promise');
});

console.log('End');

// Output: Start, End, Promise, Timeout
// Microtasks (Promises) have higher priority than macrotasks (setTimeout)
```

Understanding the event loop is crucial for writing efficient async code.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop",
        "points": 1,
        "answers": [
            {"text": "Mechanism that handles asynchronous operations", "is_correct": True},
            {"text": "A type of loop construct", "is_correct": False},
            {"text": "Event listener system", "is_correct": False},
            {"text": "Error handling mechanism", "is_correct": False},
        ],
    },
    {
        "text": "What is a WeakMap and how does it differ from Map?",
        "explanation": """# WeakMap vs Map

WeakMap holds weak references to keys and allows garbage collection of unused keys.

## Key Differences:
- **Keys**: WeakMap only accepts objects as keys, Map accepts any type
- **Garbage Collection**: WeakMap keys can be garbage collected
- **Enumeration**: WeakMap is not enumerable (no size, keys(), values())
- **Use Case**: WeakMap for metadata/private data, Map for general key-value storage

## Example:
```javascript
// Map - prevents garbage collection
let map = new Map();
let obj = {name: "Alice"};
map.set(obj, "some data");
obj = null; // Object can't be garbage collected due to Map reference

// WeakMap - allows garbage collection
let weakMap = new WeakMap();
let obj2 = {name: "Bob"};
weakMap.set(obj2, "private data");
obj2 = null; // Object can be garbage collected

// Common use case: Private data
const privateData = new WeakMap();
class Person {
    constructor(name) {
        privateData.set(this, {secret: "hidden"});
        this.name = name;
    }
    
    getSecret() {
        return privateData.get(this).secret;
    }
}
```

WeakMaps are perfect for storing metadata without preventing garbage collection.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakMap",
        "points": 1,
        "answers": [
            {"text": "WeakMap allows garbage collection of keys", "is_correct": True},
            {"text": "WeakMap is faster than Map", "is_correct": False},
            {"text": "WeakMap can store primitive keys", "is_correct": False},
            {"text": "No difference", "is_correct": False},
        ],
    },
    {
        "text": "What is the Temporal Dead Zone?",
        "explanation": """# Temporal Dead Zone (TDZ)

The time between entering a scope and the variable declaration being executed, where the variable exists but cannot be accessed.

## Example:
```javascript
console.log(varVariable); // undefined (hoisted)
// console.log(letVariable); // ReferenceError: Cannot access before initialization

var varVariable = "var value";
let letVariable = "let value";
const constVariable = "const value";

// Function example
function example() {
    console.log(x); // ReferenceError: x is in TDZ
    let x = 1;
    console.log(x); // 1
}

// Temporal Dead Zone with default parameters
function func(a = b, b = 2) {
    return a + b;
}
// func(); // ReferenceError: b is in TDZ when evaluating 'a'

// Class example
class MyClass {
    constructor() {
        console.log(this.method); // ReferenceError if method uses 'this'
    }
    
    method = () => {
        return "arrow method";
    };
}
```

TDZ prevents using variables before they're properly initialized.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#temporal_dead_zone_tdz",
        "points": 1,
        "answers": [
            {"text": "Time when variables exist but cannot be accessed", "is_correct": True},
            {"text": "Error handling mechanism", "is_correct": False},
            {"text": "Async operation delay", "is_correct": False},
            {"text": "Memory management feature", "is_correct": False},
        ],
    },
    {
        "text": "What is a Proxy in JavaScript?",
        "explanation": """# Proxy Object

Proxy allows you to intercept and customize operations performed on objects (property lookup, assignment, enumeration, etc.).

## Example:
```javascript
// Basic proxy with handler
const target = {
    name: "Alice",
    age: 25
};

const proxy = new Proxy(target, {
    get(target, property, receiver) {
        console.log(`Getting ${property}`);
        return property in target ? target[property] : "Property not found";
    },
    
    set(target, property, value, receiver) {
        console.log(`Setting ${property} to ${value}`);
        if (property === 'age' && value < 0) {
            throw new Error('Age cannot be negative');
        }
        target[property] = value;
        return true;
    }
});

console.log(proxy.name); // "Getting name" -> "Alice"
proxy.age = 30;          // "Setting age to 30"
// proxy.age = -5;       // Error: Age cannot be negative

// Validation proxy
function createValidatedObject(schema) {
    return new Proxy({}, {
        set(target, property, value) {
            const validator = schema[property];
            if (validator && !validator(value)) {
                throw new Error(`Invalid value for ${property}`);
            }
            target[property] = value;
            return true;
        }
    });
}

const user = createValidatedObject({
    email: value => value.includes('@'),
    age: value => typeof value === 'number' && value >= 0
});
```

Proxies enable meta-programming and creating dynamic object behaviors.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy",
        "points": 1,
        "answers": [
            {"text": "Intercepts and customizes object operations", "is_correct": True},
            {"text": "Network request handler", "is_correct": False},
            {"text": "Error handling wrapper", "is_correct": False},
            {"text": "Memory optimization tool", "is_correct": False},
        ],
    },
    {
        "text": """## Generator Function Analysis

**What is the output of the following code?**

```javascript
function* fibonacci() {
    let a = 0, b = 1;
    while (true) {
        yield a;
        [a, b] = [b, a + b];
    }
}

const fib = fibonacci();
console.log(fib.next().value);
console.log(fib.next().value);
console.log(fib.next().value);
```

*Choose the correct sequence:*""",
        "explanation": """# Generator Functions

Generators are functions that can be paused and resumed, yielding values one at a time.

## Code Analysis:
```javascript
function* fibonacci() {
    let a = 0, b = 1;
    while (true) {
        yield a;        // Pause and return current value
        [a, b] = [b, a + b];  // Update for next iteration
    }
}

const fib = fibonacci();  // Returns generator object
console.log(fib.next().value);  // 0 (first yield)
console.log(fib.next().value);  // 1 (second yield)  
console.log(fib.next().value);  // 1 (third yield)

// Sequence: 0, 1, 1, 2, 3, 5, 8, 13...
```

Generators are perfect for creating iterators and handling infinite sequences.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators",
        "points": 1,
        "answers": [
            {"text": "0, 1, 1", "is_correct": True},
            {"text": "1, 1, 2", "is_correct": False},
            {"text": "0, 1, 2", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between microtasks and macrotasks?",
        "explanation": """# Microtasks vs Macrotasks

JavaScript's event loop processes microtasks before macrotasks for each loop iteration.

## Examples:
**Microtasks**: Promise.then(), queueMicrotask(), MutationObserver
**Macrotasks**: setTimeout(), setInterval(), I/O operations, UI events

## Example:
```javascript
console.log('1');

setTimeout(() => console.log('2'), 0);           // Macrotask

Promise.resolve().then(() => console.log('3')); // Microtask

console.log('4');

setTimeout(() => console.log('5'), 0);           // Macrotask

Promise.resolve().then(() => console.log('6')); // Microtask

console.log('7');

// Output: 1, 4, 7, 3, 6, 2, 5
// Synchronous code first, then all microtasks, then macrotasks
```

## Priority Order:
1. Synchronous code
2. All microtasks (Promise.then, queueMicrotask)
3. One macrotask (setTimeout, setInterval)
4. Repeat from step 2

Understanding this is crucial for async code execution order.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API/Microtask_guide",
        "points": 1,
        "answers": [
            {"text": "Microtasks have higher priority than macrotasks", "is_correct": True},
            {"text": "Macrotasks have higher priority", "is_correct": False},
            {"text": "They have equal priority", "is_correct": False},
            {"text": "No difference", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of Symbol.iterator?",
        "explanation": """# Symbol.iterator

Symbol.iterator is a well-known symbol that specifies the default iterator for an object, making it iterable.

## Example:
```javascript
// Custom iterable object
const customIterable = {
    data: [1, 2, 3, 4, 5],
    
    [Symbol.iterator]() {
        let index = 0;
        const data = this.data;
        
        return {
            next() {
                if (index < data.length) {
                    return { value: data[index++], done: false };
                } else {
                    return { done: true };
                }
            }
        };
    }
};

// Now it works with for...of, spread operator, etc.
for (const value of customIterable) {
    console.log(value); // 1, 2, 3, 4, 5
}

const arr = [...customIterable]; // [1, 2, 3, 4, 5]

// Range iterator example
function* range(start, end) {
    for (let i = start; i < end; i++) {
        yield i;
    }
}

const numbers = {
    [Symbol.iterator]: () => range(1, 5)
};

console.log([...numbers]); // [1, 2, 3, 4]
```

Makes objects work with for...of loops, spread operator, and destructuring.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/iterator",
        "points": 1,
        "answers": [
            {"text": "Makes objects iterable with for...of loops", "is_correct": True},
            {"text": "Creates new symbols", "is_correct": False},
            {"text": "Handles async operations", "is_correct": False},
            {"text": "Manages object properties", "is_correct": False},
        ],
    },
    {
        "text": "What is a Service Worker?",
        "explanation": """# Service Workers

Service Workers are scripts that run in the background, separate from web pages, enabling features like offline functionality and push notifications.

## Example:
```javascript
// Register service worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js')
        .then(registration => {
            console.log('SW registered:', registration);
        })
        .catch(error => {
            console.log('SW registration failed:', error);
        });
}

// sw.js - Service Worker file
self.addEventListener('install', event => {
    console.log('Service Worker installing');
    event.waitUntil(
        caches.open('v1').then(cache => {
            return cache.addAll([
                '/',
                '/index.html',
                '/styles.css',
                '/app.js'
            ]);
        })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Return cached version or fetch from network
                return response || fetch(event.request);
            })
    );
});

// Listen for push notifications
self.addEventListener('push', event => {
    const data = event.data.json();
    const options = {
        body: data.body,
        icon: '/icon.png',
        badge: '/badge.png'
    };
    
    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});
```

Service Workers enable Progressive Web App (PWA) features.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API",
        "points": 1,
        "answers": [
            {"text": "Background script for offline functionality and push notifications", "is_correct": True},
            {"text": "Worker thread for heavy computations", "is_correct": False},
            {"text": "Server-side JavaScript runtime", "is_correct": False},
            {"text": "DOM manipulation helper", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between Object.freeze(), Object.seal(), and Object.preventExtensions()?",
        "explanation": """# Object Immutability Methods

These methods provide different levels of object immutability.

## Comparison:
- **preventExtensions()**: Can't add new properties
- **seal()**: Can't add/remove properties, can modify existing
- **freeze()**: Can't add/remove/modify properties (completely immutable)

## Example:
```javascript
const obj1 = { name: "Alice", age: 25 };
Object.preventExtensions(obj1);
obj1.city = "NYC";        // Fails silently (strict mode: TypeError)
obj1.age = 30;           // Works - can modify existing
delete obj1.name;        // Works - can delete existing
console.log(obj1);       // { age: 30 }

const obj2 = { name: "Bob", age: 30 };
Object.seal(obj2);
obj2.city = "LA";        // Fails silently
obj2.age = 35;          // Works - can modify existing
delete obj2.name;       // Fails silently
console.log(obj2);      // { name: "Bob", age: 35 }

const obj3 = { name: "Charlie", age: 40 };
Object.freeze(obj3);
obj3.city = "Chicago";  // Fails silently
obj3.age = 45;         // Fails silently
delete obj3.name;      // Fails silently
console.log(obj3);     // { name: "Charlie", age: 40 }

// Check object state
console.log(Object.isExtensible(obj1)); // false
console.log(Object.isSealed(obj2));     // true
console.log(Object.isFrozen(obj3));     // true

// Note: These are shallow operations
const nested = { user: { name: "Dave" } };
Object.freeze(nested);
nested.user.name = "David"; // This works! Nested object not frozen
```

Choose based on the level of immutability needed.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze",
        "points": 1,
        "answers": [
            {"text": "Different levels of object immutability", "is_correct": True},
            {"text": "All do the same thing", "is_correct": False},
            {"text": "Only affect nested objects", "is_correct": False},
            {"text": "Performance optimization methods", "is_correct": False},
        ],
    },
    {
        "text": "What is tail call optimization?",
        "explanation": """# Tail Call Optimization (TCO)

TCO optimizes recursive functions where the recursive call is the last operation, preventing stack overflow.

## Example:
```javascript
// Non-tail recursive (not optimized)
function factorial(n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1); // Multiplication after recursive call
}

// Tail recursive (can be optimized)
function factorialTail(n, accumulator = 1) {
    if (n <= 1) return accumulator;
    return factorialTail(n - 1, n * accumulator); // Recursive call is last
}

// Fibonacci - non-tail recursive
function fib(n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2); // Addition after recursive calls
}

// Fibonacci - tail recursive
function fibTail(n, a = 0, b = 1) {
    if (n === 0) return a;
    if (n === 1) return b;
    return fibTail(n - 1, b, a + b); // Recursive call is last
}

// TCO Requirements:
// 1. Recursive call must be the last operation
// 2. No operations after the recursive call
// 3. Must be in strict mode (ES6)

// Note: Most JavaScript engines don't implement TCO yet
// But understanding helps write stack-safe recursive functions
```

Write tail-recursive functions to avoid stack overflow errors.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions#tail_call_optimization",
        "points": 1,
        "answers": [
            {"text": "Optimization for recursive functions where recursion is the last operation", "is_correct": True},
            {"text": "Optimization for loop performance", "is_correct": False},
            {"text": "Memory management technique", "is_correct": False},
            {"text": "Async operation optimization", "is_correct": False},
        ],
    },
    {
        "text": "What is the AbortController API?",
        "explanation": """# AbortController API

AbortController provides a way to abort one or more async operations like fetch requests.

## Example:
```javascript
// Basic usage with fetch
const controller = new AbortController();
const signal = controller.signal;

fetch('/api/data', { signal })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => {
        if (error.name === 'AbortError') {
            console.log('Request was aborted');
        } else {
            console.error('Other error:', error);
        }
    });

// Abort after 5 seconds
setTimeout(() => controller.abort(), 5000);

// Multiple requests with same controller
async function fetchMultiple() {
    const controller = new AbortController();
    const signal = controller.signal;
    
    try {
        const [users, posts] = await Promise.all([
            fetch('/api/users', { signal }),
            fetch('/api/posts', { signal })
        ]);
        
        // Process results...
    } catch (error) {
        if (error.name === 'AbortError') {
            console.log('All requests aborted');
        }
    }
    
    // Abort all requests if needed
    // controller.abort();
}

// React-style cleanup
function useAsyncData(url) {
    const [data, setData] = React.useState(null);
    
    React.useEffect(() => {
        const controller = new AbortController();
        
        fetch(url, { signal: controller.signal })
            .then(response => response.json())
            .then(setData)
            .catch(error => {
                if (error.name !== 'AbortError') {
                    console.error(error);
                }
            });
        
        return () => controller.abort(); // Cleanup on unmount
    }, [url]);
    
    return data;
}
```

Essential for preventing memory leaks and unnecessary network requests.""",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/AbortController",
        "points": 1,
        "answers": [
            {"text": "API for aborting async operations like fetch requests", "is_correct": True},
            {"text": "Error handling mechanism", "is_correct": False},
            {"text": "Performance monitoring tool", "is_correct": False},
            {"text": "Security control system", "is_correct": False},
        ],
    },
    {
        "text": "What are JavaScript decorators?",
        "explanation": """# JavaScript Decorators (Experimental)

Decorators are a proposed feature for adding metadata and modifying classes and methods.

## Example (Stage 3 Proposal):
```javascript
// Method decorator
function logged(target, propertyKey, descriptor) {
    const originalMethod = descriptor.value;
    
    descriptor.value = function(...args) {
        console.log(`Calling ${propertyKey} with args:`, args);
        const result = originalMethod.apply(this, args);
        console.log(`Result:`, result);
        return result;
    };
    
    return descriptor;
}

// Class decorator
function sealed(constructor) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
    return constructor;
}

@sealed
class Calculator {
    @logged
    add(a, b) {
        return a + b;
    }
    
    @logged
    multiply(a, b) {
        return a * b;
    }
}

const calc = new Calculator();
calc.add(5, 3);      // Logs method call and result
calc.multiply(4, 2); // Logs method call and result

// Auto-bind decorator
function autobind(target, propertyKey, descriptor) {
    const originalMethod = descriptor.value;
    
    return {
        configurable: true,
        get() {
            return originalMethod.bind(this);
        }
    };
}

class EventHandler {
    @autobind
    handleClick() {
        console.log('Button clicked');
    }
}

// Property decorator (Stage 3)
function validate(validatorFn) {
    return function(target, propertyKey) {
        let value = target[propertyKey];
        
        Object.defineProperty(target, propertyKey, {
            get() { return value; },
            set(newValue) {
                if (!validatorFn(newValue)) {
                    throw new Error(`Invalid value for ${propertyKey}`);
                }
                value = newValue;
            }
        });
    };
}
```

Currently experimental but provides powerful metaprogramming capabilities.""",
        "reference": "https://github.com/tc39/proposal-decorators",
        "points": 1,
        "answers": [
            {"text": "Proposed feature for adding metadata and modifying classes", "is_correct": True},
            {"text": "CSS styling system", "is_correct": False},
            {"text": "Error handling pattern", "is_correct": False},
            {"text": "Performance optimization tool", "is_correct": False},
        ],
    },
]