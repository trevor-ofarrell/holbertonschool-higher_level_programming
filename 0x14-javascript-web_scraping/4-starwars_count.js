#!/usr/bin/node
const request = require('request');

let i = 0;
request(process.argv[2], (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  for (const movie of JSON.parse(body).results) {
    for (const chars of movie.characters) {
      if (chars.includes('18')) {
        i++;
      }
    }
  }
  console.log(i);
});
