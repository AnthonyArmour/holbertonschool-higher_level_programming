#!/usr/bin/node
/* adds item to li */

$("#add_item").click(addItem);

function addItem() {
  $("UL.my_list").append("<li>Item</li>")
}