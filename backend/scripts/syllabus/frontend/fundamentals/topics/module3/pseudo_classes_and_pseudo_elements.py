"""
Pseudo-classes and Pseudo-elements - Detailed Content

This file contains comprehensive content for the "Pseudo-classes and Pseudo-elements" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Pseudo-classes and Pseudo-elements",
    "duration": "75-90 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Pseudo-classes and pseudo-elements extend CSS selectors with powerful capabilities
    to target elements based on state, position, or to create virtual elements. This topic
    covers the most common and useful pseudo-classes and pseudo-elements.
    """,
    
    "detailed_content": {
        "introduction": """
Pseudo-classes and pseudo-elements are like special keywords in CSS that let you target elements in specific states or positions, or create elements that don't actually exist in the HTML.

The distinction between them is important:
- **Pseudo-classes** (starting with `:`) target elements based on their state or position
- **Pseudo-elements** (starting with `::`) create virtual elements or style parts of elements

Modern CSS prefers `::` for pseudo-elements to distinguish them from pseudo-classes, though `:` still works for backward compatibility. Understanding both opens up powerful styling possibilities without adding extra HTML.
        """,
        
        "key_concepts": {
            "pseudo_classes": """
**What Are Pseudo-Classes?**

Pseudo-classes are keywords preceded by a single colon that define a special state or position of an element:

```css
a:hover { color: red; }
input:focus { border: 2px solid blue; }
li:nth-child(2) { font-weight: bold; }
```

The most common pseudo-classes:

**User Interaction States**
```css
/* When user hovers over an element */
a:hover { text-decoration: underline; }
button:hover { background-color: darker; }

/* When element has keyboard focus */
input:focus { outline: 2px solid blue; }
button:focus { box-shadow: 0 0 0 3px rgba(0, 0, 255, 0.3); }

/* When element is being clicked */
button:active { transform: scale(0.98); }

/* When a link has been visited */
a:visited { color: purple; }
```

**Structural Pseudo-Classes**
```css
/* First child of parent */
li:first-child { border-top: none; }

/* Last child of parent */
li:last-child { border-bottom: none; }

/* Nth child (counting from 1) */
li:nth-child(2) { background-color: lightyellow; }

/* Every other child (odd/even) */
li:nth-child(odd) { background-color: #f5f5f5; }
li:nth-child(even) { background-color: white; }
li:nth-child(2n+1) { /* Same as odd */ }

/* Only child of parent */
p:only-child { font-weight: bold; }

/* First of type among siblings */
h2:first-of-type { margin-top: 0; }

/* Last of type among siblings */
h2:last-of-type { margin-bottom: 0; }
```

**Form-Related Pseudo-Classes**
```css
/* Checked checkbox or radio */
input:checked { border-color: green; }

/* Disabled form element */
input:disabled { opacity: 0.5; cursor: not-allowed; }

/* Enabled form element */
input:enabled { cursor: text; }

/* Input with valid value */
input:valid { border-color: green; }

/* Input with invalid value */
input:invalid { border-color: red; }

/* Input with placeholder showing */
input:placeholder-shown { color: gray; }

/* Input with focus and valid value */
input:valid:focus { box-shadow: 0 0 5px green; }
```

**Content-Based Pseudo-Classes**
```css
/* Elements with no children */
div:empty { display: none; }

/* Matches an element that is a target of a URL fragment */
section:target { background-color: lightyellow; }

/* Link that hasn't been visited */
a:link { color: blue; }

/* Negation - matches elements that don't match the selector */
button:not(:disabled) { cursor: pointer; }
li:not(.active) { opacity: 0.6; }

/* Matches if any descendant matches the selector */
div:has(> img) { border: 2px solid gray; }
```

**Practical Examples**

Interactive link states:
```css
a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

a:active {
    color: #004499;
}

a:visited {
    color: #663366;
}
```

Styled list:
```css
li {
    padding: 0.5em;
}

li:nth-child(odd) {
    background-color: #f9f9f9;
}

li:first-child {
    font-weight: bold;
    border-top: 2px solid #0066cc;
}

li:last-child {
    border-bottom: 2px solid #0066cc;
}
```
            """,
            
            "pseudo_elements": """
**What Are Pseudo-Elements?**

Pseudo-elements are keywords preceded by `::` that create virtual elements within or around elements:

```css
p::before { content: "→ "; }
p::after { content: " ←"; }
p::first-line { font-weight: bold; }
```

**The `::before` and `::after` Pseudo-Elements**

These are the most powerful and commonly used pseudo-elements. They create virtual elements that you can style:

```css
/* Add content before an element */
.note::before {
    content: "📝 ";
}

/* Add content after an element */
.important::after {
    content: " ⭐";
}

/* Clear floats using ::after */
.container::after {
    content: "";
    display: table;
    clear: both;
}
```

With `::before` and `::after`, you can:
- Add decorative content
- Create geometric shapes
- Build UI elements without adding HTML
- Clear floats (old-school method)

Important constraints:
- They only work with elements that can have content
- The `content` property is required (even if empty: `content: ""`)
- They inherit from their parent element
- They can't contain actual HTML (only text or generated content)

**Practical Examples with `::before` and `::after`**

Blockquote styling:
```css
blockquote::before {
    content: '"';
    font-size: 3em;
    color: #ccc;
    position: relative;
    top: 0.2em;
    margin-right: 0.1em;
}

blockquote::after {
    content: '"';
    font-size: 3em;
    color: #ccc;
}
```

Required field indicator:
```css
label.required::after {
    content: " *";
    color: red;
    font-weight: bold;
}
```

Decorative lines:
```css
h2::before {
    content: "";
    display: inline-block;
    width: 20px;
    height: 3px;
    background-color: #0066cc;
    margin-right: 0.5em;
    vertical-align: middle;
}
```

**Other Pseudo-Elements**

```css
/* First line of a block element */
p::first-line {
    font-weight: bold;
    text-transform: uppercase;
}

/* First letter of a block element */
p::first-letter {
    font-size: 2em;
    font-weight: bold;
    margin-right: 0.1em;
}

/* Selected text */
p::selection {
    background-color: yellow;
    color: black;
}

/* Styling placeholder text */
input::placeholder {
    color: #999;
    font-style: italic;
}

/* Styling scrollbar (WebKit browsers) */
::-webkit-scrollbar {
    width: 10px;
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}

::-webkit-scrollbar-thumb {
    background: #888;
}

::-webkit-scrollbar-thumb:hover {
    background: #555;
}
```

**Real-World Example: Styled List**

```css
ul {
    list-style: none;
    padding: 0;
}

li {
    padding: 0.5em 0 0.5em 2em;
    position: relative;
}

/* Create a custom bullet using ::before */
li::before {
    content: "▸";
    position: absolute;
    left: 0;
    color: #0066cc;
    font-weight: bold;
}

/* Highlight first item */
li:first-child::before {
    content: "★";
    color: orange;
}
```
            """,
            
            "advanced_techniques": """
**Combining Pseudo-Classes and Pseudo-Elements**

You can combine them for powerful effects:

```css
/* First paragraph's first line */
p:first-of-type::first-line {
    font-weight: bold;
}

/* Hovered list item's after element */
li:hover::after {
    content: " →";
    color: #0066cc;
}

/* Focused input's before element */
input:focus::before {
    content: "✓";
    color: green;
}
```

**Creating Shapes with Pseudo-Elements**

```css
.triangle {
    width: 0;
    height: 0;
    border-left: 50px solid transparent;
    border-right: 50px solid transparent;
    border-bottom: 100px solid blue;
}

/* Using pseudo-elements for more complex shapes */
.speech-bubble::after {
    content: "";
    position: absolute;
    bottom: -10px;
    right: 20px;
    width: 0;
    height: 0;
    border: 10px solid transparent;
    border-top-color: white;
}
```

**State Indicators**

```css
/* Form field with success state */
input:valid {
    border-color: green;
}

input:valid::after {
    content: "✓";
    color: green;
}

/* Form field with error state */
input:invalid {
    border-color: red;
}

input:invalid::after {
    content: "✗";
    color: red;
}
```

**Performance Consideration**

Pseudo-elements like `::before` and `::after` don't exist in the DOM, so they:
- Don't affect DOM size or performance
- Can't be selected by JavaScript (except through parent)
- Don't affect accessibility (don't add to screen reader)
- Must use `content` property (otherwise they're invisible)

This makes them perfect for purely decorative elements.
            """,
        },
        
        "key_takeaways": [
            "Pseudo-classes (`:`) target elements based on state or position",
            "Pseudo-elements (`::`) create virtual elements within or around elements",
            "Common pseudo-classes: `:hover`, `:focus`, `:nth-child()`, `:first-child`, `:last-child`",
            "Form pseudo-classes: `:checked`, `:disabled`, `:enabled`, `:valid`, `:invalid`",
            "`::before` and `::after` are the most powerful and commonly used pseudo-elements",
            "The `content` property is required for pseudo-elements (even if empty)",
            "Pseudo-elements can be used for decorative content, shapes, and indicators",
            "You can combine pseudo-classes and pseudo-elements for powerful effects",
            "Pseudo-elements don't affect accessibility or DOM performance",
            "Use `:not()` for negation selectors to exclude elements from styling"
        ]
    }
}
