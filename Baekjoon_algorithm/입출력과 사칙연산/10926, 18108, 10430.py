# 10926번 https://www.acmicpc.net/problem/10926
a = input()

print(a+'??!')

# 18108번 https://www.acmicpc.net/problem/18108
a = input()

print(int(a) - 543)

# 10430번 https://www.acmicpc.net/problem/10430
a, b, c = input().split()

a, b, c = int(a), int(b), int(c)

print((a+b) % c)
print(((a % c) + (b % c)) % c)
print((a*b) % c)
print(((a % c)*(b % c)) % c)

# 더 짧은 방법
A, B, C = map(int, input().split())
print((A+B) % C, ((A % C)+(B % C)) % C, (A*B) %
      C, ((A % C)*(B % C)) % C, sep="\n")
