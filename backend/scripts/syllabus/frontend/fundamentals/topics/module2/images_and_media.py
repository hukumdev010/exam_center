"""
Images and Media Elements - Detailed Content

This file contains comprehensive content for the "Images and Media" topic
from Module 2: HTML5 Fundamentals.
"""

TOPIC_CONTENT = {
    "title": "Images and Media Elements",
    "duration": "60-75 minutes",
    "difficulty": "Beginner",
    "overview": """
    Learn how to properly embed images, audio, and video in HTML5. This topic covers
    responsive images, accessibility considerations, and modern media embedding practices.
    """,
    
    "detailed_content": {
        "introduction": """
Images and media are crucial parts of modern websites. They make content more engaging,
improve user experience, and increase time spent on pages. However, they also pose challenges:

1. **Performance**: Large files slow down page load times
2. **Accessibility**: Images need text descriptions for screen readers
3. **Responsiveness**: Images need to scale properly on different devices
4. **SEO**: Media can be optimized for search engines

In this topic, we'll learn how to properly embed images and media while addressing
these challenges.
        """,
        
        "key_concepts": {
            "image_basics": """
**The Image Element**

The `<img>` tag is used to display images:

```html
<img src="photo.jpg" alt="A beautiful sunset over the ocean">
```

**Essential Attributes**

`src`: The image file path or URL (REQUIRED)
```html
<!-- File path -->
<img src="images/photo.jpg" alt="Description">

<!-- Full URL -->
<img src="https://example.com/images/photo.jpg" alt="Description">

<!-- Relative path (parent directory) -->
<img src="../images/photo.jpg" alt="Description">
```

`alt`: Alternative text (REQUIRED for accessibility)
```html
<!-- Descriptive alt text -->
<img src="sunset.jpg" alt="A golden sunset reflecting over calm ocean waters">

<!-- For decorative images, use empty alt -->
<img src="decorative-line.png" alt="">

<!-- For images containing text, transcribe the text -->
<img src="price-chart.jpg" alt="Monthly pricing chart: Basic $10, Pro $20, Enterprise $50">
```

Good alt text:
- Describes the image content, not just "image" or "photo"
- Is concise but descriptive (typically 10-15 words)
- Includes relevant context
- Doesn't start with "image of" or "picture of"

**Other Attributes**

```html
<img 
    src="photo.jpg"
    alt="A sunset"
    width="800"              <!-- Intrinsic width -->
    height="600"             <!-- Intrinsic height -->
    loading="lazy"           <!-- Lazy loading -->
    title="Click to enlarge" <!-- Tooltip on hover -->
    class="thumbnail"        <!-- CSS class -->
    id="main-hero"           <!-- Unique ID -->
>
```

`width` and `height`: Specifies dimensions
- Helps browser reserve space while loading
- Prevents layout shift when image loads
- Units: pixels (default) or percentage

```html
<!-- Pixels (most common) -->
<img src="photo.jpg" alt="Photo" width="800" height="600">

<!-- With CSS (more flexible) -->
<img src="photo.jpg" alt="Photo" style="width: 100%; height: auto;">
```

`loading="lazy"`: Defers image loading until needed
```html
<!-- Lazy load images below the fold -->
<img src="photo.jpg" alt="Photo" loading="lazy">
```

**Image Formats**

Different formats for different purposes:

| Format | Use Case | Compression |
|--------|----------|-------------|
| JPG | Photographs, complex images | Lossy |
| PNG | Graphics, logos, transparency needed | Lossless |
| WebP | Modern format, excellent compression | Lossy |
| GIF | Simple animations, limited colors | Lossless |
| SVG | Logos, icons, scalable graphics | Vector |

Best practices:
- Use JPG for photos
- Use PNG for graphics with transparency
- Use WebP for modern browsers (with JPG fallback)
- Use SVG for icons and logos
- Use GIF rarely (use video instead for animations)
            """,
            
            "responsive_images": """
**Making Images Responsive**

**Responsive Image Sizing**

Using CSS:
```html
<!-- HTML -->
<img src="photo.jpg" alt="A sunset" class="responsive">

<!-- CSS -->
<style>
    .responsive {
        width: 100%;        /* Fill container */
        height: auto;       /* Maintain aspect ratio */
        max-width: 800px;   /* Don't stretch beyond max */
        display: block;
    }
</style>
```

**The Picture Element (Advanced Responsiveness)**

For truly responsive images that change at different breakpoints:

```html
<picture>
    <!-- Mobile (max 600px) -->
    <source media="(max-width: 600px)" srcset="photo-small.jpg">
    
    <!-- Tablet (max 1200px) -->
    <source media="(max-width: 1200px)" srcset="photo-medium.jpg">
    
    <!-- Desktop and large (1200px+) -->
    <source srcset="photo-large.jpg">
    
    <!-- Fallback for browsers that don't support picture -->
    <img src="photo.jpg" alt="A sunset">
</picture>
```

The browser uses the first matching `<source>` tag that applies.

**Responsive Images for Different Pixel Densities**

For retina displays and high-DPI screens:

```html
<!-- Using srcset -->
<img 
    src="photo-1x.jpg" 
    srcset="photo-1x.jpg 1x, photo-2x.jpg 2x"
    alt="A sunset"
    width="800"
    height="600"
>

<!-- For pictures -->
<picture>
    <source srcset="photo-1x.jpg 1x, photo-2x.jpg 2x" type="image/jpeg">
    <img src="photo-1x.jpg" alt="A sunset">
</picture>
```

`1x` = normal resolution, `2x` = retina/high-DPI
The browser automatically loads the appropriate version.

**Modern Picture with Multiple Formats**

Serve WebP to modern browsers, JPG to others:

```html
<picture>
    <!-- Modern browsers (WebP) -->
    <source srcset="photo.webp" type="image/webp">
    
    <!-- Fallback (JPG) -->
    <source srcset="photo.jpg" type="image/jpeg">
    
    <!-- Old browsers -->
    <img src="photo.jpg" alt="A sunset" width="800" height="600">
</picture>
```

**The Srcset Attribute**

More flexible than `picture` for many use cases:

```html
<img 
    src="photo-medium.jpg"
    srcset="
        photo-small.jpg 400w,      <!-- 400px width -->
        photo-medium.jpg 800w,     <!-- 800px width -->
        photo-large.jpg 1200w      <!-- 1200px width -->
    "
    alt="A sunset"
    width="800"
    height="600"
>
```

The browser automatically selects the best image based on:
- Viewport size
- Device pixel ratio
- Network speed (if available)

Widths are specified with `w` (width descriptor).
            """,
            
            "figure_and_captions": """
**Figure and Caption Elements**

Semantically associate images with captions:

```html
<figure>
    <img src="sunset.jpg" alt="A golden sunset over the ocean">
    <figcaption>Figure 1: Sunset at Malibu Beach (2024)</figcaption>
</figure>
```

`<figure>`: Groups image with related content
`<figcaption>`: Provides a caption or title for the figure

**Examples**

Code example with caption:
```html
<figure>
    <pre><code>
const greeting = "Hello, World!";
console.log(greeting);
    </code></pre>
    <figcaption>Example 1: Basic JavaScript output</figcaption>
</figure>
```

Chart with caption:
```html
<figure>
    <img src="sales-chart.png" alt="Sales growth chart showing 45% increase year-over-year">
    <figcaption>
        <strong>Figure 2:</strong> Annual sales growth (2020-2024)
    </figcaption>
</figure>
```

Diagram with detailed caption:
```html
<figure>
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <!-- SVG content -->
    </svg>
    <figcaption>
        A diagram illustrating the water cycle:
        evaporation, condensation, and precipitation.
    </figcaption>
</figure>
```
            """,
            
            "audio_video_elements": """
**Audio Element**

Embed audio files:

```html
<audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    <source src="audio.ogg" type="audio/ogg">
    Your browser doesn't support HTML5 audio. Download the file here.
</audio>
```

**Attributes**:
- `controls`: Show play/pause controls
- `autoplay`: Auto-play (often blocked by browsers)
- `loop`: Loop when finished
- `muted`: Muted by default
- `preload`: "auto" (load all), "metadata" (load metadata), "none"

**Full Example**

```html
<figure>
    <figcaption>Podcast: Web Development Tips</figcaption>
    <audio controls preload="metadata">
        <source src="episode-1.mp3" type="audio/mpeg">
        <source src="episode-1.ogg" type="audio/ogg">
        <p>Your browser doesn't support HTML5 audio.</p>
    </audio>
</figure>
```

**Video Element**

Embed videos:

```html
<video controls width="640" height="360">
    <source src="video.mp4" type="video/mp4">
    <source src="video.webm" type="video/webm">
    Your browser doesn't support HTML5 video.
</video>
```

**Attributes**:
- `controls`: Show play/pause controls
- `autoplay`: Auto-play (often requires `muted`)
- `loop`: Loop when finished
- `muted`: Muted by default
- `preload`: "auto", "metadata", or "none"
- `poster`: Image to show before video plays
- `width` and `height`: Dimensions

**Responsive Video**

```html
<div class="video-container">
    <video controls poster="poster.jpg">
        <source src="video.mp4" type="video/mp4">
        <source src="video.webm" type="video/webm">
    </video>
</div>

<style>
    .video-container {
        position: relative;
        width: 100%;
        padding-bottom: 56.25%; /* 16:9 aspect ratio */
    }
    
    .video-container video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
</style>
```

**Full Video Example**

```html
<figure>
    <figcaption>Tutorial: Getting Started with HTML5</figcaption>
    <video 
        controls 
        width="640" 
        height="360"
        poster="tutorial-poster.jpg"
        preload="metadata"
    >
        <source src="tutorial.mp4" type="video/mp4">
        <source src="tutorial.webm" type="video/webm">
        <p>Your browser doesn't support HTML5 video.</p>
    </video>
</figure>
```

**Track Element (Captions/Subtitles)**

Add captions or subtitles to video:

```html
<video controls>
    <source src="video.mp4" type="video/mp4">
    <track kind="subtitles" src="subtitles-en.vtt" srclang="en" label="English">
    <track kind="subtitles" src="subtitles-es.vtt" srclang="es" label="Español">
    <track kind="captions" src="captions-en.vtt" srclang="en" label="English Captions">
</video>
```

VTT file format:
```
WEBVTT

00:00:00.000 --> 00:00:03.000
Welcome to our HTML5 tutorial

00:00:03.500 --> 00:00:07.000
In this lesson, we'll learn about semantic HTML
```
            """,
            
            "best_practices": """
**Image and Media Best Practices**

**1. Always Include Alt Text**
```html
<!-- Good -->
<img src="sunset.jpg" alt="A golden sunset over the ocean">

<!-- Avoid -->
<img src="sunset.jpg" alt="">
<img src="sunset.jpg" alt="image">
```

**2. Optimize Image Size**
- Use image compression tools
- Choose appropriate formats
- Resize images before uploading
- Consider using WebP for modern browsers

**3. Use Responsive Images**
```html
<picture>
    <source media="(max-width: 600px)" srcset="photo-small.jpg">
    <source srcset="photo-large.jpg">
    <img src="photo.jpg" alt="Description">
</picture>
```

**4. Lazy Load Images Below the Fold**
```html
<img src="photo.jpg" alt="Photo" loading="lazy">
```

**5. Use Semantic Elements**
```html
<!-- Good: figure with caption -->
<figure>
    <img src="photo.jpg" alt="Description">
    <figcaption>Photo description or source</figcaption>
</figure>

<!-- Avoid: just image in a div -->
<div>
    <img src="photo.jpg">
</div>
```

**6. Always Specify Dimensions**
```html
<img 
    src="photo.jpg" 
    alt="Photo" 
    width="800" 
    height="600"
>
```

**7. Provide Fallbacks for Media**
```html
<video controls>
    <source src="video.mp4" type="video/mp4">
    <p>Your browser doesn't support HTML5 video.</p>
</video>
```

**8. Optimize For Performance**
- Use efficient formats (WebP, MP4)
- Lazy load media below the fold
- Use thumbnails for video (poster attribute)
- Preload only when necessary
            """
        }
    }
}
