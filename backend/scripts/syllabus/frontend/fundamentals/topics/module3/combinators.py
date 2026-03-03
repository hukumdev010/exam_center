"""
Combinators - Detailed Content

This file contains comprehensive content for the "Combinators" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Combinators",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Combinators describe relationships between selectors in CSS. They allow you to
    target elements based on their position relative to other elements in the DOM tree.
    This is essential for creating flexible, maintainable stylesheets.
    """,
    
    "detailed_content": {
        "introduction": """
Combinators are symbols in CSS selectors that show the relationship between elements. They allow you to say things like "style all paragraphs inside divs" or "style list items that immediately follow headings."

Understanding combinators is crucial for:
- Writing selectors that don't depend on extra classes
- Creating flexible stylesheets that adapt to different HTML structures
- Reducing the amount of CSS you need to write
- Targeting elements based on context rather than arbitrary markers

CSS offers four main combinators, each describing a different relationship.
        """,
        
        "key_concepts": {
            "descendant_combinator": """
**Descendant Combinator (Space)**

The descendant combinator (represented by a space) targets elements that are descendants of another element, at any level:

```css
/* All <p> elements inside <div> elements */
div p {
    color: blue;
}

/* All <a> elements inside <article> elements */
article a {
    color: #0066cc;
}

/* All <li> elements inside <ul> elements */
ul li {
    margin: 0.5em 0;
}

/* Deeper nesting - any <span> inside any <div> inside <nav> */
nav div span {
    font-weight: bold;
}
```

HTML examples that match `div p`:
```html
<!-- Matches - p is child of div -->
<div>
    <p>This matches</p>
</div>

<!-- Matches - p is grandchild of div -->
<div>
    <article>
        <p>This also matches</p>
    </article>
</div>

<!-- Does NOT match - p is not inside div -->
<article>
    <p>This doesn't match</p>
</article>
```

**When to Use Descendant Combinator**

Descendant combinators are useful for:
- Styling elements within specific containers
- Creating context-dependent styles
- Reducing the need for classes

```css
/* All inputs inside forms */
form input {
    padding: 0.5em;
}

/* All links inside headers */
header a {
    color: white;
    text-decoration: none;
}

/* All text inside cards */
.card p,
.card h2,
.card h3 {
    margin: 0.5em 0;
}
```

**Performance Consideration**

The browser evaluates selectors from right to left. In `article p`, it:
1. Finds all `<p>` tags (slow - most work)
2. Filters to those inside `<article>` (faster)

While this is less efficient than just `p`, it's still very fast for most use cases.
            """,
            
            "child_combinator": """
**Child Combinator (>)**

The child combinator targets elements that are direct children of another element (only one level down):

```css
/* Direct <li> children of <ul> (not nested <ul>s) */
ul > li {
    list-style: square;
}

/* Direct <p> children of <div> (not nested divs' paragraphs) */
div > p {
    color: blue;
}

/* Direct <a> children of <nav> */
nav > a {
    margin: 0 1em;
}
```

HTML examples that match `ul > li`:
```html
<!-- Matches - li is direct child of ul -->
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
</ul>

<!-- Only OUTER items match, not items in nested ul -->
<ul>
    <li>Item 1</li>          <!-- Matches -->
    <li>Item 2              <!-- Matches -->
        <ul>
            <li>Item 2.1</li>  <!-- Does NOT match -->
            <li>Item 2.2</li>  <!-- Does NOT match -->
        </ul>
    </li>
</ul>

<!-- Does NOT match - li inside article inside ul -->
<ul>
    <article>
        <li>Item</li>  <!-- Does NOT match -->
    </article>
</ul>
```

**When to Use Child Combinator**

Use the child combinator when:
- You want to style only direct children, not all descendants
- You're working with nested structures and need fine control
- You want to avoid affecting nested versions of the same element

```css
/* Only direct paragraph children of article, not in nested sections */
article > p {
    font-size: 1.1em;
    line-height: 1.8;
}

/* Only direct item children, not in nested lists */
.menu > .menu-item {
    padding: 0.5em 1em;
}

/* Only direct images in gallery, not in nested galleries */
.gallery > img {
    border: 1px solid gray;
}
```

**Why Descendant vs Child Matters**

```css
/* Descendant - affects all ul lists inside article */
article ul {
    list-style: none;
}

/* Child - affects only direct ul children of article */
article > ul {
    list-style: none;
}
```

In a structure like:
```html
<article>
    <ul><!-- Affected by both -->
        <li>Item 1</li>
    </ul>
    <section>
        <ul><!-- Only affected by descendant selector, not child selector -->
            <li>Item 2</li>
        </ul>
    </section>
</article>
```

With child selector, nested lists aren't affected.
            """,
            
            "sibling_combinators": """
**Adjacent Sibling Combinator (+)**

The adjacent sibling combinator targets the immediately following sibling:

```css
/* Paragraphs that immediately follow headings */
h2 + p {
    font-weight: bold;
}

/* Items that follow the first item */
li:first-child + li {
    border-top: 1px solid gray;
}

/* Any element that follows an image */
img + * {
    margin-top: 1em;
}
```

HTML examples matching `h2 + p`:
```html
<!-- Matches - p immediately follows h2 -->
<h2>Title</h2>
<p>This matches</p>

<!-- Does NOT match - other element between h2 and p -->
<h2>Title</h2>
<hr>
<p>This doesn't match</p>

<!-- Does NOT match - p is not a sibling of h2 -->
<div>
    <h2>Title</h2>
</div>
<p>This doesn't match</p>
```

**General Sibling Combinator (~)**

The general sibling combinator targets all following siblings (not just the first):

```css
/* All paragraphs that follow headings */
h2 ~ p {
    color: gray;
}

/* All items after the first item */
li:first-child ~ li {
    border-top: 1px solid gray;
}

/* All content that follows article opening */
article .intro ~ * {
    margin: 1em 0;
}
```

HTML examples matching `h2 ~ p`:
```html
<!-- Both p elements match -->
<h2>Title</h2>
<p>First paragraph - matches</p>
<span>Some text</span>
<p>Second paragraph - also matches</p>

<!-- Doesn't match - p before h2 -->
<p>Before heading - doesn't match</p>
<h2>Title</h2>
<p>After heading - matches</p>
```

**Practical Examples**

Styling lists with separators:
```css
li + li {
    border-top: 1px solid #eee;
    margin-top: 1em;
    padding-top: 1em;
}
```

Spacing after headings:
```css
h2 + p {
    margin-top: 0; /* Remove default margin */
}

h2 ~ p {
    margin: 1em 0; /* Standard margin for all paragraphs after heading */
}
```

Form validation feedback:
```css
/* Error message that follows invalid input */
input:invalid + .error-message {
    color: red;
    display: block;
}

/* Success message that follows valid input */
input:valid + .success-message {
    color: green;
    display: block;
}
```
            """,
            
            "practical_combinators": """
**Real-World Examples**

**Navigation Menu**

HTML:
```html
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <div class="dropdown">
        <a href="/services">Services</a>
        <ul>
            <li><a href="/design">Design</a></li>
            <li><a href="/development">Development</a></li>
        </ul>
    </div>
</nav>
```

CSS:
```css
/* Only direct links in nav, not links in dropdowns */
nav > a {
    padding: 1em;
    color: white;
    text-decoration: none;
}

/* Items in dropdown menus */
.dropdown ul li a {
    display: block;
    padding: 0.5em 1em;
    color: #333;
}

/* Add separator between nav items */
nav > a + a {
    border-left: 1px solid rgba(255, 255, 255, 0.2);
}
```

**Article with Sidebar**

HTML:
```html
<article>
    <h1>Article Title</h1>
    <p>Opening paragraph</p>
    <section class="content">
        <p>Content paragraph</p>
        <p>More content</p>
    </section>
    <aside>Related articles</aside>
</article>
```

CSS:
```css
/* Opening paragraph special styling */
article h1 + p {
    font-weight: bold;
    font-size: 1.1em;
}

/* Content paragraphs */
article .content p {
    line-height: 1.8;
    margin-bottom: 1em;
}

/* All paragraphs after content section */
article .content ~ aside {
    background-color: #f5f5f5;
    padding: 1em;
}
```

**Form Organization**

HTML:
```html
<form>
    <input type="text" name="email" placeholder="Email">
    <input type="password" name="password" placeholder="Password">
    <label>
        <input type="checkbox" name="remember"> Remember me
    </label>
    <button type="submit">Login</button>
</form>
```

CSS:
```css
/* Space between input fields */
form input + input {
    margin-top: 1em;
}

/* Label after checkbox input */
input[type="checkbox"] + label {
    margin-left: 0.5em;
}

/* Button after all inputs */
form input ~ button,
form label ~ button {
    margin-top: 1.5em;
    width: 100%;
}
```

**Combining Multiple Combinators**

```css
/* Paragraphs inside articles that follow headings */
article h2 + p {
    font-weight: bold;
}

/* All paragraphs after the first one in article sections */
article > section > p:first-of-type + p {
    margin-top: 1em;
}

/* List items after active item */
.nav li.active + li {
    border-left: 2px solid gold;
}
```

**Avoiding Over-Specificity**

While you CAN write long combinator chains, sometimes simpler is better:

```css
/* Works but brittle - depends on exact structure */
div.container > section.main > article > p {
    color: blue;
}

/* Better - use classes for styling */
.article-text {
    color: blue;
}
```

Use combinators to reduce classes needed, but don't create dependency on perfect HTML structure.
            """,
        },
        
        "key_takeaways": [
            "Combinators describe relationships between selectors",
            "Space (descendant combinator) targets descendants at any level",
            "> (child combinator) targets only direct children",
            "+ (adjacent sibling) targets the immediately following sibling",
            "~ (general sibling) targets all following siblings",
            "Combinators help you style elements based on context",
            "They reduce the need for extra classes in HTML",
            "Child combinator is more specific than descendant combinator",
            "Sibling combinators are useful for context-dependent styling",
            "Avoid overly complex combinator chains - keep selectors readable"
        ]
    }
}
