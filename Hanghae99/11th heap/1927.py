# 파이썬 공식문서 heapq 알고리즘에 대한 설명
# https://docs.python.org/ko/3/library/heapq.html

"""
1. 첫 줄에 연산의 개수 N(1<=N<=100000)이 주어진다.
2. 다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수x
3. x가 자연수 => 배열에 x를 추가
4. x가 0 => 배열에서 가장 작은 값을 출력하고 제거
5. 0<=x<2^31 자연수 또는 0
6. 출력: 입력에서 0이 주어진 횟수만큼 답을 출력
    만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라하면 0을 출력
"""

"""

"""
import sys
import heapq

input = sys.stdin.readline

n = int(input())
list = []

for _ in range(n):
    x = int(input())

    if x > 0:
        heapq.heappush(list, x)

    # x가 0일때는 가장 작은 값을 출력하고 제거한다.
    # 배열이 비어 있으면 0을 출력한다.
    if x == 0:
        if len(list) == 0:
            print(0)
        else:
            print(heapq.heappop(list))
