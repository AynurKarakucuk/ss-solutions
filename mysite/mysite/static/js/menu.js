// SmartMenus init
$(function() {
 const $ = django.jQuery;
  $('#main-menu').smartmenus({
    subMenusSubOffsetX: 6,
    subMenusSubOffsetY: -8
  });
});

// SmartMenus mobile menu toggle button
$(function() {
 const $ = django.jQuery;
  var $mainMenuState = $('#main-menu-state');
  if ($mainMenuState.length) {
    // animate mobile menu
    $mainMenuState.change(function(e) {
      var $menu = $('#main-menu');
      if (this.checked) {
        $menu.hide().slideDown(250, function() { $menu.css('display', ''); });
      } else {
        $menu.show().slideUp(250, function() { $menu.css('display', ''); });
      }
    });
    // hide mobile menu beforeunload
    $(window).bind('beforeunload unload', function() {
      if ($mainMenuState[0].checked) {
        $mainMenuState[0].click();
      }
    });
  }
});