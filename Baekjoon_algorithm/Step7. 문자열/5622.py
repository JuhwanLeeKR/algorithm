"""
1을 걸때 2초
2를 걸때 3초
3을 걸때 4초
...
0을 걸때 11초
각 숫자에 해당하는 문자로 외운다

15 >= 첫째줄 대문자 길이 >=2
"""
import sys

input = sys.stdin.readline

word = list(map(str, input().strip()))  # strip()을 사용하여 '\n' 제거

alphabetList = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
result = 0

for i in range(len(word)):
    for j in alphabetList:
        if word[i] in j:
            result += alphabetList.index(j) + 3

print(result)
