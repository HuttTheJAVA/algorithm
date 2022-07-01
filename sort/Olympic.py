from collections import deque
import sys
input = sys.stdin.readline

n,k = map(int,input().split())

lst = []

max_num = 0

for i in range(n):
    nation,g,s,b = map(int,input().split())
    lst.append((nation,g,s,b,str(g)+str(s)+str(b)))
    max_num = max(max_num,nation)

rank = [0]*(max_num+1)

lst.sort(key=lambda x:(-x[1],-x[2],-x[3]))

for i in range(len(lst)):
    if not i:
        rank[lst[i][0]] = 1
    else:
        if lst[i][4] == lst[i-1][4]:
            rank[lst[i][0]] = rank[lst[i-1][0]]
        else:
            rank[lst[i][0]] = i+1
    if lst[i][0] == k:
        break

print(rank[k])