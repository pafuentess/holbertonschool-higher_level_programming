#!/usr/bin/node

const fs = require('fs');
const fileA = process.argv[2];
fs.readFile(fileA, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
