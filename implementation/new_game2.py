from collections import deque
import sys

n,k = map(int,input().split())

matrix = []

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for i in range(n):
    lst = list(map(int,input().split()))
    matrix.append(lst)

curr_location = [0]*k

stack_matrix = [['']*n for i in range(n)]

max_stack = 1

turn = 0

for i in range(k):
    x,y,dir = map(int,input().split())
    curr_location[i] = [x-1,y-1,dir-1,0]
    stack_matrix[x-1][y-1] = str(i)

def change_dir(dir):
    if not dir:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    elif dir == 3:
        return 2

def move_horse(nx,ny,x,y,floor,new_floor,is_red):
    global stack_matrix,curr_location,max_stack

    if not is_red:
        for member in range(len(stack_matrix[x][y][floor:])):
            number = int(stack_matrix[x][y][floor+member])
            curr_location[number] = [nx,ny,curr_location[number][2],len(new_floor)+member]
        stack_matrix[nx][ny] = stack_matrix[nx][ny] + stack_matrix[x][y][floor:]
    else:
        for member in range(len(stack_matrix[x][y][floor:])):
            number = int(stack_matrix[x][y][floor+member])
            curr_location[number] = [nx,ny,curr_location[number][2],len(new_floor)+((len(stack_matrix[x][y][floor:])-1)-member)]
        stack_matrix[nx][ny] = stack_matrix[nx][ny] + stack_matrix[x][y][floor:][::-1]
    max_stack = max(max_stack,len(stack_matrix[nx][ny]))
    stack_matrix[x][y] = stack_matrix[x][y][:floor]

def operation_white_or_red(nx,ny,x,y,floor,new_floor):
    global matrix
    if not matrix[nx][ny]:# 흰
        move_horse(nx,ny,x,y,floor,new_floor,0)
    else:# 빨
        move_horse(nx,ny,x,y,floor,new_floor,1)

while(max_stack<4 and turn<=1000):
    turn += 1
    for i in range(k):
        x = curr_location[i][0]
        y = curr_location[i][1]
        dir = curr_location[i][2]
        floor = curr_location[i][3]

        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0<=nx<n and 0<=ny<n:
            if matrix[nx][ny] != 2:
                new_floor = stack_matrix[nx][ny]
                operation_white_or_red(nx,ny,x,y,floor,new_floor)

            else:
                curr_location[i][2] = change_dir(curr_location[i][2])
                dir = curr_location[i][2]
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0<=nx<n and 0<=ny<n and matrix[nx][ny] != 2:
                    new_floor = stack_matrix[nx][ny]
                    operation_white_or_red(nx,ny,x,y,floor,new_floor)
        else:
            curr_location[i][2] = change_dir(curr_location[i][2])
            dir = curr_location[i][2]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0<=nx<n and 0<=ny<n and matrix[nx][ny] != 2:
                new_floor = stack_matrix[nx][ny]
                operation_white_or_red(nx,ny,x,y,floor,new_floor)

        if max_stack>=4:
            break

if turn <= 1000:
    print(turn)
else:
    print(-1)