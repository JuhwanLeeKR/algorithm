"""

첫째 줄에 최대 100글자
"""

import sys

input = sys.stdin.readline

word = input().strip()

croatiaWord = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatiaWord:
    word = word.replace(i, "A")

print(len(word))
