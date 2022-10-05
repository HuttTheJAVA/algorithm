from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(int,input().split())))

s_x = n//2
s_y = n//2

spread_dir_x = {0:[-1,1,-2,2,0,-1,1,-1,1,0],1:[-1,-1,0,0,2,0,0,1,1,1],2:[-1,1,-2,2,0,-1,1,-1,1,0],3:[1,1,0,0,-2,0,0,-1,-1,-1]}
spread_dir_y = {0:[1,1,0,0,-2,0,0,-1,-1,-1],1:[1,-1,2,-2,0,1,-1,1,-1,0],2:[-1,-1,0,0,2,0,0,1,1,1],3:[1,-1,-2,2,0,1,-1,1,-1,0]}
out_spread = 0
def change_dir(dir):
    dir += 1
    if dir == 4:
        dir = 0
    return dir

def spread_sand(x,y,sand,dir):
    global spread_dir_x
    global out_spread
    global spread_dir_y
    global matrix
    tmp = sand
    spread_per = [0.01,0.01,0.02,0.02,0.05,0.07,0.07,0.1,0.1,'a']
    for i in range(9):
        nx = x + spread_dir_x[dir][i]
        ny = y + spread_dir_y[dir][i]
        move_sand = int(spread_per[i]*sand)
        if 0<=nx<n and 0<=ny<n:
            matrix[nx][ny] += move_sand
        else:
            out_spread += move_sand
        tmp -= move_sand
    nx = x + spread_dir_x[dir][9]
    ny = y + spread_dir_y[dir][9]
    if 0<=nx<n and 0<=ny<n:
        matrix[nx][ny] += tmp
    else:
        out_spread += tmp
    matrix[x][y] = 0

dx = [0,1,0,-1]
dy = [-1,0,1,0]
dir = 0
move = 1
while(not (s_x == 0 and s_y == 0)):
    for _ in range(2):
        for time in range(move):
            nx = s_x + dx[dir]
            ny = s_y + dy[dir]
            if 0<=nx<n and 0<=ny<n:
                spread_sand(nx,ny,matrix[nx][ny],dir)
                s_x = nx
                s_y = ny
            if not s_x and not s_y:
                break
        if not s_x and not s_y:
            break
        dir = change_dir(dir)
    move += 1

print(out_spread)