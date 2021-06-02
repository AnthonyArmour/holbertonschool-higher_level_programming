#!/usr/bin/node
/* function that increments then calls a func */

module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
