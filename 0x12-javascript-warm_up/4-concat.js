#!/usr/bin/node
/* concats args */

let arg1;
let arg2;
if (process.argv.length > 3) {
  arg2 = process.argv[3];
  arg1 = process.argv[2];
} else if (process.argv.length === 3) {
  arg2 = 'undefined';
  arg1 = process.argv[2];
} else {
  arg2 = 'undefined';
  arg1 = 'undefined';
}
console.log(arg1 + ' is ' + arg2);
