from collections import deque

n = int(input())
li = []
queue = deque()
count = 0

for i in range(n):
    li.append(list(map(int, input())))

while queue:
    temp = queue.popleft()
    count += 1
    
    for i in range(4):
        if 

print(li)
