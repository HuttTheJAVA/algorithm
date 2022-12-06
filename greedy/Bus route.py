import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

m = int(input())

bus_route = []

for i in range(m):
    a,b = map(int,input().split())
    bus_route.append((a,b,i+1))

bus_route.sort(key=lambda x:(x[0],x[1]))

dequeue = deque()

for i in range(m):
    start,end,number = bus_route[i]
    if start > end:
        end += n
    if not dequeue:
        dequeue.append((start,end,number))
        continue
    while(1): # 여기를 타면 아직 삽입 전.
        if dequeue and start == dequeue[-1][0] and end > dequeue[-1][1]:
            dequeue.pop()
        else:
            break
    if end >= n and dequeue:
        while(1):
            if dequeue and end%n >= dequeue[0][1]:
                dequeue.popleft()
            else:
                break
    if dequeue:
        if end > dequeue[-1][1]:
            dequeue.append((start,end,number))
    else: 
        dequeue.append((start,end,number))
left_routes = []

for left_route in dequeue:
    left_routes.append(left_route[2])
left_routes.sort()
print(*left_routes)