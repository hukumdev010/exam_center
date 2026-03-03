"""
Validation and Testing - Detailed Content

This file contains comprehensive content for the "Validation and Testing" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Validation and Testing",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Proper validation and testing of HTML ensures your code follows standards, is accessible,
    and works correctly across browsers. This topic covers validation tools, testing strategies,
    and quality assurance practices.
    """,
    
    "detailed_content": {
        "introduction": """
Validation and testing are essential parts of professional web development. They ensure your HTML
is standards-compliant, accessible, performant, and works correctly across different browsers
and devices.
        """,
        
        "key_concepts": {
            "html_validation": """
**HTML Validation**

HTML validation checks if your code follows HTML5 standards:

```html
<!-- Invalid - Unclosed tag -->
<div>Content

<!-- Valid -->
<div>Content</div>

<!-- Invalid - Nesting -->
<p>Text <div>content</div></p>

<!-- Valid -->
<div>Text <p>content</p></div>

<!-- Invalid - Wrong element -->
<button href="/">Link Button</button>

<!-- Valid -->
<a href="/">Link</a>
```

Tools for validation:

1. **W3C HTML Validator**
   - https://validator.w3.org
   - Official validator from W3C
   - Check URL, upload file, or paste code
   - Shows errors and warnings

2. **VS Code Built-in Validation**
   - Works as you type
   - Install extensions for more features
   - Shows errors in Problems panel

3. **Command Line Tools**
   ```bash
   npm install -g html-validate
   html-validate index.html
   ```

4. **Browser DevTools**
   - F12 / Right-click → Inspect
   - Check Console for errors
   - Check Elements for structure
        """,
            
            "accessibility_testing": """
**Accessibility Testing**

Test if your site is accessible to everyone:

```html
<!-- Good for accessibility -->
<form>
  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>
  
  <label for="password">Password:</label>
  <input type="password" id="password" name="password" required>
  
  <button type="submit">Log In</button>
</form>

<!-- Poor accessibility -->
<form>
  <input type="text" placeholder="Email">
  <input type="password" placeholder="Password">
  <button>Log In</button>
</form>
```

Testing tools:

1. **Lighthouse (Chrome DevTools)**
   - F12 → Lighthouse tab
   - Audit page for accessibility
   - Get score and recommendations

2. **WAVE (Web Accessibility Evaluation Tool)**
   - wave.webaim.org
   - Browser extension available
   - Shows accessibility issues

3. **axe DevTools**
   - Browser extension
   - Finds accessibility issues
   - Shows how to fix them

4. **Screen Reader Testing**
   - NVDA (Windows) - Free
   - JAWS (Windows) - Paid
   - VoiceOver (macOS/iOS) - Built-in
   - TalkBack (Android) - Built-in

Manual testing:
- Navigate with keyboard only (Tab key)
- Use screen reader
- Test with browser zoom
- Check color contrast
- Test with various window sizes
        """,
            
            "cross_browser_testing": """
**Cross-Browser Testing**

Test your site on different browsers:

```html
<!-- Use feature detection for compatibility -->
<video id="video" controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <p>Your browser doesn't support HTML5 video.</p>
</video>

<!-- Use graceful degradation -->
<input type="date">
<!-- Falls back to text input on unsupported browsers -->

<!-- Add polyfills for missing features -->
<script src="https://polyfill.io/v3/polyfill.min.js"></script>
```

Browsers to test:
- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (macOS and iOS)
- Edge (Windows)
- Opera (if relevant to audience)

Testing tools:

1. **BrowserStack**
   - Cloud-based testing
   - Test on real devices
   - Paid service

2. **Sauce Labs**
   - Cloud-based testing
   - Automated and manual
   - Paid service

3. **Local Testing**
   - Install browsers locally
   - Virtual machines
   - Free but time-consuming

4. **Browser APIs for Testing**
   ```javascript
   // Detect browser capabilities
   if (navigator.geolocation) {
       // Geolocation supported
   }
   
   if ('serviceWorker' in navigator) {
       // Service Workers supported
   }
   ```
        """,
            
            "responsive_testing": """
**Responsive Design Testing**

Test on different screen sizes:

```html
<!-- Proper viewport configuration -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Media queries for responsive design -->
<style>
  body {
    font-size: 16px;
  }
  
  @media (max-width: 768px) {
    body {
      font-size: 14px;
    }
  }
  
  @media (max-width: 480px) {
    body {
      font-size: 12px;
    }
  }
</style>
```

Screen sizes to test:
- Desktop: 1920x1080, 1440x900, 1024x768
- Tablet: 768x1024 (iPad)
- Mobile: 375x667 (iPhone SE), 414x896 (iPhone 12), 360x800 (Android)

Testing tools:

1. **Chrome DevTools**
   - F12 → Device Toolbar
   - Toggle device mode
   - Test various device sizes

2. **Firefox DevTools**
   - F12 → Responsive Design Mode
   - Similar to Chrome

3. **Physical Devices**
   - Test on real phones/tablets
   - Most accurate testing

4. **Browserstack/Sauce Labs**
   - Test on real devices in cloud
        """,
            
            "performance_testing": """
**Performance Testing**

Test page load speed and performance:

```html
<!-- Optimize for performance -->
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Preload critical resources -->
  <link rel="preload" href="font.woff2" as="font" type="font/woff2" crossorigin>
  
  <!-- Defer non-critical scripts -->
  <script src="script.js" defer></script>
</head>

<body>
  <!-- Lazy load images -->
  <img src="image.jpg" loading="lazy" alt="Description">
</body>
```

Testing tools:

1. **Lighthouse (Chrome DevTools)**
   - F12 → Lighthouse
   - Performance score
   - Detailed recommendations

2. **Google PageSpeed Insights**
   - pagespeed.web.dev
   - Mobile and desktop scores
   - Field and lab data

3. **WebPageTest**
   - webpagetest.org
   - Detailed waterfall chart
   - Multiple location testing

4. **GTmetrix**
   - gtmetrix.com
   - Performance recommendations
   - Video of page load

Metrics to track:
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Cumulative Layout Shift (CLS)
- Core Web Vitals
- Page size
- Number of requests
        """,
            
            "testing_checklist": """
**HTML Testing Checklist**

Before launching:

✅ **Validation**
- [ ] Run through W3C validator
- [ ] No console errors
- [ ] No warnings in DevTools

✅ **Accessibility**
- [ ] All images have alt text
- [ ] All form fields have labels
- [ ] Headings are in order (h1 → h2 → h3)
- [ ] Links have descriptive text
- [ ] Color contrast is sufficient
- [ ] Keyboard navigation works
- [ ] Tested with screen reader

✅ **Cross-Browser**
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers

✅ **Responsive**
- [ ] Desktop (1920px, 1440px)
- [ ] Tablet (768px)
- [ ] Mobile (375px, 414px)
- [ ] Touch targets are large enough

✅ **Performance**
- [ ] Lighthouse score 90+
- [ ] Load time < 3 seconds
- [ ] Images optimized
- [ ] No unused CSS/JS

✅ **SEO**
- [ ] Title is descriptive
- [ ] Meta description present
- [ ] Canonical URL set
- [ ] Open Graph tags present
- [ ] Structured data valid

✅ **Security**
- [ ] No inline styles/scripts
- [ ] External resources from HTTPS
- [ ] No sensitive data in HTML
- [ ] Forms validate input

✅ **Content**
- [ ] No typos or grammar errors
- [ ] All links work
- [ ] Images load correctly
- [ ] Forms submit properly
- [ ] No broken functionality
        """,
            
            "automated_testing": """
**Automated Testing**

```bash
# HTML validation with npm
npm install --save-dev html-validate
npm run validate

# Accessibility testing with axe
npm install --save-dev @axe-core/cli
axe https://example.com

# Performance testing with Lighthouse
npm install --save-dev @lhci/cli@0.8.x @lhci/server@0.8.x
lhci autorun
```

Configuration file (.lighthouserc.json):
```json
{
  "ci": {
    "collect": {
      "url": ["http://localhost:3000/"],
      "numberOfRuns": 3
    },
    "upload": {
      "target": "temporary-public-storage"
    }
  }
}
```

Benefits of automated testing:
- Catch errors early
- Consistent results
- Part of CI/CD pipeline
- Prevents regressions
- Saves time in long run
        """,
        }
    }
}
