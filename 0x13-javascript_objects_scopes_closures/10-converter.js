#!/usr/bin/node
/* converts from base 10 to specified base */

exports.converter = function (base) {
  return function (st) {
    console.log(base);
    return parseInt(st.toString(10)).toString(base);
  };
};
