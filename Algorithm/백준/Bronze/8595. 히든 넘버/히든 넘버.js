// 8595.js

// in1 : 단어의 길이
// in2 : 단어
let fs = require('fs');
// let input = fs.readFileSync('test.txt').toString().split('\n');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const in1 = input[0];
const in2 = input[1];
let tmp = 0;
let sum = 0;

for (i = 0; i < Number(in1); i++) {
    if (Number.isInteger(Number(in2[i]))) {
        tmp += in2[i];
    } else {
        sum += Number(tmp);
        tmp = 0;
    }
}
sum += Number(tmp);

console.log(sum);