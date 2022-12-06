from collections import deque
import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort()

use_lst = []

bias = 0
time = 0
while(lst):
    for i in range(m-len(use_lst)):
        if lst:
            heapq.heappush(use_lst,lst.pop()+bias)
        else:
            break
    plus = heapq.heappop(use_lst)
    bias += plus - bias

while(use_lst):
    plus = heapq.heappop(use_lst)
    bias += plus - bias

print(bias)