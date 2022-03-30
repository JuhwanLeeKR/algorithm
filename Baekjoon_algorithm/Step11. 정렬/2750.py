import sys

input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

li.sort()
for i in range(n):
    print(li[i])

# 수정렬하기2와 같다
