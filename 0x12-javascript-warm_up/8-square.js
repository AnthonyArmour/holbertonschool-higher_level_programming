#!/usr/bin/node
/* prints square */

if (typeof process.argv[2] !== 'undefined' && !isNaN(process.argv[2])) {
  const x = parseInt(process.argv[2]);
  for (let xx = 0; xx < x; xx++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
