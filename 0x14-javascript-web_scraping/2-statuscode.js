#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    return console.log('code:', 404);
  }
  console.log('code:', response.statusCode);
});
