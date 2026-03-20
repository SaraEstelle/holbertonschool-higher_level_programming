# JavaScript - Warm up 🚀

## Background Context

JavaScript is used for many things. In this project, JavaScript is used for two main reasons:

- **Scripting** — similar to what we do with Python
- **Web front-end** — to make web pages dynamic

For now, we focus on learning the basic concepts of the language through scripting. Later, we will make our AirBnB project dynamic using JavaScript and jQuery.

---

## Resources

Read or watch:

- [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
- [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
- [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
- [Operators](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Math)
- [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
- [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
- [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
- [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
- [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects)
- [Module patterns](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [var, let and const](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
- [JavaScript Tutorial](https://javascript.info/)
- [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

---

## Learning Objectives

At the end of this project, you should be able to explain to anyone, **without the help of Google**:

- Why JavaScript programming is amazing
- How to run a JavaScript script
- How to create variables and constants
- The differences between `var`, `const` and `let`
- All the data types available in JavaScript
- How to use the `if` and `if...else` statements
- How to use comments
- How to assign values to variables
- How to use `while` and `for` loops
- How to use `break` and `continue` statements
- What a function is and how to use functions
- What a function that does not use a `return` statement returns
- The scope of variables
- What the arithmetic operators are and how to use them
- How to manipulate dictionaries (objects)
- How to import a file

---

## Requirements

- **Allowed editors:** `vi`, `vim`, `emacs`
- All files will be interpreted on **Ubuntu 20.04 LTS** using `node` (version 14.x)
- All files should end with a new line
- The first line of all files must be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code must be `semistandard` compliant (version 16.x.x) — Standard rules + semicolons, also following [AirBnB style](https://github.com/airbnb/javascript)
- All files must be executable
- File length will be tested using `wc`

---

## Installation

### Install Node 14

```bash
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semistandard

```bash
$ sudo npm install semistandard --global
```

---

## Tasks

| File | Description |
|------|-------------|
| `0-javascript_is_amazing.js` | Prints "JavaScript is amazing" using a constant and `console.log` |
| `1-multi_languages.js` | Prints 3 lines: "C is fun", "Python is cool", "JavaScript is amazing" |
| `2-arguments.js` | Prints a message depending on the number of arguments passed |
| `3-value_argument.js` | Prints the first argument passed to the script (no `length`) |
| `4-concat.js` | Prints two arguments in the format: "`arg1` is `arg2`" |
| `5-to_integer.js` | Converts and prints the first argument as an integer (no `try/catch`) |
| `6-multi_languages_loop.js` | Prints 3 lines using an array and a loop (one `console.log`) |
| `7-multi_c.js` | Prints "C is fun" x times, where x is the first argument |
| `8-square.js` | Prints a square of size x using the character `X` |
| `9-add.js` | Prints the addition of two integers using a function `add(a, b)` |
| `10-factorial.js` | Computes and prints a factorial recursively |
| `11-second_biggest.js` | Searches for the second biggest integer in a list of arguments |
| `12-object.js` | Updates a script to replace a value `12` with `89` in an object |
| `13-add.js` | Exports a function `add` visible from outside the file |
| `100-let_me_const.js` | *(Advanced)* Modifies the value of `myVar` to `333` |
| `101-call_me_moby.js` | *(Advanced)* Executes a function x times |
| `102-add_me_maybe.js` | *(Advanced)* Increments a number then calls a callback with the new value |
| `103-object_fct.js` | *(Advanced)* Adds a method `incr` to an object to increment its `value` |

---

## Key Concepts Covered

### `var` vs `let` vs `const`

| Keyword | Reassignable | Block-scoped | Use case |
|---------|-------------|--------------|----------|
| `var` | ✅ Yes | ❌ No (function-scoped) | ⚠️ Avoid — legacy |
| `let` | ✅ Yes | ✅ Yes | Variables that change (e.g., loop counters) |
| `const` | ❌ No | ✅ Yes | Variables that never change |

### `process.argv`

```
process.argv[0] → path to Node.js
process.argv[1] → path to the script
process.argv[2] → 1st user argument
process.argv[3] → 2nd user argument
...
```

### Modules (`require` / `exports`)

```javascript
// Export (in module file)
exports.myFunction = myFunction;

// Import (in main file)
const myFunction = require('./myModule').myFunction;
```

### Recursion

```javascript
function factorial(n) {
  if (n === 0 || n === 1) return 1;  // base case
  return n * factorial(n - 1);       // recursive case
}
```

---

## Author

- **Project by:** SARA REBATI
- **School:** Holberton School
- **Repository:** `holbertonschool-higher_level_programming`
- **Directory:** `javascript-warm_up`
