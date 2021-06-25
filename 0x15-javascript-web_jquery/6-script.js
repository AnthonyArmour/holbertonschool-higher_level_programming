#!/usr/bin/node
/* adds item to li */

$("#update_header").click(update_header);

function update_header() {
  $("header").text('New Header!!!')
}