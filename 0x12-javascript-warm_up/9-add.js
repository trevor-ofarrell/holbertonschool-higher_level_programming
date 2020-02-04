#!/usr/bin/node
const args = process.argv.slice(1);
function add (a, b) {
  var c = Number(a) + Number(b);
  return (c);
}
var a = parseInt(args[1], 10);
var b = parseInt(args[2], 10);
console.log(add(a, b));
