const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
let input = [];
let result = [];
let list = [];
let check = new Array(13).fill(false);
rl.on('line', function (line) {
  input.push(line);
})
  .on('close', async function () {
  // 답안 작성
  let answer = [];  
  input.pop(); 
  answer = lotto(input)  
  console.log(answer)
  process.exit();
});
//재귀 함수를 반복하면서 결과를 매번 저장할 반복문 함수
let lotto = function(input){
  let answer = '';
  for(let i=0;i<input.length;i++){
    let tmp = input[i].split(' ');
    let m = tmp.splice(0,1)
    let n = tmp.length;
    re(0,n,6,tmp,-1);
    answer += result.join('\n') + '\n\n'    
    result = [];
    check = new Array(13).fill(false);
    list = []
  }  
  return answer.slice(0,-2);
}
//기존 오름차순 수열만 구하는 재귀함수
let re = function(cnt,n,m, numbers,min){
  if(cnt==m){
    result.push(list.join(' '))
    return ;
  }
  for(let i=0;i<n;i++){
    if(!check[i]&&numbers[i]*1>min){
      check[i] = true;
      list[cnt] = numbers[i];
      re(cnt+1,n,m,numbers,numbers[i]*1);
      check[i] = false;
    }
  }
  return ;
}