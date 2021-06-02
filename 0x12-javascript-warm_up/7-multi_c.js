#!/usr/bin/node
/* prints x times c is fun */

if (typeof process.argv[2] !== 'undefined' && !isNaN(process.argv[2])) {
  let x = parseInt(process.argv[2]);
  for (; x > 0; x--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
