#!/usr/bin/node
/* creates new altered array with map */

const org = require('./100-data');
const second = org.list.map(function (element, index) {
  return element * index;
});
console.log(org.list);
console.log(second);
