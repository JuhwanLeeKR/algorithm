/*
# 문제41 : 소수판별

숫자가 주어지면 **소수인지 아닌지 판별하는 프로그램**을 작성해주세요.
소수이면 YES로, 소수가 아니면 NO로 출력해주세요.
(소수 : 1과 자기 자신만으로 나누어떨어지는 1보다 큰 양의 정수)
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

// 소수
// 1. 1과 자신만으로 나누어 떨어지는 수
// 1. input 값을 2로 나누어진 수 이상이면 고려할 필요가 없다.
const solution = (input) => {
  let answer = 'YES';
  for (let i = 2; i <= input / 2; i++) {
    if (input % i === 0) {
      answer = 'NO';
      break;
    }
  }
  return console.log(answer);
};

/*
const num = prompt('숫자를 입력하세요.');

function check_prime(num) {
  for (let i=2; i<num; i++) {
    const result = num % i;
    if (result === 0) {
      console.log('NO');
      return false;
    }
  }
  if (num === 1) {
    console.log('NO');
    return;
  }
  console.log('YES');
}

check_prime(num);
*/
