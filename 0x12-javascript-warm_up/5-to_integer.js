#!/usr/bin/node
/* converts string to int */

if (typeof process.argv[2] !== 'undefined' && !isNaN(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
