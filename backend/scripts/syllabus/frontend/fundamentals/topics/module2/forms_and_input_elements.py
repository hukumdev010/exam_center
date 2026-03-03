"""
Forms and Input Elements - Detailed Content

This file contains comprehensive content for the "Forms and Input Elements" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Forms and Input Elements",
    "duration": "75-90 minutes",
    "difficulty": "Intermediate",
    "overview": """
    HTML forms are the primary way users interact with websites to submit data. Learn how to
    create accessible, user-friendly forms with various input types, validation, and best practices.
    """,
    
    "detailed_content": {
        "introduction": """
Forms are fundamental to web applications. They're how users:
- Log in to accounts
- Search for content
- Make purchases
- Fill out surveys
- Provide feedback
- Subscribe to newsletters

A well-designed form is crucial for user experience. A poorly designed one can frustrate users
and lose you customers. In this topic, we'll learn how to build forms that are:

1. **Accessible**: Usable by everyone, including people with disabilities
2. **User-Friendly**: Clear, logical, and easy to fill out
3. **Secure**: Protecting user data and preventing attacks
4. **Responsive**: Looking good on all devices
5. **Functional**: Properly submitting and processing data

HTML provides all the tools you need to build excellent forms. Combined with CSS for styling
and JavaScript for validation and interaction, you can create sophisticated form experiences.
        """,
        
        "key_concepts": {
            "form_structure": """
**The `<form>` Element**

A form is a container for input elements:

```html
<form action="/submit-form" method="POST">
    <!-- Form inputs go here -->
</form>
```

**Attributes**:
- `action`: URL where the form data is sent
- `method`: HTTP method to use (GET or POST)
- `name`: Name of the form (for JavaScript reference)
- `id`: Unique identifier
- `enctype`: Encoding type for file uploads (use "multipart/form-data" for files)

**GET vs POST**

**GET**: Sends form data in the URL
```html
<form action="/search" method="GET">
    <input type="text" name="q">
    <button type="submit">Search</button>
</form>
```
When submitted, the URL becomes: `/search?q=web+development`

Use GET for:
- Searching
- Filtering
- Non-sensitive data

**POST**: Sends form data in the request body (hidden from URL)
```html
<form action="/login" method="POST">
    <input type="email" name="email">
    <input type="password" name="password">
    <button type="submit">Login</button>
</form>
```

Use POST for:
- Sensitive data (passwords, credit cards)
- Large amounts of data
- Creating/updating data
- File uploads

**Form Groups and Fieldsets**

For complex forms, group related fields using `<fieldset>`:

```html
<form>
    <fieldset>
        <legend>Personal Information</legend>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name">
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email">
    </fieldset>
    
    <fieldset>
        <legend>Address</legend>
        <label for="street">Street:</label>
        <input type="text" id="street" name="street">
        
        <label for="city">City:</label>
        <input type="text" id="city" name="city">
    </fieldset>
</form>
```

- `<fieldset>`: Groups related form controls
- `<legend>`: Provides a caption for the fieldset
            """,
            
            "input_types": """
**Basic Input Element**

The `<input>` element is the most common form element:

```html
<input type="text" name="username" id="username">
```

The `type` attribute determines what kind of input it is.

**Text Inputs**

```html
<!-- Single-line text -->
<input type="text" name="username">

<!-- Email with validation -->
<input type="email" name="email">

<!-- Password (hides characters) -->
<input type="password" name="password">

<!-- URL -->
<input type="url" name="website">

<!-- Telephone number -->
<input type="tel" name="phone">

<!-- Search -->
<input type="search" name="query">

<!-- Numbers -->
<input type="number" name="quantity" min="1" max="100" step="1">

<!-- Range slider -->
<input type="range" name="volume" min="0" max="100">
```

**Date and Time**

```html
<!-- Date picker -->
<input type="date" name="birthdate">

<!-- Month -->
<input type="month" name="start-month">

<!-- Week -->
<input type="week" name="week">

<!-- Time -->
<input type="time" name="meeting-time">

<!-- Date and time -->
<input type="datetime-local" name="event-datetime">
```

**Color Picker**

```html
<input type="color" name="favorite-color">
```

**File Upload**

```html
<input type="file" name="document">

<!-- Multiple files -->
<input type="file" name="photos" multiple>

<!-- Specific file types -->
<input type="file" name="image" accept="image/*">
<input type="file" name="pdf" accept=".pdf">
```

**Checkboxes**

```html
<label>
    <input type="checkbox" name="agree" value="yes">
    I agree to the terms
</label>

<!-- Multiple checkboxes -->
<fieldset>
    <legend>Which languages do you speak?</legend>
    
    <label>
        <input type="checkbox" name="languages" value="english">
        English
    </label>
    
    <label>
        <input type="checkbox" name="languages" value="spanish">
        Spanish
    </label>
    
    <label>
        <input type="checkbox" name="languages" value="french">
        French
    </label>
</fieldset>
```

**Radio Buttons**

For mutually exclusive options:

```html
<fieldset>
    <legend>What is your experience level?</legend>
    
    <label>
        <input type="radio" name="experience" value="beginner">
        Beginner
    </label>
    
    <label>
        <input type="radio" name="experience" value="intermediate">
        Intermediate
    </label>
    
    <label>
        <input type="radio" name="experience" value="advanced">
        Advanced
    </label>
</fieldset>
```

**Important**: All radio buttons with the same purpose should have the same `name` attribute.
The `value` attribute determines what gets sent when that option is selected.

**Buttons**

```html
<!-- Submit button -->
<button type="submit">Submit</button>

<!-- Reset button (clears form) -->
<button type="reset">Clear</button>

<!-- Generic button (use JavaScript) -->
<button type="button">Click Me</button>

<!-- Using input element -->
<input type="submit" value="Submit">
<input type="reset" value="Clear">
<input type="button" value="Click Me">
```
            """,
            
            "textarea_and_select": """
**Text Area**

For multi-line text:

```html
<label for="message">Your Message:</label>
<textarea id="message" name="message" rows="5" cols="30"></textarea>
```

Attributes:
- `rows`: Number of visible text lines
- `cols`: Number of visible characters per line
- `placeholder`: Hint text
- `maxlength`: Maximum characters allowed
- `disabled`: Disabled textarea
- `readonly`: User can't edit, but data is submitted

With placeholder:
```html
<textarea 
    name="comment" 
    placeholder="Enter your comment here..."
    rows="4"
></textarea>
```

**Select Dropdown**

```html
<label for="country">Country:</label>
<select id="country" name="country">
    <option value="">-- Select a country --</option>
    <option value="usa">United States</option>
    <option value="canada">Canada</option>
    <option value="uk">United Kingdom</option>
    <option value="australia">Australia</option>
</select>
```

**Multiple Select**

Allow users to select multiple options:

```html
<label for="skills">Select your skills:</label>
<select id="skills" name="skills" multiple>
    <option value="html">HTML</option>
    <option value="css">CSS</option>
    <option value="js">JavaScript</option>
    <option value="react">React</option>
    <option value="node">Node.js</option>
</select>
```

Users can select multiple options by holding Ctrl (or Cmd on Mac) while clicking.

**Grouped Options**

```html
<select name="category">
    <optgroup label="Fruits">
        <option value="apple">Apple</option>
        <option value="banana">Banana</option>
    </optgroup>
    
    <optgroup label="Vegetables">
        <option value="carrot">Carrot</option>
        <option value="broccoli">Broccoli</option>
    </optgroup>
</select>
```

**Datalist**

Combines text input with suggestions:

```html
<label for="browser">Choose a browser:</label>
<input type="text" id="browser" name="browser" list="browsers">

<datalist id="browsers">
    <option value="Chrome">
    <option value="Firefox">
    <option value="Safari">
    <option value="Edge">
</datalist>
```

Users can type freely or select from suggestions.
            """,
            
            "labels_and_accessibility": """
**The Label Element**

`<label>` elements are essential for accessibility:

```html
<label for="email">Email Address:</label>
<input type="email" id="email" name="email">
```

The `for` attribute links the label to the input using the input's `id`.

**Why Labels Matter**:
1. Screen readers announce labels to describe inputs
2. Larger clickable area (clicking the label focuses the input)
3. Mobile users have an easier time tapping checkboxes/radio buttons
4. Makes the form more semantic and accessible

**Implicit Labels**

You can also nest the input inside the label:

```html
<label>
    Email Address:
    <input type="email" name="email">
</label>
```

Both approaches are valid, but explicit labels (with `for` attribute) are preferred for flexibility.

**Associated Instructions**

```html
<label for="password">Password:</label>
<input type="password" id="password" name="password">
<small>Must be at least 8 characters</small>
```

**Error Messages**

```html
<label for="age">Age:</label>
<input type="number" id="age" name="age" required>
<span id="age-error" role="alert"></span>
```

Using `role="alert"` makes screen readers announce error messages immediately.
            """,
            
            "validation_and_attributes": """
**HTML5 Validation**

HTML5 provides built-in validation:

```html
<!-- Required field -->
<input type="text" name="name" required>

<!-- Email validation -->
<input type="email" name="email" required>

<!-- Number range -->
<input type="number" name="age" min="18" max="120">

<!-- Pattern matching -->
<input type="text" name="username" pattern="[a-zA-Z0-9]{3,8}">

<!-- Minimum length -->
<input type="password" name="password" minlength="8">

<!-- Maximum length -->
<input type="text" name="city" maxlength="50">

<!-- File type restriction -->
<input type="file" name="image" accept="image/*">

<!-- URL validation -->
<input type="url" name="website" required>

<!-- Telephone with pattern -->
<input type="tel" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}">

<!-- Textarea length -->
<textarea name="bio" minlength="10" maxlength="500"></textarea>
```

**Custom Error Messages**

```html
<input 
    type="email" 
    name="email" 
    required
    oninvalid="this.setCustomValidity('Please enter a valid email')"
    oninput="this.setCustomValidity('')"
>
```

**Attributes**

Common input attributes:

```html
<input 
    type="text"
    name="username"              <!-- Name for form submission -->
    id="username"                <!-- Unique identifier for labels -->
    class="form-control"         <!-- CSS class for styling -->
    placeholder="Enter username" <!-- Hint text -->
    value="default value"        <!-- Initial value -->
    disabled                     <!-- Disabled input -->
    readonly                     <!-- Can't edit but submits -->
    required                     <!-- Must fill before submission -->
    autofocus                    <!-- Focus on page load -->
    autocomplete="email"         <!-- Browser suggestions -->
    tabindex="1"                 <!-- Tab order -->
>
```

**Disabled vs ReadOnly**

- `disabled`: Input is grayed out, value is NOT submitted
- `readonly`: Input appears normal, value IS submitted but can't be edited
            """,
            
            "practical_form_example": """
**Complete Contact Form**

Here's a comprehensive, accessible form:

```html
<form action="/contact" method="POST">
    <h2>Contact Us</h2>
    <p>We'd love to hear from you. Fill out this form and we'll get back to you soon.</p>
    
    <fieldset>
        <legend>Your Information</legend>
        
        <div class="form-group">
            <label for="name">Full Name *</label>
            <input 
                type="text"
                id="name"
                name="name"
                required
                autofocus
            >
        </div>
        
        <div class="form-group">
            <label for="email">Email *</label>
            <input 
                type="email"
                id="email"
                name="email"
                required
            >
        </div>
        
        <div class="form-group">
            <label for="phone">Phone</label>
            <input 
                type="tel"
                id="phone"
                name="phone"
                placeholder="123-456-7890"
            >
        </div>
    </fieldset>
    
    <fieldset>
        <legend>Message</legend>
        
        <div class="form-group">
            <label for="subject">Subject *</label>
            <select id="subject" name="subject" required>
                <option value="">-- Select a subject --</option>
                <option value="general">General Inquiry</option>
                <option value="support">Technical Support</option>
                <option value="feedback">Feedback</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="message">Message *</label>
            <textarea 
                id="message"
                name="message"
                rows="6"
                minlength="10"
                maxlength="1000"
                required
                placeholder="Please share your message..."
            ></textarea>
        </div>
    </fieldset>
    
    <fieldset>
        <legend>Preferences</legend>
        
        <div class="form-group">
            <label>
                <input type="checkbox" name="subscribe" value="yes">
                Subscribe to our newsletter
            </label>
        </div>
        
        <div class="form-group">
            <label>How did you hear about us?</label>
            <label>
                <input type="radio" name="source" value="search">
                Search engine
            </label>
            <label>
                <input type="radio" name="source" value="social">
                Social media
            </label>
            <label>
                <input type="radio" name="source" value="friend">
                Friend referral
            </label>
        </div>
    </fieldset>
    
    <div class="form-actions">
        <button type="submit">Send Message</button>
        <button type="reset">Clear Form</button>
    </div>
    
    <p><small>* Required fields</small></p>
</form>
```

**Key Features**:
1. ✓ Proper form structure with fieldsets
2. ✓ All inputs have labels with `for` attributes
3. ✓ HTML5 validation (required, email, minlength)
4. ✓ Clear fieldsets for grouping
5. ✓ Helpful placeholder text
6. ✓ Clear indication of required fields
7. ✓ Both submit and reset buttons
8. ✓ Semantic HTML structure
            """
        }
    }
}
