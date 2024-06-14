#!/usr/bin/node
// no of movies actress is present

const request = require('request');
let str = '';
for (let i = process.argv[2].length; i >= 0; i--) {
  if (process.argv[2][i] === '/') {
    for (let j = 0; j < i; j++) {
      str = str + process.argv[2][j];
    }
    str += '/people/18';
    break;
  }
}
request(process.argv[2] , (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    request(JSON.parse(body).results[0].characters[15], (error, response, body) => {
      console.log(JSON.parse(body).films.length)
    });
  }
});
