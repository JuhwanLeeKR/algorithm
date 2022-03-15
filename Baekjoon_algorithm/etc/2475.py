n = list(map(int, input().split()))
remainder = sum(list(i*i for i in n)) % 10

print(remainder)

'''
# 코드 줄이기
print(sum(int(v)**2 for v in input().split())%10)
'''
