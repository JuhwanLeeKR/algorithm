# 1330번 https://www.acmicpc.net/problem/1330

a, b = input().split()

a, b = int(a), int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')


# 9498번 https://www.acmicpc.net/problem/9498

a = int(input())

if 89 < a <= 100:
    print('A')
elif 79 < a <= 90:
    print('B')
elif 69 < a <= 80:
    print('C')
elif 59 < a <= 70:
    print('D')
else:
    print('F')

# 더 나은 풀이
if a > 89:
    print('A')
elif a > 79:
    print('B')
elif a > 69:
    print('C')
elif a > 59:
    print('D')
else:
    print('F')
