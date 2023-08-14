let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

// 첫번째 라인
const firstLine = input[0].split(" ");
// 두번째 라인
const secondLine = input[1].split(" ").map(el => Number(el));

const N = Number(firstLine[0]);
const M = Number(firstLine[1]);

let max = 0;
// i j k + x y z
for (let i = 0; i < firstLine[0]; i++) {
    for (let j = 0; j < firstLine[0]; j++) {
        for (let k = 0; k < firstLine[0]; k++) {
            if (i == j || i == k || j == k) {
                continue;
            }

            const sum = secondLine[i] + secondLine[j] + secondLine[k];
            if (sum > max && sum <= M) {
                max = sum
            }

            if (max == M) {
                break;
            }
        }
    }
}


console.log(max);