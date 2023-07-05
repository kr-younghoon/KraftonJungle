// 1062 : 가르침
/*

k개의 글자만 가르칠수 있음

남극 언어는 anta 로 시작 => tica로 끝난다

1 첫글자에 남극 단어 : 3 가르칠 수 있는 언어 K

1 번째 줄 = a n t r c i
2 번째 줄 = a n t h e l o t i c
3 번쨰 줄 = a n t c r i 

6개를 antrci로 하면 2개를 읽을수 있다

첫번째 방법 :
즉 문자열 중복을 제거한뒤에, 찻번째 줄과 길이가 같은것중에, 모든 단어가 같으면 max +=1 올린다

해당 max가 가장 크면 해당 answer을 출력하면됨

=> 하나만 차이나거나, 더배울수 있을때 문제가됨

두번째 방법:
문자얄 중복을 통해 배열에다 넣고
해당 단어로 만들수 있는 단어 조합을 찾는다
많으면 많으수록 좋음


*/

testCase = require("fs")
  .readFileSync(process.platform == "linux" ? "/dev/stdin" : "예제.txt")
  .toString()
  .trim()
  .split("\n");

[N, K] = testCase.shift().split(" ").map(Number);
const words = testCase.map((el) => new Set(el));

const learn = new Array(26).fill(0);
const already = ["a", "c", "i", "n", "t"];
let answer = 0;
const dfs = (idx, cnt) => {
  if (cnt == K - 5) {
    readcnt = 0;
    words.map((word) => {
      check = true;
      for (w of word) {
        if (!learn[w.charCodeAt() - "a".charCodeAt()]) {
          check = false;
          break;
        }
      }
      if (check) {
        readcnt += 1;
      }
    });
    answer = Math.max(answer, readcnt);
  }
  for (let i = idx; i < 26; i++) {
    if (!learn[i]) {
      learn[i] = true;
      dfs(i, cnt + 1);
      learn[i] = false;
    }
  }
};

const solution = () => {
  if (K < 5) {
    console.log(0);
    return;
  }
  if (K == 26) {
    console.log(N);
    return;
  }

  for (word of already) {
    learn[word.charCodeAt() - "a".charCodeAt()] = 1;
  }

  dfs(0, 0);
  console.log(answer);
};
solution();
