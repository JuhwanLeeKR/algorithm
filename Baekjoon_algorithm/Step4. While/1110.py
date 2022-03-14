# 1110번, https://www.acmicpc.net/problem/1110

n = input()

if int(n) < 10:
    n = '0' + n
count = 0

newN = list(n)
while True:
    result = int(newN[0]) + int(newN[1])
    if result < 10:
        result = str('0' + str(result))
    else:
        result = str(result)

    newNum = newN[1] + result[1]
    newN = str(newNum)
    count += 1

    if newN == n:
        break

print(count)

# 간단하게 만들 예시 답안
n = int(input())
num = n
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10
    num = (b * 10) + c

    cnt = cnt + 1
    if (num == n):
        break
print(cnt)
