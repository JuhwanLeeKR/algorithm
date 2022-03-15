C = int(input())

for _ in range(C):
    scoreList = list(map(int, input().split()))
    average = sum(scoreList[1:]) / scoreList[0]

    def upAverage(score):
        if score > average:
            return score
        else:
            return

    result = list(filter(upAverage, scoreList))  # 평균이상 학생 점수 리스트
    percent = '%.3f' % (len(result) / len(scoreList[1:]) * 100)
    print(f'{percent}%')
