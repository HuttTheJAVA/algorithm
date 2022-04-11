import sys
from collections import deque
input = sys.stdin.readline

v,e = map(int,input().split())

INF = (1e9)

matrix = [[INF]*v for i in range(v)]

for i in range(e):
    a,b,c = map(int,input().split())
    matrix[a-1][b-1] = c

for k in range(v):
    for i in range(v):
        for j in range(v):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

min_val = INF

for i in range(v):
    min_val = min(matrix[i][i],min_val)

if min_val == INF:
    print(-1)
else:
    print(min_val)