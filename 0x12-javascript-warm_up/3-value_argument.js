#!/usr/bin/node
var myArgs = process.argv.slice(1);

if (!myArgs[1]) {
  console.log('No argument');
} else if (myArgs[1]) {
  console.log(myArgs[1]);
}
