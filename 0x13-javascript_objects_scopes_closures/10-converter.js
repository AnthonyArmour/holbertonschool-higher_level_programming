#!/usr/bin/node
/* converts from base 10 to specified base */

exports.converter = function (base) {
  return function (st) {
    console.log(base);
    const ret = parseInt(st.toString(10));
    return ret.toString(base);
  };
};
