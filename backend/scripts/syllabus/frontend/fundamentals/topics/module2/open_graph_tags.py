"""
Open Graph Tags - Detailed Content

This file contains comprehensive content for the "Open Graph Tags" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Open Graph Tags",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    Open Graph (OG) tags control how your web pages appear when shared on social media platforms.
    This topic covers the essential OG tags and best practices for social sharing.
    """,
    
    "detailed_content": {
        "introduction": """
The Open Graph protocol enables websites to become rich objects in social networks. By adding
Open Graph tags to your HTML, you can control how your content appears when shared on Facebook,
LinkedIn, Twitter, Instagram, and other platforms.

Without Open Graph tags, social platforms will try to guess what content to display. With them,
you have full control over the title, image, and description shown in social feeds.
        """,
        
        "key_concepts": {
            "basic_og_tags": """
**Basic Open Graph Tags**

Every page should have these four core tags:

```html
<meta property="og:title" content="The Title of Your Page">
<meta property="og:type" content="website">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/">
```

- `og:title`: The title shown in social share (usually 1-2 sentences)
- `og:type`: Type of content (website, article, profile, etc.)
- `og:image`: Image URL shown in preview (recommended: 1200x630px)
- `og:url`: The canonical URL for this page
        """,
            
            "og_description": """
**Description and Additional Tags**

```html
<meta property="og:title" content="10 Web Development Tips">
<meta property="og:type" content="article">
<meta property="og:image" content="https://example.com/og-image.jpg">
<meta property="og:url" content="https://example.com/article">
<meta property="og:description" content="Learn 10 essential tips to improve your web development skills">
<meta property="og:site_name" content="My Developer Blog">
```

Additional useful tags:
- `og:description`: 2-4 sentence description (155-200 chars)
- `og:site_name`: Name of your website
- `og:locale`: Language and region (e.g., en_US, es_ES)
        """,
            
            "og_images": """
**Open Graph Images**

```html
<!-- Single image -->
<meta property="og:image" content="https://example.com/image.jpg">

<!-- Multiple images (for platforms supporting multiple previews) -->
<meta property="og:image" content="https://example.com/image-1.jpg">
<meta property="og:image" content="https://example.com/image-2.jpg">
<meta property="og:image" content="https://example.com/image-3.jpg">

<!-- Image specifications -->
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/jpeg">

<!-- Alternative format for mobile -->
<meta property="og:image:alt" content="Description of the image for accessibility">
```

Image best practices:
- Size: 1200x630 pixels (16:9 aspect ratio)
- Format: JPG or PNG
- Size: Less than 5MB
- Descriptive: Use images that represent your content
- Alt text: Always include `og:image:alt`
        """,
            
            "og_content_types": """
**Common Open Graph Content Types**

```html
<!-- Website (default) -->
<meta property="og:type" content="website">

<!-- Article -->
<meta property="og:type" content="article">
<meta property="article:published_time" content="2024-01-15T08:00:00Z">
<meta property="article:modified_time" content="2024-01-15T12:00:00Z">
<meta property="article:author" content="https://example.com/john-doe">
<meta property="article:section" content="Technology">
<meta property="article:tag" content="web-development">

<!-- Profile -->
<meta property="og:type" content="profile">
<meta property="profile:first_name" content="John">
<meta property="profile:last_name" content="Doe">
<meta property="profile:username" content="johndoe">
<meta property="profile:gender" content="male">

<!-- Video -->
<meta property="og:type" content="video.other">
<meta property="og:video" content="https://example.com/video.mp4">
<meta property="og:video:type" content="video/mp4">
<meta property="og:video:width" content="1280">
<meta property="og:video:height" content="720">

<!-- Music -->
<meta property="og:type" content="music.song">
<meta property="music:duration" content="240">
<meta property="music:artist" content="Artist Name">

<!-- Product -->
<meta property="og:type" content="product">
<meta property="product:price:amount" content="19.99">
<meta property="product:price:currency" content="USD">
```

Choose the type that best matches your content.
        """,
            
            "article_tags": """
**Article-Specific Tags**

```html
<meta property="og:type" content="article">

<!-- Publishing details -->
<meta property="article:published_time" content="2024-12-11T10:00:00Z">
<meta property="article:modified_time" content="2024-12-11T14:00:00Z">
<meta property="article:expiration_time" content="2024-12-25T23:59:59Z">

<!-- Author information -->
<meta property="article:author" content="https://example.com/authors/john-doe">
<meta property="article:author" content="https://example.com/authors/jane-smith">

<!-- Categorization -->
<meta property="article:section" content="Technology">
<meta property="article:tag" content="web-development">
<meta property="article:tag" content="seo">
<meta property="article:tag" content="html">
```

These tags help platforms:
- Index content chronologically
- Attribute work to authors
- Categorize content
- Recommend related articles
        """,
            
            "og_internationalization": """
**Internationalization**

```html
<!-- Default/primary language -->
<meta property="og:locale" content="en_US">

<!-- Alternative language versions -->
<meta property="og:locale:alternate" content="es_ES">
<meta property="og:locale:alternate" content="fr_FR">
<meta property="og:locale:alternate" content="de_DE">

<!-- Language structure: language_TERRITORY -->
<!-- en_US = English - United States -->
<!-- es_ES = Spanish - Spain -->
<!-- pt_BR = Portuguese - Brazil -->
```

Helps platforms show content to speakers of different languages.
        """,
            
            "testing_og_tags": """
**Testing Open Graph Tags**

Use these tools to verify your OG tags work:

1. **Facebook Sharing Debugger**
   - Visit: facebook.com/developers/tools/debug/sharing
   - Enter your URL
   - See how content will appear

2. **Twitter Card Validator**
   - Visit: cards-dev.twitter.com/validator
   - Check Twitter-specific tags

3. **LinkedIn Post Inspector**
   - Visit: linkedin.com/inspector
   - Preview LinkedIn share appearance

4. **Inspect DOM**
   - In browser DevTools, check the <head> section
   - Verify all OG tags are present

Quick validation:
```html
<!-- Minimum required -->
<meta property="og:title" content="...">
<meta property="og:type" content="website">
<meta property="og:image" content="...">
<meta property="og:url" content="...">

<!-- Recommended -->
<meta property="og:description" content="...">
<meta property="og:site_name" content="...">
```
        """,
            
            "common_mistakes": """
**Common Mistakes to Avoid**

❌ **No images**: Always include a quality image

❌ **Wrong image size**: Use 1200x630px minimum

❌ **Generic titles**: Make titles specific to each page

❌ **Broken image URLs**: Ensure images are publicly accessible

❌ **Wrong content type**: Match og:type to actual content

❌ **Missing description**: Always include meaningful description

❌ **Hardcoded values**: Use dynamic values for dynamic content

✅ **Good practice**: Test with sharing debuggers regularly
        """,
        }
    }
}
