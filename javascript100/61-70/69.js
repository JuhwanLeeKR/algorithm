/*
# 문제69 : 골드바흐의 추측

골드바흐의 추측(Goldbach's conjecture)은 오래전부터 알려진 정수론의 미해결 문제로, 2보다 큰 모든 짝수는 두 개의 소수(Prime number)의 합으로 표시할 수 있다는 것이다. 이때 하나의 소수를 두 번 사용하는 것은 허용한다. - 위키백과

위 설명에서 2보다 큰 모든 짝수를 두 소수의 합으로 나타낸 것을 골드바흐 파티션이라고 합니다.

예)
100 == 47 + 53
56 == 19 + 37

**2보다 큰 짝수 n이 주어졌을 때, 골드바흐 파티션을 출력하는 코드를** 작성하세요. 

* 해당 문제의 출력 형식은 자유롭습니다. 가능하시다면 골드바흐 파티션 모두를 출력하거나, 그 차가 작은 것을 출력하거나 그 차가 큰 것 모두 출력해보세요.
*/

// 소수 구하기
let prime = [];
let isPrime = true;

for (let i = 2; i < 100; i++) {
  for (let j = 2; j < i; j++) {
    if (i % j == 0) {
      isPrime = false;
    }
  }
  if (isPrime) {
    prime.push(i);
  }
  isPrime = true;
}

let val = parseInt(prompt('숫자를 입력하세요:'), 10);

let 골드바흐파티션 = [];

for (let n of prime) {
  if (prime.includes(val - n) && n <= val - n) {
    골드바흐파티션.push([n, val - n]);
  }
}

let 차 = 골드바흐파티션.map((e) => e[1] - e[0]);

let 작은값 = 골드바흐파티션[차.indexOf(Math.min.apply(null, 차))];
let 큰값 = 골드바흐파티션[차.indexOf(Math.max.apply(null, 차))];

console.log(골드바흐파티션);
console.log(작은값);
console.log(큰값);

/*
function prime_list(n){
    //에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    let sieve = []
    for(let i = 2; i < n; i++){
      sieve.push(true);
    }

    //n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    let m = parseInt(n ** 0.5, 10);
    for(let i = 2; i < m + 1; i++){
        if (sieve[i] == true){      // i가 소수인 경우 
          for(let j = i+i; j < n; j+=i){ // i이후 i의 배수들을 False 판정
                sieve[j] = false;
            } 
        }
    }

    // 소수 목록 산출
    let prime = [];
    for(let i = 2; i < n; i++){
      if (sieve[i] == true){
        prime.push(i);
      }
    }

    return prime;
}
*/
