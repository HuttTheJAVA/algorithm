import sys
import heapq
input = sys.stdin.readline

n = int(input())


heap1 = []
heap2 = []

for i in range(n):
    num = int(input())
    if not len(heap1):
        heapq.heappush(heap1,-num)
        print(num)
        continue
    if not len(heap2):
        heapq.heappush(heap1,-num)
        heapq.heappush(heap2,-heapq.heappop(heap1))
        print(-heap1[0])
        continue
    if len(heap1) == len(heap2):
        if num <= heap2[0]:
            heapq.heappush(heap1,-num)
        else:
            heapq.heappush(heap2,num)
            heapq.heappush(heap1,-heapq.heappop(heap2))
    elif len(heap1)>len(heap2):
        if num>=heap2[0]:
            heapq.heappush(heap2,num)
        elif num<heap2[0]:
            heapq.heappush(heap1,-num)
            heapq.heappush(heap2,-heapq.heappop(heap1))
    
    print(-heap1[0])