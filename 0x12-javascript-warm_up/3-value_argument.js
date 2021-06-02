#!/usr/bin/node
/* prints first arg passed */

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
