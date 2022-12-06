from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

hx,hy = map(int,input().split())
ex,ey = map(int,input().split())

hx -= 1
hy -= 1
ex -= 1
ey -= 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

matrix = []

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

dp_matrix = [[[sys.maxsize,sys.maxsize]for i in range(m)] for i in range(n)]

dp_matrix[hx][hy][0] = 0

qu = deque()
qu.append((hx,hy,0))

while(qu):
    x,y,use = qu.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if matrix[nx][ny]:
                if not use:
                    if dp_matrix[nx][ny][1] > dp_matrix[x][y][use] + 1:
                        dp_matrix[nx][ny][1] = dp_matrix[x][y][use] + 1
                        qu.append((nx,ny,1))
            else:
                if not use:
                    if dp_matrix[nx][ny][0] > dp_matrix[x][y][use] + 1:
                        dp_matrix[nx][ny][0] = dp_matrix[x][y][use] + 1
                        qu.append((nx,ny,use))
                else:
                    if dp_matrix[nx][ny][1] > dp_matrix[x][y][use] + 1:
                        dp_matrix[nx][ny][1] = dp_matrix[x][y][use] + 1
                        qu.append((nx,ny,use))

if min(dp_matrix[ex][ey][0],dp_matrix[ex][ey][1]) != sys.maxsize:
    print(min(dp_matrix[ex][ey][0],dp_matrix[ex][ey][1]))
else:
    print(-1)