#!/usr/bin/node
const request = require('request');
let epi = process.argv[2];
request.get(`http://swapi.co/api/films/${epi}`, function (error, response, body) {
  if (error) { console.log(error); } else {
    console.log(JSON.parse(body)['title']);
  }
});
