#!/usr/bin/node
const { readFile } = require('fs');

readFile(process.argv[2], 'utf-8', (err, fileContent) => {
  if (err) {
    console.log(err);
  }
  console.log(fileContent);
});
