#!/usr/bin/node

const length = process.argv.length;

if (length < 4) {
  console.log(0);
} else {
  let order = process.argv.slice(2);
  order = order.sort();
  const lenOr = order.length;
  console.log(order[lenOr - 2]);
}
