"""
HTML Best Practices - Detailed Content

This file contains comprehensive content for the "HTML Best Practices" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "HTML Best Practices",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Writing clean, semantic, and maintainable HTML is fundamental to web development. This topic covers
    best practices, conventions, and guidelines for writing professional HTML code.
    """,
    
    "detailed_content": {
        "introduction": """
HTML best practices ensure your code is:
- Semantic: Meaning is clear to browsers, search engines, and assistive technologies
- Maintainable: Easy for other developers (and future you) to understand and modify
- Accessible: Usable by everyone, including people with disabilities
- Performant: Renders efficiently and loads quickly
- Compatible: Works across different browsers and devices
        """,
        
        "key_concepts": {
            "semantic_html": """
**Always Use Semantic HTML**

Semantic elements clearly describe their meaning to the browser and developers:

```html
<!-- Good - Semantic HTML -->
<article>
    <header>
        <h1>Article Title</h1>
        <time datetime="2024-12-11">December 11, 2024</time>
    </header>
    <p>Article introduction...</p>
    <section>
        <h2>Section Heading</h2>
        <p>Section content...</p>
    </section>
    <aside>Related reading list</aside>
    <footer>By John Doe</footer>
</article>

<!-- Bad - Using divs for everything -->
<div id="article">
    <div class="header">
        <div class="title">Article Title</div>
        <div class="date">December 11, 2024</div>
    </div>
    <div class="content">
        <div class="paragraph">Article introduction...</div>
        <div class="section">
            <div class="heading">Section Heading</div>
            <div class="paragraph">Section content...</div>
        </div>
    </div>
</div>
```

Semantic elements:
- `<article>`: Self-contained content
- `<section>`: Thematic grouping
- `<nav>`: Navigation links
- `<header>`: Introductory content
- `<footer>`: Closing content
- `<aside>`: Side content
- `<main>`: Main content (once per page)
- `<figure>`: Illustrations, diagrams
- `<figcaption>`: Caption for figure
        """,
            
            "document_structure": """
**Proper Document Structure**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Page description">
    
    <title>Page Title - Site Name</title>
    
    <link rel="icon" href="/favicon.ico">
    <link rel="stylesheet" href="/styles.css">
    <link rel="preload" href="/fonts/main.woff2" as="font">
</head>
<body>
    <skip-to-main-content>
        <a href="#main">Skip to main content</a>
    </skip-to-main-content>
    
    <header role="banner">
        <nav role="navigation">
            <!-- navigation -->
        </nav>
    </header>
    
    <main id="main" role="main">
        <!-- main content -->
    </main>
    
    <footer role="contentinfo">
        <!-- footer content -->
    </footer>
    
    <script src="/script.js" defer></script>
</body>
</html>
```

Structure rules:
- DOCTYPE at the very beginning
- lang attribute on html element
- Charset meta tag first in head
- Viewport meta tag for responsive design
- Descriptive title and meta description
- External stylesheets in head
- External scripts at end of body (or defer attribute)
        """,
            
            "naming_conventions": """
**HTML Naming Conventions**

```html
<!-- Use lowercase for tags and attributes -->
<div id="user-profile" class="card primary-action">
    <h2>User Profile</h2>
</div>

<!-- IDs and classes use kebab-case (hyphens) -->
<button id="submit-btn" class="btn btn-primary">Submit</button>

<!-- Data attributes use lowercase with hyphens -->
<article data-article-id="123" data-published-date="2024-12-11">

<!-- Avoid single-letter IDs and classes -->
<!-- Bad -->
<div id="x" class="a"></div>

<!-- Good -->
<div id="sidebar-menu" class="primary-navigation"></div>

<!-- Use semantic class names (describe content, not presentation) -->
<!-- Bad -->
<p class="red-text big-font">Error message</p>

<!-- Good -->
<p class="error-message">Error message</p>

<!-- Avoid presentational ID/class names -->
<!-- Bad -->
<div id="left-column" class="float-right"></div>

<!-- Good -->
<aside id="sidebar" class="related-content"></aside>
```

Naming guidelines:
- Use lowercase
- Use hyphens (kebab-case) for multi-word names
- Be descriptive
- Avoid single letters
- Describe meaning, not presentation
        """,
            
            "formatting_indentation": """
**Formatting and Indentation**

```html
<!-- Consistent indentation (2 or 4 spaces) -->
<div id="container">
  <header>
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>
  
  <main>
    <article>
      <h1>Article Title</h1>
      <p>Article content...</p>
    </article>
  </main>
</div>

<!-- Close tags on same line for small content -->
<p>Simple paragraph.</p>
<button>Click me</button>

<!-- New lines for complex content -->
<div id="complex">
  <h2>Complex Element</h2>
  <p>First paragraph with substantial content that explains something important.</p>
  <p>Second paragraph with more details.</p>
  <ul>
    <li>List item 1</li>
    <li>List item 2</li>
  </ul>
</div>

<!-- Always close tags -->
<!-- Bad: No closing tag -->
<p>Paragraph text

<!-- Good: Properly closed -->
<p>Paragraph text</p>

<!-- Use void element syntax correctly -->
<img src="image.jpg" alt="Description">
<br>
<hr>
<input type="text">
```

Indentation rules:
- Use consistent indentation (2 or 4 spaces)
- Indent nested elements
- Close all tags
- One element per line for clarity
- Add comments for complex sections
        """,
            
            "accessibility_practices": """
**Accessibility Best Practices**

```html
<!-- Always include alt text -->
<img src="chart.png" alt="Sales growth chart showing 25% increase over 2024">

<!-- Don't use alt attribute for decorative images -->
<img src="spacer.png" alt="">

<!-- Use label for all form inputs -->
<label for="email-field">Email address</label>
<input type="email" id="email-field" name="email" required>

<!-- Use semantic headings -->
<h1>Main Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>

<!-- Link text should be descriptive -->
<!-- Bad -->
<a href="/article">Click here</a>

<!-- Good -->
<a href="/article">Read the complete article about web accessibility</a>

<!-- Mark up lists properly -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- Use tables for tabular data only -->
<table>
  <thead>
    <tr>
      <th>Column 1</th>
      <th>Column 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
    </tr>
  </tbody>
</table>

<!-- Provide captions for media -->
<video src="video.mp4" controls>
  <track kind="captions" src="captions.vtt" srclang="en">
</video>

<!-- Use ARIA only when necessary -->
<button aria-label="Close menu">×</button>
```

Accessibility checklist:
- Semantic HTML structure
- Proper headings hierarchy
- Alt text for all images
- Descriptive link text
- Form labels for inputs
- Color not only indicator
- Keyboard accessible
- Sufficient contrast
        """,
            
            "performance_practices": """
**Performance Best Practices**

```html
<!-- Minimize HTTP requests by using modern formats -->
<!-- Use SVG for icons -->
<svg width="24" height="24">
  <!-- svg content -->
</svg>

<!-- Use WebP for images with fallback -->
<picture>
  <source srcset="image.webp" type="image/webp">
  <source srcset="image.jpg" type="image/jpeg">
  <img src="image.jpg" alt="Description">
</picture>

<!-- Lazy load images -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Preload critical resources -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>

<!-- Defer non-critical scripts -->
<script src="analytics.js" defer></script>

<!-- Async for completely independent scripts -->
<script src="external-widget.js" async></script>

<!-- Avoid inline styles (use CSS) -->
<!-- Bad -->
<div style="color: red; font-size: 16px;">Text</div>

<!-- Good -->
<div class="error-message">Text</div>

<!-- Minimize DOM elements -->
<!-- Bad - too many divs -->
<div><div><div>Content</div></div></div>

<!-- Good - minimal nesting -->
<div>Content</div>

<!-- Don't use event attributes -->
<!-- Bad -->
<button onclick="save()">Save</button>

<!-- Good -->
<button id="save-btn">Save</button>
<script>
  document.getElementById('save-btn').addEventListener('click', save);
</script>
```

Performance tips:
- Minimize DOM size
- Lazy load non-critical images
- Use modern image formats
- Preload critical resources
- Defer or async non-critical scripts
- Minimize inline CSS and JavaScript
- Use CSS for styling
- Use semantic HTML (lighter, renders faster)
        """,
            
            "common_mistakes": """
**Common Mistakes to Avoid**

❌ **Not using semantic HTML**
```html
<!-- Bad -->
<div class="header"><div class="title">Title</div></div>
<!-- Good -->
<header><h1>Title</h1></header>
```

❌ **Missing alt text on images**
```html
<!-- Bad -->
<img src="diagram.jpg">
<!-- Good -->
<img src="diagram.jpg" alt="System architecture diagram">
```

❌ **Improper heading hierarchy**
```html
<!-- Bad -->
<h1>Title</h1>
<h3>Subtitle</h3>
<!-- Good -->
<h1>Title</h1>
<h2>Subtitle</h2>
```

❌ **Divitis (too many divs)**
```html
<!-- Bad -->
<div id="container">
  <div class="wrapper">
    <div class="inner">
      <p>Content</p>
    </div>
  </div>
</div>

<!-- Good -->
<main>
  <p>Content</p>
</main>
```

❌ **Missing labels on forms**
```html
<!-- Bad -->
<input type="text" placeholder="Name">
<!-- Good -->
<label for="name">Name:</label>
<input type="text" id="name" name="name">
```

❌ **Inline styles**
```html
<!-- Bad -->
<p style="color: red; font-size: 18px;">Error</p>
<!-- Good -->
<p class="error">Error</p>
```

❌ **Not closing tags**
```html
<!-- Bad -->
<p>Paragraph
<p>Another paragraph

<!-- Good -->
<p>Paragraph</p>
<p>Another paragraph</p>
```
        """,
        }
    }
}
