$(document).ready(function() {

  var $menu = $('nav ul');
  
  $(document).on('click', '#pull', function() {
    $menu.slideToggle();
    return false;
  });

});