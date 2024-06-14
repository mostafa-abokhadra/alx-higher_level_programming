#!/usr/bin/node
// episode title
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const myjson = JSON.parse(body);
    console.log(myjson.title);
  }
});
