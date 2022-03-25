"""
각 자리가 등차수열을 이룬다.
1000이하
"""
import sys

input = sys.stdin.readline

n = int(input())

result = 0
for i in range(1, n + 1):
    numList = list(map(int, str(i)))
    if i < 100:
        result += 1
    elif numList[1] - numList[0] == numList[2] - numList[1]:
        result += 1

print(result)
