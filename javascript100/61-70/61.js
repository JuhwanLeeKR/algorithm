/*
# 문제61 : 문자열 압축하기

문자열을 입력받고 연속되는 문자열을 압축해서 표현하고 싶습니다.

입력
aaabbbbcdddd

출력
a3b4c1d4

https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
*/

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;
rl.on('line', (line) => {
  input = line;
  solution(input);
  rl.close();
});

const solution = (input) => {
  let arr = input.split('').reduce((prev, curr) => {
    prev[curr] = ++prev[curr] || 1;
    return prev;
  }, {});
  const keys = Object.keys(arr);
  const values = Object.values(arr);
  result = '';
  for (let i = 0; i < keys.length; i++) {
    result += keys[i] + values[i];
  }

  return console.log(result);
};

/*
const user_s = new String(prompt('문자열을 입력하세요'));
let result_s = '';
let store_s = user_s[0];
let count = 0;

for (let i of user_s){
  if (i === store_s){
    count += 1;
  } else{
    result_s += store_s + String(count);
    store_s = i;
    count = 1;
  }
}

result_s += store_s + String(count);
console.log(result_s);
*/
