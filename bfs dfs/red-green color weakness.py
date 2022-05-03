from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

data = []

def dfs(x,y,color):
    qu = deque()
    qu.append((x,y))
    while qu:
        x,y = qu.popleft()
        if visit[x][y] == True or data[x][y] != color:
            continue
        visit[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                qu.append((nx,ny))

def dfs_i(x,y,color):
    qu = deque()
    qu.append((x,y))
    while qu:
        x,y = qu.popleft()
        if visit_i[x][y] == True:
            continue
        if data[x][y] == "B" and color == "R" or data[x][y] == "B" and color == "G" or data[x][y] == 'G' and color == "B" or data[x][y] == 'R' and color =="B":
            continue

        visit_i[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                qu.append((nx,ny))

for i in range(n):
    data.append(list(input()))

visit = [[False]*n for i in range(n)]
visit_i = [[False]*n for i in range(n)]
count = 0
count_i = 0
max_draw = 0

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            dfs(i,j,data[i][j])
            count += 1
        if visit_i[i][j] == False:
            dfs_i(i,j,data[i][j])
            count_i += 1

print(count,count_i)