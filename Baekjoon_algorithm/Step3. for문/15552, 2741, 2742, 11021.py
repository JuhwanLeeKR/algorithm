# 15552번, https://www.acmicpc.net/problem/15552
# Tip) input 대신 sys.stdin.readline()을 쓰는 이유
# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
from numpy import arange  # 2742번에 사용
import sys  # 15552번에 사용


t = int(input())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


# 2741번, https://www.acmicpc.net/problem/2741

n = int(input())
for i in range(1, n+1):
    print(i)

# 2742번, https://www.acmicpc.net/problem/2742

n = int(input())
# range(시작값, 종료값, 증가값)
for i in range(n, 0, -1):
    print(i)

# 11021번, https://www.acmicpc.net/problem/11021

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a+b}')
