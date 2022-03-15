'''
3           - 테스트 케이스 수
1 0         - 테스트 케이스1의 첫번째 줄 (문서의 개수 N, 현재 Queue에서 위치 M)
5           - 테스트 케이스1의 두번째 줄 (N개 문서의 중요도)
4 2         - 테스트 케이스2의 첫번째 줄 (문서의 개수 N, 현재 Queue에서 위치 M)
1 2 3 4     - 테스트 케이스2의 두번째 줄 (N개 문서의 중요도)
6 0         - 테스트 케이스3의 첫번째 줄 (문서의 개수 N, 현재 Queue에서 위치 M)
1 1 9 1 1 1 - 테스트 케이스3의 두번째 줄 (N개 문서의 중요도)
'''
# https://codetorial.net/python/collections_deque.html

from collections import deque

testNum = int(input())

for _ in range(testNum):
    n, m = list(map(int, input().split()))
    # 문서의 중요도
    secList = list(map(int, input().split()))
    # 문서에 인덱스를 부여하여 식별 가능하게 한다
    num = list(range(len(secList)))

    # 1. 중요도는 최대값
    # 2. 해당 중요도가 나올때까지 돌린다
    # 3. popleft 해준다
    # 4. 다음 중요도가 나올때까지 돌린다
    # 5. posDoc이 popleft 되면 그 수를 반환한다.

    # secList, index를 deque로 만들어준다
    deq = deque(secList)
    deqIndex = deque(num)
    # 해당하는 문서에 표식을 남긴다.
    deqIndex[m] = 'o'
    # leftpop 된 수를 저장
    count = 0

    # 반복문
    while True:
        # deq 맨 왼쪽 값(index 0)이 가장 중요도가 높다면
        if deq[0] == max(deq):

            count += 1
            # popleft()된 값이 'o'라면
            if deqIndex[0] == 'o':
                print(count)
                break
            else:
                deq.popleft()
                deqIndex.popleft()
        else:
            # 한칸 왼쪽으로 이동한다.
            deq.rotate(-1)
            deqIndex.rotate(-1)
