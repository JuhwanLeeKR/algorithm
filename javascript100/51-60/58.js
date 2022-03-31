/*
# 문제58 : 콤마 찍기

원범이는 편의점 아르바이트가 끝난 후 정산을 하고자 합니다.
정산을 빨리하고 집에 가고 싶은 원범이는 프로그램을 만들려고 합니다.

**숫자를 입력받고 천 단위로 콤마(,)를 찍어주세요.**

예를 들어, **123456789**를 입력받았으면 **123,456,789**를 출력해야 합니다.
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
  const result = Number(input.toLocaleString());
  return console.log(result);
};

/*
// 내장함수 사용
const n = prompt('숫자를 입력해주세요.');
parseInt(n, 10);

console.log(n.toLocaleString());

// 재귀함수 사용
function comma(s) {
  if (s.length <= 3) {
    return s;
  } else {
    return comma(s.slice(0, s.length - 3)) + ',' + s.slice(s.length - 3);
  }
}

const n = prompt('숫자를 입력해주세요.');
console.log(comma(n));
*/
