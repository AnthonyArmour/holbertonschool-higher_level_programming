#!/usr/bin/node
/* keeps log of number of func calls */

let x = 0;
exports.logMe = function (item) {
  console.log(x + ': ' + item);
  x += 1;
};
