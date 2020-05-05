#!/usr/bin/node

const length = process.argv.length;

if (length === 2 || length === 3) {
  console.log(0);
} else if (length > 3) {
  const order = process.argv.sort();
  console.log(order[length - 2]);
}
