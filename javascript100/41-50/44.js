/*
# 문제44 : 각 자리수의 합

**사용자가 입력한 양의 정수의 각 자리수의 합을 구하는 프로그램**을 만들어주세요

**예를들어**
18234 = 1+8+2+3+4 이고 정답은 18 입니다.
3849 = 3+8+4+9 이고 정답은 24입니다.

입력 : 18234
출력 : 18

입력 : 3849
출력 : 24
*/

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;
rl.on('line', (line) => {
  input = Number(line);
  solution(input);
  rl.close();
});

const solution = (input) => {
  const toStr = String(input);
  const arr = toStr.split('');
  let result = 0;
  for (let i = 0; i < arr.length; i++) {
    result += Number(arr[i]);
  }
  return console.log(result);
};

/*
let n = prompt('숫자를 입력하세요.');
let sum = 0;

while(n !== 0){
  sum += (n % 10);
  n = Math.floor(n/10);
}

console.log(sum);
*/
