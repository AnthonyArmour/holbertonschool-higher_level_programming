#!/usr/bin/node
/* Square class inherits from rectangle */

class Square extends require('./5-square') {
  charPrint (c) {
    let a = 'X';
    if (typeof c !== 'undefined') {
      a = c;
    }
    for (let x = 0; x < this.width; x++) {
      console.log(a.repeat(this.height));
    }
  }
}
module.exports = Square;
