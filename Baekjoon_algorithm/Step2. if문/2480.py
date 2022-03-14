# 2480번 https://www.acmicpc.net/problem/2480

# Tip) sort는 반환 값이 None 입니다!
num = sorted(list(map(int, input().split())), reverse=True)

money = int()
if num[0] == num[1] == num[2]:
    money = 10000 + num[0] * 1000
elif (num[0] == num[1]) or (num[1] == num[2]):
    money = 1000 + num[1]*100
else:
    money = num[0]*100

print(money)
