"""
회원들의 나이와 이름이 주어지고
나이를 증가하는 순으로(오름차순)
나이가 같으면 먼저 가입한 사람이 앞에 오는 순 (입력은 가입한 순서대로)
"""
import sys

input = sys.stdin.readline

n = int(input())
li = []

# 따로 index를 추가를 해줄까 했으나, python의 sort가 같은 값 안에서는 서로 순서가 바뀌질 않기 때문에 상관 없다는 답변을 들었다.

for i in range(n):
    li.append(list(map(str, input().split())))

li.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(li[i][0], li[i][1])
"""
3
21 Junkyu
21 Dohyun
20 Sunyoung
"""
