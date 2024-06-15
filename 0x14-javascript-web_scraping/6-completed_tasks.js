/*#!/usr/bin/node
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
*/
#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
