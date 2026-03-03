"""Python Institute PCAP Certification"""

CERTIFICATION = {
    "name": "Python Institute PCAP",
    "description": "Python Certified Associate Programmer",
    "slug": "python-pcap",
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

```python
class A:
    def __init__(self):
        self.x = 1

obj = A()
print(obj.x)
```

*Choose the correct output:*""",
        "explanation": """# Object-Oriented Programming - Classes and Objects

> **Key Concept**: Classes are blueprints for creating objects. The `__init__` method is the constructor that initializes new instances.

## Code Breakdown:

1. **Class Definition**: `class A:` defines a new class named A
2. **Constructor Method**: `__init__(self)` is called when creating new instances
3. **Instance Variable**: `self.x = 1` sets an instance attribute
4. **Object Creation**: `obj = A()` creates a new instance
5. **Attribute Access**: `print(obj.x)` accesses the instance variable

## Example Output:
```python
class A:
    def __init__(self):
        self.x = 1

obj = A()
print(obj.x)  # Output: 1
```

### 📝 **Important Notes:**
- The `__init__` method initializes instance variables when an object is created
- Instance variables belong to specific object instances
- The `self` parameter refers to the instance being created

### 🔗 **Related Concepts:**
- Instance vs Class variables
- Object instantiation
- Constructor methods""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "**1**", "is_correct": True},
            {"text": "**None**", "is_correct": False},
            {"text": "**Error**", "is_correct": False},
            {"text": "**0**", "is_correct": False},
        ],
    },
    {
        "text": "Which method is used to handle exceptions in Python?",
        "explanation": """# Exception Handling in Python

Use `try-except` blocks to handle exceptions and prevent program crashes.

## Basic Syntax:
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid value!")
finally:
    print("This always executes")
```

## Common Exception Types:
- `ValueError` - Invalid value for operation
- `TypeError` - Wrong data type  
- `IndexError` - List index out of range
- `KeyError` - Dictionary key not found
- `ZeroDivisionError` - Division by zero

Always catch specific exceptions before general ones.""",
        "reference": "https://docs.python.org/3/tutorial/errors.html",
        "points": 1,
        "answers": [
            {"text": "try-except", "is_correct": True},
            {"text": "catch-throw", "is_correct": False},
            {"text": "handle-error", "is_correct": False},
            {"text": "exception-catch", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between a list and a tuple?",
        "explanation": """# Lists vs Tuples

Lists are mutable (can be changed), tuples are immutable (cannot be changed).

## Example:
```python
# List - mutable
my_list = [1, 2, 3]
my_list[0] = 10  # Works: [10, 2, 3]

# Tuple - immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Error: cannot modify
```

## Key Differences:
- **Mutability**: Lists can be modified, tuples cannot
- **Performance**: Tuples are faster for accessing data
- **Memory**: Tuples use less memory
- **Use cases**: Lists for dynamic data, tuples for fixed data

Use tuples for coordinates, database records, or any fixed data.
Use lists for shopping carts, user inputs, or dynamic collections.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html",
        "points": 1,
        "answers": [
            {"text": "Lists are mutable, tuples are immutable", "is_correct": True},
            {"text": "Lists are faster than tuples", "is_correct": False},
            {"text": "Tuples can store more data", "is_correct": False},
            {"text": "No difference", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'super()' function do in Python?",
        "explanation": """# Inheritance and super() Function

`super()` calls methods from the parent class in inheritance.

## Example:
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent constructor
        self.breed = breed
    
    def speak(self):
        return super().speak() + " - Woof!"
```

Allows code reuse and method extension in inheritance.""",
        "reference": "https://docs.python.org/3/library/functions.html#super",
        "points": 1,
        "answers": [
            {"text": "Calls parent class methods", "is_correct": True},
            {"text": "Creates a new class", "is_correct": False},
            {"text": "Deletes the current object", "is_correct": False},
            {"text": "Imports modules", "is_correct": False},
        ],
    },
    {
        "text": "What is a lambda function in Python?",
        "explanation": """# Lambda Functions (Anonymous Functions)

Lambda functions are small, anonymous functions that can have any number of arguments but only one expression.

## Example:
```python
# Regular function
def square(x):
    return x ** 2

# Lambda function
square_lambda = lambda x: x ** 2

# Usage in higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
# Result: [1, 4, 9, 16, 25]
```

Useful for short, one-line functions and functional programming.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions",
        "points": 1,
        "answers": [
            {"text": "A small anonymous function", "is_correct": True},
            {"text": "A type of variable", "is_correct": False},
            {"text": "A loop statement", "is_correct": False},
            {"text": "A class method", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of '__init__.py' file?",
        "explanation": """# Package Initialization with __init__.py

The `__init__.py` file makes a directory a Python package and controls what gets imported.

## Example:
```python
# mypackage/__init__.py
from .module1 import function1
from .module2 import Class2

__all__ = ['function1', 'Class2']

# Now you can import directly:
# from mypackage import function1, Class2
```

Can be empty or contain package initialization code.""",
        "reference": "https://docs.python.org/3/tutorial/modules.html#packages",
        "points": 1,
        "answers": [
            {"text": "Makes directory a Python package", "is_correct": True},
            {"text": "Initializes variables", "is_correct": False},
            {"text": "Contains main function", "is_correct": False},
            {"text": "Stores configuration", "is_correct": False},
        ],
    },
    {
        "text": """## Code Output Question

**What is the output of the following code?**

```python
list(map(lambda x: x*2, [1, 2, 3]))
```

*Choose the correct result:*""",
        "explanation": """# Map Function with Lambda

`map()` applies a function to every item in an iterable and returns an iterator.

## Example:
```python
numbers = [1, 2, 3]
doubled = list(map(lambda x: x*2, numbers))
print(doubled)  # [2, 4, 6]

# Equivalent to:
doubled = [x*2 for x in numbers]
```

Common functional programming pattern for transforming data.""",
        "reference": "https://docs.python.org/3/library/functions.html#map",
        "points": 1,
        "answers": [
            {"text": "[2, 4, 6]", "is_correct": True},
            {"text": "[1, 2, 3]", "is_correct": False},
            {"text": "[1, 4, 9]", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is a decorator in Python?",
        "explanation": """# Decorators in Python

Decorators are functions that modify or extend the behavior of other functions.

## Example:
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output: Before function call
#         Hello!
#         After function call
```

Used for logging, timing, authentication, etc.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
        "points": 1,
        "answers": [
            {"text": "A function that modifies other functions", "is_correct": True},
            {"text": "A type of variable", "is_correct": False},
            {"text": "A design pattern", "is_correct": False},
            {"text": "A data structure", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between '==' and 'is' operators?",
        "explanation": """# Equality vs Identity Operators

`==` compares values, `is` compares object identity (memory location).

## Example:
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True - same values
print(a is b)  # False - different objects
print(a is c)  # True - same object

# For small integers and strings:
x = 5
y = 5
print(x is y)  # True - Python optimizes small integers
```

Use `==` for value comparison, `is` for identity checks (especially with None).""",
        "reference": "https://docs.python.org/3/reference/expressions.html#comparisons",
        "points": 1,
        "answers": [
            {"text": "== compares values, is compares identity", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "is compares values, == compares identity", "is_correct": False},
            {"text": "== is faster than is", "is_correct": False},
        ],
    },
    {
        "text": "What does the 'yield' keyword do in Python?",
        "explanation": """# Generators and yield Keyword

`yield` creates a generator function that returns an iterator, pausing execution and resuming where it left off.

## Example:
```python
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

counter = count_up_to(3)
for num in counter:
    print(num)  # 1, 2, 3

# Memory efficient for large sequences
```

Generators produce values on-demand, saving memory for large datasets.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#generators",
        "points": 1,
        "answers": [
            {"text": "Creates a generator function", "is_correct": True},
            {"text": "Returns a value and exits", "is_correct": False},
            {"text": "Imports a module", "is_correct": False},
            {"text": "Defines a class", "is_correct": False},
        ],
    },
    {
        "text": """## File Handling Code Question

**What is the output of the following code?**

```python
with open('file.txt', 'w') as f:
    f.write('Hello')
print('File closed?', f.closed)
```

*Choose the correct output:*""",
        "explanation": """# Context Managers and 'with' Statement

The `with` statement ensures proper resource management by automatically closing files.

## Example:
```python
with open('file.txt', 'w') as f:
    f.write('Hello')
print('File closed?', f.closed)  # True

# Equivalent to:
f = open('file.txt', 'w')
try:
    f.write('Hello')
finally:
    f.close()
```

Context managers guarantee cleanup even if exceptions occur.""",
        "reference": "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files",
        "points": 1,
        "answers": [
            {"text": "File closed? True", "is_correct": True},
            {"text": "File closed? False", "is_correct": False},
            {"text": "Error", "is_correct": False},
            {"text": "File closed? None", "is_correct": False},
        ],
    },
    {
        "text": "What is list comprehension in Python?",
        "explanation": """# List Comprehensions

List comprehensions provide a concise way to create lists using a single line of code.

## Example:
```python
# Traditional approach
squares = []
for x in range(5):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# [0, 4, 16, 36, 64]
```

More readable and efficient than traditional loops for simple transformations.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
        "points": 1,
        "answers": [
            {"text": "A concise way to create lists", "is_correct": True},
            {"text": "A type of loop", "is_correct": False},
            {"text": "A function argument", "is_correct": False},
            {"text": "A data type", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between args and kwargs?",
        "explanation": """# Variable Arguments: *args and **kwargs

`*args` collects positional arguments, `**kwargs` collects keyword arguments.

## Example:
```python
def my_function(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

my_function(1, 2, 3, name="Alice", age=25)
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 25}

# Unpacking
numbers = [1, 2, 3]
data = {'x': 10, 'y': 20}
my_function(*numbers, **data)
```

Useful for flexible function signatures and function decorators.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions",
        "points": 1,
        "answers": [
            {"text": "*args for positional, **kwargs for keyword arguments", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "*args for keywords, **kwargs for positional", "is_correct": False},
            {"text": "They are data types", "is_correct": False},
        ],
    },
    {
        "text": "What is multiple inheritance in Python?",
        "explanation": """# Multiple Inheritance

A class can inherit from multiple parent classes, gaining features from all of them.

## Example:
```python
class Animal:
    def eat(self):
        return "Eating"

class Flyable:
    def fly(self):
        return "Flying"

class Bird(Animal, Flyable):  # Multiple inheritance
    def chirp(self):
        return "Chirping"

bird = Bird()
print(bird.eat())   # From Animal
print(bird.fly())   # From Flyable
print(bird.chirp()) # Own method
```

Method Resolution Order (MRO) determines which method is called when there are conflicts.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#multiple-inheritance",
        "points": 1,
        "answers": [
            {"text": "A class inheriting from multiple parent classes", "is_correct": True},
            {"text": "Creating multiple objects", "is_correct": False},
            {"text": "Having multiple methods", "is_correct": False},
            {"text": "Using multiple variables", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of __str__ and __repr__ methods?",
        "explanation": """# String Representation Methods

`__str__` defines user-friendly string representation, `__repr__` defines developer-friendly representation.

## Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Alice", 25)
print(str(p))   # Alice, 25 years old
print(repr(p))  # Person('Alice', 25)
```

`__str__` for end users, `__repr__` for debugging and development.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html#object.__str__",
        "points": 1,
        "answers": [
            {"text": "__str__ for user display, __repr__ for debugging", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "__repr__ for users, __str__ for debugging", "is_correct": False},
            {"text": "They convert objects to integers", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between shallow copy and deep copy?",
        "explanation": """# Shallow vs Deep Copy

Shallow copy creates new object but references to nested objects remain. Deep copy creates completely independent copy.

## Example:
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]

# Shallow copy
shallow = copy.copy(original)
shallow[0][0] = 'X'
print(original)  # [['X', 2, 3], [4, 5, 6]] - original affected!

# Deep copy
original = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(original)
deep[0][0] = 'X'
print(original)  # [[1, 2, 3], [4, 5, 6]] - original unchanged
```

Use deepcopy for nested mutable objects to avoid unintended modifications.""",
        "reference": "https://docs.python.org/3/library/copy.html",
        "points": 1,
        "answers": [
            {"text": "Shallow copies references, deep copy creates independent copy", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "Deep copy is faster", "is_correct": False},
            {"text": "Shallow copy creates independent copy", "is_correct": False},
        ],
    },
    {
        "text": "What are property decorators used for?",
        "explanation": """# Property Decorators

Property decorators allow methods to be accessed like attributes while maintaining control over getting/setting values.

## Example:
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.radius)  # 5 (calls getter)
c.radius = 10    # calls setter
print(c.area)    # computed property
```

Provides clean interface while controlling access and validation.""",
        "reference": "https://docs.python.org/3/library/functions.html#property",
        "points": 1,
        "answers": [
            {"text": "Control access to attributes", "is_correct": True},
            {"text": "Create new classes", "is_correct": False},
            {"text": "Handle exceptions", "is_correct": False},
            {"text": "Import modules", "is_correct": False},
        ],
    },
    {
        "text": "What is the Global Interpreter Lock (GIL) in Python?",
        "explanation": """# Global Interpreter Lock (GIL)

The GIL prevents multiple threads from executing Python code simultaneously, affecting multi-threaded performance.

## Example:
```python
import threading
import time

def cpu_intensive_task():
    # This won't run in parallel due to GIL
    total = 0
    for i in range(10000000):
        total += i
    return total

# Multiple threads, but not truly parallel
threads = []
for i in range(4):
    t = threading.Thread(target=cpu_intensive_task)
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

For CPU-bound tasks, use multiprocessing instead of threading.""",
        "reference": "https://docs.python.org/3/glossary.html#term-global-interpreter-lock",
        "points": 1,
        "answers": [
            {"text": "Prevents true parallel execution of Python threads", "is_correct": True},
            {"text": "Speeds up thread execution", "is_correct": False},
            {"text": "Manages memory allocation", "is_correct": False},
            {"text": "Handles file operations", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the __name__ == '__main__' check?",
        "explanation": """# Module Execution Check

`if __name__ == '__main__':` ensures code runs only when script is executed directly, not when imported.

## Example:
```python
# mymodule.py
def hello():
    print("Hello from module")

if __name__ == '__main__':
    print("Running as main script")
    hello()

# When run directly: prints both messages
# When imported: only function is available, no automatic execution
```

Essential for creating reusable modules with optional standalone functionality.""",
        "reference": "https://docs.python.org/3/library/__main__.html",
        "points": 1,
        "answers": [
            {"text": "Run code only when script is executed directly", "is_correct": True},
            {"text": "Check if module is imported", "is_correct": False},
            {"text": "Define the main function", "is_correct": False},
            {"text": "Handle exceptions", "is_correct": False},
        ],
    },
    {
        "text": "What is a metaclass in Python?",
        "explanation": """# Metaclasses

A metaclass is a class whose instances are classes. It controls class creation and behavior.

## Example:
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        self.connection = "Connected"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True - same instance
```

Advanced feature for controlling class creation and behavior.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html#metaclasses",
        "points": 1,
        "answers": [
            {"text": "A class that creates other classes", "is_correct": True},
            {"text": "A parent class", "is_correct": False},
            {"text": "A data structure", "is_correct": False},
            {"text": "A function decorator", "is_correct": False},
        ],
    },
    {
        "text": """## Dictionary Operations Question

**What is the output of the following code?**

```python
d = {'a': 1, 'b': 2}
result = d.get('c', 'default')
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Dictionary get() Method

The `get()` method returns the value for a key if it exists, otherwise returns a default value.

## Example:
```python
d = {'a': 1, 'b': 2}
print(d.get('a'))        # 1 (key exists)
print(d.get('c'))        # None (key doesn't exist)
print(d.get('c', 'default'))  # 'default' (custom default)

# Comparison with direct access:
# print(d['c'])  # KeyError!
```

Safer than direct dictionary access when key might not exist.""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#dict.get",
        "points": 1,
        "answers": [
            {"text": "default", "is_correct": True},
            {"text": "None", "is_correct": False},
            {"text": "Error", "is_correct": False},
            {"text": "c", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between append() and extend() methods?",
        "explanation": """# List Methods: append() vs extend()

`append()` adds a single element, `extend()` adds multiple elements from an iterable.

## Example:
```python
# append() - adds one element
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]]

# extend() - adds multiple elements
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5]

# extend() works with any iterable
list3 = ['a', 'b']
list3.extend('cd')
print(list3)  # ['a', 'b', 'c', 'd']
```

Use append() for single items, extend() for multiple items.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists",
        "points": 1,
        "answers": [
            {"text": "append() adds one element, extend() adds multiple", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "extend() adds one element, append() adds multiple", "is_correct": False},
            {"text": "append() is faster than extend()", "is_correct": False},
        ],
    },
    {
        "text": """## Set Operations Question

**What is the output of the following code?**

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1 & set2
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Set Operations

The `&` operator performs intersection, returning common elements between sets.

## Set Operations:
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1 & set2)   # {3, 4} - intersection
print(set1 | set2)   # {1, 2, 3, 4, 5, 6} - union
print(set1 - set2)   # {1, 2} - difference
print(set1 ^ set2)   # {1, 2, 5, 6} - symmetric difference

# Alternative methods:
print(set1.intersection(set2))  # Same as &
print(set1.union(set2))         # Same as |
```

Sets are useful for mathematical operations and removing duplicates.""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset",
        "points": 1,
        "answers": [
            {"text": "{3, 4}", "is_correct": True},
            {"text": "{1, 2, 3, 4, 5, 6}", "is_correct": False},
            {"text": "{1, 2}", "is_correct": False},
            {"text": "{5, 6}", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the enumerate() function?",
        "explanation": """# enumerate() Function

`enumerate()` returns an iterator that produces tuples containing count and values from an iterable.

## Example:
```python
fruits = ['apple', 'banana', 'cherry']

# Without enumerate
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# With enumerate (better)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Custom start value
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
# Output: 1: apple, 2: banana, 3: cherry
```

Cleaner and more Pythonic than manual index tracking.""",
        "reference": "https://docs.python.org/3/library/functions.html#enumerate",
        "points": 1,
        "answers": [
            {"text": "Provides index and value pairs for iteration", "is_correct": True},
            {"text": "Counts the number of elements", "is_correct": False},
            {"text": "Sorts a list", "is_correct": False},
            {"text": "Reverses a sequence", "is_correct": False},
        ],
    },
    {
        "text": """## String Methods Question

**What is the output of the following code?**

```python
text = "  Hello World  "
result = text.strip().split()
print(result)
```

*Choose the correct output:*""",
        "explanation": """# String Methods: strip() and split()

`strip()` removes whitespace from beginning and end, `split()` separates string into list.

## String Processing:
```python
text = "  Hello World  "

# Individual operations
print(text.strip())        # "Hello World"
print(text.split())        # ['Hello', 'World']
print(text.strip().split()) # ['Hello', 'World']

# Other string methods
print(text.replace('World', 'Python'))  # "  Hello Python  "
print(text.upper())                     # "  HELLO WORLD  "
print(text.lower())                     # "  hello world  "
```

Method chaining allows multiple operations in sequence.""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#string-methods",
        "points": 1,
        "answers": [
            {"text": "['Hello', 'World']", "is_correct": True},
            {"text": "['  Hello', 'World  ']", "is_correct": False},
            {"text": "'Hello World'", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between staticmethod and classmethod decorators?",
        "explanation": """# Static Methods vs Class Methods

`@staticmethod` doesn't receive any automatic first argument. `@classmethod` receives the class as first argument.

## Example:
```python
class Calculator:
    pi = 3.14159
    
    @staticmethod
    def add(x, y):
        return x + y  # No access to class or instance
    
    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2  # Uses class attribute
    
    def instance_method(self):
        return "Instance method"

# Usage
print(Calculator.add(5, 3))           # 8
print(Calculator.circle_area(5))      # 78.53975
calc = Calculator()
print(calc.instance_method())         # Instance method
```

Static methods are utility functions, class methods work with class data.""",
        "reference": "https://docs.python.org/3/library/functions.html#staticmethod",
        "points": 1,
        "answers": [
            {"text": "staticmethod has no automatic arguments, classmethod gets class", "is_correct": True},
            {"text": "Both receive the class as first argument", "is_correct": False},
            {"text": "staticmethod gets class, classmethod gets nothing", "is_correct": False},
            {"text": "There is no difference", "is_correct": False},
        ],
    },
    {
        "text": """## Boolean Logic Question

**What is the output of the following code?**

```python
result = bool([]) and bool("") or bool([1])
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Boolean Operations and Truthiness

Python evaluates truthiness: empty collections are False, non-empty are True.

## Truthiness Rules:
```python
# Falsy values
print(bool([]))        # False - empty list
print(bool(""))        # False - empty string
print(bool(0))         # False - zero
print(bool(None))      # False - None

# Truthy values
print(bool([1]))       # True - non-empty list
print(bool("hello"))   # True - non-empty string
print(bool(1))         # True - non-zero number

# Logical operations
print(False and False or True)  # True
```

Understand operator precedence: `and` before `or`.""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#truth-value-testing",
        "points": 1,
        "answers": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False},
            {"text": "None", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the zip() function?",
        "explanation": """# zip() Function

`zip()` combines multiple iterables element-wise, creating tuples of corresponding elements.

## Example:
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
cities = ['NYC', 'LA', 'Chicago']

# Combine iterables
pairs = list(zip(names, ages))
print(pairs)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Multiple iterables
triplets = list(zip(names, ages, cities))
# [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

# Unzipping
names2, ages2 = zip(*pairs)
print(names2)  # ('Alice', 'Bob', 'Charlie')
```

Stops at shortest iterable length.""",
        "reference": "https://docs.python.org/3/library/functions.html#zip",
        "points": 1,
        "answers": [
            {"text": "Combines multiple iterables element-wise", "is_correct": True},
            {"text": "Compresses files", "is_correct": False},
            {"text": "Sorts multiple lists", "is_correct": False},
            {"text": "Creates a single list from multiple lists", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between local and global variables?",
        "explanation": """# Variable Scope: Local vs Global

Local variables exist only within functions, global variables are accessible throughout the module.

## Example:
```python
x = 10  # Global variable

def my_function():
    x = 20  # Local variable (shadows global)
    y = 30  # Local variable
    print(f"Inside function: x={x}, y={y}")

my_function()  # Inside function: x=20, y=30
print(f"Outside function: x={x}")  # Outside function: x=10
# print(y)  # Error: y is not defined

# Using global keyword
def modify_global():
    global x
    x = 100  # Modifies global x

modify_global()
print(x)  # 100
```

Use `global` keyword to modify global variables inside functions.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces",
        "points": 1,
        "answers": [
            {"text": "Local exist in functions, global exist throughout module", "is_correct": True},
            {"text": "Local are faster than global", "is_correct": False},
            {"text": "Global are temporary, local are permanent", "is_correct": False},
            {"text": "There is no difference", "is_correct": False},
        ],
    },
    {
        "text": """## Exception Handling Question

**What is the output of the following code?**

```python
try:
    result = 10 / 2
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("No exception occurred")
finally:
    print("Cleanup")
```

*Choose the correct output:*""",
        "explanation": """# Exception Handling Flow

Try-except blocks with else and finally clauses control program flow during exception handling.

## Flow Explanation:
1. `try` block executes normally (10 / 2 = 5.0)
2. No exception occurs, so `except` is skipped
3. `else` executes because no exception occurred
4. `finally` always executes for cleanup

## Complete Structure:
```python
try:
    # Code that might raise exception
    pass
except SpecificException:
    # Handle specific exception
    pass
except Exception as e:
    # Handle any other exception
    pass
else:
    # Execute if no exception occurred
    pass
finally:
    # Always execute (cleanup)
    pass
```

`else` runs only if no exception, `finally` always runs.""",
        "reference": "https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions",
        "points": 1,
        "answers": [
            {"text": "Result: 5.0\\nNo exception occurred\\nCleanup", "is_correct": True},
            {"text": "Result: 5.0\\nCleanup", "is_correct": False},
            {"text": "Cannot divide by zero\\nCleanup", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the __len__ method?",
        "explanation": """# Special Method: __len__

The `__len__` method defines how the `len()` function behaves with custom objects.

## Example:
```python
class Playlist:
    def __init__(self):
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def __len__(self):
        return len(self.songs)
    
    def __str__(self):
        return f"Playlist with {len(self)} songs"

playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")

print(len(playlist))  # 2
print(playlist)       # Playlist with 2 songs
```

Enables built-in `len()` function to work with custom objects.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html#object.__len__",
        "points": 1,
        "answers": [
            {"text": "Defines behavior for len() function", "is_correct": True},
            {"text": "Calculates string length", "is_correct": False},
            {"text": "Initializes object length", "is_correct": False},
            {"text": "Converts object to integer", "is_correct": False},
        ],
    },
    {
        "text": """## Conditional Expression Question

**What is the output of the following code?**

```python
x = 5
result = "positive" if x > 0 else "negative" if x < 0 else "zero"
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Conditional Expressions (Ternary Operator)

Conditional expressions provide a concise way to choose between values based on conditions.

## Syntax and Examples:
```python
# Basic ternary operator
value = "positive" if x > 0 else "negative"

# Chained ternary operators
result = "positive" if x > 0 else "negative" if x < 0 else "zero"

# Equivalent if-elif-else
if x > 0:
    result = "positive"
elif x < 0:
    result = "negative"
else:
    result = "zero"

# Usage in function calls
print("Even" if x % 2 == 0 else "Odd")
```

More concise than full if-else statements for simple conditions.""",
        "reference": "https://docs.python.org/3/reference/expressions.html#conditional-expressions",
        "points": 1,
        "answers": [
            {"text": "positive", "is_correct": True},
            {"text": "negative", "is_correct": False},
            {"text": "zero", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between remove() and pop() methods for lists?",
        "explanation": """# List Methods: remove() vs pop()

`remove()` removes first occurrence of a value, `pop()` removes and returns element by index.

## Example:
```python
numbers = [1, 2, 3, 2, 4]

# remove() - removes by value
numbers.remove(2)  # Removes first occurrence of 2
print(numbers)     # [1, 3, 2, 4]

# pop() - removes by index and returns value
numbers = [1, 2, 3, 4, 5]
last = numbers.pop()      # Removes last element
print(last)               # 5
print(numbers)            # [1, 2, 3, 4]

second = numbers.pop(1)   # Removes element at index 1
print(second)             # 2
print(numbers)            # [1, 3, 4]
```

`remove()` for value removal, `pop()` for index-based removal with return value.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists",
        "points": 1,
        "answers": [
            {"text": "remove() removes by value, pop() removes by index", "is_correct": True},
            {"text": "Both remove by value", "is_correct": False},
            {"text": "remove() removes by index, pop() removes by value", "is_correct": False},
            {"text": "pop() is faster than remove()", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of f-strings in Python?",
        "explanation": """# F-strings (Formatted String Literals)

F-strings provide a readable and efficient way to format strings with embedded expressions.

## Example:
```python
name = "Alice"
age = 25
score = 95.75

# F-string formatting
message = f"Hello {name}, you are {age} years old!"
print(message)  # Hello Alice, you are 25 years old!

# Expressions inside f-strings
print(f"Score: {score:.1f}%")  # Score: 95.8%
print(f"Next year: {age + 1}")  # Next year: 26

# Comparison with other methods
# Old way: "Hello %s, age %d" % (name, age)
# .format(): "Hello {}, age {}".format(name, age)
# F-string: f"Hello {name}, age {age}"
```

More readable and faster than older string formatting methods.""",
        "reference": "https://docs.python.org/3/reference/lexical_analysis.html#f-strings",
        "points": 1,
        "answers": [
            {"text": "Efficient string formatting with embedded expressions", "is_correct": True},
            {"text": "File string operations", "is_correct": False},
            {"text": "Function string definitions", "is_correct": False},
            {"text": "Float string conversions", "is_correct": False},
        ],
    },
    {
        "text": """## List Slicing Question

**What is the output of the following code?**

```python
numbers = [0, 1, 2, 3, 4, 5]
result = numbers[::2]
print(result)
```

*Choose the correct output:*""",
        "explanation": """# List Slicing with Step

Slicing syntax `[start:end:step]` allows extracting elements with custom patterns.

## Slicing Examples:
```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[::2])    # [0, 2, 4] - every 2nd element
print(numbers[1::2])   # [1, 3, 5] - every 2nd starting from index 1
print(numbers[::-1])   # [5, 4, 3, 2, 1, 0] - reverse
print(numbers[2:5])    # [2, 3, 4] - from index 2 to 4
print(numbers[:3])     # [0, 1, 2] - first 3 elements
print(numbers[3:])     # [3, 4, 5] - from index 3 to end
```

Powerful feature for extracting patterns from sequences.""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#strings",
        "points": 1,
        "answers": [
            {"text": "[0, 2, 4]", "is_correct": True},
            {"text": "[1, 3, 5]", "is_correct": False},
            {"text": "[0, 1, 2, 3, 4, 5]", "is_correct": False},
            {"text": "[2, 4]", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between is and == when comparing None?",
        "explanation": """# None Comparison: is vs ==

Use `is` to check for None, not `==`. None is a singleton object with guaranteed identity.

## Example:
```python
value = None

# Correct way - using 'is'
if value is None:
    print("Value is None")

if value is not None:
    print("Value is not None")

# Incorrect way - using '=='
if value == None:  # Works but not recommended
    print("Value equals None")

# Why 'is' is preferred for None:
class AlwaysEqual:
    def __eq__(self, other):
        return True

obj = AlwaysEqual()
print(obj == None)    # True (misleading!)
print(obj is None)    # False (correct)
```

PEP 8 style guide recommends `is None` and `is not None`.""",
        "reference": "https://pep8.org/#programming-recommendations",
        "points": 1,
        "answers": [
            {"text": "Use 'is' for None comparison, not '=='", "is_correct": True},
            {"text": "Both are equivalent for None", "is_correct": False},
            {"text": "Use '==' for None comparison, not 'is'", "is_correct": False},
            {"text": "'is' is slower than '=='", "is_correct": False},
        ],
    },
    {
        "text": "What is the purpose of the any() and all() functions?",
        "explanation": """# Boolean Aggregation: any() and all()

`any()` returns True if any element is truthy, `all()` returns True if all elements are truthy.

## Example:
```python
# any() - True if at least one is True
print(any([False, False, True]))   # True
print(any([False, False, False]))  # False
print(any([]))                     # False (empty)

# all() - True if all are True
print(all([True, True, True]))     # True
print(all([True, False, True]))    # False
print(all([]))                     # True (empty - vacuous truth)

# Practical examples
numbers = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in numbers))  # True (all even)

scores = [85, 92, 78, 88]
print(any(score > 90 for score in scores))  # True (has high score)
```

Useful for checking conditions across collections.""",
        "reference": "https://docs.python.org/3/library/functions.html#any",
        "points": 1,
        "answers": [
            {"text": "any() checks if at least one is True, all() checks if all are True", "is_correct": True},
            {"text": "Both do the same thing", "is_correct": False},
            {"text": "any() counts True values, all() counts False values", "is_correct": False},
            {"text": "They convert lists to booleans", "is_correct": False},
        ],
    },
    {
        "text": """## Function Arguments Question

**What is the output of the following code?**

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

result = greet("Alice", "Hi")
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Function Default Arguments

Functions can have default parameter values that are used when arguments aren't provided.

## Example:
```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# Using default parameter
print(greet("Alice"))         # Hello, Alice!

# Overriding default parameter
print(greet("Bob", "Hi"))     # Hi, Bob!

# Positional and keyword arguments
print(greet("Charlie", message="Hey"))  # Hey, Charlie!
print(greet(message="Howdy", name="Dave"))  # Howdy, Dave!

# Mutable default arguments (avoid!)
def bad_function(items=[]):  # Don't do this
    items.append("new")
    return items

# Better approach
def good_function(items=None):
    if items is None:
        items = []
    items.append("new")
    return items
```

Default arguments provide flexibility and cleaner function calls.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#default-argument-values",
        "points": 1,
        "answers": [
            {"text": "Hi, Alice!", "is_correct": True},
            {"text": "Hello, Alice!", "is_correct": False},
            {"text": "Alice, Hi!", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": "What is the difference between break and continue statements?",
        "explanation": """# Loop Control: break vs continue

`break` exits the loop entirely, `continue` skips to the next iteration.

## Example:
```python
# break - exits loop
for i in range(10):
    if i == 5:
        break  # Loop stops here
    print(i)  # Prints: 0, 1, 2, 3, 4

print("After break loop")

# continue - skips iteration
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)  # Prints: 0, 1, 3, 4

# Practical example: processing valid data
numbers = [1, -2, 3, 0, 5, -1]
for num in numbers:
    if num <= 0:
        continue  # Skip non-positive numbers
    print(f"Processing: {num}")
```

Use `break` to exit early, `continue` to skip specific iterations.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops",
        "points": 1,
        "answers": [
            {"text": "break exits loop, continue skips to next iteration", "is_correct": True},
            {"text": "continue exits loop, break skips iteration", "is_correct": False},
            {"text": "Both exit the loop", "is_correct": False},
            {"text": "Both skip to next iteration", "is_correct": False},
        ],
    },
    {
        "text": "What is duck typing in Python?",
        "explanation": """# Duck Typing Philosophy

"If it walks like a duck and quacks like a duck, then it's a duck" - objects are used based on behavior, not type.

## Example:
```python
class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying!"

class Airplane:
    def quack(self):
        return "Plane sound!"
    
    def fly(self):
        return "Jet flying!"

def make_it_fly(thing):
    # Don't check type - just use it!
    print(thing.quack())
    print(thing.fly())

# Both work with the same function
duck = Duck()
plane = Airplane()

make_it_fly(duck)   # Works
make_it_fly(plane)  # Also works!

# Python's file-like objects example
import io
text_file = open("file.txt", "w")
string_io = io.StringIO()
# Both have write() method - both are "file-like"
```

Focus on what objects can do, not what they are.""",
        "reference": "https://docs.python.org/3/glossary.html#term-duck-typing",
        "points": 1,
        "answers": [
            {"text": "Using objects based on behavior, not explicit type", "is_correct": True},
            {"text": "A method of typing code faster", "is_correct": False},
            {"text": "A debugging technique", "is_correct": False},
            {"text": "A way to create duck objects", "is_correct": False},
        ],
    },
    {
        "text": """## Loop Output Question

**What is the output of the following code?**

```python
for i in range(3):
    for j in range(2):
        print(i, j, end=" ")
print()
```

*Choose the correct output:*""",
        "explanation": """# Nested Loops

Nested loops iterate through combinations of values from multiple ranges.

## Code Breakdown:
1. Outer loop: `i` takes values 0, 1, 2
2. Inner loop: `j` takes values 0, 1 for each `i`
3. `print(i, j, end=" ")` prints values separated by space
4. Final `print()` adds a newline

## Execution Flow:
- i=0, j=0: prints "0 0 "
- i=0, j=1: prints "0 1 "
- i=1, j=0: prints "1 0 "
- i=1, j=1: prints "1 1 "
- i=2, j=0: prints "2 0 "
- i=2, j=1: prints "2 1 "

Result: "0 0 0 1 1 0 1 1 2 0 2 1 " followed by newline.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#for-statements",
        "points": 1,
        "answers": [
            {"text": "0 0 0 1 1 0 1 1 2 0 2 1", "is_correct": True},
            {"text": "0 1 2 0 1 2", "is_correct": False},
            {"text": "0 0 1 1 2 2", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## List Comprehension Output

**What is the output of the following code?**

```python
result = [x**2 for x in range(5) if x % 2 == 1]
print(result)
```

*Choose the correct output:*""",
        "explanation": """# List Comprehension with Condition

List comprehensions can include conditions to filter elements.

## Code Breakdown:
1. `range(5)` produces: 0, 1, 2, 3, 4
2. `if x % 2 == 1` filters odd numbers: 1, 3
3. `x**2` squares each filtered number: 1²=1, 3²=9

## Step by step:
- x=0: 0%2==0 (even) → skip
- x=1: 1%2==1 (odd) → 1² = 1 → include
- x=2: 2%2==0 (even) → skip
- x=3: 3%2==1 (odd) → 3² = 9 → include
- x=4: 4%2==0 (even) → skip

Result: [1, 9]""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions",
        "points": 1,
        "answers": [
            {"text": "[1, 9]", "is_correct": True},
            {"text": "[0, 1, 4, 9, 16]", "is_correct": False},
            {"text": "[1, 4, 9]", "is_correct": False},
            {"text": "[1, 3]", "is_correct": False},
        ],
    },
    {
        "text": """## String Formatting Output

**What is the output of the following code?**

```python
name = "Python"
version = 3.9
print(f"{name} {version:.1f}")
```

*Choose the correct output:*""",
        "explanation": """# F-string Number Formatting

F-strings support format specifications for precise number display.

## Format Breakdown:
- `{name}` - displays string as-is: "Python"
- `{version:.1f}` - formats float with 1 decimal place
  - `version = 3.9`
  - `.1f` means 1 decimal place in fixed-point notation
  - Result: "3.9"

## Other Format Examples:
```python
pi = 3.14159
print(f"{pi:.2f}")    # 3.14
print(f"{pi:.0f}")    # 3
print(f"{100:05d}")   # 00100
print(f"{'text':>10}") # "      text"
```

F-strings provide powerful formatting capabilities.""",
        "reference": "https://docs.python.org/3/reference/lexical_analysis.html#f-strings",
        "points": 1,
        "answers": [
            {"text": "Python 3.9", "is_correct": True},
            {"text": "Python 3.90", "is_correct": False},
            {"text": "Python 3", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Exception Handling Output

**What is the output of the following code?**

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid number")
except:
    print("Other error")
else:
    print("Success")
finally:
    print("Done")
```

*Choose the correct output:*""",
        "explanation": """# Exception Handling Flow

Exception handling follows specific execution order based on what occurs.

## Code Analysis:
1. `int("abc")` raises `ValueError` (can't convert "abc" to integer)
2. First `except ValueError:` catches the exception
3. Prints "Invalid number"
4. `else` block is skipped (only runs if NO exception)
5. `finally` always executes for cleanup

## Exception Hierarchy:
- Specific exceptions should come before general ones
- `else` only runs when no exception occurs
- `finally` always runs regardless of exceptions

Output: "Invalid number" followed by "Done" """,
        "reference": "https://docs.python.org/3/tutorial/errors.html",
        "points": 1,
        "answers": [
            {"text": "Invalid number\\nDone", "is_correct": True},
            {"text": "Other error\\nDone", "is_correct": False},
            {"text": "Success\\nDone", "is_correct": False},
            {"text": "Done", "is_correct": False},
        ],
    },
    {
        "text": """## Class Method Output

**What is the output of the following code?**

```python
class Counter:
    count = 0
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count

c1 = Counter()
c2 = Counter()
print(Counter.get_count())
```

*Choose the correct output:*""",
        "explanation": """# Class Variables and Class Methods

Class variables are shared among all instances of a class.

## Code Analysis:
1. `Counter.count = 0` - class variable shared by all instances
2. `__init__` increments class variable when new instance created
3. `c1 = Counter()` - creates instance, count becomes 1
4. `c2 = Counter()` - creates instance, count becomes 2
5. `@classmethod` can access class variables via `cls`
6. `Counter.get_count()` returns current count: 2

## Class vs Instance Variables:
```python
class Example:
    class_var = 0      # Shared by all instances
    
    def __init__(self):
        self.instance_var = 0  # Unique to each instance
```

Class methods work with class-level data.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables",
        "points": 1,
        "answers": [
            {"text": "2", "is_correct": True},
            {"text": "0", "is_correct": False},
            {"text": "1", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Dictionary Comprehension Output

**What is the output of the following code?**

```python
words = ["apple", "banana", "cherry"]
result = {word: len(word) for word in words if len(word) > 5}
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Dictionary Comprehension with Condition

Dictionary comprehensions create dictionaries with key-value pairs based on iterables.

## Code Breakdown:
1. Iterate through words: ["apple", "banana", "cherry"]
2. Condition `if len(word) > 5` filters words
3. Create key-value pairs: `word: len(word)`

## Length Check:
- "apple": len=5 → 5 > 5? False → skip
- "banana": len=6 → 6 > 5? True → include "banana": 6
- "cherry": len=6 → 6 > 5? True → include "cherry": 6

## Dictionary Comprehension Syntax:
```python
{key_expr: value_expr for item in iterable if condition}
```

Result: {"banana": 6, "cherry": 6}""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#dictionaries",
        "points": 1,
        "answers": [
            {"text": "{'banana': 6, 'cherry': 6}", "is_correct": True},
            {"text": "{'apple': 5, 'banana': 6, 'cherry': 6}", "is_correct": False},
            {"text": "{'banana': 6}", "is_correct": False},
            {"text": "{6, 6}", "is_correct": False},
        ],
    },
    {
        "text": """## Lambda Function Output

**What is the output of the following code?**

```python
numbers = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Filter Function with Lambda

`filter()` creates an iterator with elements for which the function returns True.

## Code Analysis:
1. `lambda x: x % 2 == 0` - returns True for even numbers
2. `filter()` applies lambda to each element in numbers
3. Keep only elements where lambda returns True

## Element-by-element:
- 1: 1 % 2 == 0? False → filter out
- 2: 2 % 2 == 0? True → keep
- 3: 3 % 2 == 0? False → filter out  
- 4: 4 % 2 == 0? True → keep
- 5: 5 % 2 == 0? False → filter out

## Filter Function:
- Returns iterator, convert to list with `list()`
- Only includes elements where function returns truthy value

Result: [2, 4]""",
        "reference": "https://docs.python.org/3/library/functions.html#filter",
        "points": 1,
        "answers": [
            {"text": "[2, 4]", "is_correct": True},
            {"text": "[1, 3, 5]", "is_correct": False},
            {"text": "[1, 2, 3, 4, 5]", "is_correct": False},
            {"text": "[True, False, True, False, True]", "is_correct": False},
        ],
    },
    {
        "text": """## String Method Chaining Output

**What is the output of the following code?**

```python
text = "Hello World"
result = text.lower().replace("l", "x").upper()
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Method Chaining on Strings

String methods can be chained together, executing left to right.

## Step-by-step Execution:
1. `text = "Hello World"`
2. `.lower()` → "hello world"
3. `.replace("l", "x")` → "hexxo worxd" (all 'l' replaced with 'x')
4. `.upper()` → "HEXXO WORXD"

## Method Chaining:
Each string method returns a new string, allowing chaining:
```python
original = "Hello"
# These are equivalent:
result1 = original.lower().upper()
temp = original.lower()
result2 = temp.upper()
```

String methods don't modify original string - they return new ones.

Final result: "HEXXO WORXD" """,
        "reference": "https://docs.python.org/3/library/stdtypes.html#string-methods",
        "points": 1,
        "answers": [
            {"text": "HEXXO WORXD", "is_correct": True},
            {"text": "HELLO WORLD", "is_correct": False},
            {"text": "hello world", "is_correct": False},
            {"text": "HeLLo WoRLd", "is_correct": False},
        ],
    },
    {
        "text": """## List Slicing Advanced Output

**What is the output of the following code?**

```python
numbers = [1, 2, 3, 4, 5, 6]
result = numbers[1:5:2]
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Advanced List Slicing with Step

Slicing syntax `[start:end:step]` extracts elements with custom patterns.

## Slicing Breakdown:
- `start=1`: begin at index 1 (value 2)
- `end=5`: stop before index 5 (don't include index 5)
- `step=2`: take every 2nd element

## Index Analysis:
```
Index: 0  1  2  3  4  5
Value: 1  2  3  4  5  6
       ↑  ↑     ↑     ↑
          ↑     ↑     end (excluded)
          ↑     selected (index 3)
          selected (index 1)
```

Elements at indices 1, 3: [2, 4]

## Slicing Examples:
- `[::2]` - every 2nd element from start
- `[1::2]` - every 2nd element starting from index 1  
- `[::-1]` - reverse the list""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#strings",
        "points": 1,
        "answers": [
            {"text": "[2, 4]", "is_correct": True},
            {"text": "[2, 3, 4, 5]", "is_correct": False},
            {"text": "[1, 3, 5]", "is_correct": False},
            {"text": "[2, 3, 4]", "is_correct": False},
        ],
    },
    {
        "text": """## Generator Expression Output

**What is the output of the following code?**

```python
gen = (x * 2 for x in range(3))
result = list(gen)
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Generator Expressions

Generator expressions create iterators that produce values on-demand.

## Code Analysis:
1. `(x * 2 for x in range(3))` creates generator (note parentheses)
2. `range(3)` produces: 0, 1, 2
3. Each value is doubled: 0*2=0, 1*2=2, 2*2=4
4. `list(gen)` converts generator to list

## Generator vs List Comprehension:
```python
# Generator expression (lazy)
gen = (x * 2 for x in range(3))

# List comprehension (eager)
lst = [x * 2 for x in range(3)]
```

Generators are memory-efficient for large datasets.

Result: [0, 2, 4]""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#generator-expressions",
        "points": 1,
        "answers": [
            {"text": "[0, 2, 4]", "is_correct": True},
            {"text": "(0, 2, 4)", "is_correct": False},
            {"text": "[0, 1, 2]", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Set Operations Advanced Output

**What is the output of the following code?**

```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.symmetric_difference(set2)
print(sorted(result))
```

*Choose the correct output:*""",
        "explanation": """# Set Symmetric Difference

Symmetric difference returns elements in either set, but not in both.

## Set Analysis:
- `set1 = {1, 2, 3}`
- `set2 = {2, 3, 4}`
- Common elements: {2, 3}
- Elements only in set1: {1}
- Elements only in set2: {4}
- Symmetric difference: {1, 4}

## Set Operations Comparison:
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1 & set2)  # {2, 3} intersection
print(set1 | set2)  # {1, 2, 3, 4} union
print(set1 - set2)  # {1} difference
print(set1 ^ set2)  # {1, 4} symmetric difference
```

`sorted()` converts set to sorted list for consistent output.""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset",
        "points": 1,
        "answers": [
            {"text": "[1, 4]", "is_correct": True},
            {"text": "[2, 3]", "is_correct": False},
            {"text": "[1, 2, 3, 4]", "is_correct": False},
            {"text": "[1]", "is_correct": False},
        ],
    },
    {
        "text": """## Tuple Unpacking Output

**What is the output of the following code?**

```python
data = (1, 2, 3, 4, 5)
a, b, *rest, c = data
print(a, b, c, rest)
```

*Choose the correct output:*""",
        "explanation": """# Extended Tuple Unpacking

Python supports advanced unpacking patterns with the `*` operator.

## Unpacking Analysis:
- `data = (1, 2, 3, 4, 5)` - 5 elements
- `a` gets first element: 1
- `b` gets second element: 2  
- `c` gets last element: 5
- `*rest` captures remaining middle elements: [3, 4]

## Unpacking Patterns:
```python
# Basic unpacking
x, y, z = (1, 2, 3)

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2, 3, 4], last=5

# Ignore values
a, _, c = (1, 2, 3)  # ignore middle value
```

The `*` collects remaining values into a list.""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences",
        "points": 1,
        "answers": [
            {"text": "1 2 5 [3, 4]", "is_correct": True},
            {"text": "1 2 3 [4, 5]", "is_correct": False},
            {"text": "1 2 5 (3, 4)", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Recursive Function Output

**What is the output of the following code?**

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

result = factorial(4)
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Recursive Function Execution

Recursion breaks down problems into smaller subproblems.

## Execution Trace:
1. `factorial(4)`
2. `4 * factorial(3)`
3. `4 * (3 * factorial(2))`
4. `4 * (3 * (2 * factorial(1)))`
5. `4 * (3 * (2 * 1))` (base case: n=1 returns 1)
6. `4 * (3 * 2)` = `4 * 6` = `24`

## Call Stack:
```
factorial(4) → 4 * factorial(3)
factorial(3) → 3 * factorial(2)  
factorial(2) → 2 * factorial(1)
factorial(1) → 1 (base case)
```

Working backwards: 1 → 2*1=2 → 3*2=6 → 4*6=24

Result: 24 (4! = 4×3×2×1 = 24)""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
        "points": 1,
        "answers": [
            {"text": "24", "is_correct": True},
            {"text": "10", "is_correct": False},
            {"text": "4", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Scope and Global Variables Output

**What is the output of the following code?**

```python
x = 10

def modify_x():
    global x
    x = 20
    return x

result = modify_x()
print(x, result)
```

*Choose the correct output:*""",
        "explanation": """# Global Keyword and Variable Scope

The `global` keyword allows modification of global variables inside functions.

## Code Analysis:
1. `x = 10` - global variable
2. `global x` - declares intention to modify global x
3. `x = 20` - modifies global x (not creating local variable)
4. `return x` - returns modified global value: 20
5. Global x is now 20

## Without Global:
```python
x = 10

def modify_x():
    x = 20  # Creates local variable, doesn't affect global
    return x

result = modify_x()  # 20
print(x)  # Still 10 (global unchanged)
```

Global keyword required to modify global variables in functions.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces",
        "points": 1,
        "answers": [
            {"text": "20 20", "is_correct": True},
            {"text": "10 20", "is_correct": False},
            {"text": "20 10", "is_correct": False},
            {"text": "10 10", "is_correct": False},
        ],
    },
    {
        "text": """## Default Mutable Argument Output

**What is the output of the following code?**

```python
def add_item(item, target_list=[]):
    target_list.append(item)
    return target_list

list1 = add_item("a")
list2 = add_item("b")
print(list1, list2)
```

*Choose the correct output:*""",
        "explanation": """# Mutable Default Arguments Pitfall

Mutable default arguments are evaluated once when function is defined, not each call.

## Dangerous Pattern:
The same list object `[]` is reused for every function call!

## Execution Flow:
1. `add_item("a")` - uses shared default list, appends "a" → ["a"]
2. `list2 = add_item("b")` - same list object, appends "b" → ["a", "b"]
3. Both `list1` and `list2` reference the same list object

## Safe Pattern:
```python
def add_item(item, target_list=None):
    if target_list is None:
        target_list = []  # New list each call
    target_list.append(item)
    return target_list
```

Avoid mutable defaults - use `None` and create new objects inside function.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#default-argument-values",
        "points": 1,
        "answers": [
            {"text": "['a', 'b'] ['a', 'b']", "is_correct": True},
            {"text": "['a'] ['b']", "is_correct": False},
            {"text": "['a'] ['a', 'b']", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## List Modification During Iteration Output

**What is the output of the following code?**

```python
numbers = [1, 2, 3, 4, 5]
for i, num in enumerate(numbers):
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)
```

*Choose the correct output:*""",
        "explanation": """# Modifying List During Iteration

Modifying a list while iterating can cause unexpected behavior and skipped elements.

## Execution Analysis:
- Initial: [1, 2, 3, 4, 5]
- i=0, num=1: odd, no removal → [1, 2, 3, 4, 5]  
- i=1, num=2: even, remove 2 → [1, 3, 4, 5]
- i=2, num=4: (skipped 3!) even, remove 4 → [1, 3, 5]
- i=3, num=5: odd, no removal → [1, 3, 5]

## Problem:
When element 2 is removed, list shifts left but iterator continues to next index, skipping element 3!

## Safe Alternatives:
```python
# Create new list
numbers = [num for num in numbers if num % 2 == 1]

# Iterate backwards  
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] % 2 == 0:
        numbers.pop(i)
```

Never modify list during forward iteration.""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#for-statements",
        "points": 1,
        "answers": [
            {"text": "[1, 3, 5]", "is_correct": True},
            {"text": "[1, 3]", "is_correct": False},
            {"text": "[2, 4]", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Closure Variable Output

**What is the output of the following code?**

```python
functions = []
for i in range(3):
    functions.append(lambda: i)

result = [f() for f in functions]
print(result)
```

*Choose the correct output:*""",
        "explanation": """# Late Binding Closure Issue

Lambda functions capture variables by reference, not value.

## Problem Analysis:
1. Loop creates 3 lambda functions: `lambda: i`
2. All lambdas reference the same variable `i`
3. After loop completes, `i = 2`
4. When lambdas are called, they all see `i = 2`

## Late Binding:
The variable `i` is resolved when lambda is called, not when created.

## Solutions:
```python
# Solution 1: Default argument
functions = [lambda x=i: x for i in range(3)]

# Solution 2: Closure with parameter
functions = [(lambda x: lambda: x)(i) for i in range(3)]

# Solution 3: functools.partial
from functools import partial
functions = [partial(lambda x: x, i) for i in range(3)]
```

Result: [2, 2, 2] - all functions return final loop value.""",
        "reference": "https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result",
        "points": 1,
        "answers": [
            {"text": "[2, 2, 2]", "is_correct": True},
            {"text": "[0, 1, 2]", "is_correct": False},
            {"text": "[0, 0, 0]", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """## Class Inheritance Output

**What is the output of the following code?**

```python
class Animal:
    sound = "Generic sound"
    
    def make_sound(self):
        return self.sound

class Dog(Animal):
    sound = "Woof"

dog = Dog()
print(dog.make_sound())
```

*Choose the correct output:*""",
        "explanation": """# Class Inheritance and Method Resolution

Child classes inherit attributes and methods from parent classes.

## Inheritance Analysis:
1. `Dog` inherits from `Animal`
2. `Dog` overrides class attribute `sound = "Woof"`
3. `Dog` inherits method `make_sound()` from `Animal`
4. `self.sound` in inherited method refers to `Dog.sound`

## Method Resolution Order (MRO):
1. Check instance attributes
2. Check class attributes (Dog.sound = "Woof")  
3. Check parent class attributes
4. Continue up inheritance chain

## Inheritance Examples:
```python
class Cat(Animal):
    pass  # Uses parent's sound = "Generic sound"

cat = Cat()
print(cat.make_sound())  # "Generic sound"
```

Result: "Woof" (Dog's overridden sound attribute)""",
        "reference": "https://docs.python.org/3/tutorial/classes.html#inheritance",
        "points": 1,
        "answers": [
            {"text": "Woof", "is_correct": True},
            {"text": "Generic sound", "is_correct": False},
            {"text": "Error", "is_correct": False},
            {"text": "None", "is_correct": False},
        ],
    },
    {
        "text": """## Multiple Assignment Output

**What is the output of the following code?**

```python
a = b = [1, 2, 3]
a.append(4)
print(a, b)
```

*Choose the correct output:*""",
        "explanation": """# Multiple Assignment with Mutable Objects

Multiple assignment with `=` creates references to the same object.

## Reference Analysis:
1. `a = b = [1, 2, 3]` creates one list object
2. Both `a` and `b` reference the same list object
3. `a.append(4)` modifies the shared list
4. Both variables see the change

## Memory Diagram:
```
a ──┐
    └─► [1, 2, 3, 4]
b ──┘
```

## To Create Separate Lists:
```python
a = [1, 2, 3]
b = [1, 2, 3]  # Different objects
# or
a = [1, 2, 3]
b = a.copy()   # Create separate copy
```

Result: [1, 2, 3, 4] [1, 2, 3, 4] (both reference same modified list)""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists",
        "points": 1,
        "answers": [
            {"text": "[1, 2, 3, 4] [1, 2, 3, 4]", "is_correct": True},
            {"text": "[1, 2, 3, 4] [1, 2, 3]", "is_correct": False},
            {"text": "[1, 2, 3] [1, 2, 3, 4]", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
]
