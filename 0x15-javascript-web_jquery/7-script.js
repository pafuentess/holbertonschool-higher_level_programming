$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(people) {
  $('#character').text(people.name);
}, 'json'
);
