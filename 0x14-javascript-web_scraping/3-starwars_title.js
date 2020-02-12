#!/usr/bin/node
const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], (err, response, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
