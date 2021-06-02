#!/usr/bin/node
/* adds two nums */

function add (a, b) {
  const aa = parseInt(a);
  const bb = parseInt(b);
  return aa + bb;
}
const a = process.argv[2];
const b = process.argv[3];
console.log(add(a, b));
