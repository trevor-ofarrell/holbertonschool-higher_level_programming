#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, fileContent) => {
  if (err) {
    return console.log(err);
  }
  console.log(fileContent);
});
