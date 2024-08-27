$(document).ready(

    /**
     * This function initializes an Intersection Observer to observe the visibility of 
     * 'section div' elements on the page. When a 'section div' becomes visible, its 
     * opacity is set to 1.
     *
     * @function
     * @returns {void}
     */
    function() {

        /**
         * The Intersection Observer callback function.
         *
         * @callback IntersectionObserverCallback
         * @param {IntersectionObserverEntry[]} entries - An array of IntersectionObserverEntry objects.
         */

        /**
         * The Intersection Observer instance.
         *
         * @type {IntersectionObserver}
         */
        let observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    $(entry.target).css("opacity", "1");
                }
            });
        }, {
            threshold: 0.1
        });

        /**
         * Observe each 'section div' element.
         *
         * @type {JQuery<HTMLElement>}
         */
        $("section div").each(function() {
            observer.observe(this);
        });
    }
);