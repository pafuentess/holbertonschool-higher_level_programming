#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  return (result);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

if (isNaN(a) === false && isNaN(b) === false) {
  console.log(add(a, b));
} else {
  console.log('NaN');
}
