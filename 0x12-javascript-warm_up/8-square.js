#!/usr/bin/node
const args = process.argv.slice(1);
const size = parseInt(args[1]);

if (!size) {
  console.log('Missing size');
}
let i = 0;
let row = '';
for (i = 0; i < size; i++) {
  row += 'X';
}
for (i = 0; i < size; i++) {
  console.log(row);
}
