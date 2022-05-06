import heapq
import sys

input = sys.stdin.readline

n = int(input())

h = []

for i in range(n):
    command = int(input())
    if command:
        heapq.heappush(h,-command)
    else:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)