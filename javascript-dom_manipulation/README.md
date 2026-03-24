---
JavaScript - DOM Manipulation 🌐

Background Context
JavaScript is used to make web pages dynamic and interactive. In this project, we use JavaScript to manipulate the DOM (Document Object Model) — the in-memory representation of an HTML page — to update content, styles, and structure without reloading the page.
We also learn how to communicate with external APIs using XmlHTTPRequest and the modern Fetch API.

Resources
Read or watch:

What is JavaScript?
Introduction to the DOM
Document Interface
Element Class
Locating DOM elements using selectors
CSS Selectors
CSS Diner — Play with Selectors
DOM Scripting
Network Requests
What went wrong? Troubleshooting JavaScript


Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

How to select HTML elements in JavaScript
The differences between ID, class, and tag name selectors
How to modify an HTML element style
How to get and update an HTML element content
How to modify the DOM
How to make a request with XmlHTTPRequest
How to make a request with Fetch API
How to listen/bind to DOM events
How to listen/bind to user events


Requirements

Allowed editors: All of them
All files will be interpreted on Chrome browser (version 57.0 or later)
All files should end with a new line
A mandatory README.md file at the root of the project folder
Code must be semistandard compliant
You are not allowed to use var
HTML should not reload for each action: DOM manipulation, update values, fetch data…


Installation
Install semistandard
bashsudo npm install semistandard --global
Verify installation
bashsemistandard --version
Check your files
bashsemistandard <filename>.js
Auto-fix errors
bashsemistandard --fix <filename>.js

How to test
Each task comes with an HTML file. Open it in Chrome using Live Server (VS Code extension) to test fetch requests properly:
1. Install Live Server extension in VS Code
2. Right-click on the .html file → Open with Live Server
3. Chrome opens at http://127.0.0.1:5500/

⚠️ Do NOT open HTML files directly with file:// — Fetch API requests will be blocked by the browser's security policy.


Tasks
FileDescription0-script.jsUpdates the <header> text color to red using document.querySelector1-script.jsTurns the <header> red when user clicks on #red_header2-script.jsAdds the CSS class red to <header> when user clicks on #red_header3-script.jsToggles <header> class between red and green on click of #toggle_header4-script.jsAdds a <li>Item</li> to .my_list when user clicks on #add_item5-script.jsUpdates <header> text to New Header!!! when user clicks on #update_header6-script.jsFetches a Star Wars character name from the SWAPI and displays it in #character7-script.jsFetches all Star Wars movie titles from the SWAPI and lists them in #list_movies8-script.jsFetches the French translation of "hello" and displays it in #hello (script in <head>)100-script.js(Advanced) Adds, removes, and clears <li> elements from a list on button click101-script.js(Advanced) Fetches the translation of "hello" based on the language selected in a combo box

Key Concepts
Selecting HTML elements
javascript// By tag name
document.querySelector('header');

// By ID
document.querySelector('#myId');

// By class
document.querySelector('.myClass');

// All matching elements
document.querySelectorAll('.myClass');
Selectors — ID vs Class vs Tag
SelectorSyntaxUnique?ExampleTag'header'❌ NoAll <header> elementsID'#myId'✅ YesElement with id="myId"Class'.myClass'❌ NoAll elements with class="myClass"
Modifying style
javascript// Direct style (inline)
element.style.color = '#FF0000';
element.style.backgroundColor = 'blue';

// Via CSS class (recommended)
element.classList.add('red');
element.classList.remove('red');
element.classList.toggle('red');
element.classList.contains('red'); // → true/false
Getting and updating content
javascriptelement.textContent = 'New text';   // safe (no HTML interpretation)
element.innerHTML = '<b>Bold</b>';  // interprets HTML (⚠️ XSS risk)
input.value;                        // read input field value
Modifying the DOM
javascriptconst li = document.createElement('li'); // create
li.textContent = 'Item';                 // fill
parent.appendChild(li);                 // insert at end
parent.removeChild(li);                 // remove child
li.remove();                            // remove self
parent.innerHTML = '';                  // clear all
parent.lastElementChild;               // get last child
Listening to events
javascriptelement.addEventListener('click', function () {
  // code to run on click
});
Script in <head> — DOMContentLoaded
javascript// Required when script is loaded in <head>
document.addEventListener('DOMContentLoaded', function () {
  // DOM is fully loaded here
  const el = document.querySelector('#myElement');
});
Fetch API
javascriptfetch('https://api.example.com/data')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#result').textContent = data.name;
  })
  .catch(function (error) {
    console.log('Error:', error);
  });

Common Mistakes to Avoid
❌ Wrong✅ CorrectWhy'Click''click'Events are always lowercase'DOMContenLoaded''DOMContentLoaded'Typo — missing tResponse.json()response.json()Must match the parameter nameapprendChild()appendChild()TypofuctionfunctionTypoconsole.Log()console.log()Lowercase onlyvarconst / letvar is forbidden4-space indent2-space indentsemistandard rule

Author

Project by: REBATI SARA
School: Holberton School
Repository: holbertonschool-higher_level_programming
Directory: javascript-dom_manipulation