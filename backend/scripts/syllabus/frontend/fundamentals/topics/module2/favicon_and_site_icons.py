"""
Favicon and Site Icons - Detailed Content

This file contains comprehensive content for the "Favicon and Site Icons" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Favicon and Site Icons",
    "duration": "30-45 minutes",
    "difficulty": "Beginner",
    "overview": """
    Favicons and site icons are small images that represent your website. This topic covers how to
    implement icons for browsers, mobile devices, and various platforms.
    """,
    
    "detailed_content": {
        "introduction": """
A favicon (favorite icon) is a small image displayed in the browser tab, bookmarks, and address bar.
Modern websites need multiple icon formats for different devices and platforms (browsers, mobile home
screens, PWAs, etc.). Proper icon implementation improves brand recognition and user experience.
        """,
        
        "key_concepts": {
            "basic_favicon": """
**Basic Favicon**

```html
<!-- Simple ICO format (traditional) -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">

<!-- Modern PNG format (recommended) -->
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">

<!-- SVG favicon (scalable, modern) -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">

<!-- Place favicon.ico in root for automatic detection -->
<!-- If favicon.ico is in website root, browsers find it automatically -->
<!-- /favicon.ico -->
```

Key points:
- Favicon must be square (usually 32x32 or 16x16 for browsers)
- Keep file size small (under 10KB)
- .ico is traditional but PNG/SVG work better
- Browsers cache favicons for a long time
        """,
            
            "apple_touch_icons": """
**Apple Touch Icons (iOS)**

```html
<!-- iPhone and iPad home screen icon -->
<link rel="apple-touch-icon" href="/apple-touch-icon.png">

<!-- Specific sizes for different devices -->
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon-180x180.png">
<link rel="apple-touch-icon" sizes="152x152" href="/apple-touch-icon-152x152.png">
<link rel="apple-touch-icon" sizes="167x167" href="/apple-touch-icon-167x167.png">

<!-- Default location (optional if at /apple-touch-icon.png) -->
<!-- /apple-touch-icon.png -->
```

Specifications:
- Size: 180x180 pixels (for latest devices)
- Format: PNG with transparency
- Shape: Will be automatically rounded with gloss effect
- Should not include rounded corners (iOS adds them)

When user taps "Add to Home Screen" on iOS, this icon is used.
        """,
            
            "android_icons": """
**Android Icons**

```html
<!-- Android Chrome web app manifest -->
<link rel="manifest" href="/manifest.json">

<!-- Fallback for older Android -->
<link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png">
<link rel="icon" type="image/png" sizes="512x512" href="/android-chrome-512x512.png">

<!-- Theme color for address bar -->
<meta name="theme-color" content="#1F2937">
```

manifest.json example:
```json
{
  "name": "My Website",
  "short_name": "My Site",
  "icons": [
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#1F2937",
  "background_color": "#FFFFFF",
  "display": "standalone"
}
```

Common sizes:
- 192x192: Android Chrome
- 512x512: Splash screens
        """,
            
            "windows_icons": """
**Windows Icons**

```html
<!-- Windows tile images -->
<meta name="msapplication-TileColor" content="#1F2937">
<meta name="msapplication-TileImage" content="/mstile-144x144.png">
<meta name="msapplication-config" content="/browserconfig.xml">
```

browserconfig.xml:
```xml
<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
    <msapplication>
        <tile>
            <square70x70logo src="/mstile-70x70.png"/>
            <square150x150logo src="/mstile-150x150.png"/>
            <square310x310logo src="/mstile-310x310.png"/>
            <TileColor>#1F2937</TileColor>
        </tile>
    </msapplication>
</browserconfig>
```

Used when users pin your site to Windows Start menu.
        """,
            
            "complete_icon_setup": """
**Complete Icon Setup**

A comprehensive icon configuration:

```html
<!-- Standard favicon -->
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">

<!-- SVG favicon (modern) -->
<link rel="icon" type="image/svg+xml" href="/favicon.svg">

<!-- Apple icons -->
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

<!-- Android -->
<link rel="manifest" href="/manifest.json">

<!-- Windows -->
<meta name="msapplication-TileColor" content="#1F2937">
<meta name="msapplication-TileImage" content="/mstile-144x144.png">
<meta name="msapplication-config" content="/browserconfig.xml">

<!-- Browser theme color -->
<meta name="theme-color" content="#1F2937">

<!-- Status bar color on mobile -->
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
```

File structure:
```
/public
  /favicon.ico              (32x32 or 16x16)
  /favicon-32x32.png
  /favicon-16x16.png
  /favicon.svg
  /apple-touch-icon.png     (180x180)
  /android-chrome-192x192.png
  /android-chrome-512x512.png
  /mstile-144x144.png
  /mstile-150x150.png
  /mstile-310x310.png
  /manifest.json
  /browserconfig.xml
```
        """,
            
            "icon_best_practices": """
**Icon Design Best Practices**

1. **Consistency**: Match your brand style
2. **Simplicity**: Avoid details that disappear at small sizes
3. **Recognizable**: Users should recognize your brand
4. **Color**: Use your brand colors
5. **Safe Zone**: Keep important elements away from edges
6. **Test**: Test at actual sizes (16x16, 32x32, 180x180)
7. **Performance**: Keep file sizes small

Guidelines:
- Don't use gradients (may not scale well)
- Avoid text (unreadable at small sizes)
- Test against different backgrounds
- Use padding/safe zones
- Ensure readability at 16x16px
        """,
            
            "generating_icons": """
**Tools for Icon Generation**

1. **Online Generators**
   - favgen.com - Generate favicon and icons
   - realfavicongenerator.net - Comprehensive generator
   - favicon.io - Create favicons
   - convertio.co - Convert images to favicon

2. **Design Software**
   - Figma - Design and export
   - Adobe XD - Design tool
   - Illustrator - Vector design
   - Photoshop - Image editing

3. **Command Line**
   - ImageMagick: Convert images to various formats
   - ffmpeg: Convert between image formats
   - Sharp (Node.js): Generate responsive images

Example with ImageMagick:
```bash
convert logo.png -define icon:auto-resize=256,128,96,64,48,32,16 favicon.ico
```
        """,
        }
    }
}
