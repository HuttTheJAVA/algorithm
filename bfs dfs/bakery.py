import sys
input = sys.stdin.readline
n,m = map(int,input().split())
matrix = []

for i in range(n):
    matrix.append(list(input().strip()))

for i in range(n):
    matrix[i][0] = (i+1)

dx = [-1,0,1]
dy = [1,1,1]


def dfs(x,y,num):
    global reached,dx,dy,n,m,matrix
    if y == m-1:
        reached = True
        return
    for i in range(3):
        if reached:
            return
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and matrix[nx][ny] == '.':
            matrix[nx][ny] = num
            dfs(nx,ny,num)

for i in range(n):
    reached = False
    dfs(i,0,i+1)

cnt = 0

for i in range(n):
    if matrix[i][-1] != '.' and matrix[i][-1] != 'x':
        cnt += 1

print(cnt)