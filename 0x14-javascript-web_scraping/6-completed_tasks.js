#!/usr/bin/node

const request = require('request');
const alltasks = {};
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const tasks of (JSON.parse(body))) {
      if (tasks.completed) {
        if (!alltasks[tasks.userId]) {
          alltasks[tasks.userId] = 1;
        } else {
          alltasks[tasks.userId]++;
        }
      }
    }
    console.log(alltasks);
  }
});
