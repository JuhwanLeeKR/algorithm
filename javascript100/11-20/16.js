/*
# 문제16 : 로꾸거

문장이 입력되면 거꾸로 출력하는 프로그램을 만들어 봅시다.

입출력

입력 : 거꾸로
출력 : 로꾸거
*/

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input;
rl.on('line', (line) => {
  input = String(line);
  reverseSentence(input);
  rl.close(); // 입력을 꺼줍니다.
});

const reverseSentence = (sentence) => {
  const list = sentence.split('');
  list.reverse();
  const reverseList = list.join(''); // 정답을 참고하여 코드를 줄여보자
  console.log(reverseList);
};

/*
const n = prompt('입력하세요.');

const reverseString = n.split('').reverse().join('');

* split() 메서드는 문자열을 배열로 만들어 반환하고,
* reverse() 메서드는 배열의 순서를 반전하며,
* join() 메서드는 원소를 모두 붙여 문자열로 반환합니다.

console.log(reverseString);
*/
