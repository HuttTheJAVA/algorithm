import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

r1,c1,r2,c2 = map(int,input().split())

INF = sys.maxsize

matrix = [[INF]*n for i in range(n)]

visited = [[False]*n for i in range(n)]

dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]

qu = deque()
qu.append((r1,c1,0))

visited[r1][c1] = True

while qu:
    r1,c1,cnt = qu.popleft()
    matrix[r1][c1] = cnt
    for i in range(6):
        nx = r1 + dx[i]
        ny = c1 + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                qu.append((nx,ny,cnt+1))

if matrix[r2][c2] != INF:
    print(matrix[r2][c2])
else:
    print(-1)