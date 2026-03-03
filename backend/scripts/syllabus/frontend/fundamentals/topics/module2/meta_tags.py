"""
Meta Tags - Detailed Content

This file contains comprehensive content for the "Meta Tags" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Meta Tags",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    Meta tags provide metadata about HTML documents. This topic covers the most important and
    commonly used meta tags and their purposes.
    """,
    
    "detailed_content": {
        "introduction": """
Meta tags are HTML elements placed in the <head> section that provide information about the page
to browsers, search engines, and social media platforms. While meta tags don't display content on
the page itself, they significantly impact how your page is displayed and discovered online.
        """,
        
        "key_concepts": {
            "charset_meta_tag": """
**Character Set Meta Tag**

```html
<meta charset="UTF-8">
```

This MUST be the first meta tag in the head. It declares the character encoding:
- UTF-8: Supports all languages and special characters (recommended)
- Should be placed before all other content except title
- Without this, special characters may display incorrectly

This is critical for international content and emoji support.
        """,
            
            "viewport_meta_tag": """
**Viewport Meta Tag**

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

Controls how mobile browsers render your page:
- `width=device-width`: Page width matches device width
- `initial-scale=1.0`: Initial zoom level (1.0 = 100%)
- `maximum-scale=5.0`: Maximum zoom allowed
- `user-scalable=no`: Disable zoom (not recommended)
- `viewport-fit=cover`: Support notches on modern phones

Essential for responsive design. Without this, mobile browsers assume a 980px width.
        """,
            
            "description_meta_tag": """
**Description Meta Tag**

```html
<meta name="description" content="Learn web development with our comprehensive course covering HTML, CSS, and JavaScript.">
```

- Shown in search engine results below the page title
- Should be 150-160 characters
- Should be unique for each page
- Should accurately describe page content
- Click-through rates improve with compelling descriptions

Good descriptions:
- Summarize the page content
- Include relevant keywords naturally
- Call to action (optional)
- Are unique and specific to each page
        """,
            
            "keywords_meta_tag": """
**Keywords Meta Tag (Less Important)**

```html
<meta name="keywords" content="web development, HTML, CSS, JavaScript, frontend">
```

- Comma-separated list of keywords
- Less important for modern SEO (search engines focus on content)
- Still useful for clarity
- Don't keyword stuff (repeating keywords excessively)
- Not all search engines use this

Modern search engines prefer analyzing actual content over meta keywords.
        """,
            
            "author_copyright": """
**Author and Copyright Meta Tags**

```html
<meta name="author" content="John Doe">
<meta name="copyright" content="Copyright 2024 My Company. All rights reserved.">
<meta name="creator" content="John Doe">
<meta name="publisher" content="My Company">
```

Optional tags that identify page creator and copyright information.
        """,
            
            "robots_meta_tag": """
**Robots Meta Tag**

```html
<!-- Allow all search engines to index and follow links -->
<meta name="robots" content="index, follow">

<!-- Don't index this page -->
<meta name="robots" content="noindex">

<!-- Don't follow links on this page -->
<meta name="robots" content="nofollow">

<!-- Don't archive this page -->
<meta name="robots" content="noarchive">

<!-- Multiple values -->
<meta name="robots" content="index, follow, noarchive">
```

Common values:
- `index`: Allow search engines to index the page
- `noindex`: Don't index this page
- `follow`: Follow links on the page
- `nofollow`: Don't follow links
- `noarchive`: Don't cache the page
        """,
            
            "refresh_redirect": """
**Refresh and Redirect Meta Tag**

```html
<!-- Redirect after 3 seconds -->
<meta http-equiv="refresh" content="3;url=https://example.com/new-page">

<!-- Refresh page every 60 seconds -->
<meta http-equiv="refresh" content="60">
```

Note: Redirects should prefer server-side redirects (HTTP 301) over meta redirects.
Meta redirects are useful for:
- Temporary redirects when server-side redirect isn't possible
- Scheduled page refreshes
        """,
            
            "language_meta_tag": """
**Language Meta Tag**

```html
<html lang="en">
<!-- Or in meta tag -->
<meta name="language" content="English">

<!-- For specific regions -->
<html lang="en-US"> <!-- US English -->
<html lang="en-GB"> <!-- British English -->
<html lang="es">    <!-- Spanish -->
<html lang="fr">    <!-- French -->
```

Always declare the language in the html element's `lang` attribute.
        """,
        }
    }
}
