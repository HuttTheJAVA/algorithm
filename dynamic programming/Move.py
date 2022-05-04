import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

dx = [-1,-1,0]
dy = [0,-1,-1]

data = []
for i in range(n):
    data.append(list(map(int,input().split())))

candy = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        max_candy = 0
        for v in range(3):
            nx = i+dx[v]
            ny = j+dy[v]
            if 0<=nx<n and 0<=ny<m:
                max_candy = max(max_candy,candy[nx][ny])
        candy[i][j] = max_candy+data[i][j]


print(candy[n-1][m-1])