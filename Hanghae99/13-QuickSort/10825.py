"""
1. 국어 점수가 감소하는 순서로(내림차순)
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로(오름차순)
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로(내림차순)
4. 모든 점수가 같으면 사전 순으로 증가 (오름차순)


"""
import sys

input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    name, korean, english, math = input().split()
    list.append([name, int(korean), int(english), int(math)])

list.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(list[i][0])

"""
입력
12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90
"""
