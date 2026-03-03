"""
Element Selectors - Detailed Content

This file contains comprehensive content for the "Element Selectors" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Element Selectors",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    Element selectors (also called type selectors) are the simplest and most fundamental
    way to apply styles to HTML elements. This topic covers how to target elements by
    their HTML tag name and use them effectively.
    """,
    
    "detailed_content": {
        "introduction": """
Element selectors are the most basic selectors in CSS. They target all instances of a specific HTML element on a page. When you write `p { color: blue; }`, you're using an element selector to target all `<p>` tags.

Element selectors are incredibly useful for:
- Setting global styles for all elements of a type
- Resetting default browser styles
- Establishing base styling before applying more specific overrides
- Creating consistent typography across a page
- Reducing the amount of CSS you need to write

Element selectors have the lowest specificity (other than universal selector), which means they're easy to override with more specific selectors when needed. This makes them perfect for global base styles.
        """,
        
        "key_concepts": {
            "basic_element_selectors": """
**Simple Element Selection**

The most basic syntax is just the element name:

```css
p {
    color: #333;
}

h1 {
    font-size: 2em;
}

a {
    color: #0066cc;
}

img {
    max-width: 100%;
}
```

Each rule applies to ALL instances of that element on the page. If your HTML has 10 paragraphs, the `p` rule affects all 10 of them.

**Common Elements to Style**

**Text Elements**
```css
h1, h2, h3, h4, h5, h6 { font-family: Arial, sans-serif; }
p { line-height: 1.6; }
strong { font-weight: 600; }
em { font-style: italic; }
a { text-decoration: none; }
```

**Lists**
```css
ul { list-style-type: none; }
ol { counter-reset: item; }
li { margin: 0.5em 0; }
```

**Form Elements**
```css
input { padding: 0.5em; }
button { cursor: pointer; }
textarea { resize: vertical; }
select { width: 100%; }
```

**Structural Elements**
```css
body { background-color: white; }
header { background-color: #333; }
footer { background-color: #f5f5f5; }
section { margin: 2em 0; }
```

**Why Element Selectors Matter**

Element selectors are often your first line of defense for global styling. Before writing class-specific styles, start with element selectors for defaults:

```css
/* Global resets and defaults */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
}

p { margin-bottom: 1em; }

a { color: #0066cc; }

/* Now override with classes where needed */
.button { /* Different styling for button links */ }
.error { color: red; }
```

**Performance Consideration**

Element selectors are efficient. The browser evaluates selectors from right to left, so `p` is quick to evaluate—it just finds all paragraphs. Compare:

```css
/* Very fast - direct element match */
p { color: blue; }

/* Still fast - relatively specific */
article p { color: blue; }

/* Slower - looks at many elements */
body * p { color: blue; }
```

For most projects, this doesn't matter. But knowing that simple element selectors are performant is good to understand.
            """,
            
            "grouping_selectors": """
**Applying the Same Style to Multiple Elements**

Often, you want the same style to apply to multiple different elements. Rather than writing the same rule repeatedly, you can group selectors with commas:

```css
/* Without grouping - repetitive */
h1 { color: navy; }
h2 { color: navy; }
h3 { color: navy; }
h4 { color: navy; }
h5 { color: navy; }
h6 { color: navy; }

/* With grouping - cleaner */
h1, h2, h3, h4, h5, h6 {
    color: navy;
}
```

**Common Grouping Patterns**

Grouping related form elements:
```css
input, textarea, select {
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: inherit;
}
```

Grouping text formatting elements:
```css
strong, b {
    font-weight: 700;
}

em, i {
    font-style: italic;
}

mark {
    background-color: yellow;
}
```

Grouping structural elements:
```css
header, footer, section, article {
    margin: 1em 0;
}

h1, h2, h3, h4, h5, h6 {
    line-height: 1.2;
    font-weight: 600;
}
```

**Complex Grouping**

You can combine grouping with other selectors:

```css
/* Multiple elements inside another element */
main h1, main h2 {
    color: navy;
}

/* Multiple combinators */
article > p, aside > p {
    color: gray;
}
```

This is cleaner than writing separate rules:

```css
main h1 { color: navy; }
main h2 { color: navy; }
aside > p { color: gray; }
article > p { color: gray; }
```

**Benefits of Grouping**

- **Less CSS**: Write less code, maintain less code
- **Consistency**: One change updates multiple elements
- **Readability**: Shows which elements have related styling
- **Maintainability**: Easier to understand intent
            """,
            
            "practical_applications": """
**Reset and Normalize Styles**

Browsers have default styles for elements. Resetting or normalizing these defaults is common practice:

```css
/* Simple reset */
* {
    margin: 0;
    padding: 0;
}

/* More comprehensive normalize approach */
body, html {
    margin: 0;
    padding: 0;
}

h1, h2, h3, h4, h5, h6 {
    margin: 0;
    padding: 0;
    font-weight: normal;
}

p {
    margin: 0;
    padding: 0;
}

ul, ol, li {
    list-style: none;
    margin: 0;
    padding: 0;
}
```

**Setting Base Typography**

Establish consistent typography across your site:

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #333;
}

h1 { font-size: 2.5em; }
h2 { font-size: 2em; }
h3 { font-size: 1.5em; }
h4 { font-size: 1.25em; }

p { margin-bottom: 1em; }

a { color: #0066cc; }
```

**Form Element Consistency**

Make form elements consistent across browsers:

```css
input, textarea, select, button {
    font-family: inherit;
    font-size: inherit;
    padding: 0.5em;
    border: 1px solid #ccc;
    border-radius: 4px;
}

input:focus, textarea:focus, select:focus {
    outline: none;
    border-color: #0066cc;
    box-shadow: 0 0 5px rgba(0, 102, 204, 0.3);
}

button {
    background-color: #0066cc;
    color: white;
    cursor: pointer;
}

button:hover {
    background-color: #0052a3;
}
```

**Building a Type System**

Use element selectors to establish a consistent type system:

```css
/* Headings */
h1, h2, h3, h4, h5, h6 {
    font-weight: 600;
    line-height: 1.2;
    margin: 1.5em 0 0.5em 0;
}

h1 { font-size: 2.5em; }
h2 { font-size: 2em; }
h3 { font-size: 1.5em; }
h4 { font-size: 1.25em; }
h5 { font-size: 1.1em; }
h6 { font-size: 1em; }

/* Body text */
p { margin-bottom: 1em; }

/* Links */
a {
    color: #0066cc;
    text-decoration: none;
    border-bottom: 1px solid transparent;
    transition: all 0.2s;
}

a:hover {
    border-bottom-color: #0066cc;
}

/* Code and technical text */
code { font-family: 'Courier New', monospace; }
```

This ensures:
- Consistent spacing between elements
- Predictable behavior for all elements of a type
- Easy to override for exceptions with more specific selectors
- Easy to maintain—change the rule once, affects all elements
            """,
        },
        
        "key_takeaways": [
            "Element selectors target all instances of an HTML element",
            "They're the foundation of CSS and have the lowest specificity",
            "Perfect for setting global defaults and base styles",
            "Use element selectors for typography, resets, and consistent styling",
            "Grouping selectors with commas reduces repetition",
            "Element selectors are performant and quick to evaluate",
            "Combine element selectors with other selectors for more control",
            "Best practice: use element selectors for base styles, then override with classes",
            "Consider normalizing or resetting browser defaults with element selectors",
            "Build a consistent type system starting with element selectors"
        ]
    }
}
