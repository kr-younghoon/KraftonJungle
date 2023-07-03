let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let str = input[0];
let del = input[1];
let len = del.length;
let stack = [];
for (let i = 0; i < str.length; i++) {
    let flag = false;
    if (str[i] === del[len - 1]) {
        for (let j = 0; j < len - 1; j++) {
            if (stack[stack.length - (j + 1)] === del[len - (j + 2)]) {
                continue;
            }
            flag = true;
            break;
        }
        if (flag) {
            stack.push(str[i]);
        } else {
            for (let k = 0; k < len - 1; k++) {
                stack.pop();
            }
        }
    } else {
        stack.push(str[i]);
    }
}
let result = stack.join("");
if (result === "") {
    console.log("FRULA");
} else {
    console.log(stack.join(""));
}