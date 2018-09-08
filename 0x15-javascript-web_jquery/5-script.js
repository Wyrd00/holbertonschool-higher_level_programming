$(document).ready(function () {
  $('DIV#add_item').click(function () {
    let item = '<li>Item</li>';
    $('.my_list').append(item);
  });
});
