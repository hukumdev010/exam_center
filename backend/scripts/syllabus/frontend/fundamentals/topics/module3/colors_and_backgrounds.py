"""
Colors and Backgrounds - Detailed Content

This file contains comprehensive content for the "Colors and Backgrounds" topic
from Module 3: CSS Fundamentals & Layout.
"""

TOPIC_CONTENT = {
    "title": "Colors and Backgrounds",
    "duration": "75-90 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Colors and backgrounds are fundamental to web design. This topic covers how to
    specify colors, work with different color formats, and create sophisticated
    background effects in CSS.
    """,
    
    "detailed_content": {
        "introduction": """
Color is one of the most important aspects of web design. It affects readability, aesthetics, user perception, and accessibility. CSS provides multiple ways to specify colors and create backgrounds, from simple solid colors to complex gradients and images.

Understanding color models, color formats, and accessibility considerations is essential for creating websites that look good and work for everyone.
        """,
        
        "key_concepts": {
            "color_formats": """
**CSS Color Values**

CSS supports multiple ways to specify colors:

**Named Colors**
```css
p { color: red; }
p { color: blue; }
p { color: transparent; }
p { color: currentColor; /* Inherits from parent */ }
```

CSS supports 140+ named colors. Easy to read but limited.

**Hexadecimal (Hex)**
```css
p { color: #FF0000; } /* Red */
p { color: #0066cc; } /* Blue */
p { color: #fff; }    /* White - shorthand */
p { color: #333; }    /* Dark gray - shorthand */
```

Hex colors are 6 digits (or 3 shorthand). Format: #RRGGBB

**RGB and RGBA**
```css
p { color: rgb(255, 0, 0); }           /* Red */
p { color: rgb(0, 102, 204); }         /* Blue */
p { color: rgba(255, 0, 0, 0.5); }     /* Red with 50% opacity */
p { color: rgba(0, 0, 0, 0); }         /* Transparent */
```

RGB: Red, Green, Blue values (0-255). RGBA adds Alpha (opacity, 0-1).

**HSL and HSLA**
```css
p { color: hsl(0, 100%, 50%); }        /* Red */
p { color: hsl(240, 100%, 50%); }      /* Blue */
p { color: hsla(0, 100%, 50%, 0.5); }  /* Red with 50% opacity */
```

HSL: Hue (0-360°), Saturation (0-100%), Lightness (0-100%).

**Which Format to Use?**

- **Named colors**: Simple designs, accessibility keywords
- **Hex**: Traditional, easy to read for developers
- **RGB/RGBA**: When you need transparency or programmatic generation
- **HSL/HSLA**: Better for color manipulation (adjust lightness/saturation easily)

Modern practice is moving toward HSL for better readability and maintainability.

**Color Opacity**

```css
/* Using RGBA */
p { color: rgba(0, 0, 0, 0.5); }

/* Using separate opacity property */
p {
    color: black;
    opacity: 0.5;
}

/* Using hex with alpha (modern browsers) */
p { color: #00000080; } /* Black with 50% opacity */
```

Note: `opacity` affects the entire element, while `rgba` affects only the color.
            """,
            
            "background_property": """
**Background Properties**

The `background` property controls what appears behind the content.

**Solid Color Background**
```css
body {
    background-color: #f5f5f5;
}

.card {
    background-color: white;
    padding: 1em;
}
```

**Background Images**
```css
.hero {
    background-image: url('hero.jpg');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Using background shorthand */
.hero {
    background: url('hero.jpg') center / cover no-repeat;
}
```

**Background Image Properties**

- `background-image`: URL of the image
- `background-size`: How to size the image (cover, contain, specific dimensions)
- `background-position`: Where to position the image (center, top left, etc.)
- `background-repeat`: Whether to repeat (repeat, no-repeat, repeat-x, repeat-y)
- `background-attachment`: Fixed or scroll with page

```css
.full-width {
    background-image: url('pattern.jpg');
    background-size: 100px 100px;
    background-position: top left;
    background-repeat: repeat;
    background-attachment: fixed;
}
```

**Gradients**

CSS can create gradients without images:

```css
/* Linear gradient */
div {
    background: linear-gradient(to right, red, blue);
    background: linear-gradient(45deg, red, blue);
    background: linear-gradient(to right, red 0%, blue 100%);
}

/* Radial gradient */
div {
    background: radial-gradient(circle, red, blue);
    background: radial-gradient(circle at center, red, blue);
}

/* Conic gradient */
div {
    background: conic-gradient(red, yellow, green, blue, red);
}

/* Repeating gradient */
div {
    background: repeating-linear-gradient(
        45deg,
        red,
        red 20px,
        blue 20px,
        blue 40px
    );
}
```

**Multiple Backgrounds**

```css
div {
    background-image: 
        linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
        url('background.jpg');
    background-size: 100%, 100%;
    background-position: center, center;
}
```

This creates a darkened overlay over an image.
            """,
            
            "color_accessibility": """
**Color Contrast**

Colors must have sufficient contrast for readability:

```css
/* ✅ Good contrast - text visible */
.dark-text { color: #333; background: white; }

/* ❌ Poor contrast - text hard to read */
.light-text { color: #ddd; background: white; }

/* ✅ Good contrast - meets WCAG AA standard */
a { color: #0066cc; background: white; } /* High contrast */

/* ❌ Poor contrast */
a { color: #0088dd; background: #0099ff; } /* Similar colors */
```

**WCAG Contrast Ratios**

- **Normal text**: Minimum 4.5:1 (AA), 7:1 (AAA)
- **Large text**: Minimum 3:1 (AA), 4.5:1 (AAA)

Tools like WebAIM Contrast Checker help verify contrast.

**Don't Rely Only on Color**

Don't communicate information through color alone:

```css
/* ❌ Bad - red only for error, colorblind users miss it */
.error { color: red; }

/* ✅ Good - color plus icon/text indicator */
.error {
    color: red;
}
.error::before {
    content: "⚠ ";
}
```

**System Colors**

Modern CSS supports system colors for accessibility:

```css
button {
    color: ButtonText;
    background: ButtonFace;
    border: 1px solid ButtonBorder;
}
```

System colors respect user preferences and accessibility settings.
            """,
            
            "practical_color_techniques": """
**Color Overlay Technique**

Add a semi-transparent color over an image:

```css
.hero {
    background-image:
        linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)),
        url('background.jpg');
    background-size: 100%, 100%;
    background-position: center, center;
}
```

**Creating Cards with Subtle Backgrounds**

```css
.card {
    background: white;
    border: 1px solid #eee;
}

.card:hover {
    background: #fafafa;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
```

**Color Scheme Patterns**

```css
/* Monochromatic - variations of one color */
.primary { background: #0066cc; }
.primary-light { background: #cce5ff; }
.primary-dark { background: #003d7a; }

/* Complementary colors */
.success { color: #27ae60; }  /* Green */
.warning { color: #f39c12; }  /* Orange */
.error { color: #e74c3c; }    /* Red */
```

**Dark Mode Support**

```css
body {
    background: white;
    color: black;
}

@media (prefers-color-scheme: dark) {
    body {
        background: #1a1a1a;
        color: #ffffff;
    }
    
    a { color: #66ccff; }
}
```

**Semantic Color Usage**

```css
/* Meaningful color names */
:root {
    --color-primary: #0066cc;
    --color-success: #27ae60;
    --color-warning: #f39c12;
    --color-error: #e74c3c;
    --color-neutral: #95a5a6;
}

.button-primary {
    background: var(--color-primary);
}

.badge-error {
    background: var(--color-error);
}
```
            """,
        },
        
        "key_takeaways": [
            "CSS supports multiple color formats: named, hex, RGB/RGBA, HSL/HSLA",
            "Use rgba() or hsla() for colors with transparency",
            "background-color applies solid color; background-image uses images or gradients",
            "Linear, radial, and conic gradients create complex effects without images",
            "Background shorthand combines all background properties efficiently",
            "Ensure sufficient color contrast for accessibility (minimum 4.5:1 for normal text)",
            "Don't communicate information through color alone",
            "Multiple backgrounds allow layering images and gradients",
            "background-size: cover makes images fill containers",
            "Use CSS variables for consistent, maintainable color schemes"
        ]
    }
}
