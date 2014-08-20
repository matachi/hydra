$(document).ready(function () {
  var $collapse = $('.collapse');
  var $form = $($collapse).children('form');
  $form.focusin(function() {
    $collapse.addClass('expanded');
  });
  $form.focusout(function() {
    $collapse.removeClass('expanded');
  });
});
