# 2588번 https://www.acmicpc.net/problem/2588

a = input()
b = input()

a = int(a)

A = a * int(b[2])
B = a * int(b[1])
C = a * int(b[0])
D = a * int(b)

print(A, B, C, D, sep="\n")
