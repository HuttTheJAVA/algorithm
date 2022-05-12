from collections import deque
import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

matrix = []

for i in range(n):
    matrix.append(list(map(int,list(input().strip()))))

qu = deque()

change_matrix = [[INF]*n for i in range(n)]

qu.append((0,0,0))  # x , y , change_cnt

change_matrix[0][0] = 0

while(qu):
    x,y,cnt = qu.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if not matrix[nx][ny] and change_matrix[nx][ny]>cnt+1:
                change_matrix[nx][ny] = cnt + 1
                qu.append((nx,ny,cnt+1))
            elif matrix[nx][ny] and change_matrix[nx][ny]>cnt:
                change_matrix[nx][ny] = cnt
                qu.append((nx,ny,cnt))

print(change_matrix[n-1][n-1])