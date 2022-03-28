/*
# 문제31 : 자바스크립트 자료형의 복잡도

다음 배열 내장함수의 시간 복잡도가 O(1)이 아닌 것을 모두 고르시오.

1)  arr[i]
2)  arr.push(5)
3)  arr.slice()
4)  arr.pop()
5)  arr.includes(5)
*/

// 3(start부터 end까지 복사 O(n)), 5 (arr[0]부터 검사하기 때문에 O(n))

/*
# 답안

3)  arr.slice()
5)  arr.includes(5)

정답은 '3번', '5번' 입니다.
*/
