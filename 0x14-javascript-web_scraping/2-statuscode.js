#!/usr/bin/node
// request module

const request = require('request');
request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error('error = ' + error);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
