"""
전화번호 목록이 주어지고 일관성이 있는지 없는지

긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26

선영이 번호는 일관성이 없다.

테스트 케이스의 개수 t (1 <= t <= 50)
각 테스트 케이스 첫째 줄 전화번호 수 n (1 <= n <= 10000)

output = 일관성있으면 YES 아니면 NO
"""
"""
input:
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346

output:
NO
YES
"""
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numList = [input().rstrip() for _ in range(n)]
    # 오름차순으로 정렬해서 검사
    numList.sort()
    # print(numList)
    isValid = "YES"

    for i in range(n - 1):
        if numList[i + 1].find(numList[i]) == 0:
            isValid = "NO"
            break
    print(isValid)

"""
1. 숫자가 일치해도는 되는데 추가로 다른 부분이 있어야한다.
"""
