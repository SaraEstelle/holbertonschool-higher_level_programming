![Python - Inheritance Banner](assets/banner.png)

# Python - Inheritance

## Description
This project is all about understanding **inheritance in Python** — how classes can reuse, extend, and sometimes rebel against other classes.  
Through a progressive set of exercises, I explored how objects relate to each other, how behavior can be inherited or overridden, and why inheritance is one of the superpowers of object-oriented programming.  
From simple type checks to building geometric shapes, this project proves that good design saves time… and bad design comes back to haunt you.

---

## Learning Objectives
With this project, I learned what parent and child classes really are and why their relationship matters. 
I learned how to explore the attributes and methods of a class or instance and actually understand what I’m seeing. 
I discovered when Python allows instances to receive new attributes, and when it very clearly refuses. 
I practiced creating classes that inherit from others, including multiple inheritance, while keeping things readable. 
I identified the default base class behind every Python class and learned how to override inherited methods safely and intentionally. 
I now understand what inheritance is truly for, beyond just reducing code duplication, and I can use isinstance, issubclass, type, and super with confidence.

---

## Requirements
- OS: Ubuntu 20.04 LTS
- Python version: `python3` (3.8.5)
- All files must end with a new line
- The first line of all files must be exactly: `#!/usr/bin/python3`
- A README.md file at the root of the project is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- No module imports allowed unless explicitly stated

---

## Usage / Execution
All Python scripts can be executed in two ways:

### 1. Direct execution
Make the file executable and run it directly:
```bash
chmod +x filename.py
./filename.py
```

### 2. Using Python interpreter
Run the script with Python:
```bash
python3 filename.py
```

---

## Project Progress
<p align="center">
<img src="assets/progress_barre_100.gif" alt="Mandatory tasks progress" width="80%">
</p>

<p align="center">
<sub>Mandatory tasks completion: 100% ---  Advanced tasks completion: 100%</sub>
</p>

---

## Tasks

### 0 - Lookup
- **Task status:** Mandatory  
- **Task objectives:** Learn how to inspect an object and retrieve all its available attributes and methods.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** The function returns a list containing all attributes and methods of a given object.  

**Files**
- `0-lookup.py`

---

### 1 - My list
- **Task status:** Mandatory  
- **Task objectives:** Practice inheritance by creating a custom class that extends Python’s built-in `list`.  
- **Task constraint:** No module imports allowed, elements are always integers.  
- **Expected behavior:** The list can be printed normally and also printed in sorted order without modifying the original list.  

**Files**
- `1-my_list.py`
- `tests/1-my_list.txt`

---

### 2 - Exact same object
- **Task status:** Mandatory  
- **Task objectives:** Understand strict type comparison between an object and a class.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** The function returns `True` only if the object is exactly an instance of the specified class.  

**Files**
- `2-is_same_class.py`

---

### 3 - Same class or inherit from
- **Task status:** Mandatory  
- **Task objectives:** Learn how inheritance affects type checking.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** The function returns `True` if the object is an instance of the class or any of its subclasses.  

**Files**
- `3-is_kind_of_class.py`

---

### 4 - Only sub class of
- **Task status:** Mandatory  
- **Task objectives:** Differentiate between direct instances and inherited instances.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** The function returns `True` only if the object is an instance of a subclass of the given class.  

**Files**
- `4-inherits_from.py`

---

### 5 - Geometry module
- **Task status:** Mandatory  
- **Task objectives:** Create a base class to prepare for future inheritance.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** The class exists and can be instantiated, even if it is empty.  

**Files**
- `5-base_geometry.py`

---

### 6 - Improve Geometry
- **Task status:** Mandatory  
- **Task objectives:** Introduce abstract-like behavior in a base class.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** Calling `area()` raises an exception indicating it is not implemented.  

**Files**
- `6-base_geometry.py`

---

### 7 - Integer validator
- **Task status:** Mandatory  
- **Task objectives:** Add input validation logic to a base class.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** The method validates integers and raises appropriate errors when constraints are not respected.  

**Files**
- `7-base_geometry.py`
- `tests/7-base_geometry.txt`

---

### 8 - Rectangle
- **Task status:** Mandatory  
- **Task objectives:** Practice inheritance by creating a concrete class from a base class.  
- **Task constraint:** Attributes must be private and validated using inherited methods.  
- **Expected behavior:** A rectangle can be instantiated only with valid width and height values.  

**Files**
- `8-rectangle.py`

---

### 9 - Full rectangle
- **Task status:** Mandatory  
- **Task objectives:** Complete the rectangle class with behavior and representation.  
- **Task constraint:** No getters or setters, validation through inheritance only.  
- **Expected behavior:** The rectangle can compute its area and display a custom string representation.  

**Files**
- `9-rectangle.py`

---

### 10 - Square #1
- **Task status:** Mandatory  
- **Task objectives:** Create a square class by inheriting from the rectangle class.  
- **Task constraint:** Size must be validated and stored as a private attribute.  
- **Expected behavior:** The square correctly computes its area using inherited logic.  

**Files**
- `10-square.py`

---

### 11 - Square #2
- **Task status:** Mandatory  
- **Task objectives:** Override inherited behavior to customize class representation.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** Printing the square displays a specific square description format.  

**Files**
- `11-square.py`

---

### 12 - My integer
- **Task status:** Advanced  
- **Task objectives:** Explore method overriding on built-in types.  
- **Task constraint:** No module imports allowed.  
- **Expected behavior:** Equality and inequality operators behave in the opposite way of a standard integer.  

**Files**
- `100-my_int.py`

---

### 13 - Can I?
- **Task status:** Advanced  
- **Task objectives:** Understand object mutability and attribute assignment limits.  
- **Task constraint:** No try/except blocks and no module imports allowed.  
- **Expected behavior:** A new attribute is added only if the object supports it, otherwise an error is raised.  

**Files**
- `101-add_attribute.py`

---

## Authors
**SARA REBATI**
- Student at Holberton School
- Track: Higher Level Programming
- Project: Python - Inheritance
