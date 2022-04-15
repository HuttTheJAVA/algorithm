import collections
import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

data = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    data.append(list(map(int,input().strip())))

visit = [[False]*m for _ in range(n)]

qu = deque()

qu.append((0,0))
visit[0][0] = True

while qu:
    x,y = qu.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if data[nx][ny] != 0 and visit[nx][ny] == False:
            data[nx][ny] = data[x][y]+1
            visit[nx][ny] = True
            qu.append((nx,ny))

print(data[n-1][m-1])