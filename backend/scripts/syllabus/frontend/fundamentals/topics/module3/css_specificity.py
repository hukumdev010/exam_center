"""
CSS Specificity - Detailed Content

This file contains comprehensive content for the "CSS Specificity" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "CSS Specificity",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    CSS specificity determines which styles are applied when multiple rules target
    the same element. Understanding specificity is essential for writing CSS that
    works as expected and is easy to maintain.
    """,
    
    "detailed_content": {
        "introduction": """
Specificity is one of the most important and misunderstood concepts in CSS. It's the set of rules that browsers use to determine which CSS rule "wins" when multiple rules target the same element.

Without understanding specificity, you'll find yourself:
- Writing `!important` to force styles to apply
- Getting frustrated when styles don't work
- Creating increasingly complex selectors
- Finding CSS hard to maintain and update

Mastering specificity leads to:
- CSS that's predictable and works as intended
- Easier to override and extend styles
- Less reliance on hacks like `!important`
- Cleaner, more maintainable stylesheets
        """,
        
        "key_concepts": {
            "how_specificity_works": """
**The Specificity Calculation**

Specificity is calculated using a 4-part scoring system: (a, b, c, d)

- **a**: Inline styles (style attribute) = 1000 points
- **b**: IDs = 100 points
- **c**: Classes, pseudo-classes, attributes = 10 points
- **d**: Elements and pseudo-elements = 1 point

The style with the highest specificity wins.

**Examples**

```css
p                          /* (0,0,0,1) = 1 point */

.intro                     /* (0,0,1,0) = 10 points */

p.intro                    /* (0,0,1,1) = 11 points */

#header                    /* (0,1,0,0) = 100 points */

div#header                 /* (0,1,0,1) = 101 points */

.nav .menu-item            /* (0,0,2,0) = 20 points */

#header .nav a:hover       /* (0,1,2,1) = 121 points */

div#main.container p:first-line  /* (0,1,1,2) = 112 points */
```

**Which Wins?**

If you have these rules:
```css
p { color: blue; }         /* Specificity: 1 */
.highlight { color: red; } /* Specificity: 10 */
p.highlight { color: green; } /* Specificity: 11 */
```

Applied to:
```html
<p class="highlight">Text</p>
```

The text will be green (specificity 11 wins).

**The Special Case of !important**

The `!important` flag overrides specificity:

```css
p { color: blue; }
.highlight { color: red !important; } /* This wins */
```

The `.highlight` style wins even though `!important` essentially gives it infinite specificity.

⚠️ **Avoid Using !important** ⚠️

Using `!important` is generally considered bad practice because:
- It breaks the cascading nature of CSS
- It makes overriding styles difficult
- It can lead to specificity wars where you add more `!important`s to override it
- It makes CSS harder to maintain

The only valid use cases are:
- User stylesheets that need to override page styles
- Utility classes that should always apply (with caution)
- Exceptional circumstances, not regular practice

**Key Rule: Keep Specificity Low**

The goal is to keep specificity as low as possible while still targeting the right elements. This makes:
- Styles easier to override
- CSS more maintainable
- Fewer conflicts
- Simpler debugging

```css
/* ❌ Too specific - hard to override, brittle */
div.container > section.content > article > p.intro {
    font-weight: bold;
}

/* ✅ Better - use a class */
.article-intro {
    font-weight: bold;
}
```
            """,
            
            "specificity_strategies": """
**Best Practices for Managing Specificity**

**1. Use Low-Specificity Selectors**

```css
/* ❌ High specificity - specific to structure */
div#main-section.primary-content > article.featured > h2.title {
    color: blue;
}

/* ✅ Low specificity - reusable */
.article-title {
    color: blue;
}
```

**2. Avoid IDs in CSS**

Use IDs only for JavaScript hooks or page structure, not for styling:

```css
/* ❌ ID in CSS = 100 specificity points */
#user-name {
    color: blue;
}

/* ✅ Class in CSS = 10 specificity points */
.user-name {
    color: blue;
}
```

When you later need to override `.user-name`, it's easy. Overriding `#user-name` requires another ID (creating specificity conflict).

**3. Chain Selectors Responsibly**

```css
/* ❌ Chaining increases specificity for every chain */
nav ul li a {
    color: blue;
}

nav ul li a:hover {
    color: red;
}

/* ✅ Use classes to control specificity */
.nav-link {
    color: blue;
}

.nav-link:hover {
    color: red;
}
```

**4. Use Specificity Hierarchy**

Create a logical structure for your CSS:

```css
/* Base styles - lowest specificity */
body { font-family: Arial; }
p { margin: 1em 0; }

/* Component styles - medium specificity */
.button { padding: 0.5em 1em; }
.button-primary { background: blue; }

/* Contextual overrides - use combinator or higher class chain */
.sidebar .button { padding: 0.25em 0.5em; }
```

**5. Use Attribute Selectors Instead of Complex Chains**

```css
/* ❌ High specificity through chaining */
div.error-message p {
    color: red;
}

/* ✅ Use attributes or classes */
[data-message="error"] {
    color: red;
}
```

**Debugging Specificity Issues**

When a style isn't applying:

1. **Check if the selector actually matches** - Use browser DevTools to inspect
2. **Check specificity** - Is another rule's specificity higher?
3. **Check source order** - If specificity is equal, the last rule wins
4. **Check !important** - Is `!important` being used?

Use browser DevTools:
- Right-click element, "Inspect"
- Look at Styles panel
- Struck-through rules have lower specificity and were overridden
- Green checkmark shows which rule won

```
Specific rule that applies ✓
Less specific rule (struck through)
Even less specific rule (struck through)
```

**The Cascade Principle**

CSS stands for "Cascading" Style Sheets. When specificity is equal, the LAST rule wins:

```css
.button { background: blue; }
.button { background: red; }
/* Background is red - later rule wins */
```

```css
.button { background: blue; }
.primary { background: green; }
.button { background: red; } /* Last rule wins */
/* Background is red */
```

This is why importing stylesheets in order matters - later stylesheets override earlier ones with equal specificity.
            """,
            
            "practical_examples": """
**Real-World Specificity Scenarios**

**Scenario 1: Button Styling**

```css
/* Base button style - low specificity */
.button {
    padding: 0.5em 1em;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

/* Button variations - same specificity as base, order matters */
.button-primary {
    background-color: blue;
    color: white;
}

.button-secondary {
    background-color: gray;
    color: white;
}

/* Size variations */
.button-small {
    padding: 0.25em 0.5em;
    font-size: 0.9em;
}

/* Context-specific override - use combinator, not specificity increase */
.modal .button {
    width: 100%;
}
```

HTML:
```html
<!-- Base button -->
<button class="button button-primary">Submit</button>

<!-- Different context -->
<div class="modal">
    <button class="button button-primary">OK</button>
</div>
```

**Scenario 2: Link Styling**

```css
/* Base link style */
a {
    color: #0066cc;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Special links */
.link-external {
    padding-right: 1.5em;
}

.link-external::after {
    content: " ↗";
}

/* Links in specific context */
footer a {
    color: white;
}

footer a:hover {
    text-decoration: underline;
}
```

**Scenario 3: Form Validation**

```css
/* Input base style */
input {
    padding: 0.5em;
    border: 1px solid #ccc;
}

/* Valid state - pseudo-class, not high specificity */
input:valid {
    border-color: green;
    background-color: #f0fff0;
}

/* Invalid state */
input:invalid {
    border-color: red;
    background-color: #fff0f0;
}

/* Disabled state */
input:disabled {
    background-color: #f5f5f5;
    cursor: not-allowed;
}

/* Required state - attribute selector */
input[required] {
    border-width: 2px;
}
```

**Scenario 4: Typography Hierarchy**

```css
/* Base typography - lowest specificity */
h1 { font-size: 2.5em; }
h2 { font-size: 2em; }
h3 { font-size: 1.5em; }

/* When used as page title */
.page-title {
    color: navy;
    text-align: center;
}

/* When used in sidebar */
.sidebar h2 {
    font-size: 1.3em;
    color: gray;
}

/* When used in card */
.card h3 {
    margin: 0;
    color: darkblue;
}
```

The key is:
- Set base styles with element selectors (low specificity)
- Add classes for variations
- Use combinators or attribute selectors for context, not specificity increase
- Avoid IDs in CSS
- Never use !important (except in rare cases)
            """,
        },
        
        "key_takeaways": [
            "Specificity determines which CSS rule applies when multiple rules target the same element",
            "Specificity is calculated as (a,b,c,d): inline styles, IDs, classes/attributes, elements",
            "When specificity is equal, the last rule in source order wins",
            "Keep specificity as low as possible for maintainable CSS",
            "Avoid using IDs in CSS stylesheets - use them only for structure",
            "Avoid using !important except in exceptional circumstances",
            "Use classes for styling, combinators for context",
            "Attribute selectors allow precise targeting without increasing specificity unnecessarily",
            "Browser DevTools show which rules apply and why others don't",
            "Understanding the cascade is as important as understanding specificity"
        ]
    }
}
