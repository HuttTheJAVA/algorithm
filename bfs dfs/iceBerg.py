from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

matrix = []

for i in range(n):
    line = list(map(int,input().split()))
    matrix.append(line)

ice_cnt = 0

start_point = (None,None)

is_seperate = False

year = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            ice_cnt += 1
            if start_point == (None,None):
                start_point = (i,j)

while(not is_seperate and ice_cnt):
    save_melting_amount = [[0]*m for i in range(n)]
    visit = [[0]*m for i in range(n)]
    change = False
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                for idx in range(len(dx)):
                    nx = i + dx[idx]
                    ny = j + dy[idx]
                    if 0<=nx<n and 0<=ny<m and not matrix[nx][ny]:
                        save_melting_amount[i][j] += 1
                
    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                matrix[i][j] -= save_melting_amount[i][j]
                if matrix[i][j]<=0:
                    matrix[i][j] = 0
                    ice_cnt -= 1
                else:
                    if not change:
                        start_point = (i,j)
                        change = True
    
    if ice_cnt:

        bfs_ice_cnt = 0
        qu = deque()
        qu.append(start_point)
        visit[start_point[0]][start_point[1]] = 1
        bfs_ice_cnt += 1
        while(qu):
            x,y = qu.popleft()
            for idx in range(len(dx)):
                nx = x + dx[idx]
                ny = y + dy[idx]
                if 0<=nx<n and 0<=ny<m and matrix[nx][ny] and not visit[nx][ny]:
                    qu.append((nx,ny))
                    visit[nx][ny] = 1
                    bfs_ice_cnt += 1
        
        if bfs_ice_cnt != ice_cnt:
            is_seperate = True
    year += 1


if is_seperate:
    print(year)
else:
    print(0)