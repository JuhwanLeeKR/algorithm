"""
가낭흔 한 최대의 예산
1. 모든 요청 가능하면 그대로
2. 없으면 특정한 정수 상한액


지방의 수 n
지방의 예산 요청
총 예산

4
120 110 140 150
485

127

5
70 80 30 40 100
450

100
"""
import sys

input = sys.stdin.readline

n = int(input())
requests = list(map(int, input().split()))
m = int(input())

if sum(requests) <= m:
    end = max(requests)
else:
    start = 0
    end = max(requests)
    while start <= end:
        mid = (start + end) // 2
        num = 0
        for i in requests:
            if i >= mid:
                num += mid
            else:
                num += i
        if num <= m:
            start = mid + 1
        else:
            end = mid - 1

print(end)
