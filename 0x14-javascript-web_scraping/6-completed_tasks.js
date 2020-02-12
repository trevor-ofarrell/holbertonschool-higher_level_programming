#!/usr/bin/node
const request = require('request');

const users = [];
var ret = {};
let count = 0;

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  for (const task of JSON.parse(body)) {
    if (task.completed) {
      users.push(task.userId);
    }
  }
  for (var i = 1; i < 11; i++) {
    count = 0;
    for (let j = 0; j <= users.length; j++) {
      if (Number(users[j]) === Number(i)) {
        count++;
      }
      ret[String(i)] = count;
    }
  }
  console.log(ret);
});
