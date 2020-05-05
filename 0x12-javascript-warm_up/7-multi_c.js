#!/usr/bin/node

const length = process.argv.length;
let value = '';

if (length === 2) {
  console.log('Missing number of occurrences');
} else if (length > 2) {
  value = parseInt(process.argv[2]);
  if (isNaN(value) === true) {
    console.log('Missing number of occurrences');
  } else {
    for (let i = 0; i < value; i++) {
      console.log('C is fun');
    }
  }
}
