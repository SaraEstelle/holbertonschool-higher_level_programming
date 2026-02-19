🌑 RESTful API – From HTTP Fundamentals to Secure Authentication
<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=RESTful%20API%20Project&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=HTTP%20•%20Flask%20•%20JWT%20•%20Authentication%20•%20Backend%20Engineering&descAlignY=60&descSize=16" /> </p>

<p align="center">












</p>
📖 Introduction

Modern applications constantly communicate through APIs.
This project explores the complete lifecycle of RESTful API development, from understanding HTTP basics to implementing secure authentication systems.

## Through Tasks 0 → 5, this repository demonstrates:

HTTP/HTTPS fundamentals

API consumption with curl

API consumption with Python

Manual API development using http.server

REST API development using Flask

API Security using Basic Authentication

JWT-based authentication

Role-based access control

This project simulates real-world backend engineering practices.

---
---

## 🧱 Project Structure

restful-api/
│
├── task_00_http_basics.md
├── task_01_curl_commands.sh
├── task_02_requests.py
├── task_03_http_server.py
├── task_04_flask.py
├── task_05_basic_security.py
│
├── posts.csv
└── README.md


---

## 🎯 Learning Objectives

- Understand HTTP requests and responses
- Know the difference between HTTP and HTTPS
- Consume APIs using curl
- Process API responses in Python
- Create a basic HTTP server
- Build scalable APIs with Flask
- Implement authentication & authorization
- JWT authentication system
- Role-based access control

---

## 🔹 Task 0 – HTTP / HTTPS Basics

**HTTP Request Example:**

GET /index.html HTTP/1.1
Host: example.com


**HTTP Response Example:**

HTTP/1.1 200 OK
Content-Type: text/html


**HTTP vs HTTPS**

| HTTP  | HTTPS |
|-------|-------|
| Plain text | Encrypted (SSL/TLS) |
| Port 80 | Port 443 |
| Vulnerable | Secure |

**Common Methods**

| Method | Description |
|--------|------------|
| GET    | Retrieve data |
| POST   | Create data |
| PUT    | Update data |
| DELETE | Remove data |

---

## 🔹 Task 1 – API Consumption with curl

Fetch posts:

```bash
curl https://jsonplaceholder.typicode.com/posts
View headers only:

curl -I https://jsonplaceholder.typicode.com/posts
POST request:

curl -X POST -d "title=foo&body=bar&userId=1" \
https://jsonplaceholder.typicode.com/posts
```

----
🔹 Task 2 – API Consumption with Python
---
File: task_02_requests.py

Functions

- fetch_and_print_posts() – prints status code and post titles

- fetch_and_save_posts() – fetches posts and saves to posts.csv


----
🔹 Task 3 – API with http.server
---
Run server:
```bash
python3 task_03_http_server.py
```

Access via:
```arduino
http://localhost:8000

Endpoints:

Endpoint	Description
/	Welcome message
/data	JSON data
/status	OK
/info	API metadata
Other	404 Not Found
```
---
🔹 Task 4 – REST API with Flask
---

Run:
```bash
python3 task_04_flask.py
```
Runs at:
```cpp
http://127.0.0.1:5000
```

Endpoints:

Endpoint	Method
/	GET
/status	GET
/data	GET
/users/<username>	GET
/add_user	POST

---
🔹 Task 5 – API Security & Authentication
---
File: task_05_basic_security.py

Basic Authentication

Protected route:
```vbnet
GET /basic-protected
```

Returns:

- 401 if unauthorized

- 200 if credentials valid

JWT Authentication

Login route:
```bash
POST /login
````

Returns:

```json
{
  "access_token": "<JWT_TOKEN>"
}
```
Protected Route

```vbnet
GET /jwt-protected
```

Requires:
```makefile
Authorization: Bearer <TOKEN>
```
Admin-Only Route

```pgsql
GET /admin-only
```

Returns:

* 403 if not admin

* 200 if admin

Security Practices:

* Password hashing

* Stateless JWT authentication

* Custom JWT error handlers

* Role validation

* Proper 401 & 403 usage


---
📊 REST API Architecture
---
Client → Web Server → API Logic → Database
        ← Response  ← Processing ←

---
🚀 Installation
---

Install dependencies:

pip install Flask Flask-HTTPAuth Flask-JWT-Extended


Run secured API:

python3 task_05_basic_security.py

---
🧠 Skills Demonstrated
---

Backend development

REST architecture

HTTP protocol mastery

Secure authentication systems

Flask framework usage

API design best practices

---
👨‍💻 Author
---

SARA REBATI
Software Engineering Student – Holberton School

GitHub: https://github.com/SaraEstelle
