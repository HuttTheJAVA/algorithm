import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

a,b = 1,1

dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

def dfs(data,visit,x,y):
    visit[x][y] = True
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and ny>=0 and nx<len(data) and ny<len(data[0]):
            if data[nx][ny] == 1 and visit[nx][ny] != True:
                dfs(data,visit,nx,ny)

while(1):
    island = 0
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    data = []
    visit = [[False]*a for i in range(b)]
    for i in range(b):
        data.append(list(map(int,input().split())))
    
    for i in range(b):
        for j in range(a):
            if data[i][j] == 1 and visit[i][j] != True:
                dfs(data,visit,i,j)
                island += 1

    print(island)