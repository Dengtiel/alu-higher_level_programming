#!/usr/bin/node

const originalList = require('./100-data').list;

console.log(originalList);

const mappedList = originalList.map((value, index) => value * index);

console.log(mappedList);
