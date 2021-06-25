#!/usr/bin/node
/* changes div to red on click using api */

$("#toggle_header").click(changeColor);

function changeColor() {
  if ($("header").hasClass( "red" )) {
    $("header").removeClass( "red" );
    $("header").addClass( "green" );
  }
  else {
    $("header").removeClass( "green" );
    $("header").addClass( "red" );
  }
}