#!/usr/bin/node
const args = process.argv.slice(1);
const range = parseInt(args[1]);
let i = 0;

if (!range) {
  console.log('Missing number of occurrences');
}
for (i = 0; i < range; i++) {
  console.log('C is fun');
}
