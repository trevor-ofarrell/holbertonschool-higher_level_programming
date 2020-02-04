#!/usr/bin/node
var args = process.argv.slice(1);
let size = parseInt(args[1])
if (!size) {
    console.log("Missing size")
}
for (i = 0; i < size; i++) {
    for (j = 0; j < size; j++) {
	console.log("X")
    }	
    console.log("")
}
