#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
console.log(url);
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    for (const i of JSON.parse(body).characters) {
      request(i, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
