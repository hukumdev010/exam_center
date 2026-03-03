"""
Attributes and Data Attributes - Detailed Content

This file contains comprehensive content for the "Attributes and Data Attributes" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Attributes and Data Attributes",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    HTML attributes provide additional information about elements. Data attributes (data-*) allow
    you to store custom data on elements for use by JavaScript. This topic covers both.
    """,
    
    "detailed_content": {
        "introduction": """
Attributes are key-value pairs that modify HTML elements. While standard attributes like id, class,
and style are well-known, HTML5 introduced data attributes that allow developers to store custom
data on elements without conflicting with standard attributes.
        """,
        
        "key_concepts": {
            "standard_attributes": """
**Standard HTML Attributes**

Common attributes that work on all elements:

```html
<!-- Global attributes -->
<div id="main-content" class="container primary" style="color: blue;">
    Content here
</div>

<!-- Title tooltip -->
<button title="Click to save your changes">Save</button>

<!-- Language -->
<p lang="en">This is English</p>

<!-- Hidden element -->
<div hidden>This won't be visible</div>

<!-- Tab order -->
<input tabindex="1">
<input tabindex="2">

<!-- Access key -->
<a href="#" accesskey="s" onclick="save()">Save (Alt+S)</a>

<!-- Disable spell check -->
<textarea spellcheck="false"></textarea>

<!-- Drag and drop -->
<div draggable="true">Drag me</div>

<!-- Content editable -->
<div contenteditable="true">Edit this text</div>
```

Standard global attributes:
- `id`: Unique identifier
- `class`: CSS class names
- `style`: Inline CSS styles
- `title`: Tooltip text
- `lang`: Language of content
- `hidden`: Hide element
- `tabindex`: Tab order
- `accesskey`: Keyboard shortcut
        """,
            
            "data_attributes": """
**Data Attributes (data-*)**

Store custom data on elements:

```html
<!-- Basic data attributes -->
<div id="user-1" data-user-id="123" data-user-role="admin" data-created="2024-01-15">
    John Doe
</div>

<!-- Multiple data on one element -->
<button 
    data-action="delete" 
    data-item-id="456" 
    data-item-type="post"
    data-confirm-message="Are you sure?"
    data-severity="high">
    Delete Post
</button>

<!-- Useful for filtering -->
<div data-category="tech" data-date="2024-12-11" data-featured="true">
    Article
</div>

<!-- Storing JSON data -->
<div data-user='{"id": 123, "name": "John", "role": "admin"}'>
    User
</div>
```

Rules:
- Must start with "data-"
- Can contain lowercase letters, numbers, hyphens, dots, colons
- Value can be any string
- Case-insensitive (data-userid, data-userId treated the same)
        """,
            
            "accessing_data_attributes": """
**Accessing Data Attributes with JavaScript**

```html
<div id="product" data-id="789" data-price="29.99" data-in-stock="true">
    Product Name
</div>

<script>
    const product = document.getElementById('product');
    
    // Using getAttribute
    console.log(product.getAttribute('data-id')); // "789"
    console.log(product.getAttribute('data-price')); // "29.99"
    
    // Using dataset (preferred)
    console.log(product.dataset.id); // "789"
    console.log(product.dataset.price); // "29.99"
    console.log(product.dataset.inStock); // "true"
    
    // Setting data attributes
    product.dataset.discount = "15%";
    product.setAttribute('data-discount', '15%');
    
    // Iterating all data attributes
    Object.entries(product.dataset).forEach(([key, value]) => {
        console.log(key + ': ' + value);
    });
</script>
```

Important:
- `dataset.propertyName` automatically converts from kebab-case to camelCase
- `data-user-name` becomes `dataset.userName`
- Data attributes always return strings
- Use parseInt(), parseFloat() to convert types
        """,
            
            "data_attributes_use_cases": """
**Common Use Cases for Data Attributes**

```html
<!-- 1. Storing IDs for CRUD operations -->
<button data-post-id="123" onclick="deletePost(this)">Delete</button>

<script>
function deletePost(button) {
    const postId = button.dataset.postId;
    fetch(`/api/posts/${postId}`, { method: 'DELETE' });
}
</script>

<!-- 2. Configuration data -->
<div data-chart-type="bar" data-chart-data="[1,2,3,4,5]">
    Loading chart...
</div>

<!-- 3. Sorting and filtering -->
<div class="products">
    <div data-price="50" data-category="electronics" data-rating="4.5">
        Laptop
    </div>
    <div data-price="20" data-category="books" data-rating="4.8">
        Book
    </div>
</div>

<!-- 4. Feature flags -->
<button data-experimental="true" data-beta-feature="true">
    Try Beta Feature
</button>

<!-- 5. Analytics tracking -->
<a href="/product" data-event-name="product-click" data-product-id="123">
    View Product
</a>

<script>
document.addEventListener('click', (e) => {
    if (e.target.dataset.eventName) {
        analytics.track(e.target.dataset.eventName, {
            productId: e.target.dataset.productId
        });
    }
});
</script>

<!-- 6. Tooltips and hints -->
<input type="text" data-tooltip="Enter your email address" 
       data-tooltip-position="top">

<!-- 7. Storing parsed JSON -->
<div data-config='{"theme":"dark","notifications":true}'>
    Settings
</div>
```
        """,
            
            "data_attributes_best_practices": """
**Best Practices**

✅ **Do:**
- Use semantic, descriptive names
- Keep data minimal (store IDs, not entire objects)
- Use lowercase with hyphens
- Document what data your page uses
- Validate data on the server

❌ **Don't:**
- Store large amounts of data (use API calls instead)
- Duplicate data from attributes
- Use for styling (use class or style attributes)
- Rely on data attributes for security
- Store sensitive information

```html
<!-- Good -->
<article data-article-id="123" data-author-id="456">
    <h2>Article Title</h2>
</article>

<!-- Bad - too much data -->
<article data-article='{"id":123,"title":"...","author":{...},"comments":[...]}'>

<!-- Bad - duplicates class info -->
<div data-theme="dark" class="dark">
    <!-- class is enough -->
</div>
```
        """,
            
            "html5_attributes": """
**Important HTML5 Attributes**

```html
<!-- Autocomplete -->
<input type="email" autocomplete="email">
<input type="password" autocomplete="current-password">

<!-- Multiple attribute on select -->
<select name="colors" multiple>
    <option>Red</option>
    <option>Green</option>
    <option>Blue</option>
</select>

<!-- Download attribute -->
<a href="file.pdf" download="document.pdf">
    Download PDF
</a>

<!-- Controls attribute -->
<video src="video.mp4" controls></video>
<audio src="audio.mp3" controls></audio>

<!-- Autoplay, loop, muted -->
<video src="video.mp4" autoplay loop muted></video>

<!-- Poster image for video -->
<video src="video.mp4" poster="thumbnail.jpg" controls></video>

<!-- Async and defer for scripts -->
<script src="script.js" async></script>
<script src="important.js" defer></script>

<!-- Loading attribute (lazy loading) -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Intrinsic size hints -->
<img src="image.jpg" width="800" height="600" alt="Description">

<!-- Disabled state -->
<button disabled>Can't click</button>
<input type="text" disabled>

<!-- Autofocus -->
<input type="text" autofocus>
```

These attributes enhance functionality without JavaScript.
        """,
        }
    }
}
