"""
Web Standards and W3C - Detailed Content

This file contains content for the "Web Standards and W3C" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Web Standards and W3C",
    "duration": "8-10 minutes",
    "difficulty": "Beginner",
    "overview": """
    Web standards are agreements on how web technologies should work. The W3C (World Wide Web Consortium)
    maintains these standards. Understanding web standards helps you write better, more compatible code.
    """,
    
    "detailed_content": {
        "introduction": """
The web could have been chaotic. Each browser company could implement HTML, CSS, and JavaScript differently.
Instead, there are standards—agreements on how these technologies should work. This is crucial because it means
your code should work the same way across all browsers.

The W3C (World Wide Web Consortium) is an international community that develops these standards. It's led by
Tim Berners-Lee, who invented the web. Without standards, the web wouldn't be the universal platform it is today.
        """,
        
        "key_concepts": {
            "what_are_standards": """
**Why Standards Matter**

Before standards, each browser did things differently:
- HTML parsed differently
- CSS applied differently
- JavaScript behaved differently
- Nothing worked consistently across browsers

With standards, developers write code once and it works everywhere. This is why the web scales to billions of users.

**Major Standard Bodies**

**W3C (World Wide Web Consortium)**: 
- Maintains HTML, CSS, and web API standards
- Works on accessibility, security, performance

**WHATWG (Web Hypertext Application Technology Working Group)**:
- Maintains living standards for HTML and DOM
- More agile than W3C, evolves continuously

**ECMA International**:
- Maintains JavaScript standard (ECMAScript/ES)
- Defines JavaScript specifications

**IETF (Internet Engineering Task Force)**:
- Maintains HTTP, HTTPS, and other protocols
            """,
            
            "standard_examples": """
**HTML Standard**

Defines how browsers should parse and display HTML:
- Valid element names and attributes
- How to handle errors (missing closing tags, etc.)
- What doctype means
- How forms should work
- How images should be loaded

Example: What does `<div>` mean? The standard defines it.

**CSS Standard**

Defines how styling should work:
- Valid properties and values
- How specificity works
- How cascade works
- Box model
- Flexbox and Grid layout

Example: How does `margin: 0 auto;` center elements? The standard defines it.

**JavaScript Standard (ECMAScript)**

Defines JavaScript syntax and behavior:
- How variables work
- Functions and scope
- Objects and prototypes
- Promises and async/await
- New features each year

Example: How does `const` work? The standard defines it.

**Web APIs Standard**

Defines browser APIs:
- DOM (Document Object Model)
- Fetch API
- LocalStorage
- Canvas
- WebGL

Example: How does `document.querySelector()` work? The standard defines it.
            """,
            
            "conformance_levels": """
**Semantic HTML**

Writing HTML that matches the standard:

```html
<!-- Non-semantic -->
<div class="header">
  <div class="nav">
    <div>Home</div>
    <div>About</div>
  </div>
</div>

<!-- Semantic (standards-compliant) -->
<header>
  <nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
  </nav>
</header>
```

Semantic HTML is better for accessibility, SEO, and code clarity.

**Valid CSS**

CSS that matches the standard:

```css
/* Invalid - typo */
color: red;;      /* Double semicolon */
marign: 10px;     /* Typo in property name */

/* Valid - follows standard */
color: red;
margin: 10px;
```

**Following Best Practices**

The standards suggest best practices:
- Use semantic HTML elements
- Separate content (HTML), styling (CSS), behavior (JavaScript)
- Make pages responsive
- Ensure accessibility
- Write valid code
            """,
            
            "browser_compatibility": """
**Different Browser Support**

Browsers don't always support all standards immediately:

- New standards take years to develop
- Browser companies gradually implement them
- Old browsers don't support new features
- Some features are partially supported

Example: CSS Grid was standardized in 2017. Some older browsers still don't support it.

**Progressive Enhancement**

Build with standards-compliant basics, then add enhancements:

1. Core functionality works for everyone
2. Modern browsers get enhanced experience
3. If JavaScript fails, basic site still works
4. If CSS feature unsupported, fallback styling works

Example:
```css
/* Fallback for old browsers */
.grid {
  display: flex;
}

/* Modern browsers */
@supports (display: grid) {
  .grid {
    display: grid;
  }
}
```

**Polyfills**

JavaScript code that adds support for unsupported features:

```javascript
// Fetch polyfill for older browsers
if (!window.fetch) {
  // Provide fetch functionality
}
```
            """,
            
            "staying_current": """
**Following Standards**

Resources for learning standards:

- **MDN Web Docs**: Best documentation for web standards
- **W3C Website**: Official standards (technical, dense)
- **WHATWG Specifications**: Living HTML standard
- **Can I Use**: Browser compatibility for features

**Standards Bodies Track**

- GitHub discussions and issues
- Mailing lists
- In-person meetings
- Community input

You can participate in shaping the web's future!

**Advocating for Standards**

As a developer:
- Report browser bugs
- Request features
- Test new features
- Provide feedback

Your voice matters in shaping web standards.
            """
        }
    },
    
    "key_takeaways": [
        "W3C and WHATWG maintain web standards",
        "Standards ensure code works across browsers",
        "HTML, CSS, and JavaScript all have standards",
        "Semantic HTML follows best practices",
        "Progressive enhancement works with varying browser support",
        "MDN Web Docs is the best resource for standards",
        "Following standards makes better, more compatible code"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Check a website with W3C HTML validator",
            "Look up CSS property on MDN and read the standard",
            "Check browser support for a feature on Can I Use",
            "Write semantic HTML markup",
            "Use progressive enhancement in your code"
        ]
    },
    
    "related_topics": [
        "Browser Compatibility",
        "HTML Fundamentals",
        "CSS Best Practices"
    ]
}
