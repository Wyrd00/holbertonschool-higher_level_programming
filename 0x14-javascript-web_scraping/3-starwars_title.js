#!/usr/bin/node
const request = require('request');
let epi = process.argv[2];
request.get(`http://swapi.co/api/films/${epi}`, function (error, response, body) {
  console.log(JSON.parse(body)['title']);
});
