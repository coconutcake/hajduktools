//----------------------------------------------------//
////////////////////////////////////////////////////////
////////// COCOTOOLS by Mateusz Ignatowicz /////////////
////////// Github: coconutcake             /////////////
////////////////////////////////////////////////////////
//----------------------------------------------------//

// All show up
function showup() {
    $("body").hide();
    $('div').removeClass('initiallyHidden');
    console.log('initiallyHidden removed');
}

// Scrolled top bar [BASIC]
function coconavi_b(target, topoffset, tempo) {
    $(window).bind('scroll', function() {
        if ($(window).scrollTop() > topoffset) {
            $(target).slideDown(tempo);
        } else {
            $(target).slideUp(tempo);
        }
    });
}

// Scrolled top bar [advanced]
function coconavi(target, topoffset, css_class, logo_class, trans_logo) {
    var navbar = $(target);
    var navbar_brand = $('.navbar-brand');
    $(window).scroll(function() {
        if ($(window).scrollTop() <= topoffset) {
            navbar.removeClass(css_class);
            navbar_brand.removeClass('navbar-brand-scroll');
            $(logo_class).removeClass(trans_logo)
            console.log('class removed');
        } else {
            $(logo_class).addClass(trans_logo)
            navbar_brand.addClass('navbar-brand-scroll');
            navbar.addClass(css_class);
            console.log('class added');
        }
    });

};

(function($) {
    $.fn.coconavi2 = function(options) {
        var settings = $.extend({
            title: "DCALC", //title
            title_color: "rgb(34, 202, 132)", //title color
            title_b: "2rem", //title font big
            title_s: "1rem", //title font small
            logo: "/static/calc.png", //logo path
            logo_sm: "40px", //logo size small
            logo_big: "60px", //logo size big
            logo_margin_sm: "0", //logo margin small
            logo_margin_b: "1rem", //logo margin big
            logout: "/accounts/logout", //logout path
            topoffset: 40, //viewport offset tolerance
            line: "10px solid rgb(34, 202, 132)", //line
            bg: "",
            bg_scrolled: "#FFF",
        }, options);
        var _init = function() {
            coconavi('.navbar', settings.topoffset, 'navbar-scroll', '#logo', 'logo-sm');
        }
        th = $(this);
        style = $("<style>");
        lo = $('#logo');
        nav = $('.navbar');
        var element = document.getElementsByClassName('navbar-scroll');

        return [
            // Html:
            th.html('<nav class="navbar fixed-top rounded"><div class="container"><div class="navbar-header p-1"><img id="logo" class="logo" src=""><a class="navbar-brand text-uppercase font-weight-bold p-1" href="#"><span class="align-middle">' + settings.title + '</span></a></div><div class="d-flex bd-highlight"><div class="p-2 w-100 bd-highlight"></div><div class="p-2 flex-shrink-1 bd-highlight"><a id="logout" href=""><span class="align-middle"><button type="submit" class="shadow btn btn-secondary btn-md ">Logout</button></span></a></div></div></nav>'),

            // Attrs:
            $("#logo").attr('src', settings.logo),
            $("img.logo-sm").css('width', settings.logo_sm),
            $("img.logo-sm").css('margin', settings.logo_margin_sm),
            $("img.logo").css('margin', settings.logo_margin_b),
            $("img.logo").css('width', settings.logo_big),
            $(".navbar-brand").css('font-size', settings.title_b),
            $("#logout").attr('href', settings.logout),
            //default css:
            style.prop("type", "text/css").html("\
            .bg {\
            } .navbar {\
                border-bottom: 0;\
                padding: 30px 0;\
                transition-duration: 0.6s;\
            } .navbar-default .navbar-brand,.navbar-default .navbar-nav>li>a {\
                color: #183532;\
            } .navbar-scroll {\
                padding: 5px 0;\
                transition-duration: 0.5s;\
                transition-timing-function: cubic-bezier(.91, .01, .1, 1);\
            } .navbar-brand {\
                transition-duration: 0.5s;\
                transition-timing-function: cubic-bezier(.91, .01, .1, 1);\
            } .navbar-brand-scroll {\
                transition-duration: 0.5s;\
                transition-timing-function: cubic-bezier(.91, .01, .1, 1);\
            } .nav-dropdown-scroll {\
                background: #e7eaea;\
                box-shadow: 0px 10px 9px rgba(0, 0, 0, 0.4);\
            } img.logo {\
                margin: 1rem;\
                width: 60px;\
                transition-duration: 0.5s!important;\
                transition-timing-function: cubic-bezier(.91, .01, .1, 1);\
                animation: spinning .5s cubic-bezier(.91, .01, .1, 1);\
            } .logo-sm {\
                margin: 1rem;\
                width: 40px!important;\
                transition-duration: 0.5s!important;\
                transition-timing-function: cubic-bezier(.91, .01, .1, 1);\
                animation: spinning .5s cubic-bezier(.91, .01, .1, 1);\
            } @keyframes spinning-a {\
                0% {\
                    transform: scale(1, 0);\
                } 100% {\
                    transform: scale(1.0, 1.0);\
                }\
            } @keyframes spinning {\
                    0% {\
                        transform: scale(1, 0);\
                    }  3% {\
                        transform: scale(1.0, 1.0);\
                    } 15% {\
                        transform: scale(1.0, 0);\
                    } 24% {\
                        transform: scale(1.0, 1.0);\
                    } 32% {\
                        transform: scale(1.0, 0);\
                    } 47% {\
                        transform: scale(1.0, 1.0);\
                    } 73% {\
                        transform: scale(1.0, 0);\
                    } 100% {\
                        transform: scale(1.0, 1.0);\
                    }\
                }")
            .appendTo("head"),
            // Update css
            $("head").append(
                '<style>.navbar-scroll { background: ' + settings.bg_scrolled + ';border-bottom: ' + settings.line + ';}.navbar-brand { color: ' + settings.title_color + ';}.navbar-brand-scroll { font-size: ' + settings.title_s + '!important;}</style>'
            ),
            // Load function
            _init()
        ]
    };
}(jQuery));
$('#coconavi').coconavi2();

// function: CLEAR INPUTS..................................
function clear_target(target, result) {
    $(target).val('')
    $(result).empty();
    console.log('cleared')
}