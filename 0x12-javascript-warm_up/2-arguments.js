#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
// console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
