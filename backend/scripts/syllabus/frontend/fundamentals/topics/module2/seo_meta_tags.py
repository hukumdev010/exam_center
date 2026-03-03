"""
SEO Meta Tags - Detailed Content

This file contains comprehensive content for the "SEO Meta Tags" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "SEO Meta Tags",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    SEO meta tags specifically target search engine optimization. This topic covers tags that improve
    your site's visibility in search results and social sharing.
    """,
    
    "detailed_content": {
        "introduction": """
SEO (Search Engine Optimization) meta tags help search engines understand your content and display
your pages appropriately in search results. They also control how your content appears when shared
on social media platforms.
        """,
        
        "key_concepts": {
            "canonical_tags": """
**Canonical Tags**

```html
<!-- Tell search engines which version is the original -->
<link rel="canonical" href="https://example.com/article">

<!-- Example: Multiple URLs for same content -->
<!-- URL 1: https://example.com/article -->
<!-- URL 2: https://example.com/article?ref=social -->
<!-- URL 3: https://example.com/article/mobile -->

<!-- All should have this canonical tag pointing to primary URL -->
<link rel="canonical" href="https://example.com/article">
```

Use canonical tags to:
- Prevent duplicate content issues
- Consolidate page authority to one URL
- Manage URL parameters and variations
- Specify mobile vs desktop versions
        """,
            
            "og_tags": """
**Open Graph Tags**

```html
<!-- Basic Open Graph tags -->
<meta property="og:title" content="Article Title">
<meta property="og:description" content="Article description goes here">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/article">
<meta property="og:type" content="article">

<!-- For articles -->
<meta property="article:published_time" content="2024-12-11T10:00:00Z">
<meta property="article:modified_time" content="2024-12-11T14:00:00Z">
<meta property="article:author" content="https://example.com/authors/john-doe">
<meta property="article:section" content="Technology">
<meta property="article:tag" content="web-development">
<meta property="article:tag" content="seo">

<!-- For other types -->
<meta property="og:type" content="website">
<meta property="og:type" content="profile">
<meta property="og:type" content="music.song">
<meta property="og:type" content="video.movie">
```

Open Graph controls how content appears when shared on:
- Facebook
- LinkedIn
- Pinterest
- WhatsApp
- Telegram
- Other social platforms

Common OG properties:
- `og:title`: Page title
- `og:description`: Page description
- `og:image`: Image URL for preview
- `og:url`: Canonical URL
- `og:type`: Content type
- `og:site_name`: Website name
        """,
            
            "twitter_tags": """
**Twitter Card Tags**

```html
<!-- Summary card (default) -->
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="Page Title">
<meta name="twitter:description" content="Page description">
<meta name="twitter:image" content="https://example.com/image.jpg">
<meta name="twitter:creator" content="@yourhandle">
<meta name="twitter:site" content="@yoursite">

<!-- Summary card with large image -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://example.com/large-image.jpg">

<!-- App card -->
<meta name="twitter:card" content="app">
<meta name="twitter:app:name:iphone" content="App Name">
<meta name="twitter:app:id:iphone" content="123456789">
<meta name="twitter:app:url:iphone" content="https://example.com/app">
```

Twitter Card types:
- `summary`: Small preview
- `summary_large_image`: Large preview
- `app`: Links to app
- `player`: Video/audio preview
        """,
            
            "structured_data": """
**Structured Data / Schema.org**

```html
<!-- JSON-LD (recommended) -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Headline",
  "description": "Article description",
  "image": "https://example.com/image.jpg",
  "datePublished": "2024-12-11",
  "dateModified": "2024-12-11",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  },
  "publisher": {
    "@type": "Organization",
    "name": "My Website",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
</script>

<!-- Microdata (alternative) -->
<article itemscope itemtype="https://schema.org/Article">
  <h1 itemprop="headline">Article Title</h1>
  <p itemprop="description">Article description</p>
  <img itemprop="image" src="image.jpg">
</article>

<!-- RDFa (alternative) -->
<article vocab="https://schema.org/" typeof="Article">
  <h1 property="headline">Article Title</h1>
  <p property="description">Article description</p>
</article>
```

Structured data helps search engines understand:
- Content type and structure
- Product information and pricing
- Events and schedules
- Company information
- Recipes and ingredients
- Ratings and reviews

Benefits:
- Rich snippets in search results
- Knowledge panels
- Voice assistant understanding
- Better search visibility
        """,
            
            "preload_prefetch": """
**Resource Hints**

```html
<!-- Preload critical resources -->
<link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="image.webp" as="image">

<!-- Prefetch for likely next navigation -->
<link rel="prefetch" href="next-page.html">
<link rel="prefetch" href="styles.css">

<!-- DNS prefetch for external domains -->
<link rel="dns-prefetch" href="//example.com">

<!-- Preconnect with TLS -->
<link rel="preconnect" href="//cdn.example.com" crossorigin>

<!-- Prerender entire page (expensive) -->
<link rel="prerender" href="next-page.html">
```

Use cases:
- `preload`: Fonts, critical images, scripts needed soon
- `prefetch`: Resources needed on next page
- `dns-prefetch`: External domains you'll connect to
- `preconnect`: Establish early connection to domain
        """,
            
            "mobile_specific": """
**Mobile and Browser Specific Tags**

```html
<!-- App icon (favicon alternative) -->
<link rel="apple-touch-icon" href="apple-icon.png">
<link rel="icon" type="image/png" href="favicon.png">

<!-- Status bar color on mobile -->
<meta name="theme-color" content="#1F2937">

<!-- Disable tap highlight on mobile -->
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">

<!-- App status bar style (iOS) -->
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">

<!-- App name (iOS) -->
<meta name="apple-mobile-web-app-title" content="My App">

<!-- Format detection -->
<meta name="format-detection" content="telephone=no">
```

Improves mobile experience and app-like behavior.
        """,
        }
    }
}
