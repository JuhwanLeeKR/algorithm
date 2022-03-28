# 11650에서 lambda식을 약간만 수정해주면 되는 문제

import sys

input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    x, y = input().split()
    list.append([int(x), int(y)])

list.sort(key=lambda x: (x[1], x[0]))

for i in range(n):
    print(" ".join(map(str, list[i])))
