# https://programmers.co.kr/learn/courses/30/lessons/42889
"""
실패율을 구하는 코드를 완성하라.
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
전체 스테이지의 개수 N
게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담긴 배열을 return

실패율이 같으면 작은 스테이지 부터
"""
"""
1의 개수 / 1 이상의 수 1 / 8
2의 개수 / 2 이상의 수 3 / 7
3의 개수 / 3 이상의 수 2 / 4
4의 개수 / 4 이상의 수 1 / 2
5의 개수 / 5 이상의 수 0 / 5
"""
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):
    answer = []
    li = []
    for i in range(1, N + 1):
        count = 0

        for j in range(len(stages)):
            if stages[j] >= i:
                count += 1

        if count == 0:
            count = 1
        li.append([i, stages.count(i) / count])

    li.sort(key=lambda x: (-x[1], x[0]))

    for i in range(N):
        answer.append(li[i][0])

    return print(answer)


solution(N, stages)
"""
#input
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
#output
[3,4,2,1,5]

#input
N = 4
stages = [4,4,4,4,4]
#output
	[4,1,2,3]
"""
