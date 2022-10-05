import sys
input = sys.stdin.readline

n = int(input())

class_lst = []

for i in range(n):
    money,day = map(int,input().split())
    class_lst.append([money,day])

class_lst.sort(key=lambda x:(-x[0],x[1]))

for i in range(n):
    if class_lst[i][1]<1:
        continue
    day = class_lst[i][1]
    for j in range(i+1,len(class_lst)):
        if class_lst[j][1]>=day:
            class_lst[j][1] -= 1

money = 0

for i in range(len(class_lst)):
    if class_lst[i][1]>0:
        money += class_lst[i][0]

print(money)