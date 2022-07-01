import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
  a,b = map(int,input().split())
  lst.append((a,b))

lst.sort(key=lambda x:(x[0],x[1]))

end = None

cnt = 0

for i in range(n):
  if end != None and lst[i][0] >= end:
    cnt += 1
    end = lst[i][1]
  if end == None:
    end = lst[i][1]
    cnt = 1
  elif lst[i][1] <= end:
    end = lst[i][1]

print(cnt)