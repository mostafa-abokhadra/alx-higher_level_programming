#!/usr/bin/node
// writing script to a file

const fs = require('node:fs');

try {
  fs.writeFile(process.argv[2], process.argv[3], (err) => {
    if (err) {
      console.log(err);
    }
  });
} catch (err) {

}
