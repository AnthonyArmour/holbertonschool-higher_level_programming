#!/usr/bin/node
/* prints factorial */

function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  const y = parseInt(x);
  if (y === 1) {
    return 1;
  } else {
    return y * factorial(y - 1);
  }
}
const num = factorial(process.argv[2]);
console.log(num);
