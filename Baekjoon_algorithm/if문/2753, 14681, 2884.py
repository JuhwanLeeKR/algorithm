# 2753 https://www.acmicpc.net/problem/2753

a = int(input())

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print(1)
else:
    print(0)


# 14681 https://www.acmicpc.net/problem/14681

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print(2)

# 2884 https://www.acmicpc.net/problem/2884

h, m = input().split()

h = int(h)
m = int(m) - 45

if m >= 0:
    print(h, m)
elif h == 0 and m < 0:
    print(23, 60+m)
else:
    print(h-1, 60+m)
