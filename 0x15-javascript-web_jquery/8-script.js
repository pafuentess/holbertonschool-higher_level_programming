$.get('https://fourtonfish.com/hellosalut/?lang=fr', function(people) {
  $('div#hello').text(data.hello);
}, 'json'
);
