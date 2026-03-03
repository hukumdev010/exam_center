"""CSS Developer Certification"""

CERTIFICATION = {
    "name": "CSS Developer Certification",
    "description": ("Advanced CSS expertise including modern layout systems, "
                    "animations, performance optimization, and cutting-edge "
                    "CSS features"),
    "slug": "css-developer-certification",
    "level": "Associate",
    "duration": 120,
    "questions_count": 75,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": ("When implementing a CSS Grid layout with dynamic content "
                 "where items can span multiple rows based on their content "
                 "height, how do you ensure proper grid alignment while "
                 "preventing overlapping items?"),
        "explanation": ("Use 'grid-auto-rows: min-content' or "
                        "'grid-auto-rows: max-content' to let rows size based "
                        "on content. For spanning multiple rows dynamically, "
                        "use 'grid-row: span var(--row-span)' with CSS custom "
                        "properties calculated via JavaScript, or implement "
                        "subgrid (where supported) for nested grid alignment."),
        "reference": ("https://developer.mozilla.org/en-US/docs/Web/CSS/"
                      "CSS_Grid_Layout/Auto-placement_in_CSS_Grid_Layout"),
        "points": 3,
        "answers": [
            {"text": ("Use fixed row heights with overflow: hidden to "
                      "prevent overlapping"), "is_correct": False},
            {"text": ("Use grid-auto-rows with content-based sizing and "
                      "dynamic span values"), "is_correct": True},
            {"text": ("Convert to flexbox layout for better content "
                      "adaptation"), "is_correct": False},
            {"text": ("Use absolute positioning within grid cells for "
                      "dynamic sizing"), "is_correct": False}
        ]
    },
    {
        "text": "In CSS Custom Properties (CSS Variables), what happens when you use 'inherit', 'initial', and 'unset' values, and how do they differ in behavior from regular CSS properties?",
        "explanation": "CSS Custom Properties inherit by default like inherited properties. 'inherit' forces inheritance, 'initial' resets to the initial value (empty string for custom properties), and 'unset' acts like 'inherit' since custom properties are inherited. This differs from regular properties where 'unset' behavior depends on whether the property naturally inherits.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties",
        "points": 2,
        "answers": [
            {"text": "Custom properties behave identically to regular properties with these values", "is_correct": False},
            {"text": "Custom properties inherit by default, so 'unset' acts like 'inherit' unlike regular properties", "is_correct": True},
            {"text": "These values are not supported for custom properties", "is_correct": False},
            {"text": "Custom properties always use 'initial' behavior regardless of the keyword used", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS Container Queries for responsive components, what are the key differences between size-based and style-based container queries, and how do you handle container query polyfills for browser compatibility?",
        "explanation": "Size-based container queries (@container) respond to container dimensions using containment context. Style-based container queries (@container style()) respond to CSS property values of the container. For compatibility, use CSS Container Query Polyfill or PostCSS plugins, ensuring proper fallbacks and progressive enhancement strategies.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Container_Queries",
        "points": 3,
        "answers": [
            {"text": "Both query types are identical in functionality and implementation", "is_correct": False},
            {"text": "Size queries use dimensions, style queries use property values, require polyfills for compatibility", "is_correct": True},
            {"text": "Container queries are fully supported across all browsers without polyfills", "is_correct": False},
            {"text": "Style-based queries are deprecated in favor of size-based queries", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Flexbox, when you have flex items with different 'flex-basis' values and the container is smaller than the sum of all basis values, how does the shrinking algorithm distribute the negative space?",
        "explanation": "CSS uses the flex shrink algorithm: negative space is distributed proportionally based on each item's 'flex-shrink' value multiplied by its flex-basis. Items with larger flex-basis and higher flex-shrink values lose more space. The formula is: shrink amount = (negative space × item shrink × item basis) / sum of (all shrink × all basis).",
        "reference": "https://www.w3.org/TR/css-flexbox-1/#resolve-flexible-lengths",
        "points": 3,
        "answers": [
            {"text": "Negative space is distributed equally among all flex items", "is_correct": False},
            {"text": "Space is distributed proportionally based on flex-shrink multiplied by flex-basis", "is_correct": True},
            {"text": "Only items with flex-shrink > 0 shrink, others maintain their basis", "is_correct": False},
            {"text": "The largest items shrink first until they match the smallest items", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS animations with complex timing functions, what is the difference between 'steps()' and 'cubic-bezier()' functions, and how do you optimize animations for 60fps performance?",
        "explanation": "steps() creates discrete frame-based animations (like sprite sheets), while cubic-bezier() creates smooth mathematical curves. For 60fps performance: animate only transform and opacity properties, use 'will-change' sparingly, prefer CSS transforms over changing layout properties, and use animation-fill-mode to avoid unnecessary repaints.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Tips",
        "points": 3,
        "answers": [
            {"text": "Both functions create identical smooth animations with different syntax", "is_correct": False},
            {"text": "steps() creates discrete frames, cubic-bezier() creates smooth curves; optimize with transforms and will-change", "is_correct": True},
            {"text": "steps() is deprecated in favor of cubic-bezier() for all animations", "is_correct": False},
            {"text": "Animation performance is automatically optimized by modern browsers", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Grid's 'subgrid' feature, what problems does it solve that regular nested grids cannot, and how do you handle browser fallbacks for unsupported implementations?",
        "explanation": "Subgrid allows nested grids to inherit parent grid tracks, solving alignment issues across different nesting levels and enabling true grid-based design systems. For fallbacks, use @supports feature queries to detect subgrid support and provide alternative layouts using regular grid or flexbox for unsupported browsers.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Subgrid",
        "points": 3,
        "answers": [
            {"text": "Subgrid only provides performance benefits without solving layout problems", "is_correct": False},
            {"text": "Subgrid enables track inheritance for proper alignment across nesting levels with @supports fallbacks", "is_correct": True},
            {"text": "Subgrid is fully supported and doesn't require fallback strategies", "is_correct": False},
            {"text": "Regular nested grids provide identical functionality to subgrid", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS logical properties for internationalization, how do 'margin-inline-start' and 'margin-block-start' differ from 'margin-left' and 'margin-top', and what are the implications for RTL layouts?",
        "explanation": "Logical properties adapt to writing direction and text orientation. 'margin-inline-start' maps to left in LTR and right in RTL, while 'margin-block-start' maps to top in horizontal writing modes. This eliminates the need for direction-specific CSS overrides and creates truly international-ready layouts.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Logical_Properties",
        "points": 2,
        "answers": [
            {"text": "Logical properties are just aliases for physical properties with identical behavior", "is_correct": False},
            {"text": "Logical properties adapt to writing direction, eliminating need for RTL-specific overrides", "is_correct": True},
            {"text": "Logical properties only work with Grid and Flexbox layouts", "is_correct": False},
            {"text": "Physical properties automatically convert to logical equivalents in RTL contexts", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Cascade Layers (@layer), what is the specificity behavior within and between layers, and how do you architect a maintainable layer system for large applications?",
        "explanation": "Within layers, normal specificity rules apply. Between layers, layer order determines precedence regardless of specificity - later layers override earlier ones. Architect with base layer (resets, defaults), component layers (by feature), utility layers, and theme layers. Use unlayered styles sparingly as they have highest precedence.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/@layer",
        "points": 3,
        "answers": [
            {"text": "Specificity works identically within layers and normal CSS", "is_correct": False},
            {"text": "Layer order overrides specificity between layers; architect with base, component, utility layers", "is_correct": True},
            {"text": "Cascade layers are only useful for CSS frameworks, not application development", "is_correct": False},
            {"text": "All styles must be placed in layers for cascade layers to work properly", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS Scroll Snap, what is the difference between 'scroll-snap-type: x mandatory' and 'scroll-snap-type: x proximity', and how do you handle scroll snap in nested scrollable containers?",
        "explanation": "'mandatory' forces snapping - users cannot leave the scroll container between snap points. 'proximity' suggests snapping - it only snaps if the scroll position is close to a snap point. For nested containers, each container can have its own snap behavior, but avoid conflicting snap axes to prevent user experience issues.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Scroll_Snap",
        "points": 2,
        "answers": [
            {"text": "Both mandatory and proximity have identical snapping behavior", "is_correct": False},
            {"text": "Mandatory forces snapping, proximity suggests it; each container has independent snap behavior", "is_correct": True},
            {"text": "Nested scroll containers cannot use scroll snap simultaneously", "is_correct": False},
            {"text": "Proximity mode is deprecated in favor of mandatory for all use cases", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Containment (@supports (contain: layout)), what performance benefits does each containment type provide, and when should you use 'contain: strict' versus selective containment?",
        "explanation": "Layout containment isolates internal layout from external changes. Style containment prevents style recalculation cascade. Paint containment creates stacking context and clips overflow. Size containment makes sizing independent of contents. Use 'strict' (layout + style + paint + size) for independent components, selective containment for fine-tuned performance.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/contain",
        "points": 3,
        "answers": [
            {"text": "All containment types provide identical performance benefits", "is_correct": False},
            {"text": "Each type isolates different aspects; use strict for independent components, selective for fine-tuning", "is_correct": True},
            {"text": "Containment only affects visual appearance without performance impact", "is_correct": False},
            {"text": "Strict containment should be applied to all elements for maximum performance", "is_correct": False}
        ]
    },
    {
        "text": "When working with CSS Houdini Paint API, how do you create a custom paint worklet that responds to CSS custom properties, and what are the performance implications compared to traditional background images?",
        "explanation": "Paint worklets are registered with CSS.paintWorklet.addModule() and use paint() function in CSS. They can access CSS custom properties via inputProperties and redraw when properties change. Performance-wise, they're rendered on the compositor thread, avoiding main thread blocking, but require JavaScript execution and should be optimized for repeated calls.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API",
        "points": 3,
        "answers": [
            {"text": "Paint worklets only work with predefined patterns and cannot use custom properties", "is_correct": False},
            {"text": "Paint worklets use registerPaint() with inputProperties and run on compositor thread for better performance", "is_correct": True},
            {"text": "Paint worklets have worse performance than traditional images in all scenarios", "is_correct": False},
            {"text": "Paint worklets are only supported in development environments", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Color Module Level 4, what advantages do 'oklch()' and 'oklab()' color spaces provide over 'hsl()' and 'rgb()', particularly for programmatic color manipulation and accessibility?",
        "explanation": "oklch() and oklab() provide perceptually uniform color spaces where equal numeric differences correspond to equal perceived differences. They offer better color interpolation, more predictable lightness adjustments, and wider gamut support. This makes programmatic color manipulation more intuitive and improves accessibility through more accurate contrast calculations.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/oklch",
        "points": 3,
        "answers": [
            {"text": "oklch() and oklab() are just newer syntax for identical color representations", "is_correct": False},
            {"text": "oklch()/oklab() provide perceptually uniform spaces for better interpolation and accessibility", "is_correct": True},
            {"text": "These color spaces only work with HDR displays and are not useful for standard monitors", "is_correct": False},
            {"text": "hsl() and rgb() provide better browser compatibility without functional differences", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS View Transitions API, how do you create smooth transitions between different page states, and what are the performance considerations for complex transition animations?",
        "explanation": "Use document.startViewTransition() to capture before/after states, then CSS to animate between them using ::view-transition pseudo-elements. For performance: limit transitioned elements, use transform and opacity, avoid layout-triggering properties, and consider reducing animation complexity on lower-end devices using media queries.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API",
        "points": 3,
        "answers": [
            {"text": "View transitions only work between different HTML pages, not page states", "is_correct": False},
            {"text": "Use startViewTransition() with ::view-transition pseudo-elements, optimize with transforms and reduce complexity", "is_correct": True},
            {"text": "View transitions automatically optimize performance without developer consideration", "is_correct": False},
            {"text": "Complex transitions should always use JavaScript instead of the View Transitions API", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Grid Layout, what is the difference between 'auto-fit' and 'auto-fill' in repeat() functions, and how do they behave differently with leftover space?",
        "explanation": "'auto-fill' creates as many tracks as fit in the container, leaving empty tracks if there aren't enough items. 'auto-fit' collapses empty tracks to zero, allowing remaining items to grow and fill available space. This affects how grid items distribute and align when there are fewer items than potential tracks.",
        "reference": "https://css-tricks.com/auto-sizing-columns-css-grid-auto-fill-vs-auto-fit/",
        "points": 2,
        "answers": [
            {"text": "auto-fit and auto-fill have identical behavior in all scenarios", "is_correct": False},
            {"text": "auto-fill maintains empty tracks, auto-fit collapses them allowing items to grow", "is_correct": True},
            {"text": "auto-fit only works with minmax() function, auto-fill works with all track sizes", "is_correct": False},
            {"text": "auto-fill is deprecated in favor of auto-fit for responsive grids", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS custom selectors using @custom-selector (or similar future specifications), how would they improve CSS maintainability, and what are current alternatives for achieving similar functionality?",
        "explanation": "Custom selectors would allow defining reusable selector patterns, improving maintainability and reducing repetition. Currently, use CSS preprocessors (Sass mixins/extends), CSS-in-JS libraries with dynamic selectors, or CSS custom properties with attribute selectors for pseudo-custom selector behavior.",
        "reference": "https://www.w3.org/TR/css-extensions-1/#custom-selectors",
        "points": 2,
        "answers": [
            {"text": "Custom selectors are fully supported and widely used in modern CSS", "is_correct": False},
            {"text": "Custom selectors would improve maintainability; use preprocessors or CSS-in-JS as alternatives", "is_correct": True},
            {"text": "Custom selectors only provide syntax sugar without functional benefits", "is_correct": False},
            {"text": "CSS already has sufficient selector features making custom selectors unnecessary", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Anchor Positioning, how do you position elements relative to other elements outside their containing block hierarchy, and what are the accessibility considerations?",
        "explanation": "Use anchor-name on the anchor element and position-anchor on the positioned element, with anchor() function for positioning relative to anchor edges. For accessibility, ensure anchored elements remain logically associated in DOM order, provide fallback positioning for unsupported browsers, and maintain keyboard navigation flow.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Anchor_Positioning",
        "points": 3,
        "answers": [
            {"text": "Anchor positioning only works within the same containing block", "is_correct": False},
            {"text": "Use anchor-name/position-anchor with anchor() function, maintain DOM order for accessibility", "is_correct": True},
            {"text": "Anchored elements automatically inherit accessibility properties from their anchors", "is_correct": False},
            {"text": "Anchor positioning is purely visual and has no accessibility implications", "is_correct": False}
        ]
    },
    {
        "text": "When optimizing CSS for Critical Rendering Path, what strategies ensure above-the-fold content renders quickly while avoiding FOUC (Flash of Unstyled Content)?",
        "explanation": "Inline critical CSS in HTML head, load non-critical CSS asynchronously, use resource hints (preload/prefetch), minimize CSS size and complexity, avoid @import, use CSS containment for performance isolation, and implement progressive enhancement patterns to gracefully handle loading states.",
        "reference": "https://web.dev/critical-rendering-path/",
        "points": 3,
        "answers": [
            {"text": "Loading all CSS synchronously provides the best user experience", "is_correct": False},
            {"text": "Inline critical CSS, async load non-critical, use resource hints, and progressive enhancement", "is_correct": True},
            {"text": "FOUC is unavoidable and should be accepted as normal web behavior", "is_correct": False},
            {"text": "JavaScript should handle all styling to avoid CSS loading issues", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Flexbox, when using 'align-content' on a flex container, why doesn't it work with single-line flex containers, and how do you achieve similar alignment effects?",
        "explanation": "'align-content' aligns flex lines in the cross axis, so it requires multiple lines (flex-wrap: wrap) to have an effect. For single-line containers, use 'align-items' to align flex items within the line, or use 'justify-content' for main axis alignment. You can also force wrapping or use Grid for more complex alignment needs.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/align-content",
        "points": 2,
        "answers": [
            {"text": "align-content works identically on single-line and multi-line containers", "is_correct": False},
            {"text": "align-content needs multiple flex lines; use align-items for single-line alignment", "is_correct": True},
            {"text": "align-content is deprecated and should be replaced with align-items", "is_correct": False},
            {"text": "Single-line containers don't support cross-axis alignment properties", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS-in-JS solutions, what are the performance trade-offs between runtime styling (styled-components) versus build-time extraction (Linaria), and how do you optimize for production?",
        "explanation": "Runtime CSS-in-JS provides dynamic theming and component props styling but adds JavaScript bundle size and runtime overhead. Build-time extraction generates static CSS files with better performance but less dynamic capability. Optimize with: CSS prop for static styles, styled-components for dynamic ones, CSS extraction in production, and component-level code splitting.",
        "reference": "https://css-tricks.com/a-thorough-analysis-of-css-in-js/",
        "points": 3,
        "answers": [
            {"text": "Runtime and build-time CSS-in-JS have identical performance characteristics", "is_correct": False},
            {"text": "Runtime offers dynamics but adds overhead; build-time provides performance but less flexibility", "is_correct": True},
            {"text": "CSS-in-JS always performs worse than traditional CSS in all scenarios", "is_correct": False},
            {"text": "Production performance is not affected by CSS-in-JS implementation choices", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Box Model, what is the difference between 'box-sizing: border-box' and 'box-sizing: content-box' in terms of width calculation, and why is border-box often preferred for layout?",
        "explanation": "'content-box' (default) makes width apply only to content, with padding and borders added outside. 'border-box' includes padding and borders within the specified width. Border-box is preferred for layouts because it makes sizing predictable - a 100px wide element is always 100px total width regardless of padding/borders.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing",
        "points": 1,
        "answers": [
            {"text": "Both box-sizing values calculate width identically", "is_correct": False},
            {"text": "border-box includes padding/borders in width calculation, making layouts more predictable", "is_correct": True},
            {"text": "content-box is always preferred for responsive design", "is_correct": False},
            {"text": "box-sizing only affects height calculations, not width", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS animations that need to synchronize with JavaScript events, how do you use animation events ('animationstart', 'animationend') effectively, and what are the timing considerations?",
        "explanation": "Use addEventListener for animation events to coordinate CSS animations with JavaScript. 'animationstart' fires when animation begins, 'animationend' when it completes, 'animationiteration' for each cycle. Consider animation-delay, animation-fill-mode for state management, and use Promise-based wrappers for async/await patterns with animation completion.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event",
        "points": 2,
        "answers": [
            {"text": "CSS animations cannot be synchronized with JavaScript events", "is_correct": False},
            {"text": "Use animation events with addEventListener for synchronization, consider timing and fill-mode", "is_correct": True},
            {"text": "Animation events only fire in development mode for debugging purposes", "is_correct": False},
            {"text": "JavaScript timers are more reliable than animation events for synchronization", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Grid, how do you implement a masonry layout using native CSS Grid properties, and what are the limitations compared to JavaScript masonry libraries?",
        "explanation": "CSS Grid masonry is proposed with 'grid-template-rows: masonry' but has limited support. Current alternatives include: CSS Grid with manual item placement, Flexbox with column-count, or CSS Grid with subgrid. Limitations: no automatic item reordering, limited browser support, and less flexible than JavaScript libraries for complex masonry algorithms.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Masonry_Layout",
        "points": 3,
        "answers": [
            {"text": "Native CSS Grid masonry is fully supported across all modern browsers", "is_correct": False},
            {"text": "Masonry is proposed with grid-template-rows: masonry but has limitations and poor support", "is_correct": True},
            {"text": "CSS Grid cannot create masonry layouts and requires JavaScript libraries", "is_correct": False},
            {"text": "Masonry layouts are deprecated in favor of regular grid layouts", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS theming with custom properties, how do you structure CSS variables for scalability, and what patterns prevent naming conflicts in large applications?",
        "explanation": "Structure with semantic layers: global tokens (--color-primary), component tokens (--button-bg), and local tokens (--local-spacing). Use naming conventions like BEM for CSS variables (--component__element--modifier). Implement CSS cascade layers, use CSS Modules or styled-components for scoping, and consider design token tools for systematic management.",
        "reference": "https://web.dev/css-custom-properties-theming/",
        "points": 2,
        "answers": [
            {"text": "All CSS variables should be global for maximum reusability", "is_correct": False},
            {"text": "Use semantic layering with naming conventions, scoping, and design token systems", "is_correct": True},
            {"text": "CSS variables automatically prevent naming conflicts", "is_correct": False},
            {"text": "Theming should be handled entirely in JavaScript to avoid CSS complexity", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Selector Matching, what is the performance difference between attribute selectors, class selectors, and ID selectors, and how do you optimize selector performance for large DOMs?",
        "explanation": "Performance ranking: ID selectors (fastest) > class selectors > attribute selectors > complex selectors. IDs use hash maps, classes use indexed lists, attributes require string matching. Optimize by: avoiding deep descendant selectors, using specific classes over complex attribute queries, and minimizing universal selectors and :not() pseudo-classes.",
        "reference": "https://csswizardry.com/2011/09/writing-efficient-css-selectors/",
        "points": 2,
        "answers": [
            {"text": "All selector types have identical performance characteristics", "is_correct": False},
            {"text": "ID > class > attribute selectors for performance; optimize with specific classes and shallow nesting", "is_correct": True},
            {"text": "Attribute selectors are always faster than class selectors", "is_correct": False},
            {"text": "Selector performance is irrelevant in modern browsers", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS for print media, what specific considerations and properties ensure proper pagination, color management, and layout preservation?",
        "explanation": "Use @media print queries, control pagination with page-break-before/after, use @page for page dimensions and margins, implement orphans/widows for text flow control, ensure color/background printing considerations, use cm/in units for accurate sizing, and test with actual print preview and different paper sizes.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/@media#Media_types",
        "points": 2,
        "answers": [
            {"text": "Print styles automatically inherit all screen styles without modifications", "is_correct": False},
            {"text": "Use @media print, @page rules, pagination controls, and physical units for print optimization", "is_correct": True},
            {"text": "Print media queries are deprecated in favor of responsive design", "is_correct": False},
            {"text": "JavaScript is required for all print layout customizations", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Transform functions, what is the difference between 'transform-origin' and the transform functions themselves in terms of coordinate systems and animation behavior?",
        "explanation": "'transform-origin' sets the pivot point for transformations (default: center), affecting how rotations, scales, and skews are applied. Transform functions operate relative to this origin point. Changing transform-origin during animations can create different visual effects - animations rotate/scale around different points, which is crucial for complex animation choreography.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin",
        "points": 2,
        "answers": [
            {"text": "transform-origin and transform functions are interchangeable properties", "is_correct": False},
            {"text": "transform-origin sets the pivot point affecting how transform functions are applied and animated", "is_correct": True},
            {"text": "transform-origin only affects 3D transforms, not 2D transformations", "is_correct": False},
            {"text": "Changing transform-origin has no visual impact on transform animations", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS Scroll-driven Animations, how do you create animations that respond to scroll position, and what performance optimizations ensure smooth scrolling?",
        "explanation": "Use animation-timeline: scroll() to tie animations to scroll progress, or view() for element visibility progress. Optimize performance by animating only transform and opacity properties, using animation-range for precise control, implementing CSS containment, and avoiding layout-triggering properties during scroll animations.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Scroll-driven_Animations",
        "points": 3,
        "answers": [
            {"text": "Scroll-driven animations require JavaScript and cannot use pure CSS", "is_correct": False},
            {"text": "Use animation-timeline with scroll()/view(), optimize with transforms and containment", "is_correct": True},
            {"text": "Scroll animations automatically optimize performance without developer consideration", "is_correct": False},
            {"text": "Scroll-driven animations only work with CSS Grid layouts", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Flexbox, when you have flex items with different heights and use 'align-items: stretch', how does this interact with intrinsic sizing and aspect ratios of replaced elements like images?",
        "explanation": "'align-items: stretch' makes flex items fill the cross-axis, but replaced elements (images, videos) with intrinsic aspect ratios won't stretch unless their height is explicitly set or object-fit is used. The natural aspect ratio is preserved. Use 'align-self: stretch' with 'height: 100%' and 'object-fit: cover/contain' for proper stretching behavior.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Aligning_Items_in_a_Flex_Container",
        "points": 2,
        "answers": [
            {"text": "stretch always forces all flex items to the same height regardless of content", "is_correct": False},
            {"text": "Replaced elements preserve aspect ratios unless explicitly sized with object-fit", "is_correct": True},
            {"text": "Images automatically stretch to fill flex containers without additional CSS", "is_correct": False},
            {"text": "align-items: stretch only affects text content, not replaced elements", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS for high-DPI displays, how do you use media queries like 'resolution' and '-webkit-device-pixel-ratio' effectively, and what are best practices for responsive images?",
        "explanation": "Use @media (min-resolution: 2dppx) for modern browsers, fallback to (-webkit-min-device-pixel-ratio: 2) for older WebKit. Implement responsive images with srcset and sizes attributes, provide multiple image densities (1x, 2x, 3x), use SVG for icons when possible, and consider CSS image-set() for background images on high-DPI displays.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/@media/resolution",
        "points": 2,
        "answers": [
            {"text": "High-DPI displays automatically scale all images without developer intervention", "is_correct": False},
            {"text": "Use resolution media queries with srcset/sizes for responsive images and multiple densities", "is_correct": True},
            {"text": "device-pixel-ratio media queries are sufficient for all high-DPI scenarios", "is_correct": False},
            {"text": "CSS cannot detect display density, requiring JavaScript for high-DPI support", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Overflow, what is the difference between 'overflow: clip' and 'overflow: hidden', and when would you choose each for performance and functionality?",
        "explanation": "'overflow: hidden' creates a new stacking context and allows programmatic scrolling, while 'overflow: clip' simply clips content without creating stacking context and prevents all scrolling. Use 'clip' for better performance when you don't need scrolling capabilities, and 'hidden' when you need stacking context or might enable scrolling programmatically.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/overflow",
        "points": 2,
        "answers": [
            {"text": "clip and hidden have identical functionality and performance characteristics", "is_correct": False},
            {"text": "clip prevents scrolling without stacking context, hidden allows programmatic scrolling with stacking context", "is_correct": True},
            {"text": "clip is deprecated and should be replaced with hidden in all cases", "is_correct": False},
            {"text": "hidden provides better performance than clip in all scenarios", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS Intrinsic Web Design patterns, how do you combine CSS Grid, Flexbox, and intrinsic sizing (min-content, max-content, fit-content) to create truly responsive layouts without media queries?",
        "explanation": "Combine CSS Grid's minmax() with intrinsic keywords, use fit-content() for flexible sizing, implement auto-fit/auto-fill for responsive columns, use flexbox for component-level responsiveness, and leverage CSS clamp() for fluid typography and spacing. This creates layouts that adapt to content and available space naturally.",
        "reference": "https://aneventapart.com/news/post/intrinsic-web-design-with-css-grid-flexbox-and-intrinsic-sizing",
        "points": 3,
        "answers": [
            {"text": "Intrinsic web design requires media queries for all responsive behavior", "is_correct": False},
            {"text": "Combine Grid minmax(), intrinsic keywords, flexbox, and clamp() for content-driven responsiveness", "is_correct": True},
            {"text": "Intrinsic sizing is only useful for typography, not layout systems", "is_correct": False},
            {"text": "CSS Grid and Flexbox cannot be used together in intrinsic design patterns", "is_correct": False}
        ]
    },
    {
        "text": "In CSS position: sticky, what are the common issues with sticky positioning in scrollable containers, and how do you debug and fix sticky elements that aren't working?",
        "explanation": "Common issues: parent containers with overflow: hidden/auto create new scroll contexts, sticky elements need a defined top/bottom/left/right value, and the sticky container must have sufficient height. Debug by checking computed styles, scroll contexts, and container heights. Fix by adjusting overflow properties and ensuring proper positioning context.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/position",
        "points": 2,
        "answers": [
            {"text": "Sticky positioning works identically in all container types without special considerations", "is_correct": False},
            {"text": "Check overflow properties, positioning values, and container heights; adjust scroll contexts", "is_correct": True},
            {"text": "Sticky elements automatically work without any positioning or container requirements", "is_correct": False},
            {"text": "JavaScript is required to make sticky positioning work properly", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS Counter Styles for custom list numbering, how do you create complex numbering systems (like legal document numbering), and what are the limitations of CSS counters?",
        "explanation": "Use @counter-style for custom numbering systems, counter() and counters() functions for nested numbering, and counter-reset/counter-increment for control. Limitations include: no complex mathematical operations, limited formatting options, performance impact with many counters, and no access to counter values in JavaScript without additional work.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/@counter-style",
        "points": 3,
        "answers": [
            {"text": "CSS counters can handle any mathematical numbering system without limitations", "is_correct": False},
            {"text": "Use @counter-style and counter functions for custom systems, but limitations exist for complex operations", "is_correct": True},
            {"text": "CSS counters are deprecated in favor of JavaScript-based numbering", "is_correct": False},
            {"text": "Counter styles only work with ordered lists and cannot be used elsewhere", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Multi-column Layout, how do you control column breaks, balance content across columns, and handle spanning elements effectively?",
        "explanation": "Use break-before/break-after/break-inside for break control, column-fill for balancing (auto vs balance), column-span for spanning elements across all columns. Control orphans/widows for text flow, use column-gap for spacing, and consider that spanning elements create new column contexts above and below.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Columns",
        "points": 2,
        "answers": [
            {"text": "Multi-column layouts automatically balance content without developer control", "is_correct": False},
            {"text": "Use break properties, column-fill for balance, column-span for spanning, control text flow", "is_correct": True},
            {"text": "Spanning elements are not supported in CSS multi-column layouts", "is_correct": False},
            {"text": "Column breaks can only be controlled through JavaScript, not CSS", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS for component libraries, how do you ensure style encapsulation while maintaining themability and preventing style leakage between components?",
        "explanation": "Use CSS Modules, styled-components, or Shadow DOM for encapsulation. Implement CSS custom properties for theming APIs, use BEM or similar naming conventions, leverage CSS cascade layers for predictable specificity, provide CSS reset/normalization, and use PostCSS or build tools for automatic scoping and optimization.",
        "reference": "https://css-tricks.com/css-modules-part-1-need/",
        "points": 3,
        "answers": [
            {"text": "Global CSS is sufficient for component libraries without special encapsulation needs", "is_correct": False},
            {"text": "Use CSS Modules/styled-components/Shadow DOM with custom properties for theming and naming conventions", "is_correct": True},
            {"text": "JavaScript is the only reliable way to prevent style leakage in components", "is_correct": False},
            {"text": "CSS encapsulation automatically prevents all styling conflicts between components", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Performance optimization, what impact do CSS selectors, property calculations, and layout operations have on rendering performance, and how do you measure and optimize them?",
        "explanation": "CSS selector performance affects style calculation time, complex selectors slow matching. Property calculations impact paint/composite phases. Layout operations are most expensive (reflow). Measure with DevTools Performance tab, Lighthouse, and rendering metrics. Optimize by simplifying selectors, using transform/opacity for animations, and minimizing layout-triggering properties.",
        "reference": "https://web.dev/css-performance/",
        "points": 3,
        "answers": [
            {"text": "All CSS operations have equal performance impact and cannot be optimized", "is_correct": False},
            {"text": "Selectors affect style calculation, properties affect paint, layout is most expensive; measure and optimize accordingly", "is_correct": True},
            {"text": "CSS performance is automatically optimized by browsers without developer intervention", "is_correct": False},
            {"text": "JavaScript always provides better performance than CSS for styling operations", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS for accessibility, how do you ensure proper focus management, color contrast, and support for assistive technologies while maintaining visual design requirements?",
        "explanation": "Implement visible focus indicators with :focus-visible, ensure 4.5:1 color contrast ratios, use semantic HTML with ARIA labels, provide alternative text for CSS-generated content, support prefers-reduced-motion, use relative units for scalability, and test with screen readers. Balance visual design with accessibility using progressive enhancement.",
        "reference": "https://web.dev/accessibility-css/",
        "points": 3,
        "answers": [
            {"text": "Accessibility requirements always conflict with visual design and require compromises", "is_correct": False},
            {"text": "Use focus indicators, contrast ratios, semantic HTML, motion preferences, and progressive enhancement", "is_correct": True},
            {"text": "CSS accessibility features are automatically handled by assistive technologies", "is_correct": False},
            {"text": "Visual design should take priority over accessibility considerations", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Grid's implicit grid behavior, how does the algorithm determine placement for items without explicit grid-area assignments, and how do you control the implicit grid sizing?",
        "explanation": "CSS Grid uses auto-placement algorithm: items flow row-wise by default, filling available cells. For items without explicit placement, grid creates implicit tracks as needed. Control with grid-auto-flow (row/column/dense), grid-auto-rows/grid-auto-columns for implicit track sizing, and grid-template-areas for explicit regions.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Auto-placement_in_CSS_Grid_Layout",
        "points": 3,
        "answers": [
            {"text": "Implicit grid items are randomly placed without predictable algorithm", "is_correct": False},
            {"text": "Auto-placement flows row-wise by default; control with grid-auto-flow and grid-auto sizing", "is_correct": True},
            {"text": "All grid items must be explicitly placed to avoid layout issues", "is_correct": False},
            {"text": "Implicit grid behavior cannot be controlled and uses browser defaults", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS animations for complex UI interactions (like drag-and-drop or complex transitions), how do you coordinate multiple animation timelines and handle user interruptions gracefully?",
        "explanation": "Use animation-play-state for pause/resume control, coordinate with CSS custom properties and JavaScript, implement animation queues with delays, use animation-fill-mode for state management, handle interruptions by resetting or transitioning to current state, and consider Web Animations API for complex orchestration.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API",
        "points": 3,
        "answers": [
            {"text": "Complex animations should only be handled with JavaScript libraries", "is_correct": False},
            {"text": "Use animation-play-state, custom properties, fill-mode, and Web Animations API for coordination", "is_correct": True},
            {"text": "CSS animations cannot be interrupted or coordinated with user interactions", "is_correct": False},
            {"text": "Multiple animation timelines automatically coordinate without developer intervention", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Houdini Layout API, how do you create custom layout algorithms that work alongside existing layout methods, and what are the performance and compatibility considerations?",
        "explanation": "Register layout worklets with CSS.layoutWorklet.addModule(), define intrinsicSizes and layout methods, use display: layout() in CSS. Performance: runs on main thread (unlike Paint API), so optimize for speed. Compatibility: limited browser support, requires progressive enhancement and fallbacks to standard layouts.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/API/CSS_Layout_API",
        "points": 3,
        "answers": [
            {"text": "Layout API is fully supported and can replace all existing layout methods", "is_correct": False},
            {"text": "Register worklets with layout methods, optimize for main thread, provide fallbacks for compatibility", "is_correct": True},
            {"text": "Custom layout algorithms run on compositor thread for better performance", "is_correct": False},
            {"text": "Layout API only works with CSS Grid and cannot integrate with other layout systems", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS for cross-browser compatibility, what are the key strategies for handling vendor prefixes, feature detection, and progressive enhancement in modern web development?",
        "explanation": "Use Autoprefixer for automatic vendor prefixes, @supports for feature detection, implement progressive enhancement with fallbacks, use PostCSS for compatibility processing, test across browsers, provide polyfills for unsupported features, and follow feature support matrices to determine baseline requirements.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/@supports",
        "points": 2,
        "answers": [
            {"text": "Modern browsers have eliminated the need for cross-browser compatibility considerations", "is_correct": False},
            {"text": "Use Autoprefixer, @supports, progressive enhancement, and polyfills for compatibility", "is_correct": True},
            {"text": "Manual vendor prefixing is more reliable than automated tools", "is_correct": False},
            {"text": "CSS compatibility issues are automatically resolved by browser auto-update mechanisms", "is_correct": False}
        ]
    },
    {
        "text": "In CSS Mathematics Functions (min(), max(), clamp()), how do you create responsive design systems without media queries, and what are the performance implications of complex calculations?",
        "explanation": "Use clamp() for fluid typography and spacing, min()/max() for container queries-like behavior, combine with calc() for complex responsive formulas, use CSS custom properties for maintainable systems. Performance: calculations happen at computed value time, so complex nested calculations can impact performance on lower-end devices.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/clamp",
        "points": 2,
        "answers": [
            {"text": "Math functions cannot replace media queries for responsive design", "is_correct": False},
            {"text": "Use clamp() for fluid design, min/max for constraints, consider calculation performance impact", "is_correct": True},
            {"text": "Mathematical functions have no performance implications regardless of complexity", "is_correct": False},
            {"text": "CSS math functions are only useful for simple numeric calculations", "is_correct": False}
        ]
    },
    {
        "text": "When implementing CSS for design systems at scale, how do you structure CSS architecture to support multiple teams, maintain consistency, and enable efficient updates across products?",
        "explanation": "Implement atomic design principles, use design tokens for consistent values, create component-based CSS architecture, establish naming conventions (BEM/OOCSS), use CSS-in-JS or CSS Modules for scoping, implement automated testing for visual regression, and provide comprehensive documentation and guidelines.",
        "reference": "https://atomicdesign.bradfrost.com/",
        "points": 3,
        "answers": [
            {"text": "Large design systems should use monolithic CSS files for simplicity", "is_correct": False},
            {"text": "Use atomic design, design tokens, component architecture, naming conventions, and automated testing", "is_correct": True},
            {"text": "Each team should maintain separate CSS without shared systems", "is_correct": False},
            {"text": "CSS architecture doesn't significantly impact team collaboration or maintenance", "is_correct": False}
        ]
    },
    {
        "text": ("Which CSS code correctly creates a responsive card layout "
                 "that stacks vertically on mobile and shows 3 cards per row "
                 "on desktop?"),
        "explanation": ("The correct implementation uses CSS Grid with "
                        "auto-fit and minmax() to create responsive columns "
                        "that adapt based on available space. The "
                        "minmax(300px, 1fr) ensures cards are at least 300px "
                        "wide but can grow, and auto-fit allows the layout "
                        "to stack when space is insufficient."),
        "reference": ("https://css-tricks.com/auto-sizing-columns-css-grid-"
                      "auto-fill-vs-auto-fit/"),
        "points": 2,
        "answers": [
            {"text": (".cards { display: flex; flex-wrap: wrap; } "
                      ".card { flex: 1 0 33.333%; }"), "is_correct": False},
            {"text": (".cards { display: grid; grid-template-columns: "
                      "repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; }"),
             "is_correct": True},
            {"text": (".cards { display: grid; grid-template-columns: "
                      "repeat(3, 1fr); } @media (max-width: 768px) { "
                      "grid-template-columns: 1fr; }"), "is_correct": False},
            {"text": (".cards { display: block; } .card { width: 33.333%; "
                      "float: left; }"), "is_correct": False}
        ]
    },
    {
        "text": ("What is the correct CSS to create a smooth hover animation "
                 "that scales an element to 110% and changes its color with "
                 "a 0.3s transition?"),
        "explanation": ("The correct implementation uses the transition "
                        "property on the base element to define the animation "
                        "duration and properties, then uses transform: "
                        "scale() and color change in the hover state. This "
                        "ensures smooth transitions in both directions."),
        "reference": ("https://developer.mozilla.org/en-US/docs/Web/CSS/"
                      "CSS_Transitions/Using_CSS_transitions"),
        "points": 1,
        "answers": [
            {"text": (".element { transition: all 0.3s ease; } "
                      ".element:hover { transform: scale(1.1); "
                      "color: #007bff; }"), "is_correct": True},
            {"text": (".element:hover { transition: 0.3s; "
                      "transform: scale(110%); color: blue; }"),
             "is_correct": False},
            {"text": (".element { animation: hover 0.3s; } "
                      ".element:hover { scale: 1.1; color: #007bff; }"),
             "is_correct": False},
            {"text": (".element { transform: scale(1); } "
                      ".element:hover { transform: scale(1.1); "
                      "transition: 0.3s; }"), "is_correct": False}
        ]
    },
    {
        "text": ("Which CSS code correctly creates a centered modal overlay "
                 "that covers the entire viewport?"),
        "explanation": ("The correct implementation uses fixed positioning to "
                        "cover the entire viewport, flexbox for perfect "
                        "centering, and a high z-index to ensure the modal "
                        "appears above other content. The rgba background "
                        "creates a semi-transparent overlay."),
        "reference": "https://css-tricks.com/considerations-styling-modal/",
        "points": 2,
        "answers": [
            {"text": (".modal-overlay { position: absolute; top: 0; left: 0; "
                      "width: 100%; height: 100%; display: flex; "
                      "align-items: center; justify-content: center; }"), 
             "is_correct": False},
            {"text": (".modal-overlay { position: fixed; top: 0; left: 0; "
                      "width: 100%; height: 100%; "
                      "background: rgba(0,0,0,0.5); display: flex; "
                      "align-items: center; justify-content: center; "
                      "z-index: 1000; }"), "is_correct": True},
            {"text": (".modal-overlay { position: relative; margin: 0 auto; "
                      "display: block; text-align: center; }"), 
             "is_correct": False},
            {"text": (".modal-overlay { position: sticky; top: 50%; left: 50%; "
                      "transform: translate(-50%, -50%); }"), 
             "is_correct": False}
        ]
    },
    {
        "text": ("What CSS code creates a CSS-only hamburger menu animation "
                 "that transforms from three lines to an X when clicked?"),
        "explanation": ("This uses a checkbox hack with CSS transforms to "
                        "animate the hamburger lines. The middle line "
                        "disappears (opacity: 0), while the top and bottom "
                        "lines rotate to form an X shape using transform-"
                        "origin and rotate transforms."),
        "reference": ("https://css-tricks.com/three-css-alternatives-to-"
                      "javascript-navigation/"),
        "points": 3,
        "answers": [
            {"text": (".hamburger input:checked ~ .line:nth-child(1) { "
                      "transform: rotate(45deg); } .hamburger "
                      "input:checked ~ .line:nth-child(2) { opacity: 0; }"),
             "is_correct": False},
            {"text": (".hamburger input:checked ~ .line:nth-child(1) { "
                      "transform: rotate(45deg) translate(6px, 6px); } "
                      ".hamburger input:checked ~ .line:nth-child(2) { "
                      "opacity: 0; } .hamburger input:checked ~ "
                      ".line:nth-child(3) { transform: rotate(-45deg) "
                      "translate(6px, -6px); }"), "is_correct": True},
            {"text": (".hamburger:active .line { transform: rotateZ(45deg); "
                      "opacity: 0.5; }"), "is_correct": False},
            {"text": (".hamburger .line { animation: rotate 0.3s; } "
                      "@keyframes rotate { to { transform: "
                      "rotate(90deg); } }"),
             "is_correct": False}
        ]
    },
    {
        "text": ("Which CSS creates a perfect circular progress indicator "
                 "using conic gradients?"),
        "explanation": ("This creates a circular progress indicator using "
                        "conic-gradient with CSS custom properties. The "
                        "gradient goes from the progress color to "
                        "transparent, creating a partial circle effect. "
                        "The transform rotates it to start from the top."),
        "reference": "https://css-tricks.com/building-progress-ring-quickly/",
        "points": 3,
        "answers": [
            {"text": (".progress { width: 100px; height: 100px; "
                      "border-radius: 50%; background: linear-gradient("
                      "90deg, #007bff var(--progress), transparent "
                      "var(--progress)); }"), "is_correct": False},
            {"text": (".progress { width: 100px; height: 100px; "
                      "border-radius: 50%; background: conic-gradient("
                      "#007bff calc(var(--progress) * 1%), transparent 0); "
                      "transform: rotate(-90deg); }"), "is_correct": True},
            {"text": (".progress { width: 100px; height: 100px; "
                      "border: 10px solid #ddd; border-top: 10px solid "
                      "#007bff; border-radius: 50%; animation: spin 1s "
                      "linear infinite; }"), "is_correct": False},
            {"text": (".progress { width: 100px; height: 100px; "
                      "background: radial-gradient(circle, #007bff "
                      "var(--progress), transparent var(--progress)); }"),
             "is_correct": False}
        ]
    },
    {
        "text": "What CSS code correctly implements a masonry-style layout using CSS Grid?",
        "explanation": "This implementation uses CSS Grid with auto-rows set to a small value and items spanning multiple rows based on their content height. The dense packing helps fill gaps, creating a masonry-like effect.",
        "reference": "https://css-tricks.com/a-complete-guide-to-css-grid/#masonry",
        "points": 3,
        "answers": [
            {"text": ".masonry { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); grid-auto-rows: 10px; } .item { grid-row-end: span var(--row-span); }", "is_correct": True},
            {"text": ".masonry { display: flex; flex-direction: column; flex-wrap: wrap; height: 100vh; } .item { break-inside: avoid; }", "is_correct": False},
            {"text": ".masonry { column-count: auto; column-width: 250px; } .item { display: inline-block; width: 100%; }", "is_correct": False},
            {"text": ".masonry { display: grid; grid-template-rows: masonry; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS creates a complex 3D card flip animation on hover?",
        "explanation": "This creates a 3D card flip effect using perspective on the container, preserve-3d on the card, and rotateY transforms on the front and back faces. The backface-visibility prevents seeing through the card during the flip.",
        "reference": "https://css-tricks.com/almanac/properties/p/perspective/",
        "points": 3,
        "answers": [
            {"text": ".card-container { perspective: 1000px; } .card { transform-style: preserve-3d; transition: transform 0.6s; } .card:hover { transform: rotateY(180deg); } .card-back { transform: rotateY(180deg); } .card-front, .card-back { backface-visibility: hidden; }", "is_correct": True},
            {"text": ".card { transition: transform 0.6s; } .card:hover { transform: rotateZ(180deg); } .card-back { display: none; } .card:hover .card-back { display: block; }", "is_correct": False},
            {"text": ".card { animation: flip 0.6s; } @keyframes flip { to { transform: scaleX(-1); } } .card-back { transform: scaleX(-1); }", "is_correct": False},
            {"text": ".card { transform: rotateY(0deg); } .card:hover { transform: rotateY(180deg); transition: 0.6s; }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS code creates a sticky navigation that changes style when scrolling past the hero section?",
        "explanation": "This uses position: sticky with a scroll-based animation timeline to change the navigation appearance. The animation-range ensures the style change occurs at the right scroll position relative to the hero section.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Scroll-driven_Animations",
        "points": 3,
        "answers": [
            {"text": ".nav { position: sticky; top: 0; animation: navScroll linear; animation-timeline: scroll(); animation-range: 0px 300px; } @keyframes navScroll { to { background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); box-shadow: 0 2px 20px rgba(0,0,0,0.1); } }", "is_correct": True},
            {"text": ".nav { position: fixed; top: 0; transition: all 0.3s; } .nav.scrolled { background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }", "is_correct": False},
            {"text": ".nav { position: sticky; top: 0; } .nav:after { content: ''; position: absolute; background: white; opacity: 0; transition: opacity 0.3s; } .nav:scroll { opacity: 1; }", "is_correct": False},
            {"text": ".nav { position: relative; animation: stick 1s forwards; } @keyframes stick { from { position: relative; } to { position: sticky; top: 0; } }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS correctly implements a CSS-only accordion with smooth height transitions?",
        "explanation": "This creates a CSS-only accordion using the checkbox hack. The max-height transition provides smooth animation, and the large max-height value (500px) accommodates varying content sizes while maintaining the animation effect.",
        "reference": "https://css-tricks.com/css3-accordion/",
        "points": 2,
        "answers": [
            {"text": ".accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.3s ease; } .accordion-toggle:checked + .accordion-content { max-height: 500px; }", "is_correct": True},
            {"text": ".accordion-content { height: 0; transition: height 0.3s; } .accordion-toggle:checked + .accordion-content { height: auto; }", "is_correct": False},
            {"text": ".accordion-content { display: none; } .accordion-toggle:checked + .accordion-content { display: block; animation: slideDown 0.3s; }", "is_correct": False},
            {"text": ".accordion-content { transform: scaleY(0); transition: transform 0.3s; } .accordion-toggle:checked + .accordion-content { transform: scaleY(1); }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS creates a loading spinner with multiple animated dots?",
        "explanation": "This creates a loading animation with three dots that bounce in sequence. Each dot has a different animation delay to create the wave effect, and the animation uses transform: translateY() for smooth movement.",
        "reference": "https://css-tricks.com/single-element-loaders-the-spinner/",
        "points": 2,
        "answers": [
            {"text": ".loader { display: flex; gap: 4px; } .dot { width: 8px; height: 8px; border-radius: 50%; background: #007bff; animation: bounce 1.4s infinite both; } .dot:nth-child(1) { animation-delay: -0.32s; } .dot:nth-child(2) { animation-delay: -0.16s; } @keyframes bounce { 0%, 80%, 100% { transform: scale(0); } 40% { transform: scale(1); } }", "is_correct": False},
            {"text": ".loader { display: flex; gap: 4px; } .dot { width: 8px; height: 8px; border-radius: 50%; background: #007bff; animation: bounce 1s infinite ease-in-out both; } .dot:nth-child(1) { animation-delay: -0.32s; } .dot:nth-child(2) { animation-delay: -0.16s; } @keyframes bounce { 0%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-12px); } }", "is_correct": True},
            {"text": ".loader .dot { animation: spin 1s linear infinite; } @keyframes spin { to { transform: rotate(360deg); } }", "is_correct": False},
            {"text": ".loader { animation: pulse 1s infinite; } @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.5; } 100% { opacity: 1; } }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS code correctly creates a responsive typography system using fluid font sizes?",
        "explanation": "This creates fluid typography using clamp() function that scales smoothly between minimum and maximum sizes based on viewport width. The calc() function creates a responsive scaling factor, while rem units ensure accessibility.",
        "reference": "https://css-tricks.com/linearly-scale-font-size-with-css-clamp-based-on-the-viewport/",
        "points": 2,
        "answers": [
            {"text": "h1 { font-size: clamp(1.5rem, 4vw, 3rem); } h2 { font-size: clamp(1.25rem, 3vw, 2.5rem); } h3 { font-size: clamp(1.125rem, 2.5vw, 2rem); }", "is_correct": True},
            {"text": "h1 { font-size: calc(16px + 2vw); } h2 { font-size: calc(14px + 1.5vw); } h3 { font-size: calc(12px + 1vw); }", "is_correct": False},
            {"text": "@media (min-width: 768px) { h1 { font-size: 3rem; } h2 { font-size: 2.5rem; } } @media (max-width: 767px) { h1 { font-size: 1.5rem; } h2 { font-size: 1.25rem; } }", "is_correct": False},
            {"text": "h1 { font-size: max(1.5rem, min(4vw, 3rem)); } h2 { font-size: max(1.25rem, min(3vw, 2.5rem)); }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS creates a parallax scrolling effect using only CSS transforms?",
        "explanation": "This creates a pure CSS parallax effect using transform3d() for hardware acceleration and perspective. Different elements move at different speeds during scroll by applying different translateZ values within a perspective container.",
        "reference": "https://css-tricks.com/pure-css-parallax-websites/",
        "points": 3,
        "answers": [
            {"text": ".parallax-container { height: 100vh; overflow-x: hidden; overflow-y: auto; perspective: 1px; } .parallax-element { position: absolute; top: 0; transform: translateZ(-1px) scale(2); }", "is_correct": True},
            {"text": ".parallax-element { position: fixed; background-attachment: fixed; background-size: cover; }", "is_correct": False},
            {"text": ".parallax-element { animation: parallax linear; animation-timeline: scroll(); } @keyframes parallax { to { transform: translateY(-50%); } }", "is_correct": False},
            {"text": ".parallax-element { transform: translateY(calc(-50% * var(--scroll-ratio))); }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS correctly implements a custom dropdown with smooth animations and accessibility features?",
        "explanation": "This creates an accessible dropdown with smooth height transitions, proper ARIA states, and keyboard navigation support. The max-height technique allows for smooth animation while maintaining accessibility with focus states.",
        "reference": "https://css-tricks.com/solved-with-css-dropdown-menus/",
        "points": 3,
        "answers": [
            {"text": ".dropdown-menu { max-height: 0; overflow: hidden; opacity: 0; transition: max-height 0.3s ease, opacity 0.3s ease; } .dropdown:hover .dropdown-menu, .dropdown:focus-within .dropdown-menu { max-height: 300px; opacity: 1; } .dropdown-item:focus { background: #f0f0f0; outline: 2px solid #007bff; }", "is_correct": True},
            {"text": ".dropdown-menu { display: none; } .dropdown:hover .dropdown-menu { display: block; animation: fadeIn 0.3s; } @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }", "is_correct": False},
            {"text": ".dropdown-menu { visibility: hidden; } .dropdown:hover .dropdown-menu { visibility: visible; transition: visibility 0.3s; }", "is_correct": False},
            {"text": ".dropdown-menu { transform: translateY(-100%); } .dropdown:hover .dropdown-menu { transform: translateY(0); transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1); }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS code creates a responsive image gallery with lightbox functionality using only CSS?",
        "explanation": "This creates a CSS-only lightbox using the :target pseudo-selector and z-index layering. The transform and opacity provide smooth transitions, while the overlay covers the entire viewport for the lightbox effect.",
        "reference": "https://css-tricks.com/css-only-lightbox/",
        "points": 3,
        "answers": [
            {"text": ".lightbox { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); display: flex; align-items: center; justify-content: center; opacity: 0; visibility: hidden; transition: all 0.3s ease; } .lightbox:target { opacity: 1; visibility: visible; }", "is_correct": True},
            {"text": ".gallery img:hover { transform: scale(3); z-index: 1000; position: relative; }", "is_correct": False},
            {"text": ".lightbox { display: none; } .gallery img:focus + .lightbox { display: flex; }", "is_correct": False},
            {"text": ".lightbox-overlay { position: absolute; background: black; } .lightbox:checked + .lightbox-overlay { display: block; }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS creates a complex gradient border with animation?",
        "explanation": "This creates an animated gradient border using a pseudo-element with a larger gradient background. The content area is positioned above with a solid background, creating the border effect. The animation rotates the gradient continuously.",
        "reference": "https://css-tricks.com/gradient-borders-in-css/",
        "points": 3,
        "answers": [
            {"text": ".gradient-border { position: relative; background: white; } .gradient-border::before { content: ''; position: absolute; inset: -2px; background: linear-gradient(45deg, #ff0000, #00ff00, #0000ff, #ff0000); border-radius: inherit; z-index: -1; animation: rotate 3s linear infinite; } @keyframes rotate { to { transform: rotate(360deg); } }", "is_correct": True},
            {"text": ".gradient-border { border: 2px solid; border-image: linear-gradient(45deg, red, green, blue) 1; animation: borderSpin 3s infinite; }", "is_correct": False},
            {"text": ".gradient-border { outline: 2px solid transparent; background: linear-gradient(white, white) content-box, linear-gradient(45deg, red, green, blue) border-box; }", "is_correct": False},
            {"text": ".gradient-border { box-shadow: 0 0 0 2px red, 0 0 0 4px green, 0 0 0 6px blue; animation: pulse 3s infinite; }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS creates a morphing button that transforms into a loading spinner on click?",
        "explanation": "This creates a morphing button using the checkbox hack. When checked, the button transforms into a circular spinner with rotating border animation. The width and height transitions create the morphing effect.",
        "reference": "https://css-tricks.com/morphing-buttons-concept/",
        "points": 3,
        "answers": [
            {"text": ".morph-btn { width: 150px; height: 50px; border: none; border-radius: 25px; background: #007bff; color: white; transition: all 0.3s ease; cursor: pointer; } .morph-btn:checked { width: 50px; border-radius: 50%; } .morph-btn:checked::after { content: ''; display: block; width: 20px; height: 20px; border: 2px solid transparent; border-top: 2px solid white; border-radius: 50%; animation: spin 1s linear infinite; }", "is_correct": True},
            {"text": ".morph-btn:active { transform: scale(0.95); background: #0056b3; } .morph-btn:focus { outline: 2px solid #007bff; }", "is_correct": False},
            {"text": ".morph-btn { animation: morph 2s infinite alternate; } @keyframes morph { to { border-radius: 50%; width: 50px; } }", "is_correct": False},
            {"text": ".morph-btn:hover { border-radius: 50%; width: 50px; height: 50px; }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS correctly implements a tooltip with dynamic positioning using container queries?",
        "explanation": "This creates adaptive tooltips using container queries to adjust positioning based on available space. The tooltip changes its position (top/bottom) and arrow direction based on the container's size, ensuring it's always visible.",
        "reference": "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Container_Queries",
        "points": 3,
        "answers": [
            {"text": ".tooltip-container { container-type: inline-size; } .tooltip { position: absolute; bottom: 100%; left: 50%; transform: translateX(-50%); } @container (max-height: 200px) { .tooltip { top: 100%; bottom: auto; } .tooltip::before { border-bottom: 5px solid black; border-top: none; top: -5px; bottom: auto; } }", "is_correct": True},
            {"text": ".tooltip { position: relative; } .tooltip:hover::after { content: attr(data-tooltip); position: absolute; top: -30px; left: 50%; transform: translateX(-50%); }", "is_correct": False},
            {"text": "@media (max-height: 200px) { .tooltip { position: fixed; top: 10px; } }", "is_correct": False},
            {"text": ".tooltip { top: auto; bottom: 100%; } .tooltip:focus-within { top: 100%; bottom: auto; }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS creates a complex CSS-only pricing table with animated feature comparisons?",
        "explanation": "This creates an interactive pricing table where hovering over features highlights them across all plans with smooth animations. The transform and transition effects create engaging visual feedback for comparing features.",
        "reference": "https://css-tricks.com/comparison-table-ui-pattern/",
        "points": 2,
        "answers": [
            {"text": ".pricing-table { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; } .feature-row:hover { background: #f8f9fa; transform: scale(1.02); transition: all 0.2s ease; } .feature-row:hover .feature-cell { background: #e3f2fd; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }", "is_correct": True},
            {"text": ".pricing-plan { border: 1px solid #ddd; } .pricing-plan:hover { border-color: #007bff; }", "is_correct": False},
            {"text": ".pricing-table .plan { animation: slideIn 0.5s ease; } @keyframes slideIn { from { transform: translateY(20px); opacity: 0; } }", "is_correct": False},
            {"text": ".feature { opacity: 0.7; } .plan:hover .feature { opacity: 1; transition: opacity 0.3s; }", "is_correct": False}
        ]
    },
    {
        "text": "Which CSS creates a responsive sidebar navigation with overlay for mobile?",
        "explanation": "This creates a responsive sidebar that's always visible on desktop but becomes an overlay on mobile. The checkbox hack controls the mobile state, and transform transitions provide smooth slide animations.",
        "reference": "https://css-tricks.com/off-canvas-menu-with-css-target-pseudo-class-and-transition/",
        "points": 2,
        "answers": [
            {"text": ".sidebar { position: fixed; top: 0; left: -250px; width: 250px; height: 100vh; background: #333; transition: transform 0.3s ease; z-index: 1000; } .sidebar-toggle:checked ~ .sidebar { transform: translateX(250px); } @media (min-width: 768px) { .sidebar { position: static; transform: translateX(0); } }", "is_correct": True},
            {"text": ".sidebar { display: none; } @media (min-width: 768px) { .sidebar { display: block; } } .mobile-menu { display: block; } @media (min-width: 768px) { .mobile-menu { display: none; } }", "is_correct": False},
            {"text": ".sidebar { width: 0; overflow: hidden; transition: width 0.3s; } .sidebar.open { width: 250px; }", "is_correct": False},
            {"text": ".sidebar { opacity: 0; visibility: hidden; } .sidebar:target { opacity: 1; visibility: visible; }", "is_correct": False}
        ]
    },
    {
        "text": "What CSS code creates a staggered animation for a list of items appearing in sequence?",
        "explanation": "This creates a staggered animation where each list item appears with a delay. The calc() function dynamically calculates delays based on the item's position, creating a wave effect as items animate in sequence.",
        "reference": "https://css-tricks.com/staggered-animations/",
        "points": 2,
        "answers": [
            {"text": ".list-item { opacity: 0; transform: translateY(20px); animation: fadeInUp 0.6s ease forwards; } .list-item:nth-child(1) { animation-delay: 0.1s; } .list-item:nth-child(2) { animation-delay: 0.2s; } .list-item:nth-child(3) { animation-delay: 0.3s; } @keyframes fadeInUp { to { opacity: 1; transform: translateY(0); } }", "is_correct": True},
            {"text": ".list { animation: stagger 2s ease-in-out; } @keyframes stagger { 0% { opacity: 0; } 100% { opacity: 1; } }", "is_correct": False},
            {"text": ".list-item { transition: all 0.3s ease; } .list:hover .list-item { transform: scale(1.05); }", "is_correct": False},
            {"text": ".list-item { animation: slideIn 1s infinite alternate; } @keyframes slideIn { from { margin-left: -100%; } to { margin-left: 0; } }", "is_correct": False}
        ]
    }
]