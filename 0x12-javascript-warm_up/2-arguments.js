#!/usr/bin/node

// Get the count of arguments passed to the script
const argsCount = process.argv.length - 2;

// Check the number of arguments and print the corresponding message
if (argsCount === 0) {
	console.log("No argument");
} else if (argsCount === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
