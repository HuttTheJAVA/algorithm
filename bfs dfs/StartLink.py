from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

F,S,G,U,D = map(int,input().split())

INF = sys.maxsize

floor = [INF]*(F+1)

floor[S] = 0

qu = deque()

qu.append((S,0))

while(qu):
    now,press = qu.popleft()
    if now - D > 0:
        if floor[now - D] > press+1:
            floor[now - D] = press + 1
            qu.append((now-D,press+1))
    if now + U <= F:
        if floor[now + U] > press+1:
            floor[now + U] = press + 1
            qu.append((now+U,press+1))
    
if floor[G] != INF:
    print(floor[G])
else:
    print("use the stairs")