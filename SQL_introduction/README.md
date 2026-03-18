SQL – Introduction
Holberton School – Higher Level Programming

📘 Overview
This project introduces the fundamentals of SQL and relational databases.
You will learn how to interact with MySQL 8.0, create and manipulate databases, and write SQL queries using proper syntax and conventions.

The project consists of multiple tasks designed to build a strong foundation in database management and querying.

🎯 Learning Objectives
By the end of this project, you should be able to explain, without using Google:

General Concepts
What a database is

What a relational database is

What SQL stands for

What MySQL is

How to create a database in MySQL

The meaning of DDL and DML

How to CREATE or ALTER a table

How to SELECT data from a table

How to INSERT, UPDATE, or DELETE data

What subqueries are

How to use MySQL functions

These objectives come directly from the project page .

📚 Resources
Recommended reading and tutorials:

What is Database & SQL?

Install MySQL (MySQL Server)

A Basic MySQL Tutorial

Basic SQL statements: DDL and DML

Basic queries: SQL and RA

SQL technique: functions

SQL technique: subqueries

What makes the big difference between a backtick and an apostrophe?

MySQL Cheat Sheet

MySQL 8.0 SQL Statement Syntax

Additional consolidated resource (due to temporary link issues)

🛠️ Requirements
General
Allowed editors: vi, vim, emacs

All files executed on Ubuntu 22.04 LTS with MySQL 8.0

Each file must end with a new line

Each SQL query must include a comment above it

Each file must start with a comment describing the task

All SQL keywords must be UPPERCASE

A README.md at the root of the project is mandatory

File length will be tested using wc

These requirements are explicitly listed in the project instructions .

🧪 Running MySQL in the Sandbox
Ubuntu 22.04 (Current CoD Image)
Steps include:

Request an Ubuntu 22.04 container

Update packages

Install MySQL server

Start the MySQL service

Connect using:

bash
mysql -uroot
Ubuntu 20.04 (Old Image)
Credentials: root/root

Start MySQL manually:

bash
service mysql start
Full installation and connection instructions are provided in the project page .

📝 SQL File Comment Example
sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name
FROM students
WHERE batch_id = 3
ORDER BY created_at DESC
LIMIT 3;
📂 Project Structure
Your repository should follow this structure:

Code
holbertonschool-higher_level_programming/
└── SQL_introduction/
    ├── 0-list_databases.sql
    ├── 1-create_database.sql
    ├── 2-delete_database.sql
    ├── ...
    ├── 18-temperatures_0.sql
    ├── 19-temperatures_1.sql
    └── 20-temperatures_2.sql
🧩 Tasks Overview
The project includes 20 tasks, such as:

Listing databases

Creating and deleting databases

Listing tables

Creating tables

Inserting and updating records

Using aggregate functions

Writing subqueries

Handling UTF‑8

Temperature analysis queries

All tasks and examples are visible on the project page .

✔️ Example Badge Set for GitHub
md
![SQL](https://img.shields.io/badge/SQL-MySQL%208.0-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange)
![Status](https://img.shields.io/badge/Progress-100%25-brightgreen)
![Style](https://img.shields.io/badge/Keywords-UPPERCASE-important)
🎉 Conclusion
This project builds the essential foundation for working with relational databases and SQL.
Mastering these concepts is crucial for backend development, data engineering, and any system that relies on structured data.
