#!/usr/bin/node

const fs = require('fs');

// Get arguments from command line
const [, , fileA, fileB, fileC] = process.argv;

try {
  // Read content from the source files
  const contentA = fs.readFileSync(fileA, 'utf8');
  const contentB = fs.readFileSync(fileB, 'utf8');

  // Concatenate and write to the destination file
  fs.writeFileSync(fileC, contentA + contentB, 'utf8');
} catch (error) {
  console.error('Error:', error.message);
}
