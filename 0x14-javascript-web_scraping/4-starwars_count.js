#!/usr/bin/node
const request = require('request');
let api = process.argv[2];
request.get(api, function (error, response, body) {
  if (error) { console.log(error); } else {
    let counter = 0;
    let resp = JSON.parse(body)['results'];
    for (let chars of resp) {
      for (let wedge of chars['characters']) {
        if (wedge.includes('18')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
