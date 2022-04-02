/*
# 문제70 : 행렬 곱하기

행렬 2개가 주어졌을 때 곱할 수 있는 행렬인지 확인하고 곱할 수 있다면 그 결과를 출력하고,
곱할 수 없다면 -1을 출력하는 프로그램을 만들어주세요.

입력
a = [[1, 2],
		[2, 4]]

b = [[1, 0],
		[0, 3]]

출력
[[1, 6],
[2, 12]]
*/
a = [
  [1, 2],
  [2, 4],
];

b = [
  [1, 0],
  [0, 3],
];

const solution = (a, b) => {
  if (a[0].length !== b.length || a.length !== b[0].length) return -1;
  result = [];
  const len = a[0].length;

  if (len === b.length) {
    for (let i = 0; i < len; i++) {
      let row = [];
      for (let j = 0; j < len; j++) {
        let x = 0;
        for (let k = 0; k < len; k++) {
          x += a[i][k] * b[k][j];
        }
        row.push(x);
      }
      result.push(row);
    }
    return result;
  }
};

console.log(solution(a, b));
