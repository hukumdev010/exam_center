"""
Links and Navigation - Detailed Content

This file contains comprehensive content for the "Links and Navigation" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Links and Navigation",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    Links are the foundation of web navigation. Learn how to create accessible, semantic links,
    implement effective navigation structures, and build user-friendly menus and breadcrumbs.
    """,
    
    "detailed_content": {
        "introduction": """
Links (`<a>` elements) are what make the web a "web"—they connect documents and allow users
to navigate between pages. A seemingly simple element, the `<a>` tag is actually powerful and
has many nuances.

In this topic, we'll learn how to:
1. Create links that are accessible and semantic
2. Link to different types of resources
3. Implement various navigation patterns
4. Optimize links for SEO
5. Provide good user experience with link styling

Good link implementation is crucial for:
- **Navigation**: Allowing users to move through your site
- **SEO**: Search engines follow links to discover and rank pages
- **Accessibility**: Screen readers need to understand link purpose
- **User Experience**: Clear links help users know where they're going
        """,
        
        "key_concepts": {
            "basic_links": """
**The Anchor Element (`<a>`)**

The basic structure:

```html
<a href="https://example.com">Click here</a>
```

**Essential Attributes**

`href` (REQUIRED): Where the link goes
```html
<!-- Full URL (absolute) -->
<a href="https://example.com">External Site</a>

<!-- Relative path (same domain) -->
<a href="/about">About Page</a>
<a href="/blog/post-1">Blog Post</a>
<a href="../parent-page">Parent Directory</a>

<!-- File in same directory -->
<a href="contact.html">Contact Us</a>

<!-- Link to ID on same page (anchor) -->
<a href="#contact-section">Jump to Contact</a>

<!-- Email link -->
<a href="mailto:contact@example.com">Email Us</a>

<!-- Phone link -->
<a href="tel:+1-555-123-4567">Call Us</a>

<!-- Download file -->
<a href="/files/document.pdf">Download PDF</a>
```

**Common Attributes**

```html
<a 
    href="https://example.com"
    title="Visit Example.com"           <!-- Tooltip -->
    target="_blank"                     <!-- Open in new tab -->
    rel="noopener noreferrer"          <!-- Security for new tabs -->
    download="filename.pdf"             <!-- Trigger download -->
    id="main-link"                      <!-- CSS/JS reference -->
    class="button"                      <!-- CSS styling -->
    aria-label="Visit our homepage"    <!-- Accessible label -->
>
    Click here
</a>
```

**Important Attributes Explained**

`target="_blank"`: Opens in new tab/window
```html
<!-- Always use rel attribute for security -->
<a href="https://external-site.com" target="_blank" rel="noopener noreferrer">
    Visit external site
</a>
```

`rel`: Relationship between current and linked document
```html
<!-- Prevent passing referrer information -->
<a href="https://example.com" rel="noreferrer">

<!-- Indicate it's not a recommendation/endorsement -->
<a href="https://example.com" rel="nofollow">

<!-- Common combination for external links -->
<a href="https://external.com" target="_blank" rel="noopener noreferrer">

<!-- Next/previous in sequence -->
<a href="/article-2" rel="next">Next Article</a>
<a href="/article-1" rel="prev">Previous Article</a>

<!-- Indicate it's an external link -->
<a href="https://example.com" rel="external">
```

**Download Attribute**

```html
<!-- Trigger download with default name -->
<a href="/files/document.pdf" download>Download PDF</a>

<!-- Download with custom filename -->
<a href="/files/document.pdf" download="my-document.pdf">Download PDF</a>
```
            """,
            
            "link_text_best_practices": """
**Writing Good Link Text**

The text inside a link is crucial for:
- **Accessibility**: Screen reader users hear the link text
- **SEO**: Search engines use link text to understand pages
- **Usability**: Users scan for meaningful links

**Bad Link Text**
```html
<!-- Generic, meaningless -->
<a href="/about">Click here</a>
<a href="/blog">Read more</a>
<a href="/products">Link</a>

<!-- Unclear context -->
<a href="/terms">Terms</a>
<a href="/download">Download</a>
```

**Good Link Text**
```html
<!-- Descriptive, clear purpose -->
<a href="/about">Learn about our company</a>
<a href="/blog/getting-started">Getting Started with React</a>
<a href="/products/pricing">View our pricing plans</a>

<!-- Context provided -->
<a href="/terms">Read our terms of service</a>
<a href="/guide.pdf">Download the complete guide (PDF, 2.5 MB)</a>
```

**Link Text Guidelines**

1. **Be Descriptive**: Describe where the link goes, not "click here"
```html
<!-- Good -->
<p>Learn more about <a href="/products">our products</a>.</p>

<!-- Bad -->
<p><a href="/products">Click here</a> to see products.</p>
```

2. **Be Concise**: Keep it brief (3-5 words ideal)
```html
<!-- Good -->
<a href="/contact">Contact our sales team</a>

<!-- Too long -->
<a href="/contact">Contact our sales team to discuss pricing and product features</a>
```

3. **Use Unique Text**: Each link should have distinct text
```html
<!-- Bad: Multiple links with same text -->
<a href="/blog/post-1">Read more</a>
<a href="/blog/post-2">Read more</a>

<!-- Good: Descriptive unique text -->
<a href="/blog/post-1">Getting Started with React</a>
<a href="/blog/post-2">Advanced CSS Techniques</a>
```

4. **Provide Context for Accessibility**
```html
<!-- Good: Text is self-contained -->
<a href="/pdf/whitepaper.pdf">Download our React whitepaper</a>

<!-- Bad: Meaning depends on surrounding text -->
<p>Our latest research is available <a href="/pdf/whitepaper.pdf">here</a>.</p>

<!-- Better: Add aria-label for context -->
<p>Our latest research is available <a href="/pdf/whitepaper.pdf" aria-label="Download React whitepaper">here</a>.</p>
```
            """,
            
            "navigation_patterns": """
**Navigation Structures**

**Main Navigation (Header Menu)**

```html
<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/services">Services</a>
    <a href="/blog">Blog</a>
    <a href="/contact">Contact</a>
</nav>
```

Better with semantic list:
```html
<nav>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/services">Services</a></li>
        <li><a href="/blog">Blog</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
</nav>
```

**Breadcrumb Navigation**

Shows hierarchy of current page:

```html
<nav aria-label="Breadcrumb">
    <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/products">Products</a></li>
        <li><a href="/products/electronics">Electronics</a></li>
        <li aria-current="page">Laptops</li>
    </ol>
</nav>
```

CSS to display as breadcrumbs:
```css
nav ol {
    display: flex;
    list-style: none;
    padding: 0;
    margin: 0;
}

nav li::before {
    content: " / ";
    margin: 0 0.5rem;
}

nav li:first-child::before {
    content: "";
    margin: 0;
}
```

Renders as: Home / Products / Electronics / Laptops

**Pagination**

For pages with multiple results:

```html
<nav aria-label="Pagination">
    <ul>
        <li>
            <a href="/results?page=1" rel="prev">← Previous</a>
        </li>
        <li><a href="/results?page=1">1</a></li>
        <li><a href="/results?page=2">2</a></li>
        <li><a href="/results?page=3" aria-current="page">3</a></li>
        <li><a href="/results?page=4">4</a></li>
        <li><a href="/results?page=5">5</a></li>
        <li>
            <a href="/results?page=5" rel="next">Next →</a>
        </li>
    </ul>
</nav>
```

**Tabbed Navigation**

For switching between sections (usually with JavaScript):

```html
<nav role="tablist">
    <a href="#panel1" role="tab" aria-selected="true" aria-controls="panel1">
        Profile
    </a>
    <a href="#panel2" role="tab" aria-selected="false" aria-controls="panel2">
        Settings
    </a>
    <a href="#panel3" role="tab" aria-selected="false" aria-controls="panel3">
        Privacy
    </a>
</nav>

<div id="panel1" role="tabpanel" aria-labelledby="tab1">
    Profile content...
</div>
<div id="panel2" role="tabpanel" aria-labelledby="tab2" hidden>
    Settings content...
</div>
<div id="panel3" role="tabpanel" aria-labelledby="tab3" hidden>
    Privacy content...
</div>
```

**Footer Navigation**

```html
<footer>
    <nav>
        <h3>Company</h3>
        <ul>
            <li><a href="/about">About Us</a></li>
            <li><a href="/careers">Careers</a></li>
            <li><a href="/press">Press</a></li>
        </ul>
    </nav>
    
    <nav>
        <h3>Product</h3>
        <ul>
            <li><a href="/features">Features</a></li>
            <li><a href="/pricing">Pricing</a></li>
            <li><a href="/docs">Documentation</a></li>
        </ul>
    </nav>
    
    <nav>
        <h3>Legal</h3>
        <ul>
            <li><a href="/privacy">Privacy</a></li>
            <li><a href="/terms">Terms</a></li>
        </ul>
    </nav>
</footer>
```
            """,
            
            "anchors_and_skip_links": """
**Page Anchors (Jump Links)**

Link to specific sections on a page:

```html
<!-- Link to section -->
<a href="#contact-section">Jump to Contact</a>

<!-- The section it links to -->
<section id="contact-section">
    <h2>Contact Us</h2>
    <p>Contact information...</p>
</section>
```

**Using Anchors in Navigation**

```html
<nav>
    <a href="#services">Services</a>
    <a href="#pricing">Pricing</a>
    <a href="#testimonials">Testimonials</a>
    <a href="#contact">Contact</a>
</nav>

<section id="services">
    <h2>Our Services</h2>
</section>

<section id="pricing">
    <h2>Pricing Plans</h2>
</section>

<section id="testimonials">
    <h2>What Our Clients Say</h2>
</section>

<section id="contact">
    <h2>Get In Touch</h2>
</section>
```

**Skip Links (Accessibility)**

Allow users to skip navigation and jump to main content:

```html
<a href="#main-content" class="skip-link">Skip to main content</a>

<header>
    <!-- Navigation -->
</header>

<main id="main-content">
    <!-- Page content -->
</main>
```

CSS to hide skip link but show on focus:
```css
.skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    background: #000;
    color: white;
    padding: 8px;
    z-index: 100;
}

.skip-link:focus {
    top: 0;
}
```

Screen reader and keyboard users can use this to jump to main content.
            """,
            
            "practical_example": """
**Complete Navigation Example**

Here's a realistic navigation structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Company - Home</title>
</head>
<body>
    <!-- Skip link for accessibility -->
    <a href="#main-content" class="skip-link">Skip to main content</a>
    
    <!-- Header with main navigation -->
    <header>
        <div class="logo">
            <a href="/">My Company</a>
        </div>
        
        <nav role="navigation" aria-label="Main">
            <ul>
                <li><a href="/">Home</a></li>
                <li><a href="/about">About</a></li>
                <li><a href="/services">Services</a></li>
                <li><a href="/blog">Blog</a></li>
                <li><a href="/contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <!-- Main content -->
    <main id="main-content">
        <!-- Page content with section anchors -->
        <section id="hero">
            <h1>Welcome</h1>
            <p><a href="/services">Explore our services</a></p>
        </section>
        
        <section id="about">
            <h2>About Us</h2>
            <p>Learn more <a href="/about">about our company</a>.</p>
        </section>
        
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li><a href="/services/web-design">Web Design</a></li>
                <li><a href="/services/development">Development</a></li>
                <li><a href="/services/consulting">Consulting</a></li>
            </ul>
        </section>
    </main>
    
    <!-- Footer with additional navigation -->
    <footer>
        <!-- Breadcrumb for current page context -->
        <nav aria-label="Breadcrumb">
            <ol>
                <li><a href="/">Home</a></li>
            </ol>
        </nav>
        
        <!-- Footer navigation -->
        <nav aria-label="Footer">
            <h3>Quick Links</h3>
            <ul>
                <li><a href="/privacy">Privacy Policy</a></li>
                <li><a href="/terms">Terms of Service</a></li>
                <li><a href="/sitemap">Sitemap</a></li>
                <li><a href="https://twitter.com/mycompany" target="_blank" rel="noopener noreferrer">Twitter</a></li>
            </ul>
        </nav>
        
        <p>&copy; 2024 My Company. All rights reserved.</p>
    </footer>
    
    <style>
        .skip-link {
            position: absolute;
            top: -40px;
            left: 0;
            background: #000;
            color: white;
            padding: 8px;
            z-index: 100;
        }
        
        .skip-link:focus {
            top: 0;
        }
    </style>
</body>
</html>
```

**Key Takeaways**:
1. ✓ Clear, descriptive link text
2. ✓ Proper semantic structure
3. ✓ Accessible navigation with ARIA labels
4. ✓ Skip links for keyboard users
5. ✓ Breadcrumb navigation
6. ✓ Footer navigation
7. ✓ Proper use of target="_blank" with security attributes
8. ✓ Section anchors for jump links
            """
        }
    }
}
