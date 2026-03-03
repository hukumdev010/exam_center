"""
Developer Tools and DevTools - Detailed Content

This file contains content for the "Developer Tools and DevTools" topic
from Module 1: Web Development Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Developer Tools and DevTools",
    "duration": "10-15 minutes",
    "difficulty": "Beginner",
    "overview": """
    Developer Tools (DevTools) are essential software for web development. Built into every modern browser,
    they allow you to inspect, debug, and optimize your web applications. Mastering DevTools is one of the
    most important skills for frontend developers.
    """,
    
    "detailed_content": {
        "introduction": """
If the browser is your platform, then DevTools is your workshop. These are built-in utilities in every modern browser
that let you:

- Inspect and modify HTML and CSS in real-time
- Debug JavaScript code with breakpoints and step execution
- Monitor network requests and performance
- Test responsive design on different devices
- Analyze memory and CPU usage
- Simulate mobile devices
- Test accessibility features

Professional developers spend hours in DevTools every day. Learning to use them effectively will dramatically improve
your productivity and your ability to debug problems.
        """,
        
        "key_concepts": {
            "accessing_devtools": """
**How to Open DevTools**

Most browsers follow the same shortcuts:

**Windows/Linux**:
- Press `F12`
- Or `Ctrl + Shift + I` (most browsers)
- Or right-click any element and select "Inspect Element"

**macOS**:
- Press `Cmd + Option + I`
- Or right-click and select "Inspect Element"

DevTools typically opens at the bottom or right side of your browser. You can detach it to a separate window or
move it to different positions.

**The Most Important Tab**: Right-click any element on a page and select "Inspect Element." This is the fastest way
to jump to an element in DevTools.
            """,
            
            "key_tabs": """
**The Elements/Inspector Tab**

This shows the HTML structure of the page and allows you to:
- View the complete HTML tree
- Inspect individual elements
- See applied CSS styles
- Edit HTML and CSS in real-time (changes aren't saved to your files)
- View computed styles and layout information
- Find elements by hovering

**The Console Tab**

A JavaScript playground where you can:
- See error messages and logs
- Execute JavaScript code
- Test code snippets
- Debug problems

Common uses:
```javascript
// View variables
console.log(user)

// Execute commands
document.querySelectorAll('.button').length

// Change the page
document.body.style.backgroundColor = 'red'
```

**The Network Tab**

Shows all HTTP requests and responses:
- What resources are being loaded (HTML, CSS, JS, images)
- How large each file is
- How long each request takes
- Response status codes (200, 404, 500, etc.)
- Response headers and bodies

This is invaluable for debugging why pages are slow or resources aren't loading.

**The Application Tab**

Inspect client-side storage:
- **Cookies**: See what data is stored
- **LocalStorage**: View persistent key-value data
- **SessionStorage**: View temporary session data
- **IndexedDB**: Inspect client-side databases

**The Performance Tab**

Analyze page load and runtime performance:
- Record a performance profile
- See what's taking the most time
- Identify bottlenecks
- Optimize rendering and JavaScript execution

**The Sources Tab**

A full JavaScript debugger:
- Set breakpoints in your code
- Step through code line by line
- Inspect variables at runtime
- Watch expressions change
- Execute code in the console in the context of a breakpoint

**Example Debugging Flow**:
1. Click on a line number to set a breakpoint
2. Perform an action that triggers the code
3. Execution pauses at the breakpoint
4. Inspect variables, step through code, see the call stack
5. Continue execution when ready
            """,
            
            "essential_skills": """
**Inspecting Elements**

Click the "Select Element" button (arrow icon) in the top-left of DevTools. Now hover over any element on the page
to see its HTML, CSS, applied styles, and layout information. This is the single most useful thing you'll do in DevTools.

**Modifying CSS in Real-Time**

In the Styles panel, click on any CSS property to edit it. Changes appear immediately on the page. This is perfect for
experimenting with designs before writing code.

Example: Click on a color value and change it to see what it looks like.

**Finding Layout Issues**

The Console will show you all errors and warnings. Look here first when something isn't working. Common errors:
- "Uncaught TypeError: Cannot read property X of undefined"
- "Failed to load resource: the server responded with a status of 404"
- "Access to XMLHttpRequest blocked by CORS policy"

**Responsive Design Testing**

Click the device toggle icon to switch to mobile view. You can:
- Test different screen sizes
- See how your layout responds
- Simulate touch events
- Test on specific devices (iPhone, iPad, Android)

**Performance Profiling**

For slow pages:
1. Open the Performance tab
2. Click Record
3. Interact with the page
4. Click Stop
5. Analyze what took the most time

This shows you whether JavaScript, rendering, or network requests are the bottleneck.

**Debugging a Slow Page**

1. Check the Network tab—is a resource loading slowly?
2. Check the Performance tab—is JavaScript taking too long?
3. Check the Console—are there errors or warnings?
4. Try disabling JavaScript or CSS to identify what's causing issues
            """,
            
            "advanced_features": """
**Conditional Breakpoints**

Instead of breaking on every execution, break only when a condition is true:
```javascript
// Right-click line number for conditional breakpoint
breakpoint: count > 10
```

**Debug Mobile Devices**

You can debug actual mobile devices:
- Android: Connect via USB, enable Developer Mode
- iOS: Use Safari to debug iOS devices

This is essential for testing real mobile behavior.

**Simulate Network Conditions**

Throttle your network speed to test on slow connections. Common presets:
- Fast 3G
- Slow 3G
- Offline

This helps you understand how your app performs for users on slow connections.

**Memory Profiling**

Check for memory leaks and excessive memory usage. Take heap snapshots and compare them to find what's consuming
memory.

**Accessibility Audit**

Run an accessibility audit to find issues like:
- Missing alt text on images
- Contrast problems
- Missing labels on form fields
- Keyboard navigation issues
            """
        }
    },
    
    "key_takeaways": [
        "DevTools is your most important development tool",
        "Press F12 to open DevTools instantly",
        "The Elements tab lets you inspect and modify HTML/CSS",
        "The Console is a JavaScript playground",
        "The Network tab shows all HTTP requests",
        "The Sources tab is a full JavaScript debugger",
        "Use Performance tab to identify bottlenecks",
        "Always check the Console for errors first"
    ],
    
    "further_exploration": {
        "practical_exercises": [
            "Open any website and press F12",
            "Inspect different elements on the page",
            "Try modifying CSS colors and seeing changes in real-time",
            "Check the Network tab and watch resources load",
            "Go to the Console and execute some JavaScript",
            "Set a breakpoint in JavaScript code and step through it",
            "Check the mobile responsive view for different screen sizes",
            "View what's stored in LocalStorage and Cookies"
        ],
        "discussion_questions": [
            "Why is the Network tab important for debugging?",
            "What's the difference between editing CSS in DevTools vs in your code?",
            "How would you use DevTools to find why a page is slow?",
            "Why is understanding the Console important for debugging?"
        ]
    },
    
    "related_topics": [
        "Code Editors and IDEs",
        "JavaScript Debugging",
        "Performance Optimization",
        "Responsive Design"
    ]
}
