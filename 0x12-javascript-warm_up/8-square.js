#!/usr/bin/node

const length = process.argv.length;
const value = parseInt(process.argv[2]);

if (length === 2 || (isNaN(value) === true)) {
  console.log('Missing size');
} else if (length > 2) {
  for (let i = 0; i < value; i++) {
    console.log('X'.repeat(value));
  }
}
