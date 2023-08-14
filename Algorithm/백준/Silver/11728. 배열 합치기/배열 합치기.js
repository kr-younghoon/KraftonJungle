let fs = require('fs');
// let input = fs.readFileSync('test.txt').toString().split('\n');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// 첫번째줄 -> 배열 A 의 크기 N, 배열 B 크기 M
// 두번째줄 -> 배열 A의 내용
// // 세번째줄 -> 배열 B의 내용


// console.log(input[1] + " " + input[2]);
let A = (input[1].split(" "));
let B = (input[2].split(" "));
let tmp = A.concat(B);
// console.log(tmp);
// console.log(tmp.split(" "));
tmp = tmp.sort((A, B) => A - B) ;

console.log(tmp.join(" "));
