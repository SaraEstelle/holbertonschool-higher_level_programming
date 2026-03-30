# Python - Everything is Object

![Python](https://img.shields.io/badge/Python-3.8.5-blue?logo=python&logoColor=white)
![Holberton School](https://img.shields.io/badge/Holberton-School-red)
![License](https://img.shields.io/badge/License-MIT-green)

## 📚 Description

This project explores one of Python's most fundamental concepts: **everything is an object**.

Every value in Python — integers, strings, lists, functions, even `None` — is an object with:
- an **identity** (unique memory address, accessible via `id()`)
- a **type** (its class, accessible via `type()`)
- a **value** (its content)

Understanding the difference between **mutable** and **immutable** objects, how **references** and **aliases** work, and how Python **passes arguments to functions** is essential for writing correct, predictable Python code.

---

## 🧠 Learning Objectives

By the end of this project, you should be able to explain — without Google:

- What is an object
- The difference between a class and an object/instance
- The difference between mutable and immutable objects
- What is a reference, an assignment, and an alias
- How to check if two variables are identical (`is`) or point to the same object (`id()`)
- How to display the memory address of a variable
- What are the built-in mutable types
- What are the built-in immutable types
- How Python passes variables to functions

---

## 🗂️ Project Structure

```
python-everything_is_object/
├── README.md
├── 0-answer.txt         # type
├── 1-answer.txt         # id
├── 2-answer.txt         # No
├── 3-answer.txt         # Yes
├── 4-answer.txt         # Yes
├── 5-answer.txt         # No
├── 6-answer.txt         # True
├── 7-answer.txt         # True
├── 8-answer.txt         # True
├── 9-answer.txt         # False
├── 10-answer.txt        # True
├── 11-answer.txt        # False
├── 12-answer.txt        # True
├── 13-answer.txt        # True
├── 14-answer.txt        # [1, 2, 3, 4]
├── 15-answer.txt        # [1, 2, 3]
├── 16-answer.txt        # 1
├── 17-answer.txt        # [1, 2, 3, 4]
├── 18-answer.txt        # [1, 2, 3]
├── 19-copy_list.py      # Copy a list function
├── 20-answer.txt        # Yes
├── 21-answer.txt        # Yes
├── 22-answer.txt        # No
├── 23-answer.txt        # Yes
├── 24-answer.txt        # True
├── 25-answer.txt        # False
├── 26-answer.txt        # True
├── 27-answer.txt        # No
└── 28-answer.txt        # Yes
```

---

## ⚙️ Requirements

### Python Scripts
- Python 3.8.5 (Ubuntu 20.04 LTS)
- First line: `#!/usr/bin/python3`
- PEP 8 / pycodestyle 2.7.*
- All files must be executable
- All files must end with a new line

### Answer `.txt` Files
- One line only
- No shebang
- No leading or trailing spaces
- Must end with a new line

---

## 🔑 Key Concepts

### `==` vs `is`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True  → same value
print(a is b)   # False → different objects in memory
print(id(a) == id(b))  # False
```

### Mutable vs Immutable

| Immutable | Mutable |
|-----------|---------|
| `int`, `float`, `complex` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `bool`, `bytes`, `frozenset` | `bytearray` |

```python
# Immutable — creates a new object
a = "cat"
a = "dog"       # new object, original untouched

# Mutable — modifies in place
l = [1, 2, 3]
l[0] = 99       # same object, same id()
```

### Integer Interning (CPython)

CPython caches integers from **-5 to 256**:

```python
a = 89
b = 89
print(a is b)   # True  ← same cached object

a = 300
b = 300
print(a is b)   # False ← outside cache range
```

### The Alias Trap

```python
l1 = [1, 2, 3]
l2 = l1             # alias — same object!

l1.append(4)
print(l2)           # [1, 2, 3, 4] ← l2 is affected

# To avoid this, clone the list:
l2 = l1[:]          # or list(l1) or l1.copy()
```

### `+` vs `+=` on Lists

```python
l = [1, 2, 3]
l = l + [4]     # creates a NEW object → new id()
l += [4]        # mutates in place    → same id()
```

### Function Arguments

```python
# Immutable → no side effects
def increment(n):
    n += 1       # local reassignment, original unchanged

a = 1
increment(a)
print(a)        # 1 ← unchanged

# Mutable → side effects via mutation
def add_item(lst):
    lst.append(4)   # mutates the shared object

l = [1, 2, 3]
add_item(l)
print(l)        # [1, 2, 3, 4] ← modified!
```

---

## 📝 Task 19 — `copy_list` function

```python
#!/usr/bin/python3
def copy_list(a_list):
    return a_list[:]
```

**Usage:**
```bash
$ ./19-main.py
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]
True
False
```

---

## 📖 Blog Post

A detailed blog post covering all concepts from this project has been published:

- **Medium:** `https://medium.com/p/6cad9d9b3b64?postPublishedType=initial`

---

## 👤 Author

**SARA REBATI**
- GitHub: [@SaraEstelle](https://github.com/SaraEstelle)
- LinkedIn: [Sara Rebati](https://linkedin.com/in/)
- Holberton School

---

## 📄 License

This project is part of the Holberton School curriculum.