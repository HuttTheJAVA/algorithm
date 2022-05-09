from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())

dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,-1,1]

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

def dfs(x,y):
    qu = deque()
    qu.append((x,y))
    while qu:
        x,y = qu.popleft()
        if data[x][y] == 0 or data[x][y] == 2:
            continue
        data[x][y] = 2
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                qu.append((nx,ny))

alp = 0

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            dfs(i,j)
            alp += 1
    
print(alp)