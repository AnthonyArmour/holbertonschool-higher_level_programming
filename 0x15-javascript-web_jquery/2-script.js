#!/usr/bin/node
/* changes div to red on click */


const click = document.getElementById("red_header");
click.addEventListener('click', changeColor);

function changeColor() {
  document.querySelector('header').style.color = "#FF0000";
}