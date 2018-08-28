#!/usr/bin/node

function secondMax (a) {
  if (a.length === 0 || a.length === 1) {
    return 0;
  }
  a.sort((n, m) => n - m).pop();
  return Math.max(...a);
}

let arrayStr = process.argv.slice(2);
let arrayNum = arrayStr.map(Number);
console.log(secondMax(arrayNum));
