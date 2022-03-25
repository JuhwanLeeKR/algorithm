"""
그룹단어: 각 문자가 연속해서 but, 떨어져서 반복되면 그룹단어 x (ex.aba, abab)
"""
import sys

input = sys.stdin.readline

n = int(input())  # 100보다 작은 자연수

result = n
for i in range(n):
    word = input().strip()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            pass
        elif word[j] in word[j + 1 :]:
            result -= 1
            break


print(result)
