import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

data = []

qu = deque()

x,y,d = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(n):
    data.append(list(map(int,input().split())))

visited = [[False]*m for i in range(n)]

def direction(dir):
    dir -= 1
    if dir < 0:
        dir = 3
    return dir

def robot(x,y,d,cnt):

    qu.append((x,y,d))
    
    while(qu):
        x,y,d = qu.popleft()
        done = False
        visited[x][y] = True
        for i in range(4):
            idx = direction(d)
            d = idx
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and data[nx][ny] != 1:
                    qu.append((nx,ny,idx))
                    cnt += 1
                    done = True
                    break

        if not done:
            bx = x - dx[idx]
            by = y - dy[idx]
            if data[bx][by] != 1:
                qu.append((bx,by,idx))
            else:
                return cnt

print(robot(x,y,d,1))