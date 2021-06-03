#!/usr/bin/node
/* Square class inherits from rectangle */

const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
