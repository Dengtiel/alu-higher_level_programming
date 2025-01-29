#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

// Iterate through the original dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // If the occurrences count doesn't exist in newDict, create a new array
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  
  // Push the userId into the appropriate occurrences category
  newDict[occurrences].push(userId);
}

console.log(newDict);
