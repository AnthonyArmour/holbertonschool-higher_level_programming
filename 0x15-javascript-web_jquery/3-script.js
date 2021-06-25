#!/usr/bin/node
/* changes div to red on click using api */

$("#red_header").click(changeColor);

function changeColor() {
  $("header").addClass( "red" );
}