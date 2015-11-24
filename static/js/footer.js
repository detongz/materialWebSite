$(document).ready(function() {

   var docHeight = $(window).height();
   var footerHeight = $('#footer').height();
   var footerTop = $('#footer').position().top;

   if (footerTop < docHeight) {
    $('#content').css('height',  (docHeight - footerHeight - 40) + 'px');
   }
  });
