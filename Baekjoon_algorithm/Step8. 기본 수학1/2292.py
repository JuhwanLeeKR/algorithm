"""
1 -> 1
2-7 (6) -> 2
8-19 (12) -> 3
20-37 (18) -> 4
6씩 증가
"""
import sys

input = sys.stdin.readline

n = int(input())
root = 1
count = 1

while n > root:
    root = root + (6 * count)
    count += 1
print(count)
