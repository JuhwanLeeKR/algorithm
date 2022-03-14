# 10952번, https://www.acmicpc.net/problem/10952

import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    print(a+b)

# 10951번, https://www.acmicpc.net/problem/10951

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except:
        break
