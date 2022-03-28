/*
# 문제2 : 배열의 내장함수

<pass>부분에 배열 내장함수를 이용하여 코드를 입력하고 다음과 같이 출력되게 하세요.

데이터
var arr = [200, 100, 300];
//pass
console.log(arr);

출력
[200, 100, 10000, 300]
*/
const arr = [200, 100, 300];

arr.splice(2, 0, 10000);
console.log(arr);

/*
var arr = [200, 100, 300];
arr.splice(2, 0, 10000); 
// splice() 메서드는 배열의 요소를 삭제 또는 교체하거나 새 요소를 추가하여 배열의 내용을 변경합니다.
console.log(arr);
*/
