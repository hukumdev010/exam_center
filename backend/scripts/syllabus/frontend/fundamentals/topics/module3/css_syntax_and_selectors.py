"""
CSS Syntax and Selectors - Detailed Content

This file contains comprehensive content for the "CSS Syntax and Selectors" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "CSS Syntax and Selectors",
    "duration": "75-90 minutes",
    "difficulty": "Beginner",
    "overview": """
    CSS (Cascading Style Sheets) is the language of web design. This topic covers
    the fundamental syntax of CSS and the powerful selector system that targets
    HTML elements for styling.
    """,
    
    "detailed_content": {
        "introduction": """
CSS stands for Cascading Style Sheets, and it's the technology responsible for how websites look. While HTML provides structure and meaning to content, CSS controls the presentation—colors, layouts, fonts, spacing, animations, and more.

CSS is deceptively simple to start with but incredibly powerful when mastered. You can create simple, static stylesheets for basic websites, or you can harness CSS's advanced features to build complex, responsive, interactive designs. The "cascading" part of CSS is particularly important—it describes how styles are applied based on specificity and source order.

Understanding CSS selectors is fundamental to being an effective web developer. Selectors are how you target the HTML elements you want to style. With the right selectors, you can style specific elements, groups of elements, or even elements based on their state or position in the document. Master selectors, and you've taken a huge step toward CSS mastery.

CSS has evolved dramatically over the past decade. Modern CSS includes features like CSS variables, grid layout, flexbox, and feature queries that would have been unimaginable in the early days. This makes CSS a more capable language than ever, but also means there's a lot to learn.
        """,
        
        "key_concepts": {
            "css_fundamentals": """
**What is CSS?**

CSS is a separate language from HTML. While HTML says "this is a heading" (structure), CSS says "make all headings blue, 24 pixels tall, with sans-serif font" (presentation).

Separating content from presentation is a key principle of web development:
- **HTML**: The what (content and structure)
- **CSS**: The how (presentation and style)
- **JavaScript**: The behavior (interactivity)

This separation has many benefits:
- Multiple stylesheets can target the same HTML
- The same CSS can style different HTML structures
- You can change the entire design without touching HTML
- HTML remains accessible even without CSS
- Teams can have designers and developers work independently

**The CSS Syntax**

A CSS rule consists of two parts: a **selector** and a **declaration block**:

```css
selector {
    property: value;
    another-property: another-value;
}
```

For example:
```css
p {
    color: blue;
    font-size: 16px;
}
```

Breaking this down:
- `p`: The **selector** (targets paragraph elements)
- `color: blue;`: A **declaration** (property and value pair)
- `font-size: 16px;`: Another declaration
- The entire block `{ ... }` is the **declaration block**

**Properties and Values**

CSS properties describe what aspect of the element to style:
- `color`: Text color
- `background-color`: Background color
- `font-size`: Text size
- `margin`: Space outside an element
- `padding`: Space inside an element
- `width`: Element width
- `height`: Element height
- `display`: How to render the element

Values are the specific settings for those properties:
- `blue`, `#0000FF`, `rgb(0, 0, 255)`: Different ways to specify blue
- `16px`, `1em`, `1.5rem`: Different units for sizes
- `center`, `flex-start`, `baseline`: Different alignment values

**Whitespace and Formatting**

CSS is flexible about whitespace. These are all equivalent:

```css
/* Single line */
p { color: blue; font-size: 16px; }

/* Multiple lines (standard) */
p {
    color: blue;
    font-size: 16px;
}

/* With extra whitespace */
p
{
    color:  blue;
    font-size:  16px ;
}
```

The multi-line format is standard because it's more readable. But the browser doesn't care—it's all the same.

**Comments**

CSS comments are ignored by the browser:

```css
/* Single-line comment */

/*
    Multi-line comment
    useful for longer explanations
    or temporarily disabling code
*/

p { color: blue; /* Inline comment */ }
```

Comments are essential for:
- Explaining complex selectors or values
- Noting why a particular approach was chosen
- Disabling styles temporarily during development
- Helping other developers understand your choices
            """,
            
            "selector_types": """
**Introduction to Selectors**

A selector is a pattern that targets HTML elements for styling. CSS offers many different ways to select elements, from simple to sophisticated. Understanding selectors is crucial because:
- Without the right selector, you can't target the right elements
- Overly broad selectors might affect unintended elements
- Specific selectors help you avoid conflicts and override issues

Selectors can target:
- Specific element types (all `<p>` tags)
- Elements with specific classes or IDs
- Elements in specific states (hovered, focused, etc.)
- Elements based on their position in the document structure
- Elements based on their attributes

**Simple Selectors**

The simplest selectors target by element type, class, or ID:

```css
/* Element selector - targets all <p> elements */
p {
    color: black;
}

/* Class selector - targets all elements with class "highlight" */
.highlight {
    background-color: yellow;
}

/* ID selector - targets the element with id "header" */
#header {
    background-color: navy;
}

/* Universal selector - targets all elements */
* {
    margin: 0;
    padding: 0;
}

/* Attribute selector - targets elements with a specific attribute */
input[type="text"] {
    border: 1px solid gray;
}
```

**Combinators**

Combinators show relationships between selectors:

```css
/* Descendant combinator (space) - all <p> inside <div> */
div p {
    color: gray;
}

/* Child combinator (>) - only <p> that are direct children of <div> */
div > p {
    color: gray;
}

/* Adjacent sibling combinator (+) - <p> immediately after <h2> */
h2 + p {
    font-weight: bold;
}

/* General sibling combinator (~) - all <p> siblings after <h2> */
h2 ~ p {
    text-decoration: underline;
}
```

**Pseudo-classes**

Pseudo-classes target specific states or positions:

```css
/* :hover - when user hovers over an element */
a:hover {
    text-decoration: underline;
}

/* :focus - when an element has focus */
input:focus {
    border-color: blue;
}

/* :nth-child() - target by position */
li:nth-child(2) {
    font-weight: bold;
}

/* :first-child, :last-child */
p:first-child {
    margin-top: 0;
}

/* :not() - negation */
li:not(.disabled) {
    cursor: pointer;
}
```

**Pseudo-elements**

Pseudo-elements create virtual elements within or around elements:

```css
/* ::before - create content before an element */
p::before {
    content: "→ ";
}

/* ::after - create content after an element */
p::after {
    content: " ←";
}

/* ::first-line - style the first line of text */
p::first-line {
    font-weight: bold;
}

/* ::first-letter - style the first letter */
p::first-letter {
    font-size: 2em;
}

/* ::selection - style selected text */
p::selection {
    background-color: yellow;
}
```

These are just the basic selectors. CSS offers many more, allowing you to target elements with incredible precision.
            """,
            
            "best_practices": """
**Selector Best Practices**

**Keep Selectors Specific But Not Too Specific**

Too generic:
```css
/* This affects ALL divs on the page! */
div {
    color: red;
}
```

Better:
```css
/* Only divs with the card class */
.card {
    color: red;
}
```

Too specific (unnecessary):
```css
/* This works but is too specific */
html body main article div p.intro {
    color: red;
}
```

Optimal:
```css
/* Just specific enough */
.article-intro {
    color: red;
}
```

Overly specific selectors have problems:
- Hard to override if needed
- Tightly coupled to HTML structure
- Performance suffers (browsers evaluate selectors right to left)
- Brittle—break if the HTML structure changes

**Avoid Overly Complex Selectors**

While CSS lets you create complex selectors, they're often not worth it:

```css
/* Complex and hard to understand */
body > main > section.featured > div.container > article > p:first-of-type {
    font-weight: bold;
}

/* Better: use a class */
.featured-intro {
    font-weight: bold;
}
```

**Understand Selector Performance**

Browsers evaluate selectors from right to left. So in `section.featured article p`, the browser:
1. Finds all `<p>` tags (slowest—most work)
2. Filters to those inside `<article>` (less work)
3. Filters to those inside `.featured` (less work)

This means:
- Simple, efficient selectors are usually fine for most projects
- Overly complex selectors can impact performance
- Rightmost selector is most important (make it as specific as possible)

For most projects, this isn't a major concern—don't over-optimize. But understanding selector efficiency helps you write better CSS.

**Use Classes for Styling, IDs for Functionality**

```css
/* Good: use classes for styling */
.button { ... }
.button-primary { ... }
.button-secondary { ... }

/* Use IDs for JavaScript or unique page elements */
#main-navigation { ... }
#user-profile { ... }
```

Benefits:
- Classes are reusable (multiple elements can have the same class)
- IDs are unique (only one element should have each ID)
- It's clearer that classes are for styling, IDs for functionality
- Easier to override and extend styles with classes

**Name Classes Semantically**

Good class names describe the purpose, not the appearance:

```css
/* Bad: describes appearance, changes meaning if design changes */
.red-text { color: red; }
.big-font { font-size: 24px; }
.float-left { float: left; }

/* Good: describes purpose */
.error-message { color: red; }
.section-title { font-size: 24px; }
.article-thumbnail { float: left; }
```

With semantic names:
- Class names remain valid even if styles change
- Developers understand intent without seeing CSS
- Easier to maintain and refactor
- Better for team communication
            """,
        },
        
        "practical_examples": """
**Building a Styled Navigation Bar**

HTML:
```html
<nav class="navbar">
    <div class="navbar-logo">Logo</div>
    <ul class="navbar-menu">
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>
```

CSS:
```css
.navbar {
    background-color: #333;
    padding: 1em;
    display: flex;
    justify-content: space-between;
}

.navbar-logo {
    color: white;
    font-weight: bold;
    font-size: 1.5em;
}

.navbar-menu {
    list-style: none;
    display: flex;
    gap: 2em;
    margin: 0;
    padding: 0;
}

.navbar-menu a {
    color: white;
    text-decoration: none;
}

.navbar-menu a:hover {
    text-decoration: underline;
}
```

This example demonstrates:
- Using classes to select elements for styling
- Combining multiple selectors (descendant combinator)
- Using pseudo-classes for interactive states
- Building layout with CSS

**The Cascade in Action**

HTML:
```html
<p>Regular paragraph</p>
<p class="highlight">Highlighted paragraph</p>
<p id="featured">Featured paragraph</p>
```

CSS:
```css
p {
    color: black;        /* All paragraphs are black */
    font-size: 16px;
}

.highlight {
    color: blue;        /* highlighted paragraphs are blue */
}

#featured {
    color: red;         /* featured paragraph is red */
    font-size: 18px;    /* and slightly larger */
}
```

The cascade means:
- All `<p>` tags start with the base styles
- `.highlight` paragraphs override the color to blue
- `#featured` overrides color to red and size to 18px

Understanding this is crucial for writing CSS that doesn't fight itself.
        """,
        
        "key_takeaways": [
            "CSS is used to style and present content defined by HTML",
            "CSS rules consist of selectors and declaration blocks",
            "Selectors are patterns that target HTML elements for styling",
            "Simple selectors (element, class, ID) are the foundation",
            "Pseudo-classes and pseudo-elements allow advanced targeting",
            "Combinators show relationships between selectors",
            "The cascade and specificity determine which styles apply",
            "Write specific enough selectors to target the right elements without being overly complex",
            "Use classes for reusable styles and semantic naming conventions",
            "Understanding the cascade is crucial for effective CSS"
        ]
    }
}
