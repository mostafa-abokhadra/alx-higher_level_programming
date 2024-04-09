#!/usr/bin/node
if (process.argv[2] === undefined || !Number(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let l = 0; l < process.argv[2]; l++) {
    for (let i = 0; i < process.argv[2]; i++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
