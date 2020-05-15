$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (people) {
    $('div#hello').text(people.hello);
  }, 'json'
);
});