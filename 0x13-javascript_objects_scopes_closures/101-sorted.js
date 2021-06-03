#!/usr/bin/node
/* finds value occurences */

const dic = require('./101-data');
const dic2 = {};
for (const k in dic.dict) {
  if (!dic2[dic.dict[k].toString()]) {
    dic2[dic.dict[k].toString()] = [];
  }
  dic2[dic.dict[k].toString()].push(k.toString());
}
console.log(dic2);
