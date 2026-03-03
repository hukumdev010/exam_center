"""
Input Types - Detailed Content

This file contains comprehensive content for the "Input Types" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Input Types",
    "duration": "60-75 minutes",
    "difficulty": "Intermediate",
    "overview": """
    HTML5 introduced many new input types that provide native validation, appropriate keyboards,
    and enhanced user experience. This topic covers all available input types and their use cases.
    """,
    
    "detailed_content": {
        "introduction": """
HTML5 provides specialized input types for different data formats. Using the correct input type
improves user experience by showing appropriate keyboards on mobile devices, provides native validation,
and makes forms more accessible.
        """,
        
        "key_concepts": {
            "text_inputs": """
**Text-Based Input Types**

```html
<!-- Standard text -->
<input type="text" name="username">

<!-- Password (masked) -->
<input type="password" name="password">

<!-- Email with validation -->
<input type="email" name="email">

<!-- URL with validation -->
<input type="url" name="website">

<!-- Search (browser may show recent searches) -->
<input type="search" name="query">

<!-- Telephone (doesn't validate format, just provides phone keyboard) -->
<input type="tel" name="phone">
```

Each type provides appropriate keyboard on mobile devices and may include validation.
        """,
            
            "numeric_inputs": """
**Numeric Input Types**

```html
<!-- Integer number -->
<input type="number" name="age" min="0" max="120">

<!-- Decimal number -->
<input type="number" name="price" min="0" step="0.01">

<!-- Range slider -->
<input type="range" name="volume" min="0" max="100" value="50">
```

- `type="number"`: Spinners for increasing/decreasing values
- `type="range"`: Slider control
- `step`: Increment amount
- `min`/`max`: Value constraints
        """,
            
            "date_time_inputs": """
**Date and Time Input Types**

```html
<!-- Date picker -->
<input type="date" name="birthdate">

<!-- Month picker -->
<input type="month" name="month">

<!-- Week picker -->
<input type="week" name="week">

<!-- Time picker -->
<input type="time" name="appointment-time">

<!-- Date and time -->
<input type="datetime-local" name="meeting-time">
```

Browser provides native date/time pickers. On mobile, shows appropriate keyboard.
        """,
            
            "color_input": """
**Color Input Type**

```html
<input type="color" name="favorite-color" value="#FF0000">

<!-- Display selected color -->
<input type="color" id="color-picker">
<p>Selected color: <span id="color-value">#FF0000</span></p>

<script>
    document.getElementById('color-picker').addEventListener('input', (e) => {
        document.getElementById('color-value').textContent = e.target.value;
    });
</script>
```

Shows a color picker interface. Returns hex color code.
        """,
            
            "file_input": """
**File Input Type**

```html
<!-- Single file -->
<input type="file" name="document">

<!-- Multiple files -->
<input type="file" name="images" multiple>

<!-- Specific file types -->
<input type="file" name="photo" accept="image/*">

<!-- Multiple specific types -->
<input type="file" name="document" accept=".pdf,.doc,.docx">

<!-- Video files -->
<input type="file" name="video" accept="video/*">
```

Attributes:
- `multiple`: Allow selecting multiple files
- `accept`: Filter visible files by type
  - `image/*`: All image types
  - `video/*`: All video types
  - `.pdf`: Specific file extension
  - `image/jpeg`: Specific MIME type
        """,
            
            "hidden_input": """
**Hidden Input Type**

```html
<input type="hidden" name="user-id" value="12345">
<input type="hidden" name="session-token" value="abc123xyz">
```

Sends data with form but isn't visible to user. Useful for:
- Session tokens
- User IDs
- CSRF protection tokens
- Form identifiers
        """,
            
            "checkbox_radio": """
**Checkbox and Radio Buttons**

```html
<!-- Checkboxes (multiple selections) -->
<label>
    <input type="checkbox" name="interests" value="sports"> Sports
</label>
<label>
    <input type="checkbox" name="interests" value="music"> Music
</label>
<label>
    <input type="checkbox" name="interests" value="reading"> Reading
</label>

<!-- Radio buttons (single selection) -->
<fieldset>
    <legend>Choose your experience level:</legend>
    <label>
        <input type="radio" name="level" value="beginner"> Beginner
    </label>
    <label>
        <input type="radio" name="level" value="intermediate"> Intermediate
    </label>
    <label>
        <input type="radio" name="level" value="advanced"> Advanced
    </label>
</fieldset>
```

- Checkboxes: Multiple selections allowed
- Radio buttons: Only one selection per group (same name)
        """,
            
            "buttons": """
**Button Types**

```html
<!-- Submit form -->
<input type="submit" value="Send Form">
<button type="submit">Send Form</button>

<!-- Reset form to defaults -->
<input type="reset" value="Clear Form">
<button type="reset">Clear Form</button>

<!-- Button with no default action -->
<input type="button" value="Click Me">
<button type="button">Click Me</button>

<!-- Button that looks like a link -->
<button type="button" style="background:none;border:none;color:blue;cursor:pointer;">
    Click here
</button>
```

- `submit`: Sends form data to action URL
- `reset`: Resets form to initial values
- `button`: No default behavior, use with JavaScript
        """,
            
            "input_validation_examples": """
**Input Type Validation Examples**

```html
<form>
    <!-- Email must be valid format -->
    <input type="email" required>
    
    <!-- URL must be valid format -->
    <input type="url" required>
    
    <!-- Number must be between 1 and 100 -->
    <input type="number" min="1" max="100" required>
    
    <!-- Must be future date -->
    <input type="date" min="2024-12-11" required>
    
    <!-- Time within business hours -->
    <input type="time" min="09:00" max="17:00" required>
    
    <button type="submit">Submit</button>
</form>
```

The browser validates input before allowing submission.
        """,
        }
    }
}
