# 이것이 코딩테스트다 p.182
"""
내용이 너무 길어서 정확한 내용은 책을 참고하길 바랍니다.

두개의 배열 A B => N개의 원소로 구성되어있음, 모두 자연수
최대 K번의 바꿔치기 연산(A,B 배열 원소를 하나씩 골라서 바꿔치기)
최종목표: A 배열의 원소합이 최대
"""
"""
예시1
N=5, K=3
A = [1,2,5,4,3]
B = [5,5,6,6,5]

정답 26
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))
# A에서 가장 작은 요소를 B에서 가장 큰 요소와 바꾼다
# 단, A에서 가장 작은 요소는 B에서 가장 큰 요소보다 커야한다.

listA.sort
listB.sort(reverse=True)

print(listA, listB)

for i in range(k):
    if listA[i] < listB[i]:
        listA[i] = listB[i]
        listB[i] = listA[i]
    else:
        break

print(sum(listA))


"""
입력
5 3
1 2 5 4 3
5 5 6 6 5

출력
26
"""
