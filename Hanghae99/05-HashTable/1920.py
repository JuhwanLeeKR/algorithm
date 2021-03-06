'''
5         N    자연수
4 1 5 2 3 A[N] 정수
5         M    자연수
1 3 7 9 5      A안에 존재하는지 알아내자
'''

'''import sys


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
        print(0)'''

# 시간초과
'''
1920문제가 아닌 10816 풀이 입니다.
https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10816-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%EC%8B%A4%EB%B2%844-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89



import sys
input = sys.stdin.readline
#  변수로 받아서 사용가능하다

n = int(input())
# https://brownbears.tistory.com/37 파이썬 *(애스터리스크) 사용법
aList = [*map(int, input().split())]
m = int(input())
bList = [*map(int, input().split())]

count = {}
for i in aList:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for target in bList:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")'''
