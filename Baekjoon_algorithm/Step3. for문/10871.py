# 10871번, https://www.acmicpc.net/problem/10871
# n, x = map(int, input().split())
# a = list(map(int, input().split()))

n, x = map(int, input().split())
a = list(map(int, input().split()))

result = []
for i in range(n):
    if a[i] < x:
        result.append(a[i])

# Tip) 정수에 join을 사용하면 typeError가 뜬다!!!!!
result = ' '.join(str(_) for _ in result)
print(result)
