#!/usr/bin/node

const value = process.argv[2];

if (!isNaN(Number(value))) {
  console.log('My number:', Number(value));
} else {
  console.log('Not a number');
}
