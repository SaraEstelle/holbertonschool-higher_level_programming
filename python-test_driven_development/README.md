## Python – Test‑Driven Development
Holberton School – Higher Level Programming

📘 Overview
This project introduces Test‑Driven Development (TDD) in Python.
You will learn how to write documentation‑based tests using doctest, how to structure test files, and how to think about edge cases before writing any implementation.

The project emphasizes writing tests first, then writing the code that satisfies them — a core principle of TDD.

All project details come from the official Holberton page .

🎯 Learning Objectives
By the end of this project, you should be able to explain, without using Google:

General Concepts
Why Python programming is awesome

What an interactive test is

Why tests are important

How to write docstrings that generate tests

How to write documentation for modules and functions

What doctest option flags are

How to identify and test edge cases

📚 Resources
Recommended reading and tutorials:

doctest — Test interactive Python examples

doctest – Testing through documentation

Unit Tests in Python

🛠️ Requirements
Python Scripts
Allowed editors: vi, vim, emacs

All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5

All files must end with a new line

First line of every file must be:

bash
#!/usr/bin/python3
Code must follow pycodestyle 2.7.\*

All files must be executable

A README.md is mandatory

File length will be tested using wc

Python Test Cases
Test files must be inside a tests/ folder

Test files must be .txt

Tests executed using:

bash
python3 -m doctest ./tests/*
All modules and functions must have proper documentation

Documentation must be a full sentence, not a single word

Collaboration on test cases is encouraged

These requirements are listed on the project page .

🧩 Tasks Overview
This project includes 6 tasks, covering:

0. Integers addition
Write a function that adds two integers with strict type validation.

Accepts integers or floats

Floats are cast to integers

Raises TypeError with specific messages

No imports allowed

Example from the project page :

Code
3
98
100
98
b must be an integer
a must be an integer
Other tasks include:
Dividing matrices

Printing formatted names

Printing squares

Text indentation

Writing unittests for a max‑integer function

📂 Project Structure
Code
holbertonschool-higher_level_programming/
└── python-test_driven_development/
    ├── 0-add_integer.py
    ├── 2-matrix_divided.py
    ├── 3-say_my_name.py
    ├── 4-print_square.py
    ├── 5-text_indentation.py
    ├── tests/
    │   ├── 0-add_integer.txt
    │   ├── 2-matrix_divided.txt
    │   ├── 3-say_my_name.txt
    │   ├── 4-print_square.txt
    │   ├── 5-text_indentation.txt
    │   └── 6-max_integer_test.py
    └── 6-max_integer.py
✔️ Example Badge Set for GitHub
md
![TDD](https://img.shields.io/badge/Methodology-TDD-blueviolet)
![Doctest](https://img.shields.io/badge/Testing-Doctest-yellow)
![Unittest](https://img.shields.io/badge/Testing-Unittest-green)
🎉 Conclusion
This project strengthens your ability to write robust, well‑tested Python code.
By mastering TDD, doctest, and documentation‑driven development, you build habits that scale to large, professional software systems.
