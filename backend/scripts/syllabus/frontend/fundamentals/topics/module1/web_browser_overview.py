"""
Web Browser Overview - Detailed Content

This file contains content for the "Web Browser Overview" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Web Browser Overview",
    "duration": "10-15 minutes",
    "difficulty": "Beginner",
    "overview": """
    Web browsers are the most important tool in web development. Understanding how browsers work—how they parse HTML,
    apply CSS, execute JavaScript, and render pages—is fundamental to becoming a great frontend developer.
    """,
    
    "detailed_content": {
        "introduction": """
A web browser is software that retrieves and displays web pages. Most people think of browsers as simple tools for
viewing websites, but they're actually incredibly complex programs that do much more:

- Fetch resources from the internet
- Parse and interpret code (HTML, CSS, JavaScript)
- Execute complex algorithms and logic
- Manage user input and events
- Maintain security and privacy
- Optimize performance
- Render beautiful visual designs

As a frontend developer, the browser is your primary platform. Your code runs inside a browser, and understanding how
the browser works is essential to writing good frontend code.
        """,
        
        "key_concepts": {
            "popular_browsers": """
**Major Browsers**

The most widely used browsers are:

**Chrome** (Google): The most popular browser with about 65% market share. Fast, developer-friendly, with excellent
DevTools. Chromium-based.

**Firefox** (Mozilla): About 10% market share. Known for privacy focus and excellent developer tools. Open-source
and independent engine (Gecko).

**Safari** (Apple): About 20% market share, especially on iOS and macOS. WebKit engine. Important for testing because
it has different behavior than Chrome.

**Edge** (Microsoft): Growing adoption, especially in enterprise. Based on Chromium, so similar to Chrome.

**Other Browsers**: Opera, Brave, Arc, and many others. Most modern browsers use Chromium or WebKit under the hood.

**Why It Matters**: Web developers need to test their applications on multiple browsers because they render and behave
differently. A button might look perfect in Chrome but broken in Safari.
            """,
            
            "how_browsers_work": """
**The Rendering Process**

When you visit a website, the browser goes through several steps:

1. **DNS Lookup**: Browser resolves the domain name (example.com) to an IP address
2. **HTTP Request**: Browser sends an HTTP request to the server
3. **Receive HTML**: Server sends back the HTML file
4. **Parse HTML**: Browser reads the HTML and builds a tree structure (DOM)
5. **Request Resources**: Browser identifies CSS, JavaScript, and image files referenced in HTML and requests them
6. **Parse CSS**: Browser applies CSS styles to elements
7. **Execute JavaScript**: Browser runs JavaScript code, which can modify the DOM and apply styles
8. **Render**: Browser calculates the layout of all elements on the page
9. **Paint**: Browser draws pixels to the screen
10. **Display**: User sees the rendered page

This process is called the "critical rendering path." Understanding it helps you optimize performance.

**Example**:
```html
<html>
  <head>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <h1>Hello World</h1>
    <script src="app.js"></script>
  </body>
</html>
```

Browser executes:
1. Parse `<html>` and `<head>` tags
2. See `<link>` to CSS file, request it
3. Parse `<body>`
4. See `<h1>` and add it to DOM
5. See `<script>` tag, request JavaScript file
6. When JS arrives, execute it
7. JS might modify the DOM
8. Render the final page
            """,
            
            "key_features": """
**DOM (Document Object Model)**

The DOM is a tree representation of the HTML document. When the browser parses HTML, it builds the DOM:

```
html
├── head
│   ├── title
│   └── link (CSS)
└── body
    ├── h1 (Hello World)
    ├── p (Some text)
    └── button (Click me)
```

JavaScript can query and modify the DOM, which updates what the user sees. This is a core part of interactivity.

**Event Handling**

Browsers detect user interactions (clicks, typing, scrolling) and trigger events. JavaScript can listen for these
events and respond:
```javascript
button.addEventListener('click', () => {
  console.log('Button clicked!');
});
```

**CSS Cascade and Specificity**

The browser applies CSS rules in order, with later rules overriding earlier ones. Understanding cascade and specificity
is crucial for styling.

**JavaScript Runtime**

The browser includes a JavaScript engine that executes your code. Modern engines are incredibly fast and sophisticated,
with features like:
- Just-In-Time (JIT) compilation
- Garbage collection
- Async/await support
- Module system (import/export)

**Local Storage and Cookies**

Browsers can store data locally:
- **Cookies**: Small text files sent with HTTP requests
- **LocalStorage**: Key-value storage persisting across sessions
- **SessionStorage**: Temporary storage for current session
- **IndexedDB**: Full database in the browser

**Console and DevTools**

The browser's developer tools let you:
- Inspect HTML elements
- Debug JavaScript
- Check network requests
- Monitor performance
- Analyze memory usage

These tools are essential for frontend development.
            """,
            
            "browser_security": """
**Sandbox Model**

Browsers run JavaScript in a sandbox—an isolated environment with limited access:

✓ Can: Access DOM, LocalStorage, make network requests, manipulate styles
✗ Cannot: Access your file system, read other websites' cookies, directly access hardware

This protects your privacy and security.

**Same-Origin Policy**

Browsers prevent JavaScript from one website accessing another website's data. This protects against many attacks.

**HTTPS and Security**

Secure websites use HTTPS, which encrypts communication between browser and server. Browsers show a lock icon for
secure sites and warn you about insecure ones.

**Content Security Policy**

Website developers can set rules about what resources the browser can load, protecting against injection attacks.
            """,
            
            "browser_differences": """
**Why Browsers Differ**

Even though browsers follow web standards, they:
- Implement new features at different times
- Have different performance characteristics
- Sometimes interpret standards differently
- Support different new technologies

This is why testing across browsers is important.

**Example Differences**:
- CSS Grid works on Chrome, Firefox, Edge, Safari but with slightly different rendering
- Some CSS features only work in Safari
- JavaScript performance varies between browsers
- Mobile browsers have different behavior than desktop browsers

This inconsistency is why developers often use "autoprefixer" tools and conduct cross-browser testing.
            """
        }
    },
    
    "key_takeaways": [
        "Browsers parse HTML, apply CSS, and execute JavaScript",
        "The DOM is a tree representation of your HTML",
        "Browsers run JavaScript in a sandbox for security",
        "DevTools are essential development tools",
        "Different browsers render pages differently",
        "Understanding the rendering process helps optimize performance",
        "Browsers implement web standards but with some differences"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Open DevTools (F12 or right-click > Inspect)",
            "Go to the Elements/Inspector tab and inspect different elements",
            "Look at the Console tab and try executing JavaScript",
            "Check the Network tab and watch requests as you load a page",
            "Try editing CSS in DevTools and see changes in real-time",
            "Use the Performance tab to measure page load speed"
        ],
        "discussion_questions": [
            "Why is cross-browser testing important?",
            "What would happen if JavaScript executed outside the browser sandbox?",
            "How does the rendering process affect page load performance?",
            "Why do developers use DevTools?"
        ]
    },
    
    "related_topics": [
        "Developer Tools and DevTools",
        "JavaScript Basics",
        "HTML Fundamentals",
        "CSS Styling"
    ]
}
