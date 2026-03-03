"""
Text Formatting Elements - Detailed Content

This file contains comprehensive content for the "Text Formatting Elements" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Text Formatting Elements",
    "duration": "45-60 minutes",
    "difficulty": "Beginner",
    "overview": """
    HTML provides various elements to format and semantically describe text content. This topic covers
    both structural and presentational text formatting elements and when to use each.
    """,
    
    "detailed_content": {
        "introduction": """
HTML offers many ways to format and style text. It's important to distinguish between semantic
(meaning-based) elements and purely presentational ones. Semantic elements carry meaning that helps
assistive technologies and search engines understand your content better.
        """,
        
        "key_concepts": {
            "heading_elements": """
**Heading Elements**

HTML provides six heading levels, from `<h1>` to `<h6>`:

```html
<h1>Main heading</h1>
<h2>Secondary heading</h2>
<h3>Tertiary heading</h3>
```

Best practices:
- Use `<h1>` only once per page for the main title
- Use headings in order (don't jump from h1 to h3)
- Use them for document structure, not just styling
- Each heading should have a logical hierarchy
        """,
            
            "emphasis_and_importance": """
**Emphasis and Strong Importance**

Use `<em>` for emphasis and `<strong>` for strong importance:

```html
<p>This is <em>emphasized</em> text.</p>
<p>This is <strong>important</strong> text.</p>
```

- `<em>` (emphasis): Used for text you want to stress. Screen readers will emphasize it.
- `<strong>` (strong): Used for content of strong importance. Screen readers will read it with strong emphasis.

Don't use `<i>` or `<b>` for emphasis in modern HTML. They're purely presentational.
        """,
            
            "semantic_vs_presentational": """
**Semantic vs Presentational Elements**

Semantic elements describe the meaning of content:
- `<strong>`: Important content
- `<em>`: Emphasized content
- `<mark>`: Highlighted text
- `<code>`: Computer code
- `<kbd>`: Keyboard input
- `<samp>`: Output from a computer program

Presentational elements just style text (avoid these - use CSS instead):
- `<b>`: Bold (no semantic meaning)
- `<i>`: Italic (no semantic meaning)

Always prefer semantic elements. They improve accessibility and are more meaningful to search engines.
        """,
            
            "special_text_elements": """
**Special Text Elements**

```html
<p>This is <mark>highlighted</mark> text.</p>
<p>The formula is <var>E</var> = <var>mc</var><sup>2</sup></p>
<p>H<sub>2</sub>O is water.</p>
<p>This text is <del>deleted</del> and <ins>inserted</ins>.</p>
<p><small>This is small print.</small></p>
```

- `<mark>`: Highlighted or referenced text
- `<code>`: Computer code snippets
- `<kbd>`: Keyboard or user input
- `<samp>`: Output from a computer program
- `<var>`: Variables or placeholders
- `<sup>`: Superscript (like exponents)
- `<sub>`: Subscript (like chemical formulas)
- `<del>`: Deleted text (shows strikethrough)
- `<ins>`: Inserted text (shows underline)
- `<small>`: Fine print or small text
        """,
            
            "quotations": """
**Quotation Elements**

```html
<blockquote cite="https://example.com">
    <p>This is a block-level quote from another source.</p>
</blockquote>

<p>This is a quote: <q cite="https://example.com">inline quotation</q></p>

<p><cite>The Title of the Work</cite> by Author Name</p>
```

- `<blockquote>`: A block-level quotation
- `<q>`: An inline quotation
- `<cite>`: The title of a work or name of an author
- `cite` attribute: URL to the source of the quotation
        """,
            
            "preformatted_text": """
**Preformatted Text**

The `<pre>` element preserves whitespace and line breaks:

```html
<pre>
    This text
        maintains its
            formatting
</pre>
```

Useful for code samples, ASCII art, or any text where spacing matters.
        """,
        }
    }
}
