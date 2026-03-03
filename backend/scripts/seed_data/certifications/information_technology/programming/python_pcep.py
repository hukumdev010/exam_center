"""Python Institute PCEP Certification"""

CERTIFICATION = {
    "name": "Python Institute PCEP",
    "description": "Python Certified Entry-level Programmer",
    "slug": "python-pcep",
    "level": "Entry",
    "duration": 45,
    "questions_count": 40,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "What is Python?",
        "explanation": """# Python Programming Language

**Python** is a high-level, interpreted, general-purpose programming language known for its simplicity and readability.

## Key Features:
- **High-level**: Abstract from complex details
- **Interpreted**: No compilation needed, runs directly
- **Object-oriented**: Supports classes and objects
- **Cross-platform**: Runs on Windows, Mac, Linux

## Examples:

### 1. Simple Program
```python
print("Hello, World!")
# Output: Hello, World!
```

### 2. Variables and Data Types
```python
name = "Alice"          # String
age = 25               # Integer
height = 5.6           # Float
is_student = True      # Boolean

print(f"Name: {name}, Age: {age}")
# Output: Name: Alice, Age: 25
```

### 3. Basic Operations
```python
# Arithmetic
x = 10 + 5    # 15
y = 20 - 8    # 12
z = 4 * 3     # 12

# String operations
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World
```""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html",
        "points": 1,
        "answers": [
            {"text": "A high-level programming language", "is_correct": True},
            {"text": "A database management system", "is_correct": False},
            {"text": "An operating system", "is_correct": False},
            {"text": "A web browser", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of print(bool(0))?",
        "explanation": """# Boolean Values in Python

**bool(0)** returns False because 0 is considered a **falsy** value in Python.

## Falsy Values:
- `False`, `0`, `0.0`
- Empty sequences: `""`, `[]`, `()`
- `None`

## Truthy Values:
- `True`, any non-zero number
- Non-empty sequences: `"hello"`, `[1, 2]`

## Examples:

### 1. Boolean Conversion
```python
print(bool(0))        # False
print(bool(1))        # True
print(bool(-5))       # True
print(bool(0.0))      # False
print(bool(3.14))     # True
```

### 2. Empty vs Non-empty
```python
print(bool(""))       # False (empty string)
print(bool("Hello"))  # True (non-empty string)
print(bool([]))       # False (empty list)
print(bool([1, 2]))   # True (non-empty list)
```

### 3. Practical Usage
```python
numbers = [1, 2, 3, 4, 5]

if numbers:  # Checks if list is not empty
    print("List has items")
else:
    print("List is empty")
# Output: List has items
```""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#truth",
        "points": 1,
        "answers": [
            {"text": "True", "is_correct": False},
            {"text": "False", "is_correct": True},
            {"text": "0", "is_correct": False},
            {"text": "None", "is_correct": False},
        ],
    },
    {
        "text": "Which method adds an element to the end of a list?",
        "explanation": """# List Methods in Python

**append()** method adds a single element to the end of a list.

## Common List Methods:
- `append()` - Add one element to end
- `extend()` - Add multiple elements
- `insert()` - Add at specific position
- `remove()` - Remove by value

## Examples:

### 1. Using append()
```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ["apple", "banana", "orange"]

# Append can add any data type
numbers = [1, 2, 3]
numbers.append(4)
numbers.append([5, 6])  # Adds entire list as one element
print(numbers)  # [1, 2, 3, 4, [5, 6]]
```

### 2. append() vs extend()
```python
# Using append() - adds as single element
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]]

# Using extend() - adds each element separately
list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # [1, 2, 3, 4, 5]
```

### 3. insert() for specific position
```python
colors = ["red", "blue"]
colors.insert(1, "green")  # Insert at index 1
print(colors)  # ["red", "green", "blue"]
```""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#more-on-lists",
        "points": 1,
        "answers": [
            {"text": "add()", "is_correct": False},
            {"text": "append()", "is_correct": True},
            {"text": "insert()", "is_correct": False},
            {"text": "extend()", "is_correct": False},
        ],
    },
    {
        "text": "What does the len() function return?",
        "explanation": """# len() Function in Python

**len()** function returns the **number of items** in a sequence or collection.

## Works with:
- Strings, lists, tuples, sets, dictionaries
- Any object that implements `__len__()` method

## Examples:

### 1. String Length
```python
text = "Hello World"
print(len(text))  # 11 (includes space)

name = "Python"
print(len(name))  # 6
```

### 2. List Length
```python
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # 5

empty_list = []
print(len(empty_list))  # 0
```

### 3. Dictionary Length
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print(len(student))  # 3 (number of key-value pairs)
```

### 4. Practical Usage
```python
# Check if list is empty
items = []
if len(items) == 0:
    print("No items found")

# Better way (more Pythonic)
if not items:
    print("No items found")

# Loop with length
words = ["hello", "world", "python"]
for i in range(len(words)):
    print(f"{i}: {words[i]}")
```""",
        "reference": "https://docs.python.org/3/library/functions.html#len",
        "points": 1,
        "answers": [
            {"text": "The length of an object", "is_correct": True},
            {"text": "The type of an object", "is_correct": False},
            {"text": "The value of an object", "is_correct": False},
            {"text": "The memory address", "is_correct": False},
        ],
    },
    {
        "text": "What is the correct way to create a comment in Python?",
        "explanation": """# Comments in Python

**Comments** in Python start with the `#` symbol. Everything after `#` on that line is ignored by the interpreter.

## Types of Comments:

### 1. Single-line Comments
```python
# This is a comment
print("Hello World")  # This is also a comment

# You can have multiple lines of comments
# Each line needs its own # symbol
x = 5  # Variable assignment
```

### 2. Multi-line Comments (using triple quotes)
```python
'''
This is a multi-line comment
using triple single quotes
'''

\"\"\"
This is also a multi-line comment
using triple double quotes
\"\"\"

def my_function():
    \"\"\"
    This is a docstring - special type of comment
    Used to document functions, classes, modules
    \"\"\"
    return "Hello"
```

### 3. Commenting Best Practices
```python
# Good: Explain WHY, not WHAT
total = price * tax_rate  # Apply local tax rate

# Bad: Just repeating what code does
x = x + 1  # Add 1 to x

# Good: Explain complex logic
# Calculate compound interest using A = P(1+r/n)^(nt)
amount = principal * (1 + rate/frequency) ** (frequency * time)
```""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator",
        "points": 1,
        "answers": [
            {"text": "// This is a comment", "is_correct": False},
            {"text": "/* This is a comment */", "is_correct": False},
            {"text": "# This is a comment", "is_correct": True},
            {"text": "<!-- This is a comment -->", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following is a valid Python variable name?",
        "explanation": """# Python Variable Naming Rules

**Valid variable names** in Python must follow specific rules and conventions.

## Rules (Required):
- Must start with letter (a-z, A-Z) or underscore (_)
- Can contain letters, numbers, and underscores
- Case-sensitive
- Cannot be Python keywords

## Examples:

### 1. Valid Names
```python
name = "Alice"           # lowercase
firstName = "Bob"        # camelCase
first_name = "Charlie"   # snake_case (preferred)
_private = "secret"      # starts with underscore
age2 = 25               # contains numbers
MAX_SIZE = 100          # constants (all uppercase)
```

### 2. Invalid Names
```python
# These will cause SyntaxError:
2name = "invalid"        # starts with number
first-name = "invalid"   # contains hyphen
class = "invalid"        # Python keyword
first name = "invalid"   # contains space
```

### 3. Python Keywords (Reserved)
```python
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 
#  'break', 'class', 'continue', 'def', 'del', 'elif', 
#  'else', 'except', 'finally', 'for', 'from', 'global', 
#  'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#  'not', 'or', 'pass', 'raise', 'return', 'try', 
#  'while', 'with', 'yield']
```

### 4. Naming Conventions
```python
# Variables and functions: snake_case
user_age = 25
def calculate_total():
    pass

# Constants: ALL_CAPS
PI = 3.14159
MAX_RETRIES = 5

# Classes: PascalCase
class StudentRecord:
    pass
```""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator",
        "points": 1,
        "answers": [
            {"text": "2name", "is_correct": False},
            {"text": "first-name", "is_correct": False},
            {"text": "first_name", "is_correct": True},
            {"text": "class", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of print(type(3.14))?",
        "explanation": """# Data Types in Python

**type()** function returns the data type of an object. `3.14` is a **float** (floating-point number).

## Basic Data Types:

### 1. Numeric Types
```python
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(2+3j))      # <class 'complex'>
```

### 2. Text Type
```python
print(type("Hello"))   # <class 'str'>
print(type('Python'))  # <class 'str'>
```

### 3. Boolean Type
```python
print(type(True))      # <class 'bool'>
print(type(False))     # <class 'bool'>
```

### 4. Sequence Types
```python
print(type([1, 2, 3]))      # <class 'list'>
print(type((1, 2, 3)))      # <class 'tuple'>
print(type(range(5)))       # <class 'range'>
```

### 5. Mapping Type
```python
print(type({"a": 1, "b": 2}))  # <class 'dict'>
```

### 6. Set Types
```python
print(type({1, 2, 3}))      # <class 'set'>
print(type(frozenset()))    # <class 'frozenset'>
```

### 7. Type Checking
```python
x = 3.14
print(isinstance(x, float))  # True
print(isinstance(x, int))    # False

# Check multiple types
y = 42
print(isinstance(y, (int, float)))  # True
```""",
        "reference": "https://docs.python.org/3/library/stdtypes.html",
        "points": 1,
        "answers": [
            {"text": "<class 'int'>", "is_correct": False},
            {"text": "<class 'float'>", "is_correct": True},
            {"text": "<class 'str'>", "is_correct": False},
            {"text": "<class 'number'>", "is_correct": False},
        ],
    },
    {
        "text": "Which operator is used for string concatenation in Python?",
        "explanation": """# String Concatenation in Python

**+ operator** is used to concatenate (join) strings in Python.

## String Operations:

### 1. Basic Concatenation
```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe

greeting = "Hello" + " " + "World"
print(greeting)   # Hello World
```

### 2. Multiple String Concatenation
```python
result = "Python" + " " + "is" + " " + "awesome"
print(result)  # Python is awesome

# With variables
language = "Python"
adjective = "powerful"
sentence = language + " is " + adjective + "!"
print(sentence)  # Python is powerful!
```

### 3. Alternative Methods
```python
# Using f-strings (Python 3.6+) - Recommended
name = "Alice"
age = 25
message = f"My name is {name} and I am {age} years old"

# Using format() method
message = "My name is {} and I am {} years old".format(name, age)

# Using join() for multiple strings
words = ["Python", "is", "great"]
sentence = " ".join(words)  # Python is great
```

### 4. Common Pitfalls
```python
# This works with strings
result = "5" + "3"
print(result)  # "53" (string concatenation)

# But this causes error with mixed types
# result = "Age: " + 25  # TypeError!

# Correct way:
age = 25
result = "Age: " + str(age)  # Convert to string first
# Or use f-string:
result = f"Age: {age}"
```""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#strings",
        "points": 1,
        "answers": [
            {"text": "&", "is_correct": False},
            {"text": "+", "is_correct": True},
            {"text": "*", "is_correct": False},
            {"text": ".", "is_correct": False},
        ],
    },
    {
        "text": "What will be the output of print(5 // 2)?",
        "explanation": """# Floor Division Operator (//) in Python

**// operator** performs **floor division**, returning the largest integer less than or equal to the division result.

## Division Operators:

### 1. Floor Division (//)
```python
print(5 // 2)    # 2 (floor division)
print(7 // 3)    # 2
print(10 // 4)   # 2
print(9 // 3)    # 3 (exact division)

# Works with negative numbers
print(-7 // 3)   # -3 (floors toward negative infinity)
print(7 // -3)   # -3
```

### 2. Regular Division (/)
```python
print(5 / 2)     # 2.5 (returns float)
print(7 / 3)     # 2.3333333333333335
print(10 / 4)    # 2.5
print(9 / 3)     # 3.0 (still returns float)
```

### 3. Modulo Operator (%)
```python
print(5 % 2)     # 1 (remainder)
print(7 % 3)     # 1
print(10 % 4)    # 2
print(9 % 3)     # 0 (no remainder)
```

### 4. Practical Examples
```python
# Calculate pages needed for items
total_items = 23
items_per_page = 5
pages = total_items // items_per_page + (1 if total_items % items_per_page > 0 else 0)
print(f"Need {pages} pages")  # Need 5 pages

# Time conversion
total_seconds = 3725
hours = total_seconds // 3600      # 1
minutes = (total_seconds % 3600) // 60  # 2
seconds = total_seconds % 60       # 5
print(f"{hours}:{minutes:02d}:{seconds:02d}")  # 1:02:05
```

### 5. Float Floor Division
```python
print(5.0 // 2.0)    # 2.0 (returns float)
print(7.5 // 2.5)    # 3.0
print(5.7 // 2)      # 2.0
```""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#numbers",
        "points": 1,
        "answers": [
            {"text": "2.5", "is_correct": False},
            {"text": "2", "is_correct": True},
            {"text": "3", "is_correct": False},
            {"text": "2.0", "is_correct": False},
        ],
    },
    {
        "text": "Which keyword is used to define a function in Python?",
        "explanation": """# Function Definition in Python

**def** keyword is used to define functions in Python.

## Function Syntax:
```python
def function_name(parameters):
    \"\"\"Optional docstring\"\"\"
    # Function body
    return value  # Optional
```

## Examples:

### 1. Simple Function
```python
def greet():
    print("Hello, World!")

greet()  # Call the function
# Output: Hello, World!
```

### 2. Function with Parameters
```python
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Hello, Alice!
greet_person("Bob")    # Hello, Bob!
```

### 3. Function with Return Value
```python
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print(sum_result)  # 8
```

### 4. Function with Default Parameters
```python
def introduce(name, age=25):
    return f"My name is {name} and I am {age} years old"

print(introduce("Alice"))         # Uses default age
print(introduce("Bob", 30))       # Uses provided age
```

### 5. Function with Multiple Return Values
```python
def get_name_age():
    name = "Charlie"
    age = 28
    return name, age  # Returns tuple

person_name, person_age = get_name_age()
print(f"{person_name} is {person_age} years old")
```

### 6. Function with Docstring
```python
def calculate_area(radius):
    \"\"\"
    Calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle
        
    Returns:
        float: The area of the circle
    \"\"\"
    return 3.14159 * radius ** 2
```""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#defining-functions",
        "points": 1,
        "answers": [
            {"text": "function", "is_correct": False},
            {"text": "def", "is_correct": True},
            {"text": "define", "is_correct": False},
            {"text": "func", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of print(range(3))?",
        "explanation": """# Range Object in Python

**range(3)** creates a range object, not a list. When printed, it shows the range representation.

## Range Function:

### 1. Basic Range Usage
```python
print(range(3))        # range(0, 3)
print(list(range(3)))  # [0, 1, 2] - Convert to list to see values

print(range(1, 5))     # range(1, 5)
print(list(range(1, 5)))  # [1, 2, 3, 4]
```

### 2. Range Parameters
```python
# range(stop)
print(list(range(5)))     # [0, 1, 2, 3, 4]

# range(start, stop)
print(list(range(2, 7)))  # [2, 3, 4, 5, 6]

# range(start, stop, step)
print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]
print(list(range(10, 0, -1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### 3. Range in Loops
```python
# Most common usage - for loops
for i in range(3):
    print(i)
# Output: 0, 1, 2

# Range with custom start/stop
for i in range(1, 4):
    print(f"Number: {i}")
# Output: Number: 1, Number: 2, Number: 3
```

### 4. Range Properties
```python
r = range(5)
print(len(r))     # 5
print(2 in r)     # True
print(5 in r)     # False

# Range is memory efficient
big_range = range(1000000)  # No memory used until accessed
```

### 5. Practical Examples
```python
# Generate index positions
items = ['apple', 'banana', 'orange']
for i in range(len(items)):
    print(f"{i}: {items[i]}")

# Countdown
for count in range(5, 0, -1):
    print(count)
print("Go!")
```""",
        "reference": "https://docs.python.org/3/library/stdtypes.html#range",
        "points": 1,
        "answers": [
            {"text": "[0, 1, 2]", "is_correct": False},
            {"text": "range(0, 3)", "is_correct": True},
            {"text": "(0, 1, 2)", "is_correct": False},
            {"text": "0 1 2", "is_correct": False},
        ],
    },
    {
        "text": "Which statement is used to exit from a loop in Python?",
        "explanation": """# Loop Control Statements in Python

**break** statement is used to exit/terminate a loop immediately.

## Loop Control Keywords:
- `break` - Exit loop completely
- `continue` - Skip current iteration, continue with next
- `pass` - Do nothing (placeholder)

## Examples:

### 1. Using break
```python
# Exit loop when condition met
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# Search and exit
numbers = [1, 3, 7, 2, 9, 5]
target = 7
for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")
```

### 2. Using continue
```python
# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip rest of loop body
    print(i)
# Output: 1, 3, 5, 7, 9

# Process only valid data
data = [1, -2, 3, 0, 5, -1]
for value in data:
    if value <= 0:
        continue  # Skip negative/zero values
    print(f"Processing: {value}")
```

### 3. Nested Loops with break
```python
# Break only exits innermost loop
for i in range(3):
    print(f"Outer loop: {i}")
    for j in range(3):
        if j == 1:
            break  # Only breaks inner loop
        print(f"  Inner loop: {j}")

# To break outer loop, use flag or function
found = False
for i in range(3):
    if found:
        break
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
```

### 4. While Loop with break
```python
count = 0
while True:  # Infinite loop
    count += 1
    print(count)
    if count >= 5:
        break  # Exit the loop
# Output: 1, 2, 3, 4, 5
```

### 5. Loop-else Clause
```python
# else executes if loop completes normally (no break)
for i in range(5):
    if i == 10:  # This condition never met
        break
else:
    print("Loop completed normally")  # This will execute

# With break
for i in range(5):
    if i == 3:
        break
else:
    print("This won't execute")  # Skipped due to break
```""",
        "reference": "https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements",
        "points": 1,
        "answers": [
            {"text": "exit", "is_correct": False},
            {"text": "break", "is_correct": True},
            {"text": "stop", "is_correct": False},
            {"text": "end", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of print('Python'[0])?",
        "explanation": """# String Indexing in Python

**String indexing** uses square brackets to access individual characters. Python uses **zero-based indexing**.

## String Indexing:

### 1. Positive Indexing
```python
text = "Python"
print(text[0])    # 'P' - First character
print(text[1])    # 'y' - Second character
print(text[2])    # 't' - Third character
print(text[5])    # 'n' - Last character
```

### 2. Negative Indexing
```python
text = "Python"
print(text[-1])   # 'n' - Last character
print(text[-2])   # 'o' - Second last
print(text[-6])   # 'P' - First character (same as [0])
```

### 3. String Slicing
```python
text = "Python"
print(text[0:3])   # 'Pyt' - Characters 0, 1, 2
print(text[2:])    # 'thon' - From index 2 to end
print(text[:4])    # 'Pyth' - From start to index 3
print(text[-3:])   # 'hon' - Last 3 characters
```

### 4. Step in Slicing
```python
text = "Python"
print(text[::2])   # 'Pto' - Every 2nd character
print(text[::-1])  # 'nohtyP' - Reverse string
print(text[1::2])  # 'yhn' - From index 1, every 2nd
```

### 5. Practical Examples
```python
email = "user@example.com"
username = email[:email.index('@')]  # 'user'
domain = email[email.index('@')+1:]  # 'example.com'

# Check file extension
filename = "document.pdf"
extension = filename[-4:]  # '.pdf'

# Get first and last characters
word = "Hello"
first_last = word[0] + word[-1]  # 'Ho'
```

### 6. Index Error Handling
```python
text = "Hi"
# print(text[5])  # IndexError: string index out of range

# Safe access
if len(text) > 5:
    print(text[5])
else:
    print("Index out of range")
```""",
        "reference": "https://docs.python.org/3/tutorial/introduction.html#strings",
        "points": 1,
        "answers": [
            {"text": "'P'", "is_correct": True},
            {"text": "'y'", "is_correct": False},
            {"text": "'Python'", "is_correct": False},
            {"text": "0", "is_correct": False},
        ],
    },
    {
        "text": "Which data structure is mutable in Python?",
        "explanation": """# Mutable vs Immutable Data Structures

**Lists** are mutable in Python, meaning their contents can be changed after creation.

## Mutable Types (Can be changed):
- **Lists** `[]`
- **Dictionaries** `{}`
- **Sets** `{}`

## Immutable Types (Cannot be changed):
- **Strings** `""`
- **Tuples** `()`
- **Numbers** (int, float)

## Examples:

### 1. Lists are Mutable
```python
# Lists can be modified
fruits = ["apple", "banana"]
fruits.append("orange")          # Add element
fruits[0] = "grape"              # Change element
fruits.remove("banana")          # Remove element
print(fruits)  # ['grape', 'orange']
```

### 2. Strings are Immutable
```python
# Strings cannot be modified
text = "Hello"
# text[0] = "h"  # TypeError: 'str' object doesn't support item assignment

# Create new string instead
text = "h" + text[1:]  # "hello"
new_text = text.replace("H", "h")  # Creates new string
```

### 3. Tuples are Immutable
```python
coordinates = (3, 4)
# coordinates[0] = 5  # TypeError: 'tuple' object doesn't support item assignment

# Create new tuple instead
coordinates = (5, 4)
```

### 4. Dictionaries are Mutable
```python
student = {"name": "Alice", "age": 20}
student["grade"] = "A"           # Add new key-value pair
student["age"] = 21              # Modify existing value
del student["name"]              # Remove key-value pair
print(student)  # {'age': 21, 'grade': 'A'}
```

### 5. Practical Implications
```python
# List modification affects all references
list1 = [1, 2, 3]
list2 = list1  # Both point to same list
list2.append(4)
print(list1)  # [1, 2, 3, 4] - Original list changed!

# String operations create new objects
str1 = "hello"
str2 = str1    # Both point to same string
str2 = str1.upper()  # Creates new string
print(str1)    # "hello" - Original unchanged
print(str2)    # "HELLO" - New string
```""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html",
        "points": 1,
        "answers": [
            {"text": "String", "is_correct": False},
            {"text": "List", "is_correct": True},
            {"text": "Tuple", "is_correct": False},
            {"text": "Integer", "is_correct": False},
        ],
    },
    {
        "text": "What keyword is used to check if a value exists in a sequence?",
        "explanation": """# Membership Operator 'in' in Python

**in** keyword is used to check if a value exists in a sequence (string, list, tuple, set, dictionary).

## Syntax:
```python
value in sequence    # Returns True/False
value not in sequence  # Returns True/False (opposite)
```

## Examples:

### 1. Lists and Tuples
```python
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)      # True
print(6 in numbers)      # False
print(6 not in numbers)  # True

colors = ("red", "blue", "green")
print("blue" in colors)    # True
print("yellow" in colors)  # False
```

### 2. Strings
```python
text = "Python programming"
print("Python" in text)     # True
print("Java" in text)       # False
print("gram" in text)       # True (substring)

# Case sensitive
print("python" in text)     # False (lowercase)
print("python" in text.lower())  # True
```

### 3. Dictionaries
```python
student = {"name": "Alice", "age": 25, "grade": "A"}

# Checks keys (not values)
print("name" in student)     # True
print("Alice" in student)    # False (it's a value, not key)

# To check values
print("Alice" in student.values())  # True

# To check key-value pairs
print(("name", "Alice") in student.items())  # True
```

### 4. Sets
```python
unique_numbers = {1, 2, 3, 4, 5}
print(3 in unique_numbers)   # True
print(6 in unique_numbers)   # False

# Sets provide O(1) lookup time
```

### 5. Practical Examples
```python
# Validate user input
valid_choices = ["yes", "no", "maybe"]
user_input = "yes"
if user_input in valid_choices:
    print("Valid choice")

# Check file extension
filename = "document.pdf"
allowed_extensions = [".pdf", ".doc", ".txt"]
if any(filename.endswith(ext) for ext in allowed_extensions):
    print("File type allowed")

# Filter data
emails = ["user1@gmail.com", "user2@yahoo.com", "user3@gmail.com"]
gmail_users = [email for email in emails if "@gmail.com" in email]
print(gmail_users)  # ['user1@gmail.com', 'user3@gmail.com']
```

### 6. Performance Considerations
```python
# List: O(n) time complexity
large_list = list(range(1000000))
print(500000 in large_list)  # Slower for large lists

# Set: O(1) time complexity
large_set = set(range(1000000))
print(500000 in large_set)   # Much faster
```""",
        "reference": "https://docs.python.org/3/reference/expressions.html#membership-test-operations",
        "points": 1,
        "answers": [
            {"text": "exists", "is_correct": False},
            {"text": "in", "is_correct": True},
            {"text": "contains", "is_correct": False},
            {"text": "has", "is_correct": False},
        ],
    },
    {
        "text": "What is the output of print({1, 2, 3} & {2, 3, 4})?",
        "explanation": """# Set Operations in Python

**& operator** performs set **intersection**, returning common elements between two sets.

## Set Operations:

### 1. Intersection (&)
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 & set2
print(result)  # {2, 3} - Common elements

# Alternative method
result = set1.intersection(set2)
print(result)  # {2, 3}
```

### 2. Union (|)
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 | set2
print(result)  # {1, 2, 3, 4} - All unique elements

# Alternative method
result = set1.union(set2)
print(result)  # {1, 2, 3, 4}
```

### 3. Difference (-)
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 - set2
print(result)  # {1} - Elements in set1 but not in set2

result = set2 - set1
print(result)  # {4} - Elements in set2 but not in set1
```

### 4. Symmetric Difference (^)
```python
set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1 ^ set2
print(result)  # {1, 4} - Elements in either set, but not in both

# Alternative method
result = set1.symmetric_difference(set2)
print(result)  # {1, 4}
```

### 5. Practical Examples
```python
# Find common interests
alice_hobbies = {"reading", "swimming", "coding"}
bob_hobbies = {"swimming", "gaming", "coding"}
common_hobbies = alice_hobbies & bob_hobbies
print(common_hobbies)  # {'swimming', 'coding'}

# Find unique skills
alice_skills = {"python", "sql", "excel"}
bob_skills = {"java", "sql", "powerbi"}
all_skills = alice_skills | bob_skills
print(all_skills)  # {'python', 'sql', 'excel', 'java', 'powerbi'}

# Find missing skills
required_skills = {"python", "sql", "excel", "powerbi"}
alice_missing = required_skills - alice_skills
print(alice_missing)  # {'powerbi'}
```

### 6. Set Comparisons
```python
set1 = {1, 2}
set2 = {1, 2, 3}

print(set1.issubset(set2))    # True - set1 is subset of set2
print(set2.issuperset(set1))  # True - set2 contains all of set1
print(set1.isdisjoint({3, 4}))  # True - no common elements
```""",
        "reference": "https://docs.python.org/3/tutorial/datastructures.html#sets",
        "points": 1,
        "answers": [
            {"text": "{1, 2, 3, 4}", "is_correct": False},
            {"text": "{2, 3}", "is_correct": True},
            {"text": "{1, 4}", "is_correct": False},
            {"text": "{1}", "is_correct": False},
        ],
    },
]