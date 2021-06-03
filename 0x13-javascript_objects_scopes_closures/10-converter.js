#!/usr/bin/node
/* converts from base 10 to specified base */

exports.converter = function (base) {
  const b = base;
  return function (st) {
    console.log(b);
    const ret = parseInt(st.toString(10));
    return ret.toString(b);
  };
};
