#!/usr/bin/node
exports.esrever = function (list) {
  const listy = [];
  for (let i = list.length - 1, j = 0; i >= 0; i--, j++) {
    listy[j] = list[i];
  }
  return listy;
};
