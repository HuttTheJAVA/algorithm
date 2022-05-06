import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    command = int(input())
    if command:
        heapq.heappush(heap,(abs(command),command))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)