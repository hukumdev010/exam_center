"""
Class and ID Selectors - Detailed Content

This file contains comprehensive content for the "Class and ID Selectors" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Class and ID Selectors",
    "duration": "60-75 minutes",
    "difficulty": "Beginner",
    "overview": """
    Class and ID selectors are fundamental tools for targeting specific elements in CSS.
    This topic covers when and how to use classes and IDs, their differences, and best
    practices for naming and organizing them.
    """,
    
    "detailed_content": {
        "introduction": """
While element selectors target all instances of an element type, class and ID selectors let you target specific elements or groups of elements. Classes and IDs are attributes you add to HTML elements, and CSS selectors use them to apply targeted styles.

Class selectors (`.classname`) are far more common than ID selectors (`#idname`), and understanding when to use each is crucial. Classes are reusable and can appear on many elements; IDs should be unique, appearing on at most one element per page.

The distinction between classes and IDs is one of the most important concepts in CSS. Used correctly, they lead to maintainable, scalable stylesheets. Used incorrectly, they can create messy, hard-to-maintain CSS that fights itself.
        """,
        
        "key_concepts": {
            "understanding_classes": """
**What Are Classes?**

A class is an attribute you add to HTML elements to group them or identify them for styling purposes:

```html
<p class="intro">This is an introductory paragraph.</p>
<p>This is a regular paragraph.</p>
<p class="intro">This is another introductory paragraph.</p>
```

In CSS, you target elements with a class using a dot (`.`):

```css
.intro {
    font-weight: bold;
    font-size: 1.1em;
}
```

**Key Characteristics of Classes**

- **Reusable**: Many HTML elements can have the same class
- **Multiple Classes**: An element can have multiple classes
- **Lower Specificity**: Lower than ID, but higher than element selectors
- **Flexible**: Easy to add, remove, or change dynamically with JavaScript

**Multiple Classes on One Element**

Separate multiple class names with spaces:

```html
<button class="btn btn-primary btn-large">
    Click Me
</button>
```

CSS:
```css
.btn {
    padding: 0.5em 1em;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.btn-primary {
    background-color: #0066cc;
    color: white;
}

.btn-large {
    padding: 1em 2em;
    font-size: 1.1em;
}
```

This approach is powerful:
- `.btn` establishes base button styles
- `.btn-primary` adds primary styling
- `.btn-large` makes it bigger
- One element gets all three styles

**Class Naming Conventions**

Write meaningful class names that describe purpose, not appearance:

```css
/* ❌ Bad - describes appearance, becomes wrong if design changes */
.red-text { color: red; }
.big-font { font-size: 24px; }
.float-left { float: left; }

/* ✅ Good - describes purpose/component */
.error-message { color: red; }
.page-title { font-size: 24px; }
.sidebar { float: left; }
```

Common naming conventions:

**BEM (Block Element Modifier)**
```css
.card { /* Block - main component */ }
.card__header { /* Element - part of block */ }
.card__title { /* Element */ }
.card--featured { /* Modifier - variation */ }
.card--small { /* Modifier */ }
```

**Simple Descriptive Names**
```css
.alert { /* Main component */ }
.alert-success { /* Variation */ }
.alert-error { /* Variation */ }
.alert-message { /* Sub-element */ }
```

**Kebab-case (preferred in CSS)**
```css
.primary-button { /* not .primaryButton */ }
.sidebar-navigation { /* not .sidebarNavigation */ }
.featured-article { /* not .featuredArticle */ }
```

Use lowercase and hyphens for consistency and readability.
            """,
            
            "understanding_ids": """
**What Are IDs?**

An ID is an attribute used to give a unique identifier to an element:

```html
<header id="main-header">
    <h1>Welcome</h1>
</header>
<main id="main-content">
    <article>...</article>
</main>
<footer id="footer">
    <p>&copy; 2025</p>
</footer>
```

In CSS, you target elements with an ID using a hash (#):

```css
#main-header {
    background-color: #333;
    color: white;
}

#main-content {
    padding: 2em;
}

#footer {
    background-color: #f5f5f5;
    text-align: center;
}
```

**Key Characteristics of IDs**

- **Unique**: Each ID should appear on at most one element per page
- **High Specificity**: Higher specificity than classes (harder to override)
- **Limited Reusability**: Should not be reused across elements
- **Functional**: Often used for JavaScript hooks and anchors

**IDs vs Classes: When to Use Each**

**Use Classes for Styling**

Classes are the primary way to apply reusable styles:

```css
.button { /* Reusable button style */ }
.button-primary { /* Variation */ }
.card { /* Reusable card style */ }
.alert { /* Reusable alert style */ }
```

```html
<button class="button button-primary">Save</button>
<button class="button">Cancel</button>
<div class="card">...</div>
<div class="card">...</div>
<div class="alert alert-error">Error occurred</div>
```

**Use IDs for Unique Page Sections**

IDs are appropriate for unique structural sections:

```css
#header { /* Page header */ }
#main-content { /* Main content area */ }
#sidebar { /* Sidebar */ }
#footer { /* Page footer */ }
```

```html
<header id="header">...</header>
<main id="main-content">...</main>
<aside id="sidebar">...</aside>
<footer id="footer">...</footer>
```

**Use IDs for JavaScript Hooks**

JavaScript often uses IDs to target elements:

```html
<button id="submit-button">Submit</button>
<form id="contact-form">...</form>
```

```javascript
const submitBtn = document.getElementById('submit-button');
const form = document.getElementById('contact-form');
```

**Use IDs for Page Anchors**

IDs enable linking to specific sections:

```html
<a href="#features">Jump to Features</a>

<section id="features">
    <h2>Features</h2>
</section>
```

**The Specificity Problem with IDs**

IDs have very high specificity, which can cause problems:

```css
#header { color: blue; }

/* This won't work - ID has higher specificity */
.text-red { color: red; }
```

```html
<h1 id="header" class="text-red">Title</h1>
<!-- Will be blue, not red! -->
```

To avoid this, many developers minimize ID use in CSS and prefer classes.
            """,
            
            "specificity_and_practice": """
**Specificity Calculation**

When multiple CSS rules target the same element, specificity determines which rule wins:

- Element selector: 1 point
- Class selector: 10 points
- ID selector: 100 points
- Inline styles: 1000 points

Examples:

```css
p { color: blue; } /* Specificity: 1 */

.intro { color: green; } /* Specificity: 10 */

#special { color: red; } /* Specificity: 100 */

.container .intro { color: purple; } /* Specificity: 10 + 10 = 20 */

.container > .intro { color: orange; } /* Specificity: 10 + 10 = 20 */
```

When HTML matches multiple rules, the highest specificity wins.

**Practical Class Organization**

Here's how a real project might organize classes:

**Component Classes**
```css
/* Cards */
.card { ... }
.card-header { ... }
.card-body { ... }
.card-footer { ... }

/* Buttons */
.btn { ... }
.btn-primary { ... }
.btn-secondary { ... }

/* Forms */
.form-group { ... }
.form-input { ... }
.form-label { ... }
```

**Utility Classes**
```css
.text-center { text-align: center; }
.text-right { text-align: right; }
.mb-1 { margin-bottom: 0.5em; }
.mb-2 { margin-bottom: 1em; }
.mt-1 { margin-top: 0.5em; }
.p-1 { padding: 0.5em; }
.hidden { display: none; }
.flex { display: flex; }
```

**State Classes**
```css
.is-active { ... }
.is-disabled { ... }
.is-loading { ... }
.is-error { ... }
.is-success { ... }
```

**Best Practices**

✅ **Do**
- Use classes for styling (most of your CSS)
- Use IDs for unique sections and JavaScript hooks
- Name classes semantically
- Use kebab-case for class names
- Write classes to be reusable
- Keep specificity low

❌ **Don't**
- Use IDs for general styling
- Create overly specific selectors
- Name classes after appearance (`red-text`, `big-button`)
- Use unnecessary elements just to apply styles
- Create classes that are too generic (`.section`, `.container`)
- Make classes too narrow (`.product-card-in-featured-section`)
            """,
        },
        
        "key_takeaways": [
            "Classes are reusable and should be your primary styling tool",
            "IDs are unique identifiers useful for structure and JavaScript hooks",
            "Use classes for reusable components and styling",
            "Use IDs for unique page sections and JavaScript targeting",
            "Multiple classes can be applied to a single element",
            "Write semantic class names that describe purpose, not appearance",
            "Keep class names lowercase and use hyphens (kebab-case)",
            "Avoid using IDs in CSS to keep specificity low and CSS maintainable",
            "Consider using naming conventions like BEM for consistency",
            "Remember that class selectors have higher specificity than element selectors but lower than IDs"
        ]
    }
}
