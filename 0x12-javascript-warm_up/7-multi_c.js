#!/usr/bin/node

const num = process.argv[2];
if (isNaN(Number(num))) {
  console.log('Missing number of occurrences');
}

for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
