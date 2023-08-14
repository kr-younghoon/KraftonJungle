const fs = require('fs');
const [n, input] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const inputArr = input.trim().split(" ")

const in1 = n;
const in2 = input;
let sum = 0;

for (var i = 0; i < in1; i++) {
    let num = Number(in2[i]);
    sum += num;
}

console.log(sum);