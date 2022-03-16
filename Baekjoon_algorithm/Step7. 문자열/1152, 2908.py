# 1152
'''
import sys

sentense = list(sys.stdin.readline().split())
print(len(sentense))
'''

# 2908
a, b = list(map(str, input().split()))
A = list(a)
B = list(b)
reverseA = int("".join(list(reversed(A))))
reverseB = int("".join(list(reversed(B))))

if reverseA > reverseB:
    print(reverseA)
else:
    print(reverseB)


'''
#### 코드 줄이기
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])
print(a if a > b else b)
'''
