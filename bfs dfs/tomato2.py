from collections import deque
import sys

input = sys.stdin.readline

m,n,h = map(int,input().split())

data = []
box = []

xt = [0,1,0,-1,0,0]
yt = [1,0,-1,0,0,0]
zt = [0,0,0,0,-1,1]

for i in range(h):
    box = []
    for j in range(n):
        box.append(list(map(int,input().split())))
    data.append(box)

qu = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 1:
                qu.append((i,j,k))

while(qu):
    z,x,y = qu.popleft()
    for i in range(6):
        nz = z + zt[i]
        nx = x + xt[i]
        ny = y + yt[i]
        if nz<0 or nz>=h or nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if data[nz][nx][ny] == 0:
            data[nz][nx][ny] = data[z][x][y] + 1
            qu.append((nz,nx,ny))

max_day = 0


for i in range(h):
    result = "isZERO?"
    for lines in data[i]:
        max_day = max(max_day,max(lines))
        if lines.count(0) != 0:
            result = "notZERO"
            break
        
    if result == "notZERO":
        break

if result == "notZERO":
    print(-1)
else:
    print(max_day-1)