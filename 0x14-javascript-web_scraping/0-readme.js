#!/usr/bin/node
const { readFile } = require('fs');

var args = process.argv.slice(1);
readFile(String(args[1]), 'utf-8', (err, fileContent) => {
  const str = fileContent;
  if (err) {
    console.log(err);
  }
  console.log(str);
});
