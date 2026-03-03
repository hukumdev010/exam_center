"""
Performance Considerations - Detailed Content

This file contains content for the "Performance Considerations" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Performance Considerations",
    "duration": "8-10 minutes",
    "difficulty": "Beginner",
    "overview": """
    Web performance is about making sites fast. Slow websites frustrate users, lose revenue, and rank poorly in
    search results. Understanding basic performance concepts helps you build faster applications.
    """,
    
    "detailed_content": {
        "introduction": """
Every second counts on the web. If your site takes 3 seconds to load instead of 1 second, you lose 40% of users.
If it takes 10 seconds, 90% of people leave. Performance isn't a nice-to-have feature; it's essential.

Web performance includes many aspects: how fast pages load, how smooth they feel, how responsive they are to
interactions. Performance affects user satisfaction, SEO rankings, and business metrics.
        """,
        
        "key_concepts": {
            "why_performance_matters": """
**User Experience**

- Fast sites feel responsive
- Slow sites frustrate users
- Users judge sites on first impression
- Slow loading loses visitors immediately

**Business Metrics**

- 100ms delay = 1% sales decrease (Amazon)
- 1 second delay = 7% conversion loss (some studies)
- Page speed affects Google search rankings
- Mobile performance especially important

**Network Considerations**

- Not everyone has fast internet
- Mobile networks are slower than WiFi
- Users on 3G wait 10+ seconds for large pages
- International users experience latency

**Device Considerations**

- Old devices are slow
- Mobile processors less powerful than desktop
- Limited RAM on mobile devices
- Battery drain from heavy processing
            """,
            
            "performance_metrics": """
**Key Metrics**

**Loading Performance**

- **FCP (First Contentful Paint)**: When first content appears (goal: < 1.8s)
- **LCP (Largest Contentful Paint)**: When main content loads (goal: < 2.5s)
- **Load Time**: When page fully loads

**Interactivity**

- **FID (First Input Delay)**: Delay from user input to response (goal: < 100ms)
- **INP (Interaction to Next Paint)**: Responsiveness to interactions

**Visual Stability**

- **CLS (Cumulative Layout Shift)**: How much layout moves (goal: < 0.1)
- Unexpected layout shifts are annoying

**Measuring Performance**

Use **Lighthouse** in DevTools:
1. Open DevTools
2. Go to Lighthouse tab
3. Run audit
4. See performance score and suggestions

Google PageSpeed Insights also measures performance.

**Real User Monitoring**

Tools like:
- Google Analytics
- Sentry
- Datadog

Track real user experience, not just lab measurements.
            """,
            
            "optimization_techniques": """
**Reduce File Sizes**

**Code Minification**:
```javascript
// Original
function addNumbers(a, b) {
  return a + b;
}

// Minified
function addNumbers(a,b){return a+b}
```

Minified code is smaller but harder to read. Only minify production builds.

**Compression**:
- GZIP compression reduces file sizes 50-80%
- Brotli compression even better
- Servers automatically compress text files

**Image Optimization**:
- Serve appropriately sized images
- Use modern formats (WebP instead of JPG)
- Compress images
- Use SVG for icons and logos

```html
<!-- Responsive images -->
<img 
  src="image-small.jpg"
  srcset="image-small.jpg 500w, image-large.jpg 1000w"
  alt="Description"
/>
```

**Lazy Loading**

Load resources only when needed:

```html
<!-- Lazy load images -->
<img src="image.jpg" loading="lazy" />

<!-- Lazy load scripts -->
<script async src="script.js"></script>
```

**Code Splitting**

Load only code needed for current page:

```javascript
// Import only when needed
const module = await import('./heavy-module.js');
```

**Caching**

Store files locally to avoid re-downloading:

```javascript
// Cache images, CSS, JavaScript
// Set Cache-Control headers
Cache-Control: max-age=31536000  // 1 year
```

Service Workers cache resources offline.

**Async and Defer**

Control when JavaScript loads:

```html
<!-- Render blocking - waits -->
<script src="script.js"></script>

<!-- Async - load in background -->
<script async src="script.js"></script>

<!-- Defer - load but wait to execute -->
<script defer src="script.js"></script>
```
            """,
            
            "common_issues": """
**Render-Blocking Resources**

CSS and JavaScript can block page rendering. Optimize:

- Load CSS in head
- Load JavaScript at end of body
- Use async/defer for non-critical scripts
- Inline critical CSS
- Defer non-critical CSS

**Large Bundles**

Modern JavaScript frameworks can create huge bundles:

- React: ~42KB
- Vue: ~33KB
- Angular: ~130KB

Add tree-shaking and code splitting to reduce size.

**Unoptimized Images**

Images are usually the biggest assets:

- Average website is 50% images by size
- Compress ruthlessly
- Use appropriate dimensions
- Consider WebP format

**Inefficient JavaScript**

Bad JavaScript performs poorly:

- Unnecessary re-renders
- Memory leaks
- Long-running operations
- Too many event listeners
            """,
            
            "best_practices": """
**Development Habits**

- Test performance early and often
- Use Lighthouse regularly
- Monitor Core Web Vitals
- Profile with DevTools Performance tab
- Set performance budgets
- Use production builds for testing

**Tools for Performance**

- **Webpack Bundle Analyzer**: See bundle size breakdown
- **Lighthouse**: Google's performance audit
- **WebPageTest**: Detailed performance analysis
- **Sentry**: Error tracking and performance

**Progressive Enhancement**

- Send fast initial page
- Add enhancements progressively
- Works without JavaScript
- Enhanced with JavaScript

This ensures site works even if slow connections or script fails.
            """
        }
    },
    
    "key_takeaways": [
        "Performance dramatically affects user experience",
        "Measure performance with Lighthouse and Core Web Vitals",
        "Optimize images—they're usually the largest assets",
        "Use code minification, compression, and lazy loading",
        "Reduce JavaScript bundle size",
        "Test performance on slow networks",
        "Monitor real user performance",
        "Performance optimization is ongoing, not one-time"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Run Lighthouse audit on any website",
            "Optimize images and compare file sizes",
            "Minify your CSS and JavaScript",
            "Set up lazy loading for images",
            "Profile JavaScript in DevTools Performance tab",
            "Check Core Web Vitals for a website"
        ]
    },
    
    "related_topics": [
        "Production vs Development",
        "Developer Tools and DevTools",
        "Web Performance Best Practices"
    ]
}
