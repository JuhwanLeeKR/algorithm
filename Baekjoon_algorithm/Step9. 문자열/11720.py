n = int(input())
# list() 함수는 인자로서 시퀀스(문자열, 튜플) 또는 집합(딕셔너리) 또는 iterable(반복할 수 잇는) 개체(range())가 와야한다.
li = list(map(int, input()))
print(sum(li))
