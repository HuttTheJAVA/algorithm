from collections import deque
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = map(int,input().split())

dx = [0,1,0,-1]
dy = [1,0,-1,0]

data = []

for i in range(n):
    data.append(list(map(int,input().strip())))

result = 0
def dfs(x,y):
    global result
    qu = deque()
    qu.append((x,y))
    while qu:
        x,y = qu.popleft()
        if data[x][y] == 1:
            continue
        data[x][y] = 1
        if x == n-1:
            result = 1
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                qu.append((nx,ny))

for i in range(m):
    if data[0][i] != 1:
        dfs(0,i)
        if result == 1:
            break

if result:
    print('YES')
else:
    print("NO")