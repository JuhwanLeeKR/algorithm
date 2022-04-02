# 이코테 p.201 떡볶이 떡 만들기
"""
떡볶이 떡의 길이가 일정하지 않다.
대신 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰준다.
절단기 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단
낮은 떡은 안 잘리고 긴 떡은 잘린다.

손님이 요청한 총 길이 M
절단기에 설정할 수 있는 높이의 최댓값

첫 줄 떡의 개수 N과 요청한 떡의 길이 M

예시
4 6
19 15 10 17

15
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ricecakeHeight = list(map(int, input().split()))

# (ricecakeHeight[0] - 최댓값)의 합 >= 손님이 가져가는 떡 높이

cutHeight = 0

start = 0
end = max(ricecakeHeight)
while start <= end:
    mid = (start + end) // 2
    givenRicecake = 0
    for i in ricecakeHeight:
        if i > mid:
            givenRicecake += i - mid
    if givenRicecake < m:
        end = mid - 1
    else:
        cutHeight = mid
        start = mid + 1

print(cutHeight)
