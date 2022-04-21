from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

mep = []

for i in range(n):
    mep.append(list(input().strip()))

INF = sys.maxsize

dx = [0,1,0,-1]
dy = [1,0,-1,0]

max_dist = 0

def check_dist(x,y):
    global max_dist
    dist_map = [[INF]*m for i in range(n)]
    dist_map[x][y] = 0
    qu = deque()
    qu.append((x,y))
    path = [(x,y)]
    while qu:
        x,y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if mep[nx][ny] == 'L' and dist_map[nx][ny]>dist_map[x][y]+1:
                    dist_map[nx][ny] = dist_map[x][y]+1
                    qu.append((nx,ny))
                    path.append((nx,ny))
    for x,y in path:
        if dist_map[x][y]>max_dist:
            max_dist = dist_map[x][y]
                

for i in range(n):
    for j in range(m):
        if mep[i][j] == 'L':
            check_dist(i,j)

print(max_dist)