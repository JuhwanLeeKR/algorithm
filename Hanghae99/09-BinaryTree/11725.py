"""
이진트리
root는 무조건 1
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
dict = defaultdict(list)
for i in range(n - 1):
    a, b = map(str, input().split())
    dict[a].append(b)
    dict[b].append(a)

def dfs(i):
    for n in dict[i]:
        if 
    

print(dict)
