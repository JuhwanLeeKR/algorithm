from collections import deque

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]


def solution(progresses, speeds):
    # 1. progresses의 순서에 speeds의 인덱스 만큼 더해진다
    # 2. progresses[0]이 >=100이면 leftpop 된다
    # 3. leftpop 되었을때 다시 progresses[0]일때 값을 조회하여 >=0 이면 또 반복한다
    # 4. 이때 갯수도 저장해 주어야한다 (리스트 만들어서 따로 저장)
    # 5. len(progresses)가 0일때까지 반복
    # ! leftpop할때 speeds도 같이 빼줘야한다!
    deqProg = deque(progresses)
    deqSpd = deque(speeds)

    print(deqProg, deqSpd)

    answer = []
    while True:
        # leftpop 갯수를 저장하기 위한 변수 선언
        count = 0
        # deqProg와 deqSpd 요소를 전부 더해준다
        sumList = deque()
        for i in range(len(deqSpd)):
            sumList.append(deqProg[i] + deqSpd[i])
        deqProg = sumList
        # while문을 돌려서 [0]이 100이상일때 leftpop을 해준다 count +1 -> 아니면 종료
        while True:
            if len(sumList) == 0:
                break
            elif sumList[0] >= 100:
                sumList.popleft()
                deqSpd.popleft()
                count += 1
            else:
                break

        if count > 0:
            answer.append(count)
            print(count)
            count = 0

        if len(sumList) == 0:
            break

    return answer


# solution(progresses, speeds)
