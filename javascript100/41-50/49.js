/*
# 문제49 : 최댓값 구하기

순서가 없는 10개의 숫자가 공백으로 구분되어 주어진다. 주어진 숫자들 중 최댓값을 반환하라.
*/

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];
rl.on('line', (line) => {
  input = line.split(' ').map((el) => Number(el));
  solution(input);
  rl.close();
});

const solution = (input) => {
  const max = Math.max(...input);
  return console.log(max);
};

/*
let numbers = prompt('10개의 숫자를 입력하세요').split(' ').map((n) => {
  return parseInt(n, 10);
});

numbers.sort((a, b) => {
  return b-a;
});

console.log(numbers[0]);
*/
