import heapq
import sys

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    num = int(input())
    heapq.heappush(heap,num)

cost = 0

while(1):
    if len(heap)>1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        cost += num1 + num2 
        heapq.heappush(heap,num1+num2)
    else:
        break
print(cost)