import heapq
import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    heap = []
    cost = 0
    for num in lst:
        heapq.heappush(heap,num)
    while(1):
        if len(heap)>1:
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            cost += val1+val2
            val3 = val1+val2
            heapq.heappush(heap,val3)
        else:
            break
    print(cost)