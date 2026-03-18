Python – Input/Output
Holberton School – Higher Level Programming

📘 Overview
This project introduces Python’s file handling, JSON serialization, and command‑line argument features.
You will learn how to read and write files safely, use the with statement, manipulate file cursors, and convert Python objects to and from JSON.

All requirements and tasks come directly from the official Holberton project page ().

🎯 Learning Objectives
By the end of this project, you should be able to explain, without using Google:

General Concepts
Why Python programming is awesome

How to open a file

How to write text to a file

How to read the full content of a file

How to read a file line by line

How to move the cursor in a file

How to ensure a file is properly closed

What the with statement is and how to use it

What JSON is

What serialization and deserialization are

How to convert a Python data structure to a JSON string

How to convert a JSON string to a Python data structure

How to access command‑line parameters in a Python script

📚 Resources
Recommended reading and videos:

7.2. Reading and Writing Files

8.7. Predefined Clean‑up Actions

Dive Into Python 3 – Chapter 11: Files (until 11.4 Binary Files)

JSON encoder and decoder

Learn to Program 8: Reading/Writing Files

Automate the Boring Stuff with Python (Ch. 8 & Ch. 14 excerpts)

sys package

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

A README.md at the root of the project is mandatory

File length will be tested using wc

Python Test Cases
Test files must be inside a tests/ folder

Test files must be .txt

Tests executed using:

bash
python3 -m doctest ./tests/*
All modules, classes, and functions must have proper documentation

Documentation must be a real sentence, not a single word

Collaboration on test cases is encouraged

All requirements are listed on the project page ().

🧩 Tasks Overview
The project includes 13 tasks, covering:

Reading files

Writing and appending text

JSON serialization/deserialization

Saving and loading objects

Working with command‑line arguments

Converting classes to JSON

Re‑creating objects from JSON

Pascal’s Triangle generation

Example: Task 0 – Read file
Write a function that reads a UTF‑8 text file and prints its content to stdout.

Must use with

No imports

No exception handling required

Example from the project page ():

Code
We offer a truly innovative approach to education:
focus on building reliable applications and scalable systems, take on real-world challenges, collaborate with your peers.

A school every software engineer would have dreamt of!
📂 Project Structure
Code
holbertonschool-higher_level_programming/
└── python-input_output/
    ├── 0-read_file.py
    ├── 1-write_file.py
    ├── 2-append_write.py
    ├── 3-to_json_string.py
    ├── 4-from_json_string.py
    ├── 5-save_to_json_file.py
    ├── 6-load_from_json_file.py
    ├── 7-add_item.py
    ├── 8-class_to_json.py
    ├── 9-student.py
    ├── 10-student.py
    ├── 11-student.py
    └── 12-pascal_triangle.py
✔️ Example Badge Set for GitHub
md
![Files](https://img.shields.io/badge/Python-File%20Handling-blue)
![JSON](https://img.shields.io/badge/JSON-Serialization-green)
![Doctest](https://img.shields.io/badge/Testing-Doctest-yellow)
🎉 Conclusion
This project strengthens your ability to work with files, JSON, and command‑line arguments — essential skills for real‑world Python development.
Mastering these concepts prepares you for more advanced topics such as serialization, persistence, and data processing.
