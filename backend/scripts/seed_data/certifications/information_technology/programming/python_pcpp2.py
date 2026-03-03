"""Python Institute PCPP-2 Certification"""

CERTIFICATION = {
    "name": "Python Institute PCPP-2",
    "description": "Python Certified Professional Programmer Level 2",
    "slug": "python-pcpp2",
    "level": "Expert",
    "duration": 65,
    "questions_count": 20,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": """What is the output of this advanced metaclass code?

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
print(db1 is db2)
```""",
        "explanation": """This implements the Singleton pattern using metaclasses.
The metaclass ensures only one instance of Database exists by 
overriding __call__. Both db1 and db2 refer to the same object.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "True", "is_correct": True},
            {"text": "False", "is_correct": False},
            {"text": "None", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of __slots__ memory optimization?""",
        "explanation": """__slots__ prevents the creation of __dict__ for 
instances, using a fixed-size array instead. This saves memory 
and can improve attribute access speed.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Faster method calls", "is_correct": False},
            {"text": "Memory optimization and attribute restriction", 
             "is_correct": True},
            {"text": "Better inheritance", "is_correct": False},
            {"text": "Thread safety", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this descriptor code?

```python
class Validator:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return obj.__dict__[self.name]
    
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Must be string")
        obj.__dict__[self.name] = value.upper()

class Person:
    name = Validator('name')
    
    def __init__(self, name):
        self.name = name

p = Person("alice")
print(p.name)
```""",
        "explanation": """This descriptor validates and transforms data 
on assignment. The setter converts strings to uppercase, so 'alice'
becomes 'ALICE'.""",
        "reference": "https://docs.python.org/3/howto/descriptor.html",
        "points": 1,
        "answers": [
            {"text": "alice", "is_correct": False},
            {"text": "ALICE", "is_correct": True},
            {"text": "None", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between __new__ and __init__?""",
        "explanation": """__new__ is responsible for creating and returning 
a new instance, while __init__ initializes an already-created instance.
__new__ is called first and is a static method.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "__new__ initializes, __init__ creates", "is_correct": False},
            {"text": "__new__ creates instance, __init__ initializes", 
             "is_correct": True},
            {"text": "No difference", "is_correct": False},
            {"text": "__init__ runs first", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this advanced async code?

```python
import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    return f"Task {name} done"

async def main():
    results = await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
        return_exceptions=True
    )
    for r in results:
        print(r)

asyncio.run(main())
```""",
        "explanation": """asyncio.gather() runs tasks concurrently and 
returns results in the order they were passed (not completion order).
All tasks complete despite different delays.""",
        "reference": "https://docs.python.org/3/library/asyncio-task.html",
        "points": 1,
        "answers": [
            {"text": "Task B done\\nTask A done\\nTask C done", "is_correct": False},
            {"text": "Task A done\\nTask B done\\nTask C done", "is_correct": True},
            {"text": "Task C done\\nTask A done\\nTask B done", "is_correct": False},
            {"text": "Random order", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of the @functools.lru_cache decorator?""",
        "explanation": """@lru_cache implements memoization by caching 
function results based on arguments. It uses a Least Recently Used 
eviction policy to limit memory usage.""",
        "reference": "https://docs.python.org/3/library/functools.html",
        "points": 1,
        "answers": [
            {"text": "Caches function results for performance", "is_correct": True},
            {"text": "Makes functions thread-safe", "is_correct": False},
            {"text": "Validates function arguments", "is_correct": False},
            {"text": "Logs function calls", "is_correct": False},
        ],
    },
    {
        "text": """What is the Global Interpreter Lock (GIL)?""",
        "explanation": """The GIL is a mutex that allows only one thread 
to execute Python bytecode at a time. It limits true parallelism 
for CPU-bound tasks but doesn't affect I/O-bound operations.""",
        "reference": "https://docs.python.org/3/glossary.html#term-GIL",
        "points": 1,
        "answers": [
            {"text": "A memory management feature", "is_correct": False},
            {"text": "A lock that limits thread parallelism", "is_correct": True},
            {"text": "A garbage collection mechanism", "is_correct": False},
            {"text": "A debugging tool", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this weakref code?

```python
import weakref
import gc

class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass("test")
weak_ref = weakref.ref(obj)

print(weak_ref() is not None)
del obj
gc.collect()
print(weak_ref() is not None)
```""",
        "explanation": """Weak references don't prevent garbage collection.
After deleting obj and running gc.collect(), the object is destroyed
and the weak reference returns None.""",
        "reference": "https://docs.python.org/3/library/weakref.html",
        "points": 1,
        "answers": [
            {"text": "True\\nTrue", "is_correct": False},
            {"text": "True\\nFalse", "is_correct": True},
            {"text": "False\\nFalse", "is_correct": False},
            {"text": "False\\nTrue", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between multiprocessing and threading?""",
        "explanation": """Multiprocessing creates separate processes with 
their own memory space, avoiding GIL limitations. Threading shares 
memory but is limited by GIL for CPU-bound tasks.""",
        "reference": "https://docs.python.org/3/library/multiprocessing.html",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "Multiprocessing avoids GIL, threading doesn't", 
             "is_correct": True},
            {"text": "Threading is always faster", "is_correct": False},
            {"text": "Multiprocessing can't share data", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this generator delegation code?

```python
def inner_gen():
    yield 1
    yield 2

def outer_gen():
    yield from inner_gen()
    yield 3

gen = outer_gen()
print(list(gen))
```""",
        "explanation": """The 'yield from' syntax delegates to another 
generator, yielding all its values. The output combines values 
from inner_gen() followed by the final yield.""",
        "reference": "https://docs.python.org/3/reference/expressions.html",
        "points": 1,
        "answers": [
            {"text": "[1, 2, 3]", "is_correct": True},
            {"text": "[3, 1, 2]", "is_correct": False},
            {"text": "[[1, 2], 3]", "is_correct": False},
            {"text": "[1, 2]", "is_correct": False},
        ],
    },
    {
        "text": """What is monkey patching in Python?""",
        "explanation": """Monkey patching is the dynamic modification of 
classes or modules at runtime by changing their attributes or methods.
It's powerful but can make code harder to understand.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "A testing technique", "is_correct": False},
            {"text": "Runtime modification of classes/modules", "is_correct": True},
            {"text": "A design pattern", "is_correct": False},
            {"text": "Error handling", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this advanced property code?

```python
class Temperature:
    def __init__(self):
        self._celsius = 0
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

t = Temperature()
t.fahrenheit = 100
print(f"{t._celsius:.1f}")
```""",
        "explanation": """Properties allow computed attributes with custom 
getters and setters. Setting fahrenheit to 100 converts to celsius 
using the formula (F - 32) * 5/9.""",
        "reference": "https://docs.python.org/3/library/functions.html",
        "points": 1,
        "answers": [
            {"text": "37.8", "is_correct": True},
            {"text": "100.0", "is_correct": False},
            {"text": "0.0", "is_correct": False},
            {"text": "32.0", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of __enter__ and __exit__ methods?""",
        "explanation": """These methods implement the context manager protocol
for the 'with' statement. __enter__ sets up the context, __exit__ 
handles cleanup and exception management.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Class inheritance", "is_correct": False},
            {"text": "Context manager protocol for 'with' statements", 
             "is_correct": True},
            {"text": "Iterator protocol", "is_correct": False},
            {"text": "Exception handling", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this multiple inheritance MRO code?

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D().method())
print([cls.__name__ for cls in D.__mro__])
```""",
        "explanation": """Python uses C3 linearization for Method Resolution 
Order (MRO). D inherits from B first, so B's method is called. 
The MRO follows the inheritance hierarchy.""",
        "reference": "https://docs.python.org/3/tutorial/classes.html",
        "points": 1,
        "answers": [
            {"text": "B\\n['D', 'B', 'C', 'A', 'object']", "is_correct": True},
            {"text": "C\\n['D', 'C', 'B', 'A', 'object']", "is_correct": False},
            {"text": "A\\n['D', 'A', 'B', 'C', 'object']", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """What is the difference between copy.copy() and copy.deepcopy()?""",
        "explanation": """copy.copy() creates a shallow copy (new object, 
but references to nested objects). copy.deepcopy() creates a deep 
copy (recursively copies all nested objects).""",
        "reference": "https://docs.python.org/3/library/copy.html",
        "points": 1,
        "answers": [
            {"text": "No difference", "is_correct": False},
            {"text": "Shallow vs deep copying of nested objects", "is_correct": True},
            {"text": "Speed difference only", "is_correct": False},
            {"text": "Different syntax only", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of __call__ method in classes?""",
        "explanation": """__call__ makes instances of a class callable 
like functions. When you call obj(), Python invokes obj.__call__().
Useful for creating function-like objects.""",
        "reference": "https://docs.python.org/3/reference/datamodel.html",
        "points": 1,
        "answers": [
            {"text": "Initialize objects", "is_correct": False},
            {"text": "Make instances callable like functions", "is_correct": True},
            {"text": "Handle method calls", "is_correct": False},
            {"text": "Create class instances", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this advanced exception handling code?

```python
class CustomError(Exception):
    pass

try:
    try:
        raise CustomError("Inner error")
    except CustomError as e:
        print(f"Caught: {e}")
        raise ValueError("Outer error") from e
except ValueError as e:
    print(f"Outer: {e}")
    print(f"Cause: {e.__cause__}")
```""",
        "explanation": """The 'raise ... from' syntax creates an exception 
chain. The original exception becomes the __cause__ of the new one,
preserving the error context.""",
        "reference": "https://docs.python.org/3/tutorial/errors.html",
        "points": 1,
        "answers": [
            {"text": "Caught: Inner error\\nOuter: Outer error\\n"
                     "Cause: Inner error", "is_correct": True},
            {"text": "Caught: Inner error\\nOuter: Outer error\\n"
                     "Cause: None", "is_correct": False},
            {"text": "Only: Outer: Outer error", "is_correct": False},
            {"text": "Error", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of collections.namedtuple?""",
        "explanation": """namedtuple creates tuple subclasses with named 
fields, combining memory efficiency of tuples with readability of 
named attributes. Fields are accessible by name or index.""",
        "reference": "https://docs.python.org/3/library/collections.html",
        "points": 1,
        "answers": [
            {"text": "Creates mutable tuples", "is_correct": False},
            {"text": "Creates tuples with named, accessible fields", 
             "is_correct": True},
            {"text": "Creates nested data structures", "is_correct": False},
            {"text": "Creates ordered dictionaries", "is_correct": False},
        ],
    },
    {
        "text": """What is the output of this dataclass code?

```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int = 0
    scores: list = field(default_factory=list)

p1 = Person("Alice")
p2 = Person("Bob")
p1.scores.append(100)
print(len(p2.scores))
```""",
        "explanation": """dataclasses with default_factory create new 
instances for each object, avoiding shared mutable defaults. 
p1 and p2 have separate lists.""",
        "reference": "https://docs.python.org/3/library/dataclasses.html",
        "points": 1,
        "answers": [
            {"text": "0", "is_correct": True},
            {"text": "1", "is_correct": False},
            {"text": "Error", "is_correct": False},
            {"text": "None", "is_correct": False},
        ],
    },
    {
        "text": """What is the purpose of functools.wraps decorator?""",
        "explanation": """@functools.wraps preserves the original function's
metadata (name, docstring, annotations) when creating decorators.
Essential for proper decorator implementation.""",
        "reference": "https://docs.python.org/3/library/functools.html",
        "points": 1,
        "answers": [
            {"text": "Wraps function calls", "is_correct": False},
            {"text": "Preserves original function metadata", "is_correct": True},
            {"text": "Handles exceptions", "is_correct": False},
            {"text": "Validates arguments", "is_correct": False},
        ],
    },
]