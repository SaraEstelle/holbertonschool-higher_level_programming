🐍 Python — More Classes and Objects

📑 Table of Contents

📚 Introduction

🎯 Learning Objectives

📁 Project Structure

🧠 Key Concepts

🧩 File Descriptions

🧪 Testing & Validation

📐 Diagrams & Models

🛠️ Best Practices

📎 Useful Resources

✨ Author

📚 Introduction

This project expands your understanding of Object-Oriented Programming (OOP) in Python by introducing more advanced concepts beyond the basics learned in Classes and Objects.
You will explore how Python handles object behavior, comparison, class-level attributes, static methods, and more.

The goal is to help you design clean, modular, and reusable classes while understanding how Python’s data model works under the hood.

🎯 Learning Objectives

By the end of this project, you should be able to:

Use special methods (__str__, __repr__, __del__, comparison operators…)

Differentiate instance attributes from class attributes

Implement class methods and static methods

Control attribute access using properties

Compare objects using custom logic

Understand how Python manages object lifecycle

Write classes that follow clean design principles and PEP 8

📁 Project Structure

Code
.
├── 0-rectangle.py
├── 1-rectangle.py
├── 2-rectangle.py
├── 3-rectangle.py
├── 4-rectangle.py
├── 5-rectangle.py
├── 6-rectangle.py
├── 7-rectangle.py
├── 8-rectangle.py
├── 9-rectangle.py
├── tests/
│   ├── test_0.txt
│   ├── test_1.txt
│   └── ...
└── README.md

🧠 Key Concepts

🔹 Special Methods (Magic Methods)
Python allows you to customize object behavior:

__str__ → user-friendly string representation

__repr__ → official representation (used for debugging)

__del__ → called when an object is deleted

__eq__, __lt__, __le__ → comparison operators

🔹 Class Attributes
Shared across all instances:

python
number_of_instances = 0
print_symbol = "#"
🔹 Class Methods
Operate on the class itself:

python
@classmethod
def my_method(cls):
    ...
🔹 Static Methods
Utility functions inside a class:

python
@staticmethod
def helper():
    ...
🔹 Encapsulation & Properties
Control access to private attributes:

python
@property
def width(self):
    return self.__width

🧩 File Descriptions
File	Description
0-rectangle.py	Empty Rectangle class
1-rectangle.py	Private attributes + initialization
2-rectangle.py	Getters, setters, validation
3-rectangle.py	area() and perimeter()
4-rectangle.py	Custom __str__
5-rectangle.py	Custom __repr__
6-rectangle.py	Custom __del__
7-rectangle.py	Class attribute number_of_instances
8-rectangle.py	Class attribute print_symbol
9-rectangle.py	Static method bigger_or_equal()

🧪 Testing & Validation
✔️ Run doctests
Code
python3 -m doctest -v <file>
✔️ Check PEP 8 compliance
Code
pycodestyle .
✔️ Make scripts executable
Each file must start with:

Code
#!/usr/bin/python3

📐 Diagrams & Models
🔸 Rectangle Class Model
Code
        ┌──────────────────────────┐
        │        Rectangle         │
        ├──────────────────────────┤
        │ - __width                │
        │ - __height               │
        │ - number_of_instances    │
        │ - print_symbol           │
        ├──────────────────────────┤
        │ + area()                 │
        │ + perimeter()            │
        │ + __str__()              │
        │ + __repr__()             │
        │ + __del__()              │
        │ + bigger_or_equal()      │
        └──────────────────────────┘

🔸 Object Lifecycle

Code
Definition → Instantiation → Usage → Deletion
🛠️ Best Practices
Validate all inputs in setters or __init__

Use __repr__ to make objects reconstructible

Keep classes focused (Single Responsibility Principle)

Prefer properties over direct attribute access

Use class attributes for shared state

Avoid side effects in static methods

📎 Useful Resources
Python Classes Tutorial: https://docs.python.org/3/tutorial/classes.html (docs.python.org in Bing)

Python Data Model (special methods): https://docs.python.org/3/reference/datamodel.html (docs.python.org in Bing)

PEP 8 Style Guide: https://peps.python.org/pep-0008/

✨ Author
Project completed as part of the Holberton School curriculum.
Documentation written by Sara Rebati.
