#!/usr/bin/node

// Prints the first argument if it can be converted to an integer.

const num = parseInt(process.argv[2]);

console.log(Number.isInteger(num) ? `My number : ${num}` : 'Not a number');
