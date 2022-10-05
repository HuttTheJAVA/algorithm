from collections import deque
import sys
import copy
input = sys.stdin.readline

r,c,k = map(int,input().split())

dx_dct = {1:[-1,0,1],2:[-1,0,1],3:[-1,-1,-1],4:[1,1,1]}
dy_dct = {1:[1,1,1],2:[-1,-1,-1],3:[-1,0,1],4:[-1,0,1]}

dx = [0,1,0,-1]
dy = [1,0,-1,0]

dir_range = {1:(-4,4,1,5),2:(-4,4,-5,-1),3:(-5,-1,-4,4),4:(1,5,-4,4)}

status_matrix = []

wall_dct = {} # 튜플 형식으로 추가해야됨. (x1,y1,x2,y2) 이런 식으로..

temperature_matrix = [[0]*c for i in range(r)]

for i in range(r):
    status_matrix.append(list(map(int,input().split())))

wall_cnt = int(input())

for i in range(wall_cnt):
    x,y,t = map(int,input().split())
    x = x - 1
    y = y - 1
    if t:
        if 0<=y+1<c:
            wall_dct[(x,y,x,y+1)] = 1
            wall_dct[(x,y+1,x,y)] = 1
    else:
        if 0<=x-1<r:
            wall_dct[(x,y,x-1,y)] = 1
            wall_dct[(x-1,y,x,y)] = 1

heater_x_y = []

check_cell = []

for i in range(r):
    for j in range(c):
        if 0<status_matrix[i][j]<5:
            heater_x_y.append((i,j,status_matrix[i][j]))
        elif status_matrix[i][j] == 5:
            check_cell.append((i,j))

chocolate = 0

heater_x_y = heater_x_y[::-1]  ## 이거 제출시 지울것.

while(1):
    visit_matrix = [[0]*c for i in range(r)]
    plus_matrix = [[0]*c for i in range(r)]
    plus_spread_temperature_matrix = [[0]*c for i in range(r)]
    minus_spread_temperature_matrix = [[0]*c for i in range(r)]

    for x_y_dir in heater_x_y:
        init_x = x_y_dir[0]
        init_y = x_y_dir[1]
        direction = x_y_dir[2]
        L_x = dir_range[direction][0]
        R_x = dir_range[direction][1]
        L_y = dir_range[direction][2]
        R_y = dir_range[direction][3]
        x = init_x + dx_dct[direction][1]
        y = init_y + dy_dct[direction][1]
        plus = 5
        if 0<=x<r and 0<=y<c:
            qu = deque()
            qu.append((x,y,plus))
            plus_matrix[x][y] += plus
            visit_matrix[x][y] += 1
        while(qu):
            x,y,plus = qu.popleft()
            for i in range(3):
                nx = x + dx_dct[direction][i]
                ny = y + dy_dct[direction][i]
                if 0<=nx<r and 0<=ny<c and visit_matrix[nx][ny] <= 0 and init_x + L_x <= nx <= init_x + R_x and init_y + L_y <= ny <= init_y + R_y:
                    if i == 1:
                        if (x,y,nx,ny) not in wall_dct:
                            visit_matrix[nx][ny] += 1
                            plus_matrix[nx][ny] += plus - 1
                            qu.append((nx,ny,plus-1))
                            continue

                    if direction  > 2:
                        pivot_x = x
                        pivot_y = ny
                    else:
                        pivot_x = nx
                        pivot_y = y

                    if (nx,ny,pivot_x,pivot_y) not in wall_dct and (x,y,pivot_x,pivot_y) not in wall_dct:
                        visit_matrix[nx][ny] += 1
                        plus_matrix[nx][ny] += plus - 1
                        qu.append((nx,ny,plus-1))
        visit_matrix = [[0]*c for i in range(r)]

    for i in range(r):
        for j in range(c):
            temperature_matrix[i][j] += plus_matrix[i][j]

    for i in range(r):
        for j in range(c):
            for dir in range(4):
                adj_x = i + dx[dir]
                adj_y = j + dy[dir]
                if 0<=adj_x<r and 0<=adj_y<c and temperature_matrix[i][j] > temperature_matrix[adj_x][adj_y] and (i,j,adj_x,adj_y) not in wall_dct:
                    gap = temperature_matrix[i][j] - temperature_matrix[adj_x][adj_y]
                    minus_spread_temperature_matrix[i][j] += int(gap/4)
                    plus_spread_temperature_matrix[adj_x][adj_y] += int(gap/4)
    
    for i in range(r):
        for j in range(c):
            temperature_matrix[i][j] -= minus_spread_temperature_matrix[i][j]
            temperature_matrix[i][j] += plus_spread_temperature_matrix[i][j]
    
    out_x = 0
    out_y = 0

    if temperature_matrix[out_x][out_y]:
        temperature_matrix[out_x][out_y] -= 1

    out_dir = 0

    next_out_x = None 
    next_out_y = None
    change = 0
    while(change < 4):
        next_out_x = out_x + dx[out_dir]
        next_out_y = out_y + dy[out_dir]
        if not next_out_x and not next_out_y:
            break
        if 0<=next_out_x<r and 0<=next_out_y<c:
            if temperature_matrix[next_out_x][next_out_y]:
                temperature_matrix[next_out_x][next_out_y] -= 1
            out_x = next_out_x
            out_y = next_out_y
        else:
            out_dir += 1
            change += 1
    
    res = True

    chocolate += 1

    for x_y in check_cell:
        if temperature_matrix[x_y[0]][x_y[1]] < k:
            res = False
            break
    
    if chocolate > 100 or res:
        break

print(chocolate)