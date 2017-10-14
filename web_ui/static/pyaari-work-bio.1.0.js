if (typeof jQuery === "undefined") throw new Error("pfd-work-bio requires jQuery")

; (function ($) {
    var PfdWorkBio = {
        _templates: {
            _visual: _.template('<img src="<%=data.src%>" alt="<%=data.alt%>" />'),
            _readMore: _.template('<a href="#" class="read-more">Read more +</a>')
        },
        _ctor: function () {
            $(window).on('desktop tablet', this._wide);
            $(window).on('mobile', this._narrow);
            $(window).on('load', function () {
                PfdWorkBio._draw();
            });
        },
        _draw: function () {
            var e = $('#work-visuals li').first()
            PfdWorkBio._render(e);
        },
        _render: function (e) {
            var visual = $(PfdWorkBio._templates._visual({ data: { src: '/images/' + e.data('visual') + '.jpg', alt: "" } })).hide().on('load', function () {
                $(this).prependTo(e).fadeIn(function () {
                    if (e.next()[0])
                        PfdWorkBio._render(e.next());
                });
            });
        },
        _wide: function () {
            var wh = $(window).height(),
                bh = $('#work-bio').height();
            if (wh > bh) {
                $('#work-bio').css({ position: 'fixed', float: '' });
                $(window).off('scroll').on('scroll', function () {
                    $('#work-bio').css({ top: Math.max(0 - $(this).scrollTop(), -90) });
                });
            }
            else {
                $(window).off('scroll');
                $('#work-bio').css({ position: 'relative', float: 'left', top: '' });
            }

            // Hide read-more (and expand)
            $('#preamble a.read-more').fadeOut(function () {
                ReadMore.slideDown($(this));
                $(this).remove();
            });
        },
        _narrow: function (fn) {
            $('#work-bio').css({ position: 'relative', float: '', top: '' });
            $(window).off('scroll');
            // Show read-more (and collapse)
            if ($('#preamble a.read-more').length === 0)
                $(PfdWorkBio._templates._readMore()).appendTo('#preamble').fadeIn(function () {
                    ReadMore.init('slide');
                });
        }
    };
    PfdWorkBio._ctor();
})(jQuery)