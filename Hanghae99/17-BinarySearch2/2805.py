"""
상근이는 나무 M미터가 필요
절단기 높이 H 지정
떡볶이 떡 문제와 유사함

나무의 수 n 나무의 길이 m

4 7
20 15 10 17

15

5 20
4 42 40 26 46

36
"""
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
treeHeight = list(map(int, input().split()))

currentHeight = 0

start = 0
end = max(treeHeight)

while start <= end:
    mid = (start + end) // 2
    recievedTree = 0
    for i in treeHeight:
        if i > mid:
            recievedTree += i - mid
        if recievedTree > m:
            break

    if recievedTree < m:
        end = mid - 1
    else:
        currentHeight = mid
        start = mid + 1

print(currentHeight)
