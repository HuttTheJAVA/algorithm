from collections import deque
import sys
import random as r
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]
max_death = 0
def Baaaaaaaaaduk2(start_i,cnt):
    global n,m,matrix,max_death
    if cnt == 2:
        visit = [[0]*m for i in range(n)]
        local_death = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 2 and not visit[i][j]:
                    group_cnt = 1
                    Misaeng = False
                    qu = deque()
                    qu.append((i,j))
                    visit[i][j] = 1
                    while(qu):
                        x,y = qu.popleft()
                        for idx in range(4):
                            nx = x + dx[idx]
                            ny = y + dy[idx]
                            if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and matrix[nx][ny] != 1:
                                if matrix[nx][ny] == 0:
                                    Misaeng = True
                                else:
                                    group_cnt += 1
                                qu.append((nx,ny))
                                visit[nx][ny] = 1
                    if not Misaeng:
                        local_death += group_cnt
        max_death = max(max_death,local_death)
        return
    for i in range(start_i,n):
        for j in range(m):
            if not matrix[i][j]:
                matrix[i][j] = 1
                Baaaaaaaaaduk2(i,cnt+1)
                matrix[i][j] = 0

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            matrix[i][j] = 1
            Baaaaaaaaaduk2(i,1)
            matrix[i][j] = 0

print(max_death)