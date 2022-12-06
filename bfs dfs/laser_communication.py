from collections import deque
import sys

input = sys.stdin.readline

w,h = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(h):
    matrix.append(list(input().strip()))

bend_matrix = [[[sys.maxsize]*4 for i in range(w)] for i in range(h)]

start_x_y = []
end_x_y = []

for i in range(h):
    for j in range(w):
        if matrix[i][j] == 'C':
            if len(start_x_y):
                end_x_y.append((i,j))
            else:
                start_x_y.append((i,j))

for i in range(4):
    bend_matrix[start_x_y[0][0]][start_x_y[0][1]][i] = 0

qu = deque()

x = start_x_y[0][0]
y = start_x_y[0][1]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<=nx<h and 0<=ny<w and matrix[nx][ny] != '*':
        bend_matrix[nx][ny][i] = 0
        qu.append((nx,ny,i,0))

while(qu):
    x,y,prev_dir,bend_cnt = qu.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w:
            if matrix[nx][ny] != '*':
                if i != prev_dir:
                    if bend_matrix[nx][ny][i] > bend_cnt + 1:
                        bend_matrix[nx][ny][i] = bend_cnt + 1
                        if matrix[nx][ny] != 'C':
                            qu.append((nx,ny,i,bend_cnt+1))
                else:
                    if bend_matrix[nx][ny][i] > bend_cnt:
                        bend_matrix[nx][ny][i] = bend_cnt
                        if matrix[nx][ny] != 'C':
                            qu.append((nx,ny,prev_dir,bend_cnt))

res = sys.maxsize
for i in range(4):
    if bend_matrix[end_x_y[0][0]][end_x_y[0][1]][i] < res:
        res = bend_matrix[end_x_y[0][0]][end_x_y[0][1]][i]

print(res)