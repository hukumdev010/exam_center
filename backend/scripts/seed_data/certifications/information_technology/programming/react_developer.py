"""React Developer Certification"""

CERTIFICATION = {
    "name": "React Developer Certification",
    "description": "React.js framework expertise",
    "slug": "react-developer-certification",
    "level": "Associate",
    "duration": 120,
    "questions_count": 66,
    "category_slug": "programming",
    "is_active": True,
}

QUESTIONS = [
    {
        "text": "When implementing a React component that needs to synchronize with an external data store and prevent memory leaks, which pattern would be the most appropriate for handling subscription cleanup in useEffect?",
        "explanation": "The correct pattern is to return a cleanup function from useEffect that unsubscribes from the external store. This ensures that subscriptions are properly cleaned up when the component unmounts or when dependencies change, preventing memory leaks.",
        "reference": "https://react.dev/reference/react/useEffect#subscribing-to-an-external-store",
        "points": 2,
        "answers": [
            {"text": "Use useLayoutEffect with async/await for cleanup operations", "is_correct": False},
            {"text": "Return a cleanup function from useEffect that handles unsubscription", "is_correct": True},
            {"text": "Use multiple useEffect hooks without cleanup functions", "is_correct": False},
            {"text": "Implement cleanup in componentWillUnmount only", "is_correct": False}
        ]
    },
    {
        "text": "In React's reconciliation process, what happens when you change the key prop of a component during re-rendering, and why is this behavior crucial for performance optimization?",
        "explanation": "When a component's key changes, React treats it as a completely different component, unmounting the old instance and mounting a new one. This resets all state and triggers lifecycle methods. This behavior is crucial for forcing component resets and optimizing lists where item identity changes.",
        "reference": "https://react.dev/learn/preserving-and-resetting-state#option-2-resetting-state-with-a-key",
        "points": 2,
        "answers": [
            {"text": "React updates the component in-place while preserving its state", "is_correct": False},
            {"text": "React unmounts the old component and mounts a new instance, resetting all state", "is_correct": True},
            {"text": "React only updates the DOM attributes without affecting component lifecycle", "is_correct": False},
            {"text": "React batches the key change with other updates for better performance", "is_correct": False}
        ]
    },
    {
        "text": "What is the primary difference between React.memo and useMemo, and in which scenario would you choose React.memo over useMemo for optimizing component re-renders?",
        "explanation": "React.memo is a higher-order component that prevents unnecessary re-renders of the entire component when props haven't changed, while useMemo memoizes expensive calculations inside a component. React.memo should be used when you want to prevent the entire component from re-rendering based on prop changes.",
        "reference": "https://react.dev/reference/react/memo",
        "points": 2,
        "answers": [
            {"text": "React.memo memoizes function results, useMemo prevents component re-renders", "is_correct": False},
            {"text": "React.memo prevents component re-renders when props are unchanged, useMemo memoizes expensive calculations", "is_correct": True},
            {"text": "React.memo is for class components, useMemo is for functional components", "is_correct": False},
            {"text": "React.memo and useMemo are interchangeable optimization techniques", "is_correct": False}
        ]
    },
    {
        "text": "When implementing a custom hook that manages asynchronous operations, what pattern should you follow to handle race conditions where multiple async operations might complete in different orders?",
        "explanation": "The correct pattern is to use a cleanup function or AbortController to cancel pending operations when the component unmounts or when dependencies change. This prevents race conditions where a later request might be overwritten by an earlier one that completes later.",
        "reference": "https://react.dev/reference/react/useEffect#fetching-data-with-effects",
        "points": 3,
        "answers": [
            {"text": "Always use the latest response regardless of request order", "is_correct": False},
            {"text": "Implement request cancellation using AbortController or cleanup functions", "is_correct": True},
            {"text": "Queue all requests and process them sequentially", "is_correct": False},
            {"text": "Use setTimeout to delay request processing", "is_correct": False}
        ]
    },
    {
        "text": "In React's concurrent features, what is the purpose of the useTransition hook, and how does it differ from useDeferredValue in terms of user interaction prioritization?",
        "explanation": "useTransition allows you to mark state updates as non-urgent transitions, keeping the UI responsive during expensive operations. useDeferredValue defers updating a value until more urgent updates finish. useTransition is for controlling when updates happen, while useDeferredValue is for deferring specific values.",
        "reference": "https://react.dev/reference/react/useTransition",
        "points": 3,
        "answers": [
            {"text": "useTransition defers values, useDeferredValue marks transitions as non-urgent", "is_correct": False},
            {"text": "useTransition marks updates as non-urgent, useDeferredValue defers specific value updates", "is_correct": True},
            {"text": "Both hooks serve identical purposes and are interchangeable", "is_correct": False},
            {"text": "useTransition is for animations, useDeferredValue is for data fetching", "is_correct": False}
        ]
    },
    {
        "text": "What happens when you call setState multiple times synchronously in React 18, and how does automatic batching affect the number of re-renders compared to React 17?",
        "explanation": "In React 18, automatic batching groups multiple setState calls into a single re-render, even outside of React event handlers (like in timeouts, promises, etc.). This reduces the number of re-renders compared to React 17, which only batched updates inside React event handlers.",
        "reference": "https://react.dev/blog/2022/03/29/react-v18#new-feature-automatic-batching",
        "points": 2,
        "answers": [
            {"text": "Each setState call triggers a separate re-render in both versions", "is_correct": False},
            {"text": "React 18 automatically batches all setState calls, React 17 only batched in event handlers", "is_correct": True},
            {"text": "React 18 prevents all re-renders until the next tick", "is_correct": False},
            {"text": "Batching behavior is identical between React 17 and 18", "is_correct": False}
        ]
    },
    {
        "text": "When implementing error boundaries in React, why can't you catch errors that occur during event handlers, and what is the recommended approach for handling such errors?",
        "explanation": "Error boundaries cannot catch errors in event handlers because these errors don't occur during rendering. Event handler errors don't break the component tree. The recommended approach is to use try-catch blocks within event handlers or implement global error handling.",
        "reference": "https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary",
        "points": 2,
        "answers": [
            {"text": "Event handler errors are automatically handled by React's error boundary system", "is_correct": False},
            {"text": "Error boundaries don't catch event handler errors; use try-catch blocks instead", "is_correct": True},
            {"text": "Event handler errors cause the entire application to crash without recovery", "is_correct": False},
            {"text": "Error boundaries only work in production mode for event handlers", "is_correct": False}
        ]
    },
    {
        "text": "In React's Context API, what performance implications arise when you have multiple consumers of the same context, and how can you optimize context updates to prevent unnecessary re-renders?",
        "explanation": "When context value changes, all consuming components re-render regardless of which part of the context they use. Optimization strategies include splitting contexts, memoizing context values, using selectors, or implementing context selectors with custom hooks to subscribe to specific parts of the context.",
        "reference": "https://react.dev/learn/passing-data-deeply-with-context#before-you-use-context",
        "points": 3,
        "answers": [
            {"text": "Context automatically optimizes updates to prevent unnecessary re-renders", "is_correct": False},
            {"text": "All context consumers re-render on any context change; optimize by splitting contexts or using selectors", "is_correct": True},
            {"text": "Only components that directly use changed context properties will re-render", "is_correct": False},
            {"text": "Context performance is identical to prop drilling in terms of re-renders", "is_correct": False}
        ]
    },
    {
        "text": "What is the difference between useCallback and useMemo in terms of what they memoize, and provide a specific scenario where useCallback would be essential for performance optimization?",
        "explanation": "useCallback memoizes the function itself, while useMemo memoizes the result of calling a function. useCallback is essential when passing callbacks to optimized child components (wrapped in React.memo) to prevent unnecessary re-renders caused by new function references on every render.",
        "reference": "https://react.dev/reference/react/useCallback",
        "points": 2,
        "answers": [
            {"text": "useCallback memoizes function results, useMemo memoizes the function reference", "is_correct": False},
            {"text": "useCallback memoizes function references, useMemo memoizes computed values", "is_correct": True},
            {"text": "Both hooks memoize function results but with different syntax", "is_correct": False},
            {"text": "useCallback is for async functions, useMemo is for synchronous functions", "is_correct": False}
        ]
    },
    {
        "text": "When working with React's Suspense feature for data fetching, what happens to components that are suspended, and how does React handle the fallback UI during the suspension period?",
        "explanation": "When a component suspends (throws a promise), React stops rendering that component and its children, then looks up the tree for the nearest Suspense boundary. The Suspense boundary renders the fallback UI while waiting for the promise to resolve, after which it attempts to render the suspended component again.",
        "reference": "https://react.dev/reference/react/Suspense",
        "points": 3,
        "answers": [
            {"text": "Suspended components continue rendering with placeholder data", "is_correct": False},
            {"text": "React renders the fallback UI and retries the suspended component when the promise resolves", "is_correct": True},
            {"text": "Suspended components cause the entire page to show a loading state", "is_correct": False},
            {"text": "React queues suspended components for background rendering", "is_correct": False}
        ]
    },
    {
        "text": "In React's strict mode, why are components rendered twice during development, and what specific issues does this double rendering help developers identify in their code?",
        "explanation": "Strict mode double-renders components to help identify side effects and ensure components are pure. It helps catch issues like functions that mutate props/state, components that rely on single-execution assumptions, or components that don't handle being called multiple times correctly.",
        "reference": "https://react.dev/reference/react/StrictMode",
        "points": 2,
        "answers": [
            {"text": "Double rendering tests component performance under heavy load", "is_correct": False},
            {"text": "Double rendering helps identify side effects and ensures component purity", "is_correct": True},
            {"text": "Double rendering simulates React's concurrent rendering behavior", "is_correct": False},
            {"text": "Double rendering is used to test component memory usage", "is_correct": False}
        ]
    },
    {
        "text": "When implementing a React application with server-side rendering (SSR), what is hydration, and what common issues can cause hydration mismatches between server and client?",
        "explanation": "Hydration is the process where React attaches event listeners and makes the server-rendered HTML interactive. Mismatches occur when server and client render different content, often due to date/time differences, random values, browser-only APIs, or conditional rendering based on client-side state.",
        "reference": "https://react.dev/reference/react-dom/client/hydrateRoot",
        "points": 3,
        "answers": [
            {"text": "Hydration replaces server HTML with client-rendered components", "is_correct": False},
            {"text": "Hydration attaches interactivity to server HTML; mismatches occur from different server/client rendering", "is_correct": True},
            {"text": "Hydration only handles event listener attachment without content verification", "is_correct": False},
            {"text": "Hydration is the process of loading CSS styles on the client side", "is_correct": False}
        ]
    },
    {
        "text": "What is the significance of React keys in list rendering, and why does using array indices as keys potentially cause issues in dynamic lists with reordering capabilities?",
        "explanation": "Keys help React identify which items have changed, been added, or removed during reconciliation. Using array indices as keys can cause issues when items are reordered because React might incorrectly match components, leading to state being preserved in wrong items or performance problems.",
        "reference": "https://react.dev/learn/rendering-lists#why-does-react-need-keys",
        "points": 2,
        "answers": [
            {"text": "Array indices always provide optimal performance for React reconciliation", "is_correct": False},
            {"text": "Array indices can cause incorrect component matching and state preservation issues in dynamic lists", "is_correct": True},
            {"text": "Keys are only necessary for styling purposes in React lists", "is_correct": False},
            {"text": "Array indices are the recommended approach for all list scenarios", "is_correct": False}
        ]
    },
    {
        "text": "In React's useReducer hook, what advantages does it provide over useState when managing complex state logic, and when should you consider migrating from useState to useReducer?",
        "explanation": "useReducer is beneficial for complex state logic involving multiple sub-values, when next state depends on previous state, or when you need to optimize performance by passing dispatch down instead of callbacks. Consider migrating when useState logic becomes complex, involves multiple related state updates, or when you need predictable state transitions.",
        "reference": "https://react.dev/reference/react/useReducer",
        "points": 2,
        "answers": [
            {"text": "useReducer is only useful for Redux-style global state management", "is_correct": False},
            {"text": "useReducer helps with complex state logic, multiple related updates, and performance optimization", "is_correct": True},
            {"text": "useReducer automatically prevents all unnecessary re-renders", "is_correct": False},
            {"text": "useReducer is required for all state management in functional components", "is_correct": False}
        ]
    },
    {
        "text": "When implementing ref forwarding in React, what problem does React.forwardRef solve, and why is it necessary when creating reusable component libraries?",
        "explanation": "React.forwardRef allows parent components to access DOM elements inside child components by forwarding refs through component boundaries. It's necessary for reusable libraries because it enables imperative actions (like focus, scroll) and integration with third-party libraries that need direct DOM access.",
        "reference": "https://react.dev/reference/react/forwardRef",
        "points": 2,
        "answers": [
            {"text": "forwardRef automatically manages component lifecycle methods", "is_correct": False},
            {"text": "forwardRef enables parent access to child DOM elements through ref forwarding", "is_correct": True},
            {"text": "forwardRef prevents memory leaks in component hierarchies", "is_correct": False},
            {"text": "forwardRef is only used for performance optimization in large applications", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of the dependency array in React hooks like useEffect and useMemo, and what are the potential consequences of omitting dependencies or providing an incorrect dependency list?",
        "explanation": "The dependency array tells React when to re-run the effect or recalculate the memoized value. Omitting dependencies can lead to stale closures and bugs where effects don't update with current values. Incorrect dependencies can cause infinite loops or missed updates, leading to unexpected behavior.",
        "reference": "https://react.dev/reference/react/useEffect#specifying-reactive-dependencies",
        "points": 2,
        "answers": [
            {"text": "Dependencies only affect performance, not correctness of the code", "is_correct": False},
            {"text": "Dependencies control when effects run; incorrect dependencies cause stale closures and bugs", "is_correct": True},
            {"text": "Dependencies are optional and mainly used for code organization", "is_correct": False},
            {"text": "Dependencies prevent components from re-rendering entirely", "is_correct": False}
        ]
    },
    {
        "text": "In React's concurrent rendering, what is the difference between urgent and non-urgent updates, and how does React prioritize these different types of updates to maintain responsiveness?",
        "explanation": "Urgent updates are user-initiated interactions (clicks, typing) that need immediate feedback. Non-urgent updates include data fetching results or animations. React prioritizes urgent updates to maintain responsiveness, potentially interrupting and resuming non-urgent work to handle urgent updates first.",
        "reference": "https://react.dev/blog/2022/03/29/react-v18#what-is-concurrent-react",
        "points": 3,
        "answers": [
            {"text": "All updates have equal priority in React's concurrent rendering", "is_correct": False},
            {"text": "Urgent updates (user interactions) are prioritized over non-urgent updates (data fetching)", "is_correct": True},
            {"text": "Non-urgent updates always complete before urgent updates can begin", "is_correct": False},
            {"text": "Update priority is determined randomly by React's scheduler", "is_correct": False}
        ]
    },
    {
        "text": "When creating a custom hook that manages component mounting state to prevent state updates on unmounted components, what pattern should you implement to avoid memory leaks and React warnings?",
        "explanation": "The pattern involves using useRef to track mounting state and useEffect to set a cleanup function that marks the component as unmounted. Check this ref before any asynchronous state updates to prevent 'setState on unmounted component' warnings and potential memory leaks.",
        "reference": "https://react.dev/reference/react/useEffect#fetching-data-with-effects",
        "points": 3,
        "answers": [
            {"text": "Use useState to track mounting state and check it before updates", "is_correct": False},
            {"text": "Use useRef to track mounting state and cleanup function to mark unmounted", "is_correct": True},
            {"text": "Rely on React's automatic cleanup of pending state updates", "is_correct": False},
            {"text": "Use global variables to track component mounting state", "is_correct": False}
        ]
    },
    {
        "text": "What is React's reconciliation algorithm, and how does it determine whether to update, create, or destroy DOM elements during the diffing process?",
        "explanation": "React's reconciliation algorithm compares new virtual DOM with previous virtual DOM. It uses heuristics: different element types create new DOM nodes, same types update props, and keys help identify moved elements in lists. This process minimizes expensive DOM operations while keeping the UI in sync.",
        "reference": "https://react.dev/learn/preserving-and-resetting-state#the-ui-tree",
        "points": 3,
        "answers": [
            {"text": "React recreates the entire DOM tree on every update for consistency", "is_correct": False},
            {"text": "React compares virtual DOM trees using element types, props, and keys to minimize DOM operations", "is_correct": True},
            {"text": "React only updates DOM elements that have changed CSS styles", "is_correct": False},
            {"text": "React uses machine learning to predict which DOM updates are necessary", "is_correct": False}
        ]
    },
    {
        "text": "In React's portal feature (ReactDOM.createPortal), what problem does it solve, and what are the important considerations regarding event bubbling and context propagation?",
        "explanation": "Portals solve the problem of rendering children into DOM nodes outside the parent component's hierarchy, useful for modals and tooltips. Event bubbling still follows React's component tree (not DOM tree), and React context is preserved through portals, maintaining the logical component relationship.",
        "reference": "https://react.dev/reference/react-dom/createPortal",
        "points": 2,
        "answers": [
            {"text": "Portals only change visual rendering without affecting React's logical tree", "is_correct": False},
            {"text": "Portals render outside parent DOM while preserving event bubbling and context through React tree", "is_correct": True},
            {"text": "Portals break event bubbling and context propagation for security reasons", "is_correct": False},
            {"text": "Portals are only used for performance optimization in large applications", "is_correct": False}
        ]
    },
    {
        "text": "When implementing code splitting in React applications using React.lazy and Suspense, what happens during the loading process, and how can you handle loading errors gracefully?",
        "explanation": "React.lazy dynamically imports components, returning a promise. During loading, the component suspends and Suspense shows fallback UI. Loading errors can be handled using Error Boundaries around the Suspense component, as lazy loading failures are treated as rendering errors.",
        "reference": "https://react.dev/reference/react/lazy",
        "points": 3,
        "answers": [
            {"text": "Loading errors automatically retry without additional error handling needed", "is_correct": False},
            {"text": "Use Error Boundaries around Suspense to catch lazy loading failures", "is_correct": True},
            {"text": "Lazy loading errors cause the entire application to crash without recovery", "is_correct": False},
            {"text": "Loading states are handled automatically by React.lazy without Suspense", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of React's useLayoutEffect hook, and in what specific scenarios should you choose useLayoutEffect over useEffect for DOM manipulation?",
        "explanation": "useLayoutEffect runs synchronously after all DOM mutations but before the browser paints, making it suitable for DOM measurements and synchronous DOM updates that need to happen before the user sees the result. Use it when you need to read layout from DOM or make DOM changes that should be visible immediately.",
        "reference": "https://react.dev/reference/react/useLayoutEffect",
        "points": 3,
        "answers": [
            {"text": "useLayoutEffect is only for class components, useEffect is for functional components", "is_correct": False},
            {"text": "useLayoutEffect runs synchronously before paint, ideal for DOM measurements and immediate updates", "is_correct": True},
            {"text": "useLayoutEffect has better performance than useEffect in all scenarios", "is_correct": False},
            {"text": "useLayoutEffect automatically prevents all layout shifts in React applications", "is_correct": False}
        ]
    },
    {
        "text": "When working with React's useImperativeHandle hook, what specific problem does it solve in the context of ref forwarding, and why should its usage be limited?",
        "explanation": "useImperativeHandle customizes the instance value exposed through refs, allowing parent components to call specific methods on child components. It should be limited because it breaks React's declarative paradigm and can make components harder to reason about. It's mainly useful for integrating with imperative libraries.",
        "reference": "https://react.dev/reference/react/useImperativeHandle",
        "points": 3,
        "answers": [
            {"text": "useImperativeHandle is the preferred method for all parent-child communication", "is_correct": False},
            {"text": "useImperativeHandle exposes custom methods through refs but breaks declarative patterns", "is_correct": True},
            {"text": "useImperativeHandle automatically optimizes component rendering performance", "is_correct": False},
            {"text": "useImperativeHandle is required for all functional components using refs", "is_correct": False}
        ]
    },
    {
        "text": "In React's development environment, what is the purpose of the React Developer Tools profiler, and what specific performance metrics does it help developers identify and optimize?",
        "explanation": "The React Profiler helps identify performance bottlenecks by showing which components rendered, why they rendered, and how long rendering took. It helps optimize unnecessary re-renders, expensive computations, and component update patterns by providing flame graphs and interaction tracking.",
        "reference": "https://react.dev/learn/react-developer-tools",
        "points": 2,
        "answers": [
            {"text": "Profiler only shows component hierarchy without performance information", "is_correct": False},
            {"text": "Profiler identifies rendering performance, unnecessary re-renders, and component update patterns", "is_correct": True},
            {"text": "Profiler automatically fixes all performance issues in React applications", "is_correct": False},
            {"text": "Profiler only works in production builds for accurate measurements", "is_correct": False}
        ]
    },
    {
        "text": "What happens when you pass an object or array as a dependency to useEffect, and why might this cause unexpected behavior or infinite re-renders in your React component?",
        "explanation": "Objects and arrays are compared by reference, not by value. If you create a new object/array on each render (even with identical contents), useEffect will see it as a changed dependency and re-run, potentially causing infinite loops. This is why dependencies should be primitive values or stable references.",
        "reference": "https://react.dev/reference/react/useEffect#specifying-reactive-dependencies",
        "points": 2,
        "answers": [
            {"text": "React automatically deep compares objects and arrays in dependency arrays", "is_correct": False},
            {"text": "Objects/arrays are compared by reference, causing re-runs when references change even with same content", "is_correct": True},
            {"text": "useEffect ignores object and array dependencies for performance reasons", "is_correct": False},
            {"text": "React converts all dependencies to strings before comparison", "is_correct": False}
        ]
    },
    {
        "text": "When implementing a React component that needs to integrate with a third-party DOM library (like a charting library), what lifecycle considerations and patterns should you follow to ensure proper cleanup and avoid conflicts?",
        "explanation": "Use useEffect for initialization and return a cleanup function to destroy the third-party library instance. Use refs to store library instances, ensure the library doesn't interfere with React's DOM management, and consider using useLayoutEffect if the library needs synchronous DOM access before paint.",
        "reference": "https://react.dev/learn/escape-hatches#integrating-with-non-react-widgets",
        "points": 3,
        "answers": [
            {"text": "Third-party libraries automatically integrate with React without special considerations", "is_correct": False},
            {"text": "Use useEffect for setup/cleanup, refs for instances, and ensure proper DOM lifecycle management", "is_correct": True},
            {"text": "Only class components can properly integrate with third-party DOM libraries", "is_correct": False},
            {"text": "Third-party integrations should be handled in component constructors only", "is_correct": False}
        ]
    },
    {
        "text": "In React's state management, what is the difference between local component state, lifted state, and derived state, and when should you choose each approach?",
        "explanation": "Local state belongs to a single component, lifted state is moved up to share between components, and derived state is computed from other state/props. Use local state for component-specific data, lift state when multiple components need access, and derive state when values can be calculated from existing data.",
        "reference": "https://react.dev/learn/sharing-state-between-components",
        "points": 2,
        "answers": [
            {"text": "All state should be local to components for better performance", "is_correct": False},
            {"text": "Use local state for component data, lift for sharing, derive for computed values", "is_correct": True},
            {"text": "Derived state should always be stored in component state for reliability", "is_correct": False},
            {"text": "State management approach doesn't affect component reusability or maintainability", "is_correct": False}
        ]
    },
    {
        "text": "What is React's Fiber architecture, and how does it improve upon the previous reconciliation algorithm in terms of handling large component trees and maintaining responsiveness?",
        "explanation": "Fiber is React's reconciliation engine that breaks rendering work into units that can be paused and resumed. It enables React to prioritize urgent updates, interrupt less important work, and maintain 60fps by yielding control back to the browser when needed, unlike the previous synchronous stack reconciler.",
        "reference": "https://github.com/acdlite/react-fiber-architecture",
        "points": 3,
        "answers": [
            {"text": "Fiber only improves memory usage without affecting rendering performance", "is_correct": False},
            {"text": "Fiber enables interruptible rendering, work prioritization, and maintains responsiveness", "is_correct": True},
            {"text": "Fiber eliminates the virtual DOM to improve performance", "is_correct": False},
            {"text": "Fiber is only beneficial for server-side rendering scenarios", "is_correct": False}
        ]
    },
    {
        "text": "When using React's Context API for theme management, what performance optimization strategies can you implement to prevent unnecessary re-renders when only specific theme properties change?",
        "explanation": "Split theme context into multiple contexts (colors, typography, spacing), use React.memo on consumers, memoize context values to prevent object recreation, implement context selectors with custom hooks, or use state management libraries designed for granular subscriptions.",
        "reference": "https://react.dev/learn/passing-data-deeply-with-context#before-you-use-context",
        "points": 3,
        "answers": [
            {"text": "Context automatically optimizes for partial theme updates without additional work", "is_correct": False},
            {"text": "Split contexts, memoize values, use React.memo, or implement context selectors", "is_correct": True},
            {"text": "Always use global state management instead of Context for theme management", "is_correct": False},
            {"text": "Theme changes should trigger full application re-renders for consistency", "is_correct": False}
        ]
    },
    {
        "text": "In React applications using TypeScript, what are the benefits of using discriminated unions for props, and how do they improve type safety and developer experience in component APIs?",
        "explanation": "Discriminated unions use a common property to distinguish between different prop configurations, preventing invalid prop combinations and enabling TypeScript to narrow types automatically. This improves type safety by catching invalid prop combinations at compile time and provides better IntelliSense.",
        "reference": "https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html#discriminating-unions",
        "points": 2,
        "answers": [
            {"text": "Discriminated unions only improve runtime performance without type benefits", "is_correct": False},
            {"text": "Discriminated unions prevent invalid prop combinations and enable automatic type narrowing", "is_correct": True},
            {"text": "Discriminated unions are only useful for styling props in React components", "is_correct": False},
            {"text": "Discriminated unions eliminate the need for prop validation in React", "is_correct": False}
        ]
    },
    {
        "text": "When implementing optimistic updates in a React application, what patterns should you follow to handle rollback scenarios when the server operation fails, and how do you maintain data consistency?",
        "explanation": "Implement optimistic updates by immediately updating local state, storing the previous state for rollback, and reverting to the previous state if the server request fails. Use techniques like optimistic IDs, conflict resolution strategies, and proper error handling to maintain data consistency.",
        "reference": "https://react.dev/reference/react/useOptimistic",
        "points": 3,
        "answers": [
            {"text": "Optimistic updates should never be rolled back to maintain user experience", "is_correct": False},
            {"text": "Store previous state, revert on failure, handle conflicts, and use optimistic IDs", "is_correct": True},
            {"text": "Server failures in optimistic updates should cause full page reloads", "is_correct": False},
            {"text": "Optimistic updates automatically handle all failure scenarios without additional code", "is_correct": False}
        ]
    },
    {
        "text": "What are React Server Components, and how do they differ from traditional client-side components in terms of rendering location, capabilities, and limitations?",
        "explanation": "React Server Components render on the server and send rendered output to the client, reducing bundle size and enabling direct data access. They can't use browser APIs, event handlers, or most hooks, but can access server resources directly. They complement, not replace, client components.",
        "reference": "https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components",
        "points": 3,
        "answers": [
            {"text": "Server Components are just server-side rendered versions of regular React components", "is_correct": False},
            {"text": "Server Components render on server, can't use browser APIs, but access server resources directly", "is_correct": True},
            {"text": "Server Components completely replace the need for client-side React components", "is_correct": False},
            {"text": "Server Components only provide SEO benefits without other advantages", "is_correct": False}
        ]
    },
    {
        "text": "In React testing, what is the difference between shallow rendering and full DOM rendering, and when would you choose each approach for testing different aspects of component behavior?",
        "explanation": "Shallow rendering only renders the component itself without child components, useful for unit testing component logic in isolation. Full DOM rendering renders the complete component tree, better for integration testing, testing component interactions, and behavior that depends on child components.",
        "reference": "https://testing-library.com/docs/react-testing-library/intro/",
        "points": 2,
        "answers": [
            {"text": "Shallow rendering is always preferred for better test performance", "is_correct": False},
            {"text": "Shallow rendering for unit tests, full DOM rendering for integration and interaction testing", "is_correct": True},
            {"text": "Full DOM rendering should be avoided due to performance implications", "is_correct": False},
            {"text": "Both approaches test identical component behavior and are interchangeable", "is_correct": False}
        ]
    },
    {
        "text": "When implementing a React component library, what considerations should you make regarding prop forwarding, component composition, and ensuring components are flexible enough for various use cases?",
        "explanation": "Design for composition over inheritance, use render props or children functions for flexibility, implement proper prop forwarding with forwardRef, provide sensible defaults while allowing customization, use compound components for related functionality, and ensure accessibility and theming support.",
        "reference": "https://react.dev/learn/passing-props-to-a-component",
        "points": 3,
        "answers": [
            {"text": "Component libraries should be highly opinionated with minimal customization options", "is_correct": False},
            {"text": "Focus on composition, prop forwarding, render props, defaults, and accessibility", "is_correct": True},
            {"text": "All component library props should be required to ensure consistent usage", "is_correct": False},
            {"text": "Component libraries should avoid using React patterns like forwardRef", "is_correct": False}
        ]
    },
    {
        "text": "What is the purpose of React's useSyncExternalStore hook, and in what scenarios would you use it instead of useState or useEffect for managing external data sources?",
        "explanation": "useSyncExternalStore safely subscribes to external stores (like browser APIs or third-party state management) that exist outside React's control. It handles the subscription/unsubscription lifecycle and ensures consistent values during concurrent rendering, preventing tearing and race conditions.",
        "reference": "https://react.dev/reference/react/useSyncExternalStore",
        "points": 3,
        "answers": [
            {"text": "useSyncExternalStore is only for Redux integration in React applications", "is_correct": False},
            {"text": "useSyncExternalStore safely subscribes to external stores and prevents tearing in concurrent rendering", "is_correct": True},
            {"text": "useSyncExternalStore replaces all useState usage for better performance", "is_correct": False},
            {"text": "useSyncExternalStore is deprecated in favor of useEffect for external data", "is_correct": False}
        ]
    },
    {
        "text": "In React's concurrent features, what is tearing, and how do React 18's new hooks like useSyncExternalStore and useId help prevent common issues in concurrent rendering?",
        "explanation": "Tearing occurs when different parts of the UI show inconsistent data during concurrent rendering. useSyncExternalStore prevents tearing by ensuring consistent external store values, while useId generates stable unique IDs that remain consistent between server and client rendering, preventing hydration mismatches.",
        "reference": "https://react.dev/blog/2022/03/29/react-v18#new-feature-concurrent-features",
        "points": 3,
        "answers": [
            {"text": "Tearing is a performance optimization technique used in React's concurrent rendering", "is_correct": False},
            {"text": "Tearing is inconsistent data display; useSyncExternalStore and useId prevent related issues", "is_correct": True},
            {"text": "Tearing only affects server-side rendering and has no impact on client rendering", "is_correct": False},
            {"text": "React 18 eliminates all possibility of tearing without requiring special hooks", "is_correct": False}
        ]
    },
    {
        "text": "When implementing a React component that renders a large dataset with virtualization, what performance considerations should you account for regarding component re-renders and memory usage optimization?",
        "explanation": "For large datasets with virtualization, implement proper memoization for row renderers, use stable keys, implement proper cleanup for DOM elements outside viewport, optimize scroll event handling with throttling/debouncing, and ensure minimal re-renders by memoizing expensive calculations and using React.memo strategically.",
        "reference": "https://react.dev/learn/rendering-lists#optimizing-re-renders-when-list-items-can-move-around",
        "points": 3,
        "answers": [
            {"text": "React automatically optimizes all virtualized lists without additional considerations", "is_correct": False},
            {"text": "Implement memoization, stable keys, proper cleanup, and optimized scroll handling", "is_correct": True},
            {"text": "Only focus on DOM manipulation without React-specific optimizations", "is_correct": False},
            {"text": "Virtualization eliminates all performance concerns in React applications", "is_correct": False}
        ]
    },
    {
        "text": "In React's new use() hook proposal, how does it differ from useEffect for data fetching, and what advantages does it provide for handling promises and async operations in components?",
        "explanation": "The use() hook can read promises and context, works in both server and client components, suspends the component until the promise resolves, and integrates better with React's concurrent features compared to useEffect which requires manual state management for async operations.",
        "reference": "https://react.dev/reference/react/use",
        "points": 3,
        "answers": [
            {"text": "use() is identical to useEffect but with different syntax for async operations", "is_correct": False},
            {"text": "use() can read promises directly, suspends components, and works with concurrent features", "is_correct": True},
            {"text": "use() only works in class components for backward compatibility", "is_correct": False},
            {"text": "use() replaces all useState operations in functional components", "is_correct": False}
        ]
    },
    {
        "text": "When implementing a React form with complex validation logic, dynamic fields, and real-time updates, what patterns should you use to manage form state efficiently while preventing unnecessary re-renders?",
        "explanation": "Use uncontrolled components with refs for performance-critical fields, implement field-level subscriptions, use libraries like React Hook Form that minimize re-renders, memoize validation functions, debounce expensive validations, and consider splitting large forms into smaller components with local state.",
        "reference": "https://react.dev/learn/managing-state#choosing-the-state-structure",
        "points": 3,
        "answers": [
            {"text": "Always use controlled components with useState for all form fields", "is_correct": False},
            {"text": "Mix controlled/uncontrolled patterns, use field subscriptions, memoize validations, and split forms", "is_correct": True},
            {"text": "Store all form data in global state to prevent local re-renders", "is_correct": False},
            {"text": "Avoid any state management and use only DOM APIs for form handling", "is_correct": False}
        ]
    },
    {
        "text": "In React's experimental features, what is the purpose of the startTransition API, and how does it work with time slicing to improve user experience during expensive updates?",
        "explanation": "startTransition marks updates as non-urgent, allowing React to interrupt them for more urgent work like user interactions. Time slicing breaks work into chunks, yielding control back to the browser to maintain 60fps and responsiveness during expensive operations like large list updates or complex calculations.",
        "reference": "https://react.dev/reference/react/startTransition",
        "points": 3,
        "answers": [
            {"text": "startTransition only affects animation performance without impacting other updates", "is_correct": False},
            {"text": "startTransition enables interruptible updates and time slicing for responsiveness", "is_correct": True},
            {"text": "startTransition automatically optimizes all component re-renders", "is_correct": False},
            {"text": "startTransition is only useful for server-side rendering optimizations", "is_correct": False}
        ]
    },
    {
        "text": "When building a React application with micro-frontend architecture, what challenges arise with state sharing, event communication, and component isolation, and how should you address them?",
        "explanation": "Challenges include isolated bundle contexts, different React versions, state synchronization across apps, and event communication. Solutions include using module federation, shared state libraries, custom events, standardized communication protocols, and careful dependency management to prevent version conflicts.",
        "reference": "https://react.dev/learn/sharing-state-between-components",
        "points": 3,
        "answers": [
            {"text": "Micro-frontends eliminate all state sharing and communication challenges", "is_correct": False},
            {"text": "Use module federation, shared libraries, custom events, and careful dependency management", "is_correct": True},
            {"text": "Each micro-frontend should operate completely independently without any shared resources", "is_correct": False},
            {"text": "Global variables are the recommended approach for micro-frontend communication", "is_correct": False}
        ]
    },
    {
        "text": "In React's Strict Mode, what additional development behaviors does it enforce beyond double rendering, and why are these behaviors crucial for identifying potential issues in concurrent React?",
        "explanation": "Strict Mode also double-invokes constructor, render, and state updater functions, warns about deprecated APIs, detects unexpected side effects, ensures reusable state, and helps identify components that don't handle being called multiple times correctly, which is crucial for concurrent rendering reliability.",
        "reference": "https://react.dev/reference/react/StrictMode#enabling-strict-mode-for-entire-app",
        "points": 2,
        "answers": [
            {"text": "Strict Mode only affects rendering behavior without other development checks", "is_correct": False},
            {"text": "Double-invokes functions, warns about deprecated APIs, and detects side effects for concurrent safety", "is_correct": True},
            {"text": "Strict Mode automatically fixes all detected issues in the application", "is_correct": False},
            {"text": "Strict Mode is only useful for class components and has no effect on hooks", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components that need to work with Web Components, what integration challenges do you face, and what patterns ensure proper data flow and event handling between React and Web Components?",
        "explanation": "Challenges include property vs attribute differences, event system incompatibilities, and lifecycle mismatches. Use refs to access Web Component APIs, handle custom events with addEventListener, convert React props to appropriate attributes/properties, and use useEffect for lifecycle synchronization.",
        "reference": "https://react.dev/reference/react-dom/components#custom-html-elements",
        "points": 3,
        "answers": [
            {"text": "React and Web Components integrate seamlessly without any special considerations", "is_correct": False},
            {"text": "Use refs for APIs, handle custom events, convert props appropriately, and sync lifecycles", "is_correct": True},
            {"text": "Web Components cannot be used within React applications", "is_correct": False},
            {"text": "Only class components can properly integrate with Web Components", "is_correct": False}
        ]
    },
    {
        "text": "In React's useDebugValue hook, what is its primary purpose, and how does it enhance the developer experience when creating and debugging custom hooks in development tools?",
        "explanation": "useDebugValue provides a way to display custom hook values in React Developer Tools. It accepts a value and optional formatting function, only runs in development mode, and helps developers understand custom hook state and behavior during debugging without affecting production performance.",
        "reference": "https://react.dev/reference/react/useDebugValue",
        "points": 2,
        "answers": [
            {"text": "useDebugValue improves runtime performance by optimizing hook execution", "is_correct": False},
            {"text": "useDebugValue displays custom hook values in React Developer Tools for debugging", "is_correct": True},
            {"text": "useDebugValue automatically validates hook usage and prevents common mistakes", "is_correct": False},
            {"text": "useDebugValue is required for all custom hooks to function properly", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components for a design system library, what considerations should you make regarding prop polymorphism, composition patterns, and ensuring components remain flexible while maintaining type safety?",
        "explanation": "Implement 'as' prop for polymorphic components, use render props or children functions for flexibility, provide proper TypeScript generics, use composition over inheritance, implement proper prop forwarding, and consider compound component patterns for related functionality while maintaining strong typing.",
        "reference": "https://react.dev/learn/passing-props-to-a-component#forwarding-props-with-the-jsx-spread-syntax",
        "points": 3,
        "answers": [
            {"text": "Design systems should use fixed component APIs without polymorphism for consistency", "is_correct": False},
            {"text": "Use polymorphic props, composition patterns, TypeScript generics, and proper forwarding", "is_correct": True},
            {"text": "Type safety is not important in design system components", "is_correct": False},
            {"text": "All design system components should be implemented as higher-order components", "is_correct": False}
        ]
    },
    {
        "text": "In React's upcoming features, what is the purpose of the Offscreen component, and how does it enable new patterns for performance optimization and user experience improvements?",
        "explanation": "Offscreen allows components to render in background without being visible, enabling prerendering, maintaining component state while hidden, implementing tabs without unmounting, and preparing content before it's needed, leading to instant transitions and improved perceived performance.",
        "reference": "https://react.dev/blog/2022/03/29/react-v18#react-18-release-notes",
        "points": 3,
        "answers": [
            {"text": "Offscreen only provides CSS visibility controls without React-specific benefits", "is_correct": False},
            {"text": "Offscreen enables background rendering, state preservation, and preloading for instant transitions", "is_correct": True},
            {"text": "Offscreen replaces the need for code splitting and lazy loading", "is_correct": False},
            {"text": "Offscreen is only useful for mobile applications with limited resources", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components that need to handle focus management for accessibility, what patterns should you follow for focus trapping, restoration, and keyboard navigation in modal dialogs and complex UI interactions?",
        "explanation": "Implement focus trapping with sentinel elements, restore focus to triggering element on close, handle Tab and Shift+Tab cycling, manage focus for dynamic content, use proper ARIA attributes, and consider using libraries like focus-trap-react for robust focus management while ensuring screen reader compatibility.",
        "reference": "https://react.dev/learn/managing-focus-for-accessibility",
        "points": 3,
        "answers": [
            {"text": "Browser default focus behavior is sufficient for all React accessibility needs", "is_correct": False},
            {"text": "Implement focus trapping, restoration, keyboard navigation, and proper ARIA attributes", "is_correct": True},
            {"text": "Focus management is only necessary for users with disabilities", "is_correct": False},
            {"text": "React automatically handles all focus management without developer intervention", "is_correct": False}
        ]
    },
    {
        "text": "In React's scheduler package, what is the role of the MessageChannel API and how does it contribute to React's ability to perform time slicing and maintain frame rate during expensive operations?",
        "explanation": "MessageChannel provides a way to yield control back to the browser's main thread after each unit of work, allowing React to check if higher priority work needs to be done. This enables time slicing by breaking work into chunks and maintaining 60fps during expensive rendering operations.",
        "reference": "https://github.com/facebook/react/tree/main/packages/scheduler",
        "points": 3,
        "answers": [
            {"text": "MessageChannel is only used for communication between React components", "is_correct": False},
            {"text": "MessageChannel enables yielding to browser for time slicing and frame rate maintenance", "is_correct": True},
            {"text": "MessageChannel replaces all event handling in React applications", "is_correct": False},
            {"text": "MessageChannel is deprecated in favor of newer browser APIs", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React applications with internationalization (i18n), what performance and architectural considerations should you account for regarding bundle splitting, dynamic locale loading, and RTL support?",
        "explanation": "Implement locale-based code splitting, lazy load translation bundles, consider plural rules complexity, handle RTL layout changes, optimize number/date formatting, cache translations appropriately, and use libraries like react-i18next with proper Suspense integration for dynamic loading.",
        "reference": "https://react.dev/learn/conditional-rendering#conditionally-including-jsx",
        "points": 3,
        "answers": [
            {"text": "Load all translations upfront to avoid complexity in React applications", "is_correct": False},
            {"text": "Implement locale splitting, lazy loading, RTL handling, and proper caching strategies", "is_correct": True},
            {"text": "Internationalization only affects text content without other considerations", "is_correct": False},
            {"text": "React has built-in i18n support that handles all internationalization needs", "is_correct": False}
        ]
    },
    {
        "text": "In React's experimental Flight framework (React Server Components), what is the significance of the server/client boundary, and how does serialization of data work between server and client environments?",
        "explanation": "The server/client boundary determines what can be passed between environments. Server Components can access server resources but can't use client-side APIs. Data serialization is handled automatically by React Flight, but complex objects like functions can't cross the boundary, requiring careful API design.",
        "reference": "https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components",
        "points": 3,
        "answers": [
            {"text": "All React component code can seamlessly execute in both server and client environments", "is_correct": False},
            {"text": "Server/client boundary defines serialization limits and environment-specific capabilities", "is_correct": True},
            {"text": "React Flight eliminates all differences between server and client component execution", "is_correct": False},
            {"text": "Serialization is manual and requires explicit developer configuration for all data", "is_correct": False}
        ]
    },
    {
        "text": "When building React applications with real-time features using WebSockets or Server-Sent Events, what patterns should you implement to handle connection lifecycle, reconnection logic, and state synchronization effectively?",
        "explanation": "Implement custom hooks for connection management, handle reconnection with exponential backoff, maintain connection state in context, sync optimistic updates with server state, handle connection drops gracefully, and implement proper cleanup to prevent memory leaks when components unmount.",
        "reference": "https://react.dev/learn/synchronizing-with-effects#connecting-to-an-external-system",
        "points": 3,
        "answers": [
            {"text": "WebSocket connections should be managed globally outside of React component lifecycle", "is_correct": False},
            {"text": "Use custom hooks, handle reconnection, sync state, and implement proper cleanup", "is_correct": True},
            {"text": "React's built-in networking automatically handles all real-time connection scenarios", "is_correct": False},
            {"text": "Real-time features require class components to properly manage connection state", "is_correct": False}
        ]
    },
    {
        "text": "In React's performance optimization techniques, what is the difference between bailout optimizations and memoization, and when does React's automatic bailout mechanism prevent unnecessary work during reconciliation?",
        "explanation": "Bailout optimization occurs when React skips rendering a component subtree because props haven't changed (shallow comparison) or state update results in same value. Memoization (React.memo, useMemo) requires explicit implementation. Bailout is automatic but limited to reference equality checks.",
        "reference": "https://react.dev/learn/render-and-commit#step-2-react-renders-your-components",
        "points": 3,
        "answers": [
            {"text": "Bailout and memoization are identical optimization techniques with different names", "is_correct": False},
            {"text": "Bailout is automatic shallow comparison optimization, memoization requires explicit implementation", "is_correct": True},
            {"text": "Memoization always provides better performance than React's bailout mechanism", "is_correct": False},
            {"text": "Bailout optimization only works with class components, not functional components", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components that interact with browser APIs like Intersection Observer, Resize Observer, or Mutation Observer, what patterns ensure proper cleanup and avoid performance issues?",
        "explanation": "Use useEffect with proper cleanup functions to disconnect observers, implement debouncing/throttling for frequent callbacks, use refs to store observer instances, handle edge cases like component unmounting during observation, and consider using custom hooks to encapsulate observer logic for reusability.",
        "reference": "https://react.dev/learn/synchronizing-with-effects#subscribing-to-an-external-store",
        "points": 3,
        "answers": [
            {"text": "Browser observers automatically clean up when React components unmount", "is_correct": False},
            {"text": "Use useEffect cleanup, debouncing, refs for instances, and custom hooks for reusability", "is_correct": True},
            {"text": "Observer APIs should only be used in class component lifecycle methods", "is_correct": False},
            {"text": "React provides built-in hooks for all browser observer APIs", "is_correct": False}
        ]
    },
    {
        "text": "In React's upcoming selective hydration feature, what problems does it solve regarding SSR performance, and how does it prioritize which parts of the application to hydrate based on user interactions?",
        "explanation": "Selective hydration allows React to hydrate components on-demand based on user interactions, solving the problem of blocking hydration where the entire page must hydrate before becoming interactive. It prioritizes components the user is trying to interact with, enabling faster Time to Interactive.",
        "reference": "https://react.dev/blog/2021/06/08/the-plan-for-react-18#selective-hydration",
        "points": 3,
        "answers": [
            {"text": "Selective hydration only improves SEO without affecting user interaction performance", "is_correct": False},
            {"text": "Selective hydration enables on-demand component hydration based on user interactions", "is_correct": True},
            {"text": "Selective hydration eliminates the need for server-side rendering entirely", "is_correct": False},
            {"text": "Selective hydration only works with static content, not interactive components", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components for data visualization with D3.js or similar libraries, what integration challenges exist, and what patterns ensure smooth coordination between React's virtual DOM and D3's direct DOM manipulation?",
        "explanation": "Challenges include React and D3 both wanting DOM control, different update patterns, and event handling conflicts. Use React for structure and D3 for visualization logic, let React own the DOM with refs for D3 access, use useEffect for D3 lifecycle, and consider hybrid approaches or React-specific charting libraries.",
        "reference": "https://react.dev/learn/manipulating-the-dom-with-refs#how-to-manage-a-list-of-refs-using-a-ref-callback",
        "points": 3,
        "answers": [
            {"text": "D3 and React cannot be used together due to fundamental incompatibilities", "is_correct": False},
            {"text": "Use React for structure, D3 for visualization, with refs and useEffect for coordination", "is_correct": True},
            {"text": "Always let D3 control all DOM manipulation when building data visualizations", "is_correct": False},
            {"text": "React automatically optimizes all third-party DOM manipulation libraries", "is_correct": False}
        ]
    },
    {
        "text": "In React's error handling system, what is the difference between error boundaries and the onError event handler in terms of error catching scope, and what types of errors can each handle effectively?",
        "explanation": "Error boundaries catch errors during rendering, lifecycle methods, and constructors in the component tree below them, but can't catch errors in event handlers, async code, or errors in the error boundary itself. onError handles global JavaScript errors including event handlers and async operations not caught by error boundaries.",
        "reference": "https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary",
        "points": 2,
        "answers": [
            {"text": "Error boundaries and onError handle identical error types with the same scope", "is_correct": False},
            {"text": "Error boundaries catch render/lifecycle errors, onError handles global errors including async/events", "is_correct": True},
            {"text": "onError is deprecated in favor of error boundaries for all error handling scenarios", "is_correct": False},
            {"text": "Error boundaries can catch all possible JavaScript errors in React applications", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React applications with complex animation sequences using libraries like Framer Motion or React Transition Group, what performance considerations and patterns should you follow to maintain 60fps during transitions?",
        "explanation": "Use CSS transforms and opacity for GPU acceleration, minimize layout thrashing, implement proper will-change CSS properties, use useLayoutEffect for DOM measurements, debounce expensive animations, consider reduced motion preferences, and optimize component re-renders during animation sequences.",
        "reference": "https://react.dev/learn/synchronizing-with-effects#measuring-layout",
        "points": 3,
        "answers": [
            {"text": "JavaScript-based animations always perform better than CSS animations in React", "is_correct": False},
            {"text": "Use GPU-accelerated properties, minimize layout thrashing, and optimize re-renders", "is_correct": True},
            {"text": "Animation performance is automatically optimized by React without developer consideration", "is_correct": False},
            {"text": "Complex animations should always be implemented using canvas instead of DOM elements", "is_correct": False}
        ]
    },
    {
        "text": "In React's concurrent rendering architecture, what is the significance of lanes (priority levels), and how does React's scheduler use them to determine which updates to process first during time slicing?",
        "explanation": "Lanes represent different priority levels for updates (sync, default, transition, retry, etc.). React's scheduler uses lanes to determine update priority, allowing urgent updates like user input to interrupt less important work like data fetching, ensuring responsive user interactions during concurrent rendering.",
        "reference": "https://github.com/facebook/react/blob/main/packages/react-reconciler/src/ReactFiberLane.js",
        "points": 3,
        "answers": [
            {"text": "Lanes are only used for debugging purposes without affecting rendering behavior", "is_correct": False},
            {"text": "Lanes represent update priorities that enable React scheduler to prioritize urgent work", "is_correct": True},
            {"text": "All React updates have equal priority regardless of their lane assignment", "is_correct": False},
            {"text": "Lanes are automatically assigned and cannot be influenced by developer code", "is_correct": False}
        ]
    },
    {
        "text": "When building React applications with advanced routing requirements like parallel routes, nested layouts, and data preloading, what architectural patterns and considerations should guide your implementation strategy?",
        "explanation": "Implement route-based code splitting, use nested route data loading, implement parallel route rendering with Suspense, consider layout preservation strategies, use route preloading for better UX, handle route transitions gracefully, and implement proper error boundaries for route-level error handling.",
        "reference": "https://react.dev/learn/conditional-rendering#conditionally-rendering-nothing-with-null",
        "points": 3,
        "answers": [
            {"text": "Simple client-side routing is sufficient for all React application routing needs", "is_correct": False},
            {"text": "Implement code splitting, nested loading, parallel routes, and proper error boundaries", "is_correct": True},
            {"text": "All routing logic should be handled outside of React components for separation of concerns", "is_correct": False},
            {"text": "Advanced routing features negatively impact application performance and should be avoided", "is_correct": False}
        ]
    },
    {
        "text": "In React's development workflow, what is the purpose of the __REACT_DEVTOOLS_GLOBAL_HOOK__, and how does it enable React Developer Tools to inspect component state, props, and performance across different React applications?",
        "explanation": "The global hook provides a standardized interface for React DevTools to communicate with React applications, allowing inspection of component trees, state changes, prop values, and performance profiling. It works across different React versions and enables features like component highlighting and time-travel debugging.",
        "reference": "https://react.dev/learn/react-developer-tools#browser-extension",
        "points": 2,
        "answers": [
            {"text": "The global hook is only used for error reporting in production React applications", "is_correct": False},
            {"text": "The global hook enables React DevTools communication and inspection capabilities", "is_correct": True},
            {"text": "The global hook automatically optimizes React performance without developer tools", "is_correct": False},
            {"text": "The global hook is deprecated and replaced by built-in browser debugging APIs", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React applications that require sophisticated caching strategies for API responses, computed values, and component outputs, what patterns ensure cache invalidation correctness while maintaining optimal performance?",
        "explanation": "Implement cache keys based on dependency graphs, use proper cache invalidation strategies (time-based, tag-based, manual), consider cache size limits and LRU eviction, implement cache warming for critical data, use libraries like SWR or React Query for smart caching, and handle cache consistency in concurrent scenarios.",
        "reference": "https://react.dev/reference/react/useMemo#memoizing-expensive-calculations",
        "points": 3,
        "answers": [
            {"text": "Manual cache management is always more reliable than automated caching libraries", "is_correct": False},
            {"text": "Use dependency-based keys, proper invalidation, size limits, and specialized caching libraries", "is_correct": True},
            {"text": "Caching should be avoided in React applications due to state management complexity", "is_correct": False},
            {"text": "Browser localStorage provides sufficient caching capabilities for all React use cases", "is_correct": False}
        ]
    },
    {
        "text": "In React's upcoming asset loading optimizations, how do features like preloadModule and prefetchDNS integrate with React's component lifecycle to improve perceived performance and reduce loading times?",
        "explanation": "These features enable React components to declaratively specify resource loading hints, allowing the browser to preload critical modules and prefetch DNS lookups based on component rendering and user interactions, integrating with React's concurrent features for optimal timing of resource loading operations.",
        "reference": "https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#asset-loading",
        "points": 3,
        "answers": [
            {"text": "Asset loading optimizations only affect initial page load without component-level benefits", "is_correct": False},
            {"text": "Preloading integrates with component lifecycle for optimal resource loading timing", "is_correct": True},
            {"text": "React asset loading features replace all browser-native resource loading capabilities", "is_correct": False},
            {"text": "Asset loading optimizations are only useful for server-side rendered applications", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components that need to handle complex state machines with multiple states, transitions, and side effects, what patterns and libraries should you consider to manage state complexity effectively?",
        "explanation": "Consider using libraries like XState for explicit state machine modeling, implement state charts for complex logic, use useReducer with state machine patterns, clearly define valid state transitions, handle side effects consistently, and ensure state machine logic is testable and predictable.",
        "reference": "https://react.dev/reference/react/useReducer#avoiding-recreating-the-initial-state",
        "points": 3,
        "answers": [
            {"text": "useState with multiple boolean flags is sufficient for all complex state scenarios", "is_correct": False},
            {"text": "Use state machine libraries, reducers with transition patterns, and explicit state modeling", "is_correct": True},
            {"text": "Complex state machines should always be managed outside of React components", "is_correct": False},
            {"text": "State machine complexity is automatically handled by React's built-in state management", "is_correct": False}
        ]
    },
    {
        "text": "In React's experimental timeline profiler, what insights does it provide about component render timing, and how can developers use this information to identify and resolve performance bottlenecks in large applications?",
        "explanation": "The timeline profiler shows component render durations, identifies which components caused re-renders, reveals unnecessary renders, displays commit phases, and helps identify the slowest components. Developers can use this to optimize render performance, reduce unnecessary updates, and improve overall application responsiveness.",
        "reference": "https://react.dev/blog/2018/09/10/introducing-the-react-profiler",
        "points": 2,
        "answers": [
            {"text": "Timeline profiler only shows basic component hierarchy without performance insights", "is_correct": False},
            {"text": "Timeline profiler reveals render timing, unnecessary updates, and performance bottlenecks", "is_correct": True},
            {"text": "Timeline profiler automatically fixes all identified performance issues", "is_correct": False},
            {"text": "Timeline profiler is only useful for debugging server-side rendering performance", "is_correct": False}
        ]
    },
    {
        "text": "When implementing React components that require advanced keyboard navigation patterns like roving tabindex, arrow key navigation, and complex focus management for custom widgets, what accessibility patterns and ARIA attributes should you implement?",
        "explanation": "Implement roving tabindex pattern with only one focusable element, use arrow keys for navigation, implement proper ARIA roles like listbox/option, use aria-activedescendant for virtual focus, handle Home/End keys for first/last navigation, and ensure screen reader announcements with live regions and proper labels.",
        "reference": "https://www.w3.org/WAI/ARIA/apg/patterns/",
        "points": 3,
        "answers": [
            {"text": "Standard tab navigation is sufficient for all custom React widget interactions", "is_correct": False},
            {"text": "Implement roving tabindex, arrow navigation, ARIA roles, and screen reader support", "is_correct": True},
            {"text": "Keyboard navigation should be disabled in favor of mouse-only interactions", "is_correct": False},
            {"text": "React automatically provides all necessary accessibility features for custom widgets", "is_correct": False}
        ]
    },
    {
        "text": "In React's upcoming concurrent features and time slicing implementation, what is the role of the scheduler's yield mechanism, and how does it balance work prioritization with maintaining consistent frame rates during complex rendering operations?",
        "explanation": "The yield mechanism allows React to pause work and check if higher priority tasks need attention, using techniques like MessageChannel for scheduling. It balances work by yielding control back to the browser after small units of work, ensuring urgent updates can interrupt less important work while maintaining 60fps through careful timing and priority management.",
        "reference": "https://github.com/facebook/react/tree/main/packages/scheduler",
        "points": 3,
        "answers": [
            {"text": "Yield mechanism only affects development mode without impacting production performance", "is_correct": False},
            {"text": "Yield enables work interruption, priority balancing, and frame rate maintenance through controlled scheduling", "is_correct": True},
            {"text": "Yield mechanism eliminates all rendering delays by processing everything synchronously", "is_correct": False},
            {"text": "Yield is only used for error handling and has no impact on rendering performance", "is_correct": False}
        ]
    }
]
