//----------------------------------------------------//
////////////////////////////////////////////////////////
////////// COCOTOOLS by Mateusz Ignatowicz /////////////
////////// Github: coconutcake             /////////////
////////////////////////////////////////////////////////
//----------------------------------------------------//

// Scrolled top bar [slide]
function coconavi_down(target, topoffset, tempo) {  
    $(window).bind('scroll', function () {
        if ($(window).scrollTop() > topoffset) {
            $(target).slideDown(tempo);
        } else {
            $(target).slideUp(tempo);
        }
    });
}

function coconavi(target, topoffset, css_class, logo_class, trans_logo) {
    var navbar = $(target);
	$(window).scroll(function(){
		if($(window).scrollTop() <= topoffset){
            navbar.removeClass(css_class);
            $(logo_class).removeClass(trans_logo)
            console.log('class removed');
		} else {
            $(logo_class).addClass(trans_logo)
			navbar.addClass(css_class);
			console.log('class added');
		}
	});

};

function showup() {
    $("body").hide();
    $('div').removeClass('initiallyHidden');
}