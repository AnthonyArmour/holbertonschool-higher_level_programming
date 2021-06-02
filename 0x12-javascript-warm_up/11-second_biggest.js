#!/usr/bin/node
/* searches second biggest int */

const mylist = process.argv;
let mx = 0;
let mx2 = 0;
if (mylist.length >= 4) {
  let num;
  mx = parseInt(mylist[2]);
  for (let x = 0; x < mylist.length; x++) {
    num = parseInt(mylist[x]);
    if (num > mx) {
      mx2 = mx;
      mx = num;
    }
  }
}
console.log(mx2);
