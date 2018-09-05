#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let obj = {};
    let bod = JSON.parse(body);
    for (let entry of bod) {
      if (entry['completed']) {
        if (obj[entry['userId']]) {
          obj[entry['userId']] += 1;
        } else {
          obj[entry['userId']] = 1;
        }
      }
    }
    console.log(obj);
  }
});
