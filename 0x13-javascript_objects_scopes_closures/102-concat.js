#!/usr/bin/node
/* concats files */

const fd = require('fs');
fd.open('./' + process.argv[4], 'w', function (err, file) {
  if (err) throw err;
});
fd.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  fd.appendFile(process.argv[4], data, function (err) {
    if (err) throw err;
  });
});
fd.readFile(process.argv[3], 'utf8', function (err, data) {
  if (err) throw err;
  fd.appendFile(process.argv[4], data, function (err) {
    if (err) throw err;
  });
});
