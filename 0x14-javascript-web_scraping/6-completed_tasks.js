#!/usr/bin/node
// completed task

const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const users = {};
  const myjson = JSON.parse(body);
  for (let i = 0; i < myjson.length; i++) {
    if (myjson[i].userId in users === false) {
      users[myjson[i].userId] = 0;
    }
    if (myjson[i].completed) {
      users[myjson[i].userId] += 1;
    }
  }
  console.log(users);
});
