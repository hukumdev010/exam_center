"""
Form Attributes and Validation - Detailed Content

This file contains comprehensive content for the "Form Attributes and Validation" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Form Attributes and Validation",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    HTML5 provides built-in form validation capabilities and attributes to enhance form functionality.
    This topic covers validation, accessibility attributes, and best practices for forms.
    """,
    
    "detailed_content": {
        "introduction": """
HTML5 introduced native form validation, reducing the need for JavaScript validation in many cases.
Understanding form attributes and validation helps create user-friendly, accessible forms that
improve user experience and reduce errors.
        """,
        
        "key_concepts": {
            "required_attribute": """
**Required Attribute**

Mark fields that must be filled:

```html
<input type="text" name="username" required>
<input type="email" name="email" required>
<textarea name="message" required></textarea>
```

- The browser will prevent form submission if required fields are empty
- The user sees a validation message automatically
- Works without any JavaScript
        """,
            
            "input_type_validation": """
**Built-in Input Type Validation**

HTML5 input types provide automatic validation:

```html
<!-- Email validation -->
<input type="email" name="email" required>

<!-- URL validation -->
<input type="url" name="website">

<!-- Number validation -->
<input type="number" name="age" min="0" max="120">

<!-- Date validation -->
<input type="date" name="birthdate">

<!-- Time validation -->
<input type="time" name="appointment-time">

<!-- Color picker -->
<input type="color" name="favorite-color">

<!-- File upload -->
<input type="file" name="document" accept=".pdf,.doc,.docx">

<!-- Range slider -->
<input type="range" name="satisfaction" min="1" max="10">
```

Each type has built-in validation and appropriate user interface elements.
        """,
            
            "min_max_attributes": """
**Min and Max Attributes**

Control the range of values for number and date inputs:

```html
<!-- Number range -->
<input type="number" name="quantity" min="1" max="100">

<!-- Date range -->
<input type="date" name="start-date" min="2024-01-01" max="2024-12-31">

<!-- Time range -->
<input type="time" name="work-start" min="08:00" max="17:00">

<!-- Range slider -->
<input type="range" name="volume" min="0" max="100" value="50">
```

The browser will prevent submission if values are outside the specified range.
        """,
            
            "pattern_attribute": """
**Pattern Attribute**

Use regex patterns for custom validation:

```html
<!-- Phone number (US format) -->
<input type="text" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" 
       placeholder="123-456-7890">

<!-- Postal code -->
<input type="text" name="zip" pattern="[0-9]{5}" placeholder="12345">

<!-- Username (letters, numbers, underscores) -->
<input type="text" name="username" pattern="[A-Za-z0-9_]+" required>

<!-- Custom message -->
<input type="text" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
       title="Phone format: 123-456-7890">
```

The pattern attribute allows you to define custom validation rules using regular expressions.
        """,
            
            "length_constraints": """
**Length Constraints**

Control the length of text input:

```html
<!-- Minimum length -->
<input type="text" name="password" minlength="8" required>

<!-- Maximum length -->
<input type="text" name="username" maxlength="20">

<!-- Both -->
<input type="text" name="code" minlength="6" maxlength="6" required>

<!-- For textarea -->
<textarea name="comment" minlength="10" maxlength="500"></textarea>
```

- `minlength`: Minimum number of characters required
- `maxlength`: Maximum number of characters allowed
- Browsers will prevent form submission if constraints are violated
        """,
            
            "placeholder_and_title": """
**Placeholder and Title Attributes**

Provide hints and help text:

```html
<input type="email" name="email" placeholder="you@example.com">

<input type="password" name="password" placeholder="Enter at least 8 characters">

<input type="text" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}"
       title="Format: 123-456-7890" placeholder="123-456-7890">

<textarea name="message" placeholder="Enter your message here..."></textarea>
```

- `placeholder`: Shows hint text that disappears when typing
- `title`: Shows tooltip on hover, used with pattern validation
        """,
            
            "disabled_readonly": """
**Disabled and ReadOnly Attributes**

Control field interaction:

```html
<!-- Disabled - user can't interact with field -->
<input type="text" name="system-id" value="SYS-12345" disabled>

<!-- ReadOnly - user can't change but can select/copy -->
<input type="text" name="confirmation-code" value="ABC123" readonly>

<!-- In a select -->
<select name="country">
    <option value="">Select a country</option>
    <option value="usa">United States</option>
    <option value="can" disabled>Canada (Unavailable)</option>
    <option value="mex">Mexico</option>
</select>
```

Difference:
- `disabled`: Field is not part of form submission
- `readonly`: Field is part of submission but can't be changed
        """,
            
            "datalist_autocomplete": """
**Datalist for Autocomplete**

Provide suggestions without a dropdown:

```html
<input type="text" name="browser" list="browsers" placeholder="Enter browser...">

<datalist id="browsers">
    <option value="Chrome">
    <option value="Firefox">
    <option value="Safari">
    <option value="Edge">
    <option value="Opera">
</datalist>
```

Users see suggestions as they type, but can enter any value.
        """,
            
            "form_attributes": """
**Important Form Attributes**

```html
<form id="contact-form" name="contact" action="/submit" method="POST" 
      enctype="multipart/form-data" novalidate>
    <!-- Form fields -->
    <input type="submit" value="Send">
</form>
```

- `id`: Unique identifier for the form
- `name`: Form name (used with JavaScript)
- `action`: URL where form data is sent
- `method`: HTTP method (GET or POST)
- `enctype`: Encoding type (important for file uploads: multipart/form-data)
- `novalidate`: Disable browser validation (if handling with JavaScript)
- `autocomplete`: Enable/disable autocomplete ("on" or "off")
        """,
            
            "fieldset_and_legend": """
**Grouping with Fieldset and Legend**

Organize related form fields:

```html
<form>
    <fieldset>
        <legend>Contact Information</legend>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </fieldset>
    
    <fieldset>
        <legend>Preferences</legend>
        <label>
            <input type="checkbox" name="subscribe"> Subscribe to newsletter
        </label>
        
        <label>
            <input type="checkbox" name="terms" required> 
            I agree to the terms
        </label>
    </fieldset>
    
    <button type="submit">Submit</button>
</form>
```

- `<fieldset>`: Groups related fields and disables them all together
- `<legend>`: Provides a caption for the fieldset
        """,
        }
    }
}
