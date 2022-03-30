"""
각 묶음의 카드의 수 A B
합쳐서 하나로 만드는 데에는 A+B번의 비교
(ex. 20장 30장 = 50번 비교)
최소한 몇번의 비교

1<=N<=100000
각 카드 묶음의 크기 = 1000보다 작거나 같은 양의 정수
"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
li = []
for i in range(n):
    heapq.heappush(li, int(input()))
# 가장 작은 수의 합부터 구한다

result = 0
for _ in range(n - 1):
    a = heapq.heappop(li)
    b = heapq.heappop(li)
    result += a + b
    heapq.heappush(li, a + b)

if n == 1:
    result = 0

print(result)

"""
6
100
1
20
10
20
40
"""
