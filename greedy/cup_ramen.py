import heapq
import sys
import copy
input = sys.stdin.readline

n = int(input())

lst = []

for i in range(n):
    deadline,cupramen = map(int,input().split())
    lst.append((deadline,cupramen))

lst.sort(key=lambda x:(x[0],x[1]))

heap = []

for i in range(len(lst)):
    if lst[i][0] > len(heap):
        heapq.heappush(heap,(lst[i][1],lst[i][0]))
    else:
        ramen,dead = heapq.heappop(heap)
        if ramen < lst[i][1]:
            ramen = lst[i][1]
            dead = lst[i][0]
        heapq.heappush(heap,(ramen,dead))

ramen_cnt = 0

for i in range(len(heap)):
    ramen_cnt += heap[i][0]

print(ramen_cnt)