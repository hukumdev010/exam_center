"""
Semantic HTML Elements - Detailed Content

This file contains comprehensive content for the "Semantic HTML Elements" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Semantic HTML Elements",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    Semantic HTML elements provide meaning to web content. Learn how to use semantic elements
    for better accessibility, SEO, and code maintainability. This topic covers the most important
    semantic elements and when to use them.
    """,
    
    "detailed_content": {
        "introduction": """
In HTML, "semantic" means using elements that clearly describe their meaning and purpose to both
browsers and developers. When you use semantic HTML, you're not just creating elements that look
a certain way—you're communicating what kind of content is in those elements.

Semantic HTML is one of the most important practices in web development for several reasons:

1. **Accessibility**: Screen readers and assistive technologies rely on semantic HTML to understand
   the structure and purpose of content. A blind user benefits greatly when a site is built with proper
   semantic structure.

2. **SEO**: Search engines use semantic HTML to better understand your content. Proper heading hierarchy,
   article elements, and other semantic markers help search engines rank your content appropriately.

3. **Maintainability**: Code with clear semantic structure is easier for developers to understand and modify.

4. **Responsive Design**: Semantic elements interact better with CSS and JavaScript frameworks.

5. **Future-Proofing**: Standards-compliant semantic HTML is more likely to work correctly with future
   browser versions and technologies.

The great news is that using semantic HTML doesn't require learning complicated syntax. It's mostly about
choosing the right element from the options available.
        """,
        
        "key_concepts": {
            "document_structure_elements": """
**Organizing Page Structure**

These elements define the major sections of your page:

**`<header>`**
The header section typically contains:
- Site logo or branding
- Site title or tagline
- Navigation menu
- Search bar
- Language selector

```html
<header>
    <img src="logo.svg" alt="Company Logo">
    <h1>My Website</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>
</header>
```

A page can have multiple headers—for example, one at the top of the page and another at the top of
an `<article>` element. However, there should typically be only one main site header.

**`<nav>`**
Represents navigation links. Should only wrap major navigation sections:

```html
<!-- Main site navigation -->
<nav>
    <a href="/">Home</a>
    <a href="/products">Products</a>
    <a href="/about">About</a>
</nav>

<!-- Footer navigation (also valid) -->
<footer>
    <nav>
        <a href="/privacy">Privacy</a>
        <a href="/terms">Terms</a>
    </nav>
</footer>
```

**Note**: Not every link needs to be wrapped in `<nav>`. Use `<nav>` for major navigation menus.
A link in an article footer or a "Skip to content" link doesn't need `<nav>`.

**`<main>`**
Contains the main content of the page. There should be only one `<main>` element per page.

```html
<body>
    <header><!-- Navigation --></header>
    
    <main>
        <!-- Primary content -->
        <article>...</article>
    </main>
    
    <footer><!-- Footer --></footer>
</body>
```

Everything that isn't header, footer, or navigation goes in main.

**`<footer>`**
The footer typically contains:
- Copyright information
- Contact information
- Links to other pages
- Social media links
- Legal documents (privacy policy, terms of service)

```html
<footer>
    <p>&copy; 2024 My Company</p>
    <nav>
        <a href="/privacy">Privacy Policy</a>
        <a href="/terms">Terms of Service</a>
    </nav>
    <p>Contact: info@example.com</p>
</footer>
```

Like `<header>`, there can be multiple footers (e.g., one for each article), but typically one per page.

**`<aside>`**
Represents content tangentially related to the main content. Common uses:
- Sidebars
- Related articles
- Advertisements
- Pull quotes
- Callout boxes

```html
<main>
    <article>
        <h2>Main Article</h2>
        <p>Main content...</p>
    </article>
    
    <aside>
        <h3>Related Articles</h3>
        <ul>
            <li><a href="#">Related Article 1</a></li>
            <li><a href="#">Related Article 2</a></li>
        </ul>
    </aside>
</main>
```
            """,
            
            "content_grouping_elements": """
**Organizing Content Within Sections**

These elements structure the content within your pages:

**`<article>`**
Represents self-contained content that could be syndicated or distributed independently:
- Blog posts
- News articles
- Forum posts
- Product reviews
- Comments

Key characteristic: An article should be understandable on its own, without surrounding context.

```html
<article>
    <h2>How to Learn Web Development</h2>
    <p>Published by Jane Smith on January 15, 2024</p>
    
    <p>Web development is an exciting field that...</p>
    
    <h3>Getting Started</h3>
    <p>First, you'll need to learn HTML...</p>
</article>
```

Articles can be nested:
```html
<article>
    <h2>Discussion Thread</h2>
    
    <article>
        <p>First comment by User A...</p>
    </article>
    
    <article>
        <p>Reply by User B...</p>
    </article>
</article>
```

**`<section>`**
Groups related content. Use when you want to break content into thematic groupings:

```html
<article>
    <h1>Web Development Guide</h1>
    
    <section>
        <h2>Getting Started</h2>
        <p>Before you begin, you'll need...</p>
    </section>
    
    <section>
        <h2>HTML Basics</h2>
        <p>HTML is the foundation of all web pages...</p>
    </section>
    
    <section>
        <h2>CSS for Styling</h2>
        <p>CSS allows you to style your HTML...</p>
    </section>
</article>
```

**`<article>` vs `<section>`**

A common source of confusion. Here are the differences:

- `<article>`: Self-contained content. If you were to syndicate/republish just this element
  on another site, it would still make sense.
  
- `<section>`: A grouping of related content within a larger document. By itself, it doesn't
  necessarily have complete meaning.

Think of it this way: articles are typically the main content of a page, while sections organize
content within an article.

```html
<!-- Correct: Article contains sections -->
<article>
    <h1>Blog Post Title</h1>
    
    <section>
        <h2>Introduction</h2>
    </section>
    
    <section>
        <h2>Main Content</h2>
    </section>
    
    <section>
        <h2>Conclusion</h2>
    </section>
</article>

<!-- Also correct: Multiple articles, each standalone -->
<main>
    <article>
        <h2>First Blog Post</h2>
        <p>Content...</p>
    </article>
    
    <article>
        <h2>Second Blog Post</h2>
        <p>Content...</p>
    </article>
</main>
```
            """,
            
            "text_semantic_elements": """
**Semantic Meaning in Text**

These elements give semantic meaning to inline content:

**`<strong>` vs `<b>`**

`<strong>` indicates strong importance:
```html
<p>It is <strong>very important</strong> to wear a seatbelt.</p>
```

`<b>` indicates bold text without importance:
```html
<p>The book title is <b>The Great Gatsby</b>.</p>
```

Screen readers emphasize `<strong>`, but not `<b>`. Use `<strong>` for important content,
`<b>` when you just want text to be bold for styling reasons.

**`<em>` vs `<i>`**

`<em>` indicates emphasis:
```html
<p>This is a <em>really</em> important point.</p>
```

`<i>` indicates italics (often for foreign words, technical terms, or styling):
```html
<p>The word <i>déjà vu</i> is French.</p>
<p><i>The Great Gatsby</i> is my favorite book.</p>
```

Screen readers emphasize `<em>`, but treat `<i>` as normal text with italic styling.

**Other Text Elements**

```html
<mark>    Highlighted text (search results, important passages)
<small>   Fine print, disclaimers, copyright
<del>     Deleted or removed text (shows strikethrough)
<ins>     Inserted text (shows underline)
<sub>     Subscript (e.g., H₂O)
<sup>     Superscript (e.g., x²)
<code>    Inline code snippets
<kbd>     Keyboard input (Ctrl+S)
<var>     Variable or placeholder
```

Examples:
```html
<p>Search results for <mark>web development</mark></p>
<p>Price: <del>$50</del> <ins>$30</ins></p>
<p>The chemical formula is H<sub>2</sub>O</p>
<p>Einstein's famous equation: E=mc<sup>2</sup></p>
<p>Press <kbd>Ctrl+S</kbd> to save</p>
```
            """,
            
            "list_elements": """
**Different Types of Lists**

**Unordered Lists (`<ul>`)**
For lists where order doesn't matter:

```html
<ul>
    <li>Apples</li>
    <li>Bananas</li>
    <li>Oranges</li>
</ul>
```

Renders as:
- Apples
- Bananas
- Oranges

**Ordered Lists (`<ol>`)**
For lists where order matters:

```html
<ol>
    <li>Open the browser</li>
    <li>Go to the website</li>
    <li>Fill out the form</li>
    <li>Submit</li>
</ol>
```

Renders as:
1. Open the browser
2. Go to the website
3. Fill out the form
4. Submit

You can customize numbering:
```html
<!-- Start at a different number -->
<ol start="5">
    <li>Item five</li>
    <li>Item six</li>
</ol>

<!-- Reversed order -->
<ol reversed>
    <li>Last item</li>
    <li>Second to last</li>
</ol>

<!-- Roman numerals -->
<ol style="list-style-type: upper-roman;">
    <li>First</li>
    <li>Second</li>
</ol>
```

**Description Lists (`<dl>`)**
For terms and their descriptions:

```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
    
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
    
    <dt>JS</dt>
    <dd>JavaScript</dd>
</dl>
```

Each `<dt>` is a term, and each `<dd>` is its description.

**Nested Lists**
```html
<ul>
    <li>Frontend
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </li>
    <li>Backend
        <ul>
            <li>Python</li>
            <li>Node.js</li>
        </ul>
    </li>
</ul>
```
            """,
            
            "practical_example": """
**Complete Semantic Page Structure**

Here's a realistic example using many semantic elements:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Blog - Latest Web Development Insights</title>
</head>
<body>
    <header>
        <h1>Tech Blog</h1>
        <p>Expert insights on web development</p>
        <nav>
            <a href="/">Home</a>
            <a href="/posts">Posts</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <main>
        <article>
            <h2>Getting Started with React</h2>
            <p>By <strong>Sarah Developer</strong> on <time datetime="2024-01-20">January 20, 2024</time></p>
            
            <section>
                <h3>Introduction</h3>
                <p>React has become the most <em>popular</em> JavaScript library for building user interfaces.</p>
            </section>
            
            <section>
                <h3>Why Learn React?</h3>
                <ul>
                    <li>Component-based architecture</li>
                    <li>Reusable code</li>
                    <li>Strong community</li>
                </ul>
            </section>
            
            <section>
                <h3>Getting Started</h3>
                <p>To create a new React project, use:</p>
                <code>npx create-react-app my-app</code>
            </section>
        </article>

        <aside>
            <h3>Related Articles</h3>
            <ul>
                <li><a href="/javascript-basics">JavaScript Basics</a></li>
                <li><a href="/css-layout">CSS Layouts</a></li>
                <li><a href="/web-performance">Web Performance</a></li>
            </ul>
            
            <h3>About the Author</h3>
            <p><strong>Sarah Developer</strong> has been creating web applications for 8 years.</p>
        </aside>
    </main>

    <footer>
        <nav>
            <a href="/privacy">Privacy Policy</a>
            <a href="/terms">Terms of Service</a>
        </nav>
        <p>&copy; 2024 Tech Blog. All rights reserved.</p>
    </footer>
</body>
</html>
```

**Key Observations**:
1. Structure is clear: header, main (with article and aside), footer
2. Articles contain sections for logical grouping
3. Navigation is in `<nav>` elements
4. Text semantics (`<strong>`, `<em>`) are used appropriately
5. Lists organize related items
6. The whole page would make sense even with CSS disabled
            """
        }
    }
}
