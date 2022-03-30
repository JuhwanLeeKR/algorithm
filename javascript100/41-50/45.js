/*
# 문제45 : getTime()함수 사용하기

Date객체의 메소드 중 하나인 getTime()은 1970년 1월 1일 0시 0분 0초 이후로부터 지금까지 흐른 시간을 천분의 1초 단위(ms)로 반환합니다.

이를 이용하여 **현재 연도(2019)를 출력해보세요.**
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

// 입력이 어떻든 현재 년도가 나온다.
const solution = (input) => {
  const date = new Date();
  let getTime = date.getTime();
  // ms니깐 1000으로 나눈다
  getTime = getTime / 1000;
  // 365일로 나눈다
  getTime = getTime / 365;
  // 24시간으로 나눈다
  getTime = getTime / 24;
  // 3600 분으로 나눈다
  getTime = getTime / 3600;
  // 년을 구하니깐 소수점은 버린다
  getTime = Math.floor(getTime);
  // 1970년부터 시작해서
  getTime = getTime + 1970;
  return console.log(getTime);
};

/*
const d = new Date();

let year = d.getTime();
year = Math.floor(year/(3600*24*365*1000))+1970

console.log(year);
*/
