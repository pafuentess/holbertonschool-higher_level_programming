#!/usr/bin/node

const length = process.argv.length;
let first = 'undefined';
let second = 'undefined';

if (length === 3) {
  first = process.argv[2];
} else if (length === 4) {
  first = process.argv[2];
  second = process.argv[3];
}
console.log(first + ' ' + 'is' + ' ' + second);
