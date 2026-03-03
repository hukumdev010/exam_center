"""
Browser Compatibility - Detailed Content

This file contains content for the "Browser Compatibility" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Browser Compatibility",
    "duration": "8-10 minutes",
    "difficulty": "Beginner",
    "overview": """
    Different browsers support different features and have different rendering engines. Browser compatibility
    is about ensuring your web application works well across different browsers and versions.
    """,
    
    "detailed_content": {
        "introduction": """
Building a website that only works in Chrome isn't acceptable. Your users might use Firefox, Safari, Edge, or
other browsers. They might be on old devices with old browsers, or new devices with new browsers. Your job as a
web developer is to make your application work for all of them.

Browser compatibility is one of the biggest challenges in web development. It requires testing, careful coding,
and often compromises between using new features and supporting older browsers.
        """,
        
        "key_concepts": {
            "why_compatibility_matters": """
**The Browser Landscape**

Market share (approximate):
- Chrome: ~65%
- Safari: ~20%
- Firefox: ~10%
- Edge: ~3%
- Others: ~2%

You can't ignore Safari or Firefox. Even if they have small market share, ignoring them means your site is broken
for millions of users.

**Age of Browsers**

Users don't always update browsers:
- Some use old browsers by choice
- Some use very old devices that can't run new browsers
- Corporate computers often run outdated browsers
- Mobile devices often have old browsers

Supporting old browsers is expensive but sometimes necessary.

**Feature Support**

Each browser supports different features at different times:
- Chrome might support CSS Grid, but old IE doesn't
- Safari might not support a new JavaScript feature
- Firefox might have a bug in a CSS implementation

You need to know what browsers support what features.
            """,
            
            "testing_strategies": """
**Can I Use Website**

Use https://caniuse.com to check feature support:

Search for a feature (CSS Grid, Flexbox, Fetch API) and see:
- Which browsers support it
- Which versions support it
- Percentage of users with support
- What to do for unsupported browsers

Example: If 95% of users support a feature, you might use it directly.
If only 80% support it, you need a fallback.

**Browser Testing Tools**

**BrowserStack**: Test on real browsers and devices
**Sauce Labs**: Cloud-based browser testing
**CrossBrowserTesting**: Test on multiple browsers
**GitHub Actions**: Automated testing across browsers

**Manual Testing**

Test your site on:
- Chrome (latest version)
- Firefox (latest version)
- Safari (latest version)
- Edge (latest version)
- Mobile Safari (iOS)
- Chrome Mobile (Android)
- Older browser versions (IE 11 if necessary)

This is tedious but important.

**DevTools Testing**

Simulate different browsers in DevTools:
1. Open DevTools
2. Click device toggle
3. Select specific device or browser
4. Test how it renders
            """,
            
            "compatibility_techniques": """
**Feature Detection**

Check if browser supports feature before using it:

```javascript
// Check if Fetch API is supported
if (window.fetch) {
  // Use Fetch
} else {
  // Use XMLHttpRequest (older)
}
```

**CSS Prefixes**

Different browsers need different prefixes:

```css
/* Without prefix (modern) */
transform: rotate(45deg);

/* With prefixes (old browsers) */
-webkit-transform: rotate(45deg);  /* Chrome, Safari */
-moz-transform: rotate(45deg);     /* Firefox */
-ms-transform: rotate(45deg);      /* IE */
-o-transform: rotate(45deg);       /* Opera */
```

Use tools like Autoprefixer to add prefixes automatically.

**Polyfills**

JavaScript that adds support for unsupported features:

```javascript
// Polyfill for old browser that doesn't have Promise
if (!window.Promise) {
  window.Promise = require('promise-polyfill');
}
```

**Graceful Degradation**

Provide fallbacks for unsupported features:

```css
/* Fallback for old browsers */
.grid {
  display: flex;
}

/* Modern layout for new browsers */
@supports (display: grid) {
  .grid {
    display: grid;
  }
}
```

**Minimum Viable Browser Support**

Decide: What's the oldest browser you'll support?

- Modern: Only latest 2 versions of each browser
- Standard: IE 11 and newer
- Legacy: IE 8 and newer (painful and slow)

More support = more work and slower development.
            """,
            
            "practical_approach": """
**The Right Balance**

**Don't Over-Support**

- Don't support IE 8 unless you have to
- Focus on modern browsers
- Use standards and best practices
- Progressive enhancement is key

**Use Build Tools**

Tools handle compatibility automatically:
- **Babel**: Converts modern JavaScript to older syntax
- **Autoprefixer**: Adds CSS prefixes
- **PostCSS**: Processes CSS for compatibility
- **Webpack**: Bundles with compatibility in mind

**Test Important Features**

```bash
# Run tests across browsers
npm test -- --browsers Chrome,Firefox,Safari
```

**Real Device Testing**

Test on actual devices:
- Borrow friends' devices
- Use services like BrowserStack
- Test on old and new devices

**Documentation**

Document browser support:

```json
{
  "browserslist": [
    "last 2 versions",
    "not dead",
    "not IE <= 11"
  ]
}
```

This tells build tools what browsers to support.
            """,
            
            "future_of_compatibility": """
**Modern Browser Era**

Modern browsers update automatically and frequently:
- Chrome updates every 4 weeks
- Firefox updates every 4 weeks
- Safari updates with macOS
- Edge updates every 4 weeks

This means fewer old browsers to worry about.

**Feature Flags**

Use feature flags to roll out new features:

```javascript
if (feature.isEnabled('newLayout')) {
  // New layout (might not work in all browsers)
} else {
  // Old layout (works everywhere)
}
```

Let your users opt-in to new features.
            """
        }
    },
    
    "key_takeaways": [
        "Different browsers have different feature support",
        "Use Can I Use to check feature compatibility",
        "Test on multiple real browsers and devices",
        "Use feature detection and polyfills",
        "Autoprefixer automatically handles CSS prefixes",
        "Progressive enhancement provides fallbacks",
        "Modern browsers reduce compatibility burden",
        "Decide your minimum supported browser version"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Check a feature on Can I Use",
            "Test your site on different browsers",
            "Use DevTools to simulate different browsers",
            "Add prefixes to CSS and test",
            "Write a polyfill for missing feature",
            "Configure .browserslistrc in a project"
        ]
    },
    
    "related_topics": [
        "Web Standards and W3C",
        "Developer Tools and DevTools",
        "Progressive Enhancement"
    ]
}
