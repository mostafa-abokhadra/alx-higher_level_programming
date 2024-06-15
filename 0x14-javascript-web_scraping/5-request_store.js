#!/usr/bin/node
// content of webpage

const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
