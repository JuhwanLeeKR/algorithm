# 10818번, https://www.acmicpc.net/problem/10818

N = int(input())
arr = list(map(int, input().split()))

print(min(arr), max(arr))

# 2562번, https://www.acmicpc.net/problem/2562

arr = []
for _ in range(1, 10):
    n = int(input())
    arr.append(n)

# index(value, start, end)
position = arr.index(max(arr)) + 1

print(max(arr), position, sep="\n")

'''
간소화된 코드
n = [int(input()) for i in range(9)]
print(max(n), n.index(max(n)) + 1, sep='\n')
'''

# 2577번, https://acmicpc.net/problem/2577
n = [int(input()) for _ in range(3)]
arr = list(str(n[0]*n[1]*n[2]))

for i in range(10):
    # string으로 바꿀때 ''이 아닌 str을 사용하자
    print(arr.count(str(i)))
