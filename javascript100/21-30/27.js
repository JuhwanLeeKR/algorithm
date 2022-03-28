/*
# 문제27 : 객체 만들기

첫번째 입력에서는 학생의 이름이 공백으로 구분되어 입력되고, 두번째에는 그 학생의 수학 점수가 공백으로 구분되어 주어집니다.

두 개를 합쳐 **학생의 이름이 key**이고 **value가 수학 점수**인 객체를 출력해주세요.

입력
Yujin Hyewon Juhwan
70 100 30

출력
{'Yujin': 70, 'Hyewon': 100}
*/
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;
let input2;
let count = 0; // 몇번째 라인을 입력 받는지를 저장하는 변수

rl.on('line', (line) => {
  if (count == 0) input = line.trim().split(' ');
  // trim(): 문자열 좌우에서 공백을 제거하는 함수
  else if (count == 1) {
    input2 = line
      .trim()
      .split(' ')
      .map((num) => parseInt(num));
    solution(input, input2);
    rl.close();
  }
  count++;
});

const obj = {};
const solution = (input, input2) => {
  for (let i = 0; i < input.length; i++) {
    obj[input[i]] = input2[i];
  }
  console.log(obj);
};

/*
const keys = prompt('이름을 입력하세요').split(' ');
const values = prompt('점수를 입력하세요').split(' ');
const obj = {};

for (let i=0; i<keys.length; i++) {
  obj[keys[i]] = parseInt(values[i], 10);
}

console.log(obj);
*/
