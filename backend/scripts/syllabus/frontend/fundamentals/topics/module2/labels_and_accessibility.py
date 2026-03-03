"""
Labels and Accessibility - Detailed Content

This file contains comprehensive content for the "Labels and Accessibility" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Labels and Accessibility",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    Proper labels and accessibility practices ensure forms are usable by everyone, including people
    with disabilities. This topic covers labels, accessibility attributes, and best practices.
    """,
    
    "detailed_content": {
        "introduction": """
Accessible forms benefit all users, not just those with disabilities. Clear labels, proper associations,
and semantic HTML make forms easier to use, understand, and fill out. Accessibility is not just an
ethical imperative—it's often a legal requirement.
        """,
        
        "key_concepts": {
            "label_element": """
**The Label Element**

Always associate form inputs with labels:

```html
<!-- Method 1: Nested input -->
<label>
    Email:
    <input type="email" name="email" required>
</label>

<!-- Method 2: Using for attribute (preferred) -->
<label for="email-field">Email:</label>
<input type="email" id="email-field" name="email" required>

<!-- Label can come after input -->
<input type="checkbox" id="subscribe" name="subscribe">
<label for="subscribe">Subscribe to newsletter</label>
```

Key points:
- Always use `<label>` for form inputs
- Use `for` attribute to connect to input `id`
- Labels increase clickable area (better for accessibility)
- Screen readers read labels with inputs
        """,
            
            "implicit_explicit_labels": """
**Implicit vs Explicit Labels**

```html
<!-- Implicit (nested) -->
<label>
    Username:
    <input type="text" name="username">
</label>

<!-- Explicit (for/id) -->
<label for="username-field">Username:</label>
<input type="text" id="username-field" name="username">
```

Both work, but explicit labels are preferred for:
- Better compatibility with assistive technology
- More flexibility in layout
- Clearer code structure
        """,
            
            "required_optional_indicators": """
**Indicating Required vs Optional Fields**

```html
<!-- Using required attribute -->
<label for="name">Name: <span aria-label="required">*</span></label>
<input type="text" id="name" name="name" required>

<!-- Using text indication -->
<label for="name">Name (required)</label>
<input type="text" id="name" name="name" required>

<!-- Optional fields -->
<label for="phone">Phone (optional)</label>
<input type="tel" id="phone" name="phone">

<!-- Don't use only visual indicators -->
<!-- ✓ Good: Text and visual -->
Name <span style="color:red;">*</span>

<!-- ✗ Bad: Only color -->
<input type="text" style="border: 2px solid red;">
```

Always use both visual and text indicators for accessibility.
        """,
            
            "aria_labels": """
**ARIA Labels and Descriptions**

Use ARIA attributes for additional context:

```html
<!-- When visual label is not visible -->
<button aria-label="Close menu">×</button>

<!-- Describing input purpose -->
<label for="search">Search:</label>
<input type="text" id="search" name="search" 
       aria-describedby="search-help">
<small id="search-help">Search by name or email address</small>

<!-- Invalid input -->
<label for="email">Email:</label>
<input type="email" id="email" name="email" 
       aria-invalid="true" aria-describedby="email-error">
<div id="email-error" role="alert">
    Invalid email format
</div>

<!-- Loading state -->
<button type="submit" aria-busy="true">
    <span aria-hidden="true">⏳</span> Submitting...
</button>
```

Common ARIA attributes:
- `aria-label`: Alternative text for element
- `aria-labelledby`: Reference to labeling element
- `aria-describedby`: Reference to description
- `aria-invalid`: Whether input has error
- `aria-required`: Whether field is required
- `aria-hidden`: Hide from screen readers
- `aria-busy`: Loading state
- `role="alert"`: Announce updates to screen readers
        """,
            
            "help_text_descriptions": """
**Help Text and Descriptions**

Provide helpful context:

```html
<label for="password">Password:</label>
<input type="password" id="password" name="password" 
       aria-describedby="password-help" required>
<small id="password-help">
    At least 8 characters, include uppercase, lowercase, and number
</small>

<label for="phone">Phone:</label>
<input type="tel" id="phone" name="phone" 
       placeholder="123-456-7890"
       aria-describedby="phone-format" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}">
<small id="phone-format">Format: 123-456-7890</small>

<fieldset>
    <legend>Choose at least one interest:</legend>
    <small id="interests-help">We use this to personalize your experience</small>
    <label>
        <input type="checkbox" name="interests" value="news" 
               aria-describedby="interests-help">
        News
    </label>
    <label>
        <input type="checkbox" name="interests" value="updates" 
               aria-describedby="interests-help">
        Product Updates
    </label>
</fieldset>
```

Use `aria-describedby` to connect help text to form fields.
        """,
            
            "error_messages": """
**Accessible Error Messages**

```html
<label for="email">Email:</label>
<input type="email" id="email" name="email" required 
       aria-invalid="false" aria-describedby="email-error">
<div id="email-error" role="alert" style="color:red;display:none;">
    ✗ Please enter a valid email address
</div>

<script>
    document.getElementById('email').addEventListener('blur', (e) => {
        const errorDiv = document.getElementById('email-error');
        const isValid = e.target.validity.valid;
        
        e.target.setAttribute('aria-invalid', !isValid);
        errorDiv.style.display = isValid ? 'none' : 'block';
    });
</script>
```

Error messages should:
- Use `role="alert"` to announce to screen readers
- Be associated with input using `aria-describedby`
- Use clear, helpful language
- Suggest how to fix the problem
        """,
            
            "form_structure": """
**Form Structure for Accessibility**

```html
<form id="contact-form">
    <fieldset>
        <legend>Contact Information</legend>
        
        <div class="form-group">
            <label for="name">Name: <abbr title="required">*</abbr></label>
            <input type="text" id="name" name="name" required>
        </div>
        
        <div class="form-group">
            <label for="email">Email: <abbr title="required">*</abbr></label>
            <input type="email" id="email" name="email" required>
        </div>
        
        <div class="form-group">
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject">
        </div>
        
        <div class="form-group">
            <label for="message">Message: <abbr title="required">*</abbr></label>
            <textarea id="message" name="message" required></textarea>
        </div>
    </fieldset>
    
    <button type="submit">Send Message</button>
</form>
```

Best practices:
- Use `<fieldset>` to group related fields
- Use `<legend>` to describe groups
- Wrap each field in a container (like div)
- Each input needs a unique `id`
- Each label needs a corresponding `for` attribute
        """,
            
            "keyboard_navigation": """
**Keyboard Navigation**

```html
<!-- Define tab order -->
<form>
    <input type="text" name="name" tabindex="1">
    <input type="email" name="email" tabindex="2">
    <textarea name="message" tabindex="3"></textarea>
    <button type="submit" tabindex="4">Submit</button>
</form>

<!-- Skip links (advanced) -->
<a href="#main-content" style="position:absolute;left:-999px;">
    Skip to main content
</a>

<!-- Keyboard shortcuts -->
<button accesskey="s" type="submit">Submit (Alt+S)</button>
```

Considerations:
- Don't use `tabindex` unless necessary
- Allow keyboard access to all interactive elements
- Use `tabindex="0"` for elements normally not focusable
- Avoid positive `tabindex` values (breaks natural tab order)
        """,
        }
    }
}
