## SQL – More Queries
Holberton School – Higher Level Programming


📘 Overview
This project builds upon the foundations of SQL learned in the previous module and introduces more advanced database concepts.
You will work with MySQL 8.0 to create users, manage privileges, use constraints, perform joins, write subqueries, and manipulate data across multiple tables.

A manual QA review is required once the project is completed.

🎯 Learning Objectives
By the end of this project, you should be able to explain, without using Google:

General Concepts
How to create a new MySQL user

How to manage user privileges on databases and tables

What a PRIMARY KEY is

What a FOREIGN KEY is

How to use NOT NULL and UNIQUE constraints

How to retrieve data from multiple tables in a single query

What subqueries are

What JOIN and UNION operations do

These objectives are directly listed in the project instructions .

📚 Resources
Recommended reading:

How to Create a New User and Grant Permissions in MySQL

MySQL GRANT Statement

MySQL Constraints

Basic Query Operations: JOIN

SQL Techniques: Multiple Joins, DISTINCT

SQL Techniques: Join Types

SQL Techniques: Subqueries

SQL Techniques: UNION and MINUS

MySQL Cheat Sheet

The Seven Types of SQL Joins

SQL Style Guide

MySQL 8.0 SQL Statement Syntax

Database Design, Normalization, ER Modeling

🛠️ Requirements
General
Allowed editors: vi, vim, emacs

All files executed on Ubuntu 20.04 LTS using MySQL 8.0.25

Each file must end with a new line

Each SQL query must include a comment above it

Each file must start with a comment describing the task

SQL keywords must be UPPERCASE

A README.md is mandatory

File length will be tested using wc

These requirements are explicitly stated in the project page .

📝 SQL Comment Example
sql
-- 3 first students in Batch ID = 3
-- because Batch 3 is the best!
SELECT id, name
FROM students
WHERE batch_id = 3
ORDER BY created_at DESC
LIMIT 3;
🧪 Running MySQL
Using Ubuntu 20.04 Sandbox
Credentials: root/root

Start MySQL:

bash
service mysql start
Run a script:

bash
cat 0-list_databases.sql | mysql -uroot -p
Installing MySQL 8.0 on Ubuntu 20.04
(Only if not using the sandbox)

bash
sudo apt update
sudo apt install mysql-server
mysql --version
sudo mysql
Installation and connection steps are detailed in the project page .

🗄️ Importing a SQL Dump
Example from the project:

bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
This allows you to load predefined datasets for multi‑table queries.

📂 Project Structure
Your repository should follow this structure:

Code
holbertonschool-higher_level_programming/
└── SQL_more_queries/
    ├── 0-privileges.sql
    ├── 1-create_user.sql
    ├── 2-create_read_user.sql
    ├── ...
    ├── 13-count_shows_by_genre.sql
    ├── 14-my_genres.sql
    ├── 15-comedy_only.sql
    └── 16-shows_by_genre.sql
✔️ Example Badge Set for GitHub
md
![SQL](https://img.shields.io/badge/SQL-Advanced-blue)
![MySQL](https://img.shields.io/badge/MySQL-8.0-success)
![Joins](https://img.shields.io/badge/Joins-INNER%20%7C%20LEFT%20%7C%20RIGHT-yellow)
![Subqueries](https://img.shields.io/badge/Subqueries-Yes-important)
🎉 Conclusion
This project deepens your understanding of relational databases and SQL by introducing user management, constraints, joins, unions, and multi‑table queries.
Mastering these concepts is essential for backend development, data engineering, and designing scalable database systems.
