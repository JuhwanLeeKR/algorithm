# 2739번, https://www.acmicpc.net/problem/2739

n = int(input())

# range 함수를 사용
for i in range(1, 10):  # 1~9
    print(f'{n} * {i} = {n * i}')

# 10950번, https://www.acmicpc.net/problem/10950
# 언더바(_) 사용법: https://syujisu.tistory.com/130

T = int(input())

for _ in range(T):  # T만큼 반복
    a, b = map(int, input().split())
    print(a + b)

# 8393번, https://www.acmicpc.net/problem/8393

n = int(input())

result = int()
for i in range(n):
    result += i

print(result+n)
