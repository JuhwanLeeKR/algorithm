"""
캠프 때 쓸 N개의 랜선
영식이는 자체적으로 K개의 랜선 (길이 제 각각)
n개 보다 많이 만드는 것도 n개를 만드는 것에 포함

4 11
802
743
457
539

200
"""
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lanList = []
for i in range(k):
    lanList.append(int(input()))

start = 1
end = max(lanList)


while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lanList:
        lines += i // mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1


print(end)
