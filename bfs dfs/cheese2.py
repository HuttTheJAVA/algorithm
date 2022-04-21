from collections import deque
import sys

n,m = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    matrix.append(list(map(int,input().split())))

qu = deque()

cnt = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            cnt += 1

visited = [[0]*m for i in range(n)]

contact = [[0]*m for i in range(n)]
time = 0
while(cnt):
    qu.append((0,0))
    visited[0][0] = 1
    while(qu):
        x,y = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if matrix[nx][ny]:
                    contact[nx][ny] += 1
                    if contact[nx][ny] >= 2:
                        cnt -= 1
                        matrix[nx][ny] = 0
                        visited[nx][ny] = 1
                else:
                    qu.append((nx,ny))
                    visited[nx][ny] = 1
                

    visited = [[0]*m for i in range(n)]
    contact = [[0]*m for i in range(n)]
    time += 1

print(time)