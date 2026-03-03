"""Tailwind CSS Certification - Improved Version with Realistic Incorrect Answers"""

CERTIFICATION = {
    "name": "Tailwind CSS Certification",
    "description": "Utility-first CSS framework for rapid UI development",
    "slug": "tailwind-css-certification",
    "level": "Associate",
    "duration": 90,
    "questions_count": 55,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": (
            "What is the fundamental philosophy behind Tailwind CSS and "
            "how does it differ from traditional CSS frameworks? Explain "
            "the utility-first approach and its benefits."
        ),
        "explanation": (
            "Tailwind CSS follows a utility-first approach where you build "
            "custom designs by composing small, single-purpose utility "
            "classes. Unlike component-based frameworks like Bootstrap, "
            "Tailwind provides low-level utility classes for properties "
            "like padding, margin, color, font size, etc. This offers "
            "greater design flexibility, smaller bundle sizes through "
            "purging unused styles, and more maintainable code."
        ),
        "reference": "https://tailwindcss.com/docs/utility-first",
        "points": 2,
        "answers": [
            {
                "text": (
                    "Utility-first approach with small, single-purpose "
                    "classes for maximum design flexibility"
                ),
                "is_correct": True
            },
            {
                "text": "Atomic CSS approach with pre-compiled style sheets",
                "is_correct": False
            },
            {
                "text": "Component-first framework with utility helpers",
                "is_correct": False
            },
            {
                "text": "Functional CSS methodology with semantic classes",
                "is_correct": False
            },
        ],
    },
    {
        "text": (
            "In Tailwind CSS, you want to create a responsive design where "
            "an element has 'p-4' on mobile, 'p-6' on tablet (md), and "
            "'p-8' on desktop (lg). What would be the correct class "
            "combination to achieve this responsive behavior?"
        ),
        "explanation": (
            "Tailwind uses a mobile-first responsive design approach. "
            "You start with the base class (p-4 for mobile), then add "
            "prefixed classes for larger breakpoints (md:p-6 for tablet, "
            "lg:p-8 for desktop). Each breakpoint applies to that screen "
            "size and larger until overridden."
        ),
        "reference": "https://tailwindcss.com/docs/responsive-design",
        "points": 2,
        "answers": [
            {"text": "p-4 md:p-6 lg:p-8", "is_correct": True},
            {"text": "p-4 sm:p-6 md:p-8", "is_correct": False},
            {"text": "px-4 md:px-6 lg:px-8", "is_correct": False},
            {"text": "p-4 md:p-6 xl:p-8", "is_correct": False},
        ],
    },
    {
        "text": (
            "What is the purpose of the '@tailwind' directives in "
            "Tailwind CSS, and what are the three main directives you "
            "typically include in your CSS file? Explain what each "
            "directive does."
        ),
        "explanation": (
            "The @tailwind directives are used to inject Tailwind's "
            "styles into your CSS. The three main directives are: "
            "@tailwind base (injects Tailwind's base styles and "
            "Normalize.css), @tailwind components (injects component "
            "classes - usually empty unless you define custom "
            "components), and @tailwind utilities (injects all utility "
            "classes). These directives tell Tailwind where to inject "
            "its generated styles."
        ),
        "reference": "https://tailwindcss.com/docs/functions-and-directives#tailwind",
        "points": 2,
        "answers": [
            {
                "text": "@tailwind base, @tailwind components, @tailwind utilities",
                "is_correct": True
            },
            {
                "text": "@tailwind base, @tailwind variants, @tailwind utilities",
                "is_correct": False
            },
            {
                "text": "@tailwind preflight, @tailwind components, @tailwind utilities",
                "is_correct": False
            },
            {
                "text": "@tailwind base, @tailwind components, @tailwind screens",
                "is_correct": False
            },
        ],
    },
    {
        "text": (
            "You need to center a div both horizontally and vertically "
            "within its container using Flexbox in Tailwind CSS. The "
            "container should also have a minimum height of the full "
            "viewport. What combination of classes would accomplish this?"
        ),
        "explanation": (
            "To center content both horizontally and vertically using "
            "Flexbox: 'flex' enables flexbox, 'items-center' centers "
            "items vertically (align-items: center), 'justify-center' "
            "centers items horizontally (justify-content: center), and "
            "'min-h-screen' sets minimum height to 100vh (full viewport "
            "height)."
        ),
        "reference": "https://tailwindcss.com/docs/flex",
        "points": 2,
        "answers": [
            {"text": "flex items-center justify-center min-h-screen", "is_correct": True},
            {"text": "flex items-center justify-center h-screen", "is_correct": False},
            {"text": "flex content-center justify-center min-h-screen", "is_correct": False},
            {"text": "flex items-center justify-items-center min-h-screen", "is_correct": False},
        ],
    },
    {
        "text": (
            "What is the difference between 'w-1/2' and 'w-6' in "
            "Tailwind CSS? Explain the different sizing systems "
            "Tailwind uses and when you would use each approach."
        ),
        "explanation": (
            "'w-1/2' uses fractional sizing (50% width relative to "
            "parent), while 'w-6' uses Tailwind's spacing scale "
            "(1.5rem or 24px by default). Tailwind has multiple sizing "
            "systems: spacing scale (0-96, then larger jumps), "
            "fractions (1/2, 1/3, 1/4, etc.), percentages, viewport "
            "units (vw, vh), and arbitrary values. Use fractions for "
            "responsive layouts, spacing scale for consistent "
            "increments, and arbitrary values for specific requirements."
        ),
        "reference": "https://tailwindcss.com/docs/width",
        "points": 2,
        "answers": [
            {"text": "w-1/2 is fractional (50% of parent), w-6 is spacing scale (1.5rem/24px)", "is_correct": True},
            {"text": "w-1/2 is percentage, w-6 is viewport width (6vw)", "is_correct": False},
            {"text": "Both use spacing scale, w-1/2 equals 0.5rem, w-6 equals 6rem", "is_correct": False},
            {"text": "w-1/2 is responsive utility, w-6 is fixed pixel value", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create custom colors and extend Tailwind's "
            "default color palette? Explain the process of customizing "
            "the tailwind.config.js file to add your brand colors."
        ),
        "explanation": (
            "You customize colors in tailwind.config.js by extending "
            "the theme. You can add new colors to the existing palette "
            "using 'extend: { colors: { brand: '#ff6b6b' } }' or "
            "completely replace the color palette. You can also define "
            "color scales like '{ brand: { 100: '#fff5f5', 500: "
            "'#ff6b6b', 900: '#742a2a' } }'. Use extend to keep "
            "default colors, or define colors directly under theme to "
            "replace them entirely."
        ),
        "reference": "https://tailwindcss.com/docs/customizing-colors",
        "points": 2,
        "answers": [
            {"text": "Extend theme.colors in tailwind.config.js with custom color objects", "is_correct": True},
            {"text": "Define colors in theme.extend.palette configuration", "is_correct": False},
            {"text": "Import colors using @import statements in CSS", "is_correct": False},
            {"text": "Use theme.colors.custom to add new color variants", "is_correct": False},
        ],
    },
    {
        "text": (
            "What is the purpose of Tailwind's 'purge' or 'content' "
            "configuration, and why is it crucial for production builds? "
            "Explain how it affects bundle size and performance."
        ),
        "explanation": (
            "The 'content' (formerly 'purge') configuration tells "
            "Tailwind which files to scan for class names. It removes "
            "unused CSS classes from the final build, dramatically "
            "reducing file size from ~3MB to typically under 100KB. "
            "This process is crucial for production because Tailwind "
            "generates thousands of utility classes by default. You "
            "specify file patterns like './src/**/*.{js,jsx,ts,tsx,html}' "
            "to scan for used classes."
        ),
        "reference": "https://tailwindcss.com/docs/content-configuration",
        "points": 2,
        "answers": [
            {"text": "Removes unused CSS classes to reduce bundle size from ~3MB to <100KB", "is_correct": True},
            {"text": "Optimizes CSS delivery by lazy-loading unused styles", "is_correct": False},
            {"text": "Compresses CSS using gzip and removes comments", "is_correct": False},
            {"text": "Minifies class names to shorter versions for production", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to apply styles only when an element is hovered "
            "AND focused simultaneously. How would you accomplish this "
            "using Tailwind's state variants?"
        ),
        "explanation": (
            "You can chain state variants in Tailwind by combining "
            "them with colons. 'hover:focus:bg-blue-500' applies the "
            "background color only when both hover and focus states "
            "are active. Tailwind supports chaining multiple states "
            "like 'dark:hover:focus:text-white' for complex state "
            "combinations."
        ),
        "reference": "https://tailwindcss.com/docs/hover-focus-and-other-states",
        "points": 2,
        "answers": [
            {"text": "hover:focus:bg-blue-500 (chain variants with colons)", "is_correct": True},
            {"text": "hover focus:bg-blue-500 (space-separated variants)", "is_correct": False},
            {"text": "hover&focus:bg-blue-500 (ampersand separator)", "is_correct": False},
            {"text": "hover_focus:bg-blue-500 (underscore separator)", "is_correct": False},
        ],
    },
    {
        "text": (
            "What are Tailwind CSS plugins and how do they extend "
            "functionality? Give an example of a popular plugin and "
            "explain what it adds to Tailwind."
        ),
        "explanation": (
            "Tailwind plugins are JavaScript functions that extend "
            "Tailwind's functionality by adding new utility classes, "
            "components, or base styles. Popular plugins include "
            "@tailwindcss/forms (better form styling), "
            "@tailwindcss/typography (prose styles for rich text), "
            "and @tailwindcss/aspect-ratio (aspect ratio utilities). "
            "Plugins are added in tailwind.config.js under the "
            "'plugins' array and can access Tailwind's API to add styles."
        ),
        "reference": "https://tailwindcss.com/docs/plugins",
        "points": 2,
        "answers": [
            {"text": "JavaScript functions that add new utilities, components, or base styles", "is_correct": True},
            {"text": "NPM packages that provide additional Tailwind configurations", "is_correct": False},
            {"text": "CSS extensions that can be imported via @use statements", "is_correct": False},
            {"text": "Third-party themes that modify Tailwind's default design system", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you handle dark mode in Tailwind CSS? Explain the "
            "configuration options and how to apply different styles "
            "for light and dark themes."
        ),
        "explanation": (
            "Tailwind supports dark mode through the 'dark:' variant "
            "prefix. You configure it in tailwind.config.js with "
            "'darkMode: 'media'' (follows system preference) or "
            "'darkMode: 'class'' (manual toggle via .dark class). "
            "Then use classes like 'bg-white dark:bg-gray-900' and "
            "'text-black dark:text-white'. The 'class' strategy gives "
            "you programmatic control to toggle themes."
        ),
        "reference": "https://tailwindcss.com/docs/dark-mode",
        "points": 2,
        "answers": [
            {"text": "Configure darkMode in config, use dark: prefix (e.g., bg-white dark:bg-gray-900)", "is_correct": True},
            {"text": "Use theme: modifier with light/dark values (e.g., theme:light:bg-white)", "is_correct": False},
            {"text": "Import separate dark.css file with @media (prefers-color-scheme)", "is_correct": False},
            {"text": "Apply dark variants using mode:dark: prefix for all utilities", "is_correct": False},
        ],
    },
    {
        "text": (
            "What is the difference between 'space-x-4' and 'gap-4' "
            "in Tailwind CSS? When would you use each approach for "
            "spacing between elements?"
        ),
        "explanation": (
            "'space-x-4' adds horizontal margin between child elements "
            "(margin-left to all children except first), while 'gap-4' "
            "sets the gap property for flexbox or grid containers. Use "
            "'gap-x-4' for flexbox/grid layouts as it's more modern and "
            "doesn't rely on margins. Use 'space-x-4' for regular block "
            "elements or when you need margin-based spacing. Gap is "
            "generally preferred for flex/grid layouts."
        ),
        "reference": "https://tailwindcss.com/docs/space",
        "points": 2,
        "answers": [
            {"text": "space-x-4 uses margins on children, gap-4 uses CSS gap property for flex/grid", "is_correct": True},
            {"text": "space-x-4 is for grid layouts, gap-4 is for flexbox layouts", "is_correct": False},
            {"text": "Both are identical, gap-4 is the newer syntax for space-x-4", "is_correct": False},
            {"text": "space-x-4 applies padding, gap-4 applies margin between elements", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create custom utility classes in Tailwind CSS "
            "using the @layer directive? Explain the different layers "
            "and when to use each one."
        ),
        "explanation": (
            "The @layer directive allows you to add custom styles to "
            "Tailwind's layers: @layer base (for HTML element defaults), "
            "@layer components (for reusable component classes), and "
            "@layer utilities (for utility classes). Example: '@layer "
            "utilities { .scroll-snap-x { scroll-snap-type: x mandatory; "
            "} }'. This ensures your custom styles are properly ordered "
            "with Tailwind's generated styles and can be purged correctly."
        ),
        "reference": "https://tailwindcss.com/docs/adding-custom-styles#using-css-and-layer",
        "points": 2,
        "answers": [
            {"text": "Use @layer base/components/utilities to add custom styles in the correct order", "is_correct": True},
            {"text": "Use @extend layers to modify existing Tailwind utility classes", "is_correct": False},
            {"text": "Apply @custom directive within theme.extend configuration", "is_correct": False},
            {"text": "Define layers using @mixin base/components/utilities syntax", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a card component with rounded corners, "
            "shadow, padding, and a hover effect that lifts the card. "
            "What Tailwind classes would you use?"
        ),
        "explanation": (
            "For a card: 'rounded-lg' for rounded corners, 'shadow-md' "
            "for shadow, 'p-6' for padding, 'hover:shadow-lg' for "
            "larger shadow on hover, 'transition-shadow' for smooth "
            "transition, and 'duration-300' for timing."
        ),
        "reference": "https://tailwindcss.com/docs/box-shadow",
        "points": 2,
        "answers": [
            {"text": "rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow duration-300", "is_correct": True},
            {"text": "rounded-md shadow-sm p-4 hover:shadow-xl transition-all duration-200", "is_correct": False},
            {"text": "rounded-xl shadow-lg p-8 hover:shadow-2xl transition-transform duration-500", "is_correct": False},
            {"text": "rounded shadow-none p-6 hover:shadow-md transition-shadow ease-in-out", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a responsive navigation bar that stacks "
            "vertically on mobile and horizontally on desktop using Flexbox?"
        ),
        "explanation": (
            "Use 'flex flex-col md:flex-row' to stack vertically on "
            "mobile (flex-col) and horizontally on medium screens and "
            "up (md:flex-row). Add 'items-center' for alignment and "
            "'space-y-4 md:space-y-0 md:space-x-6' for spacing."
        ),
        "reference": "https://tailwindcss.com/docs/flex-direction",
        "points": 2,
        "answers": [
            {"text": "flex flex-col md:flex-row items-center space-y-4 md:space-y-0 md:space-x-6", "is_correct": True},
            {"text": "flex flex-col lg:flex-row justify-center space-y-2 lg:space-y-0 lg:space-x-4", "is_correct": False},
            {"text": "flex flex-column md:flex-horizontal items-start gap-y-4 md:gap-x-6", "is_correct": False},
            {"text": "grid grid-cols-1 md:grid-cols-auto items-center gap-4 md:gap-6", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a form input with focus styles including "
            "a blue border and blue ring. What classes would you use?"
        ),
        "explanation": (
            "Use 'border border-gray-300 focus:border-blue-500 "
            "focus:ring-2 focus:ring-blue-200' for a gray border that "
            "becomes blue on focus with a blue ring. Add 'outline-none' "
            "to remove default outline."
        ),
        "reference": "https://tailwindcss.com/docs/ring-width",
        "points": 2,
        "answers": [
            {"text": "border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 outline-none", "is_correct": True},
            {"text": "border border-gray-400 focus:border-blue-600 focus:ring-1 focus:ring-blue-300 outline-0", "is_correct": False},
            {"text": "border-2 border-gray-200 focus:border-blue-400 focus:ring-3 focus:ring-blue-100", "is_correct": False},
            {"text": "border border-slate-300 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-200", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a CSS Grid layout with 3 columns on "
            "desktop, 2 columns on tablet, and 1 column on mobile?"
        ),
        "explanation": (
            "Use 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3' to "
            "create a responsive grid. 'grid' enables CSS Grid, "
            "'grid-cols-1' sets 1 column by default (mobile), "
            "'md:grid-cols-2' sets 2 columns on medium screens, and "
            "'lg:grid-cols-3' sets 3 columns on large screens."
        ),
        "reference": "https://tailwindcss.com/docs/grid-template-columns",
        "points": 2,
        "answers": [
            {"text": "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3", "is_correct": True},
            {"text": "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3", "is_correct": False},
            {"text": "grid grid-cols-auto md:grid-cols-2 xl:grid-cols-3", "is_correct": False},
            {"text": "grid grid-template-cols-1 md:grid-template-cols-2 lg:grid-template-cols-3", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to hide an element on mobile but show it on "
            "tablet and desktop. Which classes would you use?"
        ),
        "explanation": (
            "Use 'hidden md:block' to hide the element by default "
            "(mobile) and show it as a block element on medium screens "
            "and larger (tablet/desktop). You could also use 'hidden "
            "md:flex' if you need flexbox display."
        ),
        "reference": "https://tailwindcss.com/docs/display",
        "points": 2,
        "answers": [
            {"text": "hidden md:block", "is_correct": True},
            {"text": "hidden sm:block", "is_correct": False},
            {"text": "invisible md:visible", "is_correct": False},
            {"text": "hidden lg:block", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a button with a gradient background "
            "that changes on hover?"
        ),
        "explanation": (
            "Use 'bg-gradient-to-r from-blue-500 to-purple-600 "
            "hover:from-blue-600 hover:to-purple-700' for a "
            "left-to-right gradient that darkens on hover. Add "
            "'transition-all duration-300' for smooth transition."
        ),
        "reference": "https://tailwindcss.com/docs/gradient-color-stops",
        "points": 2,
        "answers": [
            {"text": "bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700", "is_correct": True},
            {"text": "bg-gradient-to-b from-blue-400 to-purple-500 hover:from-blue-500 hover:to-purple-600", "is_correct": False},
            {"text": "bg-gradient-linear from-blue-500 to-purple-600 hover:from-blue-700 hover:to-purple-800", "is_correct": False},
            {"text": "bg-gradient-radial from-blue-500 via-purple-600 hover:from-blue-600 hover:via-purple-700", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a modal overlay that covers the full "
            "screen with a semi-transparent background. What classes "
            "would you use?"
        ),
        "explanation": (
            "Use 'fixed inset-0 bg-black bg-opacity-50 z-50' where "
            "'fixed' positions it relative to viewport, 'inset-0' "
            "covers the full screen (top-0 right-0 bottom-0 left-0), "
            "'bg-black bg-opacity-50' creates semi-transparent black "
            "background, and 'z-50' ensures it's on top."
        ),
        "reference": "https://tailwindcss.com/docs/background-opacity",
        "points": 2,
        "answers": [
            {"text": "fixed inset-0 bg-black bg-opacity-50 z-50", "is_correct": True},
            {"text": "absolute inset-0 bg-gray-900 bg-opacity-75 z-40", "is_correct": False},
            {"text": "fixed top-0 left-0 w-full h-full bg-black/50 z-50", "is_correct": False},
            {"text": "sticky inset-0 bg-slate-800 opacity-50 z-index-50", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a sticky header that stays at the "
            "top of the page when scrolling?"
        ),
        "explanation": (
            "Use 'sticky top-0 z-40' where 'sticky' creates a sticky "
            "positioned element, 'top-0' positions it at the top when "
            "sticky, and 'z-40' ensures it stays above other content. "
            "You might also add 'bg-white shadow-md' for styling."
        ),
        "reference": "https://tailwindcss.com/docs/position",
        "points": 2,
        "answers": [
            {"text": "sticky top-0 z-40", "is_correct": True},
            {"text": "fixed top-0 z-40", "is_correct": False},
            {"text": "sticky top-0 z-index-40", "is_correct": False},
            {"text": "relative sticky-top z-40", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a loading spinner using CSS animations. "
            "What Tailwind classes would you use?"
        ),
        "explanation": (
            "Use 'animate-spin' for continuous rotation animation. "
            "For a spinner, you might use it on a div with 'w-8 h-8 "
            "border-4 border-blue-500 border-t-transparent rounded-full' "
            "to create a spinning circle with a transparent section."
        ),
        "reference": "https://tailwindcss.com/docs/animation",
        "points": 2,
        "answers": [
            {"text": "animate-spin w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full", "is_correct": True},
            {"text": "animate-pulse w-6 h-6 border-2 border-blue-400 border-top-transparent rounded-full", "is_correct": False},
            {"text": "animate-bounce w-8 h-8 bg-blue-500 rounded-full", "is_correct": False},
            {"text": "animate-rotate w-10 h-10 border-3 border-blue-600 border-t-clear rounded-circle", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a responsive image that maintains its "
            "aspect ratio and doesn't overflow its container?"
        ),
        "explanation": (
            "Use 'w-full h-auto object-cover' where 'w-full' makes "
            "it take full width of container, 'h-auto' maintains "
            "aspect ratio, and 'object-cover' ensures it covers the "
            "container without distortion. For a specific aspect "
            "ratio, you could use 'aspect-w-16 aspect-h-9' with the "
            "aspect-ratio plugin."
        ),
        "reference": "https://tailwindcss.com/docs/object-fit",
        "points": 2,
        "answers": [
            {"text": "w-full h-auto object-cover", "is_correct": True},
            {"text": "w-auto h-full object-fit", "is_correct": False},
            {"text": "max-w-full max-h-full object-contain", "is_correct": False},
            {"text": "w-100 h-auto object-scale-down", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a tooltip that appears on hover. How "
            "would you position it above the trigger element?"
        ),
        "explanation": (
            "Use 'relative' on the trigger element and 'absolute "
            "bottom-full left-1/2 transform -translate-x-1/2 mb-2' "
            "on the tooltip. This positions it absolutely above the "
            "trigger (bottom-full), centers it horizontally "
            "(left-1/2 -translate-x-1/2), and adds margin (mb-2)."
        ),
        "reference": "https://tailwindcss.com/docs/position",
        "points": 2,
        "answers": [
            {"text": "absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2", "is_correct": True},
            {"text": "absolute top-full left-1/2 transform -translate-x-1/2 mt-2", "is_correct": False},
            {"text": "fixed bottom-100 left-50 translate-x-[-50%] mb-2", "is_correct": False},
            {"text": "relative top-0 left-center transform -translate-x-half mb-2", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a sidebar layout where the sidebar is "
            "fixed width and the main content takes the remaining space?"
        ),
        "explanation": (
            "Use 'flex' on the container, 'w-64 flex-shrink-0' on "
            "the sidebar (fixed width, no shrinking), and 'flex-1' "
            "on the main content (takes remaining space). You could "
            "also use 'min-h-screen' on the container for full height."
        ),
        "reference": "https://tailwindcss.com/docs/flex",
        "points": 2,
        "answers": [
            {"text": "Container: flex, Sidebar: w-64 flex-shrink-0, Main: flex-1", "is_correct": True},
            {"text": "Container: grid grid-cols-[250px_1fr], Sidebar: w-full, Main: w-full", "is_correct": False},
            {"text": "Container: flex, Sidebar: w-1/4 flex-none, Main: w-3/4", "is_correct": False},
            {"text": "Container: block, Sidebar: fixed w-64, Main: ml-64", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to style a form validation error message with "
            "red text and a red border on the input. What classes "
            "would you use?"
        ),
        "explanation": (
            "For the input: 'border-red-500 focus:border-red-500 "
            "focus:ring-red-200' and for the error message: "
            "'text-red-500 text-sm mt-1'. You might also add "
            "'bg-red-50' to the input for a subtle red background."
        ),
        "reference": "https://tailwindcss.com/docs/text-color",
        "points": 2,
        "answers": [
            {"text": "Input: border-red-500 focus:ring-red-200, Message: text-red-500 text-sm", "is_correct": True},
            {"text": "Input: border-red-400 focus:ring-red-300, Message: text-red-600 text-xs", "is_correct": False},
            {"text": "Input: ring-red-500 focus:border-red-400, Message: text-rose-500 text-base", "is_correct": False},
            {"text": "Input: outline-red-500 focus:outline-red-600, Message: text-red-700 text-lg", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a responsive typography scale where "
            "headings are smaller on mobile and larger on desktop?"
        ),
        "explanation": (
            "Use responsive text utilities like 'text-2xl md:text-4xl "
            "lg:text-5xl' for a heading that starts at 2xl on mobile, "
            "becomes 4xl on medium screens, and 5xl on large screens. "
            "You can also adjust line height with 'leading-tight "
            "md:leading-none'."
        ),
        "reference": "https://tailwindcss.com/docs/font-size",
        "points": 2,
        "answers": [
            {"text": "text-2xl md:text-4xl lg:text-5xl leading-tight md:leading-none", "is_correct": True},
            {"text": "text-xl sm:text-3xl md:text-4xl leading-normal sm:leading-tight", "is_correct": False},
            {"text": "text-lg md:text-2xl xl:text-4xl line-height-sm md:line-height-none", "is_correct": False},
            {"text": "text-base md:text-xl lg:text-3xl leading-relaxed md:leading-snug", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a hamburger menu icon that transforms "
            "into an X when clicked. What approach would you take "
            "with Tailwind?"
        ),
        "explanation": (
            "Create three bars with 'w-6 h-0.5 bg-gray-800 "
            "transition-all duration-300'. Use JavaScript to toggle "
            "classes: first bar 'rotate-45 translate-y-2', middle "
            "bar 'opacity-0', third bar '-rotate-45 -translate-y-2' "
            "to form an X shape."
        ),
        "reference": "https://tailwindcss.com/docs/transform",
        "points": 2,
        "answers": [
            {"text": "Use transform classes with rotate-45, translate, and opacity with transition-all", "is_correct": True},
            {"text": "Use transform classes with rotate-90, scale, and visibility with transition-transform", "is_correct": False},
            {"text": "Use animation classes with spin, fade, and translate with duration-500", "is_correct": False},
            {"text": "Use matrix transforms with rotate-30, skew, and opacity with ease-in-out", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a progress bar that fills from 0% "
            "to any percentage?"
        ),
        "explanation": (
            "Create a container with 'w-full bg-gray-200 rounded-full "
            "h-4' and a progress element inside with 'bg-blue-500 "
            "h-4 rounded-full transition-all duration-500' with "
            "dynamic width using 'w-[${percentage}%]' or by setting "
            "the width with JavaScript/CSS variables."
        ),
        "reference": "https://tailwindcss.com/docs/width",
        "points": 2,
        "answers": [
            {"text": "Container: w-full bg-gray-200 rounded-full, Progress: bg-blue-500 h-4 rounded-full with dynamic width", "is_correct": True},
            {"text": "Container: w-screen bg-slate-300 rounded, Progress: bg-indigo-500 h-3 rounded with flex-grow", "is_correct": False},
            {"text": "Container: max-w-full bg-gray-100 pill-shape, Progress: bg-cyan-500 full-height with transform-scale", "is_correct": False},
            {"text": "Container: w-auto bg-neutral-200 curved, Progress: bg-emerald-500 h-5 with animate-pulse", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a dropdown menu that appears below "
            "a button. How would you position it correctly?"
        ),
        "explanation": (
            "Use 'relative' on the button container and 'absolute "
            "top-full left-0 mt-2 z-50' on the dropdown. 'top-full' "
            "positions it below the button, 'left-0' aligns it to "
            "the left edge, 'mt-2' adds space, and 'z-50' ensures "
            "it appears above other content."
        ),
        "reference": "https://tailwindcss.com/docs/position",
        "points": 2,
        "answers": [
            {"text": "Button container: relative, Dropdown: absolute top-full left-0 mt-2 z-50", "is_correct": True},
            {"text": "Button container: static, Dropdown: fixed bottom-full right-0 mb-2 z-40", "is_correct": False},
            {"text": "Button container: relative, Dropdown: absolute bottom-0 left-full ml-2 z-30", "is_correct": False},
            {"text": "Button container: sticky, Dropdown: absolute top-0 right-full mr-2 z-60", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a card grid that automatically adjusts "
            "the number of columns based on available space?"
        ),
        "explanation": (
            "Use 'grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))]' "
            "or the simpler 'grid grid-cols-1 sm:grid-cols-2 "
            "lg:grid-cols-3 xl:grid-cols-4' for responsive breakpoints. "
            "The auto-fit approach automatically fits as many columns "
            "as possible based on the minimum width."
        ),
        "reference": "https://tailwindcss.com/docs/grid-template-columns",
        "points": 2,
        "answers": [
            {"text": "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 or auto-fit with minmax", "is_correct": True},
            {"text": "grid grid-cols-auto md:grid-cols-2 lg:grid-cols-4 with gap-auto", "is_correct": False},
            {"text": "flex flex-wrap with flex-basis-1/3 md:flex-basis-1/4 lg:flex-basis-1/5", "is_correct": False},
            {"text": "grid grid-template-responsive with cols-fit-content and auto-columns", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a search input with an icon inside. "
            "How would you position the icon?"
        ),
        "explanation": (
            "Use 'relative' on the container, style the input with "
            "'pl-10' (left padding for icon space), and position "
            "the icon with 'absolute left-3 top-1/2 transform "
            "-translate-y-1/2'. This centers the icon vertically "
            "and positions it inside the input."
        ),
        "reference": "https://tailwindcss.com/docs/position",
        "points": 2,
        "answers": [
            {"text": "Container: relative, Input: pl-10, Icon: absolute left-3 top-1/2 transform -translate-y-1/2", "is_correct": True},
            {"text": "Container: static, Input: pr-8, Icon: fixed right-2 top-1/2 transform -translate-y-1/2", "is_correct": False},
            {"text": "Container: relative, Input: px-12, Icon: absolute left-4 bottom-1/2 transform translate-y-1/2", "is_correct": False},
            {"text": "Container: flex, Input: flex-1 pl-8, Icon: absolute left-2 center transform -translate-center", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a badge or chip component with rounded "
            "corners and a close button?"
        ),
        "explanation": (
            "Use 'inline-flex items-center px-3 py-1 rounded-full "
            "text-sm bg-blue-100 text-blue-800' for the badge "
            "container, and 'ml-2 w-4 h-4 cursor-pointer "
            "hover:bg-blue-200 rounded-full' for the close button "
            "with an × icon inside."
        ),
        "reference": "https://tailwindcss.com/docs/border-radius",
        "points": 2,
        "answers": [
            {"text": "inline-flex items-center px-3 py-1 rounded-full text-sm bg-blue-100 text-blue-800", "is_correct": True},
            {"text": "flex items-center px-4 py-2 rounded-lg text-base bg-indigo-200 text-indigo-900", "is_correct": False},
            {"text": "inline-block px-2 py-0.5 rounded-xl text-xs bg-purple-50 text-purple-700", "is_correct": False},
            {"text": "span items-baseline px-5 py-1.5 rounded-md text-lg bg-cyan-300 text-cyan-800", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a responsive table that becomes "
            "horizontally scrollable on mobile. What approach "
            "would you use?"
        ),
        "explanation": (
            "Wrap the table in a div with 'overflow-x-auto' and "
            "optionally add 'min-w-full' to the table itself. For "
            "better mobile experience, you might also use "
            "'whitespace-nowrap' on cells to prevent text wrapping "
            "and add 'scrollbar-thin' if you have the scrollbar plugin."
        ),
        "reference": "https://tailwindcss.com/docs/overflow",
        "points": 2,
        "answers": [
            {"text": "Wrapper: overflow-x-auto, Table: min-w-full, Cells: whitespace-nowrap", "is_correct": True},
            {"text": "Wrapper: overflow-scroll, Table: w-max, Cells: text-truncate", "is_correct": False},
            {"text": "Wrapper: scroll-x-hidden, Table: max-w-screen, Cells: break-words", "is_correct": False},
            {"text": "Wrapper: overflow-auto, Table: w-screen, Cells: whitespace-pre-wrap", "is_correct": False},
        ],
    },
      {
        "text": (
            "How do you create a skeleton loading animation for a card "
            "while content is loading?"
        ),
        "explanation": (
            "Use 'animate-pulse' on a container with placeholder "
            "elements. For example: 'bg-gray-300 rounded' for shapes "
            "and 'h-4 bg-gray-300 rounded' for text lines. The pulse "
            "animation creates a subtle shimmer effect that indicates "
            "loading."
        ),
        "reference": "https://tailwindcss.com/docs/animation",
        "points": 2,
        "answers": [
            {"text": "animate-pulse with bg-gray-300 rounded placeholder elements", "is_correct": True},
            {"text": "animate-bounce with bg-slate-200 rounded-lg placeholders", "is_correct": False},
            {"text": "animate-spin with bg-gray-400 circular loading elements", "is_correct": False},
            {"text": "animate-ping with bg-neutral-300 square shimmer blocks", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a testimonial card with a quote icon "
            "positioned partially outside the card. How would you "
            "achieve this?"
        ),
        "explanation": (
            "Use 'relative' on the card and 'absolute -top-4 left-4' "
            "on the quote icon to position it partially outside the "
            "card's top boundary. You might also add 'bg-white "
            "rounded-full p-2' to the icon container for better "
            "visibility."
        ),
        "reference": "https://tailwindcss.com/docs/position",
        "points": 2,
        "answers": [
            {"text": "Card: relative, Icon: absolute -top-4 left-4 bg-white rounded-full p-2", "is_correct": True},
            {"text": "Card: static, Icon: fixed -top-6 left-6 bg-gray-100 rounded-lg p-3", "is_correct": False},
            {"text": "Card: relative, Icon: absolute -bottom-2 right-2 bg-blue-50 pill p-1", "is_correct": False},
            {"text": "Card: sticky, Icon: absolute -top-8 center bg-white circular p-4", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a responsive pricing table with "
            "highlighted 'popular' plan in the center?"
        ),
        "explanation": (
            "Use 'grid grid-cols-1 md:grid-cols-3 gap-6' for the "
            "container. For the popular plan, add 'transform "
            "md:scale-105 md:-mt-4' to make it slightly larger and "
            "elevated. Add 'ring-2 ring-blue-500' for a blue "
            "border highlight."
        ),
        "reference": "https://tailwindcss.com/docs/scale",
        "points": 2,
        "answers": [
            {"text": "Grid layout with transform md:scale-105 md:-mt-4 ring-2 ring-blue-500 on popular plan", "is_correct": True},
            {"text": "Flex layout with transform lg:scale-110 lg:-mb-6 border-4 border-green-400", "is_correct": False},
            {"text": "Grid layout with zoom md:scale-120 md:-my-8 outline-3 outline-purple-600", "is_correct": False},
            {"text": "Block layout with enlarge md:scale-100 md:-mt-2 shadow-xl shadow-red-500", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a tabbed interface where only the "
            "active tab content is visible. What classes would you use?"
        ),
        "explanation": (
            "Use 'hidden' class on all tab content panels by default, "
            "then use JavaScript to toggle 'hidden' class off the "
            "active panel. For tab buttons, use 'border-b-2 "
            "border-transparent' by default and 'border-blue-500 "
            "text-blue-600' for active state."
        ),
        "reference": "https://tailwindcss.com/docs/display",
        "points": 2,
        "answers": [
            {"text": "Tab content: hidden (toggle off for active), Tab buttons: border-b-2 with active states", "is_correct": True},
            {"text": "Tab content: invisible (toggle visible for active), Tab buttons: border-t-2 with focus states", "is_correct": False},
            {"text": "Tab content: opacity-0 (toggle opacity-100 for active), Tab buttons: underline with hover states", "is_correct": False},
            {"text": "Tab content: scale-0 (toggle scale-100 for active), Tab buttons: ring-2 with selected states", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a footer that sticks to the bottom "
            "of the page even when content is short?"
        ),
        "explanation": (
            "Use 'min-h-screen flex flex-col' on the body/main "
            "container, 'flex-1' on the main content area to take "
            "available space, and the footer will naturally stick "
            "to the bottom. Alternatively, use 'grid min-h-screen "
            "grid-rows-[1fr,auto]'."
        ),
        "reference": "https://tailwindcss.com/docs/min-height",
        "points": 2,
        "answers": [
            {"text": "Container: min-h-screen flex flex-col, Main: flex-1, Footer: natural positioning", "is_correct": True},
            {"text": "Container: h-full grid grid-rows-auto, Main: flex-grow, Footer: sticky bottom-0", "is_correct": False},
            {"text": "Container: min-h-full flex flex-column, Main: flex-auto, Footer: absolute bottom-0", "is_correct": False},
            {"text": "Container: height-screen flex vertical, Main: expand-1, Footer: fixed bottom", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a image gallery with lightbox effect. "
            "How would you approach the overlay and modal?"
        ),
        "explanation": (
            "Use 'fixed inset-0 bg-black bg-opacity-75 z-50 flex "
            "items-center justify-center' for the lightbox overlay. "
            "The image inside can have 'max-w-full max-h-full "
            "object-contain' to fit properly. Add 'transition-opacity "
            "duration-300' for smooth appearance."
        ),
        "reference": "https://tailwindcss.com/docs/background-opacity",
        "points": 2,
        "answers": [
            {"text": "fixed inset-0 bg-black bg-opacity-75 z-50 flex items-center justify-center", "is_correct": True},
            {"text": "absolute full-screen bg-gray-900 opacity-80 z-40 grid place-items-center", "is_correct": False},
            {"text": "sticky viewport bg-slate-800 bg-opacity-60 z-30 flex content-center", "is_correct": False},
            {"text": "relative overlay bg-dark transparency-70 z-index-high flex middle-center", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a notification toast that slides in "
            "from the top right corner?"
        ),
        "explanation": (
            "Use 'fixed top-4 right-4 z-50 transform translate-x-full' "
            "initially (hidden off-screen), then remove 'translate-x-full' "
            "and add 'transition-transform duration-300' to slide it "
            "in. Include 'bg-white shadow-lg rounded-lg p-4' for styling."
        ),
        "reference": "https://tailwindcss.com/docs/translate",
        "points": 2,
        "answers": [
            {"text": "fixed top-4 right-4 z-50 transform translate-x-full with transition-transform", "is_correct": True},
            {"text": "absolute top-0 right-0 z-40 transform translate-y-full with transition-all", "is_correct": False},
            {"text": "sticky top-2 right-2 z-60 transform scale-0 with transition-scale", "is_correct": False},
            {"text": "relative corner-top-right z-50 transform rotate-90 with transition-rotate", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a responsive dashboard layout with "
            "a collapsible sidebar. What approach would you take?"
        ),
        "explanation": (
            "Use 'transform -translate-x-full lg:translate-x-0' on "
            "the sidebar to hide it on mobile and show it on large "
            "screens. Add 'transition-transform duration-300' for "
            "smooth animation. Use JavaScript to toggle "
            "'translate-x-0' class for mobile sidebar visibility."
        ),
        "reference": "https://tailwindcss.com/docs/translate",
        "points": 2,
        "answers": [
            {"text": "transform -translate-x-full lg:translate-x-0 with transition-transform and JS toggle", "is_correct": True},
            {"text": "transform -translate-y-full md:translate-y-0 with transition-all and CSS toggle", "is_correct": False},
            {"text": "transform scale-0 xl:scale-100 with transition-scale and hover toggle", "is_correct": False},
            {"text": "transform rotate-90 lg:rotate-0 with transition-rotate and media toggle", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a multi-step form progress indicator "
            "with connected lines?"
        ),
        "explanation": (
            "Use flex layout with circles for steps and connecting "
            "lines. Steps: 'w-8 h-8 rounded-full flex items-center "
            "justify-center' with conditional 'bg-blue-500 text-white' "
            "for completed/active steps. Connecting lines: 'flex-1 "
            "h-1 bg-gray-300' between steps."
        ),
        "reference": "https://tailwindcss.com/docs/flex",
        "points": 2,
        "answers": [
            {"text": "Flex layout with rounded circles and flex-1 connecting lines with conditional styling", "is_correct": True},
            {"text": "Grid layout with circular steps and grid-auto-flow connecting bars with state classes", "is_correct": False},
            {"text": "Block layout with rounded divs and absolute positioned lines with active indicators", "is_correct": False},
            {"text": "Inline layout with pill shapes and floating connectors with progress markers", "is_correct": False},
        ],
    },
    {
        "text": (
            "You want to create a image comparison slider (before/after). "
            "How would you implement the slider handle and positioning?"
        ),
        "explanation": (
            "Use 'relative overflow-hidden' on container. Position "
            "after image with 'absolute top-0 left-0 w-full h-full' "
            "and clip it with 'clip-path' or use a mask. The slider "
            "handle can be 'absolute top-0 bottom-0 w-1 bg-white' "
            "with drag functionality to update the clipping width."
        ),
        "reference": "https://tailwindcss.com/docs/position",
        "points": 2,
        "answers": [
            {"text": "relative overflow-hidden container with absolute positioned images and draggable handle", "is_correct": True},
            {"text": "static overflow-visible container with fixed positioned images and clickable slider", "is_correct": False},
            {"text": "sticky overflow-scroll container with relative positioned images and hover handle", "is_correct": False},
            {"text": "absolute overflow-auto container with sticky positioned images and animated divider", "is_correct": False},
        ],
    },
    {
        "text": (
            "How do you create a accordion component where only one "
            "panel can be open at a time?"
        ),
        "explanation": (
            "Use 'border border-gray-200 rounded-lg' for each panel. "
            "Headers have 'cursor-pointer p-4 hover:bg-gray-50'. "
            "Content panels use 'hidden' by default, toggle to "
            "'block' with 'p-4 border-t' for active panel. Use "
            "JavaScript to manage which panel is open."
        ),
        "reference": "https://tailwindcss.com/docs/display",
        "points": 2,
        "answers": [
            {"text": "Border panels with cursor-pointer headers and hidden/block content with JS state management", "is_correct": True},
            {"text": "Shadow panels with hover-cursor headers and invisible/visible content with CSS state control", "is_correct": False},
            {"text": "Ring panels with pointer-cursor headers and opacity-0/opacity-100 content with animation state", "is_correct": False},
            {"text": "Outline panels with click-cursor headers and scale-0/scale-100 content with transform state", "is_correct": False},
        ],
    },
    {
        "text": (
            "You need to create a drag-and-drop file upload area "
            "with visual feedback. What styling approach would you use?"
        ),
        "explanation": (
            "Use 'border-2 border-dashed border-gray-300 rounded-lg "
            "p-8 text-center' for the drop zone. Add "
            "'hover:border-blue-400 hover:bg-blue-50' for hover "
            "state and 'border-blue-500 bg-blue-50' for drag-over "
            "state using JavaScript to toggle classes."
        ),
        "reference": "https://tailwindcss.com/docs/border-style",
        "points": 2,
        "answers": [
            {"text": "border-2 border-dashed with hover and drag-over state classes using JS", "is_correct": True},
            {"text": "border-4 border-dotted with focus and active state classes using CSS", "is_correct": False},
            {"text": "outline-2 outline-dashed with mouseover and drop state classes using jQuery", "is_correct": False},
            {"text": "ring-2 ring-dashed with enter and leave state classes using React", "is_correct": False},
        ],
    },

]