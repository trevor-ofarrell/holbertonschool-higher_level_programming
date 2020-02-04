#!/usr/bin/node
var args = process.argv.slice(1);
if (!parseInt(args[1], 10)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[1]));
}
