// 기본적인 사용
{
  const readline = require('readline');

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });
}

// 한 줄에 문자 하나만 받을 때 (문제 39번)
/* input
querty
*/
{
  let input;
  rl.on('line', (line) => {
    input = line;
    solution(input);
    rl.close();
  });
}
// 한 줄에 숫자 하나만 받을 때 (문제 36번)
/* input
2
*/
{
  let input;
  rl.on('line', (line) => {
    input = Number(line);
    solution(input);
    rl.close();
  });
}

// 한 줄에 여러 숫자를 받을 때 (문제 38번)
/* input
97 86 75 66 55 97 85 97 97 95
*/
{
  let input = [];
  rl.on('line', (line) => {
    input = line.split(' ').map((el) => Number(el));
    solution(input);
    rl.close();
  });
}

// 한 줄에 여러 문자를 받을 때 (문제 37번)
/* input
원범 원범 혜원 혜원 혜원 혜원 유진 유진
*/
{
  let input = [];
  rl.on('line', (line) => {
    input = line.split(' ').map((el) => el);
    solution(input);
    rl.close();
  });
}

// 여러 줄 숫자를 받을때 (문제 40번)
/*input
50
5
20
20
20
20
20
*/
{
  let limit;
  let N;
  let input = [];
  let count = 0;

  rl.on('line', (line) => {
    if (count == 0) limit = Number(line);
    else if (count == 1) {
      N = Number(line);
    } else if (count < N + 2) {
      input.push(line);
      if (count === N + 1) {
        solution(limit, N, input);
        rl.close();
      }
    }
    count++;
  });
}

// 정답은 solution()을 사용한다.
{
  const solution = (input) => {
    let result;
    return console.log(input, result);
  };
}
