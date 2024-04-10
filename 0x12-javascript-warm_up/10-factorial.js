#!/usr/bin/node

function fact (num) {
  if (num === 0) {
    return 1;
  }
  return num * fact(num - 1);
}

if (process.argv[2] === undefined || !Number(process.argv[2])) {
  console.log('1');
} else {
  console.log(fact(process.argv[2]));
}
