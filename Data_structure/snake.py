import sys
from collections import deque
input = sys.stdin.readline

turn = [[] for i in range(10001)]

n = int(input())

apple = int(input())

apple_matrix = [[0]*(n+1) for i in range(n+1)]

for i in range(apple):
    row,col = map(int,input().split())
    apple_matrix[row-1][col-1] = 1

t = int(input())

for i in range(t):
    x,c = input().split()
    turn[int(x)] = c

snake = deque([(0,0)])

dx = [0,1,0,-1]
dy = [1,0,-1,0]

sec = 0

dir = 0

x,y = 0,0
while(1):
    sec += 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if (nx,ny) in snake or not(0<=nx<n) or not(0<=ny<n):
        break
    if apple_matrix[nx][ny]:
        apple_matrix[nx][ny] = 0
        snake.append((nx,ny))
        
    else:
        snake.popleft()
        snake.append((nx,ny))
    if turn[sec]:
        if turn[sec] == 'D':
            dir += 1
            if dir>3:
                dir = 0
        elif turn[sec] == 'L':
            dir -= 1
            if dir<0:
                dir = 3
    x = nx
    y = ny
    
print(sec)