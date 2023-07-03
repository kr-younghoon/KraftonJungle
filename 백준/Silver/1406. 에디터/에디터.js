// 1406.js

let fs = require('fs');
// let input = fs.readFileSync('test.txt').toString().split('\n');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
/*
abcd
3
P x
L
P y */

function Solution() {
    const left = s.split("");
    const right = [];

    for (let i = 0; i < commands.length; i++) {
        const [command, value] = commands[i].split(" ");
        // console.log(command)
        switch (command) {
            case "L":
                if (left.length != 0) {
                    right.push(left.pop());
                }
                break;
            case "D":
                if (right.length != 0) {
                    left.push(right.pop());
                }
                break;
            case "B":
                if (left.length != 0) {
                    left.pop();
                }
                break;
            case "P":
                left.push(value);
                break;
        }
    }
    let result = left.concat(right.reverse()).join("");
    console.log(result);
}

let s = input[0];
const commands = [];
for (i = 2; i < input.length; i++) {
    commands.push(input[i]);
}
// console.log(commands);
Solution();