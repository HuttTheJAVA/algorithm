import sys

input = sys.stdin.readline

n = int(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

visit = [[False]*(n) for i in range(n)]

data = []

for i in range(n):
    data.append(list(map(int,input().strip())))

def dfs(x,y):
    global pivot
    pivot += 1
    visit[x][y] = True

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if visit[nx][ny] == False and data[nx][ny] == 1:
            dfs(nx,ny)

result = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and visit[i][j] == False:
            pivot = 0
            dfs(i,j)
            result.append(pivot)

print(len(result))
result.sort()
for i in result:
    print(i)