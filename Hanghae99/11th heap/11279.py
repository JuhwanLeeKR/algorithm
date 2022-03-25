# 1927번 문제의 반대라고 생각하면 쉽다.
# https://www.daleseo.com/python-heapq/
# heapq는 최소 힙 기능만을 동작한다.


import sys
import heapq

input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(list, (-x, x))  # (우선 순위, 값)

    # x가 0일때는 가장 큰 값을 출력하고 제거한다.
    # 배열이 비어 있으면 0을 출력한다.
    if x == 0:
        if len(list) == 0:
            print(0)
        else:
            print(heapq.heappop(list)[1])  # index 1
