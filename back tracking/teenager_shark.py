import sys
import copy
input = sys.stdin.readline

matrix = [[]for i in range(4)]

dir_matrix = [[]for i in range(4)]

for i in range(4):
    line = list(map(int,input().split()))
    for j in range(0,len(line),2):
        matrix[i].append(line[j])
        dir_matrix[i].append(line[j+1])

sx = 0
sy = 0

location_dct = {}

dx = ["No",-1,-1,0,1,1,1,0,-1]
dy = ["No",0,-1,-1,-1,0,1,1,1]

for i in range(4):
    for j in range(4):
        location_dct[matrix[i][j]] = [i,j]

max_kill = 0
if matrix[0][0] != -1:     # -1이면 그 칸에 생선이 없는것.
    max_kill += matrix[0][0]
    location_dct[matrix[0][0]] = [-1,-1]    
    matrix[0][0] = 88 # 88 == shark
    sx = 0
    sy = 0

def ccw(dir):     #dir는 반시계 회전한 값을 넣어줘야 된다.
    if dir > 8:
        dir = 1
    return dir

def move_fish(local_location_dct,local_matrix,local_dir_matrix):
    global dx,dy
    for i in range(1,17):
        if local_location_dct[i] != [-1,-1]:
            x = local_location_dct[i][0]
            y = local_location_dct[i][1]
            dir = local_dir_matrix[x][y]
            for _ in range(1,8):
                nx = x + dx[dir]
                ny = y + dy[dir]
                if 0<=nx<4 and 0<=ny<4 and local_matrix[nx][ny] != 88:
                    tmp = local_matrix[nx][ny]
                    tmp_dir = local_dir_matrix[nx][ny]
                    local_matrix[nx][ny] = local_matrix[x][y]
                    local_matrix[x][y] = tmp
                    local_dir_matrix[nx][ny] = dir
                    local_location_dct[local_matrix[nx][ny]] = [nx,ny]
                    if tmp != -1:
                        local_dir_matrix[x][y] = tmp_dir
                        local_location_dct[tmp] = [x,y]

                    break
                else:
                    dir = ccw(dir+1)
            
    return local_matrix,local_dir_matrix,local_location_dct

def shark_move(x,y,kill,local_matrix,local_location_dct,local_dir_matrix):
    global max_kill

    local_matrix,local_dir_matrix,local_location_dct = move_fish(local_location_dct,local_matrix,local_dir_matrix)
    init_matrix = copy.deepcopy(local_matrix)
    init_dir_matrix = copy.deepcopy(local_dir_matrix)
    init_location_matrix = copy.deepcopy(local_location_dct)

    weight = 1
    while(1):
        nx = x + weight*dx[local_dir_matrix[x][y]]
        ny = y + weight*dy[local_dir_matrix[x][y]]
        if 0<=nx<4 and 0<=ny<4:
            if local_matrix[nx][ny] != -1:
                fish_number = local_matrix[nx][ny]
                local_matrix[x][y] = -1
                local_location_dct[fish_number] = [-1,-1]
                local_matrix[nx][ny] = 88
                shark_move(nx,ny,kill+fish_number,local_matrix,local_location_dct,local_dir_matrix)
                local_matrix = copy.deepcopy(init_matrix)
                local_dir_matrix = copy.deepcopy(init_dir_matrix)
                local_location_dct = copy.deepcopy(init_location_matrix)
        else:
            max_kill = max(max_kill,kill)
            return
        weight += 1
    


shark_move(0,0,max_kill,matrix,location_dct,dir_matrix)

print(max_kill)