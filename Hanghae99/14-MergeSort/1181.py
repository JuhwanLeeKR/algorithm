"""
알파벳 소문자로 이루어진 N개의 단어
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로

입력 첫째줄 단어 n (1<= n <= 20000)
문자열의 길이 <= 50
여러번 입력 = 한번
"""
import sys

input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    word = input().rstrip()
    li.append(word)

li = list(set(li))
li.sort()
li.sort(key=lambda x: len(x))

for i in range(len(li)):
    print(li[i])


"""
# input
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""
