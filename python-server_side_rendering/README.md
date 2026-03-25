# JavaScript - DOM Manipulation 🌐

## Background Context

JavaScript is used to make web pages **dynamic and interactive**. In this project, we use JavaScript to manipulate the **DOM (Document Object Model)** — the in-memory representation of an HTML page — to update content, styles, and structure **without reloading the page**.

We also learn how to communicate with external APIs using **XmlHTTPRequest** and the modern **Fetch API**.

---

## Resources

Read or watch:

- [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
- [Introduction to the DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)
- [Document Interface](https://developer.mozilla.org/en-US/docs/Web/API/Document)
- [Element Class](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [Locating DOM elements using selectors](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors)
- [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors)
- [CSS Diner — Play with Selectors](https://flukeout.github.io/)
- [DOM Scripting](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents)
- [Network Requests](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Fetching_data)
- [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)

---

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

- How to select HTML elements in JavaScript
- The differences between ID, class, and tag name selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a request with XmlHTTPRequest
- How to make a request with Fetch API
- How to listen/bind to DOM events
- How to listen/bind to user events

---

## Requirements

- **Allowed editors:** All of them
- All files will be interpreted on **Chrome browser** (version 57.0 or later)
- All files should end with a new line
- A mandatory `README.md` file at the root of the project folder
- Code must be `semistandard` compliant
- You are **not allowed to use `var`**
- HTML should **not reload** for each action: DOM manipulation, update values, fetch data…

---

## Installation

### Install semistandard

```bash
sudo npm install semistandard --global
```

### Verify installation

```bash
semistandard --version
```

### Check your files

```bash
semistandard <filename>.js
```

### Auto-fix errors

```bash
semistandard --fix <filename>.js
```

---

## How to test

Each task comes with an HTML file. Open it in Chrome using **Live Server** (VS Code extension) to test fetch requests properly:

```
1. Install Live Server extension in VS Code
2. Right-click on the .html file → Open with Live Server
3. Chrome opens at http://127.0.0.1:5500/
```

> ⚠️ Do NOT open HTML files directly with `file://` — Fetch API requests will be blocked by the browser's security policy.

---

## Tasks

| File | Description |
|------|-------------|
| `0-script.js` | Updates the `<header>` text color to red using `document.querySelector` |
| `1-script.js` | Turns the `<header>` red when user clicks on `#red_header` |
| `2-script.js` | Adds the CSS class `red` to `<header>` when user clicks on `#red_header` |
| `3-script.js` | Toggles `<header>` class between `red` and `green` on click of `#toggle_header` |
| `4-script.js` | Adds a `<li>Item</li>` to `.my_list` when user clicks on `#add_item` |
| `5-script.js` | Updates `<header>` text to `New Header!!!` when user clicks on `#update_header` |
| `6-script.js` | Fetches a Star Wars character name from the SWAPI and displays it in `#character` |
| `7-script.js` | Fetches all Star Wars movie titles from the SWAPI and lists them in `#list_movies` |
| `8-script.js` | Fetches the French translation of "hello" and displays it in `#hello` (script in `<head>`) |
| `100-script.js` | *(Advanced)* Adds, removes, and clears `<li>` elements from a list on button click |
| `101-script.js` | *(Advanced)* Fetches the translation of "hello" based on the language selected in a combo box |

---

## Key Concepts

### Selecting HTML elements

```javascript
// By tag name
document.querySelector('header');

// By ID
document.querySelector('#myId');

// By class
document.querySelector('.myClass');

// All matching elements
document.querySelectorAll('.myClass');
```

### Selectors — ID vs Class vs Tag

| Selector | Syntax | Unique? | Example |
|----------|--------|---------|---------|
| Tag | `'header'` | ❌ No | All `<header>` elements |
| ID | `'#myId'` | ✅ Yes | Element with `id="myId"` |
| Class | `'.myClass'` | ❌ No | All elements with `class="myClass"` |

### Modifying style

```javascript
// Direct style (inline)
element.style.color = '#FF0000';
element.style.backgroundColor = 'blue';

// Via CSS class (recommended)
element.classList.add('red');
element.classList.remove('red');
element.classList.toggle('red');
element.classList.contains('red'); // → true/false
```

### Getting and updating content

```javascript
element.textContent = 'New text';   // safe (no HTML interpretation)
element.innerHTML = '<b>Bold</b>';  // interprets HTML (⚠️ XSS risk)
input.value;                        // read input field value
```

### Modifying the DOM

```javascript
const li = document.createElement('li'); // create
li.textContent = 'Item';                 // fill
parent.appendChild(li);                 // insert at end
parent.removeChild(li);                 // remove child
li.remove();                            // remove self
parent.innerHTML = '';                  // clear all
parent.lastElementChild;               // get last child
```

### Listening to events

```javascript
element.addEventListener('click', function () {
  // code to run on click
});
```

### Script in `<head>` — DOMContentLoaded

```javascript
// Required when script is loaded in <head>
document.addEventListener('DOMContentLoaded', function () {
  // DOM is fully loaded here
  const el = document.querySelector('#myElement');
});
```

### Fetch API

```javascript
fetch('https://api.example.com/data')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#result').textContent = data.name;
  })
  .catch(function (error) {
    console.log('Error:', error);
  });
```

---

## Common Mistakes to Avoid

| ❌ Wrong | ✅ Correct | Why |
|---------|----------|-----|
| `'Click'` | `'click'` | Events are always lowercase |
| `'DOMContenLoaded'` | `'DOMContentLoaded'` | Typo — missing `t` |
| `Response.json()` | `response.json()` | Must match the parameter name |
| `apprendChild()` | `appendChild()` | Typo |
| `fuction` | `function` | Typo |
| `console.Log()` | `console.log()` | Lowercase only |
| `var` | `const` / `let` | `var` is forbidden |
| 4-space indent | 2-space indent | semistandard rule |

---

## Author

- **Project by:** REBATI SARA
- **School:** Holberton School
- **Repository:** `holbertonschool-higher_level_programming`
- **Directory:** `javascript-dom_manipulation`