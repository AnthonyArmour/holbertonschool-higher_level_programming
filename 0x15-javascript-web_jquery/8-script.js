#!/usr/bin/node

$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  success: function(data) {
    // the query below shows results key which holds list of resluts
    // $('#list_movies').append('<li>'+ JSON.stringify(data)+ '</li>');
    for (const obj of data.results) {
      $('#list_movies').append('<li>'+ obj.title+ '</li>');
    };
  }
});
