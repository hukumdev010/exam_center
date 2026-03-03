"""
HTML Document Structure - Detailed Content

This file contains comprehensive content for the "HTML Document Structure" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "HTML Document Structure",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    Understanding the standard HTML document structure is fundamental to web development. This topic covers
    the essential elements that make up a valid HTML document and their roles.
    """,
    
    "detailed_content": {
        "introduction": """
Every HTML document follows a specific structure. While browsers are forgiving and will render pages that
don't follow this structure perfectly, understanding the correct structure is essential for writing
professional, accessible, and maintainable code.

The HTML document structure includes the DOCTYPE declaration, html, head, and body elements, each serving
a specific purpose in how the page is rendered and interpreted by browsers.
        """,
        
        "key_concepts": {
            "doctype_declaration": """
**DOCTYPE Declaration**

The DOCTYPE (Document Type Declaration) must be the very first line of an HTML document:

```html
<!DOCTYPE html>
```

This tells the browser that you're using HTML5. It's not actually an HTML tag - it's an instruction to
the browser. Without it, some browsers may render your page in "quirks mode," where they emulate older
browser behavior for compatibility with legacy websites.

For HTML5, the DOCTYPE is simple and standardized. In older versions of HTML, it was much more verbose.
        """,
            
            "html_root_element": """
**The <html> Root Element**

The `<html>` element wraps all content in your document and represents the root of the HTML document:

```html
<!DOCTYPE html>
<html lang="en">
    <!-- All other content goes here -->
</html>
```

The `lang` attribute specifies the language of the document. This helps browsers, search engines, and
screen readers understand what language the content is in.
        """,
            
            "head_section": """
**The <head> Element**

The `<head>` section contains metadata and information about the page that isn't directly visible to users:

```html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js"></script>
</head>
```

Important head elements include:
- `<meta charset="UTF-8">`: Specifies the character encoding
- `<meta name="viewport">`: Controls how the page scales on different devices
- `<title>`: The page title shown in the browser tab
- `<link>`: Links to external resources like stylesheets
- `<script>`: Links to or embeds JavaScript code
- `<style>`: Inline CSS rules
- `<meta>`: Various metadata about the page
        """,
            
            "body_section": """
**The <body> Element**

The `<body>` element contains all the content that's visible to users:

```html
<body>
    <h1>Welcome to my website</h1>
    <p>This is the visible content.</p>
</body>
```

All interactive elements, text, images, and other content users see goes in the body.
        """,
            
            "complete_document_example": """
**Complete HTML Document Structure**

Here's a complete, properly structured HTML5 document:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
        </nav>
    </header>
    
    <main>
        <article>
            <h2>Article Title</h2>
            <p>Article content goes here.</p>
        </article>
    </main>
    
    <footer>
        <p>&copy; 2024 My Website. All rights reserved.</p>
    </footer>
</body>
</html>
```

This structure ensures your page is properly formatted, accessible, and optimized for both humans and machines.
        """,
        }
    }
}
