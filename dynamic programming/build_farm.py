from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

matrix = []
for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

dx = [-1,-1,0] #↖ ↑ ←
dy = [-1,0,-1]

dp_matrix = [[0]*m for i in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j]:
            dp_matrix[i][j] = -1

for i in range(n):
    for j in range(m):
        if not matrix[i][j]:
            val = sys.maxsize
            for idx in range(3):
                nx = i + dx[idx]
                ny = j + dy[idx]
                if 0<=nx<n and 0<=ny<m:
                    val = min(val,dp_matrix[nx][ny])
                else:
                    break
            if val == sys.maxsize:
                val = -1
            dp_matrix[i][j] = val+1

max_leng = -1

for i in range(n):
    for j in range(m):
        max_leng = max(max_leng,dp_matrix[i][j])

print(max_leng+1)