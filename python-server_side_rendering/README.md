# Python - Server-Side Rendering

> **Holberton School** — Higher Level Programming
---

## 📋 Description

This project explores **Server-Side Rendering (SSR)** using Python and Flask.
Unlike client-side rendering where the browser builds the page with JavaScript, SSR generates fully formed HTML on the server before sending it to the client — making pages faster to display, easier to index by search engines, and simpler to maintain.

Through four progressive tasks, this project covers:
- Python string templating from scratch
- Building a Flask application with Jinja2 templates
- Dynamic content rendering with loops and conditions
- Reading data from JSON, CSV, and SQLite databases
- Handling query parameters and edge cases

---

## 🗂️ Project Structure

```
python-server_side_rendering/
├── task_00_intro.py          # String templating without frameworks
├── task_01_jinja.py          # Basic Flask app with Jinja2 templates
├── task_02_logic.py          # Loops and conditions in templates
├── task_03_files.py          # JSON and CSV data sources
├── task_04_db.py             # SQLite as data source
│
├── items.json                # Data for task 02
├── products.json             # Product data for tasks 03 & 04
├── products.csv              # Product data in CSV format
├── products.db               # SQLite database (generated)
├── create_db.py              # Script to initialize the database
├── template.txt              # Invitation template for task 00
│
└── templates/
    ├── index.html            # Home page
    ├── about.html            # About page
    ├── contact.html          # Contact page
    ├── header.html           # Reusable header component
    ├── footer.html           # Reusable footer component
    ├── items.html            # Dynamic items list (task 02)
    └── product_display.html  # Products table with error handling (tasks 03 & 04)
```

---

## ⚙️ Requirements

- Python 3.x
- Flask

```bash
pip install Flask
```

No other external dependencies — `json`, `csv`, and `sqlite3` are all part of Python's standard library.

---

## 🚀 Tasks

### Task 0 — Python String Templating
**File:** `task_00_intro.py`

Generates personalized invitation files from a template using Python's `.replace()` method.

**Key concepts:** `str.replace()`, `isinstance()`, `dict.get()`, file I/O, input validation

```bash
python3 -c "
from task_00_intro import generate_invitations
with open('template.txt', 'r') as f:
    template = f.read()
attendees = [
    {'name': 'Alice', 'event_title': 'Python Conference', 'event_date': '2023-07-15', 'event_location': 'New York'},
    {'name': 'Bob', 'event_title': 'Data Science Workshop', 'event_date': '2023-08-20', 'event_location': 'San Francisco'},
    {'name': 'Charlie', 'event_title': 'AI Summit', 'event_date': None, 'event_location': 'Boston'}
]
generate_invitations(template, attendees)
"
# Output: output_1.txt, output_2.txt, output_3.txt
```

Error handling:
- Empty template → logs message and stops
- Empty attendee list → logs message and stops
- Missing field in dict → replaced with `"N/A"`
- Wrong input types → logs error and stops

---

### Task 1 — Basic Flask + Jinja2 Templates
**File:** `task_01_jinja.py`

A Flask application serving three pages (Home, About, Contact) with a shared header and footer using Jinja's `{% include %}`.

**Key concepts:** Flask routes, `render_template()`, `{% include %}`, reusable components

```bash
python3 task_01_jinja.py
```

| Route | Page |
|---|---|
| `/` | Home |
| `/about` | About Us |
| `/contact` | Contact Us |

---

### Task 2 — Dynamic Templates with Loops and Conditions
**File:** `task_02_logic.py`

Reads a list of items from `items.json` and displays them dynamically. Handles the empty list case with a conditional message.

**Key concepts:** `json.load()`, Jinja `{% for %}`, Jinja `{% if %}`, passing data to templates

```bash
python3 task_02_logic.py
```

| Route | Description |
|---|---|
| `/items` | Displays item list or "No items found" if empty |

Test with empty list by editing `items.json`:
```json
{ "items": [] }
```

---

### Task 3 — JSON and CSV Data Sources
**File:** `task_03_files.py`

A `/products` route that reads from either `products.json` or `products.csv` based on a `source` query parameter. Supports optional filtering by `id`.

**Key concepts:** `csv.DictReader`, `request.args`, query parameters, error messages in templates

```bash
python3 task_03_files.py
```

| URL | Result |
|---|---|
| `/products?source=json` | All products from JSON |
| `/products?source=csv` | All products from CSV |
| `/products?source=json&id=1` | Single product filtered by id |
| `/products?source=json&id=99` | "Product not found" |
| `/products?source=xml` | "Wrong source" |

---

### Task 4 — SQLite Database Source
**File:** `task_04_db.py`

Extends Task 3 by adding `source=sql` which reads from a SQLite database. All three sources use the same template.

**Key concepts:** `sqlite3`, `row_factory`, `conn.commit()`, `CREATE TABLE IF NOT EXISTS`

```bash
# Step 1: Create the database (run once)
python3 create_db.py

# Step 2: Launch the app
python3 task_04_db.py
```

| URL | Result |
|---|---|
| `/products?source=sql` | All products from SQLite |
| `/products?source=sql&id=1` | Laptop only |
| `/products?source=sql&id=99` | "Product not found" |

---

## 📊 Data Files

### items.json
```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

### products.json
```json
[
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99},
    {"id": 3, "name": "Python Book", "category": "Education", "price": 39.99}
]
```

### products.csv
```
id,name,category,price
1,Laptop,Electronics,799.99
2,Coffee Mug,Home Goods,15.99
3,Python Book,Education,39.99
```

---

## 🔑 Key Concepts Summary

| Task | What you learn |
|---|---|
| Task 0 | Manual templating — understand what Jinja does under the hood |
| Task 1 | Flask routing + `{% include %}` for DRY templates |
| Task 2 | `{% for %}` + `{% if %}` — Jinja logic in templates |
| Task 3 | Multiple data sources, query params, error handling |
| Task 4 | SQLite integration — one template, three data sources |

### SSR vs Client-Side Rendering

| | SSR (this project) | CSR (React, Vue...) |
|---|---|---|
| HTML built by | Server (Python/Flask) | Browser (JavaScript) |
| First load speed | Fast — HTML ready to display | Slow — JS must run first |
| SEO | Excellent — crawlers see full HTML | Harder — crawlers may miss content |
| Complexity | Simpler for data-heavy pages | Better for highly interactive UIs |

---

## 📚 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja2 Documentation](https://jinja.palletsprojects.com/)
- [Python sqlite3 Module](https://docs.python.org/3/library/sqlite3.html)
- [Python csv Module](https://docs.python.org/3/library/csv.html)
- [Python json Module](https://docs.python.org/3/library/json.html)

---

## 👤 Author

**Sara Estelle**
Holberton School — Higher Level Programming