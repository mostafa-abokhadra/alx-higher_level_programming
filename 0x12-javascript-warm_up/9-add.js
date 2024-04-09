#!/usr/bin/node

function add (a, b) {
  console.log(Number(process.argv[2]) + Number(process.argv[3]));
}

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('NaN');
} else {
  add(process.argv[2], process.argv[3]);
}
