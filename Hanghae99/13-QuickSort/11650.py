"""
2차원 평면 위의 점 N개가 주어진다.
좌표를 x 좌표가 증가하는 순(오름차순)
x좌표가 같으면 y좌표가 증가하는 순서로 (오름차순)
"""
import sys

input = sys.stdin.readline

n = int(input())
list = []
for _ in range(n):
    x, y = input().split()
    list.append([int(x), int(y)])

list.sort(key=lambda x: (x[0], x[1]))

for i in range(n):
    print(" ".join(map(str, list[i])))

"""
# 입력
5
3 4
1 1
1 -1
2 2
3 3

# 출력
1 -1
1 1
2 2
3 3
3 4
"""
