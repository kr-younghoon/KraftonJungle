// 10974.js

// 모든 순열

let input = require('fs')
    .readFileSync(process.platform == 'linux' ? '/dev/stdin' : 'test.txt')
    .toString()
    .split('\n');

let n = +input.shift();
let target = input.shift();

const solution = (n) => {
    let answer = [];
    let visited = new Array(n + 1).fill(0);
    let tmp = [];
    const dfs = (cnt) => {
        if (cnt === n) {
            answer.push(tmp.join(' '));
        } else {
            for (let i = 1; i <= n; i++) {
                if (!visited[i]) {
                    visited[i] = 1;
                    tmp.push(i);
                    dfs(cnt + 1);
                    tmp.pop();
                    visited[i] = 0;
                }
            }
        }
    };
    dfs(0);

    return answer.join('\n');
};

console.log(solution(n, target));
