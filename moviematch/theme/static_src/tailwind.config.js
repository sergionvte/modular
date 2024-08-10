/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',
        '../static/js/*.js',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',
        '../../static/js/*.js',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',
        '../../**/static/js/*.js',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'bg0_h': '#1d2021',
                'bg0': '#282828',
                'bg1': '#3c3836',
                'bg2': '#504945',
                'bg3': '#665c54',
                'bg4': '#7c6f64',
                'gray': '#928374',
                'orange': '#d65d0e',
                'bg0_s': '#32302f',
                'fg4': '#a89984',
                'fg3': '#bdae93',
                'fg2': '#d5c4a1',
                'fg1': '#ebdbb2',
                'fg0': '#fbf1c7',
                'orange_slow': '#fe8019',

                'fg_color': '#D2CDB3',
                'bg_color': '#30313A',
                'highlight_color': '#4792A3',
                'hover_color': '#54757A',
                'dark_color': '#3A3F43',
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
