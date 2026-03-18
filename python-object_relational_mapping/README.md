## Python – Object‑Relational Mapping
Holberton School – Higher Level Programming

📘 Overview
This project connects two essential worlds: Python and Databases.
You will learn how to interact with MySQL using:

MySQLdb — executing raw SQL queries directly from Python

SQLAlchemy — an Object‑Relational Mapper (ORM) that lets you manipulate database rows as Python objects

The goal is to understand both approaches and appreciate how ORMs abstract away SQL while keeping your code flexible and storage‑agnostic.

All project details come from the official Holberton page .

🎯 Learning Objectives
By the end of this project, you should be able to explain, without using Google:

General Concepts
How to connect to a MySQL database from a Python script

How to SELECT rows from a MySQL table using Python

How to INSERT rows into a MySQL table using Python

What an ORM is and why it is useful

How to map a Python class to a MySQL table using SQLAlchemy

📚 Resources
Recommended reading and tutorials:

Object‑relational mappers

MySQLdb documentation

MySQLdb tutorial

SQLAlchemy tutorial

SQLAlchemy ORM documentation

Flask SQLAlchemy

SQLAlchemy cheatsheets

Common pitfalls for SQLAlchemy beginners

🛠️ Requirements
General
Allowed editors: vi, vim, emacs

All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5

MySQLdb version: 2.0.x

SQLAlchemy version: 1.4.x

All files must end with a new line

First line of every file must be:

bash
#!/usr/bin/python3
Code must follow pycodestyle 2.7.\*

All files must be executable

A README.md is mandatory

All modules, classes, and functions must include proper documentation

Documentation must be a full sentence, not a single word

You are not allowed to use execute() with SQLAlchemy

These requirements are listed on the project page .

🧩 Project Structure
This project includes 15 tasks, covering:

Part 1 — MySQLdb (Raw SQL)
Listing states

Filtering states

Preventing SQL injection

Listing cities

Joining tables

Part 2 — SQLAlchemy (ORM)
Creating models

Querying objects

Filtering with ORM syntax

Adding, updating, and deleting objects

Listing cities by state

🧪 Environment Setup
Install MySQL 8.0
Instructions provided on the project page .

Install MySQLdb 2.0.x
bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient==2.0.3
Install SQLAlchemy 1.4.x
bash
sudo pip3 install SQLAlchemy==1.4.22
📂 Repository Structure
Code
holbertonschool-higher_level_programming/
└── python-object_relational_mapping/
    ├── 0-select_states.py
    ├── 1-filter_states.py
    ├── 2-my_filter_states.py
    ├── 3-my_safe_filter_states.py
    ├── 4-cities_by_state.py
    ├── 5-filter_cities.py
    ├── model_state.py
    ├── 7-model_state_fetch_all.py
    ├── 8-model_state_fetch_first.py
    ├── 9-model_state_filter_a.py
    ├── 10-model_state_my_get.py
    ├── 11-model_state_insert.py
    ├── 12-model_state_update_id_2.py
    ├── 13-model_state_delete_a.py
    └── 14-model_city_fetch_by_state.py
✔️ Example Badge Set for GitHub
md
![MySQLdb](https://img.shields.io/badge/Library-MySQLdb%202.0.x-blue)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy%201.4.x-orange)
![Database](https://img.shields.io/badge/Database-MySQL%208.0-success)
🎉 Conclusion
This project gives you hands‑on experience with both raw SQL and ORM‑based database manipulation.
Mastering these tools is essential for backend development, API design, and scalable application architecture.
