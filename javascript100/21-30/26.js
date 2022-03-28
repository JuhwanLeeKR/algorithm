/*
# 문제26 : 행성 문제2

우리 태양계를 이루는 행성은 수성, 금성, 지구, 화성, 목성, 토성, 천왕성, 해왕성이 있습니다.
이 행성들의 영어 이름은 Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune입니다.

**행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램**을 만들어 주세요.
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
  let result;
  switch (input) {
    case '수성':
      result = 'Mercury';
      break;
    case '금성':
      result = 'Venus';
      break;
    case '지구':
      result = 'Earth';
      break;
    case '화성':
      result = 'Mars';
      break;
    case '목성':
      result = 'Jupiter';
      break;
    case '토성':
      result = 'Saturn';
      break;
    case '천왕성':
      result = 'Uranus';
      break;
    case '해왕성':
      result = 'Neptune';
      break;
    default:
      result = '행성 이름을 한글로 입력해 주세요!';
  }
  console.log(result);
};

/*
const planets = {
	'수성' : 'Mercury',
	'금성' : 'Venus',
	'지구' : 'Earth',
	'화성' : 'Mars',
	'목성' : 'Jupiter',
	'토성' : 'Saturn',
	'천왕성' : 'Uranus',
	'해왕성' : 'Neptune',
};

const name = prompt("행성의 이름을 입력하세요.");

console.log(planets[name]);

// object를 활용하여 더욱 간단하게 할 수 있다.
*/
