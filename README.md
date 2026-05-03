# Python Core Concepts

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-OOP%20%7C%20DSA%20%7C%20File%20Handling%20%7C%20Decorators-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A comprehensive, topic-modular Python reference repository covering core language fundamentals through advanced paradigms including OOP, functional programming constructs, built-in data structures, file I/O, and exception handling. Each module is structured as an isolated, self-documented script with inline examples — designed for iterative exploration rather than linear execution.

---

## Table of Contents

- [Repository Structure](#repository-structure)
- [Module Breakdown](#module-breakdown)
- [Key Concepts & Implementations](#key-concepts--implementations)
- [Executable Entrypoints](#executable-entrypoints)
- [Prerequisites & Setup](#prerequisites--setup)
- [Usage](#usage)
- [Learning Progression](#learning-progression)
- [Author](#author)

---

## Repository Structure

```bash
tanishq-mathur35-python-core-concepts/
├── Advanced_Python.py              # Higher-order functions, decorators, comprehensions
├── Basics.py                       # Primitive types, type coercion, string operations, I/O
├── conditionals.py                 # Branching logic, ternary expressions, nested conditions
├── exception_handling.py           # Structured error handling, custom exception raising
├── for_loops.py                    # Iteration constructs, loop control statements
├── for_loops_questions.py          # 10 algorithmic problems solved via for-loop iteration
├── functions.py                    # Function signatures, argument types, return semantics
├── operators.py                    # Operator categories, precedence, comparison on strings
├── random_number.py                # CLI game — random number guessing with input validation
├── while_loops.py                  # Condition-driven loops, digit extraction, reversal
│
├── Data_Structures/
│   ├── dictionary.py               # Hash map operations, traversal, built-in dict methods
│   ├── dictionary_questions.py     # Merge strategies, value aggregation, frequency maps
│   ├── list.py                     # Dynamic array operations, all list methods with examples
│   ├── list_questions.py           # Linear search, max/2nd-max, sort validation
│   ├── set.py                      # Hash-set operations, set algebra (union, intersection, diff)
│   └── tuple.py                    # Immutable sequences, packing/unpacking, tuple methods
│
├── File_Handling/
│   ├── basic.py                    # Low-level file I/O using built-in open()
│   ├── hello.txt                   # Sample flat file for read/write demonstrations
│   └── Project/
│       └── main.py                 # Full CRUD CLI file manager built with pathlib.Path
│
├── OOPS/
│   ├── main.py                     # Class anatomy — attributes, constructors, method types
│   ├── inheritance.py              # Single, multiple, and multilevel inheritance with super()
│   ├── polymorphism.py             # Runtime polymorphism via method overriding and duck typing
│   ├── encapsulation.py            # Access modifiers — protected (_) and private (__) members
│   ├── abstraction.py              # Abstract base classes via abc.ABC and @abstractmethod
│   └── dunder_methods.py           # Operator overloading with __str__, __add__
│
└── package/
    ├── maths.py                    # Custom importable module — arithmetic operations
    └── hello.py                    # Custom importable module — greeting utility
```

---

## Module Breakdown

### `Basics.py`

Covers Python's primitive type system (`int`, `float`, `complex`, `str`, `bool`), implicit vs. explicit type conversion using built-in callables (`int()`, `str()`, `ord()`, `chr()`, `bool()`), string indexing, step-based slicing, formatted string literals (`f-strings`), and raw string literals.

### `operators.py`

Demonstrates all operator categories: arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), augmented assignment (`+=`, `-=`, etc.), comparison operators including Unicode-based string comparison via `ord()`, and short-circuit evaluation in logical operators (`and`, `or`, `not`).

### `conditionals.py`

Implements conditional branching using `if-elif-else` chains, nested conditionals, and inline ternary expressions. Includes a leap year checker using the compound divisibility rule: `year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)`.

### `for_loops.py` / `for_loops_questions.py`

Covers `range()`-based iteration with start, stop, and step arguments including negative steps. Loop control flow via `break`, `continue`, and `pass`. Practice problems include: sum of natural numbers, factorial computation, factor enumeration, perfect number check, prime number validation, string reversal, palindrome detection, and character/digit/special-character frequency count.

### `while_loops.py`

Condition-based iteration with integer decomposition problems: extracting individual digits using modulo arithmetic, reversing an integer, and palindrome checking on numeric input.

### `functions.py`

Covers function definition and invocation, all argument-passing conventions (positional, keyword, default), variadic arguments via `*args` and `**kwargs`, and the `return` statement. Includes a palindrome checker implemented as a reusable function.

### `Advanced_Python.py`

Higher-order constructs including first-class decorator functions using the wrapper pattern, argument-aware decorators via `*args`/`**kwargs` forwarding, list comprehensions with conditional filters, dictionary comprehensions, `lambda` expressions, and the functional `map()` and `filter()` built-ins. Also covers custom package creation and usage of the built-in `math` module.

### `exception_handling.py`

Structured error handling using `try-except-else-finally` blocks with `Exception` as the base catch type. Demonstrates the `raise` keyword for programmatic exception triggering with custom error messages and `ValueError` as a specific exception type.

---

## Key Concepts & Implementations

### Data Structures

| Structure | Ordering  | Mutability | Duplicates  | Indexing | Internal Mechanism |
| --------- | --------- | ---------- | ----------- | -------- | ------------------ |
| `list`    | Ordered   | Mutable    | Allowed     | Yes      | Dynamic array      |
| `tuple`   | Ordered   | Immutable  | Allowed     | Yes      | Static array       |
| `set`     | Unordered | Mutable    | Not allowed | No       | Hash table         |
| `dict`    | Ordered\* | Mutable    | Keys unique | No       | Hash map           |

> \*Dictionaries maintain insertion order as of Python 3.7+

#### Set Algebra (`Data_Structures/set.py`)

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

a | b   # Union              → {1, 2, 3, 4, 5, 6, 7, 8}
a & b   # Intersection       → {4, 5}
a - b   # Difference         → {1, 2, 3}
a ^ b   # Symmetric Diff     → {1, 2, 3, 6, 7, 8}
```

### Object-Oriented Programming (`OOPS/`)

#### Inheritance Hierarchy

```
Animal (Base)
  └── Dog                     (Single Inheritance)

Factory (Base)
  └── JodhpurFactory
        └── MumbaiFactory     (Multilevel Inheritance)

Human + Animal
  └── Robots                  (Multiple Inheritance)
```

#### Abstraction via ABC

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass
```

Concrete subclasses (`Square`, `Circle`) must implement all abstract methods. Attempting to instantiate the abstract class directly raises `TypeError`.

#### Access Modifiers

```python
class Factory:
    _protected = "accessible in subclasses by convention"
    __private  = "name-mangled to _Factory__private by interpreter"
```

#### Operator Overloading via Dunder Methods

```python
def __add__(self, other):   # overloads the + operator between instances
def __str__(self):          # overloads str() cast and print() output
```

### File Handling (`File_Handling/`)

`basic.py` demonstrates low-level file I/O via the built-in `open()` function with mode flags (`r`, `w`, `a`).

`Project/main.py` implements a full CRUD CLI application using `pathlib.Path`:

| Operation | Method Used                | Mode |
| --------- | -------------------------- | ---- |
| Create    | `Path.exists()` + `open()` | `w`  |
| Read      | `open()` + `.read()`       | `r`  |
| Rename    | `Path.rename()`            | —    |
| Overwrite | `open()`                   | `w`  |
| Append    | `open()`                   | `a`  |
| Delete    | `Path.unlink()`            | —    |

### Decorator Pattern (`Advanced_Python.py`)

```python
def decorate(func):
    def wrapper(*args, **kwargs):
        print("pre-call logic")
        func(*args, **kwargs)
        print("post-call logic")
    return wrapper

@decorate
def addition(a, b, c):
    print(a + b + c)
```

The `wrapper` function intercepts the call, executes cross-cutting logic, and delegates to the original function — equivalent to the Gang of Four Decorator structural pattern.

---

## Executable Entrypoints

Most scripts are structured as **commented example blocks** intended to be uncommented and run selectively. The following files execute directly without modification:

| File                            | Description                                                             | Input Required                             |
| ------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------ |
| `random_number.py`              | CLI number guessing game with attempt counter and `ValueError` handling | Yes — integer guesses via stdin            |
| `while_loops.py`                | Prompts for an integer and checks its palindrome property               | Yes — integer via stdin                    |
| `File_Handling/Project/main.py` | Full CRUD file manager, menu-driven                                     | Yes — menu choices and filenames via stdin |
| `Data_Structures/set.py`        | Prints set algebra results for two hardcoded sets                       | No                                         |

---

## Prerequisites & Setup

**Requirements:**

- Python `3.7` or higher (`3.10+` recommended)
- No external dependencies — standard library only (`random`, `pathlib`, `abc`, `math`)

**Clone the repository:**

```bash
git clone https://github.com/tanishq-mathur35/python-core-concepts.git
cd tanishq-mathur35-python-core-concepts
```

**Verify Python version:**

```bash
python --version
```

---

## Usage

Run any top-level script directly:

```bash
python Basics.py
python Advanced_Python.py
python random_number.py
```

Run the file manager project:

```bash
python File_Handling/Project/main.py
```

Run data structure modules:

```bash
python Data_Structures/set.py
python Data_Structures/list.py
```

Run OOP modules:

```bash
python OOPS/inheritance.py
python OOPS/dunder_methods.py
```

> **Note:** Files containing only commented-out blocks produce no output until a block is uncommented. Each block is independently executable — uncomment the target section and run the file.

---

## Learning Progression

Recommended module sequence for systematic coverage:

```
Basics.py
  → operators.py
    → conditionals.py
      → for_loops.py → for_loops_questions.py
        → while_loops.py
          → functions.py
            → Advanced_Python.py
              → exception_handling.py
                → Data_Structures/ (list → tuple → set → dictionary)
                  → File_Handling/ (basic.py → Project/main.py)
                    → OOPS/ (main → inheritance → polymorphism → encapsulation → abstraction → dunder_methods)
```

---

## Author

**Tanishq Mathur**
[@tanishq-mathur35](https://github.com/tanishq-mathur35)
