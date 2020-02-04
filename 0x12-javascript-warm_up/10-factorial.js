#!/usr/bin/node
const args = process.argv.slice(1);
function factorial (x) {
  if (!x || x === 0) {
    return (1);
  }
  return (x * factorial(x - 1));
}
const x = parseInt(args[1], 10);
console.log(factorial(x));
