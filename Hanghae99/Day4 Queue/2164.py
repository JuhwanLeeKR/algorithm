from collections import deque
# deque를 import 해줘야한다

'''
N = int(input())
# list로 queue 생성
queue = []

# 숫자를 부여하는 배열 생성
for i in range(1, N+1):
    queue.append(i)

while len(queue):
    queue.pop(0)  # 첫번째 카드를 버린다.
    queue.append(queue[0])  # 맨 위 카드를 끝에 놓는다.
    queue.pop(0)  # 끝에 추가한 카드를 삭제한다.

    if len(queue) == 1:
        break

print(queue[0])
'''

######################################
# 시간초과가 뜨므로 deque를 사용해야한다.
######################################

'''
from collections import deque

N = int(input())
queue = []

# 숫자를 부여하는 배열 생성
for i in range(1, N+1):
    queue.append(i)

deque = deque(queue)

while len(queue):
    deque.popleft()
    move = deque.popleft()
    deque.append(move)

    if len(deque) == 1:
        break

print(deque[0])
'''

######################################
# 좀 더 간결하게
######################################

N = int(input())

deque = deque([i for i in range(1, N+1)])

while(len(deque) > 1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])
