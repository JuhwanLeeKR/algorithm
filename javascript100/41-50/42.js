/*
# 문제42 : 2020년

2020년 1월 1일은 수요일입니다. 2020년 a월 b일은 무슨 요일일까요?
두 수 a, b를 입력받아 2020년 a월 b일이 무슨 요일인지 리턴하는 함수 solution을 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각 SUN, MON, TUE, WED, THU, FRI, SAT 입니다.

예를 들어 a = 5, b = 24라면 5월 24일은 일요일이므로 문자열 "SUN"를 반환하세요.

**제한 조건**
2020년은 윤년입니다.
2020년 a월 b일은 실제로 있는 날입니다. 
(13월 26일이나 2월 45일 같은 날짜는 주어지지 않습니다.)
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

// 2020년은 윤년 (2월 29일까지 있음)
// SUN, MON, TUE, WED, THU, FRI, SAT
// a = 1, b = 1 WED
// 1  2  3  4  5  6  7  8  9  10 11 12
// 31 29 31 30 31 30 31 31 30 31 30 31
const solution = (input) => {
  let a = input[0];
  let b = input[1];

  if (
    a > 12 ||
    b > 31 ||
    (a === 2 && b > 29) ||
    (a === 4, 6, 9, 11 && b > 30)
  ) {
    return console.log('정확한 날짜를 입력해주세요!');
  }
  let dayNum = 0;
  const day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30];
  // 1월 1일이 수요일 dayNum === 1 'WED'
  const dayOfWeek = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
  for (let i = 0; i < a - 1; i++) {
    dayNum += day[i];
  }
  dayNum += b;
  const result = dayOfWeek[(dayNum % 7) + 2];

  return console.log(result);
};

/*
const month = prompt('월을 입력하세요.');
const date = prompt('일을 입력하세요.');

function solution(a,b){
    const day = ["SUN","MON","TUE","WED","THU","FRI","SAT"];

    const x = new Date('2020-'+a+'-'+b);
    return day[x.getDay()];
}
console.log(solution(month, date));
 */
