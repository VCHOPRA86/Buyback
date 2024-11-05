jQuery.noConflict();
(function ($) {
  $(function () {
    $( '.site-pop-search' ).click(function() {
      $( '.search-form-top' ).toggleClass( 'active' );
    });
    // bootstrap select
    $('.selectpicker').selectpicker();

    // swiper slider
    var swiper = new Swiper('.device-swiper', {
      slidesPerView: 6,
      spaceBetween: 30,
      freeMode: false,
      autoplay: {
        delay: 2000,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      breakpoints: {
        480: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        767: {
          slidesPerView: 2,
          spaceBetween: 30
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 30
        }
      }
    });
    // swiper slider
    var swiper = new Swiper('.seller-swiper', {
      slidesPerView: 5,
      spaceBetween: 30,
      freeMode: false,
      autoplay: {
        delay: 2000,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      breakpoints: {
        480: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        767: {
          slidesPerView: 3,
          spaceBetween: 30
        },
        1024: {
          slidesPerView: 3,
          spaceBetween: 30
        }
      }
    });
    // swiper slider
    var swiper = new Swiper('.review-swiper', {
      slidesPerView: 1,
      spaceBetween: 30,
      freeMode: true,
      autoplay: {
        delay: 5000,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    });
    // swiper slider
    var swiper = new Swiper('.brand-swiper', {
      slidesPerView: 5,
      spaceBetween: 30,
      freeMode: false,
      autoplay: {
        delay: 1000,
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      breakpoints: {
        480: {
          slidesPerView: 1,
          spaceBetween: 10
        },
        767: {
          slidesPerView: 3,
          spaceBetween: 30
        }
      }
    });


    // slide and push menu
    var menuRight = document.getElementById('cbp-spmenu-s2'),
      showRightPush = document.getElementById('showRightPush'),
      body = document.body;

    showRightPush.onclick = function () {
      classie.toggle(this, 'active');
      classie.toggle(body, 'cbp-spmenu-push-toleft');
      classie.toggle(menuRight, 'cbp-spmenu-open');
      disableOther('showRightPush');
    };

    function disableOther(button) {
      if (button !== 'showRightPush') {
        classie.toggle(showRightPush, 'disabled');
      }
    }

  });
})(jQuery);