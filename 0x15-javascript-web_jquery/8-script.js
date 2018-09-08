$.get('https://swapi.co/api/films/?format=json', function (data, textStatus) {
  $.each(data.results, function (i, movie) {
    let item = document.createElement('li');
    item.innerHTML = movie['title'];
    $('UL#list_movies').append(item);
  });
});
