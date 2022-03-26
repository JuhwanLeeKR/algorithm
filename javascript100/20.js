/*
# 문제20 : 몫과 나머지

공백으로 구분하여 두 숫자가 주어집니다.
두번째 숫자로 첫번째 숫자를 나누었을 때 **그 몫과 나머지를 공백으로 구분하여 출력하세요.**

입출력

입력 : 10 2
출력 : 5 0
*/

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
let A, B;
rl.on('line', (line) => {
  input = line.split(' ').map((el) => parseInt(el));
  A = input[0];
  B = input[1];
  solution(A, B);
  rl.close();
});

const solution = (a, b) => {
  let c, d;
  c = parseInt(a / b);
  d = a % b;
  console.log(c, d);
};

/*
const n = prompt('수를 입력하세요.').split(' ');

const result = Math.floor(parseInt(n[0], 10) / parseInt(n[1], 10));
const left = parseInt(n[0], 10) % parseInt(n[1], 10);

console.log(result, left);
*/
