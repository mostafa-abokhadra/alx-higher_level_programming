#!/usr/bin/node
// reading file
const fs = require('node:fs');
try {
  const data = fs.readFileSync(process.argv[2], 'utf-8');
  console.log(data);
} catch (err) {
  console.log(err);
}
