#!/usr/bin/node

function compareNumbers (a, b) {
  return a - b;
}

const length = process.argv.length;

if (length < 4) {
  console.log(0);
} else {
  const order = process.argv.slice(2);
  order.sort(compareNumbers);
  const lenOr = order.length;
  console.log(order[lenOr - 2]);
}
