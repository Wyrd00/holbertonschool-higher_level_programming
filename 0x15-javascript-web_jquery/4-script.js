$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    if ($(this).hasClass('green')) {
      $(this).addClass('red');
      $(this).removeClass('green');
      $(this).css('red', '#FF0000');
    } else {
      $(this).removeClass('red');
      $(this).addClass('green');
      $(this).css('green', '#00FF00');
    }
  });
});
