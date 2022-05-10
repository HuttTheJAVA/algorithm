import sys
from collections import deque

input = sys.stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]

n,k = map(int,input().split())

data = []

for i in range(n):
    data.append(list(map(int,input().split())))

depth,ex,wy = map(int,input().split())

order = []

for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            order.append((data[i][j],i,j,0))

order.sort()

order = deque(order)

def bfs(depth):

    while order:
        virus,x,y,time = order.popleft()
        if time == depth:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = virus
                order.append((virus,nx,ny,time+1))


bfs(depth)
print(data[ex-1][wy-1])