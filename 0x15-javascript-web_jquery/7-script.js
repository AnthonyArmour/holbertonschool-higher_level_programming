#!/usr/bin/node
/* fetches name from a URL */

// let searchParams = URLSearchParams("https://swapi-api.hbtn.io/api/people/5/?format=json");
// url_prefix = "https://swapi-api.hbtn.io/api/people/5/?"

//  if (searchParams.has(url_prefix + "name")) {
//   let json_dict = searchParams.get(url_prefix + "name")
//   $("div.character").text(json_dict["name"])
// }

$.get("https://swapi-api.hbtn.io/api/people/5/?format=json")
  .done(function (data) {
      dic = JSON.stringify(data)
    //   $("#.character").text("ant")
      $('<p>' + dic["name"] + '</p>').appendTo('#div.character');
  })