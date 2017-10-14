(function ($) {
    $.fn.right = function (selector, data, fn) {
        var p = selector ? $(selector) : this.parent();
        return p.width() - this.position().left - this.width();
    };
    $(window).on('load resize', function (ev) {
        var tabletSize = 1200,
            mobileSize = 768;
        if ($(this).width() > tabletSize)
            var sizeEv = $.extend({}, ev, { type: 'desktop' });
        else if ($(this).width() <= tabletSize
            && $(this).width() > mobileSize)
            var sizeEv = $.extend({}, ev, { type: 'tablet' });
        else
            var sizeEv = $.extend({}, ev, { type: 'mobile' });
        return $(this).trigger(sizeEv);
    });
    $.fn.desktop = function (selector, data, fn) {
        return this.on('desktop', selector, data, fn);
    };
    $.fn.tablet = function (selector, data, fn) {
        return this.on('tablet', selector, data, fn);
    };
    $.fn.mobile = function (selector, data, fn) {
        return this.on('mobile', selector, data, fn);
    };
    $(window).on('resize', function (e) {
        clearTimeout(window.__id);

        window.__id = setTimeout(function () {
            var ev = $.extend({}, e, { type: 'resized' });
            return $(window).trigger(ev);
        }, 200);
    });
    $.fn.resized = function (selector, data, fn) {
        return this.on('resized', selector, data, fn);
    };
})(jQuery);



//$('.menu, .close, .nav').click(function (e) {
//    var $bar = $('nav#sidebar'),
//        $cnt = $('.site-body, .site-header, .site-footer, #map'),
//        w = $bar.outerWidth();
//    if ($bar.position().left < 0) {
//        $bar.stop().animate({ left: 0 });
//        $cnt.stop().animate({ left: w });
//        $('.banner span').each(function () {
//            $(this).stop().animate({ 'backgroundPositionX': w });
//        });
//    }
//    else {
//        $bar.stop().animate({ left: 0 - w });
//        $cnt.stop().animate({ left: 0 });
//        $('.banner span').each(function (i,o) {
//            $(this).stop().animate({ 'backgroundPositionX': 0 });
//        });
//    }
//})
//(function ($) {

//})(jQuery);