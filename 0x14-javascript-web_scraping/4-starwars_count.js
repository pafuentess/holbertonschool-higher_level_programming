#!/usr/bin/node

const request = require('request');
let count = 0;
request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const i of (JSON.parse(body).results)) {
      for (const j of i.characters) {
        if (j.endsWith('18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
