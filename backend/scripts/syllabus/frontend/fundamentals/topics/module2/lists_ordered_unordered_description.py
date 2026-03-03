"""
Lists (Ordered, Unordered, Description) - Detailed Content

This file contains comprehensive content for the "Lists" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Lists (Ordered, Unordered, Description)",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    HTML provides three types of lists for organizing and presenting information. This topic covers
    how to use each type correctly and when to apply them.
    """,
    
    "detailed_content": {
        "introduction": """
Lists are one of the most commonly used HTML elements. They're used to organize related items and
improve both readability and semantic structure. Choosing the right list type is important for
accessibility and search engine optimization.
        """,
        
        "key_concepts": {
            "unordered_lists": """
**Unordered Lists**

Unordered lists (bulleted lists) are used for items in no particular order:

```html
<ul>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
</ul>
```

- `<ul>`: Unordered list container
- `<li>`: Individual list item

By default, unordered lists display with bullet points. You can change the marker style with CSS:

```css
ul {
    list-style-type: square;  /* square, circle, disc, none */
}
```

Use unordered lists for:
- Shopping lists
- Feature lists
- Navigation menus
- Sets of related items with no order
        """,
            
            "ordered_lists": """
**Ordered Lists**

Ordered lists (numbered lists) are used for items in a specific sequence:

```html
<ol>
    <li>First step</li>
    <li>Second step</li>
    <li>Third step</li>
</ol>
```

- `<ol>`: Ordered list container
- `<li>`: Individual list item

You can customize ordered lists:

```html
<ol start="5">
    <li>Fifth item</li>
    <li>Sixth item</li>
</ol>

<ol type="A">
    <li>Item A</li>
    <li>Item B</li>
</ol>
```

Attributes:
- `start`: Starting number (default is 1)
- `type`: Number style (1, a, A, i, I)
- `reversed`: Reverse the counting order

Use ordered lists for:
- Step-by-step instructions
- Ranked items
- Numbered procedures
- Sequences that have a logical order
        """,
            
            "description_lists": """
**Description Lists**

Description lists (definition lists) pair terms with their descriptions:

```html
<dl>
    <dt>HTML</dt>
    <dd>HyperText Markup Language</dd>
    
    <dt>CSS</dt>
    <dd>Cascading Style Sheets</dd>
    
    <dt>JavaScript</dt>
    <dd>A programming language that enables interactive web pages</dd>
</dl>
```

- `<dl>`: Description list container
- `<dt>`: Definition term
- `<dd>`: Definition or description

You can have multiple definitions for a single term:

```html
<dl>
    <dt>Apple</dt>
    <dd>A red fruit</dd>
    <dd>A technology company</dd>
</dl>
```

Use description lists for:
- Glossaries
- FAQ sections (question/answer pairs)
- Key-value pairs
- Terms and definitions
        """,
            
            "nested_lists": """
**Nested Lists**

You can nest lists within other lists:

```html
<ul>
    <li>Frontend
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </li>
    <li>Backend
        <ul>
            <li>Python</li>
            <li>JavaScript (Node.js)</li>
            <li>Java</li>
        </ul>
    </li>
</ul>
```

Tips for nesting:
- Keep nesting levels reasonable (2-3 deep is usually sufficient)
- Use consistent list types when nesting
- Ensure proper indentation for readability
- Each nested list must be inside a `<li>` element
        """,
            
            "best_practices": """
**Best Practices**

1. **Use semantic list elements** - Don't use divs or custom structures for lists
2. **Use the correct list type** - Match the list type to your content
3. **Keep lists simple** - Very long lists should be paginated or filtered
4. **Use CSS for styling** - Never use HTML attributes for visual styling alone
5. **Make lists accessible** - Screen readers rely on proper list markup
6. **Validate your HTML** - Ensure proper nesting and structure
        """,
        }
    }
}
