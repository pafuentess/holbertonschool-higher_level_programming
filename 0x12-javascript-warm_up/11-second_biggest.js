#!/usr/bin/node

const length = process.argv.length;

if (length === 2 || length === 3) {
  console.log(0);
} else if (length > 3) {
  let order = process.argv.slice(2);
  order = order.sort();
  const lenOr = order.length;
  console.log(order[lenOr - 2]);
}
