'''
5         N    자연수
4 1 5 2 3 A[N] 정수
5         M    자연수
1 3 7 9 5      A안에 존재하는지 알아내자
'''

import sys


n = int(sys.stdin.readline())
aList = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
bList = list(map(int, sys.stdin.readline().split()))

# 중복제거
setAList = set(aList)
setBList = set(bList)

intersection = list(setAList & setBList)

result = []
for i in range(len(bList)):
    if bList[i] in intersection:
        print(1)
    else:
        print(0)

## 시간초과
#https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10816-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%EC%8B%A4%EB%B2%844-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89
####