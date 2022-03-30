import sys

input = sys.stdin.readline

li = list(map(str, input().rstrip()))

li.sort(reverse=True)
result = int("".join(li))
print(result)
