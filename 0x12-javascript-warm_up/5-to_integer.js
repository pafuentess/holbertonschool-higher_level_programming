#!/usr/bin/node

const length = process.argv.length;
let value = '';

if (length === 2) {
  console.log('Not a number');
} else if (length > 2) {
  value = parseInt(process.argv[2]);
  if (isNaN(value) === true) {
    console.log('Not a number');
  } else {
    console.log('My number:', value);
  }
}
