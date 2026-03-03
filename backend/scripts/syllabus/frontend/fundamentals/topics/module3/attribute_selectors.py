"""
Attribute Selectors - Detailed Content

This file contains comprehensive content for the "Attribute Selectors" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Attribute Selectors",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Attribute selectors allow you to target HTML elements based on their attributes
    and attribute values. This powerful feature enables precise styling without
    relying solely on classes or IDs.
    """,
    
    "detailed_content": {
        "introduction": """
Attribute selectors are powerful CSS tools that let you target elements based on their HTML attributes. Whether an element has a specific attribute, or has an attribute with a specific value, attribute selectors can help you apply styles.

Attribute selectors are particularly useful for:
- Styling form inputs by type without adding extra classes
- Targeting links by protocol (email, external, etc.)
- Styling elements with data attributes
- Creating responsive designs based on viewport attributes
- Reducing the need for extra HTML classes

They're underutilized in many stylesheets, but they're incredibly helpful for keeping HTML clean and reducing CSS complexity.
        """,
        
        "key_concepts": {
            "basic_attribute_selectors": """
**Types of Attribute Selectors**

**Presence Selector - [attribute]**
Matches elements that have a specific attribute, regardless of value:

```css
/* All input elements with a required attribute */
input[required] {
    border: 2px solid orange;
}

/* All links with a title attribute */
a[title] {
    text-decoration: underline dotted;
}

/* All form elements with a disabled attribute */
input[disabled] {
    opacity: 0.5;
    cursor: not-allowed;
}
```

**Exact Value Selector - [attribute="value"]**
Matches elements where the attribute exactly equals the value:

```css
/* Buttons with type="submit" */
button[type="submit"] {
    background-color: green;
}

/* Links pointing to external sites */
a[target="_blank"] {
    padding-right: 1.5em;
}

/* Form inputs of type "email" */
input[type="email"] {
    border: 1px solid #ccc;
}

/* All images with specific alt text */
img[alt="logo"] {
    max-height: 100px;
}
```

**Substring Matching Selectors**

These match attributes containing substrings:

```css
/* Attribute starts with a value - [attribute^="value"] */
a[href^="https"] {
    padding-right: 1.5em;
}
/* Matches: https://example.com, https://google.com */

/* Attribute ends with a value - [attribute$="value"] */
a[href$=".pdf"] {
    padding-right: 1.5em;
}
/* Matches: document.pdf, guide.pdf */

/* Attribute contains a value - [attribute*="value"] */
img[alt*="screenshot"] {
    border: 1px solid gray;
}
/* Matches: "screenshot-1", "my-screenshot", "screenshot" */

/* Attribute contains word - [attribute~="value"] */
div[class~="featured"] {
    border: 2px solid gold;
}
/* Matches: class="featured", class="article featured large" */
/* Does NOT match: class="featured-article" */
```

**Case-Insensitive Matching - [attribute="value" i]**

By default, matching is case-sensitive. Use `i` flag for case-insensitivity:

```css
/* Matches TYPE, type, Type */
input[type="submit" i] {
    background-color: green;
}

/* Matches .pdf, .PDF, .Pdf */
a[href$=".pdf" i] {
    padding-right: 1.5em;
}
```

**Practical Examples**

Form styling:
```css
/* Text inputs */
input[type="text"] {
    padding: 0.5em;
    border: 1px solid #ccc;
}

/* Number inputs */
input[type="number"] {
    text-align: right;
}

/* Checkboxes */
input[type="checkbox"] {
    margin: 0.5em;
}

/* Radio buttons */
input[type="radio"] {
    margin: 0 0.5em;
}

/* Required fields */
input[required] {
    border: 2px solid orange;
}

/* Disabled fields */
input[disabled] {
    background-color: #f5f5f5;
    cursor: not-allowed;
}
```

Link styling:
```css
/* External links */
a[target="_blank"]::after {
    content: " ↗";
    font-size: 0.8em;
}

/* Email links */
a[href^="mailto:"]::before {
    content: "✉ ";
}

/* Phone links */
a[href^="tel:"]::before {
    content: "☎ ";
}

/* PDF links */
a[href$=".pdf"]::after {
    content: " (PDF)";
    font-size: 0.8em;
}

/* Secure links */
a[href^="https://"] {
    color: green;
}

/* Insecure links */
a[href^="http://"] {
    color: red;
}
```

Image styling:
```css
/* Images with alt text */
img[alt] {
    border: 1px solid #ccc;
}

/* Images without alt text (for accessibility checking) */
img:not([alt]) {
    border: 3px solid red;
    /* Helps identify images missing alt text */
}

/* Responsive images */
img[srcset] {
    width: 100%;
    height: auto;
}
```
            """,
            
            "data_attributes": """
**Styling with Data Attributes**

Data attributes (`data-*`) are custom attributes that store information in HTML elements. They're perfect for styling without adding extra classes:

```html
<button data-status="active">Active</button>
<button data-status="inactive">Inactive</button>
<button data-status="pending">Pending</button>

<div data-priority="high">Important task</div>
<div data-priority="medium">Regular task</div>
<div data-priority="low">Low priority</div>
```

CSS:
```css
/* Different styles based on data attribute value */
button[data-status="active"] {
    background-color: green;
    color: white;
}

button[data-status="inactive"] {
    background-color: gray;
    color: white;
    opacity: 0.5;
}

button[data-status="pending"] {
    background-color: orange;
    color: white;
}

/* Div styling */
div[data-priority="high"] {
    border-left: 4px solid red;
    background-color: #ffe0e0;
}

div[data-priority="medium"] {
    border-left: 4px solid orange;
    background-color: #fff5e0;
}

div[data-priority="low"] {
    border-left: 4px solid gray;
    background-color: #f5f5f5;
}
```

**Why Use Data Attributes?**

- Keep HTML clean without extra classes
- Semantic meaning (data-* conveys purpose)
- Easier for JavaScript to access
- Multiple values can be stored
- Works perfectly with attribute selectors

**Combining with Pseudo-Elements**

```html
<div data-rating="5">Five-star product</div>
```

```css
div[data-rating="5"]::before {
    content: "★★★★★";
    color: gold;
    margin-right: 0.5em;
}

div[data-rating="4"]::before {
    content: "★★★★☆";
}

div[data-rating="3"]::before {
    content: "★★★☆☆";
}
```
            """,
            
            "advanced_patterns": """
**Combining Attribute Selectors**

You can use multiple attribute selectors together:

```css
/* Input that is both required AND type="text" */
input[required][type="text"] {
    border: 2px solid orange;
}

/* Link that opens in new tab AND is external */
a[target="_blank"][rel="noopener"] {
    padding-right: 1.5em;
}

/* Button that is both type="submit" AND disabled */
button[type="submit"][disabled] {
    opacity: 0.5;
    cursor: not-allowed;
}
```

**Complex Selectors**

```css
/* Form control inside a disabled fieldset */
fieldset[disabled] input,
fieldset[disabled] select,
fieldset[disabled] textarea {
    cursor: not-allowed;
    opacity: 0.6;
}

/* Required form fields with error state */
input[required]:invalid {
    border-color: red;
    background-color: #ffe0e0;
}

/* Required form fields with valid state */
input[required]:valid {
    border-color: green;
    background-color: #e0ffe0;
}
```

**Real-World Example: Product Rating System**

HTML:
```html
<div class="product" data-category="electronics" data-rating="4.5">
    <h3>Laptop</h3>
</div>

<div class="product" data-category="books" data-rating="3.8">
    <h3>Novel</h3>
</div>
```

CSS:
```css
/* Highlight high-rated products */
.product[data-rating^="4"],
.product[data-rating^="5"] {
    border: 2px solid gold;
    background-color: #fffef0;
}

/* Style low-rated products */
.product[data-rating^="1"],
.product[data-rating^="2"] {
    opacity: 0.7;
}

/* Filter by category */
.product[data-category="electronics"] {
    border-left: 4px solid blue;
}

.product[data-category="books"] {
    border-left: 4px solid green;
}
```

**Performance Note**

Attribute selectors are more efficient than they used to be in older browsers. Modern browsers handle them very well. Some considerations:

- Substring matching (`*=`, `^=`, `$=`, `~=`) is slightly slower than exact matching (`=`)
- Still faster than JavaScript equivalent
- Perfectly fine for normal use

Don't worry about performance unless dealing with thousands of elements.
            """,
        },
        
        "key_takeaways": [
            "Attribute selectors target elements based on HTML attributes",
            "[attr] selects elements that have the attribute",
            "[attr=\"value\"] selects elements with exact attribute value",
            "[attr^=\"value\"] selects if attribute starts with value (prefix match)",
            "[attr$=\"value\"] selects if attribute ends with value (suffix match)",
            "[attr*=\"value\"] selects if attribute contains value (substring match)",
            "[attr~=\"value\"] selects if attribute contains word separated by whitespace",
            "Use case-insensitive flag [attr=\"value\" i] for case-insensitive matching",
            "Data attributes (data-*) are perfect for custom styling without extra classes",
            "Attribute selectors reduce need for extra classes and keep HTML clean"
        ]
    }
}
