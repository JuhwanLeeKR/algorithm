"""
n개의 수가 주어졌을 때, 이를 오름차순
1<=n <=1000000
절댓값 1,000,000 (음수도 가능)
"""
import sys

input = sys.stdin.readline

n = int(input())
li = []

for i in range(n):
    li.append(int(input()))

li.sort()
for i in range(n):
    print(li[i])
