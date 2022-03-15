# 3052번, https://www.acmicpc.net/problem/3052

li = []
count = 0
for _ in range(10):
    n = int(input())
    remainder = n % 42
    if remainder not in li:
        count += 1
    li.append(remainder)

print(count)


'''
print(len(set(map(lambda x:int(x)%42,open(0).read().split()))))
'''
