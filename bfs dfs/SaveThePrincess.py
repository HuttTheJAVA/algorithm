import time
start = time.time()
from collections import deque
import sys
from itertools import combinations
input = sys.stdin.readline

n,m,t = map(int,input().split())

matrix = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            matrix[i][j] = sys.maxsize
        elif matrix[i][j] == 2:
            matrix[i][j] = 'Sword!'
        else:
            matrix[i][j] = 'The Wall'

visit = [[0]*m for i in range(n)]

qu = deque()
qu.append((0,0))
matrix[0][0] = 0

while(qu):
    x,y = qu.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and not visit[nx][ny] and matrix[nx][ny] != "The Wall":
            if matrix[nx][ny] == 'Sword!':
                if abs(nx - (n-1)) + abs(ny - (m-1)) + matrix[x][y] + 1 < matrix[-1][-1]:
                    matrix[-1][-1] = abs(nx - (n-1)) + abs(ny - (m-1)) + matrix[x][y] + 1 
            elif matrix[nx][ny] > matrix[x][y] + 1:
                matrix[nx][ny] = matrix[x][y] + 1
                qu.append((nx,ny))
                visit[nx][ny] = 1

if matrix[-1][-1] <= t:
    print(matrix[-1][-1])
else:
    print("Fail")