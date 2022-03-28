/*
# 문제19 : 제곱을 구하자

공백으로 구분하여 두 숫자 a와 b가 주어지면, **a의 b승**을 구하는 프로그램을 작성하세요.
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
  result = 1;
  for (let i = 1; i <= b; i++) {
    result *= a;
  }
  console.log(result);
};

/*
const n = prompt('수를 입력하세요.').split(' ');

console.log(Math.pow(parseInt(n[0], 10), parseInt(n[1], 10)));
*/
