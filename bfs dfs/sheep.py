from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())

data = []

for i in range(n):
    data.append(list(input().strip()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visit = [[0]*m for i in range(n)]

def dfs(x,y):
    wolf = 0
    sheep = 0
    qu = deque()
    qu.append((x,y))
    while qu:
        x,y = qu.popleft()
        if visit[x][y] == 1:
            continue
        visit[x][y] = 1
        if data[x][y] == "#":
            continue
        if data[x][y] == "o":
            sheep += 1
        if data[x][y] == 'v':
            wolf += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                qu.append((nx,ny))
    return wolf,sheep

wolf_survive = 0
sheep_survive = 0

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and data[i][j] != "#":
            wolf,sheep = dfs(i,j)
            if wolf>=sheep:
                wolf_survive += wolf
            else:
                sheep_survive += sheep

print(sheep_survive,wolf_survive)