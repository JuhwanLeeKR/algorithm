# 1546번, https://www.acmicpc.net/problem/1546
# index 범위 밖인지 확인하기!

n = int(input())
score = list(map(int, input().split()))

li = []
for i in range(n):
    newScore = score[i] / max(score) * 100
    li.append(newScore)
aver = sum(li) / n
print(aver)

'''
n=int(input())
a=[0]*n
a=list(map(int,input().split()))
a.sort()
t=a[n-1]
print(sum(a)*100/t/n)
'''
