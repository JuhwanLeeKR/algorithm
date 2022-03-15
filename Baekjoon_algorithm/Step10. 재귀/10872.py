n = int(input())

result = 1
if n == 0:
    print(1)
else:
    numList = list(range(1, n+1))
    for num in numList:
        result *= num
    print(result)
