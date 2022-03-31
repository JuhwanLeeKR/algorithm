"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표
H-Index를 나타내는 값인 h를 구하여라

발표한 논문 n편
h번 이상 인용된 논문이 h편 이상
나머지 논문이 h번 이하 인용되었다면 h의 최댓값 = h 인덱스
논문의 인용 횟수를 담은 배열 citations

발표한 논문의 수는 1편 이상 1000편 이하
논문 별 인용 횟수는 0회 이상 10000회 이하
"""


def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    answer = 0

    if max(citations) == 0:
        return 0

    for i in range(n):
        if citations[i] > i:
            answer += 1
    return answer


citations = [6, 6, 6, 6, 4, 0]
print(solution(citations))
"""
citations = [3, 0, 6, 1, 5]
return = 3
"""
