'''
A(고정) + B * n(노트북 개수) < C(노트북 가격) * n(개수)
손익 분기 개수 = A / (C-B)
'''
A, B, C = map(int, input().split())

if (C - B) <= 0:
    print("-1")
else:
    N = A / (C - B) + 1
    print(int(N))
