"""
도현이의 집 N개가 수직선 위에 있다. 같은 좌표 x
어디서나 와이파이를 즐기기 위해서 집에 공유기 C개 설치
한 집에는 공유기 하나만, 인접한 두 공유기 사이의 거리를 가능한 크게
c개의 공유기를 n개의 집에 적당히 설치

5 3
1
2
8
4
9
"""
import sys

input = sys.stdin.readline

n, c = map(int, input().split())

homeLocation = []
for i in range(n):
    homeLocation.append(int(input()))

homeLocation.sort()
# 공유기 사이 거리 최솟값
start = 1
# 공유기 사이 거리 최대값
end = homeLocation[-1] - homeLocation[0]

maxGap = 0
while start <= end:
    mid = (start + end) // 2
    # 공유기 설치 위치
    value = homeLocation[0]
    count = 1

    for i in range(1, n):
        if homeLocation[i] >= value + mid:
            count += 1
            value = homeLocation[i]
    if count >= c:
        start = mid + 1
        maxGap = mid
    else:
        end = mid - 1
print(maxGap)
