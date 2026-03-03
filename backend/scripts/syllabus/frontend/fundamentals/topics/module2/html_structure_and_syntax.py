"""
HTML Structure and Syntax - Detailed Content

This file contains comprehensive content for the "HTML Structure and Syntax" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "HTML Structure and Syntax",
    "duration": "60-75 minutes",
    "difficulty": "Beginner",
    "overview": """
    HTML (HyperText Markup Language) is the foundation of web development. This topic covers
    the fundamental syntax, document structure, and best practices for writing clean, semantic HTML.
    """,
    
    "detailed_content": {
        "introduction": """
HTML is not a programming language—it's a markup language. "Markup" means you're marking up content to describe
its structure and meaning. This distinction is important: while JavaScript tells the browser to *do* things,
HTML tells the browser *what things are*.

Every web page you've ever visited, from the simplest blog to complex applications like Gmail or Figma,
is built on HTML. It's the skeleton that gives a web page its structure and semantic meaning.

HTML is also remarkably stable and forgiving. Browsers are incredibly good at guessing what you meant even
if your HTML isn't perfectly formatted. However, writing valid, semantic HTML is important for:
- **Accessibility**: Screen readers and assistive technologies rely on proper HTML structure
- **SEO**: Search engines use HTML semantics to understand your content
- **Maintainability**: Well-structured code is easier for others (and future you) to understand
- **Performance**: Valid HTML renders more efficiently
- **Future-proofing**: Your HTML will work longer without modification
        """,
        
        "key_concepts": {
            "html_basics": """
**What is HTML?**

HTML stands for HyperText Markup Language:
- **HyperText**: Text with links (the "hyper" part is about connections between documents)
- **Markup**: Using special tags to annotate or "mark up" content
- **Language**: A standardized system for communicating structure

HTML uses a system of **tags** enclosed in angle brackets to describe content:

```html
<tag>content</tag>
```

Tags are the fundamental building blocks of HTML. They tell the browser what kind of content they contain.

**Elements vs Tags**

An **element** consists of:
- Opening tag: `<tagname>`
- Content
- Closing tag: `</tagname>`

For example:
```html
<p>This is a paragraph element.</p>
```

Some elements are **self-closing** or **void elements** and don't need a closing tag:
```html
<img src="image.jpg" alt="description">
<br>
<input type="text">
```

**Attributes**

Tags can have **attributes** that provide additional information:

```html
<img src="photo.jpg" alt="A beautiful sunset">
<a href="https://example.com" target="_blank">Click here</a>
```

In the first example:
- `src` is an attribute that specifies the image path
- `alt` is an attribute that describes the image for accessibility

In the second example:
- `href` specifies the link destination
- `target="_blank"` makes the link open in a new tab

Attributes always go in the opening tag and follow the format: `attribute="value"`

**Case Sensitivity**

HTML is case-insensitive. These are all valid:
```html
<p>Paragraph</p>
<P>Paragraph</P>
<P>Paragraph</p>
```

However, **lowercase is the standard and recommended practice**. Using lowercase makes your code:
- Consistent with modern conventions
- Easier to read
- Compatible with XHTML if needed
            """,
            
            "document_structure": """
**The Complete HTML Document**

While browsers are forgiving and will display content even without proper structure, a complete HTML document
should follow this structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
</head>
<body>
    <h1>Main Heading</h1>
    <p>Page content goes here.</p>
</body>
</html>
```

Let's break down each part:

**DOCTYPE Declaration**
```html
<!DOCTYPE html>
```
This tells the browser this is an HTML5 document. It must be the very first line. The `!DOCTYPE` declaration
is not an HTML tag—it's a special instruction for the browser.

**The `<html>` Element**
```html
<html lang="en">
```
This is the root element that wraps all other content. The `lang` attribute declares the document's language,
which helps:
- Screen readers pronounce content correctly
- Search engines understand the language
- Browsers can apply language-specific styling

**The `<head>` Section**
The head contains metadata about the document—information that isn't directly displayed but is important:

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <meta name="description" content="Page description">
    <link rel="stylesheet" href="styles.css">
    <script src="script.js"></script>
</head>
```

- `<meta charset="UTF-8">`: Specifies character encoding. Always use UTF-8.
- `<meta name="viewport" ...>`: Essential for responsive design. Tells the browser how to scale the page.
- `<title>`: The page title that appears in the browser tab and search results.
- `<meta name="description" ...>`: Summary that appears in search results.
- `<link>`: Links to external resources like stylesheets.
- `<script>`: Links to JavaScript files or contains inline scripts.

**The `<body>` Element**
```html
<body>
    <!-- All visible content goes here -->
</body>
```
Everything users see and interact with goes in the body.

**Comments**
Comments are notes in the code that browsers ignore:
```html
<!-- This is a comment -->
<!-- 
    Multi-line comments are useful for longer explanations
    and for temporarily disabling code
-->
```
            """,
            
            "semantic_elements": """
**Semantic HTML**

Semantic HTML means using elements that clearly describe the meaning of their content. 

**Non-Semantic Elements** (don't convey meaning):
```html
<div>
<span>
```
These are generic containers. There's nothing wrong with them, but they don't communicate what kind of
content they contain.

**Semantic Elements** (clearly describe their content):
```html
<article>, <section>, <nav>, <header>, <footer>, <main>, <aside>
<h1>, <h2>, <h3>, etc. (headings)
<p> (paragraph)
<ul>, <ol>, <li> (lists)
<button> (button)
<form> (form)
```

**Example Comparison**

Non-semantic:
```html
<div>
    <div>My Blog</div>
    <div>
        <div><a href="/">Home</a></div>
        <div><a href="/about">About</a></div>
    </div>
</div>
```

Semantic:
```html
<header>
    <h1>My Blog</h1>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
    </nav>
</header>
```

Both render the same visually, but the semantic version:
- Clearly communicates the purpose of each section
- Is accessible to screen readers
- Is better for SEO
- Is easier for developers to maintain

**Common Semantic Elements**

```html
<header>  <!-- Top section of page or section, typically with logo and nav -->
<nav>     <!-- Navigation links -->
<main>    <!-- Main content area (one per page) -->
<article> <!-- Self-contained content (blog post, news story, etc.) -->
<section> <!-- Generic thematic grouping of content -->
<aside>   <!-- Side content (sidebar, related links, etc.) -->
<footer>  <!-- Bottom section, typically with copyright, links, etc. -->
```

A typical semantic layout:
```html
<header>
    <h1>Site Title</h1>
    <nav><!-- Navigation --></nav>
</header>

<main>
    <article>
        <h2>Article Title</h2>
        <p>Content...</p>
    </article>
    
    <section>
        <h3>Related Content</h3>
        <!-- More content -->
    </section>
</main>

<footer>
    <p>&copy; 2024 My Site</p>
</footer>
```
            """,
            
            "practical_example": """
**Building Your First HTML Page**

Here's a complete, semantic HTML page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to My Blog</title>
    <meta name="description" content="A blog about web development">
</head>
<body>
    <header>
        <h1>My Web Development Blog</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/articles">Articles</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>

    <main>
        <article>
            <h2>Getting Started with HTML</h2>
            <p>Published on January 1, 2024</p>
            
            <p>HTML is the foundation of all web pages. In this article, we'll explore
            the basics of HTML syntax and structure.</p>
            
            <h3>Key Concepts</h3>
            <ul>
                <li>HTML uses tags to markup content</li>
                <li>Tags are enclosed in angle brackets</li>
                <li>Most tags have an opening and closing tag</li>
                <li>Semantic HTML improves accessibility</li>
            </ul>
        </article>

        <aside>
            <h3>Related Articles</h3>
            <ul>
                <li><a href="/css-basics">CSS Basics</a></li>
                <li><a href="/js-intro">JavaScript Introduction</a></li>
            </ul>
        </aside>
    </main>

    <footer>
        <p>&copy; 2024 My Blog. All rights reserved.</p>
    </footer>
</body>
</html>
```

**Key Takeaways**:
1. Start every HTML document with `<!DOCTYPE html>`
2. Use semantic elements to clearly describe your content
3. Include important metadata in the `<head>`
4. Make sure your HTML is well-nested and properly formatted
5. Use meaningful element names—avoid unnecessary `<div>` wrappers
            """,
            
            "best_practices": """
**HTML Best Practices**

1. **Validate Your HTML**: Use the W3C HTML Validator to catch errors:
   https://validator.w3.org/

2. **Use Semantic Elements**: Choose the right element for the job, not just any element that "looks right".

3. **Proper Nesting**: Elements must be properly nested:
   ```html
   <!-- Correct -->
   <p>This is <strong>bold</strong> text.</p>
   
   <!-- Wrong -->
   <p>This is <strong>bold text.</p></strong>
   ```

4. **Consistent Indentation**: Makes code readable:
   ```html
   <div>
       <p>Content</p>
   </div>
   ```

5. **Alt Text for Images**: Always include descriptive alt text:
   ```html
   <img src="sunset.jpg" alt="A golden sunset over mountains">
   ```

6. **Meaningful IDs and Classes**: Use descriptive names:
   ```html
   <!-- Good -->
   <nav id="main-navigation"></nav>
   <section class="featured-articles"></section>
   
   <!-- Poor -->
   <nav id="nav1"></nav>
   <section class="section1"></section>
   ```

7. **Single Responsibility**: Each element should have one purpose:
   ```html
   <!-- Use semantic elements -->
   <header><!-- Top of page --></header>
   <main><!-- Main content --></main>
   <footer><!-- Bottom of page --></footer>
   ```

8. **Mobile-First Meta Viewport**: Always include the viewport meta tag:
   ```html
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   ```

9. **Use Lowercase**: While HTML is case-insensitive, lowercase is the standard:
   ```html
   <!-- Standard -->
   <button>Click Me</button>
   
   <!-- Non-standard (avoid) -->
   <BUTTON>Click Me</BUTTON>
   ```

10. **Keep It Simple**: Don't add unnecessary elements or attributes.
            """
        }
    }
}
