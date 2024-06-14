#!/usr/bin/node
// no of movies actress is present

const request = require('request');

let count = 0;
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const myjson = JSON.parse(body);
  for (let i = 0; i < myjson.results.length; i++) {
    const characters = myjson.results[i].characters;
    for (let j = 0; j < characters.length; j++) {
      let str = '';
      for (let k = characters[j].length - 2; k >= 0; k--) {
        if (characters[j][k] === '/') {
          break;
        }
        str += characters[j][k];
      }
      str = str.split('').reverse().join('');
      if (Number(str) === 18) {
        count += 1;
      }
    }
  }
  console.log(count);
});
