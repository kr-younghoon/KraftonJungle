const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim();
let N = input;
let ans = "";
let i = 2;
while (N != 1) {
    if (N % i === 0) {
        console.log(i);
        N /= i;
    } else {
        i++;
    }
}
   