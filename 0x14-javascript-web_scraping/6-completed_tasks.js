#!/usr/bin/node
// completed tasks

const request = require('request');

request(process.argv[2], (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    const myjson = JSON.parse(body);

    for (let i = 0; i < myjson.length; ++i) {
      const userId = myjson[i].userId;
      const completed = myjson[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }
    console.log(completedTasksByUsers);
  }
});
