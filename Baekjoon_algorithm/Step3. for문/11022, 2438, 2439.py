# 11022번, https://www.acmicpc.net/problem/11022

t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')

# 2438번, https://www.acmicpc.net/problem/2438

n = int(input())

for i in range(1, n+1):
    print('*'*i)

# 2439번, https://www.acmicpc.net/problem/2439

n = int(input())

for i in range(1, n+1):
    print(' '*(n-i) + '*'*i)
