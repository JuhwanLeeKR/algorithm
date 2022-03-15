n = int(input())
for _ in range(n):
    li = list(input())  # ['O','O','X','X','O','X','X','O','O','O']
    score = 0
    sumScore = 0
    for item in li:
        if item == 'O':
            score += 1
            sumScore += score
        else:
            score = 0
    print(sumScore)


'''
for _ in range(int(input())):print(sum(map(lambda x:(l:=len(x))*(l+1)//2,(s:=input().split("X")))))
'''

'''
n=int(input())
for i in range(n):
  a=list(input())
  score=0
  check=1
  for j in range(len(a)):
    if a[j]=='O':
      score+=check
      check+=1
    else:
      check=1
  print(score)
'''
