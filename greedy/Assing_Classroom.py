from collections import deque
import sys
import heapq
input = sys.stdin.readline
import random as r
n = int(input())

class_time_lst = []

for i in range(n):
    start,end = map(int,input().split())
    class_time_lst.append((start,end))

class_time_lst.sort(key=lambda x:(-x[0],-x[1]))

heap = []

class_cnt = 1

first_class = class_time_lst.pop()

heapq.heappush(heap,first_class[1])

while(class_time_lst):
    next_class = class_time_lst.pop()
    tail = heapq.heappop(heap)
    if next_class[0] >= tail:
        heapq.heappush(heap,next_class[1])
    else:
        heapq.heappush(heap,tail)
        heapq.heappush(heap,next_class[1])
        class_cnt += 1

print(class_cnt)
