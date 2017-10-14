//;(function($){
	var ReadMore = {
		init: function(opts) {
			$('.read-more').each(function () {
			    var _p = $(this).parent();
                if (opts==='slide')
                    $('p, h3', _p).slideUp();
			    else
                    $('p, h3', _p).hide();
				$(this).click(function (e) {
					e.preventDefault();
					ReadMore.toggle($(this),_p);
				})
			});
		},
		toggle: function(e,o) {
			if (e.hasClass('on'))
				ReadMore._slideUp(e, o);
			else
				ReadMore._slideDown(e, o);
		},
		_slideDown: function(e,o) {
			$('p, h3', o).slideDown();
			e.text('Read less -').addClass('on');
		},
		_slideUp: function(e,o) {
			$('p, h3', o).slideUp();
			e.text('Read more +').removeClass('on');
		},
		slideDown: function (e) {
		    var _o = $(e).parent();
		    this._slideDown(e, _o);
		},
		slideUp: function (e) {
		    var _o = $(e).parent();
		    this._slideUp(e, _o);
		}
	};
//})(jQuery);