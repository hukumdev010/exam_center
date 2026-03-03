"""
Meta Tags and Document Head - Detailed Content

This file contains comprehensive content for the "Meta Tags" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Meta Tags and Document Head",
    "duration": "45-60 minutes",
    "difficulty": "Beginner to Intermediate",
    "overview": """
    Meta tags provide metadata about HTML documents. Learn how to use meta tags for SEO,
    social sharing, mobile optimization, and other important document properties.
    """,
    
    "detailed_content": {
        "introduction": """
While most of your HTML goes in the `<body>` where users can see it, the `<head>` section
contains important metadata that affects:

1. **Search Engine Optimization (SEO)**: How your page appears in search results
2. **Social Sharing**: How your page looks when shared on social media
3. **Mobile Experience**: How your page displays on mobile devices
4. **Browser Behavior**: How the browser handles your page
5. **Security**: Protecting your site and users

Meta tags are a critical but often overlooked part of web development. A poorly optimized
head section can harm your SEO, hurt your social media presence, and make your site perform
poorly on mobile devices.

In this topic, we'll cover the essential meta tags that every modern website should have.
        """,
        
        "key_concepts": {
            "essential_meta_tags": """
**The Most Important Meta Tags**

These meta tags should be on every website:

**Character Encoding**
```html
<meta charset="UTF-8">
```
Specifies the character encoding. UTF-8 is universal and supports all languages.
This must be declared early in the `<head>`.

**Viewport Meta Tag (Essential for Mobile)**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
This tells mobile browsers to:
- Set viewport width to device width
- Start zoom at 100%
- Allow user zoom

**Critical**: Without this tag, mobile devices treat your site as a desktop page and zoom out.

Properties:
- `width=device-width`: Match the device width
- `initial-scale=1.0`: Initial zoom level
- `maximum-scale=5.0`: Maximum user zoom
- `minimum-scale=0.5`: Minimum user zoom
- `user-scalable=yes`: Allow user zooming
- `viewport-fit=cover`: For notched phones (iPhone X+)

**Page Title**
```html
<title>My Website - A Brief Description</title>
```
The title appears in:
- Browser tab
- Search results (as the main link)
- Browser history
- Bookmarks

Good titles are:
- Descriptive and specific
- Reasonably short (50-60 characters ideal)
- Include important keywords first
- Unique for each page

**Bad title**: "Home"
**Good title**: "Premium Web Design Services | My Company"
**Bad title**: "My Awesome Site About Web Development and Design and Everything Else"
**Good title**: "Web Design & Development Services"

**Description Meta Tag**
```html
<meta name="description" content="Learn web development with our comprehensive courses and tutorials. Free and premium content available.">
```
The description appears in search results under the title. It's like a sales pitch for your page.

Properties:
- Good descriptions are 150-160 characters
- Should accurately describe the page
- Should include relevant keywords
- Should be unique per page
- Write for humans, not just search engines

**Bad description**: "This is a web page."
**Good description**: "Master modern web development with interactive courses covering HTML, CSS, JavaScript, React, and more. Start learning today with our free content."
            """,
            
            "seo_meta_tags": """
**Search Engine Optimization (SEO) Meta Tags**

**Keywords Meta Tag**
```html
<meta name="keywords" content="web development, html, css, javascript, react">
```
Note: Most search engines ignore this tag now, but it doesn't hurt to include it.

**Robots Meta Tag**
Controls how search engines index and display your page:
```html
<!-- Allow all (default) -->
<meta name="robots" content="index, follow">

<!-- Prevent indexing -->
<meta name="robots" content="noindex, follow">

<!-- Prevent following links -->
<meta name="robots" content="index, nofollow">

<!-- Completely prevent -->
<meta name="robots" content="noindex, nofollow">

<!-- Don't show snippets in results -->
<meta name="robots" content="index, follow, nosnippet">
```

**Author Meta Tag**
```html
<meta name="author" content="John Smith">
```

**Copyright**
```html
<meta name="copyright" content="2024 My Company. All rights reserved.">
```

**Language**
While you should use `lang` attribute in `<html>` tag, you can also specify:
```html
<meta http-equiv="content-language" content="en-US">
```

**Refresh Tag**
Automatically refresh or redirect:
```html
<!-- Refresh every 30 seconds -->
<meta http-equiv="refresh" content="30">

<!-- Redirect to another page after 5 seconds -->
<meta http-equiv="refresh" content="5;url=https://example.com">
```
Use sparingly—users find this annoying.

**X-UA-Compatible (IE Legacy Support)**
```html
<meta http-equiv="X-UA-Compatible" content="IE=edge">
```
Forces Internet Explorer to use the latest rendering. Mostly obsolete now.
            """,
            
            "open_graph_tags": """
**Open Graph Tags (Social Media)**

When you share a link on Facebook, LinkedIn, Twitter, etc., the page's Open Graph tags
determine how it appears.

**Basic Open Graph Tags**

```html
<!-- Page title -->
<meta property="og:title" content="Amazing Web Development Course">

<!-- Page description -->
<meta property="og:description" content="Learn web development from scratch with our comprehensive course">

<!-- Featured image (recommended: 1200x630px) -->
<meta property="og:image" content="https://example.com/image.jpg">

<!-- Page URL -->
<meta property="og:url" content="https://example.com/course">

<!-- Page type -->
<meta property="og:type" content="website">

<!-- Site name -->
<meta property="og:site_name" content="My Website">

<!-- Locale -->
<meta property="og:locale" content="en_US">
```

**Complete Example**

```html
<meta property="og:title" content="Learn React in 30 Days">
<meta property="og:type" content="article">
<meta property="og:url" content="https://example.com/react-course">
<meta property="og:image" content="https://example.com/react-hero.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:description" content="Master React with interactive lessons, projects, and real-world examples.">
<meta property="og:site_name" content="Dev Academy">

<!-- For articles specifically -->
<meta property="article:published_time" content="2024-01-15T09:00:00Z">
<meta property="article:modified_time" content="2024-01-20T15:30:00Z">
<meta property="article:author" content="Jane Smith">
<meta property="article:section" content="Education">
<meta property="article:tag" content="react">
<meta property="article:tag" content="javascript">
```

**Image Best Practices**
- Use high-quality images (1200x630px is standard)
- Ensure images are relevant to the content
- Test with Facebook's Sharing Debugger (developers.facebook.com)
- Use JPG for photos, PNG for graphics
            """,
            
            "twitter_and_other_tags": """
**Twitter Card Meta Tags**

Similar to Open Graph, but specifically for Twitter:

```html
<!-- Card type -->
<meta name="twitter:card" content="summary_large_image">

<!-- Twitter username -->
<meta name="twitter:creator" content="@yourname">

<!-- Title -->
<meta name="twitter:title" content="Amazing Course">

<!-- Description -->
<meta name="twitter:description" content="Learn web development step by step">

<!-- Image -->
<meta name="twitter:image" content="https://example.com/image.jpg">

<!-- Site username -->
<meta name="twitter:site" content="@yoursite">
```

**Card Types**
- `summary`: Title, description, image, link
- `summary_large_image`: Like summary but with larger image
- `player`: For audio/video
- `app`: For app promotion

**Relationship Tags**

```html
<!-- Canonical URL (prevent duplicate content penalties) -->
<link rel="canonical" href="https://example.com/article">

<!-- Alternate language versions -->
<link rel="alternate" hreflang="es" href="https://example.com/es/article">
<link rel="alternate" hreflang="fr" href="https://example.com/fr/article">
<link rel="alternate" hreflang="x-default" href="https://example.com/article">

<!-- Stylesheet -->
<link rel="stylesheet" href="style.css">

<!-- Favicon -->
<link rel="icon" href="favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="favicon.ico">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
```
            """,
            
            "mobile_and_app_tags": """
**Mobile and App Meta Tags**

**Favicon**
The small icon shown in browser tabs:

```html
<link rel="icon" href="/favicon.ico" type="image/x-icon">
<link rel="shortcut icon" href="/favicon.ico">

<!-- Modern approach (32x32 PNG) -->
<link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
<link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">

<!-- Apple Touch Icon (home screen) -->
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
```

**Web App Meta Tags**

```html
<!-- Standalone web app (can run full-screen) -->
<meta name="apple-mobile-web-app-capable" content="yes">

<!-- Status bar color (iOS) -->
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

<!-- App name on home screen -->
<meta name="apple-mobile-web-app-title" content="My App">

<!-- Android web app -->
<meta name="mobile-web-app-capable" content="yes">

<!-- Theme color -->
<meta name="theme-color" content="#007AFF">
```

**Manifest File** (for progressive web apps)
```html
<link rel="manifest" href="/manifest.json">
```

**Content Security Policy**
Helps prevent security attacks:
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline';">
```
            """,
            
            "complete_head_example": """
**Complete Head Section Example**

Here's a well-optimized head section for a blog article:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Basic Meta Tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Page Title & Description -->
    <title>Getting Started with React - A Complete Guide for Beginners</title>
    <meta name="description" content="Learn React fundamentals with this comprehensive beginner's guide. Covers components, JSX, hooks, and state management with practical examples.">
    <meta name="keywords" content="react, javascript, web development, frontend">
    
    <!-- Author & Copyright -->
    <meta name="author" content="Jane Developer">
    <meta name="copyright" content="2024 Dev Academy">
    
    <!-- Open Graph Tags (Social Media) -->
    <meta property="og:title" content="Getting Started with React - A Complete Guide for Beginners">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://example.com/blog/react-guide">
    <meta property="og:image" content="https://example.com/images/react-guide.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:description" content="Learn React fundamentals with this comprehensive beginner's guide.">
    <meta property="og:site_name" content="Dev Academy">
    <meta property="article:published_time" content="2024-01-15T09:00:00Z">
    <meta property="article:modified_time" content="2024-01-20T14:30:00Z">
    <meta property="article:author" content="Jane Developer">
    <meta property="article:section" content="Web Development">
    <meta property="article:tag" content="react">
    <meta property="article:tag" content="javascript">
    
    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:creator" content="@janedev">
    <meta name="twitter:title" content="Getting Started with React - A Complete Guide">
    <meta name="twitter:description" content="Learn React fundamentals with this comprehensive beginner's guide.">
    <meta name="twitter:image" content="https://example.com/images/react-guide.jpg">
    
    <!-- Mobile & App -->
    <meta name="theme-color" content="#007AFF">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-title" content="Dev Academy">
    
    <!-- Favicon -->
    <link rel="icon" type="image/png" href="/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="/favicon-16x16.png" sizes="16x16">
    <link rel="apple-touch-icon" href="/apple-touch-icon.png">
    
    <!-- Canonical URL -->
    <link rel="canonical" href="https://example.com/blog/react-guide">
    
    <!-- Stylesheets -->
    <link rel="stylesheet" href="/styles/main.css">
    <link rel="stylesheet" href="/styles/prism.css">
    
    <!-- Preconnect for Performance -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    
    <!-- Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_ID"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', 'GA_ID');
    </script>
</head>
<body>
    <!-- Page content -->
</body>
</html>
```

**Key Takeaways**:
1. ✓ Charset and viewport declared first
2. ✓ Clear, descriptive title
3. ✓ Detailed meta description
4. ✓ Open Graph tags for social sharing
5. ✓ Twitter Card tags
6. ✓ Mobile optimization tags
7. ✓ Favicon for branding
8. ✓ Canonical URL to prevent duplicates
9. ✓ Proper stylesheets and fonts
10. ✓ Performance optimizations (preconnect)
11. ✓ Analytics tracking
            """
        }
    }
}
