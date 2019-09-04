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

function coconavi(target, topoffset, css_class) {
    var navbar = $(target);
	$(window).scroll(function(){
		if($(window).scrollTop() <= topoffset){
            navbar.removeClass(css_class);
            $('#logo').removeClass('logo-sm')
            console.log('class removed');
		} else {
            $('#logo').addClass('logo-sm')
			navbar.addClass(css_class);
			console.log('class added');
		}
	});

};

function showup() {
    $("body").hide();
    $('div').removeClass('initiallyHidden');
}