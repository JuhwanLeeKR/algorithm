# https://www.delftstack.com/ko/howto/python/case-insensitive-string-comparison-in-python/
# 파이썬에서 대소문자를 구분하지 않는 문자열 비교

a = list(input().upper())  # 출력값이 대문자라서 upper()을 사용

count = {}
for i in a:  # try, except로 갯수를 찾을 수 있다
    try:
        count[i] += 1
    except:
        count[i] = 1
# aSet = list(set(a))
# dictionary.values()dp max()를 사용하여 최대값을 구할 수 있다

result = []
for key, value in count.items():  # for문 value로 key값 구하기
    if value == max(count.values()):
        result.append(key)
# result 값이 2개 이상이면면 ?표 출력
if len(result) != 1:
    print("?")
else:
    print("".join(result))


'''
# 코드 줄이기
n=input()
n=n.upper()
B=[]
A=[]
for i in n:
    if i not in B:
        B.append(i)
for i in B:
    A.append(n.count(i))
if A.count(max(A)) > 1:
    print('?')
else:
    print(B[A.index(max(A))])
'''
