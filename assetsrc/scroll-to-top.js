$(document).ready(function () {
  var $scrollToTop = $('.scroll-to-top');
  $scrollToTop.hide();
  // Check to see if the window is top if not then display button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
      $scrollToTop.fadeIn();
    } else {
      $scrollToTop.fadeOut();
    }
  });
  // Click event to scroll to top
  $scrollToTop.click(function () {
    $('html, body').animate({scrollTop: 0}, 250);
    return false;
  });
});
