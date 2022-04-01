# 이것이 코딩 테스트다 p.197
"""
동빈이네 전자 매장에는 부품이 N개
각 부품은 정수 형태의 고유한 번호가 있음.
손님이 M개 종류의 부품을 대량으로 구매 요청
손님이 문의한 부품 M개 종류를 모두 확인해서 견적서 작성

예시
N = 5
[8, 3, 7, 9, 2]
M = 3
[5, 7, 9]

있으면 yes 없으면 no
"""
import sys

input = sys.stdin.readline

n = int(input())
itemList = list(map(int, input().split()))
m = int(input())
orderList = list(map(int, input().split()))

result = []
for i in orderList:
    if i in itemList:
        result.append("yes")
    else:
        result.append("no")


print(" ".join(x for x in result))
"""
input
5
8 3 7 9 2
3
5 7 9

output
no yes yes
"""
"""
책을 참고해보니 이진탐색을 구현해서 풀이하는 방식도 있었고 3번째 풀이를 보니
비슷하지만 set을 쓰는 것을 발견했다. 재현님께 물어본 결과

set은 hash를 쓰기 때문에 if i in itemList: 에서 O(1)인데
list는 if i in itemList: 여기에서 O(N)의 시간을 써서 그럴겁니다

라고 답변을 주셨다.
"""
