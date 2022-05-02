import collections
import sys
from collections import deque


input = sys.stdin.readline


T = int(input())

dx = [-1,1,2,2,1,-1,-2,-2]
dy = [2,2,1,-1,-2,-2,-1,1]


for i in range(T):
    I = int(input())
    data = [[0]*I for i in range(I)]
    ex,wy = map(int,input().split())
    to_x,to_y = map(int,input().split())
    data[ex][wy] = 0
    qu = deque()
    qu.append((ex,wy))
    while(qu):
        x,y = qu.popleft()
        if x == to_x and y == to_y:
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=I or ny<0 or ny>=I:
                continue
            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                qu.append((nx,ny))

    print(data[to_x][to_y])