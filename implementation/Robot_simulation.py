from collections import deque
import sys

input = sys.stdin.readline

b,a = map(int,input().split())

n,m = map(int,input().split())

matrix = [[0]*b for i in range(a)]

robot_x_y_dir = []

comands = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

dir_dct = {'E':0,'S':1,'W':2,'N':3}
stop = False
for i in range(n):
    y,x,dir = input().split()
    x = a - int(x)
    y = int(y)-1
    dir = dir_dct[dir]
    robot_x_y_dir.append([x,y,dir]) # index+1 is robot number
    matrix[x][y] = i+1
for i in range(m):
    robot_num,kind,times = input().split()
    robot_num = int(robot_num)
    times = int(times)
    comands.append((robot_num,kind,times))

for command in comands:
    if command[1] == 'L':
        dir = robot_x_y_dir[command[0]-1][2] - command[2]%4
        if dir<0:
            dir = dir+4
        robot_x_y_dir[command[0]-1][2] = dir
    elif command[1] == 'R':
        dir = robot_x_y_dir[command[0]-1][2] + command[2]%4
        if dir>3:
            dir = dir-4
        robot_x_y_dir[command[0]-1][2] = dir
    else:
        x,y = robot_x_y_dir[command[0]-1][0],robot_x_y_dir[command[0]-1][1]
        init_x = x
        init_y = y
        dir = robot_x_y_dir[command[0]-1][2]
        for i in range(command[2]):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<a and 0<=ny<b:
                if matrix[nx][ny] != 0:
                    print("Robot %d crashes into robot %d"%(command[0],matrix[nx][ny]))
                    stop = True
                    break
                else:
                    x = nx
                    y = ny
            else:
                print("Robot %d crashes into the wall"%(command[0]))
                stop = True
                break
        if stop:
            break
        else:
            matrix[init_x][init_y] = 0
            matrix[x][y] = command[0]
            robot_x_y_dir[command[0]-1][0] = x
            robot_x_y_dir[command[0]-1][1] = y

if not stop:
    print("OK")