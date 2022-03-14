# 2525번 https://www.acmicpc.net/problem/2525

h, m = input().split()
dur = int(input())

h, m = int(h), int(m)

# h, m에 더해줄 시간을 구합니다
durH = dur//60
durM = dur % 60

h += durH
m += durM

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)
