#!/usr/bin/node
if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log('0');
} else {
  let maxy = Number(process.argv[2]);
  let secondMaxy = Number(process.argv[2]);
  for (let i = 3; i < process.argv.length; i++) {
    if (Number(process.argv[i]) > maxy) {
      maxy = Number(process.argv[i]);
    }
  }
  let i = 2;
  if (maxy === Number(process.argv[2])) {
    i = 3;
    secondMaxy = Number(process.argv[3]);
  }
  for (i; i < process.argv.length; i++) {
    if (Number(process.argv[i]) > secondMaxy && process.argv[i] < maxy) {
      secondMaxy = Number(process.argv[i]);
    }
  }
  console.log(secondMaxy);
}
