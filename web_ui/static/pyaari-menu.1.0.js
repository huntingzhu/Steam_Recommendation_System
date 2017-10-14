if (typeof jQuery === "undefined") throw new Error("pfd-menu requires jQuery")

var PfdMenu = {
    _actuatorTemplate: $('<a/>', { id: 'toc-actuator', css: { opacity: 0 }, text: 'Show Menu' }),
    _ctor: function () {
        this.$menu = $('nav#toc');

        this._actuator = this._actuatorTemplate.appendTo(this.$menu);
        this._actuator.animate({ opacity: 1 }, 1000).on('click', function (e) {
            e.preventDefault();
            PfdMenu.slideToggle();
        });
    },
    slideToggle: function () {
        if (this.$menu.hasClass('on'))
            this.slideClose();
        else
            this.slideOpen();
    },
    slideOpen: function () {
        var i = 240 - Math.min(($(window).width() - 94), 240);
        $('#container,#work-bio,#pfd-location').animate({ left: '-=' + (240 - i) });
        $('.parallax').animate({ 'backgroundPositionX': '-=' + (240 -i) });
        this.$menu.animate({ right: -i  }).addClass('on');
    },
    slideClose: function () {
        var i = 240 - Math.min(($(window).width() - 94), 240);
        $('#container,#work-bio,#pfd-location').animate({ left: 0 })
        $('.parallax').animate({ 'backgroundPositionX': '+=' + (240 - i) });
        this.$menu.animate({ right: '-=' + (240-i) }).removeClass('on');
    }
};
