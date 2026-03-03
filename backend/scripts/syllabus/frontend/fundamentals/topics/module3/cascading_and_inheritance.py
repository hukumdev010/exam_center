"""
Cascading and Inheritance - Detailed Content

This file contains comprehensive content for the "Cascading and Inheritance" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Cascading and Inheritance",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    The "Cascading" in Cascading Style Sheets refers to how styles flow from parent
    to child elements and how conflicts are resolved. Understanding cascading and
    inheritance is essential for writing effective CSS.
    """,
    
    "detailed_content": {
        "introduction": """
Cascading and inheritance are two fundamental mechanisms that make CSS work. Together, they mean you don't have to specify every style for every element—styles can flow from parents to children, and multiple stylesheets can work together seamlessly.

The word "cascade" in CSS means that styles flow downward, with later rules overriding earlier ones. Inheritance means that some CSS properties are inherited from parent elements to their children. Understanding both is key to writing efficient CSS.
        """,
        
        "key_concepts": {
            "the_cascade": """
**What is the Cascade?**

The cascade refers to how CSS resolves conflicts when multiple rules target the same element. The cascade considers:

1. **Source Order**: Later rules override earlier rules with the same specificity
2. **Specificity**: Higher specificity rules override lower specificity rules
3. **Importance**: User stylesheets and !important declarations override others

**How the Cascade Works**

Imagine these stylesheets loaded in order:

```css
/* browser-defaults.css - Loaded first */
p { color: black; }

/* style.css - Loaded second */
p { color: blue; }

/* inline-style.css - Loaded third */
p { color: red; }
```

The last one wins! The paragraph text will be red.

**Specificity in the Cascade**

When specificity differs, the more specific rule wins regardless of source order:

```css
p { color: blue; }            /* Specificity: 1 */
.highlight { color: red; }    /* Specificity: 10 - THIS WINS */
```

Even though the element selector appears first, the class selector wins because it has higher specificity.

```html
<p class="highlight">Red text</p>
```

**Source Order Matters When Specificity is Equal**

```css
.button { background: blue; }
.button { background: red; }  /* THIS WINS - same specificity, later rule */
```

This is why ordering stylesheets matters. External stylesheets in order:

```html
<link rel="stylesheet" href="normalize.css">    <!-- Loaded first -->
<link rel="stylesheet" href="base-styles.css">  <!-- Loaded second -->
<link rel="stylesheet" href="components.css">   <!-- Loaded third -->
<link rel="stylesheet" href="overrides.css">    <!-- Loaded last - wins conflicts -->
```

**The Cascade for Maintainability**

Smart use of the cascade makes CSS maintainable:

```css
/* General styles - low specificity */
button {
    padding: 0.5em 1em;
    font-size: 1em;
    border: none;
    cursor: pointer;
}

/* Variations - same specificity, later rules override */
.button-primary {
    background: blue;
    color: white;
}

.button-danger {
    background: red;
    color: white;
}

/* Contextual variations - use cascade to override */
.sidebar .button {
    font-size: 0.9em;
}
```

The cascade lets you define base styles once, then override them for specific contexts without using high-specificity selectors.
            """,
            
            "inheritance": """
**What is Inheritance?**

Inheritance means that certain CSS properties are automatically inherited by child elements from their parent. You don't have to explicitly set these properties on every element.

**Which Properties are Inherited?**

Most properties that make sense to inherit do:

**Commonly Inherited Properties:**
- `color` - Text color
- `font-family` - Font choice
- `font-size` - Text size
- `font-weight` - Text boldness
- `font-style` - Text italics
- `line-height` - Line spacing
- `text-align` - Text alignment
- `text-indent` - Indentation
- `letter-spacing` - Letter spacing
- `word-spacing` - Word spacing
- `text-transform` - Case transformation
- `list-style` - List styling

**Example of Inheritance:**

```css
body {
    font-family: Arial, sans-serif;
    color: #333;
    line-height: 1.6;
}
```

HTML:
```html
<body>
    <p>This paragraph inherits font-family, color, and line-height from body</p>
    <div>
        <span>Span also inherits from body through div</span>
    </div>
</body>
```

Every element inside body inherits these properties without you having to set them explicitly.

**Which Properties are NOT Inherited?**

Properties that control layout, spacing, or appearance:

```css
/* NOT inherited - you must set on each element */
margin          /* Space outside element */
padding         /* Space inside element */
border          /* Border styling */
width, height   /* Element dimensions */
background      /* Background styling */
position        /* Positioning */
display         /* Display mode */
```

This makes sense! You don't want all children to inherit the parent's margin or width.

**Forcing Inheritance: inherit Keyword**

You can force inheritance with the `inherit` keyword:

```css
.container {
    border: 2px solid blue;
}

.container p {
    border: inherit; /* Forces p to inherit container's border */
}
```

**Resetting Inheritance: initial Keyword**

The `initial` keyword resets a property to its default value:

```css
body {
    color: blue;
}

.reset {
    color: initial; /* Back to browser default (usually black) */
}
```

**Practical Inheritance Examples**

**Typography System**

```css
body {
    font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
    color: #333;
    line-height: 1.6;
}

/* All text elements inherit these */
p, li, span, div { /* inheritance means we don't need to set these */ }

/* Override as needed */
code {
    font-family: 'Courier New', monospace;
    background: #f5f5f5;
}

strong {
    font-weight: 600;
}
```

**Link Styling**

```css
body {
    color: #333;
}

a {
    color: #0066cc;        /* Override inherited color */
    text-decoration: none; /* Not inherited */
}

a:hover {
    text-decoration: underline;
}
```

**List Styling**

```css
ul {
    list-style: none;      /* Not inherited to nested lists */
    margin: 0;
    padding: 0;
}

li {
    margin-bottom: 0.5em;
    color: inherit;        /* Inherit color from ul */
}
```
            """,
            
            "cascade_and_inheritance_together": """
**How They Work Together**

The cascade determines which styles apply, and inheritance means you don't have to specify everything.

**Example: Building a Card Component**

```css
/* Step 1: Set base typography */
body {
    font-family: Arial, sans-serif;
    color: #333;
    line-height: 1.6;
}

/* Step 2: Create card container */
.card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 1.5em;
    background: white;
}

/* Step 3: Override inherited styles for specific elements */
.card h2 {
    color: navy;              /* Override inherited color */
    margin-top: 0;
    font-size: 1.5em;
}

.card p {
    margin: 0.5em 0;         /* Override default paragraph margin */
}

.card a {
    color: #0066cc;          /* Override inherited color again */
}
```

HTML:
```html
<div class="card">
    <h2>Card Title</h2>
    <p>This text inherits font-family, line-height from body</p>
    <p>But overrides color to navy for headings</p>
    <a href="#">Link inherits from body but overrides color</a>
</div>
```

**Real-World CSS Organization**

```css
/* 1. Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* 2. Set inherited values once */
body {
    font-family: 'Segoe UI', system-ui, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #333;
}

/* 3. Element defaults */
a { color: #0066cc; }
code { font-family: monospace; }

/* 4. Component styles - cascade overrides as needed */
.header {
    background: #333;
    color: white;  /* Override inherited color */
}

.header a {
    color: white;  /* Override a's inherited color */
}

.footer {
    background: #f5f5f5;
    color: #666;   /* Override inherited color */
    font-size: 0.9em;
}
```

**Tips for Using Cascade and Inheritance**

✅ **Do**
- Set inherited properties (color, font-family, line-height) on body or high-level containers
- Use the cascade to avoid repeating rules
- Override inherited values only when needed
- Organize stylesheets by specificity level

❌ **Don't**
- Assume all properties are inherited (they're not)
- Fight the cascade with high specificity - work with it
- Use `!important` to override inheritance issues
- Repeat styles that could be inherited from a parent
            """,
        },
        
        "key_takeaways": [
            "The cascade determines which CSS rule applies when conflicts exist",
            "Source order matters: later rules override earlier rules with equal specificity",
            "Specificity matters more than source order when specificity differs",
            "Inheritance means child elements automatically get parent's CSS property values",
            "Most typography properties are inherited (color, font-*, line-height)",
            "Layout and spacing properties are NOT inherited (margin, padding, width, height)",
            "Use the inherit keyword to force inheritance when needed",
            "Use the initial keyword to reset inherited values",
            "Smart use of inheritance and cascade reduces CSS repetition",
            "Organize stylesheets from general to specific to leverage the cascade"
        ]
    }
}
