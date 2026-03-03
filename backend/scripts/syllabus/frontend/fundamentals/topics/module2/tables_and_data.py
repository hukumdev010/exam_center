"""
Tables and Data - Detailed Content

This file contains comprehensive content for the "Tables and Data" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Tables and Data",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    HTML tables are used to display tabular data in rows and columns. This topic covers the structure,
    accessibility, and proper use of HTML tables.
    """,
    
    "detailed_content": {
        "introduction": """
Tables are designed specifically for displaying tabular data - information that naturally fits into
rows and columns. Tables should never be used for page layout (that's what CSS is for). When used
correctly, tables are accessible, semantic, and maintainable.
        """,
        
        "key_concepts": {
            "table_structure": """
**Basic Table Structure**

```html
<table>
    <thead>
        <tr>
            <th>Header 1</th>
            <th>Header 2</th>
            <th>Header 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1, Cell 1</td>
            <td>Row 1, Cell 2</td>
            <td>Row 1, Cell 3</td>
        </tr>
        <tr>
            <td>Row 2, Cell 1</td>
            <td>Row 2, Cell 2</td>
            <td>Row 2, Cell 3</td>
        </tr>
    </tbody>
    <tfoot>
        <tr>
            <th>Total</th>
            <td>Value 1</td>
            <td>Value 2</td>
        </tr>
    </tfoot>
</table>
```

Key elements:
- `<table>`: Container for the entire table
- `<thead>`: Table header (rows with column headings)
- `<tbody>`: Table body (main data rows)
- `<tfoot>`: Table footer (summary or totals)
- `<tr>`: Table row
- `<th>`: Table header cell
- `<td>`: Table data cell
        """,
            
            "table_headers": """
**Table Headers**

Always use `<th>` for header cells, not `<td>`:

```html
<!-- Good -->
<thead>
    <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
    </tr>
</thead>

<!-- Bad - using td for headers -->
<thead>
    <tr>
        <td>Name</td>
        <td>Age</td>
        <td>City</td>
    </tr>
</thead>
```

Benefits of using `<th>`:
- Better semantics for screen readers
- Headers are styled differently by browsers
- Can be associated with data cells for accessibility
        """,
            
            "table_captions_and_summaries": """
**Table Captions and Summaries**

Add captions to provide context:

```html
<table>
    <caption>Monthly Sales Data 2024</caption>
    <thead>
        <tr>
            <th>Month</th>
            <th>Sales</th>
            <th>Growth</th>
        </tr>
    </thead>
    <tbody>
        <!-- rows -->
    </tbody>
</table>
```

For complex tables, add a summary:

```html
<table summary="Sales data by month, showing monthly totals and growth percentages">
    <!-- table content -->
</table>
```

Use `<caption>` for a visible table title and `summary` attribute for additional context for screen readers.
        """,
            
            "colspan_and_rowspan": """
**Spanning Columns and Rows**

Cells can span multiple columns or rows:

```html
<table>
    <thead>
        <tr>
            <th colspan="2">Personal Information</th>
            <th colspan="2">Contact Details</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>First Name</td>
            <td>Last Name</td>
            <td>Email</td>
            <td>Phone</td>
        </tr>
        <tr>
            <td>John</td>
            <td>Doe</td>
            <td rowspan="2">john@example.com</td>
            <td>555-1234</td>
        </tr>
        <tr>
            <td>Jane</td>
            <td>Smith</td>
            <td>555-5678</td>
        </tr>
    </tbody>
</table>
```

- `colspan`: Number of columns a cell spans
- `rowspan`: Number of rows a cell spans
        """,
            
            "table_accessibility": """
**Making Tables Accessible**

Proper table markup is crucial for accessibility:

1. **Use scope attribute** to associate headers with data:

```html
<table>
    <tr>
        <th scope="col">Month</th>
        <th scope="col">Sales</th>
    </tr>
    <tr>
        <th scope="row">January</th>
        <td>$5,000</td>
    </tr>
</table>
```

2. **Add id and headers attributes** for complex tables:

```html
<table>
    <tr>
        <th id="name">Name</th>
        <th id="email">Email</th>
    </tr>
    <tr>
        <td headers="name">John</td>
        <td headers="email">john@example.com</td>
    </tr>
</table>
```

3. **Provide context** with captions and summaries

4. **Keep tables simple** - Very complex tables are hard to navigate
        """,
            
            "when_not_to_use_tables": """
**When NOT to Use Tables**

Never use tables for:
- **Page layouts**: Tables were historically used for layout before CSS existed. Always use CSS Grid or Flexbox instead.
- **Data visualization**: Use a charting library instead
- **Responsive design**: Tables don't work well on mobile devices

Using tables for layout is:
- Semantically wrong
- Bad for accessibility
- Difficult to maintain
- Slow to load
- Not responsive

Always ask: "Is this truly tabular data?" If not, don't use a table.
        """,
            
            "responsive_tables": """
**Making Tables Responsive**

Since tables don't resize well on mobile, consider alternatives:

```css
/* Allow horizontal scrolling on small screens */
@media (max-width: 768px) {
    table {
        display: block;
        overflow-x: auto;
    }
}

/* Or convert to vertical layout */
@media (max-width: 768px) {
    table, thead, tbody, tr, th, td {
        display: block;
    }
    
    tr {
        margin-bottom: 1rem;
    }
    
    td::before {
        content: attr(data-label);
        font-weight: bold;
        display: block;
    }
}
```

Use data attributes to label cells on mobile:

```html
<td data-label="Sales">$5,000</td>
```
        """,
        }
    }
}
