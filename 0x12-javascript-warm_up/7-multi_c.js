#!/usr/bin/node
let args = process.argv.slice(1);
let range = parseInt(args[1])
if (!range) {
    console.log("Missing number of occurrences")
}
for (i = 0; i < range; i++) {
    console.log("C is fun")
}
