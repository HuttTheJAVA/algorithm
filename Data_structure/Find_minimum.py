import sys
from collections import deque
import heapq
input = sys.stdin.readline

n,l = map(int,input().split())

lst = list(map(int,input().split()))

heap = []

for i in range(len(lst)):
    heapq.heappush(heap,(lst[i],i))
    while(heap):
        if heap[0][1] > i-l:
            print(heap[0][0],end=" ")
            break
        else:
            heapq.heappop(heap)