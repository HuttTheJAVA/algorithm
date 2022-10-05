from collections import deque
import sys
import copy
import heapq
input = sys.stdin.readline

n = int(input())

matrix = []

section_matrix = [[0]*n for i in range(n)]

for i in range(n):
    matrix.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

group_num = 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] and not section_matrix[i][j]:
            section_matrix[i][j] = group_num
            qu = deque()
            qu.append((i,j))
            while(qu):
                x,y = qu.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0<=nx<n and 0<=ny<n and matrix[nx][ny] and not section_matrix[nx][ny]:
                        section_matrix[nx][ny] = group_num
                        qu.append((nx,ny))
            group_num += 1

bridge = 100_000_000_000

for i in range(n):
    for j in range(n):
        if section_matrix[i][j]:
            dist_matrix = [[sys.maxsize]*n for i in range(n)]
            qu = deque()
            qu.append((i,j,section_matrix[i][j]))
            dist_matrix[i][j] = 0
            while(qu):
                x,y,section_num = qu.popleft()
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0<=nx<n and 0<=ny<n:
                        if not matrix[nx][ny]:
                            if dist_matrix[nx][ny] > dist_matrix[x][y] + 1:
                                dist_matrix[nx][ny] = dist_matrix[x][y] + 1
                                qu.append((nx,ny,section_num))
                        elif section_matrix[nx][ny] != section_num:
                            bridge = min(bridge,dist_matrix[x][y])

print(bridge)