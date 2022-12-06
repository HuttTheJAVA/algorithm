from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

head_meat = []

for i in range(n):
    a,b = map(int,input().split())
    head_meat.append((a,b))

head_meat.sort(key=lambda x:(x[1],-x[0]))   # 가격이 저렴한 순으로 정렬 (가격이 같다면, 고기양이 더 많은것이 앞으로 오도록 정렬)

min_cost = sys.maxsize

sum_cost = 0

sum_meat = 0

recent_cost = -1

for meat in head_meat:
    sum_meat += meat[0]
    if meat[1] == recent_cost:
        sum_cost += meat[1]
    else:
        sum_cost = meat[1]
        recent_cost = meat[1]
    if sum_meat >= m:
        min_cost = min(min_cost,sum_cost)

if min_cost != sys.maxsize:
    print(min_cost)
else:
    print(-1)