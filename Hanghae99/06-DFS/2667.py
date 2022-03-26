n = int(input())
li = []


for _ in range(n):
    cols = list(map(int, input()))
    li.append(cols)

rows, cols = len(li), len(li[0])
print(rows, cols)

count = 0

numList = []

stack = []

for row in range(rows):
    for col in range(cols):
        if li[row][col] != 1:
            continue

        count += 1
        stack.append((row, col))

        while stack:
            tmp = stack.pop()
            y, x = tmp

            # 방문 표시하기
            li[y][x] = "0"
            # 집의 수 더하기

            # 1. 북쪽으로 갈 수 있을까?
            if y > 0:
                if li[y - 1][x] == "1":
                    stack.append((y - 1, x))
            # 2. 서쪽으로 갈 수 있을까?
            if x > 0:
                if li[y][x - 1] == "1":
                    stack.append((y, x - 1))
            # 3. 남쪽으로 갈 수 있을까?
            if y < rows - 1:
                if li[y + 1][x] == "1":
                    stack.append((y + 1, x))
            # 4. 동쪽으로 갈 수 있을까?
            if x < cols - 1:
                if li[y][x + 1] == "1":
                    stack.append((y, x + 1))


print(count)

# 상하좌우 검사
# 숫자를 더해줘야함.
# 단지수를 출력하고 집의 수를 오름 차순으로 나타내준다.


"""n = int(input())  # 지도의 크기 받음
apt = []  # 지도를 담을 빈 배열
for _ in range(n):  # 지도의 크기만큼 받아줌
    apt.append(list(map(int, input())))
# 지도에서 이동할 위치
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 각 단지들의 집의 수를 넣어줄 빈배열
result = []

for i in range(n):
    for j in range(n):
        # 지도에서 1인 곳들을 찾아줌
        if apt[i][j] == 1:
            cnt = 1  # 1이었던 곳은 확정이므로 1부터 시작
            apt[i][j] = 0  # 시작지점 방문처리
            stack = [(i, j)]  # 스택에 시작지점을 넣어줌

            while stack:
                x, y = stack.pop()
                for k in range(4):
                    nx = x + dx[k]  # 상하좌우 이동
                    ny = y + dy[k]
                    # 범위를 벗어나는 경우에는 스택에 추가되지 않음
                    if nx < 0 or ny < 0 or nx >= n or ny >= n or apt[nx][ny] == 0:  #
                        continue
                    else:
                        apt[nx][ny] = 0  # 스택에 넣기전 방문처리.0.
                        cnt += 1  # 단지들의 수만큼 넣어줌
                        stack.append((nx, ny))  # 스택에 해당 집을 넣어줌
            # while문이 끝났다면 해당 단지의 집의 수(집의 수만큼 더해줬음)를 결과 배열에 넣어줌
            result.append(cnt)
print(len(result))  # result 배열의 길이 = 단지의 수
result = sorted(result)  # 각 단지내 집의 수를 오름차순으로 정렬해야한다고 했기에 정렬
for i in result:  # 오름차순 된 단지별 집의 수를 프린트
    print(i)"""
