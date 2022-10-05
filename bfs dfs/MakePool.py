from collections import deque
import heapq
from re import A
import sys
import random as r

input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    matrix.append(list(map(int,list(input().strip()))))

aqua = 0

bigger_height_x_y = []

for i in range(n):
    for j in range(m):
        bigger_height_x_y.append((i,j,matrix[i][j]))

bigger_height_x_y.sort(key=lambda x:(-x[2],x[0],x[1]))

for now in bigger_height_x_y:
        visit = [[0]*m for i in range(n)]
        standard_h = now[2]
        qu = deque()
        qu.append((now[0],now[1]))
        visit[i][j] = 1
        set_of_i_j = [(now[0],now[1])]
        overflow = False
        min_wall_h = None
        while(qu):
            x,y = qu.popleft()
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0<=nx<n and 0<=ny<m:
                    if matrix[nx][ny] <= standard_h:
                        if not visit[nx][ny]:
                            set_of_i_j.append((nx,ny))
                            qu.append((nx,ny))
                            visit[nx][ny] = 1
                    else:
                        if min_wall_h == None:
                            min_wall_h = matrix[nx][ny]
                        else:
                            min_wall_h = min(min_wall_h,matrix[nx][ny])
                else:
                    overflow = True
                    break
            if overflow:
                break
        if not overflow:
            for x_y in set_of_i_j:
                aqua += min_wall_h - matrix[x_y[0]][x_y[1]]
                matrix[x_y[0]][x_y[1]] = min_wall_h

print(aqua)