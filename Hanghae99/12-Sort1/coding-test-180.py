# 이것이 코딩테스트다 p.180
"""
- 첫 번째 줄에 학생의 수 N이 입력된다. (1<=N<=100000)
- 두 번째 줄부터 N + 1 번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다. 문자열 A의 길이와 학생의 성적은 100 이하의 자연수이다.

- 모든 학생의 이름을 성적이 낮은 순서대로 출력한다. 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
"""
# 2차원 배열 정렬을 사용
# https://haesoo9410.tistory.com/193

import sys

input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
    a, b = input().split()
    list.append([a, int(b)])

list.sort(key=lambda x: x[1])
for person in list:
    print(person[0], end=" ")
"""
3
홍길동 95
이순신 75
김김김 99

출력: 이순신 홍길동 김김김
"""

"""
# lambda를 쓰지 않는 방법입니다.
# sort는 index[0]을 순서로 정렬시킵니다.
import sys

input = sys.stdin.readline

n = int(input())
list = []

for i in range(n):
    a, b = input().split()
    list.append([int(b),a])

list.sort()
for person in list:
    print(person[1])
"""
