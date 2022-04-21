from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

ps = int(input())

group = [[] for i in range(ps+1)]

visit = [0]*(ps+1)

p1,p2 = map(int,input().split())

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    group[a].append(b)
    group[b].append(a)

def bfs(person,depth,finding):
    qu = deque()
    qu.append((person,depth))
    while qu:
        person,depth = qu.popleft()
        if visit[person] == 1:
            continue
        visit[person] = 1
        if person == finding:
            return depth
        for i in group[person]:
            qu.append((i,depth+1))

result = bfs(p1,0,p2)

if result:
    print(result)
else:
    print(-1)