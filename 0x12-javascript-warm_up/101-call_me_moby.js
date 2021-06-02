#!/usr/bin/node
/* function that calls function x times */

module.exports.callMeMoby = function (x, myFunction) {
  for (let xx = 0; xx < x; xx++) {
    myFunction();
  }
};
