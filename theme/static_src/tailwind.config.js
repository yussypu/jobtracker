/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    darkMode: 'class',
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
        // '../../**/*.js', // Uncomment if using JS
        // '../../**/*.py'  // Uncomment if using Python class names
    ],
    safelist: [
        'bg-blue-50', 'dark:bg-blue-900',
        'bg-yellow-50', 'dark:bg-yellow-900',
        'bg-green-50', 'dark:bg-green-900',
        'bg-red-50', 'dark:bg-red-900',
    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
