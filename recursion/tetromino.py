import sys
import copy
import random as r 
input =sys.stdin.readline

n,m = map(int,input().split())

matrix = []

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

max_value = 0

for line in matrix:
    max_value = max(max_value,max(line))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visit = [[0]*m for i in range(n)]

max_score = 0

def dfs(x,y,visit,count,score): # 방문 매트릭스와 현재 만든 테트로미노 칸 수 와 현재까지 점수
    global max_score,n,m,dx,dy,max_value
    if (4-count)*max_value+score<=max_score:
        return
    if count == 4:
        max_score = max(max_score,score)
        return
    
    for dir in range(3):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
            visit[nx][ny] = 1
            dfs(nx,ny,visit,count + 1,score + matrix[nx][ny])
            visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            visit[i][j] = 1
            dfs(i,j,visit,1,matrix[i][j])
            visit[i][j] = 0

for i in range(n):
    for j in range(m):
        for idx in range(4):
            score = matrix[i][j]
            can = True
            for dir in range(4):
                if idx != dir:
                    ni = i + dx[dir]
                    nj = j + dy[dir]
                    if 0<=ni<n and 0<=nj<m:
                        score += matrix[ni][nj]
                    else:
                        can = False
            if can:
                max_score = max(max_score,score)

print(max_score)