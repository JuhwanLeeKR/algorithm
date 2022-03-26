// node.js로 콘솔이용하여 값 입력 받기
// https://bluehorn07.tistory.com/49
/*
# 문제10 : 별 찍기

크리스마스 날, 은비는 친구들과 함께 파티를 하기로 했습니다. 그런데, 크리스마스 트리를 사는 것을 깜빡하고 말았습니다. 온 가게를 돌아다녀 봤지만 크리스마스 트리는 모두 품절이었습니다. 
하는 수 없이 은비는 프로그래밍으로 트리를 만들기로 합니다. 

**은비를 위해 프로그램을 작성해 주세요.**

입력
5

출력
    *
   ***
  *****
 *******
*********
*/

// 기존 제로초?님 강의에서 접해봤던 문제

//////////////////////////////////////////////
const readline = require('readline');

// 인터페이스 객체를 만들자.
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let N; // 정수를 저장할 변수
rl.on('line', (line) => {
  N = Number(line);
  createStar(N);
  rl.close(); // 입력을 꺼줍니다.
});

let result = '';

const createStar = (n) => {
  for (let i = 1; i <= n; i++) {
    let print = '';
    for (let j = 1; j <= n - i; j++) {
      print += ' ';
    }
    for (let k = 1; k <= 2 * i - 1; k++) {
      print += '*';
    }
    result += `${print}\n`;
  }
  console.log(result);
};
